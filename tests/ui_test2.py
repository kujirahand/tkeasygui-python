"""
UI Test
"""

import TkEasyGUI as eg

layout_left = eg.Column(
    [
        [
            eg.Frame(
                "OS",
                [
                    [eg.Checkbox("Windows")],
                    [eg.Checkbox("macOS")],
                    [eg.Checkbox("Ubuntu")],
                    [eg.Checkbox("ChromeOS")],
                ],
                expand_x=True,
            )
        ],
        [
            eg.Frame(
                "Animal",
                [
                    [eg.Radio("Dog", group_id="animal")],
                    [eg.Radio("Cat", group_id="animal")],
                    [eg.Radio("Rabit", group_id="animal")],
                ],
                expand_x=True,
                expand_y=True,
            )
        ],
        [eg.Listbox(["AAA", "BBB", "CCC"], width=10, expand_y=True)],
        [eg.VPush()],
    ],
    expand_y=True,
    vertical_alignment="top",
)

layout_center = eg.Frame(
    "Profile",
    [
        [eg.Text("Name:")],
        [eg.Input("TkEasyGUI", key="-name", expand_x=True)],
        [eg.Text("Hobby:")],
        [eg.Input("Programming", key="-name", expand_x=True)],
        [eg.Text("Fruits:")],
        [eg.Combo(["Mango", "Banana", "Apple"], default_value="Mango", expand_x=True)],
        [eg.Text("Number:")],
        [eg.Combo(["One", "Two", "Three"], default_value="One", expand_x=True)],
        [eg.Text("Language:")],
        [eg.Combo(["Python", "Rust", "C/C++"], default_value="One", expand_x=True)],
        [eg.Button("Hello", expand_x=True)],
        [eg.Button("World", expand_x=True)],
        [eg.Button("Test", expand_x=True)],
    ],
    expand_x=True,
    expand_y=True,
)

name_table = eg.Table(
    [["Alice", "30"], ["Bob", "25"], ["Charlie", "35"]],
    headings=["Name", "Age"],
    key="-table-",
    expand_x=True,
    expand_y=True,
)


layout_right = eg.Frame(
    "Info",
    [
        [eg.Text("This is the right column", width=50)],
        [eg.HSeparator()],
        [
            eg.TabGroup(
                layout=[
                    [
                        eg.Tab(
                            "Tab 1",
                            [
                                [name_table],
                            ],
                        )
                    ],
                    [
                        eg.Tab(
                            "Tab 2",
                            [[eg.Text("This is Tab 2")], [eg.Button("Button 2")]],
                        )
                    ],
                ],
                # vertical_alignment="top",
                # width=300,
                expand_y=True,
            )
        ],
    ],
    expand_x=True,
    expand_y=True,
)

layout = [[eg.Column([[layout_left, layout_center, layout_right]])]]
# event loop
# window create
window = eg.Window(
    "UI test",
    layout=layout,
    font=("Arial", 12),
    finalize=True,
    resizable=True,
)
# event loop
while window.is_running():
    event, values = window.read()
    print("#", event, values)
window.close()
