"""Digital Clock Example"""

import datetime

import TkEasyGUI as eg

# create window
layout = [[eg.Text("00:00:00", key="-output-", font=("Arial", 30))]]
window = eg.Window("Digital Clock", layout, grab_anywhere=True)
# event loop
while True:
    event, _ = window.read(timeout=10)
    if event == eg.WINDOW_CLOSED:
        break
    # show current time
    now = datetime.datetime.now()
    window["-output-"].update(now.strftime("%H:%M:%S"))
window.close()
