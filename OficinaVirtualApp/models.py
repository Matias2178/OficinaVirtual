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
    
class Suministro (models.Model):
    suministro = models.IntegerField()
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()
    piso = models.IntegerField(blank=True, null=True)
    depto = models.CharField(max_length=2, blank=True, null=True)
    barrio = models.CharField(max_length=20)
    tipo_consumo = models.CharField(max_length=10)
    demanda = models.CharField(max_length= 20)
    estado = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.suministro
                                
class Factura (models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    num_factura = models.CharField(max_length = 20)
    fecha_primer_ven = models.DateField()
    imp_primer_ven = models.CharField(max_length = 10)
    fecha_seg_ven = models.DateField()
    imp_seg_ven = models.CharField(max_length = 20)
    documento = models.BinaryField()

class Deuda(models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    documento = models.CharField(max_length = 30)
    vencimiento = models.DateField()
    importe = models.CharField(max_length = 10)
    factura = models.CharField(max_length = 30)
    estado = models.CharField(max_length = 20)
    
class Pago(models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    fecha_vencimiento = models.DateField()
    fecha_emision = models.DateField()
    importe = models.CharField(max_length = 10)
    fecha_pago = models.DateField()
    medio_pago = models.CharField(max_length = 10)
    operacion = models.IntegerField()
    estado = models.CharField(max_length = 10)
  
class Consumos(models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    fecha_consumo = models.DateField()
    consumo = models.IntegerField()

class DebitoAutomatico(models.Model):
    suministro = models.ForeignKey(Suministro, on_delete= models.CASCADE)
    tarjeta = models.CharField(max_length = 20)
    banco = models.CharField(max_length = 20)
    nombre = models.CharField(max_length = 80)
    vencimiento = models.DateField()
    estado = models.CharField(max_length = 20)
    
class Trunos (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    fecha = models.DateTimeField()
    motivo = models.CharField(max_length = 30)
    estado = models.CharField(max_length = 20)

class Alertas (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    fecha = models.DateField()
    origen = models.CharField(max_length = 20)
    motivo = models.CharField(max_length = 20)
    mensaje = models.CharField(max_length = 100)
    estado = models.CharField(max_length = 10)
     

        
    
    