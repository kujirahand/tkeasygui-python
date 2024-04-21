import TkEasyGUI as sg

# import PySimpleGUI as sg
items = [f"Item{i}" for i in range(1, 30)]

window = sg.Window("Listbox test", layout=[
    [sg.Text("Please select item:")],
    [sg.Listbox(
        items,
        default_values=["Item3"],
        enable_events=True,
        size=(20, 5), key="-listbox-")],
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
