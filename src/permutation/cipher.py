from permutation.analysis import *
from permutation.keygen import *



def validar_lista_numeros(lista):
    # Verificar que todos los elementos sean números y estén en el rango [1, len(lista)]
    n = len(lista)
    numeros_validos = set(range(1, n + 1))

    for elemento in lista:
        if not isinstance(elemento, int) or elemento not in numeros_validos:
            return False

    # Verificar que no haya números repetidos
    if len(lista) != len(set(lista)):
        return False

    return True

def revisar_clave(clave):
    if not clave:
        clave = generate_key()
    elif not isinstance(clave, list):
        clave = generate_key() 
    elif not validar_lista_numeros:
        clave = generate_key() 
    return clave



def cifrado_permutacion(texto, clave_permutacion):
  clave_permutacion = revisar_clave(clave_permutacion)
  return concatenar_listas_encriptadas(cifrado(crear_subpalabras(eliminar_especiales_y_numeros(eliminar_espacios(texto)),restar_uno_a_clave(clave_permutacion)),permutacion(restar_uno_a_clave(clave_permutacion)))),clave_permutacion


def descifrado_permutacion(texto, clave_permutacion):
  clave_permutacion = revisar_clave(clave_permutacion)
  return concatenar_listas_encriptadas(cifrado(crear_subpalabras(texto,clave_permutacion),permutacion_desencriptar(restar_uno_a_clave(clave_permutacion)))),clave_permutacion