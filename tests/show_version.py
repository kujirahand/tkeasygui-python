import subprocess
import TkEasyGUI as sg

WEB_SITE = "https://github.com/kujirahand/tkeasygui-python/"
# define layout
layout=[
    [sg.Text(f"TkEasyGUI v{sg.__version__}")],
    [sg.Button("Show web site"), sg.Button("Close")],
]
# window create
window = sg.Window("Version info", layout=layout, font=("Arial", 20))
# event loop
while window.is_alive():
    event, values = window.read()
    print("#", event, values)
    if event == "Close":
        break
    if event == "Show web site":
        if sg.is_mac():
            subprocess.call(f"open {WEB_SITE}", shell=True)
        else:
            subprocess.call(f"start {WEB_SITE}", shell=True)
window.close()
