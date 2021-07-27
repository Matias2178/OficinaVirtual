from django.contrib import admin
from OficinaVirtualApp.models import Cliente, Suministro
# Register your models here.
#Para ver mas campos de los que permite el modelo

#class ClienteAdmin(admin.ModelAdmin):
 #   list_display= ("apellido", "nombre", "calle", "numero", "piso", "depto", "barrio")
 #   spearch_field = ("apellido", "nombre", "calle")
 #   list_filter = ("apellido",) #crea una lista de filtros.
    #date_hireachi = "fecha" # para que se filtre por fechas

#admin.site.register(Cliente, ClienteAdmin)