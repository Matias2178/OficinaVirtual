from django.db import models
from OficinaVirtualApp.models import Suministro, Cliente

# Create your models here.
class Deuda (models.Model):
    TIPO =[
        ("FAC", "Factura"),
        ("DEU", "Deuda"),
        ("CPP", "Cuota Plan de Pagos"),
        ("PPA", "Plan de Pagos Anulado"),
    ]
    ESTADO =[
        ("PEN", "Pendiente"),
        ("CAN", "Cancelada"),
        ("ANU", "Anulada"),
        ("PPA", "En Proceso de Pago"),
    ]
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    documento = models.CharField(max_length = 30)
    vencimiento = models.DateField()
    importe = models.CharField(max_length = 10)
    factura = models.CharField(max_length = 30)
    estado = models.CharField(max_length=3, choices= ESTADO)
    tipo = models.CharField(max_length=3, choices= TIPO)
    
    def __str__(self):
        return '{} '.format(self.documento)
    
class Convenio (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    fecha_generacion = models.DateField()
    importe = models.CharField(max_length = 10)
    cuotas = models.IntegerField()
    importe_cuota = models.CharField(max_length = 10)
    prox_vencimiento = models.DateField( )
    cuotas_pagadas = models.IntegerField()
    estado = models.CharField(max_length = 10)
    
    def __str__ (self):
        return '{} - ${} Cuotas: {}/{}' .format(self.cliente, self.importe, self.cuotas_pagadas, self.cuotas)
    