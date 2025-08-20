"""VPush Test"""

import TkEasyGUI as sg

layout = [
    [sg.VPush()],
    [sg.Push(), sg.Text("== Middle =="), sg.Push()],
    [sg.Push(), sg.Button("OK"), sg.Push()],
    [sg.VPush()],
]

window = sg.Window(title="VPush Test", layout=layout, size=(400, 350))
while window.is_alive():
    event, values = window.read(timeout=1000)
    if event == sg.WIN_CLOSED or event == "OK":
        break
