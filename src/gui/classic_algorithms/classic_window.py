import PySimpleGUI as sg
from globals import *
from utils.helpers import (
    format_input,
    is_valid_clear_image_input,
    is_valid_encrypted_image_input,
)
from utils.text_to_image import image_to_list, list_to_image

# tabs imports
from .tabs.shift_tab import create_shift_tab
from .tabs.permutation_tab import create_permutation_tab
from .tabs.vigenere_tab import create_vigenere_tab
from .tabs.hill_tab import create_hill_tab
from .tabs.substitution_tab import create_substitution_tab
from .tabs.affine_tab import create_affine_tab

# shift imports
from classic.shift.keygen import generate_key as generate_shift_key
from classic.shift.cipher import (
    cifrado_desplazamiento,
    descifrado_desplazamiento,
    attack as analyze_shift,
)

# permutation imports
from classic.permutation.cipher import cifrado_permutacion, descifrado_permutacion
from classic.permutation.keygen import generate_key as generate_permutation_key

# vigenere imports
from classic.vigenere.cipher import cifrado_vigenere, descifrado_vigenere
from classic.vigenere.keygen import generar_clave as generar_clave_vigenere

# substitution imports
from classic.substitution.cipher import sustitucion_cripter, sustitucion_desencriptar
from classic.substitution.keygen import generate_key as generate_substitution_key

# affine imports
from classic.affine.cipher import cifrado_afin, descifrado_afin
from classic.affine.keygen import generate_key as generate_affine_key

# hill imports
from classic.hill.cipher import (
    encryption_algorithm as hill_encrypt,
    decryption_algorithm as hill_decrypt,
    encrypt_image,
    decrypt_image,
)
from classic.hill.keygen import generate_key as hill_keygen

"""
    Encryption and decryption algorithms must have the following structure

    encryption_algorithm(key: str, message: str):
        # logic goes here

        return encrypted_message, key
    
    decryption_algorithm(key: str, message: str):
        # logic goes here

        return decrypted_message, key

    Key should be validated and in case no key was provided, generate one, hence the return of the key too.
"""

"""
    The analyze function must have the following structure
    
    analyze_message_algorithm(message):
        # logic goes here

        return [{'clave': key0, 'texto_descifrado'}, {'clave': key1, 'texto_descifrado': 'decrypted_text_with_key1'}
        ..
        ..
        ..
        {'clave': keyN, 'texto_descifrado': 'decrypted_text_with_keyN'}]

    For proper formatting the analysis MUST be returned with the above-mentioned form.
    """

# clave publica: RSA, Gavin, Gamal

classic_algorithms_manager = {
    SHIFT: {
        ENCRYPT: cifrado_desplazamiento,
        DECRYPT: descifrado_desplazamiento,
        KEY_GEN: generate_shift_key,
        ANALYZE: analyze_shift,
    },
    PERMUTATION: {
        ENCRYPT: cifrado_permutacion,
        DECRYPT: descifrado_permutacion,
        KEY_GEN: generate_permutation_key,
    },
    VIGENERE: {
        ENCRYPT: cifrado_vigenere,
        DECRYPT: descifrado_vigenere,
        KEY_GEN: generar_clave_vigenere,
    },
    HILL: {
        ENCRYPT: hill_encrypt,
        DECRYPT: hill_decrypt,
        KEY_GEN: hill_keygen,
    },
    SUBSTITUTION: {
        ENCRYPT: sustitucion_cripter,
        DECRYPT: sustitucion_desencriptar,
        KEY_GEN: generate_substitution_key,
    },
    AFFINE: {
        ENCRYPT: cifrado_afin,
        DECRYPT: descifrado_afin,
        KEY_GEN: generate_affine_key,
    },
}


