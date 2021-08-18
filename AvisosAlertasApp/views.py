from django.shortcuts import render, HttpResponse
from AvisosAlertasApp.models import Aviso, Alerta
from django.contrib.auth.models import User


# Create your views here.
def avisos(request):
    avisos =  Aviso.objects.all()
    return render(request, "AvisosAlertasApp/avisos.html", {"avisos": avisos} )

def alertas(request):
    cliente = request.user.id
    alertas = Alerta.objects.filter(cliente = cliente)
    return render(request, "AvisosAlertasApp/alertas.html", {"alertas": alertas})
