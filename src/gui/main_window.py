import PySimpleGUI as sg
from gui.classic_algorithms.classic_window import create_classics_window
from gui.common.custom_elements import center_column
from shift.cipher import (
    cifrado_desplazamiento,
    descifrado_desplazamiento,
    attack as analyze_shift,
)
from shift.keygen import generate_key as generate_shift_key
from permutation.cipher import cifrado_permutacion, descifrado_permutacion
from permutation.keygen import generate_key as generate_permutation_key
from vigenere.cipher import cifrado_vigenere, descifrado_vigenere
from vigenere.keygen import generar_clave as generar_clave_vigenere
from substitution.cipher import sustitucion_cripter, sustitucion_desencriptar
from substitution.keygen import generate_key as generate_substitution_key
from affine.cipher import cifrado_afin, descifrado_afin
from affine.keygen import generate_key as generate_affine_key
from utils.helpers import format_attack, format_input, is_valid_image_input
from utils.text_to_image import image_to_list, list_to_image
from globals import *
from hill.cipher import (
    encryption_algorithm as hill_encrypt,
    decryption_algorithm as hill_decrypt,
    encrypt_image,
    decrypt_image,
)
from hill.keygen import generate_key as hill_keygen


def make_selection_window():
    layout = [
        [
            sg.Text(
                "Bienvenido a EnigmaVault, por favor selecione una categoría para comenzar"
            )
        ],
        [
            center_column(
                [
                    [sg.Button("Algoritmos clásicos", key=CLASSICS)],
                    [sg.Button("Algoritmos otro", key=OTRO)],
                ]
            )
        ],
        [center_column([[sg.Button("Salir")]])],
    ]
    return sg.Window(
        "Criptonita", layout, location=(0, 0), finalize=True, disable_close=True
    )


def make_win2():
    layout = [
        [sg.Text("The second window")],
        [sg.Input(key="-IN-", enable_events=True)],
        [sg.Text(size=(25, 1), k="-OUTPUT-")],
        [sg.Button("Erase"), sg.Button("Popup"), sg.Button("Salir")],
    ]
    return sg.Window("Second Window", layout, finalize=True, disable_close=True)


def close_window(window_manager, window):
    for window_key in window_manager:
        if window_manager[window_key]["window"] == window:
            window_manager[window_key]["window"] = None
            return True
    return False


