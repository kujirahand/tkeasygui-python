"""
TkEasyGUI Widgets
"""
import io
import os
import tkinter as tk
from datetime import datetime
from queue import Queue
from tkinter import ttk
from typing import Any, Literal, TypeAlias

from PIL import Image as PILImage
from PIL import ImageTk

import tkeasygui as eg

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
TextVAlign: TypeAlias = Literal["top", "bottom", "center"]
FontType: TypeAlias = tuple[str, int]
PointType: TypeAlias = tuple[int, int] | tuple[float, float]
ElementType: TypeAlias = "Element"
EventMode: TypeAlias = Literal["user", "system"]
OrientationType: TypeAlias = Literal["v", "h", "vertical", "horizontal"]
ListboxSelectMode: TypeAlias = Literal["multiple", "browse", "extended", "single"]
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
        self.focus_timer_id: str|None = None
        self.events: Queue = Queue()
        self.key_elements: dict[str, Element] = {}
        self.last_values: dict[str, Any] = {}
        self.flag_alive: bool = True # Pressing the close button will turn this flag to False.
        self.layout: list[list[ElementType]] = layout
        self._event_hooks: dict[str, list[callable]] = {}
        # Frame
        self.frame: ttk.Frame = ttk.Frame(self.window, padding=10)
        # set window properties
        self.window.title(title)
        self.window.protocol("WM_DELETE_WINDOW", lambda : self._close_handler())
        if size is not None:
            self.window.geometry(f"{size[0]}x{size[1]}")
        self.window.resizable(resizable, resizable)
        # create widgets
        self._create_widget(self.frame, layout)
        # pack frame
        self.frame.pack(expand=True, fill="both")
        self.frame.rowconfigure(0, weight=1)
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
    
    def register_event_hooks(self, hooks: dict[str, list[callable]]) -> None:
        """
        [Window.register_event_hooks] Register event hooks. (append events)
        **Example**
        ```
        window.register_event_hooks({
            "-input-": [
                lambda event, values: print("1", event, values),
                lambda event, values: print("2", event, values),
                lambda event, values: True, # stop event propagation
                lambda event, values: print("3", event, values),
            ],
        ```
        **Note**
        - If you specify a function that returns True, it changes the event name to f"{event}-stopped" and then re-collects the values associated with keys that occur afterwards.
        - @see `Window.read`
        """
        for event_name, handle_list in hooks.items():
            for handle in handle_list:
                if not (event_name in self._event_hooks):
                    self._event_hooks[event_name] = []
                self._event_hooks[event_name].append(handle)
    
    def _create_widget(self, parent: tk.Widget, layout: list[list["Element"]]):
        """create widget from layout"""
        # check layout
        if not (len(layout) > 0 and (isinstance(layout[0], list) or isinstance(layout[0], tuple))):
            raise TkEasyError(f"Invalid layout, should specify a two-dimensional list: {layout}")
        # prepare create
        for widgets in layout:
            for elem in widgets:
                elem.prepare_create(self)
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
                # set window and parent
                elem.window = self
                elem.parent = frame_row
                # set prev_element and next_element
                elem.prev_element = prev_element # set prev_element
                if prev_element is not None:
                    prev_element.next_element = elem
                prev_element = elem
                try:
                    widget: tk.Widget = elem.create(self, frame_row)
                    # check key
                    self.key_elements[elem.key] = elem
                    # check focus widget
                    if elem.has_value and (self.need_focus_widget is None):
                        self.need_focus_widget = widget
                    # check specila key
                    if (self.need_focus_widget is None) and (elem.key == "OK" or elem.key == "Yes"):
                        self.need_focus_widget = widget
                    # has children?
                    if elem.has_children:
                        self._create_widget(widget, elem.layout)
                except Exception as e:
                    raise Exception(f"Failed to create widget: {elem.element_type} {elem.key} {elem.props}\n{e}") from e
                # bind event (before create)
                for event_name, handle_t in elem._bind_dict.items():
                    self.bind(elem, event_name, handle_t[0], handle_t[1], handle_t[2])
                # pack widget
                fill_props = elem._get_pack_props()
                widget.pack(**fill_props)
                # debug
                if elem.expand_y:
                    row_prop["fill"] = "both"
            # add row
            frame_row.pack(**row_prop)
        # end of create
        if self.need_focus_widget is not None:
            # print("focus_set", self.need_focus_widget)
            self.need_focus_widget.focus_set()

    def move_to_center(self) -> None:
        """Move the window to the center of the screen."""
        if isinstance(self.window, tk.Tk):
            self.window.eval('tk::PlaceWindow . center')

    def read(self, timeout: int|None=None, timeout_key: str="-TIMEOUT-") -> tuple[str, dict[str, Any]]:
        """ [Window.read] Read events from the window."""
        self.timeout = timeout
        self.timeout_key = timeout_key
        time_id = time_checker_start()
        while True:
            # set timeout
            if self.timeout_id is not None:
                self.window.after_cancel(self.timeout_id)
            self.timeout_id = self.window.after("idle", self._window_idle_handler)
            # set focus timer (once when window show)
            if self.focus_timer_id is None:
                self.focus_timer_id = self.window.after("idle", _focus_window, self) # focus timer
            # mainloop - should be called only once
            root = get_root_window()
            root.mainloop()
            # after mainloop, check events
            if not self.events.empty():
                break
            # check timeout
            if timeout is None:
                continue # no timeout
            interval = time_checker_end(time_id)
            if interval > timeout:
                return (self.timeout_key, {}) # return timeout event
        # return event
        key, values = self.events.get()
        if key in self._event_hooks:
            flag_stop = self._dispatch_event_hooks(key, values)
            if flag_stop:
                key = f"{key}-stopped" # change event name
                values = self.get_values() # collect values again
        return (key, values)
    
    def _dispatch_event_hooks(self, key: str, values: dict[str, Any]) -> bool:
        """Dispatch event hooks."""
        # execute _event_hooks
        flag_stop = False
        if key in self._event_hooks:
            for handle in self._event_hooks[key]:
                result = handle(key, values)
                if result is True:
                    flag_stop = True
                    break
        return flag_stop

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

    def _window_idle_handler(self) -> None:
        """Handle window idle event."""
        _exit_mainloop()

    def _event_handler(self, key: str, values: dict[str, Any]|None) -> None:
        """Handle an event."""
        # set value
        if values is None:
            values = {}
        for k, v in self.get_values().items():
            values[k] = v
        # put event
        self.events.put((key, values))
        _exit_mainloop()
    
    def _exit_main_loop(self) -> None:
        """Exit mainloop"""
        if self.timeout_id is not None:
            self.window.after_cancel(self.timeout_id)
        _exit_mainloop()

    def _close_handler(self):
        """Handle a window close event."""
        self.flag_alive = False
        if self.timeout_id is not None:
            self.window.after_cancel(self.timeout_id)
        self._event_handler(WINDOW_CLOSED, None)

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
    
    def bind(self, element: "Element", event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
        """[Window.bind] Bind element event and handler"""
        element._bind_dict[event_name] = (handle_name, propagate, event_mode)
        if element.widget is None:
            return
        # bind to widget
        w: tk.Widget = element.widget
        w.bind(
            event_name,
            lambda e: _bind_event_handler(self, element, handle_name, e, propagate=propagate, event_mode=event_mode)
        )

def _bind_event_handler(win: Window, elem: "Element", handle_name: str, event: tk.Event, propagate: bool=True, event_mode: EventMode = "user") -> None:
    """Handle an event."""
    elem.user_bind_event = event # for compatibility with PySimpleGUI
    if event_mode == "user":
        event_key = f"{elem.key}{handle_name}"
        event_val = {"event": event}
        win.events.put((event_key, event_val))
    elif event_mode == "system":
        event_key = elem.key
        event_val = {"event": event, "event_type": handle_name}
        for key, key_elem in win.key_elements.items():
            if key_elem.has_value:
                val = key_elem.get()
                event_val[key] = val
        win.events.put((event_key, event_val))
    # propagate
    if propagate:
        # todo
        pass

def _exit_mainloop() -> None:
    """Exit mainloop"""
    root = get_root_window()
    try:
        root.quit() # exit from mainloop
    except Exception:
        # print("_exit_mainloop: failed to exit mainloop")
        pass

def _focus_window(self: Window) -> None:
    """Focus window"""
    if not self.flag_alive:
        return
    if self.need_focus_widget is not None:
        self.need_focus_widget.focus_set()
        self.need_focus_widget = None
        _exit_mainloop()

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
    def __init__(self, element_type: str, key: str|None, **kw) -> None:
        """Create an element."""
        # check key
        if key is None or key == "":
            key = generate_element_key(element_type)
        # define properties
        self.key: str = key
        self.element_type: str = element_type
        self.has_value: bool = False
        self.props: dict[str, Any] = kw
        self.widget: Any|None = None
        self.expand_x: bool = False
        self.expand_y: bool = False
        self.has_children: bool = False
        self.prev_element: Element|None = None
        self.next_element: Element|None = None
        self.window: Window|None = None
        self.parent: tk.Widget|None = None
        self._bind_dict: dict[str, tuple[str, bool, EventMode]] = {}
        self.user_bind_event: tk.Event|None = None # when bind event fired then set this value
        self.vertical_alignment: TextVAlign = "center"
    
    def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
        """
        Bind event. @see `Window.bind`
        """
        self._bind_dict[event_name] = (handle_name, propagate, event_mode)
        if self.window is not None:
            self.window.bind(self, event_name, handle_name, propagate=propagate, event_mode=event_mode)

    def disptach_event(self, values: dict[str, Any]|None=None) -> None:
        """Dispatch event"""
        if values is None:
            values = {}
        if self.window is not None:
            self.window._event_handler(self.key, values)

    def _get_pack_props(self) -> dict[str, Any]:
        """Get the fill property in `pack` method."""
        props: dict[str, Any] = {"expand": False, "fill": "none", "side": "left"}
        # check expand
        if self.expand_x and self.expand_y:
            props["expand"] = True
            props["fill"] = "both"
        elif self.expand_x:
            props["expand"] = True
            props["fill"] = "x"
        elif self.expand_y:
            props["expand"] = True
            props["fill"] = "y"
        # print("pack.props=", self.key, props)
        return props

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
        # user bind events
        if "bind_events" in self.props:
            bind_events = self.props.pop("bind_events")
            self.bind_events(bind_events)

    def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> ElementType:
        """
        Bind user events
        **Example**
        ```
        # (1) bind events in the constructor
        eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
        # (2) bind events in the method
        eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
        ```
        """
        for event_name, handle_name in events.items():
            self.bind(event_name, handle_name, event_mode=event_mode)
        return self

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

    def get_prev_widget(self, target_key: str|None=None) -> tk.Widget:
        """Get the previous widget."""
        # check target_key
        target: tk.Widget = None
        if target_key:
            if target_key in self.window.key_elements:
                target = self.window.key_elements[target_key]
                return target
        # get prev_widget
        return self.prev_element

    def __getattr__(self, name: str) -> Any:
        """Get unknown attribute."""
        # Method called when the attribute is not found in the object's instance dictionary
        if self.widget is not None:
            if hasattr(self.widget, name):
                return self.widget.__getattribute__(name)
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
        super().__init__("Frame", key, **kw)
        self.has_children = True
        self.layout = layout
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

class Column(Element):
    """Frame element."""
    def __init__(self, layout: list[list[Element]], key: str = "", background_color: str|None=None,
                 vertical_alignment: TextVAlign="top",
                 size: tuple[int, int]|None=None, **kw) -> None:
        super().__init__("Column", key, **kw)
        self.has_children = True
        self.layout = layout
        self.vertical_alignment = vertical_alignment
        if size is not None:
            self.props["size"] = size
        if background_color:
            self.props["background"] = background_color
        # self.props["anchor"] = {"top": "n", "bottom": "s", "center": "center"}[vertical_alignment]

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.widget = tk.Frame(parent, name=self.key, **self.props)
        return self.widget

    def get(self) -> Any:
        """Return Widget"""
        return self.widget

    def update(self, *args, **kw) -> None:
        """Update the widget."""
        super().update(*args, **kw)
        self.widget_update(**kw)
    
    def __getattr__(self, name):
        """Get unknown attribute."""
        if name in ["Widget"]:
            return self.widget
        return super().__getattr__(name)

class Text(Element):
    """Text element."""
    def __init__(self, text: str, key: str|None=None, text_align: TextAlign="left", font: FontType|None=None, **kw) -> None:
        super().__init__("Text", key, **kw)
        self.props["text"] = text
        self.props["justify"] = text_align
        self.props["font"] = font
    
    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        """Create a Text widget."""
        self.widget = tk.Label(parent, **self.props)
        return self.widget
    
    def get(self) -> Any:
        """Get the value of the widget."""
        return self.get_text()
    
    def get_text(self) -> str:
        return self.props["text"]
    
    def set_text(self, text: str) -> None:
        """Set the text of the widget."""
        self.props["text"] = text
        self.widget_update(text=text)

    def update(self, text: str|None=None, *args, **kw) -> None:
        """Update the widget."""
        if text is not None:
            self.set_text(text)
        super().update(*args, **kw)
        self.widget_update(**kw)

class Button(Element):
    """Button element."""
    def __init__(self, button_text: str="", key: str="", **kw) -> None:
        if key == "":
            key = button_text
        super().__init__("Button", key, **kw)
        self.has_value = False
        self.props["text"] = button_text
        self.bind_events({
            "<Button-1>": "click",
            "<Button-3>": "right_click",
            "<Return>": "return",
        }, "system")

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.widget = tk.Button(parent, **self.props)
        return self.widget

    def get(self) -> Any:
        """Get the value of the widget."""
        return self.get_text()
    
    def set_text(self, text: str) -> None:
        """Set the text of the widget."""
        self.props["text"] = text
        self.widget_update(text=text)
    
    def get_text(self) -> str:
        return self.props["text"]

    def update(self, text: str|None=None, **kw) -> None:
        """Update the widget."""
        if text is not None:
            self.props["text"] = text
            self.widget_update(text=text)
        super().update(**kw)
        self.widget_update(**kw)
    
    def __getattr__(self, name: str) -> Any:
        """Get unknown attribute. """
        # Get the text of the button. (compatibility with PySimpleGUI)
        if name == "GetText":
            return self.get_text
        elif name == "ButtonText":
            return self.get_text()
        return super().__getattr__(name)

class Checkbox(Element):
    """Button element."""
    def __init__(self, text: str="", default: bool=False, key: str="", enable_events: bool=False, **kw) -> None:
        if key == "":
            key = text
        super().__init__("Button", key, **kw)
        self.has_value = False
        self.default_value = default
        self.props["text"] = text
        if enable_events:
            self.bind_events({
                "<Button-1>": "click",
                "<Button-3>": "right_click"
            }, "system")

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.checkbox_var = tk.BooleanVar(value=self.default_value)
        self.widget = tk.Checkbutton(parent, variable=self.checkbox_var, **self.props)
        return self.widget
    
    def get_value(self) -> Any:
        """Get the value of the widget."""
        return self.checkbox_var.get()

    def set_value(self, b: bool) -> None:
        """Set the value of the widget."""
        self.checkbox_var.set(b)

    def get(self) -> Any:
        """Get the value of the widget."""
        return self.get_value()

    def set_text(self, text: str) -> None:
        """Set the text of the widget."""
        self.props["text"] = text
        self.widget_update(text=text)

    def update(self, *args, **kw) -> None:
        """Update the widget."""
        super().update(*args, **kw)
        if len(args) >= 1:
            self.set_value(args[0])
        if len(args) >= 2:
            self.set_text(args[1])
        if "text" in kw:
            self.set_text(kw.pop("text"))
        if "value" in kw:
            print("set_value", kw)
            self.set_value(kw.pop("value"))
        self.widget_update(**kw)

class Input(Element):
    """Text input element."""
    def __init__(self, text: str="", key: str="",
                 enable_events: bool=False,
                 background_color: str|None=None, color: str|None=None,
                 text_aligh: TextAlign="left",
                 readonly: bool=False, readonly_background_color: str="silver", **kw) -> None:
        super().__init__("Input", key, **kw)
        self.readonly: bool = readonly
        self.props["text"] = text # default text @see Input.create
        if background_color is not None:
            self.props["background"] = background_color
        if color is not None:
            self.props["foreground"] = color
        self.props["justify"] = text_aligh
        self.props["readonlybackground"] = readonly_background_color
        self.has_value = True
        if enable_events:
            self.bind_events({
                "<FocusIn>": "focusin",
                "<FocusOut>": "focusout",
                "<Return>": "return",
                "<Key>": "key",
                "<Button-1>": "click",
                "<Button-3>": "right_click"
            }, "system")
    
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
                 enable_events: bool=False,
                 color: str|None=None, background_color: str|None=None,
                 readonly: bool=False, readonly_background_color: str='silver',
                 size: tuple[int, int]=(50, 10),
                 **kw) -> None:
        super().__init__("Multiline", key, **kw)
        if default_text is not None:
            text = default_text
        self.props["text"] = text
        self.props["size"] = size
        if color is not None:
            self.props["foreground"] = color
        if background_color is not None:
            self.props["background"] = self.backgound_color = background_color
        self.readonly_background_color = readonly_background_color
        self.has_value = True
        self.readonly = readonly
        # bind events
        if enable_events:
            self.bind_events({
                "<FocusIn>": "focusin",
                "<FocusOut>": "focusout",
                "<Return>": "return",
                "<Key>": "key",
                "<Button-1>": "click",
                "<Button-3>": "right_click"
            }, "system")

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

