import threading
import tkinter as tk
from pprint import pprint  # noqa: F401
from queue import Queue
from tkinter import ttk
from typing import Any, Literal

#------------------------------------------------------------------------------
# Const
#------------------------------------------------------------------------------
WINDOW_CLOSED: str = "WINDOW_CLOSED"
WIN_CLOSED: str = "WINDOW_CLOSED"
WINDOW_TIMEOUT: str = "-TIMEOUT-"
LISTBOX_SELECT_MODE_MULTIPLE: str = 'multiple'
LISTBOX_SELECT_MODE_BROWSE: str = 'browse'
LISTBOX_SELECT_MODE_EXTENDED: str = 'extended'
LISTBOX_SELECT_MODE_SINGLE: str = 'single'
TABLE_SELECT_MODE_NONE: str = tk.NONE
TABLE_SELECT_MODE_BROWSE: str = tk.BROWSE
TABLE_SELECT_MODE_EXTENDED: str = tk.EXTENDED

#------------------------------------------------------------------------------
# Widget wrapper
#------------------------------------------------------------------------------
class Window:
    """
    Main window object in TkEasyGUI
    """
    def __init__(self, title: str, layout: list[list[Any]], size: (tuple[int, int]|None)=None, resizable:bool=False, modal: bool=False, **kw) -> None:
        """Create a window with a layout of widgets."""
        self.modal: bool = modal
        # check active window
        active_win = _get_active_window()
        if active_win is None:
            active_win = tk.Tk()
            active_win.configure(width=1, height=1)
        self.window: tk.Tk|tk.Toplevel = tk.Tk() if not modal else tk.Toplevel(master=active_win)
        self.timeout: int|None = None
        self.timeout_key: str = WINDOW_TIMEOUT
        self.timeout_id: str|None = None
        self.events: Queue = Queue()
        self.key_elements: dict[str, Element] = {}
        self.last_values: dict[str, Any] = {}
        self.flag_alive: bool = True # Pressing the close button will turn this flag to False.
        # Frame
        self.frame: ttk.Frame = ttk.Frame(self.window, padding=10)
        self.frame.pack(expand=True, fill="both")
        self.frame.rowconfigure(0, weight=1)
        # set window properties
        self.window.title(title)
        self.window.protocol("WM_DELETE_WINDOW", lambda : self._close_handler())
        if size is not None:
            self.window.geometry(f"{size[0]}x{size[1]}")
        self.window.resizable(resizable, resizable)
        # prepare create
        for widgets in layout:
            for elemment in widgets:
                elemment.prepare_create(self)
        # create widgets
        self.need_focus_widget: tk.Widget|None = None
        for widgets in layout:
            frame_row = ttk.Frame(self.frame, padding=5)
            # columns
            row_prop: dict[str, Any] = {"expand": True, "fill": "x", "side": "top"}
            for _col, elemment in enumerate(widgets):
                # create widget
                try:
                    elem: Element = elemment
                    widget: tk.Widget = elem.create(self, frame_row)
                    # check key
                    if elem.key != "":
                        self.key_elements[elem.key] = elem
                    if elem.has_value or elem.key == "OK" or elem.key == "Yes":
                        self.need_focus_widget = widget
                except Exception as e:
                    raise Exception(f"Failed to create widget: {elem.element_type} {elem.key} {elem.props} --- {e}") from e
                fill_prop = elem._get_fill_prop()
                fill_prop["side"] = "left"
                widget.pack(**fill_prop)
                if elem.expand_y:
                    row_prop["fill"] = "both"
            # add row
            frame_row.pack(**row_prop)
        # check modal
        if modal:
            # check position
            parent = active_win
            if parent is not None:
                self.window.geometry(f"+{parent.winfo_x()+20}+{parent.winfo_y()+20}")
            # set modal action
            self.window.attributes("-topmost", 1) # topmost
            # self.window.transient(parent)
            self.window.grab_set()
            self.window.focus_force()
        else:
            if isinstance(self.window, tk.Tk):
                self.window.eval('tk::PlaceWindow . center')
        # push window
        _window_push(self)

    def move_to_center(self) -> None:
        """Move the window to the center of the screen."""
        if isinstance(self.window, tk.Tk):
            self.window.eval('tk::PlaceWindow . center')

    def read(self, timeout: int|None=None, timeout_key: str="-TIMEOUT-") -> tuple[str, dict[str, Any]]:
        """Read events from the window."""
        self.timeout = timeout
        self.timeout_key = timeout_key
        timeout = self.timeout if self.timeout is not None else 100
        while True:
            self.timeout_id = self.window.after(timeout, _timeout_handler, self)
            self.window.after(100, _focus_window, self)
            self.window.mainloop()
            if not self.events.empty():
                # return event
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
            except Exception:
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

    def _close_handler(self):
        """Handle a window close event."""
        if self.timeout_id is not None:
            self.window.after_cancel(self.timeout_id)
        self._event_handler(WINDOW_CLOSED, None)
        self.flag_alive = False
        try:
            self.window.quit() # exit from mainloop
        except Exception:
            pass

    def close(self) -> None:
        """Close the window."""
        global active_window
        try:
            _window_pop()
            self.flag_alive = False
            self.window.quit()
            self.window.destroy()
        except Exception as _:
            pass

    def is_alive(self) -> bool:
        """Check if the window is alive."""
        return self.flag_alive
    
    def cancel_close(self) -> None:
        """Cancel the close event."""
        self.flag_alive = True
    
    def write_event_value(self, key: str, values: dict[str, Any]) -> None:
        self.events.put((key, values))
    
    def __getitem__(self, key: str) -> Any:
        """Get an element by its key."""
        return self.key_elements[key]
    
    def hide(self) -> None:
        """Hide window"""
        self.window.withdraw()
    
    def show(self) -> None:
        self.window.deiconify()

