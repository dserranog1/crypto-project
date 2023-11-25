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


def invalid_key(key):
    # implement key validation logic
    return False


def rabin_encrypt(clear_text: str, key: str):
    n = int(key)
    m = int.from_bytes(clear_text.encode("utf-8"), byteorder="big")
    encrypted_text = cifrar(m, n)
    return encrypted_text, key


def rabin_decrypt(encrypted_text: str, key: str):
    key = key.split(" ")
    key = (int(key[0]), int(key[1]))
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
    display_message = ""
    for b in [r1, r2, r3, r4]:
        # Decode bytes to string using UTF-8
        display_message += (
            b.to_bytes((b.bit_length() + 7) // 8, byteorder="big").decode(
                "utf-8", "replace"
            )
            + "\n"
        )
    return display_message, key
