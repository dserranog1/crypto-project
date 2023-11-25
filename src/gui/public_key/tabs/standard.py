import PySimpleGUI as sg
from globals import *
from gui.common.custom_elements import (
    center_column,
    create_title,
    create_clear_text_box,
    create_encrypted_text_box,
    create_public_private_key_layout,
    create_encrypt_decrypt_buttons,
    create_algorithm_selection,
)


def create_standard_tab():
    return sg.Tab(
        "Estándar (Encriptar/Desencriptar)",
        [
            [create_title("Texto claro")],
            [center_column(create_clear_text_box(STANDARD))],
            [create_title("Texto encriptado")],
            [center_column(create_encrypted_text_box(STANDARD, has_analyze=False))],
            [create_public_private_key_layout(STANDARD)],
            [
                center_column(
                    [
                        [
                            sg.Button("Generar primos", key=STANDARD + PRIME_GEN),
                            sg.Button("Generar claves", key=STANDARD + KEY_GEN),
                        ],
                    ],
                ),
            ],
            [
                center_column(
                    [
                        create_encrypt_decrypt_buttons(STANDARD),
                    ]
                )
            ],
            [center_column([create_algorithm_selection(STANDARD)])],
        ],
    )
