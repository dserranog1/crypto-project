## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key
from block.utils.common import is_hex


def valid_key(key):

    if len(key) == 32 and is_hex(key):
        return True
    return False


def aes_encrypt(hex_as_str: str, key: str) -> bytes:
    # implement aes algorithm here
    if not key or not valid_key(key):
        # key gen and validation
        key = generate_key()
    key = bytes.fromhex(key)
    data = bytes.fromhex(hex_as_str)
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
    return cipher.hex(), key.hex()


def aes_decrypt(cipher_as_str: bytes, key: bytes) -> bytes:
    if not key or not valid_key(key):
        # key gen and validation
        key = generate_key()
    key = bytes.fromhex(key)
    cipher = bytes.fromhex(cipher_as_str)
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
    return plain.hex(), key.hex()
