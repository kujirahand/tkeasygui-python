# import PySimpleGUI as sg
import TkEasyGUI as sg

# window create
font = ("", 12)
window = sg.Window("UI test", layout=[
    [sg.Input("abcdefg", key="-input-")],
    [sg.Button("select_all"), sg.Button("get_selection_pos")],
    [sg.Button("get_selection_start"), sg.Button("get_selection_length")],
    [sg.Button("set_selection_start(0,5)"), sg.Button("set_selection_start(5,2)")],
    [sg.Button("set_cursor_pos(0)"), sg.Button("set_cursor_pos(3)")],
    [sg.Button("copy"), sg.Button("paste"), sg.Button("cut")],
    [sg.Button("Exit")],
], font=("Arial", 12), finalize=True, resizable=True)
input: sg.Input = window["-input-"]
# event loop
while True:
    event, values = window.read()
    print("#", event, values)
    if event in (None, "Exit", sg.WINDOW_CLOSED):
        break
    if event == "copy":
        input.copy()
    if event == "paste":
        input.paste()
    if event == "cut":
        input.cut()
    if event == "set_cursor_pos(0)":
        input.set_cursor_pos(0)
    if event == "set_cursor_pos(3)":
        input.set_cursor_pos(3)
    if event == "select_all":
        input.select_all()
    if event == "get_selection_pos":
        start_pos, end_pos = input.get_selection_pos()
        sg.popup(f"{start_pos}-{end_pos}")
    if event == "get_selection_start":
        sg.popup(f"{input.get_selection_start()}")
    if event == "get_selection_length":
        sg.popup(f"{input.get_selection_length()}")
    if event == "set_selection_start(0,5)":
        input.set_selection_start(0, 5)
    if event == "set_selection_start(5,2)":
        input.set_selection_start(5, 2)
window.close()
