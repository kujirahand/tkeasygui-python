import TkEasyGUI as sg

# set items
items = [f"item_{i}" for i in range(50)]
# create window
window = sg.Window(
    "Listbox test",
    layout=[
        [sg.Text("Please select item:")],
        [
            sg.Listbox(
                items,
                default_values=["item_5"],
                enable_events=True,
                size=(30, 8),
                key="-listbox-",
            )
        ],
        [sg.Text("-", key="-result-")],
        [sg.Button("Select[30]"), sg.Button("Select[3]")],
        [sg.Button("OK")],
    ],
)
# event loop
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == "OK":
        selected = ",".join(values["-listbox-"])
        sg.print("You selected:", selected)
        break
    if event == "Select[3]":
        window["-listbox-"].set_cursor_index(3)
        event = "-listbox-"
    if event == "Select[30]":
        window["-listbox-"].set_cursor_index(30)
        event = "-listbox-"
    if event == "-listbox-":
        index = window["-listbox-"].get_cursor_index()
        selected = ",".join(values["-listbox-"])
        window["-result-"].update(f"[{index}] {selected}")
window.close()
