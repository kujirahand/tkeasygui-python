"""
### Graph sample
"""

from PIL import Image

import TkEasyGUI as eg

# load background image
back_image = Image.open("b.jpg").resize((400, 400))


def main():
    """Graph sample"""
    layout = [
        [
            eg.Graph(
                canvas_size=(400, 400),
                key="-canvas-",
            )
        ],
        [eg.Button("Close")],
    ]
    # create window
    window = eg.Window("graph test", layout)
    canvas: eg.Graph = window["-canvas-"]
    # event loop
    angle = 0
    while True:
        event, _ = window.read(timeout=100)
        if event in [eg.WINDOW_CLOSED, "Close"]:
            break
        # draw image
        canvas.erase()
        canvas.draw_image(data=back_image, location=(0, 0))
        angle1 = angle % 360
        angle2 = (angle + 90) % 360
        color = eg.rgb(100, 206 + (angle * 5 % 50), 156 + ((angle * 10) % 100))
        canvas.draw_arc(
            (100, 100),
            (300, 300),
            start_angle=angle1,
            extent=angle2,
            fill_color=color,
            arc_color="white",
        )
        angle += 1
        window.refresh()
    window.close()


if __name__ == "__main__":
    main()
