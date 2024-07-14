import TkEasyGUI as sg

# Create window
layout = [
    [sg.Text("date:")],
    [
        sg.Input(key="-input-"),
        sg.CalendarBrowse() # Calendar button
    ],
    [sg.CloseButton()],
]
window = sg.Window("CalendarBrowse Test", layout)

# Event loop
while window.is_running():
    # get window event
    event, values = window.read()
    print("@@@", event, values)
window.close()
