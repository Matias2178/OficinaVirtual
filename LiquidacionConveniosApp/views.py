from django.shortcuts import render, HttpResponse, redirect
from LiquidacionConveniosApp.models import Deuda, Convenio
from LiquidacionConveniosApp.forms import  DeudaForm
from OficinaVirtualApp.models import Suministro
from PagosApp.models import Pagos, Cupon_Pago
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from AvisosAlertasApp.funciones import CargarAviso

# Create your views here.
TNA_Cuota = {1: 0.0, 2: 6.0, 3: 12.0, 6: 15.0, 8: 20.0, 12: 18.0, 24: 30.0, 36 : 40.0}
suministro_activo = 0
valor_cuota = 0.0
total_convenio = 0.0

def liquidacionDeuda(request):
    usuario = request.user.id
    suministros = Suministro.objects.values_list("id", "suministro").filter(cliente = usuario) 
    formulario_deuda = DeudaForm(request.POST)
    formulario_deuda.fields['suministro'].choices = suministros
      
    info={
        "form": formulario_deuda,
    }
    suministro = formulario_deuda.data.get("suministro") 
    
    #para filtrar los vencimintos de los proximos dos meses
    fecha = date.today() + relativedelta(months = 3)
    fecha.replace(day=1)
    
    deudas = Deuda.objects.filter(suministro = suministro, estado__contains = 'PEN', vencimiento__lt = fecha)
    deudas2 = Deuda.objects.filter(suministro = suministro, estado__contains = 'CPP')
    print(deudas)
    liquidacion = {
        "form": formulario_deuda,
        "deudas": deudas,
        "deudas2": deudas2,
        "suministro":suministro,
    }
    if request.method=='POST' and 'sel_suministro' in request.POST: 

        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",liquidacion)
    
    elif request.method=='POST' and 'liquidar' in request.POST:
        datos = request.POST.getlist('apagar')
        if len(datos):
            #calculo el total de los importes
            importe = 0.0
            for dato in datos:
                item = Deuda.objects.values("importe").filter(id = dato)
                importe = importe + item[0]['importe']
            
            vencimiento = datetime.now() + timedelta(weeks=1)
            
            if vencimiento.isoweekday() == 6 : 
                vencimiento = vencimiento + timedelta(days=2)
                
            elif vencimiento.isoweekday() == 7:
                vencimiento = vencimiento + timedelta(days=1)
            actual = request.user
            
            pago = Cupon_Pago(
                cliente = actual,
                fecha_vencimiento = vencimiento,
                importe = importe,
                medio_pago = "SNP",
                estado = "PEN"                
            )
            pago.save()
            id_pago = Cupon_Pago.objects.last()
            print("Cupon de pago:", id_pago)
            for dato in datos:
                Deuda.objects.filter(id = dato).update(cupon_pago = id_pago, estado = 'PPA')
                
        cupones = Cupon_Pago.objects.filter(cliente = usuario)
        lista = {
            "cupones" : cupones,
        }
        return render(request, "PagosApp/cuponPago.html", lista)        
    
