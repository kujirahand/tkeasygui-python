import TkEasyGUI as sg

# Create window
layout = [
    [sg.Text("file:")],
    [
        sg.Input(key="-file-"),
        sg.FileBrowse(),  # FileBrowse button
    ],
    [sg.Text("folder:")],
    [
        sg.Input(key="-folder-"),
        sg.FolderBrowse(),  # FolderBrowse button
    ],
    [sg.CloseButton()],
]
window = sg.Window("FileBrowse Test", layout)

# Event loop
while window.is_running():
    # get window event
    event, values = window.read()
    print("@@@", event, values)
window.close()
