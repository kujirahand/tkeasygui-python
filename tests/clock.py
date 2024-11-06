# clock
import datetime

import TkEasyGUI as eg

# show time
def show_cur_time(window):
    now = datetime.datetime.now()
    window["-time-"].update(now.strftime("%H:%M:%S"))

# create window
window = eg.Window(
    "Digital Clock",
    layout=[
        [eg.Text("00:00:00", key="-time-", font=("Helvetica", 80))]
    ])

# event loop
show_cur_time(window)
while window.is_running():
    event, _ = window.read(timeout=1000)
    print(event)
    if event == eg.TIMEOUT_KEY:
        show_cur_time(window)
