"""element_justification test"""

import TkEasyGUI as eg

win = eg.Window(
    title="Center Test",
    layout=[
        [eg.Text("-" * 50)],
        [eg.Text("This is a test of the element justification.")],
        [eg.Text("-" * 50)],
        [eg.Button("Center")],
        [eg.Button("Close")],
    ],
    element_justification="center",  # center alignment
)
while win.is_running():
    event, values = win.read()
    if event == "Center" or event == "Close":
        break
win.close()
