"""
TkEasyGUI Widgets
"""
import io
import threading
import tkinter as tk
from pprint import pprint  # noqa: F401
from queue import Queue
from tkinter import ttk
from typing import Any, Literal, TypeAlias

from PIL import ImageTk
from PIL.JpegImagePlugin import JpegImageFile
from PIL import Image as PILImage
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

# type
TextAlign: TypeAlias = Literal["left", "right", "center"]
FontType: TypeAlias = tuple[str, int]
PointType: TypeAlias = tuple[int, int] | tuple[float, float]
ElementType: TypeAlias = "Element"
# about color (Thanks)
# https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/

#------------------------------------------------------------------------------
# Widget wrapper
#------------------------------------------------------------------------------
class TkEasyError(Exception):
    def __init__(self, message="TkEasyError"):
        self.message = message
        super().__init__(self.message)

# only one root element
_root_window: tk.Tk | None = None
def get_root_window() -> tk.Tk:
    """Get root window."""
    global _root_window
    if _root_window is None:
        _root_window = tk.Tk()
        _root_window.attributes('-alpha', 0)
    return _root_window

# active window
_window_list: list["Window"] = []
def _get_active_window() -> tk.Toplevel|None:
    """Get the active window."""
    if len(_window_list) == 0:
        return None
    return _window_list[-1].window

def _window_push(win: "Window") -> None:
    """Push a window to the list."""
    _window_list.append(win)

def _window_pop() -> None:
    """Pop a window from the list."""
    _window_list.pop()

class Window:
    """
    Main window object in TkEasyGUI
    """
    def __init__(self, title: str, layout: list[list[ElementType]], size: (tuple[str, int]|None)=None, resizable:bool=False, modal: bool=False, **kw) -> None:
        """Create a window with a layout of widgets."""
        self.modal: bool = modal
        # check active window
        active_win = _get_active_window()
        if active_win is None:
            active_win = get_root_window()
        self.window: tk.Toplevel = tk.Toplevel(master=active_win)
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
        # create widgets
        self._create_widget(self.frame, layout)
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
    
    def _create_widget(self, parent: tk.Widget, layout: list[list["Element"]]):
        # prepare create
        for widgets in layout:
            for elemment in widgets:
                elemment.prepare_create(self)
        # create widgets
        self.need_focus_widget: tk.Widget|None = None
        for widgets in layout:
            frame_row = ttk.Frame(parent, padding=5)
            # columns
            prev_element: Element|None = None
            row_prop: dict[str, Any] = {"expand": True, "fill": "x", "side": "top"}
            for _col, elemment in enumerate(widgets):
                # create widget
                elem: Element = elemment
                elem.prev_element = prev_element # set prev_element
                if prev_element is not None:
                    prev_element.next_element = elem
                prev_element = elem
                try:
                    widget: tk.Widget = elem.create(self, frame_row)
                    # check key
                    if elem.key != "":
                        self.key_elements[elem.key] = elem
                    if elem.has_value or elem.key == "OK" or elem.key == "Yes":
                        self.need_focus_widget = widget
                    # has children?
                    if elem.has_children:
                        self._create_widget(widget, elem.layout)
                except Exception as e:
                    raise Exception(f"Failed to create widget: {elem.element_type} {elem.key} {elem.props}\n{e}") from e
                # pack widget
                print("@@@pack=", elem.expand_x, elem.expand_y)
                fill_prop = elem._get_fill_prop()
                fill_prop["side"] = "left"
                widget.pack(**fill_prop)
                # debug
                print(f"Create widget: {elem.element_type} {elem.key} {fill_prop}")
                if elem.expand_y:
                    row_prop["fill"] = "both"
            # add row
            frame_row.pack(**row_prop)
        # end of create

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
            # mainloop - should be called only once
            root = get_root_window()
            root.mainloop()
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
        """ Show hidden window (hide -> show)"""
        self.window.deiconify()
    
    def refresh(self) -> "Window":
        """Refresh window"""
        try:
            self.window.update()
        except Exception:
            pass
        return self

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

