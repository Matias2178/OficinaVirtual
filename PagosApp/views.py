
from django.shortcuts import render, HttpResponse
from datetime import date
from OficinaVirtualApp.models import Suministro
from PagosApp.models import Debito_Automatico, Cupon_Pago
from PagosApp.forms import DebitoAutomaticoFrom, BajaDebitoAutomaticoFrom
from AvisosAlertasApp.funciones import CargarAviso
from PagosApp.funciones import ControlFecha

def cuponPago(request):
    usuario = request.user.id
    cupones = Cupon_Pago.objects.filter(cliente = usuario)
    lista = {
        "cupones" : cupones,
    }
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
    # print(ANIOS)
    # print(BANCOS)
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
                # deb_auto.fields['vencimiento'].initial = tjt_vencimiento    #cargo la fecha de vencimiento
                # deb_auto.fields['estado'].initial = "ACT"                   #paso a activo el estado de la tarjeta
                # deb_auto.fields['banco'].initial = deb_auto.data.get('sel_banco')
                # if deb_auto.is_valid():
                #     mensaje = "Todo bien??"
                #     deb_auto.save()
                # else:
                #     mensaje = "la cagaste"
                #     print("no se donde la cague")
                #     print(deb_auto)
                #     print(deb_auto.errors)
                
            
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
