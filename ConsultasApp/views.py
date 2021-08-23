from django.shortcuts import render, HttpResponse
from ConsultasApp.models import Consumo, Factura
from OficinaVirtualApp.models import Suministro 
from ConsultasApp.forms import ConsumoForm, FacturaForm



def consultaFacturas(request):
    facturas = FacturaForm(request.POST)
    medidor = facturas.data.get("suministro")
    lista_facturas = Factura.objects.filter(suministro = medidor)
    #suministros = SuministroForm()
    lista ={"facturas": facturas,
            "datos": lista_facturas,
            }
    if request.method == 'POST' and facturas.is_valid():
        medidor = facturas.data.get("suministro")
        lista_facturas = Factura.objects.filter(suministro = medidor)
        lista = {
                "facturas": facturas,
                "datos": lista_facturas,
        }
        
    return render(request, "ConsultasApp/facturas.html", lista)

def consultaConsumos(request):
    consumo = ConsumoForm(request.POST)
    print(consumo)
    medidor = consumo.data.get("suministro")
    datos_consumo = Consumo.objects.filter(suministro = medidor)
    lista={
            "consumos": consumo,
            "datos": datos_consumo,
    }
    if request.method == 'POST' and consumo.is_valid():
        medidor = consumo.data.get("suministro")
        datos_consumo = Consumo.objects.filter(suministro = medidor)
        print(datos_consumo.get("suministro"))
        return render(request, "ConsultasApp/consumos.html", lista) 
    
    return render(request, "ConsultasApp/consumos.html",lista)
