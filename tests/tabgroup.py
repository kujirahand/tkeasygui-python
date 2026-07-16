import TkEasyGUI as eg

layout = [
    [
        eg.TabGroup(
            layout=[
                [
                    eg.Tab(
                        "Tab 1",
                        [
                            [eg.Text("This is Tab 1")],
                            [eg.Text("This is Tab 1")],
                            [eg.Text("This is Tab 1")],
                            [eg.Text("This is Tab 1")],
                            [eg.Text("This is Tab 1")],
                            [eg.Button("Button 1")],
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
            vertical_alignment="top",
            expand_x=True,
            expand_y=True,
        )
    ]
]

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
