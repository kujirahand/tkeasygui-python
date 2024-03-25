import TkEasyGUI as sg

# import PySimpleGUI as eg

layout = [[
    sg.Canvas(
        size=(400, 400),
        key="-canvas-",
        background_color="white"
    )]]
window = sg.Window("Canvas Test", layout)
canvas = window["-canvas-"]
# Event Loop
painted = False
while True:
    event, _ = window.read(timeout=10)
    if event == sg.WINDOW_CLOSED:
        break
    # get Widget from Canvas
    if not painted:
        widget = canvas.Widget
        # draw
        widget.create_rectangle(10, 10, 300, 300, fill="yellow")
        widget.create_oval(50, 50, 350, 350, fill="blue")
        widget.create_line(10, 10, 390, 390, fill="red", width=5)
window.close()
