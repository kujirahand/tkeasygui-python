import TkEasyGUI as sg
# import PySimpleGUI as sg

window = sg.Window("Inch to cm", layout=[
    [sg.Text("Please select item:")],
    [sg.Listbox(
        ["item1", "item2", "item3"],
        default_values=["item3"],
        enable_events=True,
        size=(20, 3), key="-listbox-")],
    [sg.Text("-", key="-result-")],
])
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == "-listbox-":
        window["-result-"].update("/".join(values["-listbox-"]))
window.close()