#------------------------------------------------------------------------------
# Element
#------------------------------------------------------------------------------
# for compatibility with PySimpleGUI and etc
element_propery_alias: dict[str, str] = {
    "ButtonText": "text",
    "label": "text",
    "caption": "text",
    "justify": "text_align"
}
class Element:
    """Element class."""
    def __init__(self, element_type, key: str="", **kw) -> None:
        """Create an element."""
        self.element_type: str = element_type
        self.key = key
        self.has_value: bool = False
        self.props: dict[str, Any] = kw
        self.widget: Any|None = None
        self.expand_x: bool = False
        self.expand_y: bool = False
        self.has_children: bool = False
        self.prev_element: Element|None = None
        self.next_element: Element|None = None
    
    def _get_fill_prop(self) -> dict[str, Any]:
        """Get the fill property in `pack` method."""
        prop: dict[str, Any] = {"expand": False, "fill": "none"}
        if self.expand_x and self.expand_y:
            prop["expand"] = True
            prop["fill"] = "both"
        elif self.expand_x:
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
            # self.props["readonlybackground"] = self.props["bg"]
        if "text_color" in self.props:
            self.props["fg"] = self.props.pop("text_color")
        # expand_x
        if "expand_x" in self.props:
            self.expand_x = self.props.pop("expand_x")
        if "expand_y" in self.props:
            self.expand_y = self.props.pop("expand_y")
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
    
    def widget_update(self, **kw) -> None:
        try:
            if self.widget is not None:
                self.widget.configure(**kw)
        except Exception as e:
            raise TkEasyError(f"TkEasyGUI.Element.widget_update.Error: key='{self.key}', try to update {kw}, {e}")
    
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
        if self.widget is not None:
            if name in self.widget:
                return self.widget[name]
        return None

class Frame(Element):
    """Frame element."""
    def __init__(self, title: str, layout: list[list[Element]], key: str = "", background_color: str|None=None, size: tuple[int, int]|None=None, **kw) -> None:
        super().__init__("Frame", **kw)
        self.has_children = True
        self.layout = layout
        self.key = key
        self.props["text"] = title
        if size is not None:
            self.props["size"] = size
        if background_color:
            self.props["background"] = background_color

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.widget = tk.LabelFrame(parent, name=self.key, **self.props)
        return self.widget

    def get(self) -> Any:
        """Return Widget"""
        return self.widget

    def update(self, *args, **kw) -> None:
        """Update the widget."""
        self.widget_update(**kw)
    
    def __getattr__(self, name):
        """Get unknown attribute."""
        if name in ["Widget"]:
            return self.widget
        return super().__getattr__(name)

class Text(Element):
    """Text element."""
    def __init__(self, text: str, text_align: TextAlign="left", font: FontType|None=None, **kw) -> None:
        super().__init__("Text", **kw)
        self.props["text"] = text
        self.props["justify"] = text_align
        self.props["font"] = font
    
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
            self.widget_update(text=text)
        self.widget_update(**kw)

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
    def GetText(self) -> str:
        """Get the text of the button. (compatibility with PySimpleGUI)"""
        return self.props["text"]
    def update(self, *args, **kw) -> None:
        """Update the widget."""
        super().update(*args, **kw)
        if len(args) >= 1:
            text = args[0]
            self.props["text"] = text
            self.widget_update(text=text)
        self.widget_update(**kw)

def _button_key_checker(e: tk.Event, self: Button, win: Window) -> None:
    """Check key event for button. (Enabled Return key)"""
    # if e.keysym == "Return" or e.keysym == "space":
    if e.keysym == "Return":
        win._event_handler(self.key, {"event": e}) # throw event

class Input(Element):
    """Text input element."""
    def __init__(self, text: str="", key: str="", background_color: str="white", color: str = "black", text_aligh: TextAlign="left",
                 readonly: bool=False, readonly_background_color: str="silver", **kw) -> None:
        super().__init__("Input", **kw)
        self.readonly: bool = readonly
        self.props["text"] = text # default text @see Input.create
        self.props["background"] = background_color
        self.props["foreground"] = color
        self.props["justify"] = text_aligh
        self.props["readonlybackground"] = readonly_background_color
        self.has_value = True
        if key == "":
            key = f"-input{get_element_id()}-"
        self.key = key
    
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        """create Input widget"""
        # set default text
        self.props["textvariable"] = tk.StringVar()
        # create
        self.widget = tk.Entry(parent, name=self.key, **self.props)
        # set text
        self.widget.insert(0, self.props["text"])
        # set readonly
        if self.readonly:
            self.set_readonly(self.readonly)
        return self.widget

    def get(self) -> Any:
        """Get the value of the widget."""
        return self.props["textvariable"].get()
    def set_readonly(self, readonly: bool) -> None:
        """set readonly"""
        self.readonly = readonly
        state = "readonly" if self.readonly else "normal"
        self.widget_update(state=state)
    def update(self, *args, **kw) -> None:
        """Update the widget."""
        super().update(*args, **kw)
        if self.widget is None:
            return
        text = self.props["text"]
        if len(args) >= 1:
            text = args[0]
        # check readonly
        if "readonly" in kw:
            self.readonly = True if kw.pop("readonly") else False
            self.set_readonly(self.readonly)
        # update text
        # 1. update widget state
        readonly = self.readonly
        if readonly:
            self.set_readonly(False)
        # 2. update text property
        self.props["text"] = text
        self.props["textvariable"].set(text)
        # 3. update widget text
        self.widget.delete(0, "end")
        self.widget.insert(0, text)
        # update readonly
        if readonly:
            self.set_readonly(True)
        # update others
        self.widget_update(**kw)

