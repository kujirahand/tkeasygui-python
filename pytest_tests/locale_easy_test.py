"""Tests for TkEasyGUI/locale_easy.py"""
import pytest

from TkEasyGUI import locale_easy


@pytest.fixture(autouse=True)
def restore_locale():
    """Save and restore the global locale state around each test."""
    original_locale = locale_easy._LOCALE
    original_messages = {
        lang: dict(messages) for lang, messages in locale_easy._locale_messages.items()
    }
    yield
    locale_easy._LOCALE = original_locale
    locale_easy._locale_messages.clear()
    locale_easy._locale_messages.update(original_messages)


def test_set_and_get_locale():
    """set_locale should make get_locale return the same value."""
    locale_easy.set_locale("ja")
    assert locale_easy.get_locale() == "ja"


def test_get_text_known_key():
    """get_text should return the translated message for a known key."""
    locale_easy.set_locale("ja")
    assert locale_easy.get_text("OK") == "OK"
    assert locale_easy.get_text("Cancel") == "キャンセル"


def test_get_text_unknown_key_returns_default():
    """get_text should return default_text when the key is missing."""
    locale_easy.set_locale("ja")
    assert locale_easy.get_text("__no_such_key__", "fallback") == "fallback"


def test_get_text_unknown_key_returns_key_when_no_default():
    """get_text should return the key itself when no default_text is given."""
    locale_easy.set_locale("ja")
    assert locale_easy.get_text("__no_such_key__") == "__no_such_key__"


def test_get_text_unknown_locale_returns_key():
    """get_text should return the key when the current locale has no messages."""
    locale_easy.set_locale("__no_such_locale__")
    assert locale_easy.get_text("OK") == "OK"


def test_set_text_adds_message_to_current_locale():
    """set_text with no locale_name should update the current locale's message."""
    locale_easy.set_locale("ja")
    locale_easy.set_text("Greeting", "こんにちは")
    assert locale_easy.get_text("Greeting") == "こんにちは"


def test_set_text_overrides_existing_message():
    """set_text should be able to override a pre-existing translation."""
    locale_easy.set_locale("ja")
    locale_easy.set_text("OK", "OKです")
    assert locale_easy.get_text("OK") == "OKです"
