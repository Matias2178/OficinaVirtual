from django.shortcuts import render, HttpResponse
from AvisosAlertasApp.models import Aviso, Alerta
from OficinaVirtualApp.models import Cliente


# Create your views here.
def avisos(request):
    avisos =  Aviso.objects.all()
    return render(request, "AvisosAlertasApp/avisos.html", {"avisos": avisos} )

def alertas(request, cliente_id):
    cliente_selecionado =  Cliente.objects.get(id = cliente_id)
    alertas = Alerta.objects.filter(cliente = cliente_selecionado)
    return render(request, "AvisosAlertasApp/alertas.html", {"alertas": alertas})
