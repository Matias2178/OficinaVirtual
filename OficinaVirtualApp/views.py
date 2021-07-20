from django.shortcuts import render, HttpResponse


# Create your views here.
def inicio(request):

    return render(request, "OficinaVirtualApp/inicio.html")
    #return HttpResponse("Inicio")


def datosPersonales(request):


    return render(request, "OficinaVirtualApp/datosPersonales.html")


