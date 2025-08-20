"""Auto screenshot example for popup_xxx() methods."""

import TkEasyGUI as eg

# set auto screenshot
eg.popup_set_options(auto_screenshot=True, auto_screenshot_filename="screenshot.png")

# popup
eg.popup_buttons(
    "POPUP TEST (Please wait a moments...)", auto_close_duration=2, buttons=[]
)

# preview screenshot
eg.popup_image(
    "screenshot.png",
    image_path=eg.POPUP_AUTO_SCREENSHOT_FILENAME,
    auto_close_duration=3,
)

# preview screenshot no2
eg.popup_image(
    "screenshot.png",
    image_path=eg.POPUP_AUTO_SCREENSHOT_FILENAME,
    auto_close_duration=3,
)
