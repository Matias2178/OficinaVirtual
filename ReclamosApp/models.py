from django.db import models
from OficinaVirtualApp.models import Cliente, Suministro

# Create your models here.
class Reclamos (models.Model):
    RECLAMO = [
        ('SER', 'Sin Servicio'),
        ('VAR', 'Variaciones de Tension'),
        ('PEL', 'Peligro Via Publica'),
        ('FAC', 'Error Facturacion'),
        ('DSC', 'Discrepancia Consumo'),
        ('PRE', 'Pago Repetido'),
        ('PVH', 'Pago a Valor Historico'),   
        ('PNA', 'Pago no Acreditado'),
        ('RLQ', 'Reenvio Liquidacion'),
        ('LNR', 'Liquidacion No Recibida'),
        ('CPP', 'Consulta Planes de Pago'), 
    ]
    
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    tipo_reclamo =  models.CharField(max_length=3, choices= RECLAMO)
    detalle = models.TextField()
    alta = models.DateTimeField(auto_now_add = True, blank = True)
    imagen1 = models.ImageField(upload_to= 'reclamos')
    imagen2 = models.ImageField(upload_to= 'reclamos')

class Seguimiento (models.Model):
    reclamo = models.ForeignKey(Reclamos, on_delete = models.CASCADE, blank=True, null=True )
    fecha_novedad = models.DateTimeField(blank = True)
    area = models.CharField(max_length=10)
    observaciones = models.TextField()
    estado = models.CharField(max_length=10)