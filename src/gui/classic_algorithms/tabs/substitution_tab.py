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


def create_substitution_tab():
    return sg.Tab(
        "Algoritmo sustitución",
        [
            [create_title("Texto claro")],
            [center_column(create_clear_text_box(SUBSTITUTION))],
            [create_title("Texto encriptado")],
            [center_column(create_encrypted_text_box(SUBSTITUTION, has_analyze=True))],
            create_key_layout(SUBSTITUTION),
            [center_column([create_encrypt_decrypt_buttons(SUBSTITUTION)])],
        ],
    )
