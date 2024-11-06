import TkEasyGUI as eg

# set items
items = [f"item_{i}" for i in range(50)]
# create window
window = eg.Window(
    "Listbox test",
    layout=[
        [eg.Text("Please select item:")],
        [
            eg.Listbox(
                items,
                default_values=["item_5"],
                enable_events=True,
                size=(30, 8),
                key="-listbox-",
            )
        ],
        [eg.Text("-", key="-result-")],
        [eg.Button("Select[30]"), eg.Button("Select[3]")],
        [eg.Button("OK")],
    ],
)
# event loop
while True:
    event, values = window.read()
    print(event, values)
    if event == eg.WIN_CLOSED:
        break
    if event == "OK":
        selected = ",".join(values["-listbox-"])
        eg.print("You selected:", selected)
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
