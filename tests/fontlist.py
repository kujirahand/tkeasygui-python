
import TkEasyGUI as sg

# list fonts
fontlist = sg.get_font_list()

# create window
layout = [
    [sg.Listbox( 
        values=fontlist,
        size=(40, 20), 
        key="-fontlist-", 
        enable_events=True,
    )],
    [sg.Input("-", key="-font-", expand_x=True)],
]
window = sg.Window("Font List", layout, font=("Arial", 14))
# event loop
while True:
    event, values = window.read()
    print("# event:", event, values)
    if event == sg.WINDOW_CLOSED:
        break
    if event == "-fontlist-":
        if values["-fontlist-"]:
            window["-font-"].update(values["-fontlist-"][0])
window.close()

