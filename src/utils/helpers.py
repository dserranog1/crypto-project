# Module for common helpers


def format_attack(data):
    formatted_data = []
    for item in data:
        formatted_data.append(
            "Clave" + item["clave"] + ": " + item["texto_descifrado"] + "\n"
        )
    return "".join(formatted_data)


def format_input(input):
    return input.replace("(", "").replace(")", "").replace(",", "")


def is_valid_clear_image_input(input):
    format = input.upper().split(".")
    if format[-1] not in ["JPG", "JPEG"]:
        return False
    return True


def is_valid_encrypted_image_input(input):
    format = input.upper().split(".")
    if format[-1] not in ["PNG"]:
        return False
    return True


def dec_to_hex(dec):
    return hex(dec).split("x")[1].zfill(2)


def image_to_hex(image):
    hex_image = ""
    for rgb_channel in image:
        hex_image += dec_to_hex(rgb_channel)
    return hex_image


def hex_to_dec(hex):
    return int(hex, 16)


def heximage_to_listimage(heximage):
    listimage = []
    for i in range(0, len(heximage) - 1, 2):
        listimage.append(hex_to_dec(heximage[i : i + 2]))
    return listimage


import random


def generate_prime_number():
    limite = int(1e6)
    # Inicializar una lista de booleanos para representar si cada número es primo
    es_primo = [True] * (limite + 1)
    # 0 y 1 no son primos
    es_primo[0] = es_primo[1] = False

    # Iterar sobre los números hasta la raíz cuadrada del límite
    for num in range(2, int(limite**0.5) + 1):
        # Si el número actual es primo
        if es_primo[num]:
            # Marcar como no primo todos los múltiplos de num
            for multiplo in range(num * num, limite + 1, num):
                es_primo[multiplo] = False

    # Generar una lista de los números primos encontrados
    primos = [num for num in range(2, limite + 1) if es_primo[num]]
    p = random.choice(primos[-40:])
    return p


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
