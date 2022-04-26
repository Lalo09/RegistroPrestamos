#Improtaciones de python
from datetime import date

#Importaciones de django
from .forms import PrestamoFrom,MultiplePrestamoFrom
from django.views.generic.edit import FormView

#Importaciones internas
from .models import Prestamo

class RegistrarPRestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoFrom
    success_url = '.'

    def form_valid(self,form):

        """
        Prestamo.objects.create(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo= date.today(),
            devuelto = False
        )
        """

        prestamo = Prestamo(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo= date.today(),
            devuelto = False
        )

        prestamo.save()

        #Proceso de actualizar en stock
        """
        libro = form.cleaned_data['libro']
        libro.stock = libro.stock -1
        libro.save()
        """

        return super(RegistrarPRestamo,self).form_valid(form)

class RegistrarMultiplePrestamo(FormView):
    template_name = 'lector/add_multiple_prestamo.html'
    form_class = MultiplePrestamoFrom
    success_url = '.'

    def form_valid(self,form):

        #Ver lo que se envia en el formulario
        print(form.cleaned_data['lector'])
        print(form.cleaned_data['libros']) #Esto recoje una lista entonces para guardar hay que iterarla

        #Iterar lista para guardar
        prestamos = []
        for l in form.cleaned_data['libros']:
            prestamo = Prestamo(
                lector=form.cleaned_data['lector'],
                libro=l,
                fecha_prestamo= date.today(),
                devuelto = False
            )

            prestamos.append(prestamo)

        Prestamo.objects.bulk_create(
            prestamos 
        )

        return super(RegistrarMultiplePrestamo,self).form_valid(form)
