## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key


def invalid_key(key):
    # implement key validation logic

    # if not clave:
    #   clave = generate_key()
    # elif not clave.isdigit():
    #    clave = generate_key()
    # else:
    #    clave = int(clave)
    # return clave
    return True  # or False


# def aes_encrypt(block_of_plain_text, key):
# implement aes algorithm here
# if not key or invalid_key(key):
#    # key gen and validation
#    key = generate_key()

#
# cipher_text_block = "aes encrypt!"
# return cipher_text_block, key


## data is block_of_plain_text


def aes_encrypt(data: bytes, key: bytes) -> bytes:
    key_bit_length = len(key) * 8

    if key_bit_length == 128:
        nr = 10
    elif key_bit_length == 192:
        nr = 12
    else:  # 256-bit keys
        nr = 14

    state = state_from_bytes(data)

    key_schedule = key_expansion(key)

    add_round_key(state, key_schedule, round=0)

    for round in range(1, nr):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state, key_schedule, round)

    sub_bytes(state)
    shift_rows(state)
    add_round_key(state, key_schedule, round=nr)

    cipher = bytes_from_state(state)
    return cipher, key


# def aes_decrypt(block_of_cipher_text, key):
#    # implement aes algorithm here
#    if not key or invalid_key(key):
#        # key gen and validation
#        key = generate_key()
#
#    plain_text_block = "aes decrypt!"
#    return plain_text_block, key
#


def aes_decrypt(cipher: bytes, key: bytes) -> bytes:
    key_byte_length = len(key)
    key_bit_length = key_byte_length * 8
    nk = key_byte_length // 4

    if key_bit_length == 128:
        nr = 10
    elif key_bit_length == 192:
        nr = 12
    else:  # 256-bit keys
        nr = 14

    state = state_from_bytes(cipher)
    key_schedule = key_expansion(key)
    add_round_key(state, key_schedule, round=nr)

    for round in range(nr - 1, 0, -1):
        inv_shift_rows(state)
        inv_sub_bytes(state)
        add_round_key(state, key_schedule, round)
        inv_mix_columns(state)

    inv_shift_rows(state)
    inv_sub_bytes(state)
    add_round_key(state, key_schedule, round=0)

    plain = bytes_from_state(state)
    return plain, key
