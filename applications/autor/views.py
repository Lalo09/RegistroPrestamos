from pickle import GET
from django.shortcuts import render

from django.views.generic import ListView

from .models import Autor

class ListAutores(ListView):
    context_object_name = "lista_autores"
    template_name = "autor/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword',)
        
        """Test de consultas"""
        #return Autor.objects.listar_autores() #Mandar a llamar el Manager
        #return Autor.objects.buscar_autor(palabra_clave) 
        #return Autor.objects.buscar_autor_or(palabra_clave) 
        #return Autor.objects.buscar_autor_exclude(palabra_clave) 
        return Autor.objects.buscar_autor_edades(palabra_clave)
