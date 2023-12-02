## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key
import numpy as np
import ast


def _decompose(number):
    """Generate digits from `number` in base alphabet, least significants
    bits first.

    Since A is 1 rather than 0 in base alphabet, we are dealing with
    `number - 1` at each iteration to be able to extract the proper digits.
    """
    A_UPPERCASE = ord("A") - 1
    ALPHABET_SIZE = 27

    while number:
        number, remainder = divmod(number - 1, ALPHABET_SIZE)
        yield remainder


def base_26_to_alphabet(number):
    """Convert a decimal number to its base alphabet representation"""
    A_UPPERCASE = ord("A") - 1
    ALPHABET_SIZE = 27
    return "".join(chr(A_UPPERCASE + part) for part in _decompose(number))[::-1]


def base_alphabet_to_26(letters):
    """Convert an alphabet number to its decimal representation"""
    A_UPPERCASE = ord("A") - 1
    ALPHABET_SIZE = 27
    return sum(
        (ord(letter) - A_UPPERCASE + 1) * ALPHABET_SIZE**i
        for i, letter in enumerate(reversed(letters.upper()))
    )


def MCR(numero, potencia, modulo):
    binario = bin(potencia)[2:]
    resultado = 1
    for k in binario:
        if int(k) == 1:
            resultado = ((resultado**2) * numero) % modulo
        else:
            resultado = (resultado**2) % modulo
    return resultado


def texto_a_silabas(texto, a):
    # Eliminar espacios y convertir a mayúsculas
    texto_sin_espacios = texto.replace(" ", "").lower()

    # Crear una lista de sílabas de tres letras
    lista_silabas = [
        texto_sin_espacios[i : i + a] for i in range(0, len(texto_sin_espacios), a)
    ]

    return lista_silabas


def pad_message(message, block_size):
    message_len = len(message)
    return message + "#" * (block_size - message_len)


def invalid_key(key, is_private):

    keys = key.split(" ")

    if is_private and len(keys) == 3:

        k1, k2, k3 = keys
        return k1.isnumeric() and k2.isnumeric() and k3.isnumeric()

    elif not is_private and len(keys) == 2:

        k1, k2 = keys

        return k1.isnumeric() and k2.isnumeric()

    return False


def encriptar(message, clave_publica):
    m = base_alphabet_to_26(message)
    g, p, k = clave_publica
    b = np.random.randint(2, p - 1)
    y1 = MCR(g, b, p)
    y2 = ((pow(k, b)) * m) % p
    encrypted_message = (y1, y2)
    y1_letra = base_26_to_alphabet(y1)
    y2_letra = base_26_to_alphabet(y2)
    encrypted_message = (y1_letra, y2_letra)
    return encrypted_message


def gamal_encrypt(clear_text: str, key: str):
    key = key.split(" ")

    key = (int(key[0]), int(key[1]), int(key[2]))
    clear_text = texto_a_silabas(clear_text, 3)
    cipher_blocks = [str(encriptar(silaba, key)) for silaba in clear_text]
    tuples = [ast.literal_eval(item) for item in cipher_blocks]
    cipher_blocks = [(pad_message(i, 6), pad_message(j, 6)) for i, j in tuples]
    first_components = [item[0] for item in cipher_blocks]
    second_components = [item[1] for item in cipher_blocks]
    concatenated_first = "".join(first_components)
    concatenated_second = "".join(second_components)
    encrypted_text = (concatenated_first, concatenated_second)
    return encrypted_text, key


def desencriptar(encrypted_message, clave_privada):
    y1, y2 = encrypted_message
    y1 = y1.replace("#", "")
    y2 = y2.replace("#", "")
    y1 = base_alphabet_to_26(y1)
    y2 = base_alphabet_to_26(y2)
    a, p = clave_privada
    message_desencrypted = ((y1 ** (p - 1 - a)) * y2) % p
    message_desencrypted = base_26_to_alphabet(message_desencrypted)
    return message_desencrypted


def gamal_decrypt(encrypted_text: str, key: str):
    key = key.split(" ")

    key = (int(key[0]), int(key[1]))

    encrypted_text = ast.literal_eval(encrypted_text)
    encrypted_text0 = texto_a_silabas(encrypted_text[0], 6)
    encrypted_text1 = texto_a_silabas(encrypted_text[1], 6)
    cipher_blocks = [
        str(desencriptar((encrypted_text0[i], encrypted_text1[i]), key))
        for i in range(len(encrypted_text0))
    ]
    clear_text = "".join(cipher_blocks).lower()
    return clear_text, key
