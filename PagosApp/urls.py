"""OficinaVirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from PagosApp import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('botonPago/', login_required(views.botonPago), name="botonPago"),
    path('debitoAutomatico/', login_required(views.debitoAutomatico), name="debitoAutomatico"),
    path('bajaDebitoAutomatico/', login_required(views.bajaDebitoAutomatico), name="bajaDebitoAutomatico"),
    ]

