import TkEasyGUI as eg

window = eg.Window(
    "Test Multiline",
    layout=[
        [
            eg.Multiline(
                "123456789\n223456789\n323456789",
                key="-multiline-",
                size=(50, 10),
                enable_events=True,
                enable_key_events=True,
            )
        ],
        # selection
        [eg.Text("selection")],
        [eg.Button("set_selection_pos"), eg.Button("get_selection_pos")],
        [eg.Button("get_selected_text")],
        [eg.Button("get_selection_start"), eg.Button("get_selection_length")],
        # selection_start
        [eg.Text("selection_start")],
        [eg.Button("set_selection_start(0,5)"), eg.Button("set_selection_start(10,5)")],
        [eg.Button("set_selection_start(20,5)"), eg.Button("set_selection_start(11)")],
        # cursor
        [eg.Text("cursor")],
        [eg.Button("set_cursor_pos('3.0')"), eg.Button("set_cursor_pos('1.0')")],
        # copy / paste
        [eg.Text("copy/paste")],
        [
            eg.Button("copy"),
            eg.Button("paste"),
            eg.Button("select_all"),
            eg.Button("cut"),
        ],
    ],
)
multiline: eg.Multiline = window["-multiline-"]
while window.is_alive():
    event, values = window.read()
    print(event, values)
    if event == "終了":
        break
    elif event == "get_selection_pos":
        start_pos, end_pos = multiline.get_selection_pos()
        eg.popup(f"{start_pos}-{end_pos}")
    elif event == "set_selection_pos":
        multiline.set_selection_pos("2.0", "2.5")
    elif event == "get_selected_text":
        eg.popup(multiline.get_selected_text())
    elif event == "set_selected_text":
        eg.popup(multiline.get_selected_text())
    elif event == "copy":
        multiline.copy()
        eg.popup("copied")
    elif event == "paste":
        multiline.paste()
    elif event == "cut":
        cut = multiline.cut()
        eg.popup(f"cut: {cut}")
    elif event == "set_cursor_pos('3.0')":
        multiline.set_cursor_pos("3.0")
    elif event == "set_cursor_pos('1.0')":
        multiline.set_cursor_pos("1.0")
    elif event == "get_selection_start":
        eg.popup(multiline.get_selection_start())
    elif event == "get_selection_length":
        eg.popup(multiline.get_selection_length())
    elif event == "set_selection_start(0,5)":
        multiline.set_selection_start(0, 5)
    elif event == "set_selection_start(10,5)":
        multiline.set_selection_start(10, 5)
    elif event == "set_selection_start(20,5)":
        multiline.set_selection_start(20, 5)
    elif event == "set_selection_start(11)":
        multiline.set_selection_start(11)
    elif event == "select_all":
        multiline.select_all()
window.close()
