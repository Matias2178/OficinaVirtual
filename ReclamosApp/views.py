from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ReclamosForm
from ReclamosApp.models import Seguimiento, Reclamos
from datetime import datetime



def reclamos(request):
    formulario = ReclamosForm()
    reclamo = Reclamos
    seguimiento = Seguimiento()
     
    if request.method == 'POST':
        formulario = ReclamosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #id = formulario.data.get('suministro')
            rec = reclamo.objects.last()
            
            print(rec.id)
            id_rec = reclamo.objects.get(id=rec.id)
            seg = Seguimiento(reclamo = id_rec,
                              fecha_novedad = datetime.now(),
                              area = 'REC',
                              observaciones = 'Ingresado',
                              estado = 'REC')
            seg.save()
            return render(request,"ReclamosApp/seguimientoReclamos.html")
            
        return redirect('/reclamos/?valido')
    else:
        form = ReclamosForm()
        return render(request, "ReclamosApp/reclamos.html", {'formulario':formulario})
    
   # return render(request, "ReclamosApp/reclamos.html", {'formulario':formulario})
    

def seguimientoReclamos(request):
    reclamos = ReclamosForm()
    return render(request, "ReclamosApp/seguimientoReclamos.html")

