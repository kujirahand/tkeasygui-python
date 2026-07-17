"""
# Popup Input test with validation
"""

import TkEasyGUI as eg

a_color = eg.input(
    "What color do you like?\nPlease input the pattern `[A-Za-z]+`.",
    validation=r"^[A-Za-z]+$",
)
if (a_color is not None) and (a_color != ""):
    eg.print(f"OK, You like {a_color}.")
else:
    eg.print("You canceled the input.")
