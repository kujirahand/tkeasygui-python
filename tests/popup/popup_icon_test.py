"""popup_info icon test"""
import os
import TkEasyGUI as eg

test_root = os.path.dirname(os.path.dirname(__file__))
icon_file = os.path.join(test_root, "a.jpg")

eg.popup_info(
    "icon test",
    title="Icon test",
    icon=icon_file,
    icon_size=(64, 64),
    window_icon=icon_file,
)
