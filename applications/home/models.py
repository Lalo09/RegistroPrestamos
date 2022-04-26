from django.db import models

class Persona(models.Model):
    full_name = models.CharField('nombres',max_length=50)
    pais = models.CharField('Pais',max_length=30)
    pasaporte = models.CharField('Pasaporte',max_length=56)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo',max_length=10)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'
        unique_together = ['apelativo','pais']
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18),name="edad_mayor_18")
        ]
        #abstract = True #No crear tabla, solamente se usa para herencia

    def __str__(self):
        return self.full_name
   
#Uso de herencia
class Empleados(Persona):
    empleo = models.CharField('Empleo', max_length=55)

class Cliente(Persona):
    empleo = models.CharField('email', max_length=55)

