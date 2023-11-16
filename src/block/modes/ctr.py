# def int_to_bytearray(integer):
#     # Use int.to_bytes() to convert the integer to a bytearray of 8 bytes (64 bits)
#     byte_array = integer.to_bytes(8, byteorder='big', signed=True)
#     return byte_array

# def pad_message(message, algorithm_name):
#     if algorithm_name == "AES":
#         block_size_bits = 128 # 128 bits
#     elif algorithm_name == "DES":
#         block_size_bits = 64 # 64 bits

#     block_size_bytes = block_size_bits // 8

#     # Calculate the number of bytes needed to pad the message
#     padding_length = block_size_bytes - (len(message) % block_size_bytes)

#     # Create a padding bytearray with bytes equal to the padding length
#     padding = bytearray([padding_length] * padding_length)

#     # Convert the original message to a bytearray and then concatenate the padding
#     padded_message = bytearray(message, "utf-8") + padding

#     return padded_message


# def convert_to_128bit_blocks(input_string, algorithm_name):

#     if algorithm_name == "AES":
#         block_size_bytes = 16 # 128 bits
#     elif algorithm_name == "DES":
#         block_size_bytes = 8 # 64 bits

#     padded_message = pad_message(input_string, algorithm_name)
    

#     # Make sure each block is exactly 128 bits (16 bytes) by zero-padding if needed
#     if len(padded_message) % block_size_bytes != 0:
#         additional_padding = block_size_bytes - (len(padded_message) % block_size_bytes)
#         padded_message.extend(bytearray([0] * additional_padding))

#     num_blocks = len(padded_message) // block_size_bytes

#     blocks = [
#         padded_message[i : i + block_size_bytes]
#         for i in range(0, len(padded_message), block_size_bytes)
#     ]
#     return blocks

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


def ctr(plain_text, key, algorithm, algorithm_name):
    # algorithm is a function, it can be AES or DES, mode should be agnostic to what algorithm is being used
    # use it as you would with any other function: e.g.
    # cipher_block, key = algorithm(block_of_plain_text)
    
    if algorithm_name == "AES":
        block_size = 32
    elif algorithm_name in ["DES", "TDES"]:
        block_size = 16


    blocks = split_string_into_blocks(plain_text, block_size)

    # generate list of nonces
    
    nonce_list = []

    for i in range(len(blocks)):
        hex_ = str(i).encode("latin-1").hex()
        hex_ = pad_block(hex_, block_size)
        print(hex_)
        nonce_list.append(hex_)

    # encrypt each nonce

    cipher_nonce_1, key = algorithm(nonce_list[0], key)

    # Now, cipher the other nonces using the same key as the first nonce

    encrypted_nonce = [algorithm(nonce, key)[0] for nonce in nonce_list[1:]]
    # Now, prepend the first block to the rest

    encrypted_nonce.insert(0, cipher_nonce_1)

    # Now we have 2 lists. One of message blocks and other of enctypted nonces. To cipher the message, we do xor of each block with its corresponding nonce
    print("Encrypted nonce: ", encrypted_nonce)
    print("Blocks:", blocks)
    cipher_blocks = [hex(int(a, 16)^int(b,16))[2:] for a, b in zip(blocks, encrypted_nonce)]

    print("Cipher blocks: ", cipher_blocks)
    # Join the list to have only a string
    
    cipher_text = "".join(cipher_blocks)
    
    return cipher_text, key
