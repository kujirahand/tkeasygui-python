import tkeasygui as sg

# Create window
layout = [
    [sg.Text("For wisdom is better than corals;\n" + 
             "All other desirable things cannot compare to it.")],
    [sg.Button("OK")]
]
window = sg.Window("Proverb", layout=layout)
# Event loop
while True:
    # get window event
    event, values = window.read()
    # close button
    if event == sg.WINDOW_CLOSED:
        break
    # check OK Button
    if event == "OK":
        sg.popup("Pushed OK Button")
        break
window.close()
