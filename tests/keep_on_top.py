# import PySimpleGUI as sg
import TkEasyGUI as eg

window = eg.Window("Keeo on Top", layout=[
        [
            eg.Button("x"),
            eg.Text("This window will stay on top")
        ],
    ],
    keep_on_top=True,
    no_titlebar=True,
    grab_anywhere=True,
    alpha_channel=0.9,
)
while True:
    event, values = window.read()
    if event in [eg.WIN_CLOSED, "x"]:
        break
window.close()
