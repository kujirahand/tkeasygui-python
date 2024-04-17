"""
TkEasyGUI utilities functions
"""

from typing import Literal, TypeVar, Union

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

def set_clipboard(text):
    """copy text to clipboard"""
    pyperclip.copy(text)

def get_clipboard():
    """get text from clipboard"""
    return pyperclip.paste()


