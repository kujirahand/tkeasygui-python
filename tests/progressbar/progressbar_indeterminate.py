"""Progressbar Example (mode=indeterminate)"""

# pylint: disable=line-too-long
import time
import TkEasyGUI as eg


def main():
    """Main function"""
    start_time = time.time()
    # Create a window
    window = eg.Window(
        "Progressbar mode test",
        layout=[
            [eg.Label("mode=determinate")],
            [
                eg.Progressbar(
                    value_range=(0, 9),
                    default_value=0,
                    key="-bar1",
                    mode="determinate",
                    expand_x=True,
                )
            ],
            [eg.HSeparator()],
            [eg.Label("mode=indeterminate")],
            [
                eg.Progressbar(
                    value_range=(0, 9),
                    default_value=0,
                    key="-bar2",
                    mode="indeterminate",
                    expand_x=True,
                )
            ],
            [eg.HSeparator()],
            [eg.Button("Close", expand_x=True)],
        ],
    )
    # event loop
    while window.is_alive():
        # read events from the window
        event, _values = window.read(timeout=500)
        # print("@Event:", event, "Values:", values)
        # check events
        if event == eg.TIMEOUT_KEY:
            elapsed = time.time() - start_time
            v = elapsed % 10
            window["-bar1"].update(v)
            window["-bar2"].update(v)
            continue
        if event == "Close":
            break
    window.close()


if __name__ == "__main__":
    main()
