from django.shortcuts import render, HttpResponse
from ConsultasApp.models import Consumo, Factura
from OficinaVirtualApp.models import Suministro 


def consultaFacturas(request):
    facturas = Factura.objects.all()
    suministros = Suministro.objects.all()
    lista ={"facturas": facturas,
            "suministros": suministros
            }

    return render(request, "ConsultasApp/facturas.html", lista)

def consultaConsumos(request):
    consumos = Consumo.objects.all()
    suministros = Suministro.objects.all()
    lista ={"consumos": consumos,
            "suministros": suministros
            }
    return render(request, "ConsultasApp/consumos.html",lista)