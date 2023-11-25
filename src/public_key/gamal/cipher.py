## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key


def invalid_key(key):
    # implement key validation logic
    return False


def gamal_encrypt(clear_text: str, key: str):
    # implement gamal algorithm here
    encrypted_text = clear_text + "GAMAL ENCRYPT!!"
    return encrypted_text, key


def gamal_decrypt(encrypted_text: str, key: str):
    # implement gamal algorithm here
    clear_text = encrypted_text + "GAMAL DECRYPT!!!"
    return clear_text, key
