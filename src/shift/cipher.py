## Module for cipher and decipher logic
from shift.analysis import *
from shift.keygen import *


def revisar_clave(clave):
    if not clave:
        clave = generate_key()
    elif not clave.isdigit():
        clave = generate_key()
    else:
        clave = int(clave)
    return clave



def cifrado_desplazamiento(clave, mensaje):
    clave = revisar_clave(clave)
    return convertir_letras(cifrado_clave(clave, convertir_numeros(eliminar_espacios(mayusculas(mensaje))))), clave


def descifrado_desplazamiento(clave, mensaje):
    clave = revisar_clave(clave)
    return convertir_letras(descifrado_clave(clave, convertir_numeros(eliminar_espacios(mayusculas(mensaje))))), clave


def attack(texto_cifrado):
  lista_attack=[]
  for i in range(25):
    des= descifrado_desplazamiento(str(i), texto_cifrado)

    lista_attack.append({'clave':str(i), 'texto_descifrado':des[0]})
  return lista_attack


#prueba x

#mensaje = "attack at dawn"
#
#mensaje = mayusculas(mensaje)
#cifrado = cifrado_desplazamiento(100, mensaje)
#print(f'cifrado: {cifrado}')
#mensaje_descifrado = descifrado_desplazamiento(100, 'WPPWYGWPZWSJ')
#print(f'descifrado: {mensaje_descifrado}')
#
#texto_cifrado= 'wppwygwpzws'
#print(attack(texto_cifrado))
