# import PySimpleGUI as sg
import TkEasyGUI as sg

# define menu
menu_def = [
    ['File',['New', 'Open', 'Save', ['Save As', 'Save Temp'], 'Exit']],
    ['Edit',['Paste','Redo','Undo']],
    ['Popup',['Hello']],
]

# create window
layout = [
    [sg.Menu(menu_def)],
    [sg.Text('Menu test')],
]
window = sg.Window('Menu test',layout)
# event loop
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Hello":
        sg.popup("Hello Popup")
    if event is None:
        break
window.close()
