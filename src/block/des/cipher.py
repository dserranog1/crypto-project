## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key


def invalid_key(key):
  if len(key) == len(pt):
    return True
  return False

def des_encrypt(block_of_plain_text, key):
    # implement des algorithm here
    if not key or invalid_key(key):
        key = generar_key(len(pt))

    cipher_text_block = "des encrypt!"
    return cipher_text_block, key


def des_decrypt(block_of_cipher_text, key):
    # implement des algorithm here
    if not key or invalid_key(key):
        # key gen and validation
        key = generate_key()

    plain_text_block = "des decrypt!"
    return plain_text_block, key
