import PySimpleGUI as sg
from globals import *
from gui.common.custom_elements import (
    center_column,
    create_title,
    create_clear_text_box,
    create_encrypted_text_box,
    create_key_layout,
    create_encrypt_decrypt_buttons,
)


def create_permutation_tab():
    return sg.Tab(
        "Algoritmo permutación",
        [
            [create_title("Texto claro")],
            [center_column(create_clear_text_box(PERMUTATION))],
            [create_title("Texto encriptado")],
            [center_column(create_encrypted_text_box(PERMUTATION))],
            create_key_layout(PERMUTATION),
            [center_column([create_encrypt_decrypt_buttons(PERMUTATION)])],
        ],
    )
