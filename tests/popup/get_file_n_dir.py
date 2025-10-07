"""file dialogs Example"""

import TkEasyGUI as eg

selected_file = eg.popup_get_file(
    "Select a file", file_types=[("text file", "*.txt"), ("all", "*")]
)
if selected_file is not None:
    eg.print("You selected:", selected_file)

selected_dir = eg.popup_get_folder("Select a folder")
if selected_dir is not None:
    eg.print("You selected:", selected_dir)
