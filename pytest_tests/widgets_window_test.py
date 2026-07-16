"""Tests for TkEasyGUI/widgets_window.py"""
from TkEasyGUI import widgets_window as ww


def test_generate_element_id_increments():
    """generate_element_id should return an increasing sequence of ids."""
    first = ww.generate_element_id()
    second = ww.generate_element_id()
    assert second == first + 1


def test_generate_element_style_key_is_unique():
    """generate_element_style_key should never return the same key twice."""
    key1 = ww.generate_element_style_key("button")
    key2 = ww.generate_element_style_key("button")
    assert key1 != key2
    assert key1.startswith("-button")
    assert key2.startswith("-button")


def test_register_and_remove_element_key():
    """register_element_key should reject duplicates until the key is removed."""
    key = "-my-unique-test-key-"
    assert ww.register_element_key(key) is True
    assert ww.register_element_key(key) is False
    assert ww.remove_element_key(key) is True
    assert ww.remove_element_key(key) is False
    # once removed, the key can be registered again
    assert ww.register_element_key(key) is True
    ww.remove_element_key(key)


def test_get_root_window_returns_tk_root():
    """get_root_window should return the same singleton root window."""
    root1 = ww.get_root_window()
    root2 = ww.get_root_window()
    assert root1 is root2


def test_get_eg_window_count_starts_at_zero_or_more():
    """get_eg_window_count should return a non-negative integer."""
    assert ww.get_eg_window_count() >= 0
