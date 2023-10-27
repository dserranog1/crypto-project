## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key


def invalid_key(key):
    # implement key validation logic
    return True  # or False


def t_des_encrypt(block_of_plain_text, key):
    # implement t_des algorithm here
    if not key or invalid_key(key):
        # key gen and validation
        key = generate_key()

    cipher_text_block = "tdes encrypt!"
    return cipher_text_block, key


def t_des_decrypt(block_of_cipher_text, key):
    # implement t_des algorithm here
    if not key or invalid_key(key):
        # key gen and validation
        key = generate_key()

    plain_text_block = "tdes decrypt!"
    return plain_text_block, key
import hashlib

def tres_claves(key):
    key_1 = hex2bin(hashlib.sha256(key.encode()).hexdigest().upper()[:16])
    key_2 = hex2bin(hashlib.sha256(key_1.encode()).hexdigest().upper()[:16])
    key_3 = hex2bin(hashlib.sha256(key_2.encode()).hexdigest().upper()[:16])
    return (key_1, key_2, key_3)

def t_des_encrypt(block_of_64_bits, key, is_encrypting=True):

    keys = key_1, key_2, key_3 = tres_claves(key)

    if not is_encrypting:
      keys = keys[::-1]


    # Cifrar el texto plano con el primer algoritmo DES
    text_cifrado_1,_ = des_encrypt(block_of_64_bits, key_1)
    print('1era clave')

    # Cifrar el texto cifrado con el segundo algoritmo DES
    text_descifrado_2,_ = des_decrypt(text_cifrado_1, key_2)
    print('2daa clave')

    # Cifrar el texto cifrado con el tercer algoritmo DES
    text_cifrado_2,_ = des_encrypt(text_descifrado_2, key_3)
    print('3era clave')

    return text_cifrado_2, key_3

def t_des_decrypt(block_of_64_bits, key):
    return t_des_encrypt(block_of_64_bits, key, False)
