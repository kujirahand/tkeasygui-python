#------------------------------------------------------------------------------
# TkEasyGUI locale
#------------------------------------------------------------------------------
import locale
from typing import Union

_locale: str = ""
# locale messages
_locale_messages: dict[str, dict[str, str]] = {
    "ja": {
        "__date_format__": "%Y-%m-%d",
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
        "Select date": "日付の選択",
        "Copy": "コピー",
        "Paste": "貼り付け",
        "Cut": "切り取り",
        "File": "ファイル",
        "Open": "開く",
        "Save": "保存",
        "Run": "実行",
        "Quit": "終了",
        "Thank you.": "ありがとうございます。",
    },
    "zh": {
        "__date_format__": "%Y年%m月%d日",
        "OK": "好",
        "Cancel": "取消",
        "Yes": "是",
        "No": "不",
        "Close": "关闭",
        "Information": "信息",
        "Warning": "警告",
        "Error": "错误",
        "Question": "问题",
        "Text input": "文本输入",
        "Select date": "选择日期",
        "Copy": "复制",
        "Paste": "粘贴",
        "Cut": "剪切",
        "File": "文件",
        "Open": "打开",
        "Save": "保存",
        "Run": "运行",
        "Quit": "退出",
        "Thank you.": "谢谢。",
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

