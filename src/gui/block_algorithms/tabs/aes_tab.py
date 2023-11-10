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


def create_aes_tab():
    return sg.Tab(
        "Algoritmo AES",
        [
            [create_title("Texto claro")],
            [center_column(create_clear_text_box(AES))],
            [create_title("Texto encriptado")],
            [center_column(create_encrypted_text_box(AES, has_analyze=False))],
            create_key_layout(AES),
            [
                center_column(
                    [
                        create_encrypt_decrypt_buttons(AES),
                        [
                            sg.Button(
                                "Encriptar imagen",
                                key="AES_IMAGE_ENCRYPT",
                            ),
                            sg.Button("Desencriptar imagen", key="AES_IMAGE_DECRYPT"),
                        ],
                    ]
                )
            ],
            [center_column([create_select_mode(AES)])],
        ],
    )
