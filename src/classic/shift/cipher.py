## Module for cipher and decipher logic
from .analysis import *
from .keygen import *


def revisar_clave(clave):
    if not clave:
        clave = generate_key()
    elif not clave.isdigit():
        clave = generate_key()
    else:
        clave = int(clave)
    return clave


#def cifrado_desplazamiento(clave, mensaje):
#    # en lugar de modulo 26, que trabaje con mod 256(ascii)
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

#def attack(texto_cifrado):
#    lista_attack = []
#    for i in range(25):
#        des = descifrado_desplazamiento(str(i), texto_cifrado)
#
#        lista_attack.append({"clave": str(i), "texto_descifrado": des[0]})
#    return lista_attack
#


def cifrado_desplazamiento(texto, clave):
    clave = revisar_clave(clave)
    resultado = ""

    for char in texto:
        resultado += chr((ord(char) + clave) % 256)

    return resultado



def descifrado_desplazamiento(texto_cifrado, clave):
    clave = revisar_clave(clave)
    return cifrado_desplazamiento(texto_cifrado, -clave)


def attack(texto_cifrado):
    for desplazamiento in range(1, 257):  # Rango completo de ASCII extendido
        texto_descifrado = descifrado_desplazamiento(texto_cifrado, desplazamiento)
        print(f"Intento con desplazamiento {desplazamiento}: {texto_descifrado}")