"""
OpenCV Camera Test
Please install OpenCV
```
pip install opencv-python
pip install opencv-contrib-python
```
"""

import cv2 as cv
import TkEasyGUI as sg
# import PySimpleGUI as sg

# camera
vc = cv.VideoCapture(0)
# layout
layout = [
    [sg.Button("Exit")],
    [sg.Image(key="-image-", size=(400, 300))],
]
# event loop
window = sg.Window("Camera Test", layout)
while True:
    event, values = window.read(timeout=1)
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    # capture
    ret, frame = vc.read()
    if ret:
        frame = cv.resize(frame, (400, 300), fx=0, fy=0)
        img = cv.imencode(".png", frame)[1].tobytes()
        window["-image-"].update(img)

vc.release()
window.close()
