import TkEasyGUI as eg
# import PySimpleGUI as eg
name = eg.popup_input("What is your name?", title="Name")
eg.popup(f"Hello, {name}!")
