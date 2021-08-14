from django.shortcuts import render
import json
#from rest_framework.views import APIView

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from UsuarioApp.forms import RegistrarForm


# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = "UsuarioApp/registrar.html"
    form_class = RegistrarForm
    success_url = reverse_lazy('UsuarioApp:login')
