from PagosApp.models import Debito_Automatico
from AvisosAlertasApp.funciones import CargarAviso
from OficinaVirtualApp.models import Suministro
from datetime import date
from PagosApp.forms import PagoTarjetaFrom

def ControlFecha(medidor, clt):
   
    vencidas = Debito_Automatico.objects.filter(suministro = medidor, vencimiento__lte=date.today(), estado = "ACT").update(estado = "VEN")
    datos_medidor = Suministro.objects.values_list("suministro", "calle", "numero", "barrio").filter(id = medidor)[0] 
    
    if datos_medidor :           
        Mensaje = "Se vencio la tarjeta asociada al suministro: ({}) - {} No.: {} - Barrio:{}".format(datos_medidor[0], datos_medidor[1], datos_medidor[2], datos_medidor[3])
        
        CargarAviso(clt, "PAU", "DAV", Mensaje)
        return True
    return False

def TarjetaDatos():
    MESES = [(1,"Enero"), (2,"Febrero"), (3,"Marzo"), (4,"Abril"), (5,"Mayo"), (6,"Junio"), (7,"Julio"), (8,"Agosto"), (9,"Septiembre"), (10,"Octubre"),(11,"Noviembre"), (12,"Diciembre")]
    
    Bancos = [ "DESCONOCIDO","NUEVO BANCO DE SANTA FE S.A." ,"BANCO MACRO S.A.","BANCO SANTANDER RÍO S.A.","BBVA BANCO FRANCES S.A.","CITIBANK","BANCO DE LA NACIÓN ARGENTINA","BANCO PROV. DE BUENOS AIRES","ICBC - BANK CHINA","BANCO PROV. DE CÓRDOBA","BANCO SUPERVIELLE S.A.","BANCO CIUDAD DE BUENOS AIRES","BANCO PATAGONIA S.A.","BANCO HIPOTECARIO S.A.","HSBC BANK ARGENTINA S.A.","BANCO CREDICOOP COOP.LTDO.","BANCO COMAFI SOCIEDAD ANÓNIMA","NUEVO BANCO DEL CHACO S.A.","NUEVO BANCO DE ENTRE RÍOS S.A.","BANCO BICA S.A."]
    
    tarjetas = [ ("VSC", "VISA – TARJETA DE CRÉDITO"), 
        ("VSD", "VISA - TARJETA DE DÉBITO"),
        ("MTC", "MAESTRO - TARJETA DE CREDITO"),
        ("MTD", "MAESTRO - TARJETA DE DÉBITO"),
        ("MCR", "MASTERCARD"),]
    
    BANCOS = []
    val = 0
    for i in Bancos:
        BANCOS.append((val, i))
        val = val+1

    fecha = date.today()
    ANIOS = []
    for i in range(fecha.year, (fecha.year + 15)):
        ANIOS.append((i, i))
    
    hoy = date.today()
    informacion = {
        "bancos" : BANCOS,
        'meses' : MESES,
        'anios' : ANIOS,
        'tarjetas' : tarjetas,
    }
    return informacion
    #deb_auto = PagoTarjetaFrom()
    #deb_auto.fields['sel_banco'].choices = BANCOS
    #deb_auto.fields['MM'].choices = MESES
    #deb_auto.fields['AA'].choices = ANIOS
    #deb_auto.fields['MM'].default = hoy.month
    