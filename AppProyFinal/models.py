from django.db import models

# Create your models here.

class Hotel(models.Model):
    nombre=models.CharField(max_length=40)
    fechaApertura=models.DateField(max_length=40)
    abierto=models.BooleanField()
    estrellas=models.IntegerField()
    ciudad=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    
    def __str__(self):
        return (self.nombre)

class Habitacion(models.Model):
    numero=models.IntegerField()
    piso=models.IntegerField()
    capacidad=models.IntegerField()
    descripcion=models.CharField(max_length=150)
    ocupada=models.BooleanField()
    precio= models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    
    def __str__(self):
        return (str(self.numero) + " " + str(self.hotel))

class Reserva(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    fechaDesde=models.DateField()
    fechaHasta=models.DateField()
    cantPersonas=models.IntegerField()
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    comentarios =models.CharField(max_length=200)
    metodoPago =models.CharField(max_length=200)
    
    
    def __str__(self):
        return (str(self.nombre) + " " + str(self.apellido) + " " + str(self.fechaDesde))
