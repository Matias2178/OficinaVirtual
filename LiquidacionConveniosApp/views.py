from django.shortcuts import render, HttpResponse
#from LiquidacionConveniosApp.models import Deuda, Convenio
from LiquidacionConveniosApp.models import Deuda,Convenio
from OficinaVirtualApp.models import Suministro
from LiquidacionConveniosApp.forms import DeudaForm, SuministroForm

# Create your views here.
def liquidacionDeuda(request):
    formulario = DeudaForm()
    sumi = SuministroForm()
    
    datos= {
        "form" : formulario,
        "sumi": sumi,
    }
    if request.method == 'POST':
        formulario = DeudaForm(data=request.POST) 
        medidor = request.POST.get("suministro")
       # print(medidor)     
        #deuda = Deuda.objects.filter(suministro = medidor) #colocar filtro por usuario y deuda activa
        deuda = Deuda.objects.filter(suministro = 2)
        liquidacion = {"deudas": deuda,
                       "form": formulario,
                       "medidor": medidor,
                       }    
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",liquidacion)
    else:
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",{"form": formulario})

def convenioPago(request):
    convenio = Convenio.objects.all() 

    return render(request, "LiquidacionConveniosApp/convenioPago.html", {"convenios": convenio})
