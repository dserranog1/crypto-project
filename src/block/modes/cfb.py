def split_string_into_blocks(input_string, block_size):
    if not input_string:
        return []

    blocks = []
    for i in range(0, len(input_string), block_size):
        block = input_string[i : i + block_size]
        if len(block) < block_size:
            block = "0" * (block_size - len(block)) + block
        blocks.append(block)

    return blocks

def pad_block(block, size):
    return "0" * (size - len(block)) + block

def cfb(plain_text, key, algorithm, algorithm_name, encrypt):
    # algorithm is a function, it can be AES or DES, mode should be agnostic to what algorithm is being used
    # use it as you would with any other function: e.g.
    # cipher_block, key = algorithm(block_of_plain_text)
    
    if algorithm_name == "AES":
        block_size = 32
    elif algorithm_name in ["DES", "TDES"]:
        block_size = 16

    blocks = split_string_into_blocks(plain_text, block_size)

    iv = str(1110).encode("latin-1").hex()
    iv = pad_block(iv, block_size)


    if encrypt:
        # encrypt the iv
        result, key = algorithm(iv, key)
        # do xor between plain text and result
        cipher_text_1 = hex(int(result, 16)^int(blocks[0],16))[2:]
        cipher_text_1 = pad_block(cipher_text_1, block_size)

        cipher_blocks = []
        cipher_blocks.append(cipher_text_1)

        for i in range(1, len(blocks)):
            res, _ = algorithm(cipher_blocks[i-1], key)
            # do xor between plain text and res
            cipher_text_i = hex(int(res, 16)^int(blocks[i],16))[2:]
            cipher_text_i = pad_block(cipher_text_i, block_size)
            cipher_blocks.append(cipher_text_i)

        cipher_text = "".join(cipher_blocks)


        return cipher_text, key
    
    else:

        # encrypt the iv
        result, _ = algorithm(iv, key)
        # do xor between result and cipher text
        plain_text_1 = hex(int(result, 16)^int(blocks[0],16))[2:]
        platin_text_1 = pad_block(plain_text, block_size)
        clear_blocks = []
        clear_blocks.append(plain_text_1)
        for i in range(1, len(blocks)):
            res, _ = algorithm(blocks[i-1], key)
            # do xor
            plain_text_i = hex(int(res, 16)^int(blocks[i],16))[2:]
            plain_text_i = pad_block(plain_text_i, block_size)
            clear_blocks.append(plain_text_i)
        
        plain_text = "".join(clear_blocks)

        return plain_text, key