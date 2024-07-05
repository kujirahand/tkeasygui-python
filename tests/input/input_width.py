import TkEasyGUI as eg

# Window layout
layout = [
    [eg.Input("[width=30] Hello, World!", width=30)],
    [eg.Input("[width=20] Hello, World!", size=(20, 1))], # width or size, but height is not supported
    [eg.Button("OK")]
]
# Create the Window
with eg.Window("Hello App", layout) as window:
    # Event loop
    for event, values in window.event_iter():
        if event == "OK":
            eg.print("Thank you.")
            break  # Exit the event loop
