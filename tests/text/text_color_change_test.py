"""Text Color Change Test"""

import TkEasyGUI as eg

# generate widgets with color
text1 = eg.Text(
    "Better to enjoy what the eyes see than to wander after one's desires.",
    background_color="yellow",
    color="black",
)
text2 = eg.Text(
    "This too is futility, a chasing after the wind.",
    background_color="yellow",
    color="black",
)

# create window
window = eg.Window(
    "text/simple",
    layout=[
        [
            eg.Frame(
                "Text",
                layout=[
                    [text1],
                    [text2],
                    [
                        eg.Button("Copy to clipboard"),
                        eg.Button("Change color"),
                    ],
                ],
            )
        ],
        [eg.Button("Close")],
    ],
    font=("Arial", 16),
)

# event loop
for event, values in window.event_iter():
    if event == "Close":
        break
    if event == "Change color":
        text1.update(background="red", color="white")
        text2.update(background="blue", color="white")
    if event == "Copy to clipboard":
        s = text1.get_text() + "\n" + text2.get_text()
        eg.set_clipboard(s)
        eg.popup("Copied to clipboard.")
