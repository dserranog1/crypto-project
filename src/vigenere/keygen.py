# Module for key generation

from random import randint

lista_claves = ['eagle', 'house', 'horse', 'heaven', 'rat', 'hell', 'esplendor', 'thisisnotakey', 'airplane', 'toronja']

def generar_clave():
  clave = lista_claves[randint(0, len(lista_claves))]
  return clave
