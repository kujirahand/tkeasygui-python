"""
Counter > TkEasyGUI for The 7 Tasks of GUI Programming

@ref https://7guis.github.io/7guis/tasks/
"""

import TkEasyGUI as eg

def main():
    """Main function to run the Counter GUI application."""
    # Create a window
    window = eg.Window("Counter", layout=[[
        eg.Input("0", key="-counter-", size=(8, 1)),
        eg.Button("Count"),
    ]])
    # event loop
    while window.is_alive():
        # read events from the window
        event, values = window.read()
        # check events
        if event == "Count":
            # Increment the counter
            try:
                count = int(values["-counter-"]) + 1
                window["-counter-"].update(str(count))
            except ValueError:
                # If the input is not a valid integer, reset to 0
                window["-counter-"].update("0")
    window.close()

if __name__ == "__main__":
    main()
