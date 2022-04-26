from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """Managers para el modelo autor"""

    #Mostrar todos los autores
    def listar_autores(self):
        return self.all()

    #Buscar un autor por nombre, filtro basico
    def buscar_autor(self,kword):
        resultado = self.filter(
            nombre__icontains=kword
        )
        return resultado

    #Buscar autor por nombre o por apellido, uso de or
    def buscar_autor_or(self,kword):
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        )
        return resultado

    #Filtrar todo a excepcion de los que tengan 35 años, uso de exclude
    def buscar_autor_exclude(self,kword):
        resultado = self.filter(
            nombre__icontains=kword
        ).exclude(edad=50)
        return resultado

    #Buscar un autor por edades, uso de mayor que y menor que
    def buscar_autor_edades(self,kword):
        resultado = self.filter(
            edad__gt=30,
            edad__lt=65
        ).order_by('nombre','apellidos')
        return resultado    

    #Funciones de documentacion
    """
    https://docs.djangoproject.com/en/3.0/ref/models/querysets/
    """

    