import TkEasyGUI as eg

# Create window
layout = [[eg.Text(
    "For wisdom is better than corals;\n" + 
    "All other desirable things cannot compare to it."
)]]
window = eg.Window("Proverb", layout)
# Event loop
while True:
    # get window event
    event, values = window.read()
    # close button
    if event == eg.WINDOW_CLOSED:
        break
    # check OK Button
    if event == "OK":
        break
window.close()
