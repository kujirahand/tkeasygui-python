"""
### CalendarBrowse sample

This sample demonstrates how to use the CalendarBrowse widget.
CalendarBrowse is a button that opens a calendar dialog.
"""

import TkEasyGUI as eg

# Create window
layout = [
    [eg.Text("date:")],
    [
        eg.Input(key="-input-"),
        eg.CalendarBrowse() # Calendar button
    ],
    [eg.CloseButton()],
]
window = eg.Window("CalendarBrowse Test", layout)

# Event loop
while window.is_running():
    # get window event
    event, values = window.read()
    print("@@@", event, values)
window.close()
