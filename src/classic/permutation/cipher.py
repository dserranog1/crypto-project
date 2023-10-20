from .analysis import *
from .keygen import *


def validar_numeros_de_clave(clave):
    # Verificar que todos los elementos sean números y estén en el rango [1, len(clave)]
    n = len(clave)
    numeros_validos = set(range(1, n + 1))
    for i in range(n):
        if not clave[i].isdigit():
            return False
        clave[i] = int(clave[i])
        if clave[i] not in numeros_validos:
            return False

    # Verificar que no haya números repetidos
    if len(clave) != len(set(clave)):
        return False

    return True


def revisar_clave(clave):
    # La clave se recibe como un cadena de carácteres separada por espacios, la volvemos un arreglo donde c/elemento es un carácter para verificar
    clave = clave.split(" ")
    if not clave:
        clave = generate_key()
    elif not validar_numeros_de_clave(clave):
        clave = generate_key()
    return clave


def cifrado_permutacion(clave_permutacion, texto):
    clave_permutacion = revisar_clave(clave_permutacion)
    return (
        concatenar_listas_encriptadas(
            cifrado(
                crear_subpalabras(
                    eliminar_especiales_y_numeros(eliminar_espacios(texto)),
                    restar_uno_a_clave(clave_permutacion),
                ),
                permutacion(restar_uno_a_clave(clave_permutacion)),
            )
        ),
        clave_permutacion,
    )


def descifrado_permutacion(clave_permutacion, texto):
    clave_permutacion = revisar_clave(clave_permutacion)
    return (
        concatenar_listas_encriptadas(
            cifrado(
                crear_subpalabras(texto, clave_permutacion),
                permutacion_desencriptar(restar_uno_a_clave(clave_permutacion)),
            )
        ),
        clave_permutacion,
    )
