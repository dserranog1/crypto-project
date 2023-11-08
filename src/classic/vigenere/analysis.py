# Module for crypto analysis

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# poner criptonalasis, poder obtener el mensaje sin la contraseña


def eliminar_caracteres_invalidos(mensaje):
    mensaje = mensaje.upper()

    for letra in mensaje:
        if letra not in alfabeto:
            mensaje = mensaje.replace(letra, "")
        else:
            pass

    return mensaje
