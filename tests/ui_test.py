"""
ui test
"""
# import PySimpleGUI as sg
import TkEasyGUI as sg

# window create
window = sg.Window("UI test", layout=[
    [sg.Text("TkEasyGUI Test:")],
    [sg.Input("input1", key="-input1-", enable_events=True)],
    [sg.Multiline("multiine", key="-multiline-", enable_events=True)],
    [sg.Slider(key="-slide-", enable_events=True, orientation="h", range=(0, 100), default_value=50, expand_x=True)],
    [sg.Listbox(["list1", "list2", "list3", "list4"], key="-listbox-", enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED), sg.Text("-", key="-listbox-text-")],
    [sg.Radio("Radio1", group_id="abc", key="-radio1-", enable_events=True), sg.Radio("Radio2",group_id="abc", key="-radio2-", default=True, enable_events=True)],
    [sg.Checkbox("Checkbox", key="-checkbox-", enable_events=True), sg.Button("Change", key="-checkbox-button-")],
    [sg.Combo(["combo1", "combo2", "combo3"], default_value="combo1", key="-combo-", enable_events=True), sg.Button("Change", key="-combo-button-")],
    [sg.Button("Exit")],
], font=("Arial", 18))
# event loop
while True:
    event, values = window.read()
    print("#", event, values)
    if event in (None, "Exit", sg.WINDOW_CLOSED):
        break
    if event == "-listbox-":
        selected = " selected: " + "/".join(values["-listbox-"])
        window["-listbox-text-"].update(text=selected)
    if event == "-checkbox-button-":
        b = window["-checkbox-"].get()
        window["-checkbox-"].update(value=(not b), text="Changed")
    if event == "-combo-button-":
        window["-combo-"].update(value="combo3")
window.close()
