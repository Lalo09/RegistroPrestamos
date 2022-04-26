from distutils.command.upload import upload
from pickletools import optimize
from tabnanny import verbose
from django.db.models.signals import post_save
from django.db import models
from applications.autor.models import Autor
from PIL import Image

from .managers import LibroManager,CategoriaManager #Importar manager

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    object = CategoriaManager()

    def __str__(self):
        return str(self.id)+"-"+self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name='categoria_libro') #Referencia a llave foranea
    autores = models.ManyToManyField(Autor) #Relacion muchos a muchos
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portadas')
    mpi = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    objects = LibroManager() #Enlazar con manager

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo','fecha']

    def __str__(self):
        return  str(self.id) +" "+ self.titulo

##Tema de signal, Son Tiggers
def optimized_image(sender,instance,**kwargs):
        print("=========")
        print(instance)
        if instance.portada:
            portada = Image.open(instance.portada.path)
            portada.save(instance.portada.path,quality=20,optimize=True)

post_save.connect(optimized_image,sender=Libro)
    
    
