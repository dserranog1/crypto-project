# Module for key generation

from utils.helpers import generate_prime_number, is_prime


def generate_key(primes):
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

    private = str(p) + " private rabin"
    public = str(q) + " public rabin"
    return p, q, private, public
