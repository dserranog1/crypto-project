import PySimpleGUI as sg
from globals import *


def center_column(layout):
    return sg.Column(layout, justification="center")


def create_title(text):
    return sg.Text(
        text,
        expand_x=True,
        expand_y=True,
        pad=((0, 0), (20, 0)),
        font=("", 14, "bold"),
        justification="center",
    )


def create_clear_text_box(algorithm):
    return [
        [sg.Multiline("", key=algorithm + CLEAR_TEXT_INPUT_BOX, size=(40, 10))],
        [
            sg.Button(
                "Limpiar",
                key=algorithm + DELETE + CLEAR_TEXT_INPUT_BOX,
                pad=((0, 0), (5, 20)),
            )
        ],
    ]


def create_encrypted_text_box(algorithm, has_analyze=True):
    if has_analyze:
        return [
            [sg.Multiline("", key=algorithm + ENCRYPTED_TEXT_INPUT_BOX, size=(40, 10))],
            [
                sg.Button(
                    "Limpiar",
                    key=algorithm + DELETE + ENCRYPTED_TEXT_INPUT_BOX,
                    pad=((0, 0), (5, 20)),
                ),
                sg.Button("Analizar", key=algorithm + ANALYZE, pad=((0, 0), (5, 20))),
            ],
        ]
    return [
        [sg.Multiline("", key=algorithm + ENCRYPTED_TEXT_INPUT_BOX, size=(40, 10))],
        [
            sg.Button(
                "Limpiar",
                key=algorithm + DELETE + ENCRYPTED_TEXT_INPUT_BOX,
                pad=((0, 0), (5, 20)),
            ),
        ],
    ]


def create_key_layout(algorithm):
    return [
        sg.Text("Clave", pad=((0, 0), (20, 20))),
        sg.Input(key=algorithm + KEY_INPUT),
        sg.Button("Generar clave", key=algorithm + KEY_GEN),
    ]


def create_encrypt_decrypt_buttons(algorithm):
    return [
        sg.Button("Encriptar", key=algorithm + ENCRYPT),
        sg.Button("Desencriptar", key=algorithm + DECRYPT),
    ]


def create_select_mode(algorithm):
    modes = ["CBC", "CFB", "CTR", "ECB"]
    return [
        sg.Text("Seleccione el modo"),
        sg.Combo(modes, key=algorithm + MODE, readonly=True, default_value=modes[3]),
    ]


def create_algorithm_selection(mode):
    algorithms = [RSA, RABIN, GAMAL]
    return [
        sg.Text("Seleccione el algoritmo"),
        sg.Combo(
            algorithms, key=mode + ALGORITHM, readonly=True, default_value=algorithms[0]
        ),
    ]


def create_public_private_key_layout(algorithm):
    return sg.Column(
        [
            [
                sg.Text("Primos", pad=((0, 0), (20, 20))),
                sg.Input(key=algorithm + KEY_INPUT),
            ],
            [
                sg.Text("Clave privada", pad=((0, 0), (20, 20))),
                sg.Input(key=algorithm + PRIVATE + KEY_INPUT),
            ],
            [
                sg.Text("Clave publica", pad=((0, 0), (20, 20))),
                sg.Input(key=algorithm + PUBLIC + KEY_INPUT),
            ],
        ]
    )
