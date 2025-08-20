"""
### Canvas test

Canvas is a widget that can draw various shapes and images.
This sample demonstrates how to use draw shapes.
"""

import random

import TkEasyGUI as eg

# create window
layout = [
    [
        eg.Canvas(
            size=(400, 400),
            key="-canvas-",
            background_color="white",
            enable_events=True,
        )
    ]
]
window = eg.Window("Canvas Test", layout)
canvas = window["-canvas-"]

# initial values
ox, oy, ow = random.randint(50, 250), random.randint(50, 250), 30
flag_update = True

# Event Loop
while window.is_running():
    event, values = window.read(timeout=200)
    print(event, values)
    if event == eg.WINDOW_CLOSED:
        break
    # check mouse event
    if event == "-canvas-" and values["event_type"] == "mousemove":
        flag_update = True
        if "event" in values:
            e = values["event"]
            ox = e.x
            oy = e.y
    # Update canvas
    if flag_update:
        canvas.clear()
        # draw rectangle
        canvas.create_rectangle(50, 50, 350, 350, fill="yellow")
        # draw random lines
        for i in range(50):
            p = [random.randint(0, 400) for _ in range(4)]
            canvas.create_line(p[0], p[1], p[2], p[3], fill="green", width=1)
        # draw oval at mouse position
        canvas.create_oval(ox - ow, oy - ow, ox + ow, oy + ow, fill="blue")
        flag_update = False
# close
window.close()
