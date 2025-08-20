import TkEasyGUI as eg

test_text = """
Better to enjoy
what the eyes see than
to wander after one's desires.
This too is futility,
a chasing after the wind.
""".strip()

# create window
with eg.Window(
    "Multiline Right",
    layout=[
        [eg.Multiline(test_text, key="-multiline-", size=(50, 10), text_align="right")],
        [eg.Button("Close"), eg.Button("Add")],
    ],
) as window:
    # event loop
    for event, values in window.event_iter():
        print("## Event:", event, "values:", values)
        if event == "Close":
            break
        if event == "Add":
            more_text = (
                window["-multiline-"].get_text()
                + "\n"
                + 'He says: "A lion in the public square!"'
            )
            window["-multiline-"].set_text(more_text)
        print(event, values)
