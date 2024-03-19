# Module tkeasygui.widgets

TkEasyGUI Widgets

## Classes

### Button

```python
class Button(self, button_text: str="", key: str="", **kw)
```

Button element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Button.GetText

```python
def GetText(self) -> str
```

Get the text of the button. (compatibility with PySimpleGUI)

------

##### Button.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

##### Button.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Button.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Canvas

```python
class Canvas(self, key: str="", enable_events: bool=False, background_color: str|None=None, size: tuple[int, int]=(300, 300), **kw)
```

Canvas element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Canvas.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

##### Canvas.get

```python
def get(self) -> Any
```

Return Widget

------

##### Canvas.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Checkbox

```python
class Checkbox(self, text: str="", default: bool=False, key: str="", enable_events: bool=False, **kw)
```

Button element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Checkbox.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

##### Checkbox.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Checkbox.get_value

```python
def get_value(self) -> Any
```

Get the value of the widget.

------

##### Checkbox.set_text

```python
def set_text(self, text: str) -> None
```

Set the text of the widget.

------

##### Checkbox.set_value

```python
def set_value(self, b: bool) -> None
```

Set the value of the widget.

------

##### Checkbox.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Column

```python
class Column(
    self, layout: list[list[Element]], key: str = "", background_color: str|None=None,
     vertical_alignment: TextVAlign="top",
     size: tuple[int, int]|None=None, **kw)
```

Frame element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Column.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

##### Column.get

```python
def get(self) -> Any
```

Return Widget

------

##### Column.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Combo

```python
class Combo(self, values: list[str]=[], default_value: str="", key: str="", enable_events: bool=False, **kw)
```

Combo element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Combo.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

[Combo.create] create Listbox widget

------

##### Combo.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Combo.set_value

```python
def set_value(self, v: str) -> None
```

Set the value of the widget.

------

##### Combo.set_values

```python
def set_values(self, values: list[str]) -> None
```

Set values to list

------

##### Combo.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Element

```python
class Element(self, element_type, key: str="", **kw)
```

Element class.

Create an element.

------

#### Methods

##### Element.bind

```python
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None
```

Bind event. @see `Window.bind`

------

##### Element.bind_events

```python
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> ElementType
```

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

------

##### Element.create

```python
def create(self, win: Window, parent: tk.Widget) -> Any
```

Create a widget.

------

##### Element.disptach_event

```python
def disptach_event(self, values: dict[str, Any]|None=None) -> None
```

Dispatch event

------

##### Element.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Element.prepare_create

```python
def prepare_create(self, win: Window) -> None
```

------

##### Element.update

```python
def update(self, *args, **kw) -> None
```

Update the widget props (only change `props`)

------

##### Element.widget_update

```python
def widget_update(self, **kw) -> None
```

------

### Frame

```python
class Frame(self, title: str, layout: list[list[Element]], key: str = "", background_color: str|None=None, size: tuple[int, int]|None=None, **kw)
```

Frame element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Frame.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

##### Frame.get

```python
def get(self) -> Any
```

Return Widget

------

##### Frame.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Graph

```python
class Graph(
    self, key: str="", background_color: str|None=None,
    size: tuple[int, int]=(300, 300), canvas_size: tuple[int, int]|None=None,
    graph_bottom_left: tuple[int, int]|None=None, graph_top_right: tuple[int, int]|None=None,
    **kw)
```

Graph element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Graph.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

##### Graph.draw_arc

```python
def draw_arc(self, top_left: PointType, bottom_right: PointType, extent: int|None = None, start_angle: int|None = None, style: str|None = None, arc_color: str|None = 'black', line_width: int = 1, fill_color: str|None = None) -> int
```

Draw an arc.

------

##### Graph.draw_circle

```python
def draw_circle(self, center_location: PointType, radius: int|float, fill_color: str|None = None, line_color: str|None = 'black', line_width: int = 1) -> int
```

Draw a circle.

------

##### Graph.draw_image

