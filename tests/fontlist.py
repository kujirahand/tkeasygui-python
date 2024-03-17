import tkinter as tk
import tkinter.font as font

import tkeasygui as sg

# list fonts
tk = tk.Tk()
tk.withdraw()
fontlist = list(font.families())
print(fontlist)

# create window
layout = [
    [sg.Listbox( 
        values=fontlist,
        size=(40, 20), 
        key="-files-", 
        enable_events=True,
    )],
    [sg.Input("", key="-input-", expand_x=True)],
]
window = sg.Window("Font List", layout)
# event loop
while True:
    event, values = window.read()
    print("# event:", event, values)
    if event == sg.WINDOW_CLOSED:
        break
    if event == "-files-":
        f = values["-files-"][0] if values["-files-"] else "-"
        window["-input-"].update(f)
