import PySimpleGUI as sg
from utils.helpers import format_input, is_valid_image_input

# tabs imports
from .tabs.aes_tab import create_aes_tab
from .tabs.des_tab import create_des_tab
from .tabs.tdes_tab import create_tdes_tab

# aes imports
from block.aes.cipher import aes_encrypt, aes_decrypt
from block.aes.keygen import generate_key as aes_keygen

# des imports
from block.des.cipher import des_encrypt, des_decrypt
from block.des.keygen import generate_key as des_keygen

# tdes imports
from block.tdes.cipher import t_des_encrypt, t_des_decrypt
from block.tdes.keygen import generate_key as tdes_keygen
from globals import *

# modes
from block.modes.cbc import cbc
from block.modes.cfb import cfb
from block.modes.ctr import ctr
from block.modes.ecb import ecb

block_algorithms_manager = {
    AES: {
        ENCRYPT: aes_encrypt,
        DECRYPT: aes_decrypt,
        KEY_GEN: aes_keygen,
    },
    DES: {
        ENCRYPT: des_encrypt,
        DECRYPT: des_decrypt,
        KEY_GEN: des_keygen,
    },
    TDES: {
        ENCRYPT: t_des_encrypt,
        DECRYPT: t_des_decrypt,
        KEY_GEN: tdes_keygen,
    },
    CBC: cbc,
    CFB: cfb,
    CTR: ctr,
    ECB: ecb,
}


def create_block_window():
    aes_tab = create_aes_tab()
    des_tab = create_des_tab()
    t_des_tab = create_tdes_tab()
    Tg = sg.TabGroup(
        [
            [
                aes_tab,
                des_tab,
                t_des_tab,
            ]
        ]
    )
    layout = [[Tg], [sg.Button("Salir")]]
    return sg.Window(BLOCK, layout, location=(0, 0), finalize=True, disable_close=True)


def handle_block_window_event(window: sg.Window | None, event, values):
    algorithm_and_action = event.split("-", 1)
    algorithm_name, action = algorithm_and_action[0], algorithm_and_action[1]
    if algorithm_and_action[0] in block_algorithms_manager:
        if action in ENCRYPT:
            mode = block_algorithms_manager[values[algorithm_name + MODE]]
            algorithm_fn = block_algorithms_manager[algorithm_name][ENCRYPT]
            key = format_input(values[algorithm_name + KEY_INPUT])
            input = values[algorithm_name + CLEAR_TEXT_INPUT_BOX]
            encrypted_text, key = mode(input, key, algorithm_fn)
            window[algorithm_name + ENCRYPTED_TEXT_INPUT_BOX].update(encrypted_text)
            window[algorithm_name + KEY_INPUT].update(key)
        elif action in DECRYPT:
            mode = block_algorithms_manager[values[algorithm_name + MODE]]
            algorithm_fn = block_algorithms_manager[algorithm_name][DECRYPT]
            key = format_input(values[algorithm_name + KEY_INPUT])
            input = values[algorithm_name + ENCRYPTED_TEXT_INPUT_BOX]
            clear_text, key = mode(input, key, algorithm_fn)
            window[algorithm_name + CLEAR_TEXT_INPUT_BOX].update(clear_text)
            window[algorithm_name + KEY_INPUT].update(key)
        elif action in KEY_GEN:
            generated_key = block_algorithms_manager[algorithm_name][KEY_GEN]()
            window[algorithm_name + KEY_INPUT].update(generated_key)
        elif (action in DELETE + CLEAR_TEXT_INPUT_BOX) or (
            action in DELETE + ENCRYPTED_TEXT_INPUT_BOX
        ):
            input_box = action.split("-", 1)[1]
            window[algorithm_name + "-" + input_box].update("")
        elif action in ANALYZE:
            output = block_algorithms_manager[algorithm_name][ANALYZE](
                values[algorithm_name + ENCRYPTED_TEXT_INPUT_BOX]
            )
            # formatted_output = format_attack(output)
            sg.popup_scrolled(
                output,
                title="Resultados del análisis",
                size=(50, 10),
            )
