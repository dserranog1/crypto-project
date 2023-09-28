# Module for key generation
import random
import string

def generate_key():
  alfabeto = string.ascii_uppercase
  clave = ''.join(random.sample(alfabeto, len(alfabeto)))
  return clave