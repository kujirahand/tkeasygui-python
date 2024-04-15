import TkEasyGUI as sg
# import PySimpleGUI as sg

window = sg.Window("List Test", layout=[
    [sg.Text("Please select item:")],
    [sg.Listbox(
        ["item1", "item2", "item3"],
        default_values=["item3"],
        enable_events=True,
        size=(20, 3), key="-listbox-")],
    [sg.Text("-", key="-result-")],
    [sg.Button("Exit")],
])
while True:
    event, values = window.read()
    print(event, values)
    if event in [sg.WIN_CLOSED, "Exit"]:
        break
    if event == "-listbox-":
        window["-result-"].update("/".join(values["-listbox-"]))
window.close()
