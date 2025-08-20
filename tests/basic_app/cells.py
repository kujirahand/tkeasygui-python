"""
Cells > TkEasyGUI for The 7 Tasks of GUI Programming

@ref https://7guis.github.io/7guis/tasks/

### comment:
Currently, TkEasyGUI does not have spreadsheet functionality.
Instead, we use a read-only table to simulate cell editing.
"""

# pylint: disable=line-too-long
import random
import TkEasyGUI as eg


def main():
    """Main function"""
    # Prepare dummy data
    head = [chr(i) for i in range(ord("A"), ord("O") + 1)]
    print("Head:", head)
    data = []
    for _ in range(40):
        row = [f"{random.randint(0, 5)}" for _ in range(len(head))]
        data.append(row)

    # Create a window
    window = eg.Window(
        "Dummy Cells",
        layout=[
            [
                eg.Table(  # Read-only table to simulate cells
                    key="-table",
                    values=data,
                    headings=head,
                    enable_events=True,
                    col_widths=[4] * len(head),
                    vertical_scroll_only=False,
                    select_mode="single",
                    expand_x=True,
                    expand_y=True,
                ),
            ],
            [
                eg.Button("Edit", expand_x=True),
                eg.Button("Sum Rows", expand_x=True),
                eg.Button("Sum Columns", expand_x=True),
            ],
        ],
        size=(640, 400),
    )
    # Bind events
    window["-table"].bind_events(
        {
            "<Double-1>": "double_click",
        },
        "system",
    )
    # event loop
    while window.is_alive():
        # read events from the window
        event, values = window.read()
        print("@Event:", event, "Values:", values)
        # check events
        if event == "Sum Rows":
            index = window["-table"].get_cursor_index()
            if index < 0:
                index = None
            result = []
            for row in data:
                total = sum(int(x) for x in row)
                result.append(total)
            labels = [f"Row({i + 1:02}): {total:,}" for i, total in enumerate(result)]
            eg.popup_listbox(values=labels, title="Row Sum Result", default_index=index)
        if event == "Sum Columns":
            print("Head:", head)
            result = []
            for i, col_name in enumerate(head):
                print(col_name)
                total = 0
                for row in data:
                    total += int(row[i] if len(row) > i else 0)
                result.append(f"Column({col_name}): {total:,}")
            eg.popup_listbox(
                values=result,
                title="Column Sum Result",
            )
        if event == "Edit":
            edit_row(window["-table"], data, head)
        if event == "-table":
            event_type = values.get("event_type", "")
            if event_type == "double_click":
                edit_row(window["-table"], data, head)
    window.close()


def edit_row(table: eg.Table, data: list[list[str]], head: list[str]) -> None:
    """Edit selected row in the table"""
    index = table.get_cursor_index()
    if index < 0 or index >= len(data):
        return
    # Prepare form items
    cols = data[index]
    items = []
    for i, col in enumerate(cols):
        items.append((head[i], col))
    # popup form
    res = eg.popup_get_form(form_items=items, title="Edit Row")
    if res is None:
        return
    # Update data
    for key, val in res.items():
        i = head.index(key)
        if i >= 0:
            data[index][i] = val
    table.update(values=data)


if __name__ == "__main__":
    main()
