## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key
from block.des.cipher import des_encrypt, des_decrypt


def invalid_key(key):
    # implement key validation logic
    return True  # or False


def t_des_encrypt(block_of_64_bits, key):
    # # implement t_des algorithm here
    # if not key or invalid_key(key):
    #     # key gen and validation
    #     key = generate_key()

    # cipher_text_block = "tdes encrypt!"
    # return cipher_text_block, key
    keys_arr = key.split(" ")
    if len(keys_arr) != 3:
        keys_arr = tres_claves()

    key_1, key_2, key_3 = keys_arr[0], keys_arr[1], keys_arr[2]
    # print("generated keys before encryption", " ".join([key_1, key_2, key_3]))

    # Cifrar el texto plano con el primer algoritmo DES
    text_cifrado_1, key_1 = des_encrypt(block_of_64_bits, key_1)

    # Cifrar el texto cifrado con el segundo algoritmo DES
    text_descifrado_2, key_2 = des_decrypt(text_cifrado_1, key_2)

    # Cifrar el texto cifrado con el tercer algoritmo DES
    text_cifrado_2, key_3 = des_encrypt(text_descifrado_2, key_3)
    # print("used keys in encryption:", " ".join([key_1, key_2, key_3]))

    return text_cifrado_2, " ".join([key_1, key_2, key_3])


def t_des_decrypt(block_of_64_bits, key):
    keys_arr = key.split(" ")
    if len(keys_arr) != 3:
        keys_arr = tres_claves()

    key_3, key_2, key_1 = keys_arr[0], keys_arr[1], keys_arr[2]

    # Cifrar el texto cifrado con el tercer algoritmo DES
    text_cifrado_2, _ = des_decrypt(block_of_64_bits, key_1)

    # Cifrar el texto cifrado con el segundo algoritmo DES
    text_descifrado_2, _ = des_encrypt(text_cifrado_2, key_2)

    # Cifrar el texto plano con el primer algoritmo DES
    text_cifrado_1, _ = des_decrypt(text_descifrado_2, key_3)

    return text_cifrado_1, " ".join([key_3, key_2, key_1])
