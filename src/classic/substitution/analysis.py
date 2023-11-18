# Module for crypto analysis

# hacer el análisis, análisis de frecuencias
from .cipher import sustitucion_desencriptar

most_frequent_letters = [
    "E",
    "A",
    "O",
    "S",
    "R",
    "N",
    "I",
    "D",
    "L",
    "C",
    "T",
    "U",
    "M",
    "P",
    "B",
    "G",
    "V",
    "Y",
    "Q",
    "H",
    "F",
    "Z",
    "J",
    "Ñ",
    "X",
    "K",
    "W",
]


def get_most_frequent_letters_from_cipher_text(cipher_text):
    most_freq = []
    dic_of_appareances = {}
    cipher_text = cipher_text.upper()
    for letter in most_frequent_letters:
        dic_of_appareances[letter] = cipher_text.count(letter)
    while dic_of_appareances:
        most_freq.append(max(dic_of_appareances, key=dic_of_appareances.get))
        del dic_of_appareances[most_freq[-1]]
    return most_freq


def build_key_dict(most_freq_from_cipher_text):
    key_dict = {a: b for a, b in zip(most_freq_from_cipher_text, most_frequent_letters)}

    return key_dict


def build_key(key_dict):
    key = ""
    while key_dict:
        key += min(key_dict, key=key_dict.get)
        del key_dict[key[-1]]
    return key


def subsitution_analysis(cipher_text):
    most_from_cipher = get_most_frequent_letters_from_cipher_text(cipher_text)
    key_dic = build_key_dict(most_freq_from_cipher_text=most_from_cipher)
    key = build_key(key_dic)
    possible_clear_text, key = sustitucion_desencriptar(key, cipher_text)
    display_text = (
        "Posible clave :" + key + "\n" + "Posible texto claro: " + possible_clear_text
    )
    return display_text
