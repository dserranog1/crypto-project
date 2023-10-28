## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key


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
    
    keys = key_1, key_2, key_3 = tres_claves(key)

    # Cifrar el texto plano con el primer algoritmo DES
    text_cifrado_1,_ = des_encrypt(block_of_64_bits, key_1)

    # Cifrar el texto cifrado con el segundo algoritmo DES
    text_descifrado_2,_ = des_decrypt(text_cifrado_1, key_2)

    # Cifrar el texto cifrado con el tercer algoritmo DES
    text_cifrado_2,_ = des_encrypt(text_descifrado_2, key_3)

    return text_cifrado_2, keys

def t_des_decrypt(block_of_64_bits, key):
    
    # # implement t_des algorithm here
    # if not key or invalid_key(key):
    #     # key gen and validation
    #     key = generate_key()

    # plain_text_block = "tdes decrypt!"
    # return plain_text_block, key

    key_3, key_2, key_1 = keys

    # Cifrar el texto cifrado con el tercer algoritmo DES
    text_cifrado_2,_ = des_decrypt(block_of_64_bits, key_1)

    # Cifrar el texto cifrado con el segundo algoritmo DES
    text_descifrado_2,_ = des_encrypt(text_cifrado_2, key_2)

    # Cifrar el texto plano con el primer algoritmo DES
    text_cifrado_1,_ = des_decrypt(text_descifrado_2, key_3)

    return text_cifrado_1, keys
    

