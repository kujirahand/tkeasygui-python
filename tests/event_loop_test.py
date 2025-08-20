"""
### Event Loop with `event_iter` method sample

This sample demonstrates how to use the `event_iter` method.
"""

import TkEasyGUI as eg

# define layout
layout = [[eg.Text("Hello, World!")], [eg.Button("Exit")]]

# create a window
window = eg.Window("test", layout)

# event loop
for event, values in window.event_iter():
    if event == "Exit":
        eg.popup("Thank you.")
        break
