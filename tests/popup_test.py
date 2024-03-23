# import PySimpleGUI as sg
import tkeasygui as sg

# Display message in a dialog
sg.popup("[1] popup")
# Dialog with OK button
sg.popup_ok("[2] popup_ok")
# Dialog with OK/Cancel buttons
print(sg.popup_ok_cancel("[3] popup_ok_cancel"))
# Dialog with YES/No buttons
print(sg.popup_yes_no("[4] popup_yes_no"))
# Dialog with Cancelled button
sg.popup_cancel("[5] popup_cancel")
# Dialog with Error button
sg.popup_error("[6] popup_error")
# Dialog without waiting
sg.popup_no_wait("[7] popup_no_wait")
# Automatically close in 3 seconds
print(sg.popup_auto_close("[8] popup_auto_close", auto_close_duration=3))
# Dialog without buttons
sg.popup_no_buttons("[9]popup_no_buttons")
# Text input dialog
print(sg.popup_get_text("[10] popup_get_text"))
# Text input dialog with custom font
print(sg.popup_get_text("[10] popup_get_text", font=("Arial", 20)))
# Display information in notification area
sg.popup_notify("[11] popup_notify")
# File selection dialog
print(sg.popup_get_file("[12] popup_get_file"))
# Folder selection dialog
print(sg.popup_get_folder("[13] popup_get_folder"))
# Multi-line input box
print(sg.popup_scrolled("[14] popup_scrolled"))
# --- Below are TkEasyGUI only functionalities ---
# Color selection dialog
print(sg.popup_color("[15] popup_color"))
# Dialog with custom buttons
print(sg.popup_buttons("[16] popup_buttons", buttons=["Apple", "Banana", "Orange"]))
# Return a calendar
print(sg.popup_get_date("[17] popup_get_date"))

"""
# メッセージをダイアログに表示する
sg.popup("[1] popup")
# OKボタンを持ったダイアログ
sg.popup_ok("[2] popup_ok")
# OK/Cancelボタンを持つダイアログ
print(sg.popup_ok_cancel("[3] popup_ok_cancel"))
# YES/Noボタンを持つダイアログ
print(sg.popup_yes_no("[4] popup_yes_no"))
# Cancelledボタンを持つダイアログ
sg.popup_cancel("[5] popup_cancel")
# Errorボタンを持つダイアログ
sg.popup_error("[6] popup_error")
# 待ち時間のないダイアログ
sg.popup_no_wait("[7] popup_no_wait")
# 3秒で自動的に閉じる
print(sg.popup_auto_close("[8] popup_auto_close", auto_close_duration=3))
# ボタンのないダイアログ
sg.popup_no_buttons("[9]popup_no_buttons")
# テキスト入力ダイアログ
print(sg.popup_get_text("[10] popup_get_text"))
# テキスト入力ダイアログ
print(sg.popup_get_text("[10] popup_get_text",font=("Arial", 20)))
# 通知領域に情報を表示する
sg.popup_notify("[11] popup_notify")
# ファイル選択ダイアログ
print(sg.popup_get_file("[12] popup_get_file"))
# フォルダ選択ダイアログ
print(sg.popup_get_folder("[13] popup_get_folder"))
# 複数行入力ボックス
print(sg.popup_scrolled("[14] popup_scrolled"))
# --- 以下はTkEasyGUIのみの機能 ---
# 色選択ダイアログ
print(sg.popup_color("[15] popup_color"))
# 任意のボタンを持つダイアログ
print(sg.popup_buttons("[16] popup_buttons", buttons=["Apple","Banana","Orange"]))
# カレンダーを返す
print(sg.popup_get_date("[17] popup_get_date"))
"""
