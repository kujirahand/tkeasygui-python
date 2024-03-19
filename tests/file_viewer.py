import os

import tkeasygui as sg

# import PySimpleGUI as sg

# set path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# get font
font = ("Arial", 16)

def get_program_files():
    files = os.listdir(ROOT_DIR)
    files = [f for f in files if f.endswith('.py')]
    return files

layout = [
    [sg.Text("Programs:")],
    [
        sg.Listbox( 
            values=get_program_files(), 
            size=(40, 20), 
            key="-files-", 
            enable_events=True,
            font=font
        ),
        # right side textbox
        sg.Multiline(size=(40, 20), key="-body-", font=font, expand_y=True)
    ],
    [
        sg.Button("Close", font=font)
    ],
]
window = sg.Window("Python file Viewer", layout)
# event loop
while True:
    event, values = window.read()
    if event in [sg.WINDOW_CLOSED, "Close"]:
        break
    if event == "-files-":
        filename = values["-files-"][0]
        filepath = os.path.join(ROOT_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
            window["-body-"].update(text)
window.close()
