import os
import glob
import subprocess
from threading import Thread

# import PySimpleGUI as sg
import tkeasygui as sg

# set path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# get font
font = ("Arial", 20)

def get_program_files():
    files = os.listdir(ROOT_DIR)
    files = [f for f in files if f.endswith('.py')]
    files = list(sorted(files))
    return files

def run_program(filename):
    subprocess.run(["python", filename])

layout = [
    [sg.Text("TkEasyGUI samples:")],
    [
        # left sizde listbox
        sg.Listbox( 
            values=get_program_files(), 
            size=(30, 20), 
            key="-files-", 
            enable_events=True,
        ),
        sg.VSeparator(pad=5),
        # right side textbox
        sg.Multiline(size=(40, 20), key="-body-", expand_y=True, expand_x=True)
    ],
    [sg.HSeparator(pad=5)],
    [
        sg.Button("Run Program"),
        sg.Button("Close"),
    ],
]
window = sg.Window("Python Viewer", layout, font=font)
# event loop
while True:
    event, values = window.read()
    print("#", event, values)
    if event in [sg.WINDOW_CLOSED, "Close"]:
        break
    if event == "Run Program":
        files = values["-files-"]
        if len(files) > 0:
            filename = values["-files-"][0]
            fullpath = os.path.join(ROOT_DIR, filename)
            Thread(target=run_program, args=(fullpath,)).start()
    if event == "-files-":
        files = values["-files-"]
        if len(files) > 0:
            filename = values["-files-"][0]
            fullpath = os.path.join(ROOT_DIR, filename)
            with open(fullpath, "r", encoding="utf-8") as f:
                text = f.read()
                window["-body-"].update(text)
window.close()