class InputText(Input):
    """InputText element. (alias of Input)"""
    pass

class Multiline(Element):
    """Multiline text input element."""
    def __init__(self, text: str="", default_text: str|None=None, key: str="",
                 color: str="black", background_color: str="white",
                 readonly: bool=False, readonly_background_color: str='silver',
                 size: tuple[int, int]=(50, 10),
                 **kw) -> None:
        super().__init__("Multiline", **kw)
        if default_text is not None:
            text = default_text
        self.props["text"] = text
        self.props["size"] = size
        self.props["foreground"] = color
        self.props["background"] = self.backgound_color = background_color
        self.readonly_background_color = readonly_background_color
        self.has_value = True
        self.readonly = readonly
        if key == "":
            key = f"-multiline{get_element_id()}-"
        self.key = key
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        # text
        text = self.props.pop("text", "")
        self.widget = tk.Text(parent, name=self.key, **self.props)
        self.widget.insert("1.0", text)
        # readonly
        if self.readonly:
            self.set_readonly(self.readonly)
        return self.widget
    def get(self) -> Any:
        """Get the value of the widget."""
        if self.widget is None:
            return ""
        text = self.widget.get("1.0", "end -1c") # get all text
        self.props["text"] = text
        return text
    def update(self, *args, **kw) -> None:
        """Update the widget."""
        if len(args) >= 1:
            text = args[0] # get text
            self.set_text(text)
        if "text" in kw:
            self.set_text(kw["text"])
        if "readonly" in kw:
            self.readonly = True if kw.pop("readonly") else False
            self.set_readonly(self.readonly)
        self.widget_update(**kw)
    def set_readonly(self, readonly: bool) -> None:
        """Set readonly"""
        self.readonly = readonly
        state = "disabled" if readonly else "normal"
        bgcolor = self.readonly_background_color if readonly else self.backgound_color
        self.widget_update(state=state, background=bgcolor)

    def set_text(self, text: str) -> None:
        """Set text"""
        if self.widget is None:
            return
        if self.readonly:
            self.widget_update(state="normal")
        self.props["text"] = text
        self.widget.delete("1.0", "end") # clear text
        self.widget.insert("1.0", text) # set text
        if self.readonly:
            self.widget_update(state="disabled")

class Slider(Element):
    """Slider element."""
    def __init__(self, key: str = "", range: tuple[float, float]=(1, 10), orientation: str="v", resolution: float=1, default_value: float|None=None, **kw) -> None:
        super().__init__("Slider", **kw)
        self.key = key
        self.has_value = True
        self.range = range
        self.resolution = resolution
        self.default_value = default_value if default_value is not None else range[0]
        self.orientation = orientation
        if orientation == "v":
            self.props["orient"] = "vertical"
        elif orientation == "h":
            self.props["orient"] = "horizontal"
        elif orientation == "vertical" or orientation == "horizontal":
            self.props["orient"] = orientation

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.scale_var = tk.DoubleVar()
        self.widget = tk.Scale(
            parent,
            name=self.key,
            variable=self.scale_var,
            from_=self.range[0], to=self.range[1],
            resolution=self.resolution,
            **self.props)
        return self.widget
    
    def get(self) -> Any:
        """Return Widget"""
        return self.scale_var

    def update(self, **kw) -> None:
        """Update the widget."""
        self.widget_update(**kw)

class Canvas(Element):
    """Canvas element."""
    def __init__(self, key: str="", background_color: str|None=None, size: tuple[int, int]=(300, 300), **kw) -> None:
        super().__init__("Canvas", **kw)
        self.key = key
        self.props["size"] = size
        if background_color:
            self.props["background"] = background_color

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.widget = tk.Canvas(parent, name=self.key, **self.props)
        return self.widget

    def get(self) -> Any:
        """Return Widget"""
        return self.widget

    def update(self, *args, **kw) -> None:
        """Update the widget."""
        self.widget_update(**kw)
    
    def __getattr__(self, name):
        """Get unknown attribute."""
        if name in ["Widget"]:
            return self.widget
        return super().__getattr__(name)

