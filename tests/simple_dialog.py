import TkEasyGUI as eg

# Create window
layout = [
    [eg.Text("For wisdom is better than corals;\n" + 
             "All other desirable things cannot compare to it.")],
    [eg.Button("OK")]
]
window = eg.Window("Proverb", layout=layout)
# Event loop
while True:
    # get window event
    event, values = window.read()
    # close button
    if event == eg.WINDOW_CLOSED:
        break
    # check OK Button
    if event == "OK":
        eg.popup("Pushed OK Button")
        break
window.close()
