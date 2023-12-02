### Module for cipher and decipher logic
from .analysis import *
from .keygen import *

import random


def revisar_clave(clave):
    if not clave:
        clave = generate_key()
    elif not clave.isdigit():
        clave = generate_key()
    else:
        clave = int(clave)
    return clave


def generate_key():
    return random.randint(1, 26)


def cifrado_desplazamiento(desplazamiento_str, texto):
    desplazamiento = revisar_clave(desplazamiento_str)
    resultado = ""
    for char in texto:
        resultado += chr((ord(char) + desplazamiento) % 256)

    return (resultado, desplazamiento)


def descifrado_desplazamiento(desplazamiento_str, texto_cifrado):
    desplazamiento = revisar_clave(desplazamiento_str)
    resultado = ""
    for char in texto_cifrado:
        resultado += chr((ord(char) - desplazamiento) % 256)

    return (resultado, desplazamiento)


def attack(texto_cifrado):
    attack_result = ""
    for desplazamiento in range(1, 257):  # Rango completo de ASCII extendido
        texto_descifrado, clave_descifrado = descifrado_desplazamiento(
            str(desplazamiento), texto_cifrado
        )
        attack_result += (
            f"Intento con desplazamiento {clave_descifrado}: {texto_descifrado}"
        ) + "\n"
        print(f"Intento con desplazamiento {clave_descifrado}: {texto_descifrado}")
    return attack_result
