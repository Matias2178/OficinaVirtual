from django.db import models

# Create your models here.
#Creacion de todas las tablas necesarias para la base de datos

class Cliente (models.Model):

    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()
    piso = models.IntegerField(blank=True, null=True) #para que no sea un capmo requerido
    depto = models.CharField(max_length=2, blank=True, null=True)
    barrio = models.CharField(max_length=20)
    email = models.EmailField()
    factura = models.BooleanField(default=False)
    password = models.CharField(max_length=20)
    intentos = models.IntegerField()
    caducidad = models.DateField()
    avisos = models.IntegerField(default= 0)
    
    def __str__(self):
        return '{} {}'.format(self.apellido, self.nombre)
    
class Suministro (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null= True)
    suministro = models.IntegerField()
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()
    piso = models.IntegerField(blank=True, null=True)
    depto = models.CharField(max_length=2, blank=True, null=True)
    barrio = models.CharField(max_length=20)
    tipo_consumo = models.CharField(max_length=20)
    demanda = models.CharField(max_length= 20)
    estado = models.IntegerField()
    
    
    def __str__(self):
         return '{} - {} - {} {}'.format(self.suministro, self.cliente, self.calle, self.numero)
  
class Turno (models.Model):
    apellido = models.CharField(max_length = 20)
    nombre = models.CharField(max_length =20)
    turno = models.DateTimeField()
    motivo = models.CharField(max_length = 30)
    estado = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.turno, self.apellido, self.nombre, self.motivo, self.estado
    



     

        
    
    