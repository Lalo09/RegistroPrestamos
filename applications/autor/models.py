from django.db import models

from .managers import AutorManager #Importar manager

class Autor(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()

    objects = AutorManager() #Enlazar con manager

    def __str__(self):
        return self.nombres +" "+self.apellidos