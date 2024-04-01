# clock
import datetime

import TkEasyGUI as sg

# create window
layout = [
    [
        sg.Text("click me", font=("Arial", 30), enable_events=True, background_color="red", text_color="white"),
        sg.Text("---", key="-info-", background_color="red", text_color="white"),
    ],
    [
        sg.Text("Hello,", text_color="white", background_color="#993399"),
        sg.Text("World!", text_color="white", background_color="#FF0000"),
    ],
    [
        sg.Text("Thank you.",
                enable_events=True,
                text_color="black", background_color="#FF99FF",
                font=("Arial", 20, "underline")),
    ],
]
window = sg.Window("text/color", layout, font=("Arial", 12))
# event loop
while True:
    event, _ = window.read()
    print(event)
    if event == sg.WINDOW_CLOSED:
        break
    if event == "click me":
        window["-info-"].update("clicked")
        continue
    if event == "Thank you.":
        sg.popup("Thank you for using TkEasyGUI!")
        continue
window.close()
