"""
TkEasyGUI utilities functions
"""

import platform
import sys
import tkinter as tk
from tkinter import ttk
from typing import Any, Literal, TypeVar, Union

import pyperclip

# define TypeAlias
Window = TypeVar("Window")
Element = TypeVar("Element")
TextAlign = Literal["left", "right", "center"]
TextVAlign = Literal["top", "bottom", "center"]
FontType = Union[tuple[str, int], tuple[str, int, str]]
PointType = Union[tuple[int, int], tuple[float, float]]
EventMode = Literal["user", "system"]
OrientationType = Literal["v", "h", "vertical", "horizontal"]
ListboxSelectMode = Literal["multiple", "browse", "extended", "single"]
PadType = Union[int, tuple[int, int], tuple[tuple[int, int], tuple[int, int]]]
ReliefType = Literal["flat", "groove", "raised", "ridge", "solid", "sunken"]

# -------------------------------------------------------------------
# clipboard
# -------------------------------------------------------------------
def set_clipboard(text):
    """copy text to clipboard"""
    pyperclip.copy(text)

def get_clipboard():
    """get text from clipboard"""
    return pyperclip.paste()

#------------------------------------------------------------------------------
# utility
def get_platform() -> str:
    """get platform"""
    return platform.system()

def is_mac() -> bool:
    """platform : is mac?"""
    return get_platform() == "Darwin"

def is_win() -> bool:
    """platform : is Windows?"""
    return get_platform() == "Windows"

# -------------------------------------------------------------------
# tkinter window management
# -------------------------------------------------------------------
# only one root element
_root_window: Union[tk.Tk, None] = None
_ttk_style: Union[ttk.Style, None] = None
tkversion: str = "0.0.0"
def get_root_window() -> tk.Tk:
    """Get root window."""
    global _root_window
    global tkversion
    if _root_window is None:
        _root_window = tk.Tk()
        _root_window.attributes('-alpha', 0)
        _root_window.eval('tk::PlaceWindow . center')
        _root_window.withdraw()
        # set theme
        try:
            if "theme" in _tkeasygui_info:
                name = _tkeasygui_info["theme"]
                _ttk_style = get_ttk_style()
                _ttk_style.theme_use(name)
            else:
                set_default_theme()
        except Exception as e:
            print(f"TkEasyGUI.theme: failed to set theme {name} {e}", file=sys.stderr)
            pass
    return _root_window


# Prioritize compatibility with PySimpleGUI
_compatibility: bool = True
def set_PySimpleGUI_compatibility(flag: bool=True) -> None:
    """Set compatibility with PySimpleGUI (Default=True)"""
    global _compatibility
    _compatibility = flag

def get_ttk_style() -> ttk.Style:
    """Get ttk style"""
    global _ttk_style
    if _ttk_style is None:
        _ttk_style = ttk.Style()
    return _ttk_style

# active window
_window_list: list[Window] = []
def _get_active_window() -> Union[tk.Toplevel, None]:
    """Get the active window."""
    if len(_window_list) == 0:
        return None
    return _window_list[-1].window

def _window_parent() -> Union[Window, None]:
    """Get the parent window."""
    if len(_window_list) == 0:
        return None
    return _window_list[-1]

def _window_count() -> int:
    """Get the number of windows."""
    return len(_window_list)

def _window_push(win: Window) -> None:
    """Push a window to the list."""
    _window_list.append(win)

def _window_pop(win: Window) -> None:
    """Pop a window from the list."""
    i = _window_list.index(win)
    if i >= 0:
        _window_list.pop()

#------------------------------------------------------------------------------
# theme
_tkeasygui_info: dict[str, Any] = {}

def set_theme(name: str) -> None:
    """Change look and feel --- [TODO] Currently, the implementation is incomplete."""
    win = get_root_window()
    win.withdraw()
    style = get_ttk_style()
    style.theme_use(name)
    _tkeasygui_info["theme"] = name

def get_tnemes() -> list[str]:
    """
    Get theme list
    ```py
    print(get_themes())
    ```
    """
    win = get_root_window()
    win.withdraw()
    return ttk.Style().theme_names()

def theme(name: str) -> None:
    """Set theme (alias of set_theme)"""
    set_theme(name)

def get_current_theme() -> str:
    """Get current theme"""
    return _tkeasygui_info.get("theme", "")

def set_default_theme() -> None:
    """
    Set default theme
    ```py
    print(get_themes())
    ```
    """
    if is_mac():
        # ('aqua', 'clam', 'alt', 'default', 'classic')
        set_theme("aqua")
    elif is_win():
        # ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        # set_theme("winnative")
        # set_theme("default")
        set_theme("vista")
    else:
        set_theme("clam")

def convert_color_rgb16(color_name: str) -> tuple[int, int, int]:
    """Convert color to RGB, return (r, g, b) tuple. range=0-65535"""
    root = get_root_window()
    return root.winfo_rgb(color_name)

def convert_color_html(color_name: str) -> str:
    """Convert RGB color(16bit tuple) to HTML color name."""
    r, g, b = convert_color_rgb16(color_name)
    return f"#{r//256:02x}{g//256:02x}{b//256:02x}"

#------------------------------------------------------------------------------
# Utility functions
#------------------------------------------------------------------------------
# global variables
# auto generate element key id
_element_style_key_ids: dict[str, int] = {}
_element_key_names: dict[str, bool] = {}
def generate_element_style_key(element_type: str) -> int:
    """Get a unique id for an element."""
    element_type = element_type.lower()
    if element_type not in _element_style_key_ids:
        _element_style_key_ids[element_type] = 0
    key: str = ""
    while True:
        _element_style_key_ids[element_type] += 1
        element_id = _element_style_key_ids[element_type]
        key = f"-{element_type}{element_id}-"
        if key not in _element_key_names:
            _element_key_names[key] = True
            break
    return key

def register_element_key(key: str) -> bool:
    """Register element key."""
    if key in _element_key_names:
        return False
    _element_key_names[key] = True
    return True

_elements_with_value: int = 0
def generate_element_id() -> int:
    """Generate a unique id for a value element."""
    global _elements_with_value
    element_id = _elements_with_value
    _elements_with_value += 1
    return element_id

