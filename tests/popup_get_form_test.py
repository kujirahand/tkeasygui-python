"""popup_get_form Example"""

import TkEasyGUI as eg

# Ask simplely
result = eg.popup_get_form(["Name", "Hobbies"])
if result:
    name = result["Name"]
    hobbies = result["Hobbies"]
    eg.print(f"Hi, {name}. I know you like {hobbies}.")

# Ask with default values
result = eg.popup_get_form(
    [
        # Each item is a tuple: (label, default_or_selections, type)
        ("Name", "Suzu", "text"),
        ("Age", 20, "number"),
        ("Hobbies", ["Reading", "Writing"], "list"),
        ("OS", ["Windows", "macOS", "Ubuntu"], "combo"),
        ("Password", "", "password"),
        ("Date", "", "date"),
        ("File", "", "file"),
        ("Folder", "", "folder"),
        ("Theme Color", "", "color"),
    ],
    title="Form Test",
)
if result:
    print(result)