class Textarea(Multiline):
    """Textarea element. (alias of Multiline)"""
    pass

class Slider(Element):
    """Slider element."""
    def __init__(self, key: str = "", range: tuple[float, float]=(1, 10),
                 orientation: OrientationType="horizontal",
                 resolution: float=1, default_value: float|None=None,
                 enable_events: bool=False,
                 **kw) -> None:
        super().__init__("Slider", key, **kw)
        self.has_value = True
        self.range = range
        self.resolution = resolution
        self.default_value = default_value if default_value is not None else range[0]
        # check orientation
        self.orientation: OrientationType = orientation
        if orientation == "v":
            self.props["orient"] = "vertical"
        elif orientation == "h":
            self.props["orient"] = "horizontal"
        elif orientation == "vertical" or orientation == "horizontal":
            self.props["orient"] = orientation
        # event
        if enable_events:
            self.bind_events({
                "<ButtonRelease-1>": "release"
            }, "system")

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.scale_var = tk.DoubleVar()
        self.scale_var.set(self.default_value)
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
        return self.scale_var.get()

    def update(self, value: float|None=None, **kw) -> None:
        """Update the widget."""
        if value is not None:
            self.scale_var.set(value)
            self.disptach_event()
        else:
            self.widget_update(**kw)

class Canvas(Element):
    """Canvas element."""
    def __init__(self, key: str="", enable_events: bool=False, background_color: str|None=None, size: tuple[int, int]=(300, 300), **kw) -> None:
        super().__init__("Canvas", key, **kw)
        self.props["size"] = size
        if background_color:
            self.props["background"] = background_color
        if enable_events:
            self.bind_events({
                "<ButtonPress>": "mousedown",
                "<ButtonRelease>": "mouseup",
                "<Motion>": "mousemove"
            }, "system")

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
        if name in ["Widget", "tk_canvas"]: # compatibility with PySimpleGUI
            return self.widget
        return super().__getattr__(name)

