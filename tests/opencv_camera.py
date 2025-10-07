"""
### OpenCV Camera Test

Please install OpenCV.

```
pip install opencv-python
pip install opencv-contrib-python
```
"""

try:
    import cv2 as cv
    HAS_OPENCV = True
except ImportError:
    cv = None
    HAS_OPENCV = False
    print("OpenCV is not installed. Please install opencv-python.")

import TkEasyGUI as eg

if not HAS_OPENCV:
    eg.popup_error("OpenCV is not installed. Please install opencv-python.")
    exit()

# camera
vc = cv.VideoCapture(0)
# layout
layout = [
    [eg.Button("Exit")],
    [eg.Image(key="-image-", size=(400, 300))],
]
# event loop
window = eg.Window("Camera Test", layout)
while True:
    event, values = window.read(timeout=100)
    print("#", event, values)
    if event in (eg.WIN_CLOSED, "Exit"):
        break
    # capture
    ret, frame = vc.read()
    if ret:
        frame = cv.resize(frame, (400, 300), fx=0, fy=0)
        img = cv.imencode(".png", frame)[1].tobytes()
        window["-image-"].update(img)

vc.release()
window.close()
