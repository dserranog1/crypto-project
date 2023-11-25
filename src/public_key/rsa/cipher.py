## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key


def invalid_key(key):
    # implement key validation logic
    return True


def rsa_encrypt(clear_text: str, key: str):
    # implement rsa algorithm here
    if not key or invalid_key(key):
        # key gen and validation
        key = generate_key()
    encrypted_text = clear_text + "RSA ENCRYPT!!"
    return encrypted_text, key


def rsa_decrypt(encrypted_text: str, key: str):
    # implement rsa algorithm here
    if not key or invalid_key(key):
        # key gen and validation
        key = generate_key()
    clear_text = encrypted_text + "RSA DECRYPT!!"
    return clear_text, key
