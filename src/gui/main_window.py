import PySimpleGUI as sg
from gui.classic_algorithms.classic_window import create_classics_window
from gui.common.custom_elements import center_column

# KEYS
CLASSICS_KEY = 'classics'
SELECTION_KEY = 'selection'
OTRO_KEY = 'otro'


def make_selection_window():
    layout = [[sg.Text('Bienvenido, por favor selecione una categoría para comenzar')],
              [center_column([[sg.Button('Algoritmos clásicos', key=CLASSICS_KEY)],
                             [sg.Button('Algoritmos otro', key=OTRO_KEY)]])],
              [center_column([[sg.Button('Salir')]])]]
    return sg.Window('Criptonita', layout, location=(3400, 100), finalize=True)


def make_win2():
    layout = [[sg.Text('The second window')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25, 1), k='-OUTPUT-')],
              [sg.Button('Erase'), sg.Button('Popup'), sg.Button('Salir')]]
    return sg.Window('Second Window', layout, finalize=True)


def close_window(window_manager, window):
    for window_key in window_manager:
        if window_manager[window_key]['window'] == window:
            window_manager[window_key]['window'] = None
            return True
    return False


def init_main_window():
    sg.theme('DarkGrey13')
    window_manager = {CLASSICS_KEY: {'create_fn': create_classics_window, 'window': None},
                      OTRO_KEY: {'create_fn': make_win2, 'window': None}, }
    make_selection_window()
    while True:  # Event Loop
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Salir':
            window.close()
            if not close_window(window_manager, window):
                break
        elif event in window_manager and not window_manager[event]['window']:
            window_manager[event]['window'] = window_manager[event]['create_fn']()
