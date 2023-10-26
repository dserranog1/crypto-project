# Module for crypto analysis

def hex2text(cadena_hexadecimal):
  cadena_ascii = "".join([chr(int(cadena_hexadecimal[i : i + 2], 16)) for i in range(0, len(cadena_hexadecimal), 2)])
  return cadena_ascii

def text2hex(texto):
  hexadecimal = ''.join([hex(ord(c))[2:].upper() for c in texto])
  hexadecimal.upper()
  return hexadecimal

