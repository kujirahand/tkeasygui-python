import TkEasyGUI as eg

result = eg.popup_get_form(
    [
        ["Name", "kujira"],
        ["Age", 20, "number"],
        ["OS",["Windows", "macOS", "Ubuntu"],"combo"],
        ["Fruits", ["Banana", "Orange"], "list",],
        ["Password", "", "password"],
        ["Date", "", "date"],
        ["File", "", "file"],
        ["Theme Color", "", "color"],
    ],
    title="Form Test",
)
print(result)
