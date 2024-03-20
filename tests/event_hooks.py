import tkeasygui as eg

window = eg.Window("Event Hook Test", layout=[
    [eg.Text("Please Push OK Button, and see console log.")],
    [eg.Input("", key="-filepath-"), eg.FileBrowse()],
    [eg.Button("OK")],
    [eg.Button("STOP")],
])
window.register_event_hooks({
    "OK": [
        lambda event, values: print("hook#1:", event, values),
        lambda event, values: print("hook#2:", event, values),
        lambda event, values: print("hook#3:", event, values),
    ],
    "STOP": [
        lambda event, values: print("hook#1:", event, values),
        lambda event, values: print("hook#2:", event, values),
        lambda event, values: True, # stop event propagation
        lambda event, values: print("hook#3:", event, values),
    ]
})
while window.is_alive():
    event, values = window.read()
    if event == "OK":
        print("pushed OK")
    elif event == "STOP":
        print("pushed STOP")
    elif event == "STOP-stopped":
        print("stopped OK:", event, values)
        break
window.close()