class Graph(Element):
    """Graph element."""
    def __init__(self, key: str="", background_color: str|None=None,
        size: tuple[int, int]=(300, 300), canvas_size: tuple[int, int]|None=None,
        graph_bottom_left: tuple[int, int]|None=None, graph_top_right: tuple[int, int]|None=None,
        **kw) -> None:
        super().__init__("Graph", **kw)
        self.key = key
        # <Coordinate> graph_Declared for compatibility, but not yet implemented.
        self.graph_bottom_left = graph_bottom_left
        self.graph_top_right = graph_top_right
        # </Coordinate>
        # <size>
        self.props["size"] = size
        if canvas_size is not None:
            self.props["size"] = canvas_size
        # </size>
        if background_color:
            self.props["background"] = background_color
        self.parent_window: Window|None = None

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.widget: tk.Canvas = tk.Canvas(parent, name=self.key, **self.props)
        self.parent_window = win
        return self.widget

    def get(self) -> Any:
        """Return Widget"""
        return self.widget

    def update(self, *args, **kw) -> None:
        """Update the widget."""
        self.widget_update(**kw)
    
    def __getattr__(self, name):
        """Get unknown attribute."""
        if name in ["Widget"]:
            return self.widget
        return super().__getattr__(name)
    
    def draw_line(self, point_from: PointType, point_to: PointType, color: str = 'black', width: int = 1) -> int:
        """Draw a line."""
        return self.widget.create_line(point_from, point_to, fill=color, width=width)
    
    def draw_lines(self, points: list[PointType], color='black', width=1) -> int:
        """Draw lines."""
        return self.widget.create_line(points, fill=color, width=width)
    
    def draw_point(self, point: PointType, size: int = 2, color: str = 'black') -> int:
        """Draw a point."""
        x, y = point
        size2: float = size / 2
        return self.widget.create_oval(x-size2, y-size2, x+size2, y+size2, fill=color)
    
    def draw_circle(self, center_location: PointType, radius: int|float, fill_color: str|None = None, line_color: str|None = 'black', line_width: int = 1) -> int:
        """Draw a circle."""
        x, y = center_location
        return self.widget.create_oval(x-radius, y-radius, x+radius, y+radius, fill=fill_color, outline=line_color, width=line_width)

    def draw_oval(self, top_left: PointType, bottom_right: PointType, fill_color: str|None = None, line_color: str|None = None, line_width: int = 1):
        """Draw an oval."""
        return self.widget.create_oval(top_left, bottom_right, fill=fill_color, outline=line_color, width=line_width)
    
    def draw_arc(self, top_left: PointType, bottom_right: PointType, extent: int|None = None, start_angle: int|None = None, style: str|None = None, arc_color: str|None = 'black', line_width: int = 1, fill_color: str|None = None) -> int:
        """Draw an arc."""
        return self.widget.create_arc(top_left, bottom_right, extent=extent, start=start_angle, style=style, outline=arc_color, width=line_width, fill=fill_color)
    
    def erase(self) -> None:
        """Delete all"""
        self.widget.delete("all")
    
    def draw_rectangle(self, top_left: PointType, bottom_right: PointType, fill_color: str|None=None, line_color: str|None=None, line_width: int|None=None) -> int:
        """Draw rectangle"""
        return self.widget.create_rectangle(top_left[0], top_left[1], bottom_right[0], bottom_right[1], fill=fill_color, outline=line_color, width=line_width)
    
    def draw_polygon(self, points: list[PointType], fill_color: str|None=None, line_color: str|None=None, line_width: int|None=None) -> None:
        """Draw polygon"""
        return self.widget.create_polygon(points, fill=fill_color, outline=line_color, width=line_width)
    
    def draw_text(self, text: str, location: PointType, color: str|None='black', font: FontType=None, angle: float|str|None=0, text_location: TextAlign=tk.CENTER) -> int:
        """Draw text"""
        x, y = location
        anchor = {"left": "w", "right": "e", "center": "center"}[text_location]
        return self.widget.create_text(x, y, text=text, font=font, fill=color, angle=angle, anchor=anchor)
    
    def draw_image(self, filename: str|None=None, data: bytes|None=None, location: PointType|None=None) -> int:
        """Draw image"""
        # check location
        if location is None:
            location = (0, 0)
        # load image
        image: tk.PhotoImage|None = get_image_tk(filename=filename, data=data)
        # important
        self.widget.image = image # type: ignore
        return self.widget.create_image(location, image=image, anchor=tk.NW)

