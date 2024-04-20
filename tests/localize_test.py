import TkEasyGUI as eg

# --- popup_yes_no は、自動でローカライズに対応している ---
# simple example
ans = eg.popup_yes_no("英語が話せますか?")
eg.print("答えは？ [", ans, "].\npopup_yes_noを使うと、OS言語が何語でも答えは[Yes]か[No]になります。")

# カスタマイズの例 - custom labels
ans = eg.popup_yes_no(
    "英語がは話せますか？",
    yes_label="話せる", no_label="話せない",
    yes_value="可", no_value="不可")
eg.print("答えは... [", ans, "]. 戻り値もカスタマイズできます。")
