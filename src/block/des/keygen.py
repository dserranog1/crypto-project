# Module for key generation


import secrets


def generate_key(tam_pt):
    tam_key = tam_pt // 2
    key = secrets.token_hex(tam_key)
    return key.upper()
