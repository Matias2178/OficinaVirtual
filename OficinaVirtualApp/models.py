from django.db import models

# Create your models here.
class Clientes (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()
    piso = models.IntegerField()
    depto = models.CharField(max_length=2)
    barrio = models.CharField(max_length=20)
    tipoDni = models.CharField(max_length=3)
    dni = models.IntegerField()
    email = models.EmailField(max_length=50)
    factura = models.BooleanField(default=False)
    password = models.Password


class Suministro (models.Model):
    suministro = models.IntegerField()
    calle = models.charField(max_length=30)
    numero = models.IntegerField()
    piso = models.IntegerField()
    depto = models.CharField(max_length=2)
    barrio = models.CharField(max_length=20)
    tipoConsumo = models.CharField(max_length=10)
    demanda = models.CharField(max_length= 20)
    estado = models.IntegerField()
    



