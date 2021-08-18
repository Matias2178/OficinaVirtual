from django.shortcuts import render, HttpResponse
#from LiquidacionConveniosApp.models import Deuda, Convenio
from LiquidacionConveniosApp.models import Deuda,Convenio
from OficinaVirtualApp.models import Suministro
from LiquidacionConveniosApp.forms import DeudaForm, SuministroForm

# Create your views here.
def liquidacionDeuda(request):
    formulario = DeudaForm()
    sumi1 = SuministroForm()
    sumi = sumi1.get(id=request.user.id)
    formulario = DeudaForm(data=request.POST)
    medidor = request.POST.get("suministro")
    informacion = formulario.data.get("suministro")
    print(informacion)
    deuda = Deuda.objects.filter(suministro = informacion)
    usuario_actual = "Bienvenido: {} {}".format(request.user, request.user.id)
    deuda = "0"
    
    
    liquidacion = {
        "deudas": deuda,
        "form": formulario,
        "medidor": medidor,
        "usuario": usuario_actual,
        "deuda": deuda,
        }
    
    #if request.method == 'POST':
    if request.method=='POST' and 'sel_suministro' in request.POST: 
        formulario = DeudaForm(data=request.POST) 
        medidor = request.POST.get("suministro")
        informacion =formulario.data.get("suministro")
        deuda = Deuda.objects.filter(suministro = informacion)
        usuario_actual = "Bienvenido: {} {}".format(request.user, request.user.id)
        deuda = "0"
          
        print("hola mundo") 
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",liquidacion)
    
    elif request.method=='POST' and 'liquidar' in request.POST:
        usuario_actual = "Paga lo que debes {}".format(request.user)
        print("usuario_actual")
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",liquidacion)
    
    elif request.method=='POST' and 'convenio' in request.POST:
        usuario_actual = "Paga lo que debes {}".format(request.user)
        print("genera convenio de pago")
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",liquidacion)
        
    else:
        return render(request, "LiquidacionConveniosApp/liquidacionDeuda.html",{"form": formulario})

def convenioPago(request):
    convenio = Convenio.objects.all() 

    return render(request, "LiquidacionConveniosApp/convenioPago.html", {"convenios": convenio})
