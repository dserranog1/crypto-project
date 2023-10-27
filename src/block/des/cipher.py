## Module for cipher and decipher logic
from .analysis import *
from .keygen import generate_key


def invalid_key(block_of_plain_text, key):
    if len(key) != len(block_of_plain_text):
        return True
    return False


def des_encrypt(block_of_plain_text, key, is_encrypting=True):

    if not key or invalid_key(block_of_plain_text, key):
        key = generate_key(len(block_of_plain_text))
        
    # Key's copy
    key1 = key
    # Hex to binary
    key = hex2bin(key)

    rkb, rk = round_keys(key)
    
    if not is_encrypting:
        rkb = rkb[::-1]
        rk = rk[::-1]

    block_of_plain_text = hex2bin(block_of_plain_text)

    # Initial Permutation
    block_of_plain_text = permute(block_of_plain_text, initial_perm, 64)
    print("After initial permutation", bin2hex(block_of_plain_text))

    # Splitting
    left = block_of_plain_text[0:32]
    right = block_of_plain_text[32:64]
    for i in range(0, 16):
        # Expansion D-box: Expanding the 32 bits data into 48 bits
        right_expanded = permute(right, exp_d, 48)

        # XOR RoundKey[i] and right_expanded
        xor_x = xor(right_expanded, rkb[i])

        # S-boxex: substituting the value from s-box table by calculating row and column
        sbox_str = ""

        for j in range(0, 8):
            row = bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
            col = bin2dec(
                int(
                    xor_x[j * 6 + 1]
                    + xor_x[j * 6 + 2]
                    + xor_x[j * 6 + 3]
                    + xor_x[j * 6 + 4]
                )
            )
            val = sbox[j][row][col]
            sbox_str = sbox_str + dec2bin(val)

        # Straight D-box: After substituting rearranging the bits
        sbox_str = permute(sbox_str, per, 32)

        # XOR left and sbox_str
        result = xor(left, sbox_str)
        left = result

        # Swapper
        if i != 15:
            left, right = right, left
        print("Round ", i + 1, " ", bin2hex(left), " ", bin2hex(right), " ", rk[i])

    # Combination
    combine = left + right

    # Final permutation: final rearranging of bits to get cipher text
    cipher_text = bin2hex(permute(combine, final_perm, 64))
    
    return cipher_text, key1


def des_decrypt(block_of_cipher_text, key):
    # implement des algorithm here
    
    if not key or invalid_key(block_of_cipher_text, key):
        # key gen and validation
        key = generate_key(len(block_of_cipher_text))
        
    return des_encrypt(block_of_cipher_text, key, False)
