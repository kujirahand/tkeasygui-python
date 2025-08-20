"""
# no key sample - Inch to cm converter
"""

import TkEasyGUI as eg

window = eg.Window(
    "Inch to cm",
    layout=[
        [eg.Text("Please input Inch:")],
        [eg.Input("1"), eg.Button("Convert")],
    ],
)
while True:
    event, values = window.read()
    if event == eg.WIN_CLOSED:
        break
    if event == "Convert":
        try:
            inch = float(values[0])  # key = 0
            cm = inch * 2.54
            result = f"{inch} inch is {cm} cm"
            eg.popup(result)
        except Exception as _e:
            eg.popup("Please input number.")
window.close()
