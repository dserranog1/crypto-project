# Module for crypto analysis
import re

# analisis con IA

list_str = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def mayusculas(mensaje):
    mensaje_mayuscula = mensaje.upper()
    return mensaje_mayuscula


def eliminar_espacios(mensaje):
    mensaje_sin_espacios = mensaje.replace(" ", "")
    return mensaje_sin_espacios


def convertir_numeros(mensaje_sin_espacios):
    list_number = []
    for i in mensaje_sin_espacios:
        list_number.append(list_str.index(i))
    return list_number


def convertir_letras(mensaje_desplazado):
    string = ""
    for i in range(len(mensaje_desplazado)):
        string = string + list_str[(mensaje_desplazado[i])]

    return string


def cifrado_clave(clave, mensaje_numeros):
    lista_cifrada = []

    for i in range(len(mensaje_numeros)):
        lista_cifrada.append((mensaje_numeros[i] + clave) % 26)
    return lista_cifrada


def descifrado_clave(clave, mensaje_numeros):
    lista_descifrada = []

    for i in range(len(mensaje_numeros)):
        lista_descifrada.append((mensaje_numeros[i] - clave) % 26)
    return lista_descifrada


def eliminar_especiales_y_numeros(frase):
    # Utilizamos una expresión regular para encontrar todos los caracteres que no son letras
    # y los reemplazamos por una cadena vacía
    frase_limpia = re.sub(r"[^a-zA-Z ]", "", frase)
    return frase_limpia
