"""
### FileBrowse and FolderBrowse sample

FileBrowse is a button that opens a file dialog.
FolderBrowse is a button that opens a folder dialog.
"""

import TkEasyGUI as eg

# Create window
layout = [
    [eg.Text("file:")],
    [
        eg.Input(key="-file-"),
        eg.FileBrowse(),  # FileBrowse button
        eg.Button("Copy", key="-copy-file-"),
    ],
    [eg.Text("folder:")],
    [
        eg.Input(key="-folder-"),
        eg.FolderBrowse(),  # FolderBrowse button
        eg.Button("Copy", key="-copy-folder-"),
    ],
    [eg.CloseButton()],
]
window = eg.Window("FileBrowse Test", layout)

# Event loop
while window.is_running():
    # get window event
    event, values = window.read()
    print("@@@", event, values)
    if event == "-copy-file-":
        eg.set_clipboard(values["-file-"])
        eg.print("Copied to clipboard:\n", values["-file-"])
    if event == "-copy-folder-":
        eg.set_clipboard(values["-folder-"])
        eg.print("Copied to clipboard:\n", values["-folder-"])
window.close()
