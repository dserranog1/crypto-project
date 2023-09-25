from permutation.analysis import *
from permutation.keygen import *

def cifrado_permutacion(texto, clave_permutacion):
  return concatenar_listas_encriptadas(cifrado(crear_subpalabras(eliminar_especiales_y_numeros(eliminar_espacios(texto)),restar_uno_a_clave(clave_permutacion)),permutacion(restar_uno_a_clave(clave_permutacion))))


def descifrado_permutacion(texto, clave_permutacion):

  return concatenar_listas_encriptadas(cifrado(crear_subpalabras(texto,clave_permutacion),permutacion_desencriptar(restar_uno_a_clave(clave_permutacion))))