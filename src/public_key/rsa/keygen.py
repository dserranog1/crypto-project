# Module for key generation

from utils.helpers import generate_prime_number, is_prime
import random
import numpy as np


def generate_key(primes=""):
    primes = primes.split()
    p, q = 0, 0
    if len(primes) != 2:
        p = generate_prime_number()
        q = generate_prime_number()
    else:
        p, q = primes[0], primes[1]
        if not p.isdigit():
            p = generate_prime_number()
        elif not is_prime(int(p)):
            p = generate_prime_number()
        if not q.isdigit():
            q = generate_prime_number()
        elif not is_prime(int(q)):
            q = generate_prime_number()

    p = int(p)
    q = int(q)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Elegir un exponente público e que sea coprimo con phi_n
    # se muere si cualquiera de los dos primos es dos o si los
    # primos de eleccion son 3 y 5.
    b = random.randint(p + q, phi_n)
    while np.gcd(b, phi_n) != 1:
        b = random.randint(p + q, phi_n)
    # Calcular el exponente privado d
    a = pow(b, -1, phi_n)

    public = f"{str(n)} {str(b)}"
    private = f"{str(n)} {str(a)}"

    return p, q, private, public
