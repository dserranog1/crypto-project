# Module for key generation

def generate_key(key_size):
    # Generate a random invertible key matrix for Hill cipher
    while True:
        key_matrix = np.random.randint(0, 26, (key_size, key_size))
        try:
            validate_key(key_matrix)
            return key_matrix
        except ValueError:
            continue