def create_classics_window():
    afin_tab = create_affine_tab()
    desplazamiento_tab = create_shift_tab()
    permutacion_tab = create_permutation_tab()
    vigenere_tab = create_vigenere_tab()
    sustitucion_tab = create_substitution_tab()
    hill_tab = create_hill_tab()
    Tg = sg.TabGroup(
        [
            [
                afin_tab,
                desplazamiento_tab,
                permutacion_tab,
                vigenere_tab,
                sustitucion_tab,
                hill_tab,
            ]
        ]
    )
    layout = [[Tg], [sg.Button("Salir")]]
    return sg.Window(
        CLASSICS, layout, location=(0, 0), finalize=True, disable_close=True
    )


def handle_classics_window_event(window: sg.Window | None, event, values):
    algorithm_and_action = event.split("-", 1)
    if algorithm_and_action[0] in classic_algorithms_manager:
        algorithm, action = algorithm_and_action[0], algorithm_and_action[1]
        if action in ENCRYPT:
            encrypted_text, key = classic_algorithms_manager[algorithm][ENCRYPT](
                format_input(values[algorithm + KEY_INPUT]),
                values[algorithm + CLEAR_TEXT_INPUT_BOX],
            )
            window[algorithm + ENCRYPTED_TEXT_INPUT_BOX].update(encrypted_text)
            window[algorithm + KEY_INPUT].update(key)
        elif action in DECRYPT:
            clear_text, key = classic_algorithms_manager[algorithm][DECRYPT](
                format_input(values[algorithm + KEY_INPUT]),
                values[algorithm + ENCRYPTED_TEXT_INPUT_BOX],
            )
            window[algorithm + CLEAR_TEXT_INPUT_BOX].update(clear_text)
            window[algorithm + KEY_INPUT].update(key)
        elif action in KEY_GEN:
            generated_key = classic_algorithms_manager[algorithm][KEY_GEN]()
            window[algorithm + KEY_INPUT].update(generated_key)
        elif (action in DELETE + CLEAR_TEXT_INPUT_BOX) or (
            action in DELETE + ENCRYPTED_TEXT_INPUT_BOX
        ):
            input_box = action.split("-", 1)[1]
            window[algorithm + "-" + input_box].update("")
        elif action in ANALYZE:
            output = classic_algorithms_manager[algorithm][ANALYZE](
                values[algorithm + ENCRYPTED_TEXT_INPUT_BOX]
            )
            # formatted_output = format_attack(output)
            sg.popup_scrolled(
                output,
                title="Resultados del análisis",
                size=(50, 10),
            )
    elif algorithm_and_action[0] == "HILL_IMAGE_ENCRYPT":
        file = sg.popup_get_file(
            "Seleccion la imagen por favor (PNG, JPG, JPEG)",
            "Seleccione una imagen",
        )
        if not file:
            return  # ojo aqui
        while not is_valid_clear_image_input(file):
            sg.popup_error("Formato invalido")
            file = sg.popup_get_file(
                "Seleccion la imagen por favor (PNG, JPG, JPEG)",
                "Seleccione una imagen",
            )
            if not file:
                break
        # begin encryption
        image, original_shape = image_to_list(file)
        input_key = values[HILL_KEY_INPUT]
        if not input_key:
            input_key = hill_keygen(is_image=True)
        original_length = len(image)
        encrypted_image, key = encrypt_image(input_key, image)
        # Aditional items might've been added to complete the encryption, so we go back to the original size
        encrypted_image = encrypted_image[:original_length]
        list_to_image(encrypted_image, original_shape, "encrypted_image")
        # end encryption
        window[HILL_KEY_INPUT].update(key)
    elif algorithm_and_action[0] == "HILL_IMAGE_DECRYPT":
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
        # begin decryption
        image, original_shape = image_to_list(file)
        input_key = values[HILL_KEY_INPUT]
        if not input_key:
            input_key = hill_keygen(is_image=True)
        original_length = len(image)
        decrypted_image, key = decrypt_image(input_key, image)
        # Aditional items might've been added to complete the encryption, so we go back to the original size
        decrypted_image = decrypted_image[:original_length]
        list_to_image(decrypted_image, original_shape, "decrypted_image")
        # end decryption
        window[HILL_KEY_INPUT].update(key)
