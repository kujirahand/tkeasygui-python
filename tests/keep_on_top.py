# import PySimpleGUI as sg
import TkEasyGUI as sg

window = sg.Window("Keeo on Top", layout=[
        [
            sg.Button("x"),
            sg.Text("This window will stay on top")
        ],
    ],
    keep_on_top=True,
    no_titlebar=True,
    grab_anywhere=True,
    alpha_channel=0.9,
)
while True:
    event, values = window.read()
    if event in [sg.WIN_CLOSED, "x"]:
        break
window.close()
