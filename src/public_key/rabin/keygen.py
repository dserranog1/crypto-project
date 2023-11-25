# Module for key generation

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
    q = int(q)
    while p % 4 != 3:
        p = generate_prime_number()
    while q % 4 != 3 or q == p:
        q = generate_prime_number()
    n = p * q
    private = (p, q)
    public = n

    return p, q, private, public
