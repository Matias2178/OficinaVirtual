from django.db import models
from OficinaVirtualApp.models import Cliente

# Create your models here.
class Alerta (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    origen = models.CharField(max_length = 20)
    motivo = models.CharField(max_length = 20)
    mensaje = models.CharField(max_length = 100)
    estado = models.CharField(max_length = 10)
    
    def __str__(self):
        return '{} - {} - {} - {}' .format(self.cliente, self.fecha, self.origen, self.motivo)
    
class Aviso (models.Model):
    titulo = models.CharField(max_length = 40)
    cuerpo = models.TextField()
    publicacion = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to = 'avisos')
    
    def __str__(self):
        return '{} '.format(self.titulo)
    