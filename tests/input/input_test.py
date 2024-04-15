# import PySimpleGUI as sg
import TkEasyGUI as sg

# window create
font = ("", 12)
window = sg.Window("Input test", layout=[
    [sg.Text("Input elements:")],
    [sg.Input("input1", key="-input1-", enable_events=True, color="red")],
    [sg.Input("input2", key="-input2-", readonly=True, readonly_background_color="gray")],
    [sg.Input("input3", key="-input3-", background_color="red", text_color="white", text_align="right")],
    [sg.Button("Exit")],
], font=("Arial", 12), finalize=True, resizable=True)
# event loop
while True:
    event, values = window.read()
    print("#", event, values)
    if event in (None, "Exit", sg.WINDOW_CLOSED):
        break
window.close()
