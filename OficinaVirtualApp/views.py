from django.shortcuts import render, HttpResponse


def principal(request):
    usuario = request.user.pk
    
    return render(request, "OficinaVirtualApp/principal.html",{"usuario": usuario})

def datosPersonales(request):
    return render(request, "OficinaVirtualApp/datosPersonales.html")

def registro(request):
    return render(request, "OficinaVirtualApp/registroAAA.html")


