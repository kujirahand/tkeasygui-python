"""
Paint tool for TkEasyGUI
Using original event model
"""
import TkEasyGUI as sg

# canvas
canvas = sg.Canvas(
    size=(400, 400),
    key="-canvas-",
    background_color="red",
    enable_events=True # enable mouse events
)
"""
# same as below
canvas = sg.Canvas(
    size=(400, 400),
    key="-canvas-",
    background_color="red",
).bind_events({
    "<ButtonPress>": "mousedown",
    "<ButtonRelease>": "mouseup",
    "<Motion>": "mousemove"
}, "system")
"""

# window create
window = sg.Window("Paint tool", layout=[
    [sg.Button("Exit")],
    [canvas]])
flag_on = False
# event loop
while True:
    event, values = window.read()
    print("#", event, values)
    if event in (None, "Exit"):
        break
    if event == "-canvas-":
        # check event type
        event = values["event"]
        event_type = values["event_type"]
        if event_type == "mousedown":
            flag_on = True
        elif event_type == "mouseup":
            flag_on = False
        elif event_type == "mousemove":
            if not flag_on:
                continue
            # get mouse cursor position
            x, y = event.x, event.y
            # draw white circle
            canvas.create_oval(x, y, x+10, y+10, fill="white", outline="white")
