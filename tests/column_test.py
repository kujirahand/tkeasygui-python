# Column test
import TkEasyGUI as eg

# sample text
a_text = (("0123456789" * 5) + "\n") * 5

# define sub layout
layout1 = [[eg.Multiline(a_text, key="-size-", expand_x=True, expand_y=True)]]
layout2 = [[eg.Multiline(a_text, expand_x=True, expand_y=True)]]
layout3 = [
    [eg.Multiline(a_text, expand_x=True, expand_y=True)],
    [eg.InputText("Input1"), eg.Button("Button2")]
] 
# define main layout
col1 = eg.Column(layout1, key="col1", width=300, expand_y=True)
col2 = eg.Column(layout2, key="col2", width=300, expand_y=True)
col3 = eg.Column(layout3, key="col3", expand_x=True, expand_y=True)
main_layout = [
    [col1, col2, col3],
    [eg.HSeparator()],
    [eg.Button("Get Size"), eg.Button("Close")],
]
# create window
window = eg.Window(
    "Column test", main_layout, resizable=True, size=(900, 600), enable_events=True
)
# event loop
while window.is_running():
    event, values = window.read()
    if event == "Get Size":
        text = f"col1={col1.get_width()}\ncol2={col2.get_width()}\ncol3={col3.get_width()}"
        window["-size-"].update(text)
    elif event == "Close":
        break
window.close()
