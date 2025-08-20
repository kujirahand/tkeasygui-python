"""
### Calculator Sample

This sample demonstrates how to create a simple calculator using TkEasyGUI.
It also shows how to create multiple buttons and handle button events effectively.
"""

import TkEasyGUI as eg

# define the calculator buttons
calc_buttons = [
    ["C", "←", "//", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "%", "="],
]
font = ("Helvetica", 20)
# create window
layout = [
    [
        eg.Input(
            "0",
            key="-output-",
            background_color="white",
            color="black",
            readonly_background_color="white",
            readonly=True,
            expand_x=True,
        )
    ],
]
# create many buttons
for row in calc_buttons:
    buttons = []
    for ch in row:
        btn = eg.Button(
            ch,  # label
            key=f"-btn{ch}",
            size=(4, 1),
        )
        buttons.append(btn)
    layout.append(buttons)
window = eg.Window("Calc", layout, font=font)

# event loop
output = "0"
for event, values in window.event_iter():
    if event == eg.WINDOW_CLOSED:
        break
    # when a button is pressed
    if event.startswith("-btn"):
        # get label
        ch = window[event].get()
        # clear if text is empty (0 or error)
        if output == "0" or output.startswith("E:"):
            output = ""
        # check label
        if ch == "C":  # clear key
            output = "0"
        elif ch == "←":  # bs key
            output = output[:-1]
        elif ch == "=":  # calc
            try:
                output = str(eval(output))
            except Exception as e:
                output = "E:" + str(e)
        else:
            # add other key
            output += ch
        # update display
        window["-output-"].update(output)
