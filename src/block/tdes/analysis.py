# Module for crypto analysis

import hashlib

def tres_claves(key=None):
  
  if key == None or (len(key) != 64 and not is_binary(key)):
    key = generate_key()

    key_1 = hashlib.sha256(key.encode()).hexdigest().upper()[:16]
    key_2 = hashlib.sha256(key_1.encode()).hexdigest().upper()[:16]
    key_3 = hashlib.sha256(key_2.encode()).hexdigest().upper()[:16]
    
    # key_1 = hex2bin(hashlib.sha256(key.encode()).hexdigest().upper()[:16])
    # key_2 = hex2bin(hashlib.sha256(key_1.encode()).hexdigest().upper()[:16])
    # key_3 = hex2bin(hashlib.sha256(key_2.encode()).hexdigest().upper()[:16])
    
    return (key_1, key_2, key_3)
