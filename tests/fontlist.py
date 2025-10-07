"""
Font List Sample
"""

import TkEasyGUI as eg

# list fonts
font_items = eg.get_font_list()

# define layout
layout = [
    [
        eg.Text("Find:"),
        eg.Input(
            key="-find-",
            enable_events=True,
            expand_x=True,
        ),
        eg.Button("Clear"),
    ],
    [
        eg.Listbox(
            values=font_items,
            size=(40, 10),
            key="-fontlist-",
            enable_events=True,
        )
    ],
    [eg.Input("-", key="-font-", expand_x=True), eg.Button("Copy")],
    [
        eg.Frame(
            "Sample",
            expand_x=True,
            layout=[[eg.Text("Hello, 123 こんにちは 你好", key="-sample-")]],
        )
    ],
]
# create Window
with eg.Window("Font List", layout, font=("Arial", 18)) as window:
    # event loop
    for event, values in window.event_iter():
        print("# event:", event, values)
        if event in ("Exit", eg.WINDOW_CLOSED):
            break
        if event == "-fontlist-":
            # get font name from listbox
            fontlist: eg.Listbox = window["-fontlist-"]
            index = fontlist.get_cursor_index()
            if index >= 0:
                font_name = font_items[index]
                window["-font-"].update(font_name)
                window["-sample-"].update(font=(font_name, 18))
        if event == "Copy":
            eg.set_clipboard(values["-font-"])
            eg.print("Copied to clipboard:\n" + values["-font-"])
        if event == "-find-":
            find_str = values["-find-"]
            if not find_str:
                window["-fontlist-"].update(values=font_items)
                continue
            find_str = find_str.lower()
            new_font_items = [f for f in font_items if find_str in f.lower()]
            window["-fontlist-"].update(values=new_font_items)
        if event == "Clear":
            window["-find-"].update("")
            window["-fontlist-"].update(values=font_items)
