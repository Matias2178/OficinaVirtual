from django.shortcuts import render, HttpResponse


# Create your views here.
def inicio(request):

    return render(request, "OficinaVirtualApp/inicio.html")

def principal(request):
    return render(request, "OficinaVirtualApp/principal.html")

def datosPersonales(request):
    return render(request, "OficinaVirtualApp/datosPersonales.html")

def registro(request):
    return render(request, "OficinaVirtualApp/registro.html")


