# Module for key generation
import numpy as np


def relativos(x, y):
    n = np.max([x, y])
    m = np.min([x, y])
    while m > 0:
        t = n % m
        n = m
        m = t
    if n == 1:
        return True
    else:
        return False


def validate_key(key):
    if not key.isdigit():
        return False
    if relativos(int(key[0]), 26) != 1:
        return False
    if int(key[1]) >= 26:
        return False
    return True


def generate_key():
    # primos relativos a= 3,5,7,9,11,13,15,17,19,21,25
    A = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 25]
    num = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
    ]
    a = np.random.choice(A)
    b = np.random.choice(num)
    return str(a) + " " + str(b)
