from PIL import Image

import TkEasyGUI as sg

# load background image
back_image = Image.open("b.jpg").resize((400, 400))

def main():
    layout = [
        [sg.Graph(
            canvas_size=(400, 400),
            key='-canvas-',
        )],
        [sg.Button('Close')]]
    # create window
    window = sg.Window('graph test', layout)
    canvas: sg.Graph = window['-canvas-']
    # event loop
    angle = 0
    while True:
        event, _ = window.read(timeout=100)
        if event in [sg.WINDOW_CLOSED, "Close"]:
            break
        # draw image
        canvas.erase()
        canvas.draw_image(data=back_image, location=(0, 0))
        angle1 = angle % 360
        angle2 = (angle + 90) % 360
        color = sg.rgb(100, 206 + (angle * 5 % 50), 156 + ((angle * 10) % 100))
        canvas.draw_arc((100, 100), (300, 300), start_angle=angle1, extent=angle2, fill_color=color, arc_color="white")
        angle += 1
        window.refresh()
    window.close()

if __name__ == '__main__':
    main()

