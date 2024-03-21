"""
FileBrowse test
"""
# import PySimpleGUI as sg
import tkeasygui as sg

# window create
window = sg.Window("FileBrowser test", layout=[
    [sg.Text("File path:")],
    [sg.Input("", key="-filepath1-"), sg.FileBrowse()],
    [sg.Text("Multiple path:")],
    [sg.Input("", key="-filepath2-"), sg.FilesBrowse()],
    [sg.Text("Folder path:")],
    [sg.Input("", key="-folderpath-"), sg.FolderBrowse()],
    [sg.Button("OK")],
])
# event loop
while window.is_alive():
    event, values = window.read()
    print("#", event, values)
    if event == "OK":
        print(values)
        a = [f"path1={values['-filepath1-']}",
            f"path2={values['-filepath2-']}",
            f"folder={values['-folderpath-']}"]
        sg.popup("Selected:\n" + "\n".join(a))
        break
window.close()
