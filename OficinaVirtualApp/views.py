from django.shortcuts import render, HttpResponse

def principal(request):
    return render(request, "OficinaVirtualApp/principal.html")

def datosPersonales(request):
    return render(request, "OficinaVirtualApp/datosPersonales.html")

def registro(request):
    return render(request, "OficinaVirtualApp/registroAAA.html")


