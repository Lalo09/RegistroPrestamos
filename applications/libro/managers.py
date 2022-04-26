import datetime
from django.db import models
from django.db.models import Q, Count

class LibroManager(models.Manager):
    """Managers para el modelo libro"""

    #Listar todos los libros
    def buscar_libro(self,kword):

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2022-01-01','2022-04-08')
        )
        return resultado

    #Listar libros por rango de fechas
    def buscar_libro_por_fechas(self, kword, fecha1, fecha2):
    
        #date1 = datetime.datetime.strptime(fecha1,"%Y-%m-%d").date()
        #date2 = datetime.datetime.strptime(fecha1,"%Y-%m-%d").date()

        resultado = self.filter(
            fecha__range=(fecha1,fecha2)
        )
        return resultado

    #Listar los libros de una categoria
    def listar_libros_categoria(self,categoria):
        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')

    #Añadir un autor al libro
    def add_autor_libro(self,libro_id,autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro

class CategoriaManager(models.Manager):
    """Managers para el modelo autor"""

    def categoria_por_autor(self,autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()

    def listar_categoria_libros(self):
        resultado = self.annotate(
            num_libros = Count('categoria_libro')
        )

        for r in resultado:
            print('*********')
            print(r,r.num_libros)
            
        return resultado