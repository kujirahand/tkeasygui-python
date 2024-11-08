import TkEasyGUI as eg

result = eg.popup_get_form(
    [
        ["name", "text"],
        ["age", "number"],
        ["status", "combo", ["A", "B", "C"]],
        ["fruits", "list", ["Banana", "Orange", "Apple"]],
        ["password", "password"],
        ["date", "date"],
        ["file", "file"],
        ["theme color", "color"],
    ],
    title="Form Test",
)
print(result)
