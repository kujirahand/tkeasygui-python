"""
### ListBrowse test

This is a test for the ListBrowse and MultilineBrowse widgets.
ListBrowse is a button that opens a window with a list of items.
MultilineBrowse is a button that opens a window with a multiline text.
"""

import json

import TkEasyGUI as eg

window = eg.Window(
    "ListBrowse test",
    layout=[
        [eg.Text("ListBrowse:")],
        [
            eg.Input("", expand_x=True, key="-list-result-"),
            eg.ListBrowse(values=["red", "green", "blue"]),
        ],
        [eg.Text("MultilineBrowse:")],
        [
            eg.Input("", expand_x=True, key="-text-result-"),
            eg.MultilineBrowse("This is a pen."),
        ],
        [eg.HSeparator()],
        [eg.Button("OK"), eg.Button("Cancel")],
    ],
)
for event, values in window.event_iter():
    print("#", event, values)
    if event == "OK":
        json_str = json.dumps(values, indent=4, ensure_ascii=False)
        eg.print(json_str)
        break
    elif event == "Cancel":
        break
