import TkEasyGUI as sg

# define layout
layout=[
    [sg.Text("User Id:")],
    [sg.Input("test@example.com", key="-userid-", enable_events=True)],
    [sg.Text("Password:")],
    [sg.Input("abcdefg", key="-password-", password_char="*")],
    [sg.Button("OK"), sg.Button("Cancel")],
]
# window create
window = sg.Window("Login dialog", layout=layout)
# window.move_to_center()
# event loop
while window.is_alive():
    event, values = window.read()
    print("#", event, values)
    if event == "Cancel":
        break
    if event == "OK":
        print(window.get_location())
        sg.popup("OK, " + values["-userid-"])
window.close()
