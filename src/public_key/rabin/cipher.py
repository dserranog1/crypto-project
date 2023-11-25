## Module for cipher and decipher logic
from .analysis import *


def invalid_key(key):
    # implement key validation logic
    return False


def rabin_encrypt(clear_text: str, key: str):
    # implement rabin algorithm here
    encrypted_text = clear_text + "RABIN ENCRYPT!!"
    return encrypted_text, key


def rabin_decrypt(encrypted_text: str, key: str):
    # implement rabin algorithm here
    clear_text = encrypted_text + "RABIN DECRYPT!!!"
    return clear_text, key
