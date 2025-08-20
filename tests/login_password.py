"""
### Login dialog with password input

This snippet demonstrates a simple login dialog with a password input field.
"""

import TkEasyGUI as eg

# define layout
layout = [
    [eg.Text("User Id:")],
    [eg.Input("test@example.com", key="-userid-", enable_events=True)],
    [eg.Text("Password:")],
    [eg.Input("abcdefg", key="-password-", password_char="*")],
    [eg.Button("OK"), eg.Button("Cancel")],
]
# window create
window = eg.Window("Login dialog", layout=layout)
# window.move_to_center()
# event loop
while window.is_running():
    event, values = window.read()
    print("#", event, values)
    if event == "Cancel":
        break
    if event == "OK":
        msg = "Pushd [OK]\n"
        msg += f"User Id: {values['-userid-']}\n"
        msg += f"Password: {values['-password-']}"
        eg.print(msg)
window.close()
