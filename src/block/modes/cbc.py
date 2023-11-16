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

def cbc(plain_text, key, algorithm, algorithm_name, encrypt):
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
            # Perform xor between iv and the first block and cipher it
            # print("iv:", iv)
            # print("first block:", blocks[0])
            result = hex(int(iv, 16)^int(blocks[0],16))[2:]
            # print("xor:",result)
            result = pad_block(result, block_size)
            encrypted_result, key = algorithm(result, key) 
            # Now, encrypt the other blocks using this result

            cipher_blocks = []
            cipher_blocks.append(encrypted_result)

            for i in range(1,len(blocks)):
                res = hex(int(cipher_blocks[i-1], 16)^int(blocks[i],16))[2:] # Perform xor using the previuos result and the current block
                res = pad_block(res, block_size)
                encrypted_res, _ = algorithm(res, key)

                cipher_blocks.append(encrypted_res)
            
            cipher_text = "".join(cipher_blocks)


            return cipher_text, key
    
    else:
            # decrypt the first block:
            result, _ = algorithm(blocks[0], key)
            
            # do xor of the result with the iv

            clear_text_0 = hex(int(iv, 16)^int(result,16))[2:]
            clear_text_0 = pad_block(clear_text_0, block_size)
            clear_blocks = []

            clear_blocks.append(clear_text_0)

            for i in range(1, len(blocks)):
                res, _ = algorithm(blocks[i], key) # decrypt the block i
                plain_text_i = hex(int(blocks[i-1], 16)^int(res,16))[2:]
                plain_text_i = pad_block(plain_text_i, block_size)
                clear_blocks.append(plain_text_i)

            plain_text = "".join(clear_blocks)

            return plain_text, key