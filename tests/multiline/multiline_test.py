import TkEasyGUI as eg

test_text = """
Keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
""".strip()
text_text2 = """A joyful heart is good medicine,But a crushed spirit saps one’s strength."""

# create window
layout = [
    [eg.Multiline(test_text, size=(60, 15), key="-multiline-")],
    [eg.Button("Copy"), eg.Button("Change text")],
]
window = eg.Window("Multiline Test", layout=layout)
# get element from window
multiline: eg.Multiline = window["-multiline-"]
# event loop
while True:
    event, values = window.read()
    if event == eg.WINDOW_CLOSED: # close button
        break
    if event == "Change text":
        # multiline.update(text=text_text2)
        multiline.set_text(text_text2)
    if event == "Copy":
        multiline.select_all()
        text = multiline.copy()
        eg.popup(f"Copied:\n{text}")
window.close()
