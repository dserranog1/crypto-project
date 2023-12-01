## Module for cipher and decipher logic
from .analysis import *


def cifrar(numero, clave_publica):
    return (numero**2) % clave_publica


# algoritmo extendido de Euclides
def gcd(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        q = old_r // r
        tr, r = r, old_r - q * r
        old_r = tr

        ts, s = s, old_s - q * s
        old_s = ts

        tt, t = t, old_t - q * t
        old_t = tt

    return old_r, old_s, old_t


def texto_a_silabas(texto, a):
    # Eliminar espacios y convertir a mayúsculas
    texto_sin_espacios = texto.replace(" ", "").lower()

    # Crear una lista de sílabas de tres letras
    lista_silabas = [
        texto_sin_espacios[i : i + a] for i in range(0, len(texto_sin_espacios), a)
    ]

    return lista_silabas


def decode_integers_to_bytes(integers):
    byte_list = []
    for num in integers:
        byte_representation = num.to_bytes((num.bit_length() + 7) // 8, byteorder="big")
        byte_list.append(byte_representation)
    return byte_list


def bytes_list_to_strings(byte_list):
    string_list = []
    for byte_repr in byte_list:
        decoded_string = byte_repr.decode("utf-8", "replace")
        string_list.append(decoded_string)
    return string_list


def desencriptar(encrypted_text, key):
    p, q = key
    n = p * q
    mp = pow(int(encrypted_text), (p + 1) // 4, p)
    mq = pow(int(encrypted_text), (q + 1) // 4, q)
    ext = gcd(p, q)
    yp, yq = ext[1], ext[2]
    r1 = (yp * p * mq + yq * q * mp) % n
    r2 = n - r1
    r3 = (yp * p * mq - yq * q * mp) % n
    r4 = n - r3
    return r1, r2, r3, r4


def invalid_key(key, is_private):

    keys = key.split(" ")

    if is_private and len(keys) == 2:
        k1, k2 = keys

        return k1.isnumeric() and k2.isnumeric()

    elif not is_private and len(keys) == 1:

        k1 = keys[0]
        return k1.isnumeric()

    return False


def rabin_encrypt(clear_text: str, key: str):

    n = int(key)
    clear_text = texto_a_silabas(clear_text, 5)
    cifrado = []
    for i in clear_text:
        m = int.from_bytes(i.encode("utf-8"), byteorder="big")
        c = cifrar(m, n)
        cifrado.append(str(c))
    encrypted_text = "".join(cifrado)
    return encrypted_text, key


def rabin_decrypt(encrypted_text: str, key: str):
    key = key.split(" ")

    key = (int(key[0]), int(key[1]))
    p, q = key
    encrypted_text = texto_a_silabas(encrypted_text, 12)

    descifrado = []
    for j in encrypted_text:
        d = desencriptar(j, (p, q))

        descifrado.append(d)
    final = []
    for k in descifrado:
        byte_list = decode_integers_to_bytes(k)
        decoded_strings = bytes_list_to_strings(byte_list)
        final.append([item for item in decoded_strings if item.isalnum()])
    display_message = ["".join(sublist) for sublist in final]
    display_message = "".join(display_message)
    return display_message, key
