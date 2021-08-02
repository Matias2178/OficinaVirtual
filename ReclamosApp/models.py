from django.db import models
from OficinaVirtualApp.models import Cliente, Suministro

# Create your models here.
class Reclamos (models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    tipo_reclamo = models.CharField(max_length = 10)
    observaciones = models.TextField()
    archivo1 = models.CharField(max_length = 10)
    archivo2 = models.CharField(max_length = 10)

class Seguimiento (models.Model):
    reclamo = models.ForeignKey(Reclamos, on_delete = models.CASCADE, null=True)
    fecha_novedad = models.DateTimeField()
    area = models.CharField(max_length = 10)
    observaciones = models.TextField()
    estado = models.CharField(max_length = 10)
    