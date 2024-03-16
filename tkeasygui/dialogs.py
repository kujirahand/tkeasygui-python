import tkinter.messagebox as msg
import tkinter.simpledialog as simpledialog
import tkinter.filedialog as filedialog

#------------------------------------------------------------------------------
# Dialogs
#------------------------------------------------------------------------------
# like PySimpleGUI
def popup(message: str, title: str = "") -> None:
    """Display a message in a popup window."""
    msg.showinfo(title, message)

def popup_ok(message: str, title: str="") -> None:
    """Display a message in a popup window."""
    msg.showinfo(title, message)

def popup_yes_no(message: str, title: str = "Question") -> str:
    """Display a message in a popup window with Yes and No buttons. Return "Yes" or "No"."""
    return "Yes" if msg.askyesno(title, message) else "No"

def popup_yes_no_cancel(message: str, title: str = "Question") -> str:
    """Display a message in a popup window with Yes and No buttons. Return "Yes" or "No" or "Cancel"."""
    a = msg.askyesnocancel(title, message)
    if a is None:
        return "Cancel"
    return "Yes" if a else "No"

def popup_get_text(message: str, title: str = "", default: str = "") -> (str|None):
    """Display a message in a popup window with a text entry. Return the text entered."""
    return simpledialog.askstring(title, message, initialvalue=default)

def popup_error(message: str, title: str="Error") -> None:
    """Display a message in a popup window with an error icon."""
    msg.showerror(title, message, icon="error")

def popup_get_file(title: str="", initial_folder: str="", save_as: bool=False, multiple_files: bool=False, file_types: tuple[tuple[str, str]]=(("All Files", "*.*"),), **kw) -> (str|tuple[str]|None):
    """Popup a file selection dialog. Return the file selected."""
    if save_as:
        result = filedialog.asksaveasfilename(
            title=title,
            initialdir=initial_folder,
            filetypes=file_types,
            **kw)
    else:
        result = filedialog.askopenfilename(
            title=title, 
            initialdir=initial_folder,
            filetypes=file_types,
            multiple=multiple_files, # type: ignore
            **kw)
    return result

def popup_get_folder(title: str="", default_path: str="", **kw) -> (str|None):
    """Popup a folder selection dialog. Return the folder selected."""
    return filedialog.askdirectory(title=title, initialdir=default_path, **kw)

#------------------------------------------------------------------------------
# like TKinter
def ask_yes_no(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with Yes and No buttons. Return True or False."""
    return msg.askyesno(title, message)

def ask_ok_cancel(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with OK and Cancel buttons. Return True or False."""
    return msg.askokcancel(title, message)

def ask_retry_cancel(message: str, title: str="Question") -> bool:
    """Display a message in a popup window with Retry and Cancel buttons. Return True or False."""
    return msg.askretrycancel(title, message)

