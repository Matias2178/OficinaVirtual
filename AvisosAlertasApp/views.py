from django.shortcuts import render, HttpResponse
from AvisosAlertasApp.models import Aviso, Alerta
from django.contrib.auth.models import User


# Create your views here.
def avisos(request):
    avisos =  Aviso.objects.all().order_by('-id')
    return render(request, "AvisosAlertasApp/avisos.html", {"avisos": avisos} )

def alertas(request):
    cliente = request.user.id
    alertas = Alerta.objects.filter(cliente = cliente).order_by('-id')
    Alerta.objects.filter(cliente = cliente, estado = "EMI").update(estado = "VIS")
    if request.method == "POST":
        
        Alerta.objects.filter(cliente = cliente, estado = "VIS").update(estado = "ACE")
        return render(request, "AvisosAlertasApp/alertas.html", {"alertas": alertas})   
    return render(request, "AvisosAlertasApp/alertas.html", {"alertas": alertas})

