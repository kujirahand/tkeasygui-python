import tkeasygui as sg

# make 10 buttons
layout = [[]]
for no in range(1, 10+1):
    # create button
    btn = sg.Button(
        f"{no}", # label
        key=f"-btn{no}", # key
        size=(3, 1) # button size
    )
    layout[0].append(btn)
# make window
window = sg.Window("Many buttons", layout)
# event loop
while True:
    # event
    event, _ = window.read()
    # close button
    if event == sg.WINDOW_CLOSED:
        break
    # push button
    if event.startswith("-btn"):
        sg.popup("Pushed " + event)
        window[event].update(disabled=True)
window.close()
