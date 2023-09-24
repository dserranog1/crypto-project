# Module for common helpers


def format_attack(data):
    formatted_data = []
    for item in data:
        formatted_data.append(
            "Clave" + item["clave"] + ": " + item["texto_descifrado"] + "\n"
        )
    return "".join(formatted_data)