class Graph(Element):
    """Graph element."""
    def __init__(self, key: str="", background_color: str|None=None,
            size: tuple[int, int]=(300, 300), canvas_size: tuple[int, int]|None=None,
            graph_bottom_left: tuple[int, int]|None=None, graph_top_right: tuple[int, int]|None=None,
            **kw) -> None:
        super().__init__("Graph", key, **kw)
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
        super().__init__("Image", key, **kw)
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
    def __init__(self, values: list[str]=[], key: str="", enable_events: bool=False, select_mode: ListboxSelectMode="browse", **kw) -> None:
        super().__init__("Listbox", key, **kw)
        self.values = values
        self.has_value = True
        self.select_mode = select_mode
        self.key = key
        # event
        if enable_events:
            self.bind_events({
                "<<ListboxSelect>>": "select"
            }, "system")

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        """[Listbox.create] create Listbox widget"""
        self.window: Window = win
        self.widget = tk.Listbox(parent, selectmode=self.select_mode, **self.props)
        # insert values
        self.set_values(self.values)
        return self.widget

    def set_values(self, values: list[str]) -> None:
        """Set values to list"""
        self.values = values
        if self.widget is not None:
            # delete all
            self.widget.delete(0, "end")
            # insert data
            for i, v in enumerate(self.values):
                self.widget.insert(i, v)

    def get(self) -> Any:
        """Get the value of the widget."""
        if self.widget is None:
            return None
        wg: tk.Listbox = self.widget
        selected: list[str] = []
        selections: Any = wg.curselection()
        if selections is not None:
            for i in selections:
                index: int = int(i)
                selected.append(self.values[index])
        return selected

    def update(self, *args, **kw) -> None:
        """Update the widget."""
        if self.widget is None:
            return
        if len(args) >= 1:
            values = args[0]
            self.set_values(values)
        if "values" in kw:
            self.set_values(kw.pop("values"))
        self.widget_update(**kw)

