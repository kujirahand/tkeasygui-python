"""
### Input widget validation sample

- Validates with regular expressions on Enter key or when focus leaves the field.
- If the input doesn't match, a warning is shown and focus returns to the entry with all text selected.
"""

import TkEasyGUI as eg

layout = [
    [eg.Text("3-digit number (e.g., 123)")],
    [
        eg.Input(
            key="-num3-",
            validation=r"^\d{3}$",
            validation_message="Please enter a 3-digit number (0-9).",
            enable_events=True,
        )
    ],
    [eg.Text("Email-like (simple)")],
    [
        eg.Input(
            key="-mail-",
            validation=r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
            validation_message="Please enter a valid email address format.",
        )
    ],
    [eg.Text("Alphanumeric only")],
    [
        eg.Input(
            key="-alnum-",
            validation=r"^[A-Za-z0-9]+$",
            validation_message="Only alphanumeric characters are allowed (non-empty).",
        )
    ],
    [eg.HSeparator()],
    [eg.Button("Print Values"), eg.Button("Exit")],
]

with eg.Window("Input Validation", layout, resizable=True) as window:
    for event, values in window.event_iter():
        if event in ("Exit", eg.WIN_CLOSED):
            break
        if event == "Print Values":
            # check inputs
            if not window["-num3-"].is_valid():
                window["-num3-"].focus()
                continue
            if not window["-mail-"].is_valid():
                window["-mail-"].focus()
                continue
            if not window["-alnum-"].is_valid():
                window["-alnum-"].focus()
                continue
            eg.print(values)
