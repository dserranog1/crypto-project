import PySimpleGUI as sg
from globals import *
from gui.common.custom_elements import (
    center_column,
    create_title,
    create_clear_text_box,
    create_encrypted_text_box,
    create_key_layout,
    create_encrypt_decrypt_buttons,
    create_algorithm_selection,
)


def create_sign_tab():
    return sg.Tab(
        "Firmar",
        [
            [create_title("Texto claro")],
            [center_column(create_clear_text_box(SIGN))],
            [create_title("Texto encriptado")],
            [center_column(create_encrypted_text_box(SIGN, has_analyze=False))],
            create_key_layout(SIGN),
            [
                center_column(
                    [
                        create_encrypt_decrypt_buttons(SIGN),
                    ]
                )
            ],
            [center_column([create_algorithm_selection(SIGN)])],
        ],
    )
