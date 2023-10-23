import PySimpleGUI as sg
from globals import *
from gui.common.custom_elements import (
    center_column,
    create_title,
    create_clear_text_box,
    create_encrypted_text_box,
    create_key_layout,
    create_encrypt_decrypt_buttons,
    create_select_mode,
)


def create_tdes_tab():
    return sg.Tab(
        "Algoritmo T-DES",
        [
            [create_title("Texto claro")],
            [center_column(create_clear_text_box(TDES))],
            [create_title("Texto encriptado")],
            [center_column(create_encrypted_text_box(TDES, has_analyze=False))],
            create_key_layout(TDES),
            [center_column([create_encrypt_decrypt_buttons(TDES)])],
            [center_column([create_select_mode(TDES)])],
        ],
    )
