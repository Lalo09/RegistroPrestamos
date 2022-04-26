from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('applications.autor.urls')), #URL de aplicacion de autor
    re_path('',include('applications.libro.urls')), #URL de aplicacion de libro
    re_path('',include('applications.lector.urls')), #URL de aplicacion de lector,prestamos
    re_path('',include('applications.users.urls')), #URL de aplicacion de usuarios
    re_path('',include('applications.home.urls')), #URL de aplicacion de usuarios
]
