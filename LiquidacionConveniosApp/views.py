from django.shortcuts import render, HttpResponse, redirect
from LiquidacionConveniosApp.models import Deuda, Convenio
from LiquidacionConveniosApp.forms import DeudaForm
from OficinaVirtualApp.models import Suministro
from PagosApp.models import Pagos, Cupon_Pago
from datetime import datetime, timedelta, date
# Create your views here.

def liquidacionDeuda(request):
    usuario = request.user.id
    suministros = Suministro.objects.values_list("id", "suministro").filter(cliente = usuario) 
    formulario_deuda = DeudaForm(request.POST)
    formulario_deuda.fields['suministro'].choices = suministros
      
    info={
        "form": formulario_deuda,
    }
    suministro = formulario_deuda.data.get("suministro")
    deudas = Deuda.objects.filter(suministro = suministro)
    print(deudas)
    liquidacion = {
        "form": formulario_deuda,
        "deudas": deudas,
    }
    if request.method=='POST' and 'sel_suministro' in request.POST: 
   
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",liquidacion)
    
    elif request.method=='POST' and 'liquidar' in request.POST:
        datos = request.POST.getlist('apagar')
        print("------$$$@@@@@@@@@@_______")
        print(datos)
        if len(datos):
            #calculo el total de los importes
            importe = 0.0
            for dato in datos:
                item = Deuda.objects.values("importe").filter(id = dato)
                print(dato, item)
                importe = importe + item[0]['importe']
            print(importe)
            vencimiento = datetime.now() + timedelta(weeks=1)
            #Me aseguro que el vencimiento no caiga un fin de semana
            if vencimiento.isoweekday() == 6 : 
                vencimiento = vencimiento + timedelta(days=2)
            elif vencimiento.isoweekday() == 7:
                vencimiento = vencimiento + timedelta(days=1)
            actual = request.user
            print("Usuario:", actual)
            print(vencimiento)
            
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
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",liquidacion) #cambiar la vista
    
    elif request.method=='POST' and 'convenio' in request.POST:
        datos = request.POST.getlist('apagar')
        if len(datos):
            importe = 0.0
            for dato in datos:
                item = Deuda.objects.values("importe").filter(id = dato)
                importe = importe + item[0]['importe']
                
            una_cuota = Calculo_Intereses(importe, 1, 0.0)
            dos_cuotas = Calculo_Intereses(importe, 2, 12.0)
            tres_cuotas = Calculo_Intereses(importe, 3, 12.0)
            seis_cuotas = Calculo_Intereses(importe, 6, 12.0)
            ocho_cuotas = Calculo_Intereses(importe, 8, 18.0)
            doce_cuotas = Calculo_Intereses(importe, 12, 18.0)
            veinticuatro_cuotas = Calculo_Intereses(importe, 24, 30.0)
            trentayseis_cuotas = Calculo_Intereses(importe, 36, 30.0)
            planes = {
                "una_cuota" : una_cuota,
                "dos_cuotas": dos_cuotas,
                "tres_cuotas": tres_cuotas,
                "seis_cuotas": seis_cuotas,
                "ocho_cuotas": ocho_cuotas,
                "doce_cuotas": doce_cuotas,
                "veinticuatro_cuotas" : veinticuatro_cuotas,
                "treintayseis_cuotas" : trentayseis_cuotas,
            }
            
            return redirect("/convenios.html", planes )
        
            
        
        
        
        
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",info) #cambiar la vista
        
    else:
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",info)
def convenios(request):
    
    return render(request,"LiquidacionConveniosApp/convenios.html")

def convenioPago(request):
    cliente = request.user.id
    convenio = Convenio.objects.filter(cliente = cliente).order_by('-id')

    return render(request, "LiquidacionConveniosApp/convenioPago.html", {"convenios": convenio})

def Calculo_Intereses(importe, cuotas, tna):
    total_intereses = importe * tna / 100
    iva_intereses = total_intereses * 1.21
    total_convenio = importe + total_intereses + iva_intereses
    valor_cuota = total_convenio / cuotas
    datos = {
        "cuotas": cuotas,
        "total_intereses" : total_intereses,
        "tna" : tna,
        "iva_intereses": iva_intereses,
        "valor_cuota": valor_cuota,
        "total_convenio ": total_convenio,
    }
    return datos