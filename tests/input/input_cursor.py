"""
### Input cursor control

TkEasyGUI offers a wide range of methods to control the cursor in the Input widget.
"""

import TkEasyGUI as eg

# window create
font = ("", 12)
window = eg.Window(
    "UI test",
    layout=[
        [eg.Input("abcdefg", key="-input-")],
        [eg.Button("select_all"), eg.Button("get_selection_pos")],
        [eg.Button("get_selection_start"), eg.Button("get_selection_length")],
        [eg.Button("set_selection_start(0,5)"), eg.Button("set_selection_start(5,2)")],
        [eg.Button("set_cursor_pos(0)"), eg.Button("set_cursor_pos(3)")],
        [eg.Button("copy"), eg.Button("paste"), eg.Button("cut")],
        [eg.Button("Exit")],
    ],
    font=("Arial", 12),
    finalize=True,
    resizable=True,
)
input: eg.Input = window["-input-"]
# event loop
while True:
    event, values = window.read()
    print("#", event, values)
    if event in (None, "Exit", eg.WINDOW_CLOSED):
        break
    if event == "copy":
        input.copy()
    if event == "paste":
        input.paste()
    if event == "cut":
        input.cut()
    if event == "set_cursor_pos(0)":
        input.set_cursor_pos(0)
    if event == "set_cursor_pos(3)":
        input.set_cursor_pos(3)
    if event == "select_all":
        input.select_all()
    if event == "get_selection_pos":
        start_pos, end_pos = input.get_selection_pos()
        eg.popup(f"{start_pos}-{end_pos}")
    if event == "get_selection_start":
        eg.popup(f"{input.get_selection_start()}")
    if event == "get_selection_length":
        eg.popup(f"{input.get_selection_length()}")
    if event == "set_selection_start(0,5)":
        input.set_selection_start(0, 5)
    if event == "set_selection_start(5,2)":
        input.set_selection_start(5, 2)
window.close()
