import tkinter as tk
from tkinter import ttk
from queue import Queue
import threading
from typing import Any
from pprint import pprint

#------------------------------------------------------------------------------
# Const
#------------------------------------------------------------------------------
WINDOW_CLOSED: str = "WINDOW_CLOSED"

#------------------------------------------------------------------------------
# Widget wrapper
#------------------------------------------------------------------------------
class Window:
    def __init__(self, title: str, layout: list[list[Any]], size: (tuple[int, int]|None)=None) -> None:
        """Create a window with a layout of widgets."""
        self.window: tk.Tk = tk.Tk()
        self.timeout: int|None = None
        self.timeout_key: str = "-TIMEOUT-"
        self.timeout_id: str|None = None
        self.events: Queue = Queue()
        self.frame: ttk.Frame = ttk.Frame(self.window, padding=10)
        self.frame.pack()
        self.key_elements: dict[str, Element] = {}
        self.last_values: dict[str, Any] = {}
        # set prop
        self.window.title(title)
        self.window.protocol("WM_DELETE_WINDOW", lambda : window_close_handler(self))
        if size is not None:
            self.window.geometry(f"{size[0]}x{size[1]}")
        # create widgets
        for row, widgets in enumerate(layout):
            frame_row = ttk.Frame(self.frame)
            frame_row.pack()
            for col, elem in enumerate(widgets):
                widget: tk.Widget = elem.create(self, frame_row)
                widget.grid(row=row, column=col)
                if elem.key != "":
                    self.key_elements[elem.key] = elem

    def read(self, timeout: int|None=None, timeout_key: str="-TIMEOUT-") -> tuple[str, dict[str, Any]]:
        """Read events from the window."""
        self.timeout = timeout
        self.timeout_key = timeout_key
        timeout = self.timeout if self.timeout is not None else 100
        while True:
            self.timeout_id = self.window.after(timeout, _timeout_handler, self)
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
                continue
            # get value from widget if possible
            try:
                values[key] = val.get()
            except:
                # if not possible, return last_values
                return self.last_values
        # set cache
        self.last_values = values
        return values

    def _event_handler(self, key: str, values: dict[str, Any]|None) -> None:
        """Handle an event."""
        if values is None:
            values = {}
        for k, v in self.get_values().items():
            values[k] = v
        self.events.put((key, values))
        
    def close(self) -> None:
        """Close the window."""
        self.events.put(WINDOW_CLOSED, self.get_values())
        try:
            self.window.quit()
            self.window.destroy()
        except:
            pass
    
    def __getitem__(self, key: str) -> Any:
        """Get an element by its key."""
        return self.key_elements[key]

#------------------------------------------------------------------------------
# Element
#------------------------------------------------------------------------------
class Element:
    """Element class."""
    def __init__(self, element_type, key: str="", **kw) -> None:
        """Create an element."""
        self.element_type: str = element_type
        self.key = key
        self.has_value: bool = False
        self.props: dict[str, Any] = kw
        self.widdget: Any|None = None

    def create(self, win: Window, parent: tk.Widget) -> Any:
        """Create a widget."""
        return None
    
    def get(self) -> Any:
        """Get the value of the widget."""
        return "-"
    
    def update(self, *args, **kw) -> None:
        """Update the widget."""
        for k, v in kw.items():
            self.props[k] = v
        # if self.widget is not None:
        #    self.widget.config(**kw)

class Text(Element):
    """Text element."""
    def __init__(self, text: str, **kw) -> None:
        super().__init__("Text", **kw)
        self.props["text"] = text
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.widget: tk.Widget = tk.Label(parent, **self.props)
        return self.widget
    def get(self) -> Any:
        """Get the value of the widget."""
        return self.props["text"]

class Button(Element):
    """Button element."""
    def __init__(self, text: str="", key: str="", **kw) -> None:
        super().__init__("Button", **kw)
        if key == "":
            key = text
        self.key = key
        self.has_value = False
        self.props["text"] = text
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.widget = tk.Button(parent, **self.props)
        self.widget.bind("<Button-1>", lambda e: win._event_handler(self.key, {"event": e}))
        return self.widget
    def get(self) -> Any:
        """Get the value of the widget."""
        return self.props["text"]

class TextInput(Element):
    """Text input element."""
    def __init__(self, text: str, key: str="", **kw) -> None:
        super().__init__("TextInput", **kw)
        self.props["text"] = text
        self.has_value = True
        if key == "":
            key = f"-TextInput-{get_element_id()}-"
        self.key = key
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.string_var = tk.StringVar()
        self.props["textvariable"] = self.string_var
        self.widget = tk.Entry(parent, name=self.key, **self.props)
        return self.widget
    def get(self) -> Any:
        """Get the value of the widget."""
        return self.string_var.get()

class Multiline(Element):
    """Multiline text input element."""
    def __init__(self, default_text: str="", key: str="", **kw) -> None:
        super().__init__("Multiline", **kw)
        self.props["default_text"] = default_text
        self.has_value = True
        if key == "":
            key = f"-Mulitline-{get_element_id()}-"
        self.key = key
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        # size
        size = self.props.pop("size", (40, 15))
        self.props["width"] = size[0]
        self.props["height"] = size[1]
        # text
        default_text = self.props.pop("default_text", "")
        self.widget = tk.Text(parent, name=self.key, **self.props)
        self.widget.insert("1.0", default_text)
        return self.widget
    def get(self) -> Any:
        """Get the value of the widget."""
        return self.widget.get("1.0", "end -1c") # get all text
    def update(self, *args, **kw) -> None:
        """Update the widget."""
        if len(args) >= 1:
            text = args[0] # get text
            self.widget.delete("1.0", "end") # clear text
            self.widget.insert("1.0", text) # set text
        for k, v in kw.items():
            self.props[k] = v
        self.widget.config(**kw)


#------------------------------------------------------------------------------
# Utility functions
#------------------------------------------------------------------------------

def _timeout_handler(self: Window):
    """Handle a timeout event."""
    if self.timeout_id is not None:
        self.window.after_cancel(self.timeout_id)
    if self.timeout is not None:
        self._event_handler("-TIMEOUT-", None)
    self.window.quit()

def window_close_handler(self: Window):
    """Handle a window close event."""
    if self.timeout_id is not None:
        self.window.after_cancel(self.timeout_id)
    self._event_handler(WINDOW_CLOSED, None)
    try:
        self.window.quit()
        self.window.destroy()
    except:
        pass

element_id: int = 0
def get_element_id() -> int:
    """Get a unique id for an element."""
    global element_id
    lock = threading.Lock()
    lock.acquire()
    element_id += 1
    lock.release()
    return element_id
