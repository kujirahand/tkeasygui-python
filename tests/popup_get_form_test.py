"""popup_get_form Example"""

import TkEasyGUI as eg

# Ask with default values
result = eg.popup_get_form(
    [
        # Each item is a tuple: (label, default_or_selections, type, hint)
        ("Name", "Suzu", "text", "Enter your name"),
        ("Age", 20, "number", "Enter your age"),
        ("Hobbies", ["Reading", "Writing"], "list"),
        ("OS", ["Windows", "macOS", "Ubuntu"], "combo", "Select your OS"),
        ("Password", "", "password"),
        ("Date", "", "date", "Enter a date (YYYY-MM-DD)"),
        ("File", "", "file", "Select a file"),
        ("Folder", "", "folder"),
        ("Theme Color", "", "color", "Select a color"),
    ],
    title="Form Test",
)
if result:
    print(result)
