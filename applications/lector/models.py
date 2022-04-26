from django.db import models
from django.db.models.signals import post_delete
from applications.libro.models import Libro
from .managers import PrestamoManager
from .signals import *

class Lector(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombres + " " + self.apellidos
    

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector,on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True,null=True)
    devuelto = models.BooleanField()

    objects =  PrestamoManager()

    def save(self,*args,**kwargs):

        print("=====")
        self.libro.stock = self.libro.stock - 1
        self.libro.save()

        super(Prestamo,self).save(*args,**kwargs)

    def __str__(self):
        return self.libro.titulo + " -> " + self.lector.nombres + " " + self.lector.apellidos

#Ejecutar los triggers desde el archivo signal
post_delete.connect(update_libro_stock, sender=Prestamo)