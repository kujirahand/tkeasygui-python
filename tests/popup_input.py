import TkEasyGUI as eg

name = eg.popup_get_text("Input your name", title="Input", default_text="Kujira")
eg.popup(f"Hello, {name}!")
