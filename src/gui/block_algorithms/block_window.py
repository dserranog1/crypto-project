import PySimpleGUI as sg
from utils.helpers import (
    format_input,
    is_valid_clear_image_input,
    is_valid_encrypted_image_input,
    image_to_hex,
    heximage_to_listimage,
)
from utils.text_to_image import image_to_list, list_to_image

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
    if algorithm_and_action[0] in block_algorithms_manager:
        algorithm_name, action = algorithm_and_action[0], algorithm_and_action[1]
        if action in ENCRYPT:
            mode = block_algorithms_manager[values[algorithm_name + MODE]]
            algorithm_fn = block_algorithms_manager[algorithm_name][ENCRYPT]
            key = format_input(values[algorithm_name + KEY_INPUT])
            input = values[algorithm_name + CLEAR_TEXT_INPUT_BOX]
            encrypted_text, key = mode(input, key, algorithm_fn, algorithm_name)
            window[algorithm_name + ENCRYPTED_TEXT_INPUT_BOX].update(encrypted_text)
            window[algorithm_name + KEY_INPUT].update(key)
        elif action in DECRYPT:
            mode = block_algorithms_manager[values[algorithm_name + MODE]]
            algorithm_fn = block_algorithms_manager[algorithm_name][DECRYPT]
            key = format_input(values[algorithm_name + KEY_INPUT])
            input = values[algorithm_name + ENCRYPTED_TEXT_INPUT_BOX]
            clear_text, key = mode(input, key, algorithm_fn, algorithm_name)
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
    elif algorithm_and_action[0] == "AES_IMAGE_ENCRYPT":
        file = sg.popup_get_file(
            "Seleccion la imagen por favor (JPG, JPEG)",
            "Seleccione una imagen",
        )
        if not file:
            return  # ojo aqui
        while not is_valid_clear_image_input(file):
            sg.popup_error("Formato invalido")
            file = sg.popup_get_file(
                "Seleccion la imagen por favor (JPG, JPEG)",
                "Seleccione una imagen",
            )
            if not file:
                break
        if not file:
            return
        # begin encryption
        image, original_shape = image_to_list(file)
        input_key = values[AES_KEY_INPUT]
        if not input_key:
            input_key = aes_keygen()
        original_length = len(image)
        image_as_hex = image_to_hex(image)
        mode = block_algorithms_manager[values[AES + MODE]]
        encrypted_image_as_hex, key = mode(image_as_hex, input_key, aes_encrypt, "AES")
        encrypted_image = heximage_to_listimage(encrypted_image_as_hex)
        # Aditional items might've been added to complete the encryption, so we go back to the original size
        encrypted_image = encrypted_image[:original_length]
        list_to_image(encrypted_image, original_shape, "aes_encrypted_image")
        # end encryption
        window[AES_KEY_INPUT].update(key)
    elif algorithm_and_action[0] == "AES_IMAGE_DECRYPT":
        file = sg.popup_get_file(
            "Seleccion la imagen por favor (PNG)",
            "Seleccione una imagen",
        )
        if not file:
            return
        while not is_valid_encrypted_image_input(file):
            sg.popup_error("Formato invalido", title="Ok")
            file = sg.popup_get_file(
                "Seleccion la imagen por favor (PNG)",
                "Seleccione una imagen",
            )
            if not file:
                break
        if not file:
            return
        # begin decryption
        image, original_shape = image_to_list(file)
        input_key = values[AES_KEY_INPUT]
        if not input_key:
            input_key = aes_keygen()
        original_length = len(image)
        image_as_hex = image_to_hex(image)
        mode = block_algorithms_manager[values[AES + MODE]]
        encrypted_image_as_hex, key = mode(image_as_hex, input_key, aes_decrypt, "AES")
        encrypted_image = heximage_to_listimage(encrypted_image_as_hex)
        # Aditional items might've been added to complete the encryption, so we go back to the original size
        encrypted_image = encrypted_image[:original_length]
        list_to_image(encrypted_image, original_shape, "aes_decrypted_image")
        # end decryption
        window[AES_KEY_INPUT].update(key)
