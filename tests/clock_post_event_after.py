# clock (with window.post_event_after)
import datetime

import TkEasyGUI as sg

# create window
layout = [[sg.Text("00:00:00", key="-output-", font=("Helvetica", 80))]]
window = sg.Window("Digital Clock", layout)
window.post_event("tick", {})
# event loop
while window.is_running():
    event, _ = window.read()
    if event == "tick":
        # schedule next tick
        window.post_event_after(500, "tick", {})
        # show current time
        now = datetime.datetime.now()
        window["-output-"].update(now.strftime("%H:%M:%S"))
