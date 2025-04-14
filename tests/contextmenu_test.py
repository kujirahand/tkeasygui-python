"""Context menu tests."""

import TkEasyGUI as eg
import tkinter as tk

message = "Hello world! Click here."


def do_copy():
    """Copy to clipboard"""
    eg.copy_to_clipboard(message)
    eg.popup_info("Copied to clipboard:\n" + message)


# Create a Text element with a context menu
msg = eg.Text(
    message,
    key="-msg-",
    expand_x=True,
    expand_y=True,
    enable_events=True,
)
layout = [
    [msg],
    [eg.Button("OK")],
]
popup_menu = tk.Menu(eg.get_root_window(), tearoff=0)
popup_menu.add_command(label="Copy", command=do_copy)

with eg.Window("test", layout) as win:
    for event, values in win.event_iter():
        if event == "OK":
            break
        if event == "-msg-" and "event" in values:
            # popup menu
            popup_menu.post(values["event"].x_root, values["event"].y_root)
