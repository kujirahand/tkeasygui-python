import TkEasyGUI as eg

# Create a window
window = eg.Window("Hello World", layout=[
    [eg.Text("OS:")],
    [eg.Combo([
        "Windows", "macOS", "Ubuntu", "Other"],
        key="-os-",
        readonly=True,
        default_value="macOS")],
    [eg.Button("OK")]])
# event loop
for event, values in window.event_iter():
    if event == "OK":
        eg.print(values["-os-"])
        break