class Combo(Element):
    """Combo element."""
    def __init__(self, values: list[str]=[], default_value: str="", key: str="", enable_events: bool=False, **kw) -> None:
        super().__init__("Combo", key, **kw)
        self.values = values
        self.value: tk.StringVar|None = None
        self.default_value = default_value
        self.has_value = True
        # event
        if enable_events:
            self.bind_events({
                "<<ComboboxSelected>>": "select"
            }, "system")

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        """[Combo.create] create Listbox widget"""
        self.value = tk.StringVar(value=self.default_value)
        self.widget = ttk.Combobox(parent, values=self.values, textvariable=self.value, **self.props)
        return self.widget

    def set_values(self, values: list[str]) -> None:
        """Set values to list"""
        self.values = values
        if self.widget is not None:
            self.widget_update(values=self.values)
    
    def set_value(self, v: str) -> None:
        """Set the value of the widget."""
        self.value.set(v)

    def get(self) -> Any:
        """Get the value of the widget."""
        if self.widget is None:
            return None
        return self.value.get()

    def update(self, *args, **kw) -> None:
        """Update the widget."""
        if self.widget is None:
            return
        if len(args) >= 1:
            self.set_value(args[0])
        if "values" in kw:
            self.set_values(kw.pop("values"))
        if "value" in kw:
            self.set_value(kw.pop("value"))
        self.widget_update(**kw)

