import random

max_tamaño=8
def generate_key(max_tamaño):
    tamaño = random.randint(1, max_tamaño)
    numeros_disponibles = list(range(1, tamaño + 1))
    lista_aleatoria = random.sample(numeros_disponibles, tamaño)
    return lista_aleatoria
