"""Tests for pure helper functions in TkEasyGUI/widgets.py"""
import tkinter as tk
from unittest.mock import Mock

import pytest

try:
    from TkEasyGUI.widgets import (
        Element,
        Push,
        TabGroup,
        Text,
        VPush,
        align_center,
        align_left,
        align_right,
        rgb,
        valign_bottom,
        valign_middle,
        valign_top,
    )
except tk.TclError:
    pytest.skip("Tk is not available (no display).", allow_module_level=True)


def test_rgb():
    """The rgb function should format RGB values as a lowercase hex color string."""
    assert rgb(0, 0, 0) == "#000000"
    assert rgb(255, 255, 255) == "#ffffff"
    assert rgb(18, 52, 86) == "#123456"


def test_rgb_masks_out_of_range_values():
    """The rgb function should mask each channel to a single byte (0-255)."""
    assert rgb(256, -1, 511) == rgb(0, 255, 255)


def test_align_left_returns_parts_unchanged():
    """align_left should not add any padding elements."""
    parts: list[Element] = [Text("a"), Text("b")]
    assert align_left(parts) == parts


def test_align_right_prepends_push():
    """align_right should prepend a single Push element."""
    parts: list[Element] = [Text("a")]
    result = align_right(parts)
    assert len(result) == 2
    assert isinstance(result[0], Push)
    assert result[1] is parts[0]


def test_align_center_wraps_with_push():
    """align_center should surround the parts with Push elements on both sides."""
    parts: list[Element] = [Text("a")]
    result = align_center(parts)
    assert len(result) == 3
    assert isinstance(result[0], Push)
    assert result[1] is parts[0]
    assert isinstance(result[2], Push)


def test_align_functions_with_empty_list():
    """align_center/align_right should return an empty list when given no parts."""
    empty: list[Element] = []
    assert align_center(empty) == []
    assert align_right(empty) == []
    assert align_left(empty) == []


def test_valign_top_returns_grid_unchanged():
    """valign_top should not add any padding rows."""
    grid: list[list[Element]] = [[Text("a")]]
    assert valign_top(grid) is grid


def test_valign_middle_wraps_with_vpush_rows():
    """valign_middle should add a VPush row above and below the grid."""
    grid: list[list[Element]] = [[Text("a")]]
    result = valign_middle(grid)
    assert len(result) == 3
    assert isinstance(result[0][0], VPush)
    assert result[1] is grid[0]
    assert isinstance(result[2][0], VPush)


def test_valign_bottom_prepends_vpush_row():
    """valign_bottom should add a single VPush row above the grid."""
    grid: list[list[Element]] = [[Text("a")]]
    result = valign_bottom(grid)
    assert len(result) == 2
    assert isinstance(result[0][0], VPush)
    assert result[1] is grid[0]


def test_valign_functions_with_empty_grid():
    """valign_middle/valign_bottom should return an empty list when given no rows."""
    empty_grid: list[list[Element]] = []
    assert valign_middle(empty_grid) == []
    assert valign_bottom(empty_grid) == []


def test_tabgroup_configures_japanese_tab_style_on_windows(monkeypatch):
    """TabGroup should avoid Windows focus lines overlapping Japanese labels."""
    from TkEasyGUI import widgets

    style = Mock()
    notebook = Mock()
    monkeypatch.setattr(widgets.utils, "is_win", lambda: True)
    monkeypatch.setattr(widgets, "get_ttk_style", lambda: style)
    monkeypatch.setattr(widgets.ttk, "Notebook", lambda parent, **kw: notebook)

    parent_window = Mock(font=("Noto Sans", 11))
    tab_group = TabGroup([])
    assert tab_group.create(parent_window, Mock()) is notebook
    style.configure.assert_called_once_with(
        "TkEasyGUI.TNotebook.Tab", font=("Noto Sans", 11), padding=(8, 8)
    )
    assert tab_group.props["style"] == "TkEasyGUI.TNotebook"


def test_tabgroup_keeps_non_windows_tab_style_unchanged(monkeypatch):
    """TabGroup should not override the native tab style off Windows."""
    from TkEasyGUI import widgets

    style = Mock()
    notebook = Mock()
    monkeypatch.setattr(widgets.utils, "is_win", lambda: False)
    monkeypatch.setattr(widgets, "get_ttk_style", lambda: style)
    monkeypatch.setattr(widgets.ttk, "Notebook", lambda parent, **kw: notebook)

    tab_group = TabGroup([])
    assert tab_group.create(Mock(font=None), Mock()) is notebook
    style.configure.assert_not_called()


def test_tabgroup_respects_explicit_notebook_style_on_windows(monkeypatch):
    """A caller-provided Notebook style should not be overridden on Windows."""
    from TkEasyGUI import widgets

    style = Mock()
    notebook = Mock()
    monkeypatch.setattr(widgets.utils, "is_win", lambda: True)
    monkeypatch.setattr(widgets, "get_ttk_style", lambda: style)
    monkeypatch.setattr(widgets.ttk, "Notebook", lambda parent, **kw: notebook)

    tab_group = TabGroup([], style="Custom.TNotebook")
    assert tab_group.create(Mock(font=("Noto Sans", 11)), Mock()) is notebook
    style.configure.assert_not_called()
    assert tab_group.props["style"] == "Custom.TNotebook"


def test_tabgroup_keeps_ttk_default_font_without_window_font(monkeypatch):
    """An unspecified Window font should keep the locale-specific ttk default."""
    from TkEasyGUI import widgets

    style = Mock()
    notebook = Mock()
    monkeypatch.setattr(widgets.utils, "is_win", lambda: True)
    monkeypatch.setattr(widgets, "get_ttk_style", lambda: style)
    monkeypatch.setattr(widgets.ttk, "Notebook", lambda parent, **kw: notebook)

    tab_group = TabGroup([])
    assert tab_group.create(Mock(font=None), Mock()) is notebook
    style.configure.assert_called_once_with("TkEasyGUI.TNotebook.Tab", padding=(8, 8))


def test_input_validation_patterns():
    """Test that widgets.Input handles various validation arguments safely."""
    import re
    from TkEasyGUI.widgets import Input

    # 1. Valid regex string
    inp1 = Input(validation=r"^\d+$")
    assert inp1._validation_pattern is not None
    assert inp1._validation_pattern.pattern == r"^\d+$"

    # 2. Pre-compiled regex object
    pat = re.compile(r"^[a-z]+$")
    inp2 = Input(validation=pat)
    assert inp2._validation_pattern is pat

    # 3. Invalid regex string
    inp3 = Input(validation=r"[")
    assert inp3._validation_pattern is None

    # 4. Invalid type (e.g. dict or list)
    inp4 = Input(validation={"key": "val"})
    assert inp4._validation_pattern is None