class Table(Element):
    """Table element."""
    def __init__(self, values: list[list[str]]=[], headings: list[str]=[], key: str="", justification: TextAlign="center",
                 auto_size_columns: bool = True, max_col_width: int = 0, font: tuple[str, int]|None=None,
                 enable_events: bool=False, select_mode: str="browse", **kw) -> None:
        """Create a table."""
        super().__init__("Table", key, **kw)
        self.values = values
        self.headings = headings
        self.has_value = True
        self.enable_events = enable_events
        self.select_mode = select_mode
        self.justification: str = {"": "", "right": "e", "center": "center", "left": "w"}[justification]
        self.auto_size_columns = auto_size_columns
        self.max_col_width = max_col_width # todo
        self.font = font # todo
    
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
# Browse elements

class FileBrowse(Element):
    """FileBrowse element."""
    def __init__(self, button_text: str="...", key: str="", target_key: str|None=None,
            title: str="", file_types: tuple[tuple[str, str]]=(("All Files", "*.*"),),
            multiple_files: bool=False, initial_folder: str|None=None,
            save_as: bool=False, **kw) -> None:
        super().__init__("FileBrowse", key, **kw)
        self.has_value = False
        self.target_key = target_key
        self.title = title
        self.file_types = file_types
        self.save_as = save_as
        self.multiple_files = multiple_files
        self.initial_folder = initial_folder
        self.props["text"] = button_text
        self.bind_events({
            "<Button-1>": "click",
            "<Return>": "return",
        }, "system")

    def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
        self.widget = tk.Button(parent, **self.props)
        # hook
        win.register_event_hooks({
            self.key: [self.show_dialog]
        })
        return self.widget
    
    def _get_initial_directory(self) -> str:
        target: tk.Widget = self.get_prev_widget(self.target_key)
        # get initial directory
        init_dir = self.initial_folder
        if target is not None:
            target_text = target.get()
            if target_text != "":
                init_dir = os.path.dirname(target_text)
        return init_dir

    def show_dialog(self, *args) -> str|None:
        """Show file dialog"""
        target: tk.Widget = self.get_prev_widget(self.target_key)
        # get initial directory
        init_dir = self._get_initial_directory()
        # popup
        result = eg.popup_get_file(
            title=self.title,
            initial_folder=init_dir,
            save_as=self.save_as,
            file_types=self.file_types,
            multiple_files=self.multiple_files,
        )
        if isinstance(result, list) or isinstance(result, tuple):
            result = ";".join(result)
        if (target is not None) and (result is not None) and (result != ""):
            target.update(result)
        return result
    
    def set_text(self, text: str) -> None:
        """Set the text of the button."""
        self.props["text"] = text
        self.widget_update(text=text)

    def update(self, text: str|None=None, *args, **kw) -> None:
        """Update the widget."""
        if text is not None:
            self.set_text(text)
        super().update(*args, **kw)

