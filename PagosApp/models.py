from django.db import models
from OficinaVirtualApp.models import Suministro, Cliente
# Create your models here.
class Boton_Pago(models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    importe = models.CharField(max_length = 10)
    fecha_pago = models.DateField()
    medio_pago = models.CharField(max_length = 10)
    estado = models.CharField(max_length = 10)
    
    
class Pagos (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    factura = models.CharField(max_length = 20)
    fecha_pago = models.DateField()
    importe = models.CharField(max_length = 20)
    medio_pago = models.CharField(max_length = 20)
    operacion = models.IntegerField()
  
class Debito_Automatico(models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    tarjeta = models.CharField(max_length = 20)
    banco = models.CharField(max_length = 20)
    nombre = models.CharField(max_length = 80)
    vencimiento = models.DateField()
    estado = models.CharField(max_length = 20)

    
    