def init_main_window():
    sg.theme("DarkGrey13")
    window_manager = {
        CLASSICS: {"create_fn": create_classics_window, "window": None},
        OTRO: {"create_fn": make_win2, "window": None},
    }
    """
    Encryption and decryption algorithms must have the following structure

    encryption_algorithm(key: str, message: str):
        # logic goes here

        return encrypted_message, key
    
    decryption_algorithm(key: str, message: str):
        # logic goes here

        return decrypted_message, key

    Key should be validated and in case no key was provided, generate one, hence the return of the key too.
    """
    algorithms_manager = {
        SHIFT: {
            ENCRYPT: cifrado_desplazamiento,
            DECRYPT: descifrado_desplazamiento,
            KEY_GEN: generate_shift_key,
            ANALYZE: analyze_shift,
        },
        PERMUTATION: {
            ENCRYPT: cifrado_permutacion,
            DECRYPT: descifrado_permutacion,
            KEY_GEN: generate_permutation_key,
        },
        VIGENERE: {
            ENCRYPT: cifrado_vigenere,
            DECRYPT: descifrado_vigenere,
            KEY_GEN: generar_clave_vigenere,
        },
        HILL: {
            ENCRYPT: hill_encrypt, 
            DECRYPT: hill_decrypt, 
            KEY_GEN: hill_keygen,
        },
        SUBSTITUTION: {
            ENCRYPT: sustitucion_cripter,
            DECRYPT: sustitucion_desencriptar,
            KEY_GEN: generate_substitution_key,
        },
        AFFINE: {
            ENCRYPT: cifrado_afin,
            DECRYPT: descifrado_afin,
            KEY_GEN: generate_affine_key,
        }
    }
    """
    The analyze function must have the following structure
    
    analyze_message_algorithm(message):
        # logic goes here

        return [{'clave': key0, 'texto_descifrado'}, {'clave': key1, 'texto_descifrado': 'decrypted_text_with_key1'}
        ..
        ..
        ..
        {'clave': keyN, 'texto_descifrado': 'decrypted_text_with_keyN'}]

    For proper formatting the analysis MUST be returned with the above-mentioned form.
    """

    make_selection_window()
    while True:  # Event Loop
        window, event, values = sg.read_all_windows()
        # Retrieve in case the action was an algorithm-related action
        algorithm_and_action = event.split("-", 1)
        # If the action has to do with exiting a window, we handle that first
        if event == sg.WIN_CLOSED or event == "Salir":
            window.close()
            if not close_window(window_manager, window):
                break
        elif event in window_manager and not window_manager[event]["window"]:
            window_manager[event]["window"] = window_manager[event]["create_fn"]()
        elif algorithm_and_action[0] in algorithms_manager:
            # If action is an algorithm-related, the action/element will be in the second position
            # We unpack them for better readability
            algorithm, action = algorithm_and_action[0], algorithm_and_action[1]
            if action in ENCRYPT:
                encrypted_text, key = algorithms_manager[algorithm][ENCRYPT](
                    format_input(values[algorithm + KEY_INPUT]),
                    values[algorithm + CLEAR_TEXT_INPUT_BOX],
                )
                window[algorithm + ENCRYPTED_TEXT_INPUT_BOX].update(encrypted_text)
                window[algorithm + KEY_INPUT].update(key)
            elif action in DECRYPT:
                clear_text, key = algorithms_manager[algorithm][DECRYPT](
                    format_input(values[algorithm + KEY_INPUT]),
                    values[algorithm + ENCRYPTED_TEXT_INPUT_BOX],
                )
                window[algorithm + CLEAR_TEXT_INPUT_BOX].update(clear_text)
                window[algorithm + KEY_INPUT].update(key)
            elif action in KEY_GEN:
                generated_key = algorithms_manager[algorithm][KEY_GEN]()
                window[algorithm + KEY_INPUT].update(generated_key)
            elif (action in DELETE + CLEAR_TEXT_INPUT_BOX) or (
                action in DELETE + ENCRYPTED_TEXT_INPUT_BOX
            ):
                input_box = action.split("-", 1)[1]
                window[algorithm + "-" + input_box].update("")
            elif action in ANALYZE:
                output = algorithms_manager[algorithm][ANALYZE](
                    values[algorithm + ENCRYPTED_TEXT_INPUT_BOX]
                )
                formatted_output = format_attack(output)
                sg.popup_scrolled(
                    formatted_output,
                    title="Resultados del análisis",
                    size=(50, 10),
                )
        elif algorithm_and_action[0] == "HILL_IMAGE_ENCRYPT":
            file = sg.popup_get_file(
                "Seleccion la imagen por favor (PNG, JPG, JPEG)",
                "Seleccione una imagen",
            )
            if not file:
                continue
            while not is_valid_image_input(file):
                sg.popup_error("Formato invalido", title="Ok")
                file = sg.popup_get_file(
                    "Seleccion la imagen por favor (PNG, JPG, JPEG)",
                    "Seleccione una imagen",
                )
                if not file:
                    break
            image, original_shape = image_to_list(file)
            input_key = values[HILL_KEY_INPUT]
            if not input_key:
                input_key = hill_keygen(is_image=True)
            original_length = len(image)
            encrypted_image, key = encrypt_image(input_key, image)
            # Aditional items might've been added to complete the encryption, so we go back to the original size
            encrypted_image = encrypted_image[:original_length]
            list_to_image(encrypted_image, original_shape, "encrypted_image")

            window[HILL_KEY_INPUT].update(key)
        elif algorithm_and_action[0] == "HILL_IMAGE_DECRYPT":
            file = sg.popup_get_file(
                "Seleccion la imagen por favor (PNG, JPG, JPEG)",
                "Seleccione una imagen",
            )
            if not file:
                continue
            while not is_valid_image_input(file):
                sg.popup_error("Formato invalido", title="Ok")
                file = sg.popup_get_file(
                    "Seleccion la imagen por favor (PNG, JPG, JPEG)",
                    "Seleccione una imagen",
                )
                if not file:
                    break
            image, original_shape = image_to_list(file)
            input_key = values[HILL_KEY_INPUT]
            if not input_key:
                input_key = hill_keygen(is_image=True)
            decrypted_image, key = decrypt_image(input_key, image)
            # Aditional items might've been added to complete the encryption, so we go back to the original size
            decrypted_image = decrypted_image[:original_length]
            list_to_image(decrypted_image, original_shape, "decrypted_image")
            window[HILL_KEY_INPUT].update(key)
