"""Test popup yes/no dialog."""

import TkEasyGUI as eg

# simple
ans = eg.popup_yes_no("Can you speak Japanese?")
eg.popup_info(f"Your answer is `{ans}`.")

# set yes/no label
ans = eg.popup_yes_no(
    "Can you speak Japanese?",
    yes_label="Can",
    no_label="Can not",
    yes_value="Can",
    no_value="Can not",
)
eg.popup_info(f"Your answer is `{ans}`.")
