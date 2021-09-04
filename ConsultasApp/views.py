from django.shortcuts import render, HttpResponse

from ConsultasApp.models import Consumo, Factura
from OficinaVirtualApp.models import Suministro 
from ConsultasApp.forms import ConsumoForm, FacturaForm


def consultaFacturas(request):
    facturas = FacturaForm(request.POST)
    usuario = request.user.id
    suministros = Suministro.objects.values_list("id", "suministro").filter(cliente = usuario) 
    facturas.fields['suministro'].choices = suministros
    
    lista_facturas = ""
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
    usuario = request.user.id
    suministros = Suministro.objects.values_list("id", "suministro").filter(cliente = usuario) 
    
    consumo = ConsumoForm(request.POST)
    consumo.fields['suministro'].choices = suministros
    
    medidor = consumo.data.get('suministro')
    datos_consumo = Consumo.objects.filter(suministro = medidor)
    lista={
        "consumos": consumo,
        "datos": datos_consumo,
       
    }
    if request.method == 'POST' :
        datos_consumo = Consumo.objects.filter(suministro = medidor)
        return render(request, "ConsultasApp/consumos.html", lista) 
    
    return render(request, "ConsultasApp/consumos.html",lista)
