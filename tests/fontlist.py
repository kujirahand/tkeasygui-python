"""
Font List Sample
"""
import TkEasyGUI as eg

# list fonts
font_items = eg.get_font_list()

# define layout
layout = [
    [
        eg.Frame(
            "Sample",
            expand_x=True,
            layout=[[eg.Text("Hello, 123 こんにちは 你好", key="-sample-")]],
        )
    ],
    [
        eg.Listbox(
            values=font_items,
            size=(40, 20),
            key="-fontlist-",
            enable_events=True,
        )
    ],
    [eg.Input("-", key="-font-", expand_x=True), eg.Button("Copy")],
    [eg.Button("Exit")],
]
# create Window
with eg.Window("Font List", layout, font=("Arial", 18)) as window:
    # event loop
    for event, values in window.event_iter():
        print("# event:", event, values)
        if event == "Exit" or event == eg.WINDOW_CLOSED:
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


