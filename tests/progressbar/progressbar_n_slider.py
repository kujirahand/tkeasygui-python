"""Progressbar and Slider Example"""
# pylint: disable=line-too-long
import TkEasyGUI as eg

def main():
    """Main function"""
     # Create a window
    window = eg.Window("Progressbar Test", layout=[
        [eg.Label("Try moving the slider.")],
        [eg.Slider(value_range=(0, 100), default_value=50, key="-slider", expand_x=True, enable_changed_events=True)],
        [eg.Label("50", key="-value")],
        [eg.HSeparator()],
        [
            eg.Label("Horizontal:"),
            eg.Progressbar(value_range=(0, 100), default_value=50, key="-pbar_h", orientation="horizontal", expand_x=True)
        ],
        [eg.HSeparator()],
        [
            eg.Label("Vertical:"),
            eg.Progressbar(value_range=(0, 100), default_value=50, key="-pbar_v", length=50, orientation="vertical", thickness=40)
        ],
        [eg.HSeparator()],
        [eg.Button("Close", expand_x=True)],
    ])
    # event loop
    while window.is_alive():
        # read events from the window
        event, values = window.read()
        print("@Event:", event, "Values:", values)
        # check events
        if event == "Close":
            break
        if event == "-slider":
            # Update the progress bar based on the slider value
            v = values["-slider"]
            window["-pbar_h"].update(v)
            window["-pbar_v"].update(v)
            window["-value"].update(str(int(v)))
    window.close()

if __name__ == "__main__":
    main()
