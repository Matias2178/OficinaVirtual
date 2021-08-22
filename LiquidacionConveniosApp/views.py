from django.shortcuts import render, HttpResponse
#from LiquidacionConveniosApp.models import Deuda, Convenio
from LiquidacionConveniosApp.models import Deuda, Convenio
from LiquidacionConveniosApp.forms import DeudaForm, SuministroForm

# Create your views here.
def liquidacionDeuda(request):
    usuario = request.user.id
    formulario = DeudaForm()
    medidor = SuministroForm()#.objects.filter(cliente = usuario)    
    info={
        "form": formulario,
        "medidor": medidor,
    }
    
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
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",info) #cambiar la vista
    
    elif request.method=='POST' and 'convenio' in request.POST:
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",info) #cambiar la vista
        
    else:
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",info)

def convenioPago(request):
    convenio = Convenio.objects.all() 

    return render(request, "LiquidacionConveniosApp/convenioPago.html", {"convenios": convenio})
