# no key sample - Inch to cm converter
# import PySimpleGUI as sg
import TkEasyGUI as sg

window = sg.Window("Inch to cm", layout=[
    [sg.Text("Please input Inch:")],
    [sg.Input("1"), sg.Button("Convert")],
])
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Convert":
        try:
            inch = float(values[0]) # key = 0
            cm = inch * 2.54
            result = f"{inch} inch is {cm} cm"
            sg.popup(result)
        except Exception as _e:
            sg.popup("Please input number.")
window.close()
