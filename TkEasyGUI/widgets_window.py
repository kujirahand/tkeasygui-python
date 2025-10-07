"""TkEasyGUI Window management functions."""

import platform
import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING, Optional, Union

# Forward declaration for Window class to avoid circular imports
if TYPE_CHECKING:
    from .widgets import Window

# Type alias
KeyType = Union[str, int]


# Platform check functions (minimal implementation needed here)
def _is_mac() -> bool:
    """Check if platform is macOS."""
    return platform.system() == "Darwin"


def _is_win() -> bool:
    """Check if platform is Windows."""
    return platform.system() == "Windows"


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
            if _is_mac():
                self.set_theme("aqua")
            elif _is_win():
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
# Global window manager instance
# ------------------------------------------------------------------------------
# pylint: disable=global-statement
EG_WINDOW_MANAGER: TkWindowManager = TkWindowManager()

# TkEasyGUI's active window
EG_WINDOW_LIST: list["Window"] = []


# ------------------------------------------------------------------------------
# Utility functions for compatibility
# ------------------------------------------------------------------------------
def get_root_window() -> tk.Tk:
    """Get root window."""
    return EG_WINDOW_MANAGER.get_root()


def set_pysimplegui_compatibility(flag: bool = True) -> None:
    """Set compatibility with PySimpleGUI (Default=True)"""
    EG_WINDOW_MANAGER.set_sg_compatibility(flag)


def get_ttk_style() -> ttk.Style:
    """Get ttk style"""
    return EG_WINDOW_MANAGER.get_tkk_style()


def set_theme(name: str) -> None:
    """
    Change look and feel

    - macOS --- ('aqua', 'clam', 'alt', 'default', 'classic')
    - Windows --- ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
    - Linux --- ('clam', 'alt', 'default', 'classic')
    """
    EG_WINDOW_MANAGER.set_theme(name)


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


def get_active_eg_window() -> Union[tk.Toplevel, None]:
    """Get the active window."""
    if len(EG_WINDOW_LIST) == 0:
        return None
    return EG_WINDOW_LIST[-1].window


def get_last_eg_window() -> Union["Window", None]:
    """Get the parent window."""
    if len(EG_WINDOW_LIST) == 0:
        return None
    return EG_WINDOW_LIST[-1]


def get_eg_window_count() -> int:
    """Get the number of windows."""
    return len(EG_WINDOW_LIST)


def push_easy_window(win: "Window") -> None:
    """Push a window to the list."""
    EG_WINDOW_LIST.append(win)


def pop_easy_window(win: "Window") -> None:
    """Pop a window from the list."""
    i = EG_WINDOW_LIST.index(win)
    if i >= 0:
        EG_WINDOW_LIST.pop()
