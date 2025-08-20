"""
Temperature Converter > TkEasyGUI for The 7 Tasks of GUI Programming

@ref https://7guis.github.io/7guis/tasks/
"""

import TkEasyGUI as eg


def main():
    """Main function to run the Temperature Converter GUI application."""
    # flag
    _update = False

    def set_update_flag(value: bool):
        """Set the update flag to prevent recursive updates."""
        nonlocal _update
        _update = value

    # Create a window
    window = eg.Window(
        "Temperature Converter",
        layout=[
            [
                eg.Input("5", key="-c-", size=(5, 1), enable_events=True),
                eg.Text("Celsius = "),
                eg.Input("41", key="-f-", size=(5, 1), enable_events=True),
                eg.Text("Fahrenheit"),
            ]
        ],
    )
    # event loop
    while window.is_alive():
        # read events from the window
        event, values = window.read()
        print("@", event, values)
        # check events
        if _update:
            continue
        if event == "-c-":
            set_update_flag(True)
            try:
                c = float(values["-c-"])
                f = int(c * 9 / 5 + 32)
                window["-f-"].update(str(f))
            except ValueError:
                window["-f-"].update("0")
            window.set_timeout(set_update_flag, 100, False)
        if event == "-f-":
            set_update_flag(True)
            try:
                f = float(values["-f-"])
                c = int((f - 32) * 5 / 9)
                window["-c-"].update(str(c))
            except ValueError:
                window["-c-"].update("0")
            window.set_timeout(set_update_flag, 100, False)
    window.close()


if __name__ == "__main__":
    main()
