"""
# clock (with window.post_event_after)

This sample demonstrates how to create a digital clock using the `post_event_after` method.
"""

import datetime

import TkEasyGUI as eg

# create window
layout = [[eg.Text("00:00:00", key="-output-", font=("Helvetica", 80))]]
window = eg.Window("Digital Clock", layout)
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
