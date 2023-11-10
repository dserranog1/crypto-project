import numpy as np
import math


def key2string(key):
    string_key = ""
    for i in range(key.shape[0]):
        for j in range(key.shape[1]):
            string_key += str(key[i, j]) + " "
        string_key += ";"

    return string_key.replace(" ;", ";")[:-1]


def validate_key(key_matrix, is_image=False):
    # verify, is crashing
    if is_image:
        module = 256
    else:
        module = 26
    # Check if the key matrix is square
    if key_matrix.shape[0] != key_matrix.shape[1]:
        return False

    # Check if the key matrix is invertible
    determinant = int(np.linalg.det(key_matrix))
    if math.gcd(determinant, module) != 1:
        return False

    if not np.linalg.det(key_matrix).is_integer():
        return False
    return True


def generate_key(key_size=3, is_image=False):
    if is_image:
        module = 256
    else:
        module = 26
    # Generate a random invertible key matrix for Hill cipher
    if is_image:
        key_matrix = np.random.randint(0, 255, (key_size, key_size)) % module
    else:
        key_matrix = np.random.randint(0, 10, (key_size, key_size)) % module
    while not validate_key(key_matrix, is_image):
        if is_image:
            key_matrix = np.random.randint(0, 255, (key_size, key_size)) % module
        else:
            key_matrix = np.random.randint(0, 10, (key_size, key_size)) % module
    return key2string(key_matrix)
