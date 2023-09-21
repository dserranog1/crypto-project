import PySimpleGUI as sg


def create_classics_window():
    afin_tab = sg.Tab("Algoritmo afín", [[sg.Text('Afin logic goes here')]])
    desplazamiento_tab = sg.Tab("Algoritmo desplazamiento", [
                                [sg.Text('Desplazamiento logic goes here')]])
    vigenere_tab = sg.Tab("Algoritmo Vigenere", [
        [sg.Text('Vigenere logic goes here')]])
    sustitucion_tab = sg.Tab("Algoritmo sustitucion", [
        [sg.Text('Sustitucion logic goes here')]])
    hill_tab = sg.Tab("Algoritmo hill", [
        [sg.Text('Hill logic goes here')]])
    Tg = sg.TabGroup(
        [[afin_tab, desplazamiento_tab, vigenere_tab, sustitucion_tab, hill_tab]])
    layout = [[Tg], [sg.Button('Salir')]]
    return sg.Window('Criptonita', layout, location=(3400, 100), finalize=True)