```python
def draw_image(self, filename: str|None=None, data: bytes|None=None, location: PointType|None=None) -> int
```

Draw image

------

##### Graph.draw_line

```python
def draw_line(self, point_from: PointType, point_to: PointType, color: str = 'black', width: int = 1) -> int
```

Draw a line.

------

##### Graph.draw_lines

```python
def draw_lines(self, points: list[PointType], color='black', width=1) -> int
```

Draw lines.

------

##### Graph.draw_oval

```python
def draw_oval(self, top_left: PointType, bottom_right: PointType, fill_color: str|None = None, line_color: str|None = None, line_width: int = 1)
```

Draw an oval.

------

##### Graph.draw_point

```python
def draw_point(self, point: PointType, size: int = 2, color: str = 'black') -> int
```

Draw a point.

------

##### Graph.draw_polygon

```python
def draw_polygon(self, points: list[PointType], fill_color: str|None=None, line_color: str|None=None, line_width: int|None=None) -> None
```

Draw polygon

------

##### Graph.draw_rectangle

```python
def draw_rectangle(self, top_left: PointType, bottom_right: PointType, fill_color: str|None=None, line_color: str|None=None, line_width: int|None=None) -> int
```

Draw rectangle

------

##### Graph.draw_text

```python
def draw_text(self, text: str, location: PointType, color: str|None='black', font: FontType=None, angle: float|str|None=0, text_location: TextAlign=tk.CENTER) -> int
```

Draw text

------

##### Graph.erase

```python
def erase(self) -> None
```

Delete all

------

##### Graph.get

```python
def get(self) -> Any
```

Return Widget

------

##### Graph.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Image

```python
class Image(self, source: bytes|str|None=None, filename=None, data=None, key: str="", background_color: str|None=None, size: tuple[int, int]=(300, 300), **kw)
```

Image element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Image.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a Image widget.

------

##### Image.get

```python
def get(self) -> Any
```

Return Widget

------

##### Image.update

```python
def update(self, source: bytes|str=None, filename: str|None=None, data: bytes|None=None, **kw) -> None
```

Update the widget.

------

### Input

```python
class Input(
    self, text: str="", key: str="",
     enable_events: bool=False,
     background_color: str|None=None, color: str|None=None,
     text_aligh: TextAlign="left",
     readonly: bool=False, readonly_background_color: str="silver", **kw)
```

Text input element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Input.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

create Input widget

------

##### Input.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Input.set_readonly

```python
def set_readonly(self, readonly: bool) -> None
```

set readonly

------

##### Input.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### InputText

```python
class InputText(text: str = '', key: str = '', enable_events: bool = False, background_color: str | None = None, color: str | None = None, text_aligh: Literal['left', 'right', 'center'] = 'left', readonly: bool = False, readonly_background_color: str = 'silver', **kw)
```

InputText element. (alias of Input)

------

#### Base classes

