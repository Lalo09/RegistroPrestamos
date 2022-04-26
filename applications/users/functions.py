#Funciones de la aplicacion users

import random
import string

#Generar codigo de verificacion de registro
def code_generate(size=6, chars=string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))