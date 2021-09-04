from django.db import models
from OficinaVirtualApp.models import Cliente, Suministro
from django.contrib.auth.models import User

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
    alta = models.DateTimeField(auto_now_add = True)
    imagen1 = models.ImageField(upload_to= 'reclamos', blank = True, null=True)
    imagen2 = models.ImageField(upload_to= 'reclamos', blank = True, null = True)

    
    def __str__(self):
        return '{} - {}'.format(self.suministro, self.tipo_reclamo)

class Seguimiento (models.Model):
    AREA = [
        ('REC', 'Recepcion'),
        ('AMD', 'Administracion'),
        ('TEC', 'Area Tecnica'),
        ('FAC', 'Facturacion'),
    ]
    ESTADO = [
        ('REC', 'Recibido'),
        ('PRS', 'En Proceso'),
        ('FIN', 'Finalizado'),
    ]
    reclamo = models.ForeignKey(Reclamos, on_delete = models.CASCADE)
    fecha_novedad = models.DateTimeField()
    area = models.CharField(max_length=3, choices= AREA)
    observaciones = models.TextField()
    estado = models.CharField(max_length=3, choices= ESTADO)
    
    def __str__(self):
        return '{} - {} - {}'.format(self.reclamo, self.fecha_novedad, self.estado)