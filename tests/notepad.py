"""
### Notepad sample

This is a simple notepad application. You can save and open text.
"""

import os

import TkEasyGUI as eg

# set path
SCRIPT_DIR = os.path.dirname(__file__)
SAVE_FILE = os.path.join(SCRIPT_DIR, "notepad-save-data.txt")

# create window
layout = [
    [eg.Multiline(size=(40, 15), key="text")],
    [eg.Button("Save"), eg.Button("Open"), eg.Button("Exit")],
]
window = eg.Window("Notepad", layout=layout)

# event loop
while True:
    event, values = window.read()
    if event in ["Exit", eg.WINDOW_CLOSED]:  # exit button
        break
    # save button
    if event == "Save":
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            f.write(values["text"])
        eg.popup("Saved")
    # open button
    if event == "Open":
        if not os.path.exists(SAVE_FILE):
            continue
        # load text
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            text = f.read()
        # set to Multiline element
        window["text"].update(text)
window.close()
