from PagosApp.models import Debito_Automatico
from AvisosAlertasApp.funciones import CargarAviso
from OficinaVirtualApp.models import Suministro
from datetime import date

def ControlFecha(medidor, clt):
    print(medidor, clt)
    
    vencidas = Debito_Automatico.objects.filter(suministro = medidor, vencimiento__lte=date.today(), estado = "ACT").update(estado = "VEN")
    datos_medidor = Suministro.objects.values_list("suministro", "calle", "numero", "barrio").filter(id = medidor)[0] 
    
    if datos_medidor :           
        Mensaje = "Se vencio la tarjeta asociada al suministro: ({}) - {} No.: {} - Barrio:{}".format(datos_medidor[0], datos_medidor[1], datos_medidor[2], datos_medidor[3])
        
        CargarAviso(clt, "PAU", "DAV", Mensaje)
        return True
    return False
    
    