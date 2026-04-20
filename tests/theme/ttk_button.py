"""Compare ttk and classic button rendering."""

import TkEasyGUI as eg

layout = [
    [eg.Text("This is a modern button using ttk styles.")],
    [eg.Button("Modern", use_ttk_buttons=True)],
    [eg.HSeparator()],
    [eg.Text("This is a classic button using Tkinter styles.")],
    [eg.Button("Classic", use_ttk_buttons=False)],
]
window = eg.Window("Buttons", layout)
for event, values in window.event_iter():
    if event == "Modern":
        eg.popup("You clicked the modern button!")
    if event == "Classic":
        eg.popup("You clicked the classic button!")
window.close()
