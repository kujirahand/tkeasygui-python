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
        def __init__(self, title, layout, size=None, icon=None):
            captured["title"] = title
            captured["layout"] = layout
            captured["size"] = size
            captured["icon"] = icon
            captured["closed"] = False

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


def test_popup_input_validation(monkeypatch):
    """Test validation in popup_input function."""
    captured = {}

    class FakeWindow:
        def __init__(self, title, layout, **kwargs):
            captured["layout"] = layout
            self.closed = False

        def is_alive(self):
            return not self.closed

        def read(self):
            # First try invalid value '123' then valid value 'abc'
            if "count" not in captured:
                captured["count"] = 1
                return "OK", {"-user-": "123", "event_type": "click"}
            else:
                self.closed = True
                return "OK", {"-user-": "abc", "event_type": "click"}

        def close(self):
            self.closed = True

    monkeypatch.setattr(widgets, "Window", FakeWindow)

    popups = []

    def fake_popup(msg, *args, **kwargs):
        popups.append(msg)

    monkeypatch.setattr(dialogs, "popup", fake_popup)

    res = dialogs.popup_input(
        "Enter text", validation=r"^[a-z]+$", validation_message="Only small letters"
    )

    assert res == "abc"
    assert len(popups) == 1
    assert popups[0] == "Only small letters"


def test_popup_input_only_number(monkeypatch):
    """Test only_number constraint in popup_input function."""
    captured = {}

    class FakeWindow:
        def __init__(self, title, layout, **kwargs):
            self.closed = False

        def is_alive(self):
            return not self.closed

        def read(self):
            # First try non-number 'abc' then number '123.45'
            if "count" not in captured:
                captured["count"] = 1
                return "OK", {"-user-": "abc", "event_type": "click"}
            else:
                self.closed = True
                return "OK", {"-user-": "123.45", "event_type": "click"}

        def close(self):
            self.closed = True

    monkeypatch.setattr(widgets, "Window", FakeWindow)

    popups = []

    def fake_popup(msg, *args, **kwargs):
        popups.append(msg)

    monkeypatch.setattr(dialogs, "popup", fake_popup)

    res = dialogs.popup_input("Enter number", only_number=True)

    assert res == 123.45
    assert len(popups) == 1


def test_popup_input_invalid_validation_pattern(monkeypatch):
    """Test that invalid regex patterns or invalid types in validation do not crash popup_input."""

    class FakeWindow:
        def __init__(self, title, layout, **kwargs):
            self.closed = False

        def is_alive(self):
            return not self.closed

        def read(self):
            self.closed = True
            return "OK", {"-user-": "any_value", "event_type": "click"}

        def close(self):
            self.closed = True

    monkeypatch.setattr(widgets, "Window", FakeWindow)

    # 1. Test invalid regex string
    res1 = dialogs.popup_input("Enter text", validation=r"[")
    assert res1 == "any_value"

    # 2. Test invalid type (e.g., integer)
    res2 = dialogs.popup_input("Enter text", validation=123)
    assert res2 == "any_value"
