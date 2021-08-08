from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ReclamosForm


def reclamos(request): 
    formulario = ReclamosForm()
     
    #if request.method == 'POST':
    #	formulario = ReclamosForm(request.POST)
    #    if formulario.is_valid():
	#	    form.save()
    #    return redirect('ReclamosApp/reclamos.html')
    #else:
	#	form = ReclamosForm()
    return render(request, "ReclamosApp/reclamos.html", {'formulario':formulario})


def seguimientoReclamos(request):
    return render(request, "ReclamosApp/seguimientoReclamos.html")

