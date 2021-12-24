
from django.db.models.deletion import SET_NULL
from django.shortcuts import render, HttpResponse
from datetime import date
from OficinaVirtualApp.models import Suministro
from PagosApp.models import Debito_Automatico, Cupon_Pago
from PagosApp.forms import DebitoAutomaticoFrom, BajaDebitoAutomaticoFrom
from AvisosAlertasApp.funciones import CargarAviso
from PagosApp.funciones import ControlFecha
from PagosApp.forms import PagoTarjetaFrom
from LiquidacionConveniosApp.models import Deuda 

def cuponPago(request):
    usuario = request.user.id
    cupones = Cupon_Pago.objects.filter(cliente = usuario).exclude( estado =  'PAG')
    lista = {
        "cupones" : cupones,
    }
    if request.method == 'POST' and 'cancelar' in request.POST :
        #borra todos los datos del cupon de pago generado.
        cupon = request.POST.getlist('idcupon')
        if len(cupon):
            for cp in cupon: 
                idcupon = Cupon_Pago.objects.values('id').filter(id = cp)
                Deuda.objects.filter(cupon_pago = idcupon).update(estado = 'PEN', cupon_pago = None)
                Cupon_Pago.objects.filter(id = idcupon).update(estado = 'APU')
            
            return render(request, "OficinaVirtualApp/principal.html" )
        
    if request.method == 'POST' and 'tarjeta_debito' in request.POST :
        cupon = request.POST.getlist('idcupon')
        monto = 0.0
        if len(cupon):
            for cp in cupon: 
                apagar = Cupon_Pago.objects.values('importe').filter(id = cp)
                Cupon_Pago.objects.filter(id = cp).update(estado = "EDP")
                monto = monto + apagar[0]['importe']
                
                
        #datos = TarjetaDatos()
        #inicio = {
        #    "MM" : datos['meses'],
        #    "AA" : datos['anios'],
        #    "sel_banco" : datos["bancos"],
        #    "tarjeta" : datos['tarjetas'],
        #    "titular" : "",
        #    "numero_tarjeta" : 0,
        #}  
        #pagoTarjeta = PagoTarjetaFrom(initial = inicio)     
        lista={
            'monto' : monto,
            #'pagoTarjeta' : pagoTarjeta,
        }   
        return render(request, "PagosApp/tarjetaDebito.html", lista )
#**************************************************************************
# Se hace el pago con la tarjeta de debito
#**************************************************************************     
    elif request.method=='POST' and 'tarjetaPagar' in request.POST:
        cupones = Cupon_Pago.objects.values('id', ).filter(cliente = usuario, estado = "EDP")
        for cupon in cupones:
            Deuda.objects.filter(cupon_pago = cupon['id'], estado = 'PPA' ).update(estado = 'CAN') 
        
        Cupon_Pago.objects.filter(cliente = usuario, estado = "EDP").update(estado = 'PAG')       
        
        return render(request, "OficinaVirtualApp/principal.html" )
                
    
    return render(request, "PagosApp/cuponPago.html", lista)

