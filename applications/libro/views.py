from cgitb import html
from django.shortcuts import render

from django.views.generic import ListView,DetailView

from .models import Libro

class ListLibros(ListView):

    context_object_name = "lista_libros"
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword',)

        #fecha inicio
        f1 = self.request.GET.get('fecha1',)
        #fecha fin
        f2 = self.request.GET.get('fecha2',)

        if not palabra_clave:
            palabra_clave = ""
        
        if f1 and f2:
            return Libro.objects.buscar_libro_por_fechas(palabra_clave,f1,f2)
        else:
            return Libro.objects.buscar_libro(palabra_clave)

class ListLibrosCategoria(ListView):
    
    context_object_name = "lista_libros"
    template_name = "libro/lista-libro-categoria.html"

    def get_queryset(self):
        param=4
        return Libro.objects.listar_libros_categoria(param)

class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"