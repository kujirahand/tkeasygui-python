# import PySimpleGUI as sg
import TkEasyGUI as sg

window = sg.Window("Keeo on Top", layout=[
        [sg.Text("This window will stay on top")],
    ],
    keep_on_top=True,
    no_titlebar=True,
    grab_anywhere=True,
)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()
