import TkEasyGUI as sg

# file types
file_types = (
    ("Image files", "*.jpg;*.jpeg;*.jpe;*.heic;*.png;*.gif"),
    ("All files", "*.*"),
)
# popup
files = sg.popup_get_file(
    "Please select images.",
    file_types=file_types,
    multiple_files=True,
)
print(files)

