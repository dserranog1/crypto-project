# Module for crypto analysis

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def eliminar_caracteres_invalidos(mensaje):
    mensaje = mensaje.upper()

    for letra in mensaje:
        if letra not in alfabeto:
            mensaje = mensaje.replace(letra, "")
        else:
            pass

    return mensaje
