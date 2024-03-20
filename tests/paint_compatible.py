# import PySimpleGUI as sg
import tkeasygui as sg

# canvas
canvas = sg.Canvas(size=(400, 400), key="-canvas-", background_color="red")
# window create
window = sg.Window("Hello World", layout=[
    [sg.Button("Exit")],
    [canvas],
], finalize=True)
# bind user event
canvas.bind("<Motion>", "motion", True)
canvas.bind("<ButtonPress>", "on", True)
canvas.bind("<ButtonRelease>", "off", True)
# mouse flag
flag_on = False
# event loop
while True:
    event, values = window.read()
    print("@", event, values)
    if event in (None, "Exit"):
        break
    if event == "-canvas-on":
        flag_on = True
    elif event == "-canvas-off":
        flag_on = False
    elif event == "-canvas-motion":
        if not flag_on:
            continue
        e = canvas.user_bind_event
        w = canvas.tk_canvas
        x, y = e.x, e.y
        w.create_oval(x, y, x+10, y+10, fill="white", outline="white")
