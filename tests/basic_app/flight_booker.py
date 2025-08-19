"""
Flight Booker > TkEasyGUI for The 7 Tasks of GUI Programming

@ref https://7guis.github.io/7guis/tasks/
"""
# pylint: disable=line-too-long
import TkEasyGUI as eg

def main():
    """Main function"""
    # Create a window
    mode_list = ["one-way flight", "return flight"]
    window = eg.Window("Flight Booker", layout=[
        [eg.Combo(mode_list, key="-mode-", size=(15, 1), enable_events=True, readonly=True, default_value=mode_list[0])],
        [eg.Input("25.03.2025", key="-t1", size=(15, 1), validation=r"[0-9\.]+", validation_message="Please enter a valid number or dot")],
        [eg.Input("28.03.2025", key="-t2", size=(15, 1), validation=r"[0-9\.]+", validation_message="Please enter a valid number or dot", disabled=True)],
        [eg.Button("Book", size=(15, 1))],
    ])
    # event loop
    while window.is_alive():
        # read events from the window
        event, values = window.read()
        print("@Event:", event, "Values:", values)
        # check events
        if event == "-mode-":
            # Enable or disable the second input based on the selected mode
            if values["-mode-"] == mode_list[0]: # one-way flight
                window["-t2"].update(disabled=True)
            else:
                window["-t2"].update(disabled=False)
        elif event == "Book":
            data = [values["-t1"]] if values["-mode-"] == mode_list[0] else [values["-t1"], values["-t2"]]
            selected = eg.popup_listbox(data, title="Flight Booker", message="Your flight booking details:", default_value=data[0])
            if selected is not None:
                break
    window.close()

if __name__ == "__main__":
    main()
