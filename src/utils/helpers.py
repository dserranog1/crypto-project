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
