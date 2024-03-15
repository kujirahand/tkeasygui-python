import tkinter as tk
from tkeasygui import *

__version__ = "0.1.0"

def popup(message: str, title: str = "") -> None:
    """Display a message in a popup window."""
    tk.messagebox.showinfo(title, message)

def popup_yes_no(message: str, title: str = "") -> bool:
    """Display a message in a popup window with Yes and No buttons. Return True if Yes is clicked, False if No is clicked."""
    return tk.messagebox.askyesno(title, message)


