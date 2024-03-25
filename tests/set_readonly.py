import TkEasyGUI as eg

# import PySimpleGUI as eg

a_font = ("Arial", 20)
window = eg.Window("BasicUI", layout=[
    [eg.Button("Change", key="-change-", font=a_font),eg.Button("Readonly(tkeasygui)", font=a_font)],
    [eg.Text("Text", key="-text-", font=a_font)],
    [eg.Input("Input", key="-input-", font=a_font)],
    [eg.Multiline("Multiline", key="-multiline-", font=a_font)],
])
# event loop
readonly = False
while True:
    event, values = window.read()
    if event == eg.WINDOW_CLOSED:
        break
    print(event, values)
    if event == "-change-":
        print("change")
        window["-change-"].update("changed!!")
        window["-text-"].update("changed!!")
        window["-input-"].update("changed!!")
        window["-multiline-"].update("changed!!")
    if event == "Readonly(tkeasygui)":
        readonly = not readonly
        window["-input-"].update(readonly=readonly)
        window["-multiline-"].update(readonly=readonly)
window.close()
