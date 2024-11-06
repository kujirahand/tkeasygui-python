"""
### Many Buttons example

This example demonstrates how to create a window with many buttons.
"""

import TkEasyGUI as eg

# define layout --- make 12 buttons
layout = []
for row in range(3):
    layout.append([])
    for col in range(4):
        no = row*4+col+1
        btn = eg.Button(str(no), key=f"-button{no}",
                        size=(3, 1), metadata={"no": no})
        layout[row].append(btn)
# add close button
layout.append([eg.HSeparator()])
layout.append([eg.Button("Close")])

# make window
window = eg.Window("Many buttons", layout)

# event loop
for event, values in window.event_iter():
    # close button
    if event == "Close":
        break
    # push number button
    if event.startswith("-button"):
        # get number from metadata
        no = window[event].metadata["no"]
        eg.popup(f"You Pushed {no}")
        # disable button
        window[event].update(disabled=True)

window.close()
