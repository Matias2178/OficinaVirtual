from django.contrib import admin
from PagosApp.models import Pagos, Boton_Pago, Debito_Automatico

# Register your models here.

admin.site.register(Pagos)
admin.site.register(Boton_Pago)
admin.site.register(Debito_Automatico)