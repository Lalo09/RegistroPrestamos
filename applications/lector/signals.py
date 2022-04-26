#Triggers

#Trigger para actualizar en stock despues de una devolucion
def update_libro_stock(sender,instance, **kwargs):
    #Actualizar el stock si se elimina un prestamo
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save()