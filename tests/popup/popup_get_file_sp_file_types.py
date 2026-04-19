"""
### popup_get_file - Specify file types
"""

import TkEasyGUI as eg

# file types
file_types = [
    ("Image files", "*.jpg;*.jpeg;*.jpe;*.heic;*.png;*.gif"),
    ("All files", "*.*"),
]
# popup
files_str = eg.popup_get_file(
    "Please select images.",
    file_types=file_types,
    multiple_files=True,
    files_delimiter=eg.FILES_DELIMITER,
)
print(f"Selected: {files_str}")
if files_str:
    files = files_str.split(eg.FILES_DELIMITER)
    eg.popup_listbox(files, "Selected Files")
