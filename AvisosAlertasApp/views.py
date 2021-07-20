from django.shortcuts import render, HttpResponse

# Create your views here.
def avisos(request):

    return render(request, "AvisosAlertasApp/avisos.html")

def alertas(request):

    #return HttpResponse("Alerta de que te entra agua")
    return render(request, "AvisosAlertasApp/alertas.html")