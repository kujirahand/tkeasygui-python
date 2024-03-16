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

def popup_get_text(message: str, title: str = "", default: str = "") -> (str|None):
    """Display a message in a popup window with a text entry. Return the text entered."""
    return simpledialog.askstring(title, message, initialvalue=default)

# Widget wrapper

class Window:
    def __init__(self, title: str, layout: list[list[Element]], size: (tuple[int, int]|None)=None) -> None:
        """Create a window with a layout of widgets."""
        self.window: tk.Tk = tk.Tk()
        self.timeout: int|None = None
        self.timeout_key: str = "-TIMEOUT-"
        self.timeout_id: str|None = None
        self.events: Queue = Queue()
        self.frame: ttk.Frame = ttk.Frame(self.window, padding=10)
        self.frame.pack()
        self.key_elements: dict[str, Element] = {}
        # set prop
        self.window.title(title)
        self.window.protocol("WM_DELETE_WINDOW", lambda : window_close_handler(self))
        if size is not None:
            self.window.geometry(f"{size[0]}x{size[1]}")
        # create widgets
        for row, widgets in enumerate(layout):
            for col, elem in enumerate(widgets):
                widget: tk.Widget = elem.create(self)
                widget.grid(row=row, column=col)
                if elem.key != "":
                    self.key_elements[elem.key] = elem

    def read(self, timeout: int|None=None, timeout_key: str="-TIMEOUT-") -> tuple[str, dict[str, Any]]:
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

    def get_values(self) -> dict[str, Any]:
        """Get values from the window."""
        values: dict[str, Any] = {}
        for key,val in self.key_elements.items():
            if not val.has_value:
                print("@@@skip", key, val.get())
                continue
            values[key] = val.get()
        return values

    def event_handler(self, key: str, values: dict[str, Any]|None) -> None:
        if values is None:
            values = {}
        for k, v in self.get_values().items():
            values[k] = v
        self.events.put((key, values))
        print("@@event_handler=", key, values)

element_id: int = 0
def get_element_id() -> int:
    """Get a unique id for an element."""
    global element_id
    lock = threading.Lock()
    lock.acquire()
    element_id += 1
    lock.release()
    return element_id

class Element:
    """Element class."""
    def __init__(self, element_type, key: str="", **kw) -> None:
        """Create an element."""
        self.element_type: str = element_type
        self.key = key
        self.has_value: bool = False
        self.props: dict[str, Any] = kw
        self.widdget: Any|None = None
        print("@@@", self.props)

    def create(self, win: Window) -> Any:
        """Create a widget."""
        return None
    
    def get(self) -> Any:
        """Get the value of the widget."""
        return "-"

class Text(Element):
    def __init__(self, text: str, **kw) -> None:
        super().__init__("Text", **kw)
        self.props["text"] = text
    def create(self, win: Window) -> tk.Widget:
        self.widget: tk.Widget = tk.Label(win.frame, **self.props)
        return self.widget
    def get(self) -> Any:
        """Get the value of the widget."""
        return self.props["text"]

class TextInput(Element):
    def __init__(self, text: str, key: str="", **kw) -> None:
        super().__init__("TextInput", **kw)
        self.props["text"] = text
        self.has_value = True
        if key == "":
            key = f"-TextInput-{get_element_id()}-"
        self.key = key
    def create(self, win: Window) -> tk.Widget:
        self.string_var = tk.StringVar()
        self.props["textvariable"] = self.string_var
        self.widget = tk.Entry(win.frame, name=self.key, **self.props)
        return self.widget
    def get(self) -> Any:
        """Get the value of the widget."""
        return self.string_var.get()


class Button(Element):
    def __init__(self, text: str="", key: str="", **kw) -> None:
        super().__init__("Button", **kw)
        if key == "":
            key = text
        self.key = key
        self.has_value = False
        self.props["text"] = text
    def create(self, win: Window) -> tk.Widget:
        self.widget = tk.Button(win.frame, **self.props)
        self.widget.bind("<Button-1>", lambda e: win.event_handler(self.key, {"event": e}))
        return self.widget
    def get(self) -> Any:
        """Get the value of the widget."""
        return self.props["text"]

def timeout_handler(self: Window):
    if self.timeout_id is not None:
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
