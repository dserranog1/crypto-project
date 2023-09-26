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
from utils.helpers import format_attack, format_input
from globals import *
from hill.cipher import encryption_algorithm, decryption_algorithm, generate_key


def make_selection_window():
    layout = [
        [sg.Text("Bienvenido, por favor selecione una categoría para comenzar")],
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
    return sg.Window("Criptonita", layout, location=(0, 0), finalize=True)


def make_win2():
    layout = [
        [sg.Text("The second window")],
        [sg.Input(key="-IN-", enable_events=True)],
        [sg.Text(size=(25, 1), k="-OUTPUT-")],
        [sg.Button("Erase"), sg.Button("Popup"), sg.Button("Salir")],
    ]
    return sg.Window("Second Window", layout, finalize=True)


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
        HILL: {
            ENCRYPT: encryption_algorithm,
            DECRYPT: decryption_algorithm,
            KEY_GEN: generate_key
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
