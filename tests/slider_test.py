# import PySimpleGUI as eg
import TkEasyGUI as eg

# define layout
layout = [
    [eg.Text("-slider1-")],
    [eg.Slider(key="-slider1-", range=[0, 100], size=[30, 2], orientation="h", default_value=50, resolution=0.1)],
    [eg.HSeparator()],
    [eg.Text("-slider2- (disable_number_display=True)")],
    [
        eg.Slider(key="-slider2-", range=[0, 100], size=[30, 2], orientation="h", default_value=0, resolution=1, enable_events=True, disable_number_display=True),
        eg.Text("0.0", key="-text2-"),
    ],
    [eg.Button("Change to 20"), eg.Button("Check Value")],
    [eg.HSeparator()],
    [eg.Text("-slider3-")],
    [
        eg.Slider(key="-slider3-", range=[0, 100], size=[2, 30], orientation="v", default_value=50, resolution=0.1, disable_number_display=False, enable_changed_events=True),
        eg.VSeparator(),
        eg.Multiline("", key="-output-", size=[50, 20]),
    ],
    [eg.HSeparator()],
    [eg.Button("Exit")]
]
# create a window
window = eg.Window("Slider Test", layout)
# event loop
while True:
    event, values = window.read()
    print(f"event={event} || values={values}")
    if event in ["Exit", eg.WIN_CLOSED]:
        break
    if event == "-slider2-":
        v = values["-slider2-"]
        window["-text2-"].update(str(v))
    if event == "Change to 20":
        window["-slider1-"].update(value=20)
        window["-slider2-"].update(value=20)
        window["-text2-"].update("20.0")
    if event == "Check Value" or event == "-slider3-" or event == "-slider2-":
        s = event + "\n"
        s += f"-slider1-: {values['-slider1-']}\n"
        s += f"-slider2-: {values['-slider2-']}\n"
        s += f"-slider3-: {values['-slider3-']}\n"
        window["-output-"].update(s)
