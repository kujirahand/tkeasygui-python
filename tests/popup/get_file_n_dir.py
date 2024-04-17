import TkEasyGUI as eg

selected_file = eg.popup_get_file(
    "Select a file",
    file_types=[("text file", "*.txt"), ("all", "*")])
eg.popup("You selected:" + selected_file)
 
selected_dir = eg.popup_get_folder("Select a folder")
eg.popup("You selected:" + selected_file)
