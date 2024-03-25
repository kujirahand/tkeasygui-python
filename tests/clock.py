# clock
import datetime

import TkEasyGUI as sg

# create window
layout = [
    [sg.Text("00:00:00", key="-output-", font=("Helvetica", 80))]
]
window = sg.Window("Digital Clock", layout)
# event loop
while True:
    event, _ = window.read(timeout=10)
    if event == sg.WINDOW_CLOSED:
        break
    # show current time
    now = datetime.datetime.now()
    window["-output-"].update(
        now.strftime("%H:%M:%S")
    )
