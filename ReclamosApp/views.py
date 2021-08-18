from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ReclamosForm
from ReclamosApp.models import Seguimiento



def reclamos(request):
    formulario = ReclamosForm()
     
    if request.method == 'POST':
        formulario = ReclamosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request,"ReclamosApp/seguimientoReclamos.html")
            
        return redirect('/reclamos/?valido')
    else:
        form = ReclamosForm()
        return render(request, "ReclamosApp/reclamos.html", {'formulario':formulario})
    
   # return render(request, "ReclamosApp/reclamos.html", {'formulario':formulario})
    

def seguimientoReclamos(request):
    return render(request, "ReclamosApp/seguimientoReclamos.html")

