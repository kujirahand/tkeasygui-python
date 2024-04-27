import TkEasyGUI as sg

# generate widgets with color
text1 = sg.Text(
    "Better to enjoy what the eyes see than to wander after one's desires.",
    background_color="yellow",
    color="black")
text2 = sg.Text(
    "This too is futility, a chasing after the wind.",
    background_color="yellow",
    color="black")

# create window
window = sg.Window(
    "text/simple",
    layout=[
        [
            sg.Frame(
                "Text",
                layout=[
                    [text1],
                    [text2],
                    [
                        sg.Button("Copy to clipboard"),
                        sg.Button("Change color"),
                    ],
                ],
            )
        ],
        [sg.Button("Close")],
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
        sg.set_clipboard(s)
        sg.popup("Copied to clipboard.")
