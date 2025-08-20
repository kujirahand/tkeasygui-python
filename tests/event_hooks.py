"""
### register_event_hooks method sample

This sample demonstrates how to use the `register_event_hooks` method.
`register_event_hooks` method allows you to register multiple event hooks for each event.
"""

import TkEasyGUI as eg

window = eg.Window(
    "Event Hook Test",
    layout=[
        [
            eg.Frame(
                "Event Hooks Test",
                layout=[
                    [eg.Button("B1"), eg.Button("B2"), eg.Button("B3")],
                    [
                        eg.Multiline(
                            key="-log-", autoscroll=True, expand_x=True, expand_y=True
                        )
                    ],
                ],
            ),
        ]
    ],
)


def print_log(text, event, values):
    # print log to "-log-"
    log: eg.Multiline = window["-log-"]
    log.print("📍", text_color="blue", end="")
    log.print(event + " ", text_color="red", end="")
    log.print(text, text_color="blue")
    return False


# Register event hooks
window.register_event_hooks(
    {
        # When pushing the `B1` button, the event hooks for `B1` will be executed.
        "B1": [
            lambda event, values: print_log("B1::hook#1:", event, values),
            lambda event, values: print_log("B1::hook#2:", event, values),
            lambda event, values: print_log("B1::hook#3:", event, values),
        ],
        "B2": [
            lambda event, values: print_log("B2::hook#1:", event, values),
            lambda event, values: print_log("B2::hook#2:", event, values),
            lambda event, values: True,  # stop event propagation
            lambda event, values: print_log("B2::hook#3:", event, values),
        ],
    }
)

# Event Loop
while window.is_running():
    # get window event
    event, values = window.read()
    if event == "B1":
        print_log("@@@@ pushed B1", event, values)
    elif event == "B2":
        print_log("@@@ pushed B2", event, values)
    elif event == "B3":
        print_log("@@@ pushed B3", event, values)
window.close()
