import PySimpleGUI as sg
from gui.classic_algorithms.classic_window import create_classics_window
from gui.common.custom_elements import center_column
from shift.cipher import (
    cifrado_desplazamiento,
    descifrado_desplazamiento,
    attack as attack_shift,
)
from shift.keygen import generate_key as generate_shift_key
from utils.helpers import format_attack
from globals import *


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
    algorithms_manager = {
        ENCRYPT_SHIFT: cifrado_desplazamiento,
        DECRYPT_SHIFT: descifrado_desplazamiento,
    }
    key_gen_manager = {GENERATE_SHIFT: generate_shift_key}
    analyze_manager = {ANALYZE_SHIFT: attack_shift}
    make_selection_window()
    while True:  # Event Loop
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == "Salir":
            window.close()
            if not close_window(window_manager, window):
                break
        elif event in window_manager and not window_manager[event]["window"]:
            window_manager[event]["window"] = window_manager[event]["create_fn"]()
        elif event in algorithms_manager:
            if "ENCRYPT" in event:
                encrypted_text, key = algorithms_manager[event](
                    values[KEY_INPUT], values[CLEAR_TEXT_INPUT_BOX]
                )
                window[ENCRYPTED_TEXT_INPUT_BOX].update(encrypted_text)
                window[KEY_INPUT].update(key)
            elif "DECRYPT" in event:
                clear_text, key = algorithms_manager[event](
                    values[KEY_INPUT], values[ENCRYPTED_TEXT_INPUT_BOX]
                )
                window[CLEAR_TEXT_INPUT_BOX].update(clear_text)
                window[KEY_INPUT].update(key)
        elif event in key_gen_manager:
            generated_key = key_gen_manager[event]()
            window[KEY_INPUT].update(generated_key)
        elif "DELETE" in event:
            if "CLEAR" in event:
                window[CLEAR_TEXT_INPUT_BOX].update("")
            else:
                window[ENCRYPTED_TEXT_INPUT_BOX].update("")
        elif "ANALYZE" in event:
            output = analyze_manager[event](values[ENCRYPTED_TEXT_INPUT_BOX])
            formatted_output = format_attack(output)
            sg.popup_scrolled(
                formatted_output,
                title="Resultados del análisis",
                size=(50, 10),
            )
