from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ReclamosForm, SeguimientoFrom
from ReclamosApp.models import Seguimiento, Reclamos
from OficinaVirtualApp.models import Suministro
from datetime import datetime, timedelta

def reclamos(request):
    usuario = request.user.id
    suministros = Suministro.objects.values_list("id", "suministro").filter(cliente = usuario)  
    formulario = ReclamosForm()
    formulario.fields['suministro'].choices = suministros
    
    reclamo = Reclamos
    seguimiento = Seguimiento()
     
    if request.method == 'POST':
        formulario = ReclamosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            id_rec = reclamo.objects.last()
            print(id_rec)
            seg = Seguimiento(reclamo = id_rec,
                              fecha_novedad = datetime.now(),
                              area = 'REC',
                              observaciones = 'Ingresado',
                              estado = 'REC')
            seg.save()
            datos = {
                "reclamos": formulario,
            }
            return render(request, "ReclamosApp/seguimientoReclamos.html", datos)
            
        return redirect('/reclamos/?valido')
    else:
        form = ReclamosForm()
        return render(request, "ReclamosApp/reclamos.html", {'formulario':formulario})

    

def seguimientoReclamos(request):
    
    usuario = request.user.id
    suministros = Suministro.objects.values_list("id", "suministro").filter(cliente = usuario) 
    
    reclamo = ReclamosForm(request.POST)
    seguimiento = SeguimientoFrom(request.POST)
    
    #---- Se cargan los suministros del usuario actual ----
    reclamo.fields['suministro'].choices = suministros  
    # seguimiento.fields['lista_reclamos'].choices = [(0, "No se encuentran reclamos realizados")]
    
    medidor = reclamo.data.get('suministro')
    reclamos = Reclamos.objects.values_list("id", "tipo_reclamo").filter(suministro = medidor)
    seguimiento.fields['lista_reclamos'].choices = reclamos
    hoy = datetime.now()
    print("hoy es: ",hoy.isoweekday())
    vencimiento = hoy + timedelta(days=3)
    print("Una Semana Mas", vencimiento.isoweekday())
    #print(datetime.today().strftime('%A'))
    js = "Esto es una prueba de como son las cosasa"
    
 
    datos = {
       "reclamos": reclamo,
       "seguimiento" : seguimiento,
    }
    if request.method == "POST" and "btn_suministro" in request.POST:
        print("#####boton selec Suministro#####")
        # medidor = reclamo.data.get('suministro')
        # reclamos = Reclamos.objects.values_list("id", "tipo_reclamo").filter(suministro = medidor)
        # seguimiento.fields['lista_reclamos'].choices = reclamos
        datos = {
            "reclamos": reclamo,
            "seguimiento" : seguimiento,
        }
        return render(request, "ReclamosApp/seguimientoReclamos.html", datos)
        
    elif request.method == "POST" and "btn_reclamo" in request.POST:
        print("#####boton selec Reclamo #####")
        reclamo_id = seguimiento.data.get('lista_reclamos')
        reclamo_sel = Reclamos.objects.filter(pk = reclamo_id)
        seguimiento_sel = Seguimiento.objects.filter(reclamo = reclamo_id)
        el_reclamo = reclamo_sel[0]
        el_seguimiento = seguimiento_sel[0]
        
        error = "Puto el que lee"
        print("Reclamo:", reclamo_sel)
        print("El reclamo:", el_reclamo)
        print("Seguimiento:", seguimiento_sel)
        
        
        dato = {
            "error": error,
            "js": js,
            "reclamos": reclamo,
            "seguimiento": seguimiento,
        }
        return render(request, "ReclamosApp/seguimientoReclamos.html", dato)
    else:
        return render(request, "ReclamosApp/seguimientoReclamos.html", datos)

