import PySimpleGUI as sg
from gui.classic_algorithms.tabs.shift_tab import create_shift_tab
from gui.classic_algorithms.tabs.permutation_tab import create_permutation_tab
from gui.classic_algorithms.tabs.vigenere_tab import create_vigenere_tab
from gui.classic_algorithms.tabs.hill_tab import create_hill_tab
from gui.classic_algorithms.tabs.substitution_tab import create_substitution_tab
from gui.classic_algorithms.tabs.affine_tab import create_affine_tab

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
    return sg.Window("Criptonita", layout, location=(0, 0), finalize=True, disable_close=True)
