"""TkEasyGUI Layout Test"""

import TkEasyGUI as eg

layout = [
    [eg.Text("-" * 60)],
    eg.align_left([eg.Text("LEFT")]),
    eg.align_center([eg.Text("CENTER")]),
    eg.align_right([eg.Text("RIGHT")]),
    [eg.Text("-" * 60)],
    eg.align_center([eg.Button("Exit")]),
]

with eg.Window("Test Layout Helper", layout=layout) as win:
    for event, values in win.event_iter():
        print(event, values)
        if event == "Exit":
            break