class Image(Element):
    """Image element."""
    def __init__(self, source: bytes|str|None=None, filename=None, data=None, key: str="", background_color: str|None=None, size: tuple[int, int]=(300, 300), **kw) -> None:
        super().__init__("Image", **kw)
        self.key = key
        self.source = source
        self.filename = filename
        self.data = data
        if size is not None:
            self.props["size"] = size
        if background_color is not None:
            self.props["background"] = background_color

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        """Create a Image widget."""
        photo = get_image_tk(self.source, self.filename, self.data)
        self.widget = tk.Label(parent, image=photo, name=self.key, **self.props)
        self.widget.image = photo # type: ignore
        return self.widget

    def get(self) -> Any:
        """Return Widget"""
        return self.widget

    def update(self, source: bytes|str=None, filename: str|None=None, data: bytes|None=None, **kw) -> None:
        """Update the widget."""
        image = get_image_tk(source, filename, data)
        self.widget.configure(image=image)
        self.widget.image = image # type: ignore
        self.widget_update(**kw)
    
    def __getattr__(self, name):
        """Get unknown attribute."""
        if name in ["Widget"]:
            return self.widget
        return super().__getattr__(name)


class Listbox(Element):
    """Listbox element."""
    def __init__(self, values: list[str]=[], key: str="", enable_events: bool=False, select_mode: str="browse", **kw) -> None:
        super().__init__("Listbox", **kw)
        self.values = values
        self.has_value = True
        self.enable_events = enable_events
        self.select_mode = select_mode
        if key == "":
            key = f"-listbox{get_element_id()}-"
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
        if self.widget is None:
            return None
        selected: list[str] = []
        sel: None|Any = self.widget.curselection()
        if sel is not None:
            for i in sel:
                selected.append(self.values[int(i)])
        return selected

    def _listbox_events(self, _event: Any) -> None:
        """Handle listbox events."""
        self.window._event_handler(self.key, {})

    def update(self, *args, **kw) -> None:
        """Update the widget."""
        if self.widget is None:
            return
        if len(args) >= 1:
            values = args[0]
            kw["values"] = values
        self.values = kw["values"]
        # update list
        self.widget.delete(0, "end")
        for v in self.values:
            self.widget.insert("end", v)
        del kw["values"]
        self.widget_update(**kw)

class Table(Element):
    """Table element."""
    def __init__(self, values: list[list[str]]=[], headings: list[str]=[], key: str="", justification: TextAlign="center",
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
            key = f"-table{get_element_id()}-"
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
        if self.widget is None:
            return
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
        if self.widget is None:
            return []
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
        if self.widget is not None:
            tree = self.widget
            for i in tree.get_children(): # clear all
                tree.delete(i)
        # set values
        self.set_values(self.values, self.headings)
        # 
        del kw["values"]
        self.widget_update(**kw)

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

def rgb(r: int, g: int, b: int) -> str:
    r = r & 0xFF
    g = g & 0xFF
    b = b & 0xFF
    return f"#{r:02x}{g:02x}{b:02x}"

def get_image_tk(source: bytes|str|None=None, filename: str|None = None, data: bytes|None = None) -> tk.PhotoImage|None:
    """Get Image for tk"""
    # if source is bytes, set data
    if source is not None:
        if isinstance(source, str): # is filename
            filename = source
        else: # is data
            data = source
    # load from file?
    if filename is not None:
        try:
            return ImageTk.PhotoImage(file=filename)
        except Exception as e:
            raise TkEasyError(f"TkEasyGUI.Image.set_image.Error: filename='{filename}', {e}")
    # load from data
    if data is not None:
        try:
            # check if data is PILImage
            if isinstance(data, PILImage.Image):
                return ImageTk.PhotoImage(image=data)
            return ImageTk.PhotoImage(data=data)
        except Exception as e:
            print("[TkEasyGUI] get_image_tk.Error:", e, stderr=True)
            return data
    return None

def imagedata_to_bytes(image_data: PILImage) -> bytes:
    """Convert JPEG to PNG"""
    img_bytes = io.BytesIO()
    image_data.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    return img_bytes

def imagefile_to_bytes(filename: str) -> bytes:
    """Read image file and convert to bytes"""
    image = PILImage.open(filename)
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    return img_bytes
