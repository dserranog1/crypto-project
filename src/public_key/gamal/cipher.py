## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key


def invalid_key(key):
    # implement key validation logic
    return True


def gamal_encrypt(clear_text: str, key: str):
    # implement rsa algorithm here
    if not key or invalid_key(key):
        # key gen and validation
        key = generate_key()
    encrypted_text = clear_text + "GAMAL ENCRYPT!!"
    return encrypted_text, key


def gamal_decrypt(encrypted_text: str, key: str):
    # implement rsa algorithm here
    if not key or invalid_key(key):
        # key gen and validation
        key = generate_key()
    clear_text = encrypted_text + "GAMAL DECRYPT!!!"
    return clear_text, key
