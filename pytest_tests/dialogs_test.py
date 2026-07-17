"""Tests for dialog layout helpers."""

import tkinter as tk

import pytest

try:
    import TkEasyGUI.dialogs as dialogs
    from TkEasyGUI import widgets
except tk.TclError:
    pytest.skip("Tk is not available (no display).", allow_module_level=True)


def test_popup_get_form_displays_fourth_item_as_hint(monkeypatch):
    """A fourth form-item value is rendered as help text beside the input."""
    captured = {}

    class FakeWindow:
        def __init__(self, title, layout, size, icon):
            captured["layout"] = layout

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return False

        def event_iter(self):
            return iter(())

    monkeypatch.setattr(widgets, "Window", FakeWindow)

    assert dialogs.popup_get_form([("Name", "", "text", "Enter your name")]) is None

    hint = captured["layout"][0][-1]
    assert isinstance(hint, widgets.Text)
    assert hint.props["text"] == "Enter your name"
