# Module for key generation


from .analysis import tres_claves


def generate_key():  # generates
    keys = tres_claves()
    return " ".join(keys)
