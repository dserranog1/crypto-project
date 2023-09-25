# Module for crypto analysis

import re

def restar_uno_a_clave(lista):
    resultado = [x - 1 for x in lista]
    return resultado



def eliminar_espacios(mensaje):
    mensaje_sin_espacios = mensaje.replace(" ", "")
    return mensaje_sin_espacios

def eliminar_especiales_y_numeros(frase):
    # Utilizamos una expresión regular para encontrar todos los caracteres que no son letras
    # y los reemplazamos por una cadena vacía
    frase_limpia = re.sub(r'[^a-zA-Z ]', '', frase)
    return frase_limpia

def crear_subpalabras(palabra,clave):
    subpalabras = []
    for i in range(0, len(palabra), len(clave)):
        subpalabra = palabra[i:i+len(clave)]
        subpalabras.append(subpalabra)
    return subpalabras


def permutacion(clave):
  diccionario={}
  for i in range(len(clave)):
    diccionario[clave[i]] = i
  return diccionario


def cifrado(lista_subpalabras, diccionario):

 lista_cifrada=[]

 for subpalabra in lista_subpalabras:

    subpalabracifrada=""

    for i in range (len(diccionario)):

      if len(subpalabra)> len(diccionario):
        subpalabracifrada = subpalabracifrada + subpalabra[diccionario[i]]


      else:
          if len(subpalabra) > diccionario[i]:
            subpalabracifrada = subpalabracifrada + subpalabra[diccionario[i]]
          else:
            subpalabracifrada = subpalabracifrada + 'x'


    lista_cifrada.append(subpalabracifrada)

 return lista_cifrada


def concatenar_listas_encriptadas(lista_subpalabras):
  resultado=''
  for subpalabra in lista_subpalabras:

     resultado= resultado + subpalabra
  return resultado



# desencriptar:

def permutacion_desencriptar(clave):
  diccionario={}
  for i in range(len(clave)):
    diccionario[i] = clave[i]
  return diccionario

