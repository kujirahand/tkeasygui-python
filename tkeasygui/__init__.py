import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msg
import tkinter.simpledialog as simpledialog
from tkeasygui import *
from queue import Queue
import threading
from typing import Any, Callable

__version__ = "0.1.0"
WINDOW_CLOSED: str = "WINDOW_CLOSED"

def popup(message: str, title: str = "") -> None:
    """Display a message in a popup window."""
    msg.showinfo(title, message)

def popup_yes_no(message: str, title: str = "") -> bool:
    """Display a message in a popup window with Yes and No buttons. Return True if Yes is clicked, False if No is clicked."""
    return msg.askyesno(title, message)

def popup_get_text(message: str, title: str = "", default: str = "") -> str:
    """Display a message in a popup window with a text entry. Return the text entered."""
    return simpledialog.askstring(title, message, initialvalue=default)

# Widget wrapper
element_id: int = 0
def get_element_id() -> int:
    global element_id
    lock = threading.Lock()
    lock.acquire()
    element_id += 1
    lock.release()
    return element_id

class Window:
    def __init__(self, title: str, layout: list[list[tk.Widget]], size: tuple[int, int]=[None, None]) -> None:
        """Create a window with a layout of widgets."""
        self.window: tk.Tk = tk.Tk()
        self.timeout: int|None = None
        self.timeout_key: str = "-TIMEOUT-"
        self.timeout_id: str|None = None
        self.events: Queue = Queue()
        self.frame: ttk.Frame = ttk.Frame(self.window, padding=10)
        self.frame.pack()
        # set prop
        self.window.title(title)
        self.window.protocol("WM_DELETE_WINDOW", lambda : window_close_handler(self))
        if size[0] is not None:
            self.window.geometry(f"{size[0]}x{size[1]}")
        # create widgets
        for row, widgets in enumerate(layout):
            for col, elem in enumerate(widgets):
                widget: tk.Widget = elem.create(self)
                widget.grid(row=row, column=col)

    def read(self, timeout: int|None=None, timeout_key: str="-TIMEOUT-") -> tuple[str, dict[str, any]]:
        """Read events from the window."""
        self.timeout = timeout
        self.timeout_key = timeout_key
        timeout = self.timeout if self.timeout is not None else 100
        while True:
            self.timeout_id = self.window.after(timeout, timeout_handler, self)
            self.window.mainloop()
            if not self.events.empty():
                key, values = self.events.get()
                return (key, values)
            if self.timeout is not None:
                break
        return (self.timeout_key, {})

    def event_handler(self, key: str, values: dict[str, any]|None) -> None:
        if values is None:
            values = {}
        self.events.put((key, values))
        print("@@event_handler=", key, values)

class Element:
    """Element class."""
    def __init__(self, element_type, key: str="", **kw) -> None:
        """Create an element."""
        self.element_type: str = element_type
        if key == "":
            key = f"-{element_type}-{get_element_id()}-"
        self.key = key
        self.props: dict[str, any] = kw
        print("@@@", self.props)

    def create(self, win: Window) -> tk.Widget:
        """Create a widget."""
        return tk.Label(win.frame, text="-")

def timeout_handler(self: Window):
    self.window.after_cancel(self.timeout_id)
    if self.timeout is not None:
        self.event_handler("-TIMEOUT-", None)
    self.window.quit()

def window_close_handler(self: Window):
    if self.timeout_id is not None:
        self.window.after_cancel(self.timeout_id)
    self.event_handler(WINDOW_CLOSED, None)
    self.window.quit()
    self.window.destroy()

class Text(Element):
    def __init__(self, text: str, **kw) -> None:
        super().__init__("Text", **kw)
        self.props["text"] = text
    def create(self, win: Window) -> tk.Widget:
        return tk.Label(win.frame, **self.props)

class TextInput(Element):
    def __init__(self, text: str, **kw) -> None:
        super().__init__("TextInput", **kw)
        self.props["text"] = text
    def create(self, win: Window) -> tk.Widget:
        self.string_var = tk.StringVar()
        self.props["textvariable"] = self.string_var
        e = tk.Entry(win.frame, name=self.key, **self.props)
        return e


class Button(Element):
    def __init__(self, text: str="", key: str="", **kw) -> None:
        super().__init__("Button", **kw)
        if key == "":
            key = text
        self.key = key
        self.props["text"] = text
    def create(self, win: Window) -> tk.Widget:
        b = tk.Button(win.frame, **self.props)
        b.bind("<Button-1>", lambda e: win.event_handler(self.key, e))
        return b
