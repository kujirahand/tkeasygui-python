import time
import TkEasyGUI as eg

# long-running process sample
def long_running_process(wait):
    print("sleep start")
    time.sleep(wait)
    print("sleep end")

# define layout
layout = [
    [eg.Text("Long-running process")],
    [eg.Text("wait:"), eg.Input("3", key="-wait-")],
    [eg.Button("Start", key="-start-"), eg.Button("Exit")],
]
# create a window
window = eg.Window("Long-running process test", layout)
# event loop
while True:
    event, values = window.read()
    if event == "-start-":
        window["-start-"].update(disabled=True)
        try:
            wait = int(values["-wait-"])
        except ValueError:
            window["-wait-"].update("3")
            window["-start-"].update(disabled=False)
            continue
        window.start_thread(long_running_process, end_key="thread-end", wait=wait)
    if event == "thread-end":
        eg.print("Thread end")
        window["-start-"].update(disabled=False)
    if event in [eg.WINDOW_CLOSED, "Exit"]:
        break
# close window
window.close()
