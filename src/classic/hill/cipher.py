# Module for cipher and decipher logic
from .keygen import generate_key, validate_key, key2string
import numpy as np


def encryption_algorithm(key, message):
    # Validate the key or generate one if not provided
    module = 26

    if len(key) == 0 or not validate_key(key):
        key = generate_key(3)

    key = np.array([row.split(" ") for row in key.split(";")]).astype(int)
    if not message:
        return " ", generate_key(3)

    # Check if the key is a numpy array
    if not isinstance(key, np.ndarray):
        raise ValueError("Key must be a numpy array")

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
        encrypted_chunk_indices = np.dot(chunk_indices, key) % module
        # print("Indices: ", encrypted_chunk_indices)
        encrypted_chunk = "".join(
            [chr(index + ord("A")) for index in encrypted_chunk_indices]
        )
        encrypted_message += encrypted_chunk

    return encrypted_message, key2string(key)


def decryption_algorithm(key, message):
    module = 26
    if len(key) == 0 or not validate_key(key):
        key = generate_key(3)

    key = np.array([row.split(" ") for row in key.split(";")]).astype(int)
    if not message:
        return " ", generate_key(3)

    if not isinstance(key, np.ndarray):
        raise ValueError("Key must be a numpy array")

    key_det = int(np.linalg.det(key))

    inv_det = pow(key_det, -1, module)

    key_adj = np.linalg.inv(key) * key_det % module

    key_inv = np.round(inv_det * key_adj) % module

    # Calculate the modular multiplicative inverse of key_det modulo module
    # for i in range(1, module):
    #     if (key_det * i) % module == 1:
    #         key_det_inverse = i
    #         break
    # else:
    #     raise ValueError("Key determinant has no modular multiplicative inverse")

    decrypted_message = ""
    key_size = key.shape[0]

    for i in range(0, len(message), key_size):
        chunk = message[i : i + key_size]
        chunk_indices = [ord(char) - ord("A") for char in chunk]
        decrypted_chunk_indices = np.dot(chunk_indices, key_inv) % module
        decrypted_chunk = "".join(
            [chr(int(index) + ord("A")) for index in decrypted_chunk_indices]
        )
        decrypted_message += decrypted_chunk

    return decrypted_message, key2string(key)


def encrypt_image(key, image):
    # Validate the key or generate one if not provided
    module = 256
    key = np.array([row.split(" ") for row in key.split(";")]).astype(int)
    if len(key) == 0 or not validate_key(key, is_image=True):
        key = generate_key(3)
        key = np.array([row.split(" ") for row in key.split(";")]).astype(int)

    # Check if the key is a numpy array
    if not isinstance(key, np.ndarray):
        raise ValueError("Key must be a numpy array")

    image_len = len(image)
    key_size = key.shape[0]

    # Pad the message if its length is not a multiple of the key size
    if image_len % key_size != 0:
        padding = key_size - (image % key_size)
        print(padding)
        for i in range(padding):
            image.append(255)

    encrypted_image = []
    for i in range(0, len(image), key_size):
        chunk = image[i : i + key_size]
        encrypted_chunk = np.dot(chunk, key) % module
        encrypted_chunk = encrypted_chunk.astype("uint8")
        encrypted_image.extend(encrypted_chunk.tolist())

    return encrypted_image, key2string(key)


def decrypt_image(key, image):
    module = 256
    key = np.array([row.split(" ") for row in key.split(";")]).astype(int)
    if len(key) == 0 or not validate_key(key, is_image=True):
        key = generate_key(3)
        key = np.array([row.split(" ") for row in key.split(";")]).astype(int)
    if not isinstance(key, np.ndarray):
        raise ValueError("Key must be a numpy array")

    key_det = int(np.linalg.det(key))

    inv_det = pow(key_det, -1, module)

    key_adj = np.linalg.inv(key) * key_det % module

    key_inv = np.round(inv_det * key_adj) % module

    # Calculate the modular multiplicative inverse of key_det modulo module
    # for i in range(1, module):
    #     if (key_det * i) % module == 1:
    #         break
    # else:
    #     raise ValueError("Key determinant has no modular multiplicative inverse")

    decrypted_image = []
    key_size = key.shape[0]

    for i in range(0, len(image), key_size):
        chunk = image[i : i + key_size]
        decrypted_chunk = np.dot(chunk, key_inv) % module
        decrypted_chunk = decrypted_chunk.astype("uint8")
        decrypted_image.extend(decrypted_chunk.tolist())

    return decrypted_image, key2string(key)
