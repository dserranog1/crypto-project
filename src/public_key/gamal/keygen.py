# Module for key generation
import numpy as np

from utils.helpers import generate_prime_number, is_prime


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
    q = int(0)

    # KEY GENERATION LOGIC GOES HERE
    g = np.random.randint(1, p - 1)
    a = np.random.randint(1, p - 1)
    while a == g:
        a = np.random.randint(1, p - 1)
    k = pow(g, a, p)
    clave_publica = (g, p, k)
    clave_privada = (a, p)
    private = f"{str(a)} {str(p)}"
    public = f"{str(g)} {str(p)} {str(k)}"
    return p, q, private, public
