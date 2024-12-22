"""
element_justification test
"""

import TkEasyGUI as eg

win = eg.Window(
    title="Push Test",
    layout=[
        [eg.Text("=" * 50)],
        [eg.Button("Right")],
        [eg.Button("Center")],
    ],
    element_justification="center", # center alignment
)
while win.is_running():
    event, values = win.read()
    if event == "Center" or event == "Right":
        break
win.close()

