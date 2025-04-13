"""TkEasyGUI Layout Test"""

import TkEasyGUI as eg


def layout_helper_horizontal():
    """Test layout helper function"""
    layout = [
        [eg.Text("-" * 60)],
        eg.align_left([eg.Text("LEFT")]),
        eg.align_center([eg.Text("CENTER")]),
        eg.align_right([eg.Text("RIGHT")]),
        [eg.Text("-" * 60)],
        eg.align_center([eg.Button("Vertical"), eg.Button("Exit")]),
    ]

    with eg.Window("Test Layout Helper", layout=layout) as win:
        for event, values in win.event_iter():
            print(event, values)
            if event == "Exit":
                break
            if event == "Vertical":
                layout_helper_vertical()
                break


def layout_helper_vertical():
    """Test layout helper function"""
    layout_c1 = eg.valign_middle([eg.align_center([eg.Text("MIDDLE")])])
    layout_c2 = eg.valign_bottom([eg.align_center([eg.Text("BOTTOM")])])
    layout_c3 = eg.valign_top([eg.align_center([eg.Text("TOP")])])
    layout_c4 = [[eg.Text("", size=(1, 10))]]
    layout = [
        [
            eg.Column(layout=layout_c1, expand_y=True),
            eg.VSeparator(),
            eg.Column(layout=layout_c2, expand_y=True),
            eg.VSeparator(),
            eg.Column(layout=layout_c3, expand_y=True),
            eg.Column(layout=layout_c4),
        ],
        [eg.HSeparator()],
        eg.align_center([eg.Button("Exit")]),
    ]
    with eg.Window("Test Layout Helper", layout=layout) as win:
        for event, values in win.event_iter():
            print(event, values)
            if event == "Exit":
                break


if __name__ == "__main__":
    layout_helper_horizontal()
