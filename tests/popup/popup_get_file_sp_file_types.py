"""
### popup_get_file - Specify file types
"""

import TkEasyGUI as eg

FILES_DELIMITER = "|"

# file types
file_types = (
    ("Image files", "*.jpg;*.jpeg;*.jpe;*.heic;*.png;*.gif"),
    ("All files", "*.*"),
)
# popup
files = eg.popup_get_file(
    "Please select images.",
    file_types=file_types,
    multiple_files=True,
    files_delimiter=FILES_DELIMITER,
)
print(f"raw={files}")
if files not in (None, ""):
    print(files.split(FILES_DELIMITER))
