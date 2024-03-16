import tkeasygui as eg
win = eg.Window("Hello, world!", layout=[
    [eg.Text("Hello, world!", bg="red"), eg.TextInput("Hello, world!")],
    [eg.Text("Hello, world!"), eg.TextInput("Hello, world!")],
    [eg.Button("適用1")],
    [eg.Button("適用2")],
])
while True:
    event, values = win.read()
    print("***", event, values)
    if event == eg.WINDOW_CLOSED:
        print(values)
        break
    print("----")
print("end")
