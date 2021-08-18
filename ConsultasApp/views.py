from django.shortcuts import render, HttpResponse
from ConsultasApp.models import Consumo, Factura
from OficinaVirtualApp.models import Suministro 
from ConsultasApp.forms import ConsumoForm



def consultaFacturas(request):
    facturas = Factura.objects.all()
    suministros = Suministro.objects.all()
    lista ={"facturas": facturas,
            "suministros": suministros
            }
    

    return render(request, "ConsultasApp/facturas.html", lista)

def consultaConsumos(request):
    consumo = ConsumoForm(request.POST)
    if request.method == 'POST':
        if consumo.is_valid():
                datos_consumo = consumo.cleaned_data
                print(datos_consumo.get("suministro"))

    lista = {
            "consumos": consumo
            
    }
    return render(request, "ConsultasApp/consumos.html", lista) 
    


