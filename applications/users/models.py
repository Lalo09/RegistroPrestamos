from email.policy import default
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):

    GENDER_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino'),
    )

    username = models.CharField(max_length=10,unique=True)
    email = models.EmailField() #Poner correo unique=True para que no se repita
    nombres = models.CharField(max_length=30,blank=True)
    apellidos = models.CharField(max_length=30,blank=True)
    genero = models.CharField(max_length=1,choices=GENDER_CHOICES)
    codigo = models.CharField(max_length=6,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username' #Campo obligatorio

    REQUIRED_FIELDS = ['email']

    objects =  UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres +' '+ self.apellidos