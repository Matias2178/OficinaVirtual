from django.db import models
from OficinaVirtualApp.models import Suministro

# Create your models here.
class Factura (models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    detalle_documento = models.CharField(max_length = 20)
    vencimiento_pri = models.DateField()
    importe_pri = models.CharField(max_length = 10)
    vencimiento_seg = models.DateField()
    importe_seg = models.CharField(max_length = 20)
    documento = models.BinaryField()

class Consumo (models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    periodo = models.DateField()
    consumo = models.IntegerField()
    
