import TkEasyGUI as sg

# create window
window = sg.Window(
    "text/simple",
    layout=[[sg.Text("Hello, World!!")]],
    font=("Arial", 20))
# event loop
while window.is_alive():
    event, _ = window.read()
window.close()
