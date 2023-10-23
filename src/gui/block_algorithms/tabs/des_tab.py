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


def create_des_tab():
    return sg.Tab(
        "Algoritmo DES",
        [
            [create_title("Texto claro")],
            [center_column(create_clear_text_box(DES))],
            [create_title("Texto encriptado")],
            [center_column(create_encrypted_text_box(DES, has_analyze=False))],
            create_key_layout(DES),
            [center_column([create_encrypt_decrypt_buttons(DES)])],
            [center_column([create_select_mode(DES)])],
        ],
    )
