"""TkEasyGUI locale module"""

import locale
import os
from typing import Union

# locale
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
        "Text input": "テキスト入力",
        "Number input": "数値入力",
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
        "Please enter a number.": "数値を入力してください。",
        "Copy Message": "メッセージをコピー",
        "Validation error": "入力エラーです。正しい形式で入力してください。",
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
        "Number input": "数字输入",
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
        "Please enter a number.": "请输入一个数字。",
        "Copy Message": "复制消息",
        "Validation error": "输入错误。请以正确的格式输入。",
    },
    "ko": {
        "__date_format__": "%Y-%m-%d",
        "OK": "확인",
        "Cancel": "취소",
        "Yes": "예",
        "No": "아니요",
        "Close": "닫기",
        "Information": "정보",
        "Warning": "경고",
        "Error": "오류",
        "Question": "질문",
        "Text input": "텍스트 입력",
        "Number input": "숫자 입력",
        "Select date": "날짜 선택",
        "Copy": "복사",
        "Paste": "붙여넣기",
        "Cut": "잘라내기",
        "File": "파일",
        "Open": "열기",
        "Save": "저장",
        "Run": "실행",
        "Quit": "종료",
        "Thank you.": "감사합니다.",
        "Please enter a number.": "숫자를 입력하세요.",
        "Copy Message": "메시지 복사",
        "Validation error": "입력 오류입니다. 올바른 형식으로 입력하세요.",
    },
}


def get_locale() -> str:
    """Get locale"""
    global _locale  # pylint: disable=global-statement
    if _locale == "":
        def_locale = locale.getlocale() or (os.environ.get("LANG", "C"), "UTF-8")
        if len(def_locale) >= 1:
            _locale = def_locale[0] if def_locale[0] is not None else "en"
            if "_" in _locale:
                _locale = _locale.split("_")[0]
    return _locale


def set_locale(locale_name: str) -> None:
    """Set locale"""
    global _locale  # pylint: disable=global-statement
    _locale = locale_name


def get_text(key: str, default_text: Union[str, None] = None) -> str:
    """Get locale text"""
    current_locale = get_locale()
    if current_locale in _locale_messages:
        if key in _locale_messages[current_locale]:
            return _locale_messages[current_locale][key]
    if default_text is not None:
        return default_text
    return key


def set_text(key: str, message: str, locale_name: str = "") -> None:
    """Set locale text"""
    if locale_name == "":
        locale_name = get_locale()
        if locale_name not in _locale_messages:
            _locale_messages[locale_name] = {}
    _locale_messages[locale_name][key] = message
