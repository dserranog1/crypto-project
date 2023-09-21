# Module for crypto analysis


from analysis import *

def cifrado_desplazamiento(clave, mensaje_numeros):
  lista_cifrada=[]

  for i in range (len(mensaje_numeros)):
    lista_cifrada.append((mensaje_numeros[i]+clave)%26)
  return lista_cifrada




def descifrado_desplazamiento(clave, mensaje_numeros):
  lista_descifrada=[]

  for i in range (len(mensaje_numeros)):
    lista_descifrada.append((mensaje_numeros[i]-clave)%26)
  return lista_descifrada

