"""
# clock (with window.post_event_after)

This sample demonstrates how to create a digital clock using the `timeout` event.
"""

import datetime

import TkEasyGUI as eg


# show time
def show_cur_time(win):
    now = datetime.datetime.now()
    win["-time-"].update(now.strftime("%H:%M:%S"))


# create window
window = eg.Window(
    "Digital Clock",
    layout=[[eg.Text("00:00:00", key="-time-", font=("Helvetica", 80))]],
)

show_cur_time(window)

# event loop
while window.is_running():
    # check event
    event, _ = window.read(timeout=1000)
    print(event)
    # timeout?
    if event == eg.TIMEOUT_KEY:
        show_cur_time(window)
