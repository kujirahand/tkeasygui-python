"""
Circle Drawer > TkEasyGUI for The 7 Tasks of GUI Programming

@ref https://7guis.github.io/7guis/tasks/
"""

# pylint: disable=line-too-long
import TkEasyGUI as eg


# -------------------------------------------------------------
# Circle Items
# -------------------------------------------------------------
class CircleItem:
    """Circle Item for drawing circles"""

    def __init__(self, x: int, y: int, radius: int) -> None:
        """Initialize CircleItem with position and radius"""
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, canvas: eg.Graph) -> None:
        """Draw the circle on the given canvas"""
        canvas.draw_circle(
            (self.x, self.y), self.radius, fill_color="#F0F0FF", line_color="black"
        )


class CircleItemList:
    """List of CircleItems"""

    def __init__(self) -> None:
        """Initialize an empty list of CircleItems"""
        self.items: list[CircleItem] = []
        # Stack for redo operations (items that were undone)
        self._redo_stack: list[CircleItem] = []

    def add(self, item: CircleItem) -> None:
        """Add a CircleItem to the list"""
        self.items.append(item)
        # Adding a new item invalidates the redo history
        self._redo_stack.clear()

    def clear(self) -> None:
        """Clear all CircleItems from the list"""
        self.items.clear()
        # Clearing also drops redo history for simplicity
        self._redo_stack.clear()

    def undo(self) -> None:
        """Undo the last CircleItem"""
        if self.items:
            item = self.items.pop()
            # Push the undone item to redo stack
            self._redo_stack.append(item)

    def redo(self) -> None:
        """Redo the last undone CircleItem"""
        if self._redo_stack:
            item = self._redo_stack.pop()
            self.items.append(item)

    def can_undeo(self) -> bool:
        """Return True if undo is possible (typo kept as requested)."""
        return len(self.items) > 0

    def can_redo(self) -> bool:
        """Return True if redo is possible."""
        return len(self._redo_stack) > 0


# -------------------------------------------------------------
# Circle Drawer Application
# -------------------------------------------------------------
def main():
    """Main function"""
    circle_items = CircleItemList()
    # Create a window
    window = eg.Window(
        "Circle Drawer",
        layout=[
            [
                eg.Button("Undo", key="-undo", expand_x=True),
                eg.Button("Redo", key="-redo", expand_x=True),
            ],
            [eg.HSeparator()],
            [eg.Label("Click to draw circles:")],
            [eg.Graph(key="-canvas", size=(400, 400), expand_x=True)],
            [eg.HSeparator()],
            [eg.Label("Radius:")],
            [
                eg.Slider(
                    value_range=(10, 50),
                    default=30,
                    key="-radius",
                    size=(15, 1),
                    expand_x=True,
                )
            ],
            [eg.HSeparator()],
            [eg.Button("Clear", expand_x=True)],
        ],
    )
    # Bind events
    canvas = window["-canvas"]
    canvas.bind_events(
        {
            "<ButtonPress>": "mousedown",
        },
        "system",
    )
    draw_items(canvas, circle_items.items)
    # initialize undo/redo buttons state
    update_undo_redo_buttons(window, circle_items)
    # event loop
    while window.is_alive():
        # read events from the window
        event, values = window.read()
        print("@Event:", event, "@Values:", values)
        # check events
        if event == "Clear":
            circle_items.clear()
            draw_items(canvas, circle_items.items)
            update_undo_redo_buttons(window, circle_items)
            continue
        if event == "-undo":
            circle_items.undo()
            draw_items(canvas, circle_items.items)
            update_undo_redo_buttons(window, circle_items)
            continue
        if event == "-redo":
            circle_items.redo()
            draw_items(canvas, circle_items.items)
            update_undo_redo_buttons(window, circle_items)
            continue
        if event == "-canvas":
            c_event_type = values.get("event_type", "")
            c_event = values.get("event", {"x": 0, "y": 0})
            if c_event_type == "mousedown":
                x, y = c_event.x, c_event.y
                radius = values.get("-radius", 50)
                item = CircleItem(x, y, radius)
                circle_items.add(item)
                draw_items(canvas, circle_items.items)
                update_undo_redo_buttons(window, circle_items)

    window.close()


# -------------------------------------------------------------
# Utility functions
# -------------------------------------------------------------
def draw_items(canvas: eg.Graph, items: list[CircleItem]) -> None:
    """Draw all circle items on the canvas"""
    canvas.clear_all()
    for item in items:
        item.draw(canvas)


def update_undo_redo_buttons(window: eg.Window, items: CircleItemList) -> None:
    """Enable/Disable Undo/Redo buttons according to current state."""
    # Note: method name can_undeo intentionally matches the provided spec (typo)
    window["-undo"].set_disabled(not items.can_undeo())
    window["-redo"].set_disabled(not items.can_redo())


if __name__ == "__main__":
    main()
