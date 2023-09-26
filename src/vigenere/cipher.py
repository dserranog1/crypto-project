# Module for cipher and decipher logic

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cifrado_vigenere(clave, mensaje): #Necesita 2 argumentos digitados por el usuario

  mensaje = mensaje.upper() #Se trabaja todo en mayúsculas
  clave = clave.upper()
  
  for letra in mensaje:
    if letra not in alfabeto: #Se valida que hayan solo letras del abecedario en inglés
      print('El mensaje contiene caracteres no válidos')
  for letra in clave:
    if letra not in alfabeto: #No se aceptan símbolos ni caracteres especiales...
      clave = definir_clave()

  mensaje_cifrado = '' #Se parte de un string vacío

  clave_repetida = clave * (len(mensaje) // len(clave) + 1) #Cuántas veces se repite la clave en el mensaje en claro

  for letra_mensaje, letra_clave in zip(mensaje, clave_repetida):
    posicion_mensaje = alfabeto.find(letra_mensaje) #Son las posiciones de cada letra en el mensaje 
    posicion_clave = alfabeto.find(letra_clave) + 1 #Y en la clave, para poder sumarlas en la siguiente variable

    posicion_cifrada = posicion_mensaje + posicion_clave % len(alfabeto) - 26 if posicion_mensaje + posicion_clave >= len(alfabeto) else posicion_mensaje + posicion_clave

    mensaje_cifrado += alfabeto[posicion_cifrada] #Se busca el índice en el alfabeto y se van sumando en el string vacío

  return mensaje_cifrado, clave


def descifrado_vigenere(clave, mensaje_cifrado): #Análogamente funciona esta función al cifrado

  mensaje_cifrado = mensaje_cifrado.upper()
  clave = clave.upper()
  for letra in mensaje_cifrado:
    if letra not in alfabeto:
      print('El mensaje cifrado contiene caracteres no válidos')
  for letra in clave:
    if letra not in alfabeto:
      print('La clave contiene caracteres no válidos')

  mensaje_claro = ''
  clave_repetida = clave * (len(mensaje_cifrado) // len(clave) + 1)

  for letra_cifrada, letra_clave in zip(mensaje_cifrado, clave_repetida):
    posicion_cifrada = alfabeto.find(letra_cifrada)
    posicion_clave = alfabeto.find(letra_clave) + 1

    posicion_descifrada = posicion_cifrada - posicion_clave % len(alfabeto) + 26 if posicion_cifrada - posicion_clave < 0 else posicion_cifrada - posicion_clave
    #En la variable anterior se hace las operaciones inversas, para descrifrar el mensaje
    
    mensaje_claro += alfabeto[posicion_descifrada]

  return mensaje_claro, clave
  
