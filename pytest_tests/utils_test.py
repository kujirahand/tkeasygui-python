"""Tests for TkEasyGUI/utils.py"""
import os
import platform

from TkEasyGUI import utils


def test_save_and_load_json_file(tmp_path):
    """Data saved with save_json_file should load back unchanged."""
    filename = str(tmp_path / "data.json")
    data = {"a": 1, "b": [1, 2, 3], "c": "テスト"}
    utils.save_json_file(filename, data)
    assert os.path.exists(filename)
    loaded = utils.load_json_file(filename)
    assert loaded == data


def test_load_json_file_missing_returns_default(tmp_path):
    """Missing file should return the given default_value."""
    filename = str(tmp_path / "missing.json")
    default_value = {"default": True}
    result = utils.load_json_file(filename, default_value)
    assert result == default_value


def test_load_json_file_missing_returns_none_by_default(tmp_path):
    """Missing file should return None when no default_value is given."""
    filename = str(tmp_path / "missing.json")
    assert utils.load_json_file(filename) is None


def test_save_text_file(tmp_path):
    """save_text_file should write the given text to the file."""
    filename = str(tmp_path / "text.txt")
    utils.save_text_file(filename, "hello")
    with open(filename, "r", encoding="utf-8") as f:
        assert f.read() == "hello"


def test_append_text_file(tmp_path):
    """append_text_file should add text to the end of an existing file."""
    filename = str(tmp_path / "text.txt")
    utils.save_text_file(filename, "hello")
    utils.append_text_file(filename, " world")
    with open(filename, "r", encoding="utf-8") as f:
        assert f.read() == "hello world"


def test_str_to_float():
    """str_to_float should parse valid strings and fall back on invalid ones."""
    assert utils.str_to_float("1.5") == 1.5
    assert utils.str_to_float("not a number", 9.9) == 9.9
    assert utils.str_to_float("not a number") == 0


def test_load_text_file(tmp_path):
    """load_text_file should read back the text written to a file."""
    filename = str(tmp_path / "text.txt")
    utils.save_text_file(filename, "hello world")
    assert utils.load_text_file(filename) == "hello world"


def test_load_text_file_missing_returns_default(tmp_path):
    """Missing file should return the given default_value."""
    filename = str(tmp_path / "missing.txt")
    assert utils.load_text_file(filename, default_value="fallback") == "fallback"


def test_get_platform():
    """get_platform should match platform.system()."""
    assert utils.get_platform() == platform.system()


def test_is_mac_and_is_win_are_mutually_exclusive():
    """is_mac and is_win should agree with get_platform and not both be true."""
    assert utils.is_mac() == (utils.get_platform() == "Darwin")
    assert utils.is_win() == (utils.get_platform() == "Windows")
    assert not (utils.is_mac() and utils.is_win())
