# import PySimpleGUI as sg
import TkEasyGUI as sg

# define menu
menu_def = [
    ['File',['!New', '---', 'Open', 'Save', ['Save As', 'Save Temp'], '---', 'Exit']],
    ['Edit',['Paste','Redo','Undo']],
    ['test1',['Hello', 'World::-world1-']],
    ['test2',['Hello', 'World::-world2-']],
]

menu_def2 = [
    ["Changed", ["---", "Exit"]],
]

# create window
layout = [
    [sg.Menu(menu_def, key="-menu-")],
    [sg.Text('This is a test window for Menu element.')],
    [sg.Multiline('', size=(60, 8), key="-log-")],
    [sg.Button("Change"), sg.Button("Exit")],
]
window = sg.Window('Menu test',layout)
# event loop
while True:
    event, values = window.read()
    print(event, values)
    if event in [sg.WINDOW_CLOSED, "Exit"]:
        break
    if event == "Change":
        # change menu defined
        window["-log-"].print("Change menu")
        window["-menu-"].update(menu_def2)
    if event == "Hello":
        sg.popup("Hello Popup")
        continue
    # else
    window["-log-"].print(f"{event}", text_color="blue", background_color="yellow")
    window["-log-"].print("---", text_color="red", background_color="lightblue")
window.close()
