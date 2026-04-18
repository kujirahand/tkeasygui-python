"""
FileBrowse test
"""

# import PySimpleGUI as sg
import TkEasyGUI as eg

FILES_DELIMITER = "|"

# window create
window = eg.Window(
    "FileBrowser test",
    layout=[
        [eg.Text("File path:")],
        [eg.Input("", key="-filepath1-"), eg.FileBrowse()],
        [eg.Text("Multiple path:")],
        [eg.Input("", key="-filepath2-"), eg.FilesBrowse(files_delimiter=FILES_DELIMITER)],
        [eg.Text("Folder path:")],
        [eg.Input("", key="-folderpath-"), eg.FolderBrowse()],
        [eg.Button("OK")],
    ],
)
# event loop
while window.is_alive():
    event, values = window.read()
    print("#", event, values)
    if event == "OK":
        print(values)
        selected_multiple = values["-filepath2-"]
        selected_multiple_list = []
        if selected_multiple not in ("", None):
            selected_multiple_list = str(selected_multiple).split(FILES_DELIMITER)
        a = [
            f"path1={values['-filepath1-']}",
            f"path2={selected_multiple}",
            f"path2-list={selected_multiple_list}",
            f"folder={values['-folderpath-']}",
        ]
        eg.popup("Selected:\n" + "\n".join(a))
        break
window.close()
