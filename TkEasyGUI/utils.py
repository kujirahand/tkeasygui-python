"""TkEasyGUI utilities functions."""

import json
import os
import platform
import tkinter as tk
from tkinter import ttk
from typing import Any, Literal, Optional, Union

import pyperclip  # type: ignore
from PIL import Image as PILImage
from PIL import ImageGrab

# define TypeAlias
TextAlign = Literal["left", "right", "center"]
TextVAlign = Literal["top", "bottom", "center"]
FontType = Union[tuple[str, int], tuple[str, int, str]]
PointType = Union[tuple[int, int], tuple[float, float]]
EventMode = Literal["user", "system"]
OrientationType = Literal["v", "h", "vertical", "horizontal"]
ProgressbarMode = Literal["determinate", "indeterminate"]
ListboxSelectMode = Literal["multiple", "browse", "extended", "single"]
PadType = Union[int, tuple[int, int], tuple[tuple[int, int], tuple[int, int]]]
ReliefType = Literal["flat", "groove", "raised", "ridge", "solid", "sunken"]
KeyType = Union[str, int]
ColorFormatType = Literal["html", "rgb", "tuple"]
CursorType = Literal[
    "arrow",
    "circle",
    "cross",
    "dotbox",
    "exchange",
    "fleur",
    "hand1",
    "hand2",
    "heart",
    "man",
    "mouse",
    "pirate",
    "plus",
    "shuttle",
    "sizing",
    "spider",
    "spraycan",
    "star",
    "target",
    "tcross",
    "trek",
    "watch",
    "xterm",
    "ibeam",
    "wait",
    "size",
    "size_all",
    "size_nw_se",
    "size_ne_sw",
    "size_we",
    "size_ns",
]
ElementJustifcation = Literal["left", "center", "right", "c", "r"]
PopupGetFormItemType = Union[
    str,
    tuple[str, Any],
    tuple[str, Any, str],
]
FileTypeList = list[tuple[str, str]]


# -------------------------------------------------------------------
# clipboard
# -------------------------------------------------------------------
def set_clipboard(text):
    """Copy text to clipboard"""
    pyperclip.copy(text)


def get_clipboard():
    """Get text from clipboard"""
    return pyperclip.paste()


def copy_to_clipboard(text):
    """Copy text to clipboard"""
    set_clipboard(text)


def paste_from_clipboard():
    """Get text from clipboard"""
    return get_clipboard()


# ------------------------------------------------------------------------------
# platform utility
# ------------------------------------------------------------------------------
def get_platform() -> str:
    """Get platform"""
    return platform.system()


def is_mac() -> bool:
    """Platform : is mac?"""
    return get_platform() == "Darwin"


def is_win() -> bool:
    """Platform : is Windows?"""
    return get_platform() == "Windows"


def screenshot() -> PILImage.Image:
    """Take a screenshot."""
    screen_image = ImageGrab.grab()
    return screen_image


def get_screen_size() -> tuple[int, int]:
    """Get screen size."""
    root = get_root_window()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    return width, height


def get_screen_dpi() -> int:
    """Get screen DPI."""
    root = get_root_window()
    dpi = root.winfo_fpixels("1i")
    return int(dpi)


def get_scaling() -> float:
    """Get scaling factor."""
    root = get_root_window()
    scaling = root.tk.call("tk", "scaling")
    return float(scaling)


# ------------------------------------------------------------------------------
# text file utility
# ------------------------------------------------------------------------------
def load_text_file(
    filename: str, encoding: str = "utf-8", default_value: str = ""
) -> str:
    """Load text file."""
    if os.path.exists(filename):
        with open(filename, "r", encoding=encoding) as f:
            text = f.read()
        return text
    return default_value


def save_text_file(filename: str, text: str, encoding: str = "utf-8") -> None:
    """Save text file."""
    with open(filename, "w", encoding=encoding) as f:
        f.write(text)


def append_text_file(filename: str, text: str, encoding: str = "utf-8") -> None:
    """Append text file."""
    with open(filename, "a", encoding=encoding) as f:
        f.write(text)


def load_json_file(filename: str, default_value: Any = None) -> Any:
    """Load JSON file."""
    if os.path.exists(filename) is False:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    return default_value


