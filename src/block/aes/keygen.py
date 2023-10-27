# Module for key generation


import secrets


def generate_key():  # generates
    key = secrets.token_hex(16)
    return key
