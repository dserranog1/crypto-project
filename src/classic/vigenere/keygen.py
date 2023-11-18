# Module for key generation

import string 
import random
import hashlib


# generar claves completamente aleatorias
def generar_clave():
    
    # Genera un tamaño aleatorio para el texto entre 5 y 20 caracteres
    tamano = random.randint(5, 20)

    # Genera caracteres aleatorios para el texto utilizando el rango de caracteres imprimibles ASCII
    clave_aleatoria = ''.join(random.choice(string.ascii_lowercase) for _ in range(tamano)).upper()

    #hash_clave = hashlib.sha256(clave_aleatoria.encode()).hexdigest()

    return clave_aleatoria #hash_clave
