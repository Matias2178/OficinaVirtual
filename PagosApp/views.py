
from django.shortcuts import render, HttpResponse

def botonPago(request):


    return render(request, "PagosApp/botonPago.html")

def debitoAutomatico(request):
    return render(request, "PagosApp/debitoAutomatico.html")


def bajaDebitoAutomatico(request):
    return render(request, "PagosApp/bajaDebitoAutomatico.html")