def _timeout_handler(self: Window) -> None:
    """Handle a timeout event."""
    if self.timeout_id is not None:
        self.window.after_cancel(self.timeout_id)
    if self.timeout is not None:
        self._event_handler("-TIMEOUT-", None)
    self.window.quit()

def _focus_window(self: Window) -> None:
    """Focus window"""
    if not self.flag_alive:
        return
    if self.need_focus_widget is not None:
        self.need_focus_widget.focus_set()
        self.need_focus_widget = None
        

# active window
_window_list: list[Window] = []
def _get_active_window() -> tk.Tk|tk.Toplevel|None:
    """Get the active window."""
    if len(_window_list) == 0:
        return None
    return _window_list[-1].window

def _window_push(win: Window) -> None:
    """Push a window to the list."""
    _window_list.append(win)

def _window_pop() -> None:
    """Pop a window from the list."""
    _window_list.pop()

#------------------------------------------------------------------------------
# Element
#------------------------------------------------------------------------------
# for compatibility with PySimpleGUI and etc
element_propery_alias: dict[str, str] = {
    "ButtonText": "text",
    "label": "text",
    "caption": "text",
}
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
    
    def _get_fill_prop(self) -> dict[str, Any]:
        """Get the fill property in `pack` method."""
        prop = {"expand": False, "fill": "none"}
        if self.expand_x and self.expand_y:
            prop["expand"] = True
            prop["fill"] = "both"
        if self.expand_x:
            prop["expand"] = True
            prop["fill"] = "x"
        elif self.expand_y:
            prop["expand"] = True
            prop["fill"] = "y"
        return prop

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
            self.expand_x = self.props.pop("expand_x")
        if "expand_y" in self.props:
            self.expand_y = self.props.pop("expand_y")
        if "readonly" in self.props:
            b = self.props.pop("readonly")
            self.props["state"] = "readonly" if b else "normal"
        # convert "select_mode" to "selectmode"
        if "select_mode" in self.props:
            self.props["selectmode"] = self.props.pop("select_mode")

    def create(self, win: Window, parent: tk.Widget) -> Any:
        """Create a widget."""
        return None
    
    def get(self) -> Any:
        """Get the value of the widget."""
        return "-"
    
    def update(self, *args, **kw) -> None:
        """Update the widget props (only change `props`)"""
        for k, v in kw.items():
            self.props[k] = v
    
    def __getattr__(self, name: str) -> Any:
        """Get unknown attribute."""
        # Method called when the attribute is not found in the object's instance dictionary
        return self.__getitem__(name)

    def __getitem__(self, name: str) -> Any:
        """Get element property"""
        # For compatibility with PySImpleGUI
        if name in element_propery_alias:
            name = element_propery_alias[name]
        # check self.props
        if name in self.props:
            return self.props[name]
        # check widget native property
        if self.widdget is not None:
            if name in self.widdget:
                return self.widdget[name]
        # print("@@@error.name=", name)
        return None


