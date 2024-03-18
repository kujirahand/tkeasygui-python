import io
from PIL import Image # 画像を読み取るため
# import PySimpleGUI as sg
import tkeasygui as sg

# load background image
BACK_IMAGE = "./clock-back.jpg"
back_image = Image.open(BACK_IMAGE)
back_image = back_image.resize((400, 400))
# convert image to bytes
img_bytes = io.BytesIO()
back_image.save(img_bytes, format='PNG')
img_bytes = img_bytes.getvalue()

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
        canvas.draw_image(data=img_bytes, location=(0, 0))
        angle1 = angle % 360
        angle2 = (angle + 90) % 360
        color = sg.rgb(100, 206 + (angle * 5 % 50), 156 + ((angle * 10) % 100))
        canvas.draw_arc((100, 100), (300, 300), start_angle=angle1, extent=angle2, fill_color=color, arc_color="white")
        angle += 1
        window.refresh()
    window.close()

if __name__ == '__main__':
    main()
