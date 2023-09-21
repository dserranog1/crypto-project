import PySimpleGUI as sg


def center_column(layout):
    return sg.Column(layout, justification='center')


def create_title(text):
    return sg.Text(text, expand_x=True, expand_y=True, pad=((0, 0), (20, 0)), font=('', 14, 'bold'), justification='center')


def create_clear_text_box():
    return sg.Multiline(
        '', key='-CLEAR-INPUT-BOX', size=(40, 10))


def create_encrypted_text_box():
    return sg.Multiline(
        '', key='-ENCRYPTED-INPUT-BOX', size=(40, 10))


def create_key_layout():
    return [sg.Text('Clave', pad=((0, 0), (20, 20))), sg.Input(key='-KEY-INPUT-BOX'),
            sg.Button('Generar clave')]


def create_encrypt_decrypt_buttons(id):
    return [sg.Button('Encriptar', key='-CIPHER-'+id+'-'),
            sg.Button('Desencriptar', key='-DECRYPT-'+id+'-')]
