"""
### Set readonly test
"""

import TkEasyGUI as eg

a_font = ("Arial", 20)
window = eg.Window(
    "BasicUI",
    layout=[
        [
            eg.Button("Change", key="-change-", font=a_font),
            eg.Button("Readonly(tkeasygui)", font=a_font),
        ],
        [eg.Text("Text", key="-text-", font=a_font)],
        [eg.Input("Input", key="-input-", font=a_font)],
        [eg.Multiline("Multiline", key="-multiline-", font=a_font)],
    ],
)
# event loop
IS_READONLY = False
while True:
    event, values = window.read()
    if event == eg.WINDOW_CLOSED:
        break
    print(event, values)
    if event == "-change-":
        print("change")
        window["-change-"].update("changed!!")
        window["-text-"].update("changed!!")
        window["-input-"].update("changed!!")
        window["-multiline-"].update("changed!!")
    if event == "Readonly(tkeasygui)":
        IS_READONLY = not IS_READONLY
        window["-input-"].update(readonly=IS_READONLY)
        window["-multiline-"].update(readonly=IS_READONLY)
window.close()
