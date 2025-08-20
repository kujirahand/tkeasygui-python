"""
FileBrowse test
"""

# import PySimpleGUI as sg
import TkEasyGUI as eg

# window create
window = eg.Window(
    "FileBrowser test",
    layout=[
        [eg.Text("File path:")],
        [eg.Input("", key="-filepath1-"), eg.FileBrowse()],
        [eg.Text("Multiple path:")],
        [eg.Input("", key="-filepath2-"), eg.FilesBrowse()],
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
        a = [
            f"path1={values['-filepath1-']}",
            f"path2={values['-filepath2-']}",
            f"folder={values['-folderpath-']}",
        ]
        eg.popup("Selected:\n" + "\n".join(a))
        break
window.close()
