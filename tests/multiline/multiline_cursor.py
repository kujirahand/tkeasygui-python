import TkEasyGUI as eg

window = eg.Window("Test Multiline", layout=[
    [eg.Multiline(
        "123456789\n223456789\n323456789", key="-multiline-", size=(50, 10),
        enable_events=True, enable_key_events=True)],
    [eg.Button("set_selection_pos"), eg.Button("get_selection_pos")],
    [eg.Button("get_selected_text"), eg.Button("copy_selected_text")],
    [eg.Button("set_cursor_pos('3.0')"), eg.Button("set_cursor_pos('1.0')")],
    [eg.Button("get_selection_start"), eg.Button("get_selection_length")],
    [eg.Button("set_selection_start"), eg.Button("?")],
])
multiline:eg.Multiline = window["-multiline-"]
while window.is_alive():
    event, values = window.read()
    print(event, values)
    if event == "終了": break
    elif event == "get_selection_pos":
        start_pos, end_pos = multiline.get_selection_pos()
        eg.popup(f"{start_pos}-{end_pos}")
    elif event == "set_selection_pos":
        multiline.set_selection_pos("2.0", "2.5")
    elif event == "get_selected_text":
        eg.popup(multiline.get_selected_text())
    elif event == "set_selected_text":
        eg.popup(multiline.get_selected_text())
    elif event == "copy_selected_text":
        eg.popup(multiline.copy_selected_text())
    elif event == "set_cursor_pos('3.0')":
        multiline.set_cursor_pos("3.0")
    elif event == "set_cursor_pos('1.0')":
        multiline.set_cursor_pos("1.0")
    elif event == "get_selection_start":
        eg.popup(multiline.get_selection_start())
    elif event == "get_selection_length":
        eg.popup(multiline.get_selection_length())
    elif event == "set_selection_start":
        multiline.set_selection_start(0, 5)
window.close()
