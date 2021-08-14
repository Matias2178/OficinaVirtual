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
from django.urls import path, include
from UsuarioApp import views 
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', LoginView.as_view(template_name='UsuarioApp/index.html'),name='login'),
    path('registrar/', views.RegistroUsuario.as_view(), name="registrar"),
    path('reset/pasword_reset', PasswordResetView.as_view(template_name = 'UsuarioApp/password_reset_form.html',
                                                          email_template_name=  'registration/password_reset_email.html'),
         name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='UsuarioApp/password_reset_done.html')
         ,name='password_reset_done'),
   # path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
   #      PasswordResetConfirmView(template='UsuarioApp/password_reset.html'),
   #      name='password_reset_confirm'),
#re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
 #           auth_views.PasswordResetConfirmView.as_view(
 #               template_name='accounts/password_reset_confirm.html'),
  #          name='password_reset_confirm'),
  #  path(r'^reset/done', PasswordResetConfirmView(template='UsuarioApp/password_reset_complete.html'),
  #       name= 'password_reset_complete'),

    ]