#**************************************************************************
# Aca comineza el convenio de pago
#*************************************************************************
    elif request.method=='POST' and 'convenios' in request.POST:
        datos = request.POST.getlist('apagar')
        sm = request.POST.get('su_ministro') #rescata el numero de sumnistro "posteado"
        print("suministro: ",sm)
        #borrar los ccp por si fueron deseleccionados que no incidan en el calculo de la deuda
        
        Deuda.objects.filter(suministro = sm, estado = 'CPP').update(estado = 'PEN') 
        importe = 0.0
        if len(datos): 
            for dato in datos:
                item = Deuda.objects.values("importe").filter(id = dato)
                importe = importe + item[0]['importe']
                Deuda.objects.filter(id = dato).update(estado = 'CPP')
                
        cuotas = [1, 2, 3, 6, 8, 12, 24, 36]
        plan = []
        for c in cuotas:
            plan.append(Calculo_Intereses(importe,c,TNA_Cuota[c]))
            
        planes  = {
            "planes" : plan,
            "suministro":sm,
        }
        return render(request, "LiquidacionConveniosApp/convenios.html", planes)
    
    elif request.method=='POST' and 'convenio' in request.POST:
        planSelect = request.POST.getlist('selPlan')
        sm = request.POST.get('su_ministro')
        suministroPlan = Suministro.objects.values("suministro", "calle", "numero").filter(id = sm) 
        print(suministroPlan)
        cuotas = 0
        print(len(planSelect), planSelect)
        if len(planSelect):
            for selec in planSelect:
                cuotas = int(selec)
                break
    
        conv = Deuda.objects.values("importe").filter(suministro = sm, estado = 'CPP')
        total = 0.0
        for monto in conv:
            total = round((total + monto['importe']),2)
        
        importeCuota = Calculo_Intereses(total,cuotas,TNA_Cuota[cuotas])        
        cuotasGeneradas = generaCuotas(cuotas, importeCuota["valor_cuota"] ,suministroPlan[0]["suministro"])
        valorCuota = cuotasGeneradas[0]['importe']
        datosConvenio = {
            "sum" : suministroPlan[0]["suministro"],
            "calle": suministroPlan[0]["calle"],
            "num": suministroPlan[0]["numero"],
            "monto": total, 
            "cuotas": cuotas,
            "interes":  TNA_Cuota[cuotas],         
        }

        informacion = {
            "cuotas": cuotasGeneradas,
            "convenio": datosConvenio,
            "suministro": sm,
            "valcuota": valorCuota,
        }
        print("datos:          ", informacion)
       
        return render(request, "LiquidacionConveniosApp/convenioAceptar.html", informacion)
   
    elif request.method == 'POST' and 'AceptarConvenio' in request.POST:
        clt = request.user
        sm = int(request.POST.get('su_ministro'))
        numSum = int(request.POST.get('numsuministro'))
        cts = int (request.POST.get('cuotas'))

        impTot = float (comaypunto(request.POST.get('importeTotal')))
        impCts = float (comaypunto(request.POST.get('importeCuota')))

        print( clt, sm, cts, impTot, impCts)
        #Primero genero el convenio de pago
        convenio = Convenio(
            cliente = clt,
            importe = impTot,
            cuotas = cts,
            importe_cuota = impCts,
            cuotas_pagadas = 0,
            estado = "ACT"
        )
        convenio.save()
        #busco el id del convenio generado
        idConvenio = Convenio.objects.values("id").filter(cliente = clt).last()
        print("Id convenio", idConvenio["id"])
        
        #Paso los items seleccionados los relaciono con el convenio de pago
        Deuda.objects.filter(suministro = sm, estado = 'CPP').update(estado = 'CDP', convenio = idConvenio["id"])

        cuota = generaCuotas(cts, impCts ,numSum)
        
        idsuministro = Suministro.objects.filter(pk = sm)
        for cta in cuota:
            deudaCuota = Deuda(
                suministro = idsuministro[0],
                documento = cta['doc'],
                vencimiento = cta['vencimiento'],
                importe = cta['importe'],
                factura = cta['fact'],
                estado = "PEN",
                tipo = "CPP"
            )
            deudaCuota.save()
        Mensaje = "Generación de plan de pagos: ({}) - importe {} - Cuotas {} ".format(cta['doc'], cta['importe'],cts) 
        
        CargarAviso (clt, "AUG", "GPP", Mensaje)
        
        return render(request, "OficinaVirtualApp/principal.html" )

        
        
    elif request.method=='POST' and 'cancelconvenio' in request.POST:
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",info)
    
    else:
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",info)
    
def generaCuotas(cuotas, importeCuota, suministro):
    cuotas_generadas = []
    fecha_generacion = str(date.today().year) + str(date.today().month) + str(date.today().day)
    for a in range(1,cuotas+1):
        nombre = "Plan_" + str(suministro) + fecha_generacion + "_" + str(a)
        factura = "Cuota_" + str(suministro) + fecha_generacion + "_" + str(a)
        cuota = { 
                 "cuota" : a,
                 "vencimiento": VencimientoCuotas(a),
                 "importe": importeCuota,
                 "doc": nombre,
                 "fact": factura,
                 }
        cuotas_generadas.append(cuota)
    return cuotas_generadas
    
    
    
def convenios(request, planes): 
    return render(request,"LiquidacionConveniosApp/convenios.html", planes)

def aceptarConvenio(request):
    return render(request, "LiquidacionConveniosApp/aceptarConvenio.html")

def convenioPago(request):
    cliente = request.user.id
    convenio = Convenio.objects.filter(cliente = cliente).order_by('-id')

    return render(request, "LiquidacionConveniosApp/convenioPago.html", {"convenios": convenio})

def Calculo_Intereses(importe, cuotas, tna):
    total_intereses = round((importe * tna / 100),2)
    iva_intereses = round((total_intereses * 0.21),2)
    total_convenio = round((importe + total_intereses + iva_intereses),2)
    valor_cuota =round((total_convenio / cuotas),2)
    datos = {
        "importe" : round((importe),2),
        "cuotas": cuotas,
        "total_intereses" : total_intereses,
        "tna" : tna,
        "iva_intereses": iva_intereses,
        "valor_cuota": valor_cuota,
        "total_convenio": total_convenio,
    }
    return datos

def VencimientoCuotas (mes):
    vencimiento = date.today() + timedelta(days=31*mes)
            #Me aseguro que el vencimiento no caiga un fin de semana
    if vencimiento.isoweekday() == 6 : 
        vencimiento = vencimiento + timedelta(days=2)
    elif vencimiento.isoweekday() == 7:
        vencimiento = vencimiento + timedelta(days=1) 
    return vencimiento

def comaypunto(valor):
    val= ""
    for va in valor:
        if va == ',':
            val = val + "."
        else:
            val = val + va
    return val