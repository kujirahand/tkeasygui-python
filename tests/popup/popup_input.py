"""
# Popup Input test
"""
import os

import TkEasyGUI as eg

SCRIPT_DIR = os.path.dirname(__file__)
TESTS_DIR = os.path.dirname(SCRIPT_DIR)
IMAGE_FILE = os.path.join(TESTS_DIR, "a.jpg")

name = eg.input("What is your name?", default="John")
eg.print("Helo,", name, "! I am TkEasyGUI.")

ans = eg.popup_image("Do you like animals?", image_path=IMAGE_FILE)
eg.print("Answer is", ans)

ans = eg.popup_yes_no("Can you speak Japanese?", yes_value="can", no_value="no")
print(ans)  # "can" or "no"
if ans == "no":
    quit()

if eg.confirm("How are you?"):
    eg.print("It is good. Thank you.")
else:
    eg.print("I am sorry to hear that.")
