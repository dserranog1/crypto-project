import PySimpleGUI as sg
from .tabs.aes_tab import create_aes_tab
from .tabs.des_tab import create_des_tab
from .tabs.tdes_tab import create_tdes_tab
from globals import *


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
