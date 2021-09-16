from django.db import models
from OficinaVirtualApp.models import Cliente
from django.contrib.auth.models import User

# Create your models here.
class Alerta (models.Model):
    ORIGEN = [
        ("FAC", "Facturacion"),
        ("SER", "Servicio"),
        ("PAU", "Pagos Automatico"),
        ("GES", "Gestion"),
        ("ADM", "Administracion"),
    ]
    MOTIVO = [
        ("FAC", "Factura"),
        ("VEN", "Vencimiento"),
        ("DEU", "Deuda"),
        ("CDS", "Corte de Servicio"),
        ("PPV", "Plan de Pagos Vencido"),
        ("PDA", "Pago Debito Automatico"),
        ("BDA", "Baja Debito Automatico"),
        ("DAV", "Debito Automatico Vencido")
    ]
    ESTADO = [
        ("EMI", "Emitido"),
        ("VIS", "Visto"),
        ("ACE", "Aceptado"),
    ]
    cliente = models.ForeignKey(User, on_delete= models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    origen = models.CharField(max_length=3, choices= ORIGEN)
    motivo = models.CharField(max_length=3, choices= MOTIVO)
    mensaje = models.TextField()
    estado = models.CharField(max_length=3, choices= ESTADO)
 
    
    def __str__(self):
        return '{} - {} - {} - {}' .format(self.cliente, self.fecha, self.origen, self.motivo)
    
class Aviso (models.Model):
    titulo = models.CharField(max_length = 40)
    cuerpo = models.TextField()
    publicacion = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to = 'avisos')
    
    def __str__(self):
        return '{} '.format(self.titulo)
    