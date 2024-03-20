"""
ui test
"""
# import PySimpleGUI as sg
import tkeasygui as sg

# window create
window = sg.Window("UI test", layout=[
    [
        sg.Column(layout=[[sg.Text("hoge")]], background_color="red", vertical_alignment="top", expand_y=300),
        sg.Column(layout=[
            [sg.Text("hoge")],
            [sg.Input("hoge")],
            [sg.Text("hoge")],
            [sg.Text("hoge")],
            [sg.Text("hoge")],
            [sg.Text("hoge")],
        ], vertical_alignment="top", expand_y=300),
    ],
    [sg.Button("OK")],
])
# event loop
while window.is_alive():
    event, values = window.read()
    print("#", event, values)
    if event == "OK":
        sg.popup("OK")
        print("--hoge--")
        break
window.close()