* [`Input `](#Input)

------

### Listbox

```python
class Listbox(self, values: list[str]=[], key: str="", enable_events: bool=False, select_mode: ListboxSelectMode="browse", **kw)
```

Listbox element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Listbox.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

[Listbox.create] create Listbox widget

------

##### Listbox.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Listbox.set_values

```python
def set_values(self, values: list[str]) -> None
```

Set values to list

------

##### Listbox.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Multiline

```python
class Multiline(
    self, text: str="", default_text: str|None=None, key: str="",
     enable_events: bool=False,
     color: str|None=None, background_color: str|None=None,
     readonly: bool=False, readonly_background_color: str='silver',
     size: tuple[int, int]=(50, 10),
     **kw)
```

Multiline text input element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Multiline.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

##### Multiline.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Multiline.set_readonly

```python
def set_readonly(self, readonly: bool) -> None
```

Set readonly

------

##### Multiline.set_text

```python
def set_text(self, text: str) -> None
```

Set text

------

##### Multiline.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Slider

```python
class Slider(
    self, key: str = "", range: tuple[float, float]=(1, 10),
     orientation: OrientationType="horizontal",
     resolution: float=1, default_value: float|None=None,
     enable_events: bool=False,
     **kw)
```

Slider element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Slider.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

##### Slider.get

```python
def get(self) -> Any
```

Return Widget

------

##### Slider.update

```python
def update(self, value: float|None=None, **kw) -> None
```

Update the widget.

------

### Table

```python
class Table(
    self, values: list[list[str]]=[], headings: list[str]=[], key: str="", justification: TextAlign="center",
     auto_size_columns: bool = True, max_col_width: int = 0, font: tuple[str, int]|None=None,
     enable_events: bool=False, select_mode: str="browse", **kw)
```

Table element.

Create a table.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Table.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a Table widget.

------

##### Table.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Table.set_values

```python
def set_values(self, values: list[list[str]], headings: list[str]) -> None
```

Set values to the table.

------

##### Table.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Text

```python
class Text(self, text: str, text_align: TextAlign="left", font: FontType|None=None, **kw)
```

Text element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Text.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a Text widget.

------

##### Text.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Text.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Textarea

```python
class Textarea(text: str = '', default_text: str | None = None, key: str = '', enable_events: bool = False, color: str | None = None, background_color: str | None = None, readonly: bool = False, readonly_background_color: str = 'silver', size: tuple[int, int] = (50, 10), **kw)
```

Textarea element. (alias of Multiline)

------

#### Base classes

* [`Multiline `](#Multiline)

------

### TkEasyError

```python
class TkEasyError(self, message="TkEasyError")
```

Common base class for all non-exit exceptions.

Initialize self.  See help(type(self)) for accurate signature.

------

#### Base classes

* `builtins.Exception`

------

### Window

```python
class Window(self, title: str, layout: list[list[ElementType]], size: (tuple[str, int]|None)=None, resizable:bool=False, modal: bool=False, **kw)
```

Main window object in TkEasyGUI

Create a window with a layout of widgets.

------

#### Methods

##### Window.bind

```python
def bind(self, element: "Element", event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None
```

[Window.bind] Bind element event and handler

------

##### Window.cancel_close

```python
def cancel_close(self) -> None
```

Cancel the close event.

------

##### Window.close

```python
def close(self) -> None
```

Close the window.

------

##### Window.get_values

```python
def get_values(self) -> dict[str, Any]
```

Get values from the window.

------

##### Window.hide

```python
def hide(self) -> None
```

Hide window

------

##### Window.is_alive

```python
def is_alive(self) -> bool
```

Check if the window is alive.

------

##### Window.move_to_center

```python
def move_to_center(self) -> None
```

Move the window to the center of the screen.

------

##### Window.read

```python
def read(self, timeout: int|None=None, timeout_key: str="-TIMEOUT-") -> tuple[str, dict[str, Any]]
```

Read events from the window.

------

##### Window.refresh

```python
def refresh(self) -> "Window"
```

Refresh window

------

##### Window.show

```python
def show(self) -> None
```

Show hidden window (hide -> show)

------

##### Window.write_event_value

```python
def write_event_value(self, key: str, values: dict[str, Any]) -> None
```

## Functions

### get_element_id

```python
def get_element_id() -> int
```

Get a unique id for an element.

------

### get_image_tk

```python
def get_image_tk(source: bytes|str|None=None, filename: str|None = None, data: bytes|None = None) -> tk.PhotoImage|None
```

Get Image for tk

------

### get_root_window

```python
def get_root_window() -> tk.Tk
```

Get root window.

------

### imagedata_to_bytes

```python
def imagedata_to_bytes(image_data: PILImage) -> bytes
```

Convert JPEG to PNG

------

### imagefile_to_bytes

```python
def imagefile_to_bytes(filename: str) -> bytes
```

Read image file and convert to bytes

------

### rgb

```python
def rgb(r: int, g: int, b: int) -> str
```

------

### time_checker_end

```python
def time_checker_end(start_time: datetime) -> int
```

------

### time_checker_start

```python
def time_checker_start() -> datetime
```