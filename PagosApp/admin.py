from django.contrib import admin
from PagosApp.models import Pagos, Cupon_Pago, Debito_Automatico

# Register your models here.

admin.site.register(Pagos)
admin.site.register(Cupon_Pago)
admin.site.register(Debito_Automatico)