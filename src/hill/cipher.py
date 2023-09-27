# Module for cipher and decipher logic
from hill.keygen import generate_key, validate_key, key2string
import numpy as np


def encryption_algorithm(key, message):
    # Validate the key or generate one if not provided
    # print(key)
    key = np.array([row.split(" ") for row in key.split(";")]).astype(int)
    # print(key.shape)
    # print(key)
    # print(np.linalg.det(key))
    if key is None:
        key = generate_key(len(message))

    # Check if the key is a numpy array
    if not isinstance(key, np.ndarray):
        raise ValueError("Key must be a numpy array")

    validate_key(key)

    message = message.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    message_len = len(message)
    key_size = key.shape[0]

    # Pad the message if its length is not a multiple of the key size
    if message_len % key_size != 0:
        padding = key_size - (message_len % key_size)
        message += "X" * padding

    encrypted_message = ""
    for i in range(0, len(message), key_size):
        chunk = message[i : i + key_size]
        chunk_indices = [ord(char) - ord("A") for char in chunk]
        # print("Chunk indices: ", chunk_indices)
        encrypted_chunk_indices = np.dot(chunk_indices, key) % 26
        # print("Indices: ", encrypted_chunk_indices)
        encrypted_chunk = "".join(
            [chr(index + ord("A")) for index in encrypted_chunk_indices]
        )
        encrypted_message += encrypted_chunk

    return encrypted_message, key2string(key)


def decryption_algorithm(key, message):
    key = np.array([row.split(" ") for row in key.split(";")]).astype(int)

    if not isinstance(key, np.ndarray):
        raise ValueError("Key must be a numpy array")

    validate_key(key)

    key_det = int(np.linalg.det(key))

    inv_det = pow(key_det, -1, 26)

    key_adj = np.linalg.inv(key) * key_det % 26

    key_inv = np.round(inv_det * key_adj) % 26

    # print("key inverse: ",key_inv)
    # Calculate the modular multiplicative inverse of key_det modulo 26
    for i in range(1, 26):
        if (key_det * i) % 26 == 1:
            key_det_inverse = i
            break
    else:
        raise ValueError("Key determinant has no modular multiplicative inverse")

    decrypted_message = ""
    key_size = key.shape[0]

    for i in range(0, len(message), key_size):
        chunk = message[i : i + key_size]
        chunk_indices = [ord(char) - ord("A") for char in chunk]
        decrypted_chunk_indices = np.dot(chunk_indices, key_inv) % 26
        decrypted_chunk = "".join(
            [chr(int(index) + ord("A")) for index in decrypted_chunk_indices]
        )
        decrypted_message += decrypted_chunk

    return decrypted_message, key2string(key)
