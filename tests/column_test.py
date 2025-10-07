"""
# Column test

Using the `Column` widget allows you to divide the window horizontally and place two-dimensional widgets in each Column.
"""

import TkEasyGUI as eg

# sample text
SAMPLE_TEXT = (("0123456789" * 5) + "\n") * 5

# define sub layout
layout1 = [
    [eg.Label("col1")],
    [eg.Multiline(SAMPLE_TEXT, key="-col1-", expand_x=True, expand_y=True)],
    [eg.Button("Get Size")],
]
layout2 = [
    [eg.Label("col2")],
    [eg.Multiline(SAMPLE_TEXT, key="-col2-", expand_x=True, expand_y=True)],
    [eg.Button("Test")],
]
layout3 = [
    [eg.Label("col3")],
    [eg.Multiline(SAMPLE_TEXT, key="-col3-", expand_x=True, expand_y=True)],
    [eg.InputText("TEST(col3)", key="-input-"), eg.Button("Add")],
]
# define main layout
col1 = eg.Column(layout1, key="col1", width=300, expand_y=True)
col2 = eg.Column(layout2, key="col2", width=300, expand_y=True)
col3 = eg.Column(layout3, key="col3", expand_x=True, expand_y=True)
main_layout = [
    [col1, col2, col3],
    [eg.HSeparator()],
    [eg.Button("Close")],
]
# create window
window = eg.Window(
    "Column test", main_layout, resizable=True, size=(900, 600), enable_events=True
)
# event loop
while window.is_running():
    event, values = window.read()
    if event == "Get Size":
        text = (
            f"col1={col1.get_width()}\ncol2={col2.get_width()}\ncol3={col3.get_width()}"
        )
        window["-col1-"].update(text)
    elif event == "Test":
        window["-col2-"].update("Test button clicked")
    elif event == "Add":
        v = values["-col3-"] + "\n" + values["-input-"]
        window["-col3-"].update(v)
    elif event == "Close":
        break
window.close()
