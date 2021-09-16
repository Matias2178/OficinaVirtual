from django.db import models
from OficinaVirtualApp.models import Suministro
from django.contrib.auth.models import User
# Create your models here.
class Cupon_Pago(models.Model):
    ESTADO =[
        ("PEN", "Pendiente de Pago"),
        ("PAG", "Pagado"),
        ("VEN", "Plan de Pagos Vencido"),
        ("APU", "Anulado por Usuario"),
    ]
    MEDIO_PAGO = [
        ("TJC", "Tarjeta de Credito"),
        ("EFT", "Efectivo"),
        ("SNP", "Sin pago ") 
     ]
    cliente = models.ForeignKey(User, on_delete= models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add = True)
    fecha_vencimiento = models.DateTimeField()
    importe = models.FloatField()
    fecha_pago = models.DateTimeField(blank=True, null= True)
    medio_pago =models.CharField(max_length=3, choices= MEDIO_PAGO)
    estado = models.CharField(max_length=3, choices= ESTADO)
    
    
class Pagos (models.Model):
    cliente = models.ForeignKey(User, on_delete= models.CASCADE)
    suministro = models.IntegerField()
    factura = models.CharField(max_length = 20)
    fecha_pago = models.DateField()
    importe = models.FloatField()
    medio_pago = models.CharField(max_length = 20)
    operacion = models.IntegerField()
  
class Debito_Automatico(models.Model):
    TARJETAS = [
        ("VSC", "VISA – TARJETA DE CRÉDITO"), 
        ("VSD", "VISA - TARJETA DE DÉBITO"),
        ("MTC", "MAESTRO - TARJETA DE CREDITO"),
        ("MTD", "MAESTRO - TARJETA DE DÉBITO"),
        ("MCR", "MASTERCARD"), 
    ]
    ESTADO = [
        ("ACT", "ACTIVO"),
        ("CAN", "CANCELADA"),
        ("VEN", "VENCIDA"),
    ]
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    tarjeta = models.CharField(max_length=3, choices= TARJETAS)
    banco = models.CharField(max_length = 80)
    nombre = models.CharField(max_length = 80)
    numero_tarjeta = models.BigIntegerField()
    vencimiento = models.DateField()
    alta = models.DateTimeField(auto_now_add = True)
    baja = models.DateTimeField(blank=True, null= True)
    estado = models.CharField(max_length=3, choices= ESTADO)
    
    def __str__(self):
        return '({}) - {} - {} - {} - {} ({})' .format(self.pk, self.suministro, self.tarjeta, self.banco, self.vencimiento, self.estado)

    
    