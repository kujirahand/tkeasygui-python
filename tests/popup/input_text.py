"""popup_get_text Example"""

import TkEasyGUI as eg

name = eg.popup_get_text("What is your name?")
if name:
    eg.popup("Hello, " + name + "!")
