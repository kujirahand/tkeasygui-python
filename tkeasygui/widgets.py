import tkinter as tk
from tkinter import ttk
from queue import Queue
import threading
from typing import Any, Literal
from pprint import pprint

#------------------------------------------------------------------------------
# Const
#------------------------------------------------------------------------------
WINDOW_CLOSED: str = "WINDOW_CLOSED"
LISTBOX_SELECT_MODE_MULTIPLE: str = 'multiple'
LISTBOX_SELECT_MODE_BROWSE: str = 'browse'
LISTBOX_SELECT_MODE_EXTENDED: str = 'extended'
LISTBOX_SELECT_MODE_SINGLE: str = 'single'

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
            frame_row.pack(expand=True, fill="x")
            for col, elemment in enumerate(widgets):
                # create widget
                try:
                    elem: Element = elemment
                    elem.prepare_create(self)
                    widget: tk.Widget = elem.create(self, frame_row)
                except Exception as e:
                    raise Exception(f"Failed to create widget: {elem.element_type} {elem.key} {elem.props} --- {e}") from e
                # check expand_x
                if elem.expand_x or elem.expand_y:
                    widget.pack(expand=True, fill=elem._get_fill_prop())
                else:
                    widget.grid(row=0, column=col)
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
        self.events.put((WINDOW_CLOSED, self.get_values()))
        try:
            self.window.quit()
            self.window.destroy()
        except:
            pass
    
    def write_event_value(self, key: str, values: dict[str, Any]) -> None:
        self.events.put((key, values))
    
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
        self.expand_x: bool = False
        self.expand_y: bool = False
    
    def _get_fill_prop(self) -> Literal["none", "x", "y", "both"]:
        """Get the fill property."""
        if self.expand_x and self.expand_y:
            return "both"
        if self.expand_x:
            return "x"
        elif self.expand_y:
            return "y"
        return "none"

    def prepare_create(self, win: Window) -> None:
        # convert properties
        # size
        if "size" in self.props:
            size = self.props.pop("size", (8, 1))
            self.props["width"] = size[0]
            self.props["height"] = size[1]
        # background_color
        if "background_color" in self.props:
            self.props["bg"] = self.props.pop("background_color")
            self.props["readonlybackground"] = self.props["bg"]
        if "text_color" in self.props:
            self.props["fg"] = self.props.pop("text_color")
        # expand_x
        if "expand_x" in self.props:
            self.props.pop("expand_x")
            self.expand_x = True
        if "expand_y" in self.props:
            self.props.pop("expand_y")
            self.expand_y = True
        if "readonly" in self.props:
            b = self.props.pop("readonly")
            self.props["state"] = "readonly" if b else "normal"
        # convert "select_mode" to "selectmode"
        for key in self.props.keys():
            if "-" in key:
                new_key = key.replace("-", "")
                self.props[new_key] = self.props.pop(key)

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
    
    def GetText(self) -> Any:
        """Get the text of the widget. (for Button)"""
        return self.get()

class Text(Element):
    """Text element."""
    def __init__(self, text: str, **kw) -> None:
        super().__init__("Text", **kw)
        self.props["text"] = text
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.widget: tk.Label = tk.Label(parent, **self.props)
        return self.widget
    def get(self) -> Any:
        """Get the value of the widget."""
        return self.props["text"]
    def update(self, *args, **kw) -> None:
        """Update the widget."""
        super().update(*args, **kw)
        if len(args) >= 1:
            text = args[0]
            self.props["text"] = text
            self.widget.config(text=text)
        self.widget.config(**kw)

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

class Input(Element):
    """Text input element."""
    def __init__(self, text: str, key: str="", **kw) -> None:
        super().__init__("Input", **kw)
        self.props["text"] = text
        self.has_value = True
        if key == "":
            key = f"-Input-{get_element_id()}-"
        self.key = key
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.string_var = tk.StringVar()
        self.props["textvariable"] = self.string_var
        self.widget = tk.Entry(parent, name=self.key, **self.props)
        return self.widget
    def get(self) -> Any:
        """Get the value of the widget."""
        return self.string_var.get()
    def update(self, *args, **kw) -> None:
        """Update the widget."""
        super().update(*args, **kw)
        text = self.props["text"]
        if len(args) >= 1:
            text = args[0]
        self.props["text"] = text
        self.string_var.set(text)
        self.widget.delete(0, "end")
        self.widget.insert(0, text)
        self.widget.config(**kw)

class InputText(Input):
    """InputText element. (alias of Input)"""
    def __init__(self, text: str, key: str="", **kw) -> None:
        super().__init__(text, key, **kw)
        self.element_type = "InputText"

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

class Listbox(Element):
    """Listbox element."""
    def __init__(self, values: list[str]=[], key: str="", enable_events: bool=False, select_mode: str="browse", **kw) -> None:
        super().__init__("Listbox", **kw)
        self.values = values
        self.has_value = True
        self.enable_events = enable_events
        self.select_mode = select_mode
        if key == "":
            key = f"-Listbox-{get_element_id()}-"
        self.key = key
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.window: Window = win
        self.widget = tk.Listbox(parent, selectmode=self.select_mode, **self.props)
        for v in self.values:
            self.widget.insert("end", v)
        if self.enable_events:
            self.widget.bind("<<ListboxSelect>>", lambda e: self._listbox_events(e))
        return self.widget
    def get(self) -> Any:
        """Get the value of the widget."""
        selected: list[str] = []
        for i in self.widget.curselection():
            selected.append(self.values[int(i)])
        return selected

    def _listbox_events(self, _event: Any) -> list[str]:
        """Handle listbox events."""
        self.window._event_handler(self.key, {})

    def update(self, *args, **kw) -> None:
        """Update the widget."""
        if len(args) >= 1:
            values = args[0]
            kw["values"] = values
        self.values = kw["values"]
        # update list
        self.widget.delete(0, "end")
        for v in self.values:
            self.widget.insert("end", v)
        del kw["values"]
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