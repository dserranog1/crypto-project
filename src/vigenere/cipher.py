# Module for cipher and decipher logic

from vigenere.analysis import *
from vigenere.keygen import *

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cifrado_vigenere(clave, mensaje): #Necesita 2 argumentos digitados por el usuario

  mensaje = eliminar_caracteres_invalidos(mensaje) #Se trabaja todo en mayúsculas y sin caracteres especiales ·$%/(?= ' '
  clave = eliminar_caracteres_invalidos(clave)
  
  if len(clave) == 0:
    clave = generar_clave()

  mensaje_cifrado = '' #Se parte de un string vacío

  clave_repetida = clave * (len(mensaje) // len(clave) + 1) #Cuántas veces se repite la clave en el mensaje en claro

  for letra_mensaje, letra_clave in zip(mensaje, clave_repetida):
    posicion_mensaje = alfabeto.find(letra_mensaje) #Son las posiciones de cada letra en el mensaje 
    posicion_clave = alfabeto.find(letra_clave) + 1 #Y en la clave, para poder sumarlas en la siguiente variable

    posicion_cifrada = posicion_mensaje + posicion_clave % len(alfabeto) - 26 if posicion_mensaje + posicion_clave >= len(alfabeto) else posicion_mensaje + posicion_clave

    mensaje_cifrado += alfabeto[posicion_cifrada] #Se busca el índice en el alfabeto y se van sumando en el string vacío

  return mensaje_cifrado, clave


def descifrado_vigenere(clave, mensaje_cifrado): #Análogamente funciona esta función al cifrado

  mensaje = eliminar_caracteres_invalidos(mensaje) #Se trabaja todo en mayúsculas y sin caracteres especiales ·$%/(?= ' '
  clave = eliminar_caracteres_invalidos(clave)
  
  if len(clave) == 0:
    clave = generar_clave()

  mensaje_claro = ''
  clave_repetida = clave * (len(mensaje_cifrado) // len(clave) + 1)

  for letra_cifrada, letra_clave in zip(mensaje_cifrado, clave_repetida):
    posicion_cifrada = alfabeto.find(letra_cifrada)
    posicion_clave = alfabeto.find(letra_clave) + 1

    posicion_descifrada = posicion_cifrada - posicion_clave % len(alfabeto) + 26 if posicion_cifrada - posicion_clave < 0 else posicion_cifrada - posicion_clave
    #En la variable anterior se hace las operaciones inversas, para descrifrar el mensaje

    mensaje_claro += alfabeto[posicion_descifrada]
    
  return mensaje_claro, clave
  
