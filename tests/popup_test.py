# import PySimpleGUI as sg
import TkEasyGUI as eg


def main():
    while True:
        # select buttons
        group = eg.popup_listbox(
            values=[
                "Basic",
                "Notify",
                "Input Text",
                "Select File",
                "Calendar",
                "Others",
            ],
            message="Please select popup group:")
        if group is None:
            break
        else:
            popup_test(group)

def popup_test(group):
    if group == "Basic":
        # Display message in a dialog
        eg.popup("[1] popup")
        # Dialog with OK button
        eg.popup_ok("[2] popup_ok")
        # Dialog with OK/Cancel buttons
        r = eg.popup_ok_cancel("[3] popup_ok_cancel")
        if r == "Cancel":
            return
        # Dialog with YES/No buttons
        print(eg.popup_yes_no("[4] popup_yes_no"))
        # Dialog with Cancelled button
        eg.popup_cancel("[5] popup_cancel")
        # Dialog with Error button
        eg.popup_error("[6] popup_error")
        # Dialog without buttons
        eg.popup_no_buttons("[7]popup_no_buttons")
    if group == "Notify":
        # Display information in notification area
        eg.popup_notify("[1] popup_notify")
        # Automatically close in 3 seconds
        print(eg.popup_auto_close("[2] popup_auto_close - 3sec", auto_close_duration=3))
        # Dialog without waiting
        # sg.popup_no_wait("[3] popup_no_wait")
    if group == "Input Text":
        # Text input dialog
        print(eg.popup_get_text("[1] popup_get_text"))
        # Text input dialog with custom font
        print(eg.popup_get_text("[2] popup_get_text", font=("Arial", 20)))
        # Multi-line input box
        print(eg.popup_scrolled("[3] popup_scrolled"))
    if group == "Select File":
        # File selection dialog
        print(eg.popup_get_file("[1] popup_get_file"))
        # Folder selection dialog
        print(eg.popup_get_folder("[2] popup_get_folder"))
    if group == "Calendar":
        # Return a calendar
        print(eg.popup_get_date("[1] popup_get_date"))
    if group == "Others":
        # --- Below are TkEasyGUI only functionalities ---
        # Color selection dialog
        print(eg.popup_color("[1] popup_color"))
        # Dialog with custom buttons
        print(eg.popup_buttons("[2] popup_buttons", buttons=["Apple", "Banana", "Orange"]))

if __name__ == "__main__":
    main()

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
# カレンダーを返す
print(sg.popup_get_date("[15] popup_get_date"))

# --- 以下はTkEasyGUIのみの機能 ---
# 色選択ダイアログ
print(sg.popup_color("[30] popup_color"))
# 任意のボタンを持つダイアログ
print(sg.popup_buttons("[31] popup_buttons", buttons=["Apple","Banana","Orange"]))
"""
