# Module for key generation

def generate_key():  # generates
    key = secrets.token_hex(8)
    return key.upper()
