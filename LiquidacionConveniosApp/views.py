from django.shortcuts import render, HttpResponse
#from LiquidacionConveniosApp.models import Deuda, Convenio
from LiquidacionConveniosApp.models import Deuda, Convenio
from OficinaVirtualApp.models import Suministro
from LiquidacionConveniosApp.forms import DeudaForm, SuministroForm

# Create your views here.
def liquidacionDeuda(request):
    formulario = DeudaForm()
    
    if request.method=='POST' and 'sel_suministro' in request.POST: 
        formulario = DeudaForm(data=request.POST) 
        suministro = formulario.data.get("suministro")
        deudas = Deuda.objects.filter(suministro = suministro)
        usuario_actual = "Bienvenido: {} {}".format(request.user, request.user.id)
        total = "2187,43"
        print(deudas)
        print("hola mundo "+ suministro) 
        liquidacion = {
            "form": formulario,
            "deudas": deudas,
            "usuario": usuario_actual,
            "total": total,
        }
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",liquidacion)
    
    elif request.method=='POST' and 'liquidar' in request.POST:
        usuario_actual = "Paga lo que debes {}".format(request.user)
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",{"form": formulario}) #cambiar la vista
    
    elif request.method=='POST' and 'convenio' in request.POST:
        usuario_actual = "Paga lo que debes {}".format(request.user)
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",{"form": formulario}) #cambiar la vista
        
    else:
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",{"form": formulario})

def convenioPago(request):
    convenio = Convenio.objects.all() 

    return render(request, "LiquidacionConveniosApp/convenioPago.html", {"convenios": convenio})
