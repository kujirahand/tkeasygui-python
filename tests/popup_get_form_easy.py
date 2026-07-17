"""popup_get_form Simple example"""

import TkEasyGUI as eg

# Ask simply
result = eg.popup_get_form(["Name", "Hobbies"])
if result:
    name = result["Name"]
    hobbies = result["Hobbies"]
    eg.print(f"Hi, {name}. I know you like {hobbies}.")
else:
    eg.print("No input received.")

