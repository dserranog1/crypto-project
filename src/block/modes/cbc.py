def cbc(plain_text, key, algorithm):
    # algorithm is a function, it can be AES or DES, mode should be agnostic to what algorithm is being used
    # use it as you would with any other function: e.g.
    # cipher_block, key = algorithm(block_of_plain_text)
    cipher_text = ""
    for i in range(20):
        cipher_text, key = (
            algorithm(plain_text) + "iteration number" + i + "with algorithm" + "cbc"
        )
    return cipher_text, key
