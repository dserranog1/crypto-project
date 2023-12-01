## Module for cipher and decipher logic
from .analysis import *


def MCR(numero, potencia, modulo):
    binario = bin(potencia)[2:]
    resultado = 1
    for k in binario:
        if int(k) == 1:
            resultado = ((resultado**2) * numero) % modulo
        else:
            resultado = (resultado**2) % modulo
    return resultado


def cifrar(numero, clave_publica):
    n, b = clave_publica
    return MCR(numero, b, n)


def descifrar(numero, clave_privada):
    n, a = clave_privada
    return MCR(numero, a, n)


# convertir texto
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


def texto_a_silabas(texto, a):
    # Eliminar espacios y convertir a mayúsculas
    texto_sin_espacios = texto.replace(" ", "").lower()

    # Crear una lista de sílabas de tres letras
    lista_silabas = [
        texto_sin_espacios[i : i + a] for i in range(0, len(texto_sin_espacios), a)
    ]

    return lista_silabas


def pad_number(number, block_size):
    message_len = len(number)

    return "0" * (block_size - len(number)) + str(number)


def RSA_cifrar(texto_claro, clave_publica):
    texto_claro = texto_a_silabas(texto_claro, 3)
    cipher_blocks = [
        str(cifrar(base_alphabet_to_26(silaba), clave_publica))
        for silaba in texto_claro
    ]

    cipher_blocks = [pad_number(number, 13) for number in cipher_blocks]

    return "".join(cipher_blocks)

    # pad according to the max len:
    # for silaba in texto_claro:
    #   numero = base_alphabet_to_26(silaba)
    #   silaba_cifrada = str(cifrar(numero,clave_publica))
    #   texto_cifrado = texto_cifrado + silaba_cifrada
    return texto_cifrado


def RSA_descifrar(texto_cifrado, clave_privada):
    texto_cifrado = texto_a_silabas(texto_cifrado, 13)
    texto_descifrado = ""
    for silaba in texto_cifrado:

        silaba_descifrada = base_26_to_alphabet(descifrar(int(silaba), clave_privada))
        texto_descifrado = texto_descifrado + silaba_descifrada
    return texto_descifrado.lower()


def invalid_key(key, _):

    keys = key.split(" ")
    if len(keys) != 2:
        return False

    k1, k2 = keys

    return k1.isnumeric() and k2.isnumeric()


def rsa_encrypt(clear_text: str, key: str):
    # implement rsa algorithm here

    key = key.split(" ")
    key = (int(key[0]), int(key[1]))

    clear_text = texto_a_silabas(clear_text, 3)

    cipher_blocks = [
        str(cifrar(base_alphabet_to_26(silaba), key)) for silaba in clear_text
    ]

    cipher_blocks = [pad_number(number, 13) for number in cipher_blocks]

    return "".join(cipher_blocks), key


def rsa_decrypt(encrypted_text: str, key: str):

    key = key.split(" ")
    key = (int(key[0]), int(key[1]))
    if not encrypted_text.isdigit():
        return "No ha sido posible desencriptar esta entrada", key
    encrypted_text = texto_a_silabas(encrypted_text, 13)
    clear_text = ""
    for silaba in encrypted_text:

        silaba_descifrada = base_26_to_alphabet(descifrar(int(silaba), key))

        clear_text = clear_text + silaba_descifrada

    # implement rsa algorithm here

    return clear_text, key