class FilesBrowse(FileBrowse):
    """FilesBrowse element."""
    def __init__(self, button_text: str="...", key: str="", target_key: str|None=None,
            title: str="", file_types: tuple[tuple[str, str]]=(("All Files", "*.*"),), **kw) -> None:
        super().__init__("FilesBrowse", key, **kw)
        self.target_key = target_key
        self.title = title
        self.file_types = file_types
        self.props["text"] = button_text
        # force set params
        self.multiple_files = True
        self.save_as = False

class FileSaveAsBrowse(FileBrowse):
    """FileSaveAsBrowse element."""
    def __init__(self, button_text: str="...", key: str="", target_key: str|None=None,
            title: str="", file_types: tuple[tuple[str, str]]=(("All Files", "*.*"),), **kw) -> None:
        super().__init__("FileSaveAsBrowse", key, **kw)
        self.target_key = target_key
        self.title = title
        self.file_types = file_types
        self.props["text"] = button_text
        # force set params
        self.multiple_files = False
        self.save_as = True

class FileSaveAs(FileBrowse):
    """FileSaveAs element. (alias of FileSaveAsBrowse)"""
    pass

class FolderBrowse(FileBrowse):
    """FolderBrowse element."""
    def __init__(self, button_text: str="...", key: str="", target_key: str|None=None,
            default_path: str|None=None,
            title: str="", **kw) -> None:
        super().__init__("FolderBrowse", key, **kw)
        self.has_value = False
        self.target_key = target_key
        self.title = title
        self.default_path = default_path
        self.props["text"] = button_text
    
    def show_dialog(self, *args) -> str|None:
        """Show file dialog"""
        target: tk.Widget = self.get_prev_widget(self.target_key)
        # popup
        result = eg.popup_get_folder(
            title=self.title,
            default_path=self.default_path,
        )
        if (target is not None) and (result is not None) and (result != ""):
            target.update(result)
        return result

