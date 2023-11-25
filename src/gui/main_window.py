import PySimpleGUI as sg
from gui.classic_algorithms.classic_window import (
    create_classics_window,
    handle_classics_window_event,
)
from globals import *
from gui.block_algorithms.block_window import (
    create_block_window,
    handle_block_window_event,
)
from gui.common.custom_elements import center_column
from gui.public_key.public_key_window import (
    create_public_key_window,
    handle_public_key_window_event,
)


def make_selection_window():
    layout = [
        [
            sg.Text(
                "Bienvenido a EnigmaVault, por favor selecione una categoría para comenzar"
            ),
        ],
        [
            center_column(
                [
                    [sg.Button("Algoritmos clásicos", key=CLASSICS)],
                    [sg.Button("Algoritmos bloque", key=BLOCK)],
                    [sg.Button("Algoritmos de clave pública", key=PUBLIC_KEY)],
                ]
            )
        ],
        [center_column([[sg.Button("Salir")]])],
    ]
    return sg.Window(
        "EnigmaVault", layout, location=(0, 0), finalize=True, disable_close=True
    )


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
        BLOCK: {"create_fn": create_block_window, "window": None},
        PUBLIC_KEY: {"create_fn": create_public_key_window, "window": None},
    }

    make_selection_window()
    while True:  # Event Loop
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == "Salir":
            window.close()
            if not close_window(window_manager, window):
                break
        elif event in window_manager and not window_manager[event]["window"]:
            window_manager[event]["window"] = window_manager[event]["create_fn"]()
        elif window.Title == CLASSICS:
            handle_classics_window_event(window, event, values)
        elif window.Title == BLOCK:
            handle_block_window_event(window, event, values)
        elif window.Title == PUBLIC_KEY:
            handle_public_key_window_event(window, event, values)
