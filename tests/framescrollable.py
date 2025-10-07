"""Frame element test"""

import TkEasyGUI as eg


def test_frame() -> None:
    """Frame element test"""
    frame_layout = [
        [eg.Text("Inside Frame")],
        [eg.Input(key="-in1-")],
        [eg.Input(key="-in2-")],
        [eg.Input(key="-in3-")],
        [eg.Input(key="-in4-")],
        [eg.HSeparator()],
        [eg.Input(key="-in5-")],
        [eg.Input(key="-in6-")],
        [eg.Input(key="-in7-")],
        [eg.Input(key="-in8-")],
        [eg.HSeparator()],
        [eg.Input(key="-in9-")],
        [eg.Input(key="-in10-")],
        [eg.Input(key="-in11-")],
        [eg.Input(key="-in12-")],
        [eg.HSeparator()],
        [eg.Button("OK")],
    ]
    frame = eg.FrameScrollable(
        "Frame Title",
        frame_layout,
        key="-FRAME-",
        size=(600, 200),
        horizontal_scroll=False,
    )
    window = eg.Window("Frame Test", layout=[[frame], [eg.Button("Exit")]])

    while True:
        event, _values = window.read()
        if event in (eg.WINDOW_CLOSED, "Exit"):
            break
        if event == "OK":
            break

    window.close()


if __name__ == "__main__":
    test_frame()
