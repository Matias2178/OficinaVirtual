from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from OficinaVirtualApp.forms import ClienteForm
from OficinaVirtualApp.models import Cliente
from django.contrib.auth.models import User
from UsuarioApp.forms import RegistrarForm

def principal(request):
    usuario = request.user.pk 
    return render(request, "OficinaVirtualApp/principal.html",{"usuario": usuario})

def datosPersonales(request):
    usuario_id = request.user
    datos =  User.objects.values().filter(id = usuario_id.id) 
    clt = Cliente.objects.values().filter(usuario = usuario_id)
    print(clt)
    if not clt:
        cliente = Cliente(
            usuario = usuario_id,
            calle = ' ',
            numero = 0,
            piso = 0,
            depto = '',
            barrio = ' ',
            factura = False
        )
        cliente.save()
        clt = Cliente.objects.values().filter(usuario = usuario_id)
    cliente = ClienteForm(clt[0])
    usuarioActual = RegistrarForm(datos[0])  
    informacion = {
        "cliente": cliente,
        'usuario': usuarioActual,
    }
    if request.method== 'POST':
        nombre = request.POST.get('first_name')
        apellido = request.POST.get('last_name')
        correo = request.POST.get('email')
        cal = request.POST.get('calle')
        num = int(request.POST.get('numero'))
        pis = int(request.POST.get('piso'))
        dep = request.POST.get('depto')
        bar = request.POST.get('barrio')
        print("nombe:",nombre, 'apellido:',apellido,'email:', correo,'calle:', cal,'num:', num,'piso', pis,'dep', dep,'barrio', bar)
        User.objects.filter(id = usuario_id.id).update(
            first_name = nombre, 
            last_name = apellido, 
            email = correo)
        Cliente.objects.filter(usuario = usuario_id).update(
            calle = cal, 
            numero = num,
            piso = pis,
            depto = dep,
            barrio = bar)
        
        return render(request, "OficinaVirtualApp/principal.html" )
    return render(request, "OficinaVirtualApp/datosPersonales.html",informacion)

def registro(request):
    return render(request, "OficinaVirtualApp/registroAAA.html")

#class DatosUsuario(CreateView):
    
    




