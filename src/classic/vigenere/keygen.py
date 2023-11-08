# Module for key generation

from random import randint

lista_claves = [
    "EAGLE",
    "HOUSE",
    "HORSE",
    "HEAVEN",
    "RAT",
    "HELL",
    "ESPLENDOR",
    "THISISNOTAKEY",
    "AIRPLANE",
    "TORONJA",
]


# generar claves completamente aleatorias
def generar_clave():
    clave = lista_claves[randint(0, len(lista_claves))]
    return clave
