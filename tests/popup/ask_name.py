"""A simple example using popup_input to ask for a name and then greet the user."""

import TkEasyGUI as eg

# import PySimpleGUI as eg
name = eg.popup_input("What is your name?", title="Name")
eg.popup(f"Hello, {name}!")