def save_json_file(filename: str, data: Any) -> None:
    """Save JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# -------------------------------------------------------------------
# other utilities
# -------------------------------------------------------------------
def str_to_float(value: str, default_value: float = 0) -> float:
    """Convert string to float."""
    try:
        return float(value)
    except ValueError:
        return default_value


# -------------------------------------------------------------------
# tkinter window management
# -------------------------------------------------------------------
# pylint: disable=too-many-instance-attributes,too-few-public-methods
class TkWindowManager:
    """Manage tkinter root window."""

    def __init__(self):
        """Initialize TkWindowManager."""
        self._root: Optional[tk.Tk] = None
        self._style: Optional[ttk.Style] = None
        self._tk_version: str = "0.0.0"
        self._sg_compat_mode: bool = False
        self._theme_name: str = ""
        self._element_id_last: int = 0
        self._element_style_key_ids: dict[KeyType, int] = {}
        self._element_key_names: dict[KeyType, bool] = {}
        # initialize root window
        self._create_root()

    def _create_root(self) -> tk.Tk:
        """Create root window if not exists."""
        if self._root is None or not self._root.winfo_exists():
            self._root = tk.Tk()
            self._root.attributes("-alpha", 0)
            self._root.eval("tk::PlaceWindow . center")
            self._root.withdraw()
        if self._theme_name == "":
            if is_mac():
                self.set_theme("aqua")
            elif is_win():
                self.set_theme("vista")
            else:
                self.set_theme("clam")
        return self._root

    def get_root(self) -> tk.Tk:
        """Get root window."""
        if self._root is None:
            return self._create_root()
        return self._root

    def get_tk_version(self) -> str:
        """Get tkinter version."""
        if self._tk_version == "0.0.0":
            self._tk_version = self.get_root().tk.call("info", "patchlevel")
        return self._tk_version

    def destroy_root(self) -> None:
        """Destroy root window."""
        if self._root is not None:
            self._root.destroy()
            self._root = None

    def set_sg_compatibility(self, flag: bool = True) -> None:
        """Set compatibility with PySimpleGUI (Default=True)"""
        self._sg_compat_mode = flag

    def get_sg_compatibility(self) -> bool:
        """Get compatibility with PySimpleGUI"""
        return self._sg_compat_mode

    def get_tkk_style(self) -> ttk.Style:
        """Get ttk style"""
        if self._style is None:
            self._style = ttk.Style(self.get_root())
        return self._style

    def set_tkk_style(self, style: ttk.Style) -> None:
        """Set ttk style"""
        self._style = style
        if self._root is not None:
            self._style.master = self._root

    def set_theme(self, name: str) -> None:
        """Set theme for ttk style"""
        root = self.get_root()
        root.withdraw()
        style = self.get_tkk_style()
        style.theme_use(name)
        self._theme_name = name

    def get_theme(self) -> str:
        """Get current theme name"""
        return self._theme_name

    def generate_element_id(self) -> int:
        """Generate a unique id for an element."""
        self._element_id_last += 1
        return self._element_id_last

    def generate_element_style_key(self, element_type: str) -> str:
        """Get a unique id for an element."""
        element_type = element_type.lower()
        if element_type not in self._element_style_key_ids:
            self._element_style_key_ids[element_type] = 0
        key: KeyType = ""
        while True:
            self._element_style_key_ids[element_type] += 1
            element_id = self._element_style_key_ids[element_type]
            key = f"-{element_type}{element_id}-"
            if key not in self._element_key_names:
                self._element_key_names[key] = True
                break
        return key

    def register_element_key(self, key: KeyType) -> bool:
        """Register element key."""
        if key in self._element_key_names:
            return False
        self._element_key_names[key] = True
        return True

    def remove_element_key(self, key: KeyType) -> bool:
        """Remove element key."""
        if key in self._element_key_names:
            self._element_key_names.pop(key)
            return True
        return False


# ------------------------------------------------------------------------------
# only one root element
# ------------------------------------------------------------------------------
# pylint: disable=global-statement
EG_WINDOW_MANAGER: TkWindowManager = TkWindowManager()


def get_root_window() -> tk.Tk:
    """Get root window."""
    return EG_WINDOW_MANAGER.get_root()


def set_pysimplegui_compatibility(flag: bool = True) -> None:
    """Set compatibility with PySimpleGUI (Default=True)"""
    EG_WINDOW_MANAGER.set_sg_compatibility(flag)


def get_ttk_style() -> ttk.Style:
    """Get ttk style"""
    return EG_WINDOW_MANAGER.get_tkk_style()


# ------------------------------------------------------------------------------
# theme
_tkeasygui_info: dict[str, Any] = {}


def set_theme(name: str) -> None:
    """
    Change look and feel

    - macOS --- ('aqua', 'clam', 'alt', 'default', 'classic')
    - Windows --- ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
    - Linux --- ('clam', 'alt', 'default', 'classic')
    """
    EG_WINDOW_MANAGER.set_theme(name)


def get_tnemes() -> tuple[str, ...]:
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


# ------------------------------------------------------------------------------
# Utility functions
# ------------------------------------------------------------------------------
def generate_element_style_key(element_type: str) -> str:
    """Get a unique id for an element."""
    return EG_WINDOW_MANAGER.generate_element_style_key(element_type)


def register_element_key(key: KeyType) -> bool:
    """Register element key."""
    return EG_WINDOW_MANAGER.register_element_key(key)


def remove_element_key(key: KeyType) -> bool:
    """Remove element key."""
    return EG_WINDOW_MANAGER.remove_element_key(key)


def generate_element_id() -> int:
    """Generate a unique id for a value element."""
    return EG_WINDOW_MANAGER.generate_element_id()
