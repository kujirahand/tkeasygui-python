"""
# Window key events
"""
import TkEasyGUI as eg

layout = [
    [
        eg.Frame(
            "",
            [
                [eg.Image(size=(300, 300), filename="a.jpg")],
            ],
        ),
        eg.Frame(
            "Description",
            [
                [eg.Text("# Window('', enable_key_events=True)")],
                # [eg.Text("# Window('', return_keyboard_events=True)")],
                [eg.HSeparator()],
                [eg.Text("[S] ... Show message")],
                [eg.Text("[A] ... Show message")],
                [eg.Text("[ESC] ... Close")],
                [eg.Text("[Space] ... Show message")],
            ],
        ),
    ],
]
window = eg.Window(
    'Window key test', layout,
    enable_key_events=True,
    # return_keyboard_events=True,
    )

# event loop
while True:
    event, values = window.read()
    print(f"[{event}]", values)
    if event == eg.WIN_CLOSED:
        break
    # PySimpleGUI key events --> return_keyboard_events=True
    if event in ['Escape:27', "Escape:889192475"]: # [(for win), (for mac)]
        eg.popup("Escape key pressed")
        break
    if event in ['space:20', "space:822083616"]:
        eg.popup("space key pressed")
    elif event == 's':
        eg.popup("[S] Hello, World!")
    elif event == 'a':
        eg.popup("[A] Hello, World!")
    # TkEasyGUI key events --> enable_key_events=True
    if event == eg.WINDOW_KEY_EVENT:
        key = values["key"]
        if key == "Escape":
            eg.popup("Escape key pressed")
            break
        if key == "space":
            eg.popup("space key pressed")
        else:
            eg.popup(f"[{key}] Hello, World!")
window.close()
