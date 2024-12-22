import TkEasyGUI as eg

win = eg.Window(
    title="Push Test",
    layout=[
        [eg.Text("=" * 50)],
        [eg.Push(), eg.Button("Right")],  # right alignment
        [eg.Push(), eg.Button("Center"), eg.Push()], # center alignment
    ],
)
while win.is_running():
    event, values = win.read()
    if event == "Center" or event == "Right":
        break
win.close()

