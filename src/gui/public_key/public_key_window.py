import PySimpleGUI as sg
from utils.helpers import format_input, generate_prime_number

# tabs imports
from .tabs.standard import create_standard_tab
from .tabs.sign import create_sign_tab

# rsa imports
from public_key.rsa.cipher import (
    rsa_encrypt,
    rsa_decrypt,
    invalid_key as rsa_invalid_key,
)
from public_key.rsa.keygen import generate_key as rsa_keygen

# gamal imports
from public_key.gamal.cipher import (
    gamal_encrypt,
    gamal_decrypt,
    invalid_key as gamal_invalid_key,
)
from public_key.gamal.keygen import generate_key as gamal_keygen

# rabin imports
from public_key.rabin.cipher import (
    rabin_encrypt,
    rabin_decrypt,
    invalid_key as rabin_invalid_key,
)
from public_key.rabin.keygen import generate_key as rabin_keygen


def generate_and_update_keys(window, values, algorithm_name):
    primes = format_input(values[STANDARD + KEY_INPUT])
    p, q, private, public = public_key_algorithms_manager[algorithm_name][KEY_GEN](
        primes
    )
    window[STANDARD + KEY_INPUT].update(str(p) + ", " + str(q))
    window[STANDARD + PRIVATE + KEY_INPUT].update(private)
    window[STANDARD + PUBLIC + KEY_INPUT].update(public)
    return p, q, private, public


from globals import *

# modes

public_key_algorithms_manager = {
    RSA: {
        ENCRYPT: rsa_encrypt,
        DECRYPT: rsa_decrypt,
        KEY_GEN: rsa_keygen,
        VALID_KEY: rsa_invalid_key,
    },
    GAMAL: {
        ENCRYPT: gamal_encrypt,
        DECRYPT: gamal_decrypt,
        KEY_GEN: gamal_keygen,
        VALID_KEY: gamal_invalid_key,
    },
    RABIN: {
        ENCRYPT: rabin_encrypt,
        DECRYPT: rabin_decrypt,
        KEY_GEN: rabin_keygen,
        VALID_KEY: rabin_invalid_key,
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
        tab_name, action = standard_and_action[0], standard_and_action[1]
        if tab_name == STANDARD:
            algorithm_name = values[STANDARD + ALGORITHM]
            if action in ENCRYPT:
                algorithm_fn = public_key_algorithms_manager[algorithm_name][ENCRYPT]
                private = ""
                key = format_input(values[STANDARD + PUBLIC + KEY_INPUT])
                if not key or not public_key_algorithms_manager[algorithm_name][
                    VALID_KEY
                ](key, False):
                    p, q, private, public = generate_and_update_keys(
                        window, values, algorithm_name
                    )
                    key = public

                input = values[STANDARD + CLEAR_TEXT_INPUT_BOX]
                clear_text, key = algorithm_fn(input, key)
                window[STANDARD + ENCRYPTED_TEXT_INPUT_BOX].update(clear_text)
            elif action in DECRYPT:
                algorithm_fn = public_key_algorithms_manager[algorithm_name][DECRYPT]
                public = ""
                key = format_input(values[STANDARD + PRIVATE + KEY_INPUT])
                if not key or not public_key_algorithms_manager[algorithm_name][
                    VALID_KEY
                ](key, True):
                    p, q, private, public = generate_and_update_keys(
                        window, values, algorithm_name
                    )
                    key = private
                input = values[STANDARD + ENCRYPTED_TEXT_INPUT_BOX]
                clear_text, key = algorithm_fn(input, key)
                window[STANDARD + CLEAR_TEXT_INPUT_BOX].update(clear_text)
            elif action in PRIME_GEN:
                p = generate_prime_number()
                q = generate_prime_number()
                window[STANDARD + KEY_INPUT].update(str(p) + ", " + str(q))
            elif action in KEY_GEN:
                primes = format_input(values[STANDARD + KEY_INPUT])
                p, q, private, public = public_key_algorithms_manager[algorithm_name][
                    KEY_GEN
                ](primes)
                window[STANDARD + KEY_INPUT].update(str(p) + ", " + str(q))
                window[STANDARD + PRIVATE + KEY_INPUT].update(private)
                window[STANDARD + PUBLIC + KEY_INPUT].update(public)
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
        elif tab_name == SIGN:
            algorithm_name = values[SIGN + ALGORITHM]
            if action in ENCRYPT:
                algorithm_fn = public_key_algorithms_manager[algorithm_name][ENCRYPT]
                private = ""
                key = format_input(values[SIGN + PUBLIC + KEY_INPUT])
                if not key or public_key_algorithms_manager[algorithm_name][VALID_KEY](
                    key
                ):
                    p, q, private, public = generate_and_update_keys(
                        window, values, algorithm_name
                    )
                    key = private
                input = values[SIGN + CLEAR_TEXT_INPUT_BOX]
                clear_text, key = algorithm_fn(input, key)
                window[SIGN + ENCRYPTED_TEXT_INPUT_BOX].update(clear_text)
            elif action in DECRYPT:
                algorithm_fn = public_key_algorithms_manager[algorithm_name][DECRYPT]
                public = ""
                key = format_input(values[SIGN + PRIVATE + KEY_INPUT])
                if not key or public_key_algorithms_manager[algorithm_name][VALID_KEY](
                    key
                ):
                    p, q, private, public = generate_and_update_keys(
                        window, values, algorithm_name
                    )
                    key = public
                input = values[SIGN + ENCRYPTED_TEXT_INPUT_BOX]
                clear_text, key = algorithm_fn(input, key)
                window[SIGN + CLEAR_TEXT_INPUT_BOX].update(clear_text)
            elif action in PRIME_GEN:
                p = generate_prime_number()
                q = generate_prime_number()
                window[SIGN + KEY_INPUT].update(str(p) + ", " + str(q))
            elif action in KEY_GEN:
                primes = format_input(values[SIGN + KEY_INPUT])
                p, q, private, public = public_key_algorithms_manager[algorithm_name][
                    KEY_GEN
                ](primes)
                window[SIGN + KEY_INPUT].update(str(p) + ", " + str(q))
                window[SIGN + PRIVATE + KEY_INPUT].update(private)
                window[SIGN + PUBLIC + KEY_INPUT].update(public)
            elif (action in DELETE + CLEAR_TEXT_INPUT_BOX) or (
                action in DELETE + ENCRYPTED_TEXT_INPUT_BOX
            ):
                input_box = action.split("-", 1)[1]
                window[SIGN + "-" + input_box].update("")
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
