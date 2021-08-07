from django.shortcuts import render, HttpResponse
from LiquidacionConveniosApp.models import Deuda, Convenio
from OficinaVirtualApp.models import Suministro

# Create your views here.
def liquidacionDeuda(request):
    
    suministros = Suministro.objects.all() #cambiar a filtro
    deuda = Deuda.objects.all() #colocar filtro por usuario y deuda activa
    
    liquidacion = {"suministros": suministros,
                   "deudas": deuda
    }
    
    return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",liquidacion)

def convenioPago(request):
    convenio = Convenio.objects.all() 

    return render(request, "LiquidacionConveniosApp/convenioPago.html", {"convenios": convenio})
