from django.shortcuts import render, HttpResponse
from ConsultasApp.models import Consumo, Factura
from OficinaVirtualApp.models import Suministro 
from ConsultasApp.forms import ConsumoForm, FacturaForm



def consultaFacturas(request):
    facturas = FacturaForm(request.POST)
    medidor = facturas.data.get("suministro")
    lista_facturas = Factura.objects.filter(suministro = medidor)
    lista ={"facturas": facturas,
            "datos": lista_facturas,
    }
    print("GET")   
    print(medidor)
    if request.method == 'POST' and facturas.is_valid():
        
        medidor = facturas.data.get("suministro")
        lista_facturas = Factura.objects.filter(suministro = medidor)
        print("POST")   
        print(medidor)
        print(facturas)
        lista = {
                "facturas": facturas,
                "datos": lista_facturas,
        }
        
    return render(request, "ConsultasApp/facturas.html", lista)

def consultaConsumos(request):   
    consumo = ConsumoForm(request.POST)
    medidor = consumo.data.get("suministro")
    print("GET")
    print(medidor)
    datos_consumo = Consumo.objects.filter(suministro = medidor)

    lista={
        "consumos": consumo,
        "datos": datos_consumo,
    }
    if request.method == 'POST' :
        medidor = consumo.data.get("suministro")
        print("POST")   
        print(medidor)
        datos_consumo = Consumo.objects.filter(suministro = medidor)
        return render(request, "ConsultasApp/consumos.html", lista) 
    
    return render(request, "ConsultasApp/consumos.html",lista)
