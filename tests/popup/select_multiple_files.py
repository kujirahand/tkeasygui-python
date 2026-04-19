"""Select multiple files with a custom delimiter."""

import TkEasyGUI as eg

selected_files = eg.popup_get_file(
    "Please select files.",
    title="Select Multiple Files",
    multiple_files=True,
    files_delimiter=eg.FILES_DELIMITER,
)

if selected_files in (None, ""):
    print("No files selected.")
else:
    print(f"raw={selected_files}")
    print("split:")
    for index, file_path in enumerate(
        str(selected_files).split(eg.FILES_DELIMITER), start=1
    ):
        print(f"  {index}. {file_path}")
