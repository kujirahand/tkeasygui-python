import TkEasyGUI as eg

result = eg.popup_get_form(
    [
        ["Name", "text"],
        ["Age", "number"],
        ["OS", "combo", ["Windows", "macOS", "Ubuntu"]],
        ["Fruits", "list", ["Banana", "Orange", "Apple"]],
        ["Password", "password"],
        ["Date", "date"],
        ["File", "file"],
        ["Theme Color", "color"],
    ],
    title="Form Test",
)
print(result)
