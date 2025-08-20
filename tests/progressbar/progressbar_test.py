"""Progressbar Example"""
# pylint: disable=line-too-long
import time
import TkEasyGUI as eg

def main():
    """Main function"""
    start_time = time.time()
     # Create a window
    window = eg.Window("Progressbar Test", layout=[
        [eg.Label("00:00", key="-label", text_align="center", expand_x=True, font=("Arial", 20))],
        [eg.Progressbar(value_range=(0, 60), default_value=0, key="-bar1", expand_x=True)],
        [eg.Progressbar(value_range=(0, 60), default_value=0, key="-bar2", expand_x=True)],
        [eg.Button("Close", expand_x=True)],
    ])
    # event loop
    while window.is_alive():
        # read events from the window
        event, _values = window.read(timeout=500)
        # print("@Event:", event, "Values:", values)
        # check events
        if event == eg.TIMEOUT_KEY:
            elapsed = time.time() - start_time
            bar1 = int(elapsed / 60) % 60
            bar2 = elapsed % 60
            window["-bar1"].update(bar1)
            window["-bar2"].update(bar2)
            window["-label"].update(f"{bar1:02}:{int(bar2):02}")
            continue
        if event == "Close":
            break
    window.close()

if __name__ == "__main__":
    main()
