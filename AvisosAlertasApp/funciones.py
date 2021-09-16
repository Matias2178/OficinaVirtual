from AvisosAlertasApp.models import Alerta

def CargarAviso(clt, org, mtv, msj):
    print(clt)
    alerta = Alerta(
        cliente = clt,
        origen  = org,
        motivo = mtv,
        mensaje = msj,
        estado = "EMI")
    alerta.save()
   
    