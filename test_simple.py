import tkeasygui as eg

# create window
layout = [[eg.Text(
    "The lazy person has his cravings, yet he has nothing,\n" + 
    "But the diligent one will be fully satisfied.")]]
window = eg.Window("Proverb", layout)
# event loop
while True:
    event, values = window.read()
    if event == eg.WINDOW_CLOSED:
        break
window.close()
