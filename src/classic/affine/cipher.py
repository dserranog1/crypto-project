import numpy as np
from .keygen import *
import re

# alfabeto
letras = "abcdefghijklmnopqrstuvwxyz"
num = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
]
alfabeto = list(zip(letras, num))


def relativos(x, y):
    n = np.max([x, y])
    m = np.min([x, y])
    while m > 0:
        t = n % m
        n = m
        m = t
    if n == 1:
        return True
    else:
        return False


def transformar(texto):
    texto = texto.lower()
    trans = []
    for k in texto:
        for i in alfabeto:
            if i[0] == k:
                trans.append(i[1])
    return trans


def transformar_inverso(trans):
    texto = ""
    for k in trans:
        for i in alfabeto:
            if i[1] == k:
                texto = texto + i[0]
    return texto


def cifrado_afin(clave_afin, texto):
    texto = texto.split()
    numeros_encontrados = re.findall(r"\d+", clave_afin)
    numeros_separados_por_espacios = " ".join(numeros_encontrados)
    clave_afin = numeros_separados_por_espacios
    if not validate_key(clave_afin):
        # despues de 3 intentos con clave invalida, generar una aleatoria
        # clave invalida: no son primos relativos
        clave_afin = generate_key()
    elif len(clave_afin) == 0:
        clave_afin = generate_key()
    clave_afin = clave_afin.split()
    clave_afin[0] = int(clave_afin[0])
    clave_afin[1] = int(clave_afin[1])
    lista = []
    for k in texto:
        lista.append(transformar(k))
    for k in lista:
        for i in range(len(k)):
            k[i] = (clave_afin[0] * k[i] + clave_afin[1]) % 26
    texto_cifrado = ""
    for k in range(len(lista)):
        lista[k] = transformar_inverso(lista[k])
        texto_cifrado = texto_cifrado + lista[k] + " "
    return texto_cifrado, clave_afin


def descifrado_afin(clave_afin, texto_cifrado):
    texto_cifrado = texto_cifrado.split()
    numeros_encontrados = re.findall(r"\d+", clave_afin)
    numeros_separados_por_espacios = " ".join(numeros_encontrados)
    clave_afin = numeros_separados_por_espacios
    clave_afin = clave_afin.split()
    clave_afin[0] = int(clave_afin[0])
    clave_afin[1] = int(clave_afin[1])
    lista = []
    if not validate_key(clave_afin):
        clave_afin = generate_key()
    elif len(clave_afin) == 0:
        clave_afin = generate_key()
    # busquemos el inverso de a
    for j in range(2, 26):
        if clave_afin[0] * j % 26 == 1:
            inver = j
            break
    for k in texto_cifrado:
        lista.append(transformar(k))
    for k in lista:
        for i in range(len(k)):
            k[i] = (inver * (k[i] - clave_afin[1])) % 26
    texto = ""
    for k in lista:
        texto = texto + transformar_inverso(k) + " "
    return texto, clave_afin
