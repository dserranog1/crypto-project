import PySimpleGUI as sg
from gui.common.custom_elements import center_column, create_title, create_clear_text_box, create_encrypted_text_box, create_key_layout, create_encrypt_decrypt_buttons


def create_shift_tab():
    return sg.Tab("Algoritmo deplazamiento", [
        [create_title('Texto claro')], [center_column([[create_clear_text_box()]])], [
            create_title('Texto encriptado')], [center_column([[create_encrypted_text_box()]])],
        create_key_layout('SHIFT'),
        [center_column([create_encrypt_decrypt_buttons('SHIFT')])]])