def debitoAutomatico(request):
    mensaje = ""
    alerta = 0
    
    MESES = [(1,"Enero"), (2,"Febrero"), (3,"Marzo"), (4,"Abril"), (5,"Mayo"), (6,"Junio"), (7,"Julio"), (8,"Agosto"), (9,"Septiembre"), (10,"Octubre"),(11,"Noviembre"), (12,"Diciembre")]
    
    Bancos = [ "DESCONOCIDO","NUEVO BANCO DE SANTA FE S.A." ,"BANCO MACRO S.A.","BANCO SANTANDER RÍO S.A.","BBVA BANCO FRANCES S.A.","CITIBANK","BANCO DE LA NACIÓN ARGENTINA","BANCO PROV. DE BUENOS AIRES","ICBC - BANK CHINA","BANCO PROV. DE CÓRDOBA","BANCO SUPERVIELLE S.A.","BANCO CIUDAD DE BUENOS AIRES","BANCO PATAGONIA S.A.","BANCO HIPOTECARIO S.A.","HSBC BANK ARGENTINA S.A.","BANCO CREDICOOP COOP.LTDO.","BANCO COMAFI SOCIEDAD ANÓNIMA","NUEVO BANCO DEL CHACO S.A.","NUEVO BANCO DE ENTRE RÍOS S.A.","BANCO BICA S.A."]
    
    BANCOS = []
    val = 0
    for i in Bancos:
        BANCOS.append((val, i))
        val = val+1

    fecha = date.today()
    ANIOS = []
    for i in range(fecha.year, (fecha.year + 15)):
        ANIOS.append((i, i))
    
    usuario = request.user.id
    suministros = Suministro.objects.values_list("id", "suministro").filter(cliente = usuario) 
    hoy = date.today()
    deb_auto = DebitoAutomaticoFrom(request.POST)
    deb_auto.fields['suministro'].choices = suministros
    deb_auto.fields['sel_banco'].choices = BANCOS
    deb_auto.fields['MM'].choices = MESES
    deb_auto.fields['AA'].choices = ANIOS
    deb_auto.fields['MM'].default = hoy.month

    if request.method == 'POST' :
        aa = int (deb_auto.data.get('AA'))
        mm = int (deb_auto.data.get('MM'))        
        tjt_vencimiento = date(aa, mm, 1)

        #control si la tarjeta de credito esta vencida
        if not tjt_vencimiento > date.today():
            mensaje = "Su tarjeta se encuentra vencida"
            alerta = 1
            
        else:    
            suministro = deb_auto.data.get('suministro')
            debitos_activos = Debito_Automatico.objects.filter(suministro = suministro, estado = "ACT")
           
            if debitos_activos :
                mensaje = "Ya se encunentra activo un debito automatico asociado a este suministro"  
                alerta = 2 
                deb_auto = DebitoAutomaticoFrom()
                deb_auto.fields['suministro'].choices = suministros
                deb_auto.fields['sel_banco'].choices = BANCOS
                deb_auto.fields['MM'].choices = MESES
                deb_auto.fields['AA'].choices = ANIOS
                deb_auto.fields['MM'].default = hoy.month
            else:
                #si no puedo por las buenas lo hacemos por las malas
                num = int(deb_auto.data.get("sel_banco")) 
                id_suministro = Suministro.objects.filter(pk = suministro)
                debitos = Debito_Automatico(
                    suministro = id_suministro[0],
                    tarjeta = deb_auto.data.get("tarjeta"),
                    banco = Bancos[num],
                    nombre = deb_auto.data.get("nombre"),
                    numero_tarjeta = deb_auto.data.get("numero_tarjeta"),
                    vencimiento = tjt_vencimiento,
                    estado = "ACT"
                )
                debitos.save()
                deb_auto = DebitoAutomaticoFrom()
                deb_auto.fields['suministro'].choices = suministros
                deb_auto.fields['sel_banco'].choices = BANCOS
                deb_auto.fields['MM'].choices = MESES
                deb_auto.fields['AA'].choices = ANIOS
                deb_auto.fields['MM'].default = hoy.month
                mensaje = "Debito automatico adherido correctamente"
                alerta = 3    
            
    lista = {
        "deb_auto": deb_auto,
        "mensaje": mensaje,
        "alerta": alerta,
        }   
    return render(request, "PagosApp/debitoAutomatico.html",lista)


def bajaDebitoAutomatico(request):
    baja = BajaDebitoAutomaticoFrom(request.POST)
    usuario = request.user.id
    
    suministros = Suministro.objects.values_list("id", "suministro").filter(cliente = usuario) 

    baja.fields['suministro'].choices = suministros
    dic = {
        "baja": baja,
        # "debito": debito,
    }
    if request.method == "POST" :
        if "btn_suministro" in request.POST:
            medidor = baja.data.get("suministro")
            debito = Debito_Automatico.objects.filter(suministro = medidor, estado = "ACT" )
            cliente1 = request.user
            ControlFecha(medidor, cliente1)
            dic = {
                "baja": baja,
                "debito": debito,
            }
        elif "btn_baja" in request.POST:
            medidor = baja.data.get("suministro")
            Debito_Automatico.objects.filter(suministro = medidor, estado = "ACT").update(estado = "CAN")
            dic = {
                "baja": baja,
            }
            datos_medidor = Suministro.objects.values_list("suministro", "calle", "numero", "barrio").filter(id = medidor)[0]            
            Mensaje = "Cancelacion del debito automatico del suministro: ({}) - {} No.: {} - Barrio:{}".format(datos_medidor[0], datos_medidor[1], datos_medidor[2], datos_medidor[3])
            CargarAviso(cliente1, "PAU", "BDA", Mensaje)
            
        return render(request, "PagosApp/bajaDebitoAutomatico.html",dic)
        
      
    return render(request, "PagosApp/bajaDebitoAutomatico.html",dic)
