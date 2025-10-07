"""TkEasyGUI utilities functions."""

import json
import os
import platform
import sys
from enum import Enum
from tkinter import font as tkinter_font
from tkinter import ttk
from typing import Any, Literal, Union

import pyperclip  # type: ignore
from PIL import Image as PILImage
from PIL import ImageGrab

from . import version as tkeasygui_version

# Import window management functions from widgets_window
from .widgets_window import (
    get_root_window,
    set_theme,
)

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


class TkEasyError(Exception):
    """TkEasyError Exception class."""

    def __init__(self, message="TkEasyError"):
        """Create a TkEasyError exception."""
        self.message = message
        super().__init__(self.message)


class ImageResizeType(Enum):
    """Image resize type."""

    NO_RESIZE = "no_resize"
    FIT_HEIGHT = "fit_height"
    FIT_WIDTH = "fit_width"
    FIT_BOTH = "fit_both"
    IGNORE_ASPECT_RATIO = "ignore_aspect_ratio"
    CROP_TO_SQUARE = "crop_to_square"


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


# ------------------------------------------------------------------------------
# theme
# ------------------------------------------------------------------------------
_tkeasygui_info: dict[str, Any] = {}


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


def get_tk_version() -> str:
    """Get tk version"""
    root = get_root_window()
    tkversion = root.tk.call("info", "patchlevel")
    return tkversion


def get_tcl_version() -> str:
    """Get tcl version"""
    root = get_root_window()
    tclversion = root.tk.call("info", "tclversion")
    return tclversion


def get_font_list() -> list[str]:
    """Get font list"""
    root = get_root_window()
    root.withdraw()
    return list(tkinter_font.families())


def get_system_info():
    """Get system info"""
    # node={platform.node()}
    py_ver = sys.version.replace("\n", "")
    return f"""
tkeasygui={tkeasygui_version.__version__}
python={py_ver}
tcl_tk={get_tk_version()}
os={platform.system()}
os_version={platform.version()}
os_release={platform.release()}
architecture={platform.architecture()}
processor={platform.processor()}
    """.strip()
