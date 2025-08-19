"""
Timer > TkEasyGUI for The 7 Tasks of GUI Programming

@ref https://7guis.github.io/7guis/tasks/

[TODO] 作りかけです。
"""
# pylint: disable=line-too-long
import TkEasyGUI as eg

def main():
    """Main function"""
    # Create a window
    window = eg.Window("Flight Booker", layout=[
        [
            eg.Label("Elapsed Time:"),
            eg.Progressbar(value_range=(0, 100), key="-bar", size=(15, 20))
        ],
        [eg.Label("11.8s", key="-label")],
        [
            eg.Label("Duration:"),
            eg.Slider(value_range=(10, 100), default=10, key="-duration", size=(15, 1))
        ],
        [eg.Button("Reset", size=(15, 1))],
    ])
    # event loop
    while window.is_alive():
        # read events from the window
        event, values = window.read()
        print("@Event:", event, "Values:", values)
        # check events
    window.close()

if __name__ == "__main__":
    main()
