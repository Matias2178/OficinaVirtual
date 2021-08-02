from django.db import models
from OficinaVirtualApp.models import Cliente

# Create your models here.
class Alerta (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    fecha = models.DateField()
    origen = models.CharField(max_length = 20)
    motivo = models.CharField(max_length = 20)
    mensaje = models.CharField(max_length = 100)
    estado = models.CharField(max_length = 10)

class Aviso (models.Model):
    titulo = models.CharField(max_length = 20)
    cuerpo = models.TextField()
    publicacion = models.DateField()
    imagen = models.CharField(max_length = 20)
    