class Text(Element):
    """Text element."""
    def __init__(self, text: str, justify: Literal["left","right","center"]="left", **kw) -> None:
        super().__init__("Text", **kw)
        self.props["text"] = text
        self.props["justify"] = justify
    
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        """Create a Text widget."""
        self.widget = tk.Label(parent, **self.props)
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
    def __init__(self, button_text: str="", key: str="", **kw) -> None:
        super().__init__("Button", **kw)
        if key == "":
            key = button_text
        self.key = key
        self.has_value = False
        self.props["text"] = button_text
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.widget = tk.Button(parent, **self.props)
        self.widget.bind("<Button-1>", lambda e: win._event_handler(self.key, {"event": e}))
        self.widget.bind("<KeyPress>", lambda e: _button_key_checker(e, self, win))
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


def _button_key_checker(e: tk.Event, self: Button, win: Window) -> None:
    """Check key event for button. (Enabled Return key)"""
    # if e.keysym == "Return" or e.keysym == "space":
    if e.keysym == "Return":
        win._event_handler(self.key, {"event": e}) # throw event

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

    def _listbox_events(self, _event: Any) -> None:
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

class Table(Element):
    """Table element."""
    def __init__(self, values: list[list[str]]=[], headings: list[str]=[], key: str="", justification: Literal["right","left","center",""]="",
                 auto_size_columns: bool = True, max_col_width: int = 0, font: tuple[str, int]|None=None,
                 enable_events: bool=False, select_mode: str="browse", **kw) -> None:
        """Create a table."""
        super().__init__("Table", **kw)
        self.values = values
        self.headings = headings
        self.has_value = True
        self.enable_events = enable_events
        self.select_mode = select_mode
        self.justification: str = {"": "", "right": "e", "center": "center", "left": "w"}[justification]
        self.auto_size_columns = auto_size_columns
        self.max_col_width = max_col_width # todo
        self.font = font # todo
        if key == "":
            key = f"-Table-{get_element_id()}-"
        self.key = key
    
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        """Create a Table widget."""
        self.window: Window = win
        # create treeview
        self.frame = ttk.Frame(parent, padding=1, relief="ridge", borderwidth=1)
        columns = tuple(i+1 for i, _ in enumerate(self.headings))
        tree = self.widget = ttk.Treeview(
            self.frame,
            columns=columns,
            show="headings",
            **self.props)
        # scroll bar
        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=tree.yview)
        scrollbar.pack(expand=True, fill=tk.Y, side=tk.RIGHT)
        self.widget.pack(expand=True, fill="both", side=tk.LEFT)
        tree.configure(yscrollcommand=scrollbar.set)
        # setting for column
        streatch = tk.YES if self.auto_size_columns else tk.NO
        for i, h in enumerate(self.headings):
            self.widget.heading(i+1, text=h, anchor="center")
            kw: dict[str, Any] = {"stretch": streatch}
            if self.justification != "":
                kw["anchor"] = self.justification
            self.widget.column(i+1, **kw)
        # add data
        self.set_values(self.values, self.headings)
        if self.enable_events:
            self.widget.bind("<<TreeviewSelect>>", lambda e: self._table_events(e))
        return self.frame
    
    def set_values(self, values: list[list[str]], headings: list[str]) -> None:
        """Set values to the table."""
        self.values = values
        self.headings = headings
        # clear
        self.widget.delete(*self.widget.get_children())
        # update heading
        for i, h in enumerate(self.headings):
            self.widget.heading(i+1, text=h, anchor="center")
        # add data
        for row in self.values:
            self.widget.insert(parent="", index="end", values=row)
    
    def get(self) -> Any:
        """Get the value of the widget."""
        record_id = self.widget.focus()
        record_values = self.widget.item(record_id, "values")
        return record_values

    def _table_events(self, _event: Any) -> None:
        """Handle events."""
        self.window._event_handler(self.key, {})

    def update(self, *args, **kw) -> None:
        """Update the widget."""
        if len(args) >= 1:
            values = args[0]
            kw["values"] = values
        self.values = kw["values"]
        # update list
        tree = self.widget
        for i in tree.get_children(): # clear all
            tree.delete(i)
        # set values
        self.set_values(self.values, self.headings)
        # 
        del kw["values"]
        self.widget.config(**kw)

#------------------------------------------------------------------------------
# Utility functions
#------------------------------------------------------------------------------

element_id: int = 0
def get_element_id() -> int:
    """Get a unique id for an element."""
    global element_id
    lock = threading.Lock()
    lock.acquire()
    element_id += 1
    lock.release()
    return element_id
