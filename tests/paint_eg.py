"""
Paint tool for TkEasyGUI
Using original event model
"""
import tkeasygui as sg

# canvas
canvas = sg.Canvas(
    size=(400, 400),
    key="-canvas-",
    background_color="red"
).bind_events({
    "<ButtonPress>": "on",
    "<ButtonRelease>": "off",
    "<Motion>": "motion"
})

# window create
window = sg.Window("Hello World", layout=[
    [sg.Button("Exit")], [canvas]], finalize=True)
flag_on = False
# event loop
while True:
    event, values = window.read()
    print("#", event, values)
    if event in (None, "Exit"):
        break
    if event == "-canvas-on":
        flag_on = True
    elif event == "-canvas-off":
        flag_on = False
    elif event == "-canvas-motion":
        if not flag_on:
            continue
        e = values["event"]
        x, y = e.x, e.y
        canvas.tk_canvas.create_oval(x, y, x+10, y+10, fill="white", outline="white")
