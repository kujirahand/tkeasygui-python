#------------------------------------------------------------------------------
# TkEasyGUI locale
#------------------------------------------------------------------------------
import locale
from typing import Any, Literal, TypeVar, Union

_locale: str = ""
# locale messages
_locale_messages: dict[str, dict[str, str]] = {
    "ja": {
        "OK": "OK",
        "Cancel": "キャンセル",
        "Yes": "はい",
        "No": "いいえ",
        "Close": "閉じる",
        "Information": "お知らせ",
        "Warning": "警告",
        "Error": "エラー",
        "Question": "質問",
        "Text Input": "テキスト入力",
    },
    "zh": {
        "OK": "好",
        "Cancel": "取消",
        "Yes": "是",
        "No": "不",
        "Close": "关闭",
        "Information": "信息",
        "Warning": "警告",
        "Error": "错误",
        "Question": "问题",
        "Text Input": "文本输入",
    },
}

def get_locale() -> str:
    """get locale"""
    global _locale
    if _locale == "":
        _locale = locale.getdefaultlocale()[0]
        if "_" in _locale:
            _locale = _locale.split("_")[0]
    return _locale

def set_locale(locale: str) -> None:
    """set locale"""
    global _locale
    _locale = locale

def get_text(key: str, default_text: Union[str, None]=None) -> str:
    """get locale text"""
    locale = get_locale()
    if locale in _locale_messages:
        if key in _locale_messages[locale]:
            return _locale_messages[locale][key]
    if default_text is not None:
        return default_text
    return key

def set_text(key: str, message: str, locale:str = "") -> None:
    """set locale text"""
    if locale == "":
        locale = get_locale()
        if locale not in _locale_messages:
            _locale_messages[locale] = {}
    _locale_messages[locale][key] = message

