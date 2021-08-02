from django.db import models
from OficinaVirtualApp.models import Suministro, Cliente

# Create your models here.
class Deuda (models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    documento = models.CharField(max_length = 30)
    vencimiento = models.DateField()
    importe = models.CharField(max_length = 10)
    factura = models.CharField(max_length = 30)
    estado = models.CharField(max_length = 20)
    
class Convenio (models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    fecha_generacion = models.DateField()
    importe = models.CharField(max_length = 10)
    cuotas = models.IntegerField()
    