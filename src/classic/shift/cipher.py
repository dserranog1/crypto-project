### Module for cipher and decipher logic
from .analysis import *
from .keygen import *
#
#
#def revisar_clave(clave):
#    if not clave:
#        clave = generate_key()
#    elif not clave.isdigit():
#        clave = generate_key()
#    else:
#        clave = int(clave)
#    return clave
#
#
#def cifrado_desplazamiento(clave, mensaje):
#    clave = revisar_clave(clave)
#    return (
#        convertir_letras(
#            cifrado_clave(
#                clave,
#                convertir_numeros(
#                    eliminar_espacios(
#                        eliminar_especiales_y_numeros(mayusculas(mensaje))
#                    )
#                ),
#            )
#        ),
#        clave,
#    )
#
#
#def descifrado_desplazamiento(clave, mensaje):
#    clave = revisar_clave(clave)
#    return (
#        convertir_letras(
#            descifrado_clave(
#                clave,
#                convertir_numeros(
#                    eliminar_espacios(
#                        eliminar_especiales_y_numeros(mayusculas(mensaje))
#                    )
#                ),
#            )
#        ),
#        clave,
#    )
#
#
#def attack(texto_cifrado):
#    lista_attack = []
#    for i in range(25):
#        des = descifrado_desplazamiento(str(i), texto_cifrado)
#
#        lista_attack.append({"clave": str(i), "texto_descifrado": des[0]})
#    return lista_attack
#
#
#
#
#

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
    desplazamiento =  revisar_clave(desplazamiento_str)
    resultado = ""
    for char in texto:
        resultado += chr((ord(char) + desplazamiento) % 256)

    return (resultado, desplazamiento)

def descifrado_desplazamiento(desplazamiento_str, texto_cifrado):
    desplazamiento =  revisar_clave(desplazamiento_str)
    resultado = ""
    for char in texto_cifrado:

            resultado += chr((ord(char) - desplazamiento) % 256)

    return (resultado, desplazamiento)


def attack(texto_cifrado):
    for desplazamiento in range(1, 257):  # Rango completo de ASCII extendido
        texto_descifrado, clave_descifrado = descifrado_desplazamiento(str(desplazamiento), texto_cifrado)
        print(f"Intento con desplazamiento {clave_descifrado}: {texto_descifrado}")