# Module for cipher and decipher logic
import re
from .analysis import *
from .keygen import generate_key


def eliminar_especiales_y_numeros(frase):
    # Utilizamos una expresión regular para encontrar todos los caracteres que no son letras
    # y los reemplazamos por una cadena vacía
    frase_limpia = re.sub(r"[^a-zA-Z ]", "", frase)
    return frase_limpia


def eliminar_espacios(mensaje):
    mensaje_sin_espacios = mensaje.replace(" ", "")
    return mensaje_sin_espacios


def alfabeto_original():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {}
    for k in range(len(letras)):
        dic[letras[k]] = k
    return dic


def dic_clave(input):
    input = eliminar_espacios(input)
    input = eliminar_especiales_y_numeros(input)
    dic = {}
    for k in range(len(input)):
        dic[input[k]] = k
    return dic


def clave_valida(texto):
    # Convierte el texto a minúsculas para asegurarse de manejar mayúsculas y minúsculas de manera uniforme
    texto = eliminar_espacios(texto)
    texto = eliminar_especiales_y_numeros(texto)
    texto = texto.upper()

    # Crea un conjunto de todas las letras del alfabeto
    letras_del_alfabeto = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Convierte el texto en un conjunto de letras únicas
    letras_en_texto = set(texto)

    # Comprueba si el conjunto de letras en el texto es igual al conjunto de todas las letras del alfabeto
    return letras_en_texto == letras_del_alfabeto and len(texto) == 26


def sustitucion_cripter(claves, palabra):
    palabra = eliminar_espacios(palabra)
    palabra = palabra.upper()
    if len(claves) == 0:
        claves = generate_key()
    elif not clave_valida(claves):
        claves = generate_key()
    valores = []
    diccionario = dic_clave(claves)
    claves_encontradas = []
    a = alfabeto_original()
    for letra in palabra:
        if letra in diccionario:
            valores.append(diccionario[letra])
        else:
            valores.append(
                None
            )  # Si la letra no está en el diccionario, puedes manejarlo de acuerdo a tus necesidades
    for i in valores:
        for clave, valor in a.items():
            if valor == i:
                claves_encontradas.append(clave)
    palabra_encriptada = "".join(claves_encontradas)
    return palabra_encriptada, claves


def sustitucion_desencriptar(claves, palabra):
    palabra = eliminar_espacios(palabra)
    palabra = palabra.upper()
    if len(claves) == 0:
        claves = generate_key()
    elif not clave_valida(claves):
        claves = generate_key()
    diccionario = dic_clave(claves)
    valores = []
    claves_encontradas = []
    a = alfabeto_original()
    for letra in palabra:
        if letra in a:
            valores.append(a[letra])
        else:
            valores.append(
                None
            )  # Si la letra no está en el diccionario, puedes manejarlo de acuerdo a tus necesidades
    for i in valores:
        for clave, valor in diccionario.items():
            if valor == i:
                claves_encontradas.append(clave)
    palabra_desencriptada = "".join(claves_encontradas)
    return palabra_desencriptada, claves
