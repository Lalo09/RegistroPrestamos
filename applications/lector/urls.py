from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(
        'prestamo/add/', 
        views.RegistrarPRestamo.as_view(),
        name='prestamo-add'
    ),
    path(
        'prestamo/plus/add/', 
        views.RegistrarMultiplePrestamo.as_view(),
        name='prestamo-plus-add'
    ),
]