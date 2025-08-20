"""
CRUD > TkEasyGUI for The 7 Tasks of GUI Programming

@ref https://7guis.github.io/7guis/tasks/
"""

# pylint: disable=line-too-long,too-many-locals,too-many-statements,too-many-branches
from typing import Union, Optional
import TkEasyGUI as eg

# -------------------------------------------------------------
# DataManager for CRUD operations
# -------------------------------------------------------------
DataItems = list[dict[str, Union[str, int]]]


class DataManager:
    """DataManager for CRUD operations"""

    def __init__(self, data: Optional[DataItems] = None) -> None:
        """Initialize DataManager with optional data"""
        self.data: DataItems = []
        self.last_id: int = 1
        self.filtered_data: DataItems = []
        # set data
        if data is not None:
            self.data = data
            self.last_id = max(int(item["id"]) for item in data)
            self.filtered_data = data

    def add_item(self, name: str, surname: str) -> bool:
        """Add a new item to the data"""
        if name and surname:
            self.data.append({"id": self.last_id, "name": name, "surname": surname})
            self.last_id += 1
            return True
        return False

    def update_item(self, item_id: int, name: str, surname: str) -> bool:
        """Update an existing item by ID"""
        for item in self.data:
            if item["id"] == item_id:
                if name and surname:
                    item["name"] = name
                    item["surname"] = surname
                    return True
                return False
        return False

    def delete_item(self, item_id: int) -> bool:
        """Delete an item by ID"""
        for i, item in enumerate(self.data):
            if item["id"] == item_id:
                del self.data[i]
                return True
        return False

    def filter(self, prefix: str) -> DataItems:
        """Filter items based on prefix"""
        if prefix == "":
            self.filtered_data = self.data
            return self.filtered_data
        self.filtered_data = [
            item
            for item in self.data
            if str(item["name"]).startswith(prefix)
            or str(item["surname"]).startswith(prefix)
        ]
        return self.filtered_data

    def get_display_list(self) -> list[str]:
        """Get display list for the listbox"""
        return [f"{item['name']}, {item['surname']}" for item in self.filtered_data]


# -------------------------------------------------------------
# GUI APPLICATION
# -------------------------------------------------------------
def main():
    """Main function"""
    # Initialize DataManager with some sample data
    data_manager = DataManager(
        [
            {"id": 1, "name": "John", "surname": "Doe"},
            {"id": 2, "name": "Jane", "surname": "Smith"},
        ]
    )

    # GUI Layout
    layout_left = [
        [
            eg.Push(),
            eg.Label("Filter prefix:"),
            eg.Input("", key="-filter", width=5, enable_events=True),
        ],
        [
            eg.Listbox(
                items=data_manager.get_display_list(),
                key="-list",
                size=(20, 5),
                enable_events=True,
            )
        ],
    ]
    layout_right = [
        [eg.Label("Name:", size=(7, 1)), eg.Input("", key="-name", width=6)],
        [eg.Label("Surname:", size=(7, 1)), eg.Input("", key="-surname", width=6)],
    ]
    layout_main = [
        [
            eg.Column(layout=layout_left),
            eg.VSeparator(),
            eg.Column(layout=layout_right),
        ],
        [
            eg.Button("Create"),
            eg.Button("Update"),
            eg.Button("Delete"),
            eg.Push(),
            eg.Button("Quit"),
        ],
    ]

    # Create the main window
    window = eg.Window("CRUD Test", layout_main)

    # Event loop
    while window.is_running():
        event, values = window.read()
        if event == "-filter":
            # Update listbox based on filter input
            show_list(window, data_manager)
            continue
        if event == "-list":
            # Select item from listbox
            listbox: eg.Listbox = window["-list"]
            index = listbox.get_cursor_index()
            if index >= 0:
                item = data_manager.filtered_data[index]
                window["-name"].update(item["name"])
                window["-surname"].update(item["surname"])
            else:
                window["-name"].update("")
                window["-surname"].update("")
        if event == "Quit":
            yesno = eg.popup_yes_no("Do you want to quit?", title="Quit")
            if yesno == "Yes":
                break
            continue
        # CRUD Buttons
        if event == "Create":
            data_manager.add_item(values["-name"], values["-surname"])
            clear_inputs(window)
            show_list(window, data_manager)
            continue
        if event == "Update":
            index = window["-list"].get_cursor_index()
            if index >= 0:
                item = data_manager.filtered_data[index]
                if data_manager.update_item(
                    item["id"], values["-name"], values["-surname"]
                ):
                    clear_inputs(window)
                    show_list(window, data_manager)
                else:
                    eg.popup_error("Invalid input. Name and Surname cannot be empty.")
            else:
                eg.popup_error("No item selected for update.")
            continue
        if event == "Delete":
            index = window["-list"].get_cursor_index()
            if index >= 0:
                item = data_manager.filtered_data[index]
                if data_manager.delete_item(item["id"]):
                    eg.popup_ok(f"Deleted {item['name']} {item['surname']}")
                    clear_inputs(window)
                    show_list(window, data_manager)
                else:
                    eg.popup_error("Failed to delete item.")
            continue
    window.close()


# -------------------------------------------------------------
# GUI Utility Functions
# -------------------------------------------------------------
def show_list(window: eg.Window, data_manager: DataManager) -> None:
    """Show current list in the listbox."""
    # Get the filter string from the input field
    filter_str = window["-filter"].get()
    # Filter the data and update the listbox
    data_manager.filter(filter_str)
    window["-list"].update(values=data_manager.get_display_list())


def clear_inputs(window: eg.Window) -> None:
    """Clear input fields."""
    window["-name"].update("")
    window["-surname"].update("")
    window["-filter"].update("")


if __name__ == "__main__":
    main()
