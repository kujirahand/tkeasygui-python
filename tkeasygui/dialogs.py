import tkinter.messagebox as msg
import tkinter.simpledialog as simpledialog

#------------------------------------------------------------------------------
# Dialogs
#------------------------------------------------------------------------------
def popup(message: str, title: str = "") -> None:
    """Display a message in a popup window."""
    msg.showinfo(title, message)

def popup_yes_no(message: str, title: str = "") -> bool:
    """Display a message in a popup window with Yes and No buttons. Return True if Yes is clicked, False if No is clicked."""
    return msg.askyesno(title, message)

def popup_get_text(message: str, title: str = "", default: str = "") -> (str|None):
    """Display a message in a popup window with a text entry. Return the text entered."""
    return simpledialog.askstring(title, message, initialvalue=default)

