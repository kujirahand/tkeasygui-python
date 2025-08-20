"""
Timer > TkEasyGUI for The 7 Tasks of GUI Programming

@ref https://7guis.github.io/7guis/tasks/
"""
# pylint: disable=line-too-long
import time
import TkEasyGUI as eg

def main():
    """Main function"""
    duration = 10  # default duration in seconds
     # Create a window
    window = eg.Window("Timer", layout=[
        [
            eg.Label("Elapsed Time:", size=(10, 1)),
            eg.Progressbar(value_range=(0, 100), default_value=50, key="-bar", expand_x=True)
        ],
        [eg.Label("11.8s", key="-label")],
        [
            eg.Label("Duration:", size=(10, 1)),
            eg.Slider(value_range=(1, 60), default=duration, key="-duration", size=(15, 1), enable_changed_events=True, expand_x=True)
        ],
        [eg.Button("Reset", expand_x=True)],
    ])
    start_time = time.time()
    # event loop
    while window.is_alive():
        # read events from the window
        event, values = window.read(timeout=100)
        print("@Event:", event, "Values:", values)
        # check events
        if event == eg.TIMEOUT_KEY:
            # Calculate elapsed time and percentage
            elapsed = time.time() - start_time
            if elapsed > duration:
                elapsed = duration
                continue
            per = min(elapsed / duration, 1.0)
            # update the progress bar and label
            window["-bar"].update(per * 100)
            window["-label"].update(f"{elapsed:.1f}s")
            continue
        if event == "-duration":
            # Update duration and reset start time
            duration = values["-duration"]
            start_time = time.time()
        if event == "Reset":
            start_time = time.time()
    window.close()

if __name__ == "__main__":
    main()
