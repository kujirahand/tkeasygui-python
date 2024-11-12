"""
# Thread test

This is a test for the `Window.start_thread` method.
"""

import time

import TkEasyGUI as eg


# long-running process sample
def long_running_process(wait):
    print("sleep start")
    time.sleep(wait)
    print("sleep end")
    return f"done {wait}"

# define layout
layout = [
    [eg.Text("00:00:00", key="-time-")],
    [eg.HSeparator()],
    [eg.Text("Long-running process")],
    [eg.Text("wait:"), eg.Input("3", key="-wait-")],
    [
        eg.Button("thread1(wait=user)", key="-start1-"),
        eg.Button("thread2(wait=3)", key="-start2-"),
        eg.Button("no-thread(wait=3)", key="-start3-"),
    ],
    [eg.Button("Exit")],
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
        result = values["-threadend-"]
        eg.print(result)
        window["-start1-"].update(disabled=False)
    # === -start2- ===
    if event == "-start2-":
        window["-start2-"].update(disabled=True)
        window.start_thread(long_running_process, wait=3) # no end_key
    if event == eg.WINDOW_THREAD_END:  # no end_key
        result = values[eg.WINDOW_THREAD_END]
        eg.print(result)
        window["-start2-"].update(disabled=False)
    # === -start3- ===
    if event == "-start3-":
        res = long_running_process(3)
        eg.print(res)
# close window
window.close()
