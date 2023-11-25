import PySimpleGUI as sg
from utils.helpers import (
    format_input,
)

# tabs imports
from .tabs.standard import create_standard_tab
from .tabs.sign import create_sign_tab

# rsa imports
from public_key.rsa.cipher import rsa_encrypt, rsa_decrypt
from public_key.rsa.keygen import generate_key as rsa_keygen

# gamal imports
from public_key.gamal.cipher import gamal_encrypt, gamal_decrypt
from public_key.gamal.keygen import generate_key as gamal_keygen

# rabin imports
from public_key.rabin.cipher import rabin_encrypt, rabin_decrypt
from public_key.rabin.keygen import generate_key as rabin_keygen


from globals import *

# modes

public_key_algorithms_manager = {
    RSA: {
        ENCRYPT: rsa_encrypt,
        DECRYPT: rsa_decrypt,
        KEY_GEN: rsa_keygen,
    },
    GAMAL: {
        ENCRYPT: gamal_encrypt,
        DECRYPT: gamal_decrypt,
        KEY_GEN: gamal_keygen,
    },
    RABIN: {
        ENCRYPT: rabin_encrypt,
        DECRYPT: rabin_decrypt,
        KEY_GEN: rabin_keygen,
    },
}


def create_public_key_window():
    standard_tab = create_standard_tab()
    sign_tab = create_sign_tab()
    Tg = sg.TabGroup(
        [
            [
                standard_tab,
                sign_tab,
            ]
        ]
    )
    layout = [[Tg], [sg.Button("Salir")]]
    return sg.Window(
        PUBLIC_KEY, layout, location=(0, 0), finalize=True, disable_close=True
    )


def handle_public_key_window_event(window: sg.Window | None, event, values):
    standard_and_action = event.split("-", 1)
    if len(standard_and_action) == 2:
        _, action = standard_and_action[0], standard_and_action[1]
        algorithm_name = values[STANDARD + ALGORITHM]
        if action in ENCRYPT:
            algorithm_fn = public_key_algorithms_manager[algorithm_name][ENCRYPT]
            key = format_input(values[STANDARD + KEY_INPUT])
            print("formatted key ", key)
            input = values[STANDARD + CLEAR_TEXT_INPUT_BOX]
            encrypted_text, key = algorithm_fn(input, key)
            window[STANDARD + ENCRYPTED_TEXT_INPUT_BOX].update(encrypted_text)
            window[STANDARD + KEY_INPUT].update(key)
        elif action in DECRYPT:
            algorithm_fn = public_key_algorithms_manager[algorithm_name][DECRYPT]
            key = format_input(values[STANDARD + KEY_INPUT])
            input = values[STANDARD + CLEAR_TEXT_INPUT_BOX]
            encrypted_text, key = algorithm_fn(input, key)
            window[STANDARD + CLEAR_TEXT_INPUT_BOX].update(encrypted_text)
            window[STANDARD + KEY_INPUT].update(key)
        elif action in KEY_GEN:
            generated_key = public_key_algorithms_manager[algorithm_name][KEY_GEN]()
            window[STANDARD + KEY_INPUT].update(generated_key)
        elif (action in DELETE + CLEAR_TEXT_INPUT_BOX) or (
            action in DELETE + ENCRYPTED_TEXT_INPUT_BOX
        ):
            input_box = action.split("-", 1)[1]
            window[STANDARD + "-" + input_box].update("")
        elif action in ANALYZE:
            output = public_key_algorithms_manager[algorithm_name][ANALYZE](
                values[algorithm_name + ENCRYPTED_TEXT_INPUT_BOX]
            )
            # formatted_output = format_attack(output)
            sg.popup_scrolled(
                output,
                title="Resultados del análisis",
                size=(50, 10),
            )
