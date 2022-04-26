from unittest import result
from django.db import models
from django.db.models import Q, Count, Avg

class PrestamoManager():
    """Procedimiento para prestamos"""

    #Edades promedio del lector por edad
    def libro_promedio_edades(self):
        resultado = self.filter(
            libro_id='15'
        ).aggregate(
            promedio_edad=Avg('lector__edad')
        )
        return resultado