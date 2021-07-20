from django.shortcuts import render, HttpResponse


def consultaFacturas(request):

    return render(request, "ConsultasApp/facturas.html")

def consultaConsumos(request):

    return render(request, "ConsultasApp/consumos.html")