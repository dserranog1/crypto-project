## Module for cipher and decipher logic
from .analysis import *


def invalid_key(key):
    # implement key validation logic
    return False


def rsa_encrypt(clear_text: str, key: str):
    # implement rsa algorithm here
    encrypted_text = clear_text + "RSA ENCRYPT!!"
    return encrypted_text, key


def rsa_decrypt(encrypted_text: str, key: str):
    # implement rsa algorithm here
    clear_text = encrypted_text + "RSA DECRYPT!!"
    return clear_text, key
