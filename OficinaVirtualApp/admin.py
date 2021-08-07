from django.contrib import admin
from OficinaVirtualApp.models import Cliente, Suministro, Turno

class ClienteAdmin (admin.ModelAdmin):
    list_display =  ("apellido", "nombre", "calle", "numero" )
    search_fields = ("apellido", "nombre")


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Suministro)
admin.site.register(Turno)






