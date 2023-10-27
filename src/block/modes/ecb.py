def pad_message(message, algorithm_name):
    if algorithm_name == "AES":
        block_size_bits = 128 # 128 bits
    elif algorithm_name == "DES":
        block_size_bits = 64 # 64 bits

    block_size_bytes = block_size_bits // 8

    # Calculate the number of bytes needed to pad the message
    padding_length = block_size_bytes - (len(message) % block_size_bytes)

    # Create a padding bytearray with bytes equal to the padding length
    padding = bytearray([padding_length] * padding_length)

    # Convert the original message to a bytearray and then concatenate the padding
    padded_message = bytearray(message, "utf-8") + padding

    return padded_message


def convert_to_128bit_blocks(input_string, algorithm_name):

    if algorithm_name == "AES":
        block_size_bytes = 16 # 128 bits
    elif algorithm_name == "DES":
        block_size_bytes = 8 # 64 bits

    padded_message = pad_message(input_string, algorithm_name)
    

    # Make sure each block is exactly 128 bits (16 bytes) by zero-padding if needed
    if len(padded_message) % block_size_bytes != 0:
        additional_padding = block_size_bytes - (len(padded_message) % block_size_bytes)
        padded_message.extend(bytearray([0] * additional_padding))

    num_blocks = len(padded_message) // block_size_bytes

    blocks = [
        padded_message[i : i + block_size_bytes]
        for i in range(0, len(padded_message), block_size_bytes)
    ]
    return blocks


def ecb(plain_text, key, algorithm, algorithm_name):
    # algorithm is a function, it can be AES or DES, mode should be agnostic to what algorithm is being used
    # use it as you would with any other function: e.g.
    # cipher_block, key = algorithm(block_of_plain_text)

    blocks = convert_to_128bit_blocks(plain_text, algorithm_name)

    # first, cipher the first block and get the key

    cipher_block_1, key = algorithm(blocks[0], key)

    # Now, cipher the other blocks using the same key as the first block

    encrypted_blocks = [algorithm(block, key)[0] for block in blocks[1:]]

    # Now, prepend the first block to the rest

    encrypted_blocks.insert(0, cipher_block_1)

    # Convert the encrypted bytearray blocks back to strings

    encrypted_blocks_text = [block.decode("utf-8") for block in encrypted_blocks]

    # Join the list to have only a string

    cipher_text = "".join(encrypted_blocks_text)

    return cipher_text, key
