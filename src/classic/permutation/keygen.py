import random


def generate_key():
    tamaño = random.randint(1, 8)
    numeros_disponibles = list(range(1, tamaño + 1))
    lista_aleatoria = random.sample(numeros_disponibles, tamaño)
    return lista_aleatoria
