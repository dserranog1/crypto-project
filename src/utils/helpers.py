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
