## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key


def invalid_key(key):
    # implement key validation logic
    return True  # or False


def aes_encrypt(block_of_plain_text, key):
    # implement aes algorithm here
    if not key or invalid_key(key):
        # key gen and validation
        key = generate_key()

    cipher_text_block = "aes encrypt!"
    return cipher_text_block, key


def aes_decrypt(block_of_cipher_text, key):
    # implement aes algorithm here
    if not key or invalid_key(key):
        # key gen and validation
        key = generate_key()

    plain_text_block = "aes decrypt!"
    return plain_text_block, key