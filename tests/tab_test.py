"""TabGroup / Tab test"""
import TkEasyGUI as eg


def main():
    """Main window"""
    layout = [
        [eg.TabGroup(
            layout=[
                [
                    eg.Tab(
                        "😊 Tab 1 - Hello",
                        [
                            [eg.Text("This is Tab 1")],
                            [eg.Text("You can put any widgets here")],
                            [eg.Text("Please click the tabs to see the content change.")],
                        ],
                    )
                ],
                [
                    eg.Tab(
                        "😊 Tab 2 - World",
                        [[eg.Text("This is Tab 2")], [eg.Button("Hello")]],
                    )
                ],
                [
                    eg.Tab(
                        "😊 Tab 3 - 猫",
                        [[eg.Text("This is Tab 3")], [eg.Button("猫")]],
                    )
                ],
            ],
            # vertical_alignment="top",
            # width=300,
            expand_y=True,
        )]
    ]
    window = eg.Window("Tab Test", layout, resizable=True)
    while window.is_running():
        event, values = window.read()
        if event == eg.WINDOW_CLOSED:
            break
        if event == "Hello":
            eg.print("Hello button clicked")
        if event == "猫":
            eg.print("猫 button clicked")
    window.close()

if __name__ == "__main__":
    main()

