# Module for cipher and decipher logic
from analysis import *

def cifrado_desplazamiento(clave, mensaje):
    return convertir_letras(cifrado_clave(clave, convertir_numeros(eliminar_espacios(mensaje))))


def descifrado_desplazamiento(clave, mensaje):
    return convertir_letras(descifrado_clave(clave, convertir_numeros(eliminar_espacios(mensaje))))



## prueba x

mensaje = "attack at dawn"
mensaje= mayusculas(mensaje)


cifrado = cifrado_desplazamiento(100, mensaje)
print(f'cifrado: {cifrado}')




mensaje_descifrado= descifrado_desplazamiento(100, 'WPPWYGWPZWSJ')


print(f'descifrado: {mensaje_descifrado}')
