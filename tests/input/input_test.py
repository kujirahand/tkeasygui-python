"""
### Input widget test
"""

import TkEasyGUI as eg

# window create
font = ("", 12)
window = eg.Window(
    "Input test",
    layout=[
        [eg.Text("Input elements:")],
        [eg.Input("input1", key="-input1-", enable_events=True, color="red")],
        [
            eg.Input(
                "input2",
                key="-input2-",
                readonly=True,
                readonly_background_color="gray",
            )
        ],
        [
            eg.Input(
                "input3",
                key="-input3-",
                background_color="red",
                text_color="white",
                text_align="right",
            )
        ],
        [eg.Button("Exit")],
    ],
    font=("Arial", 12),
    finalize=True,
    resizable=True,
)
# event loop
while True:
    event, values = window.read()
    print("#", event, values)
    if event in (None, "Exit", eg.WINDOW_CLOSED):
        break
window.close()
