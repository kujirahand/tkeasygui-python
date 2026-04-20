"""Sample code for popup_get_file()"""

import TkEasyGUI as eg

# Show File dialog
file_path = eg.popup_get_file("Select a file")
eg.print(f"You selected: {file_path}")

# Show File dialog for multiple files
files = eg.popup_get_file(
    "Select files",
    multiple_files=True,
    file_types=[("Text files", "*.txt"), ("All files", "*.*")],
)
if files:
    # Split the selected files into a list and show them in a popup
    files_list = files.split(eg.FILES_DELIMITER)
    eg.popup_listbox(files_list, "Selected files")
else:
    eg.popup("No files selected.")
