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
from LiquidacionConveniosApp import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('liquidacionDeuda/', login_required(views.liquidacionDeuda), name="liquidacionDeuda"),
    path('plandepago/', login_required(views.PlanDePago), name="plandepago"),
    path('convenioPago/', login_required(views.convenioPago), name="convenioPago"),
    path('convenios/', login_required(views.convenios), name = "convenios"),
    path('convenioAceptar/', login_required(views.aceptarConvenio), name = "aceptarConvenio"),
    ]

