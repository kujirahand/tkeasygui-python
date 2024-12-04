import TkEasyGUI as eg

# define UI
layout = [
    [
        eg.Frame(
            "OS:",
            layout=[
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
            ],
        )
    ],
    [
        eg.Frame(
            "Animals",
            layout=[
                [
                    eg.Checkbox(
                        "Dog", group_id="animals", enable_events=True, default=True
                    )
                ],
                [eg.Checkbox("Cat", group_id="animals", enable_events=True)],
                [eg.Checkbox("Rabit", group_id="animals", enable_events=True)],
            ],
        )
    ],
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
