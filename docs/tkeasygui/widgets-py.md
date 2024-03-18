# Module tkeasygui.widgets

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
class Canvas(self, key: str="", background_color: str|None=None, size: tuple[int, int]=(300, 300), **kw)
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

### Element

```python
class Element(self, element_type, key: str="", **kw)
```

Element class.

Create an element.

------

#### Methods

##### Element.create

```python
def create(self, win: Window, parent: tk.Widget) -> Any
```

Create a widget.

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
def draw_text(self, text: str, location: PointType, color: str|None='black', font: FontType=None, angle: int=0, text_location: TextAlign=tk.CENTER) -> int
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

### Input

```python
class Input(
    self, text: str="", key: str="", background_color: str="white", color: str = "black", text_aligh: TextAlign="left",
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
class InputText(text: str = '', key: str = '', background_color: str = 'white', color: str = 'black', text_aligh: Literal['left', 'right', 'center'] = 'left', readonly: bool = False, readonly_background_color: str = 'silver', **kw)
```

InputText element. (alias of Input)

------

#### Base classes

* [`Input `](#Input)

------

### Listbox

```python
class Listbox(self, values: list[str]=[], key: str="", enable_events: bool=False, select_mode: str="browse", **kw)
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

Create a widget.

------

##### Listbox.get

```python
def get(self) -> Any
```

Get the value of the widget.

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
     color: str="black", background_color: str="white",
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

### Table

```python
class Table(
    self, values: list[list[str]]=[], headings: list[str]=[], key: str="", justification: Literal["right","left","center",""]="",
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
class Window(self, title: str, layout: list[list["Element"]], size: (tuple[str, int]|None)=None, resizable:bool=False, modal: bool=False, **kw)
```

Main window object in TkEasyGUI

Create a window with a layout of widgets.

------

#### Methods

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

### rgb

```python
def rgb(r: int, g: int, b: int) -> str
```