class ColorBrowse(FileBrowse):
    """FolderBrowse element."""
    def __init__(self, button_text: str="...", key: str="", target_key: str|None=None,
            default_color: str|None=None,
            title: str="", **kw) -> None:
        super().__init__("FolderBrowse", key, **kw)
        self.has_value = False
        self.target_key = target_key
        self.title = title
        self.default_color = default_color
        self.props["text"] = button_text
    
    def show_dialog(self, *args) -> str|None:
        """Show file dialog"""
        target: tk.Widget = self.get_prev_widget(self.target_key)
        # popup
        result = eg.popup_color(
            title=self.title,
            default_color=self.default_color,
        )
        if (target is not None) and (result is not None) and (result != ""):
            target.update(result)
        return result


#------------------------------------------------------------------------------
# Utility functions
#------------------------------------------------------------------------------

# global variables
# auto generate element key id
_element_key_ids: dict[str, int] = {}
_element_key_names: dict[str, bool] = {}
def generate_element_key(element_type: str) -> int:
    """Get a unique id for an element."""
    element_type = element_type.lower()
    if element_type not in _element_key_ids:
        _element_key_ids[element_type] = 0
    key: str = ""
    while True:
        _element_key_ids[element_type] += 1
        element_id = _element_key_ids[element_type]
        key = f"-{element_type}{element_id}-"
        if key not in _element_key_names:
            _element_key_names[key] = True
            break
    return key

def register_element_key(key: str) -> None:
    """Register element key."""
    _element_key_names[key] = True

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

def time_checker_start() -> datetime:
    return datetime.now()

def time_checker_end(start_time: datetime) -> int:
    elapsed_time = (datetime.now() - start_time).total_seconds()
    msec = int(elapsed_time * 1000)
    return msec
