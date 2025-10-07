"""Radio and Checkbox Example"""

import TkEasyGUI as eg


def main():
    """Main function to run the example."""
    # define UI
    layout_frame_os = [
        [
            eg.Radio(
                "Windows",
                group_id="OS",
                key="win",
                enable_events=True,
                default=True,
            )
        ],
        [eg.Radio("macOS", group_id="OS", key="mac", enable_events=True)],
        [eg.Radio("Ubuntu", group_id="OS", key="ubuntu", enable_events=True)],
        [eg.Radio("Others", group_id="OS", key="others", enable_events=True)],
    ]
    layout_frame_animals = [
        [eg.Checkbox("Dog", group_id="animals", enable_events=True, default=True)],
        [eg.Checkbox("Cat", group_id="animals", enable_events=True)],
        [eg.Checkbox("Rabit", group_id="animals", enable_events=True)],
        [eg.VPush()],
    ]
    layout = [
        [
            eg.Frame("OS:", layout=layout_frame_os, pad=(8, 8)),
            eg.VSeparator(pad=10),
            eg.Frame("Animals", layout=layout_frame_animals, pad=(8, 8)),
        ],
        [eg.HSeparator()],
        [eg.Button("OK"), eg.Button("Cancel")],
    ]
    window = eg.Window("Radio and Checkbox samples:", layout)
    while window.is_running():
        event, values = window.read()
        print("@@@", event, "values=", values)
        if event == "OK":
            os = values["OS"]
            animals = ",".join(values["animals"])
            eg.print(f"You selected: {os} and [{animals}]")
            break
        if event == "Cancel":
            break
    window.close()


if __name__ == "__main__":
    main()
