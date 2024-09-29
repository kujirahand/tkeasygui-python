import time
import TkEasyGUI as eg

# long-running process sample
def long_running_process(wait):
    print("sleep start")
    time.sleep(wait)
    print("sleep end")

# define layout
layout = [
    [eg.Text("00:00:00", key="-time-")],
    [eg.HSeparator()],
    [eg.Text("Long-running process")],
    [eg.Text("wait:"), eg.Input("3", key="-wait-")],
    [
        eg.Button("Start1", key="-start1-"),
        eg.Button("Start2", key="-start2-"),
        eg.Button("Exit"),
    ],
]
# create a window
window = eg.Window("Long-running process test", layout)
# event loop
while True:
    event, values = window.read(timeout=500, timeout_key="-timeout-")
    print("#", event, values)
    if event in [eg.WINDOW_CLOSED, "Exit"]:
        break
    if event == "-timeout-":
        now = time.strftime("%H:%M:%S")
        window["-time-"].update(now)
    # === -start1- ===
    if event == "-start1-":
        window["-start1-"].update(disabled=True)
        try:
            wait = int(values["-wait-"])
        except ValueError:
            window["-wait-"].update("3")
            window["-start1-"].update(disabled=False)
            continue
        window.start_thread(long_running_process, end_key="-threadend-", wait=wait)
    if event == "-threadend-":
        eg.print("Thread end")
        window["-start1-"].update(disabled=False)
    # === -start2- ===
    if event == "-start2-":
        window["-start2-"].update(disabled=True)
        window.start_thread(long_running_process, wait=3) # no end_key
    if event == eg.WINDOW_THREAD_END: # no end_key
        eg.print("Thread end")
        window["-start2-"].update(disabled=False)
# close window
window.close()
