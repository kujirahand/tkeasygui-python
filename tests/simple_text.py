import tkeasygui as sg

# Create window
layout = [[sg.Text(
    "For wisdom is better than corals;\n" + 
    "All other desirable things cannot compare to it."
)]]
window = sg.Window("Proverb", layout)
# Event loop
while True:
    # get window event
    event, values = window.read()
    # close button
    if event == sg.WINDOW_CLOSED:
        break
    # check OK Button
    if event == "OK":
        break
window.close()
