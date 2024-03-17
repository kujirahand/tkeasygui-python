# Module tkeasygui.widgets

## Classes

### Button

```python
class Button(self, text: str="", key: str="", **kw)
```

Button element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

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

### Element

```python
class Element(self, element_type, key: str="", **kw)
```

Element class.

Create an element.

------

#### Methods

##### Element.GetText

```python
def GetText(self) -> Any
```

Get the text of the widget. (for Button)

------

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

Update the widget.

------

### Input

```python
class Input(self, text: str, key: str="", **kw)
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

Create a widget.

------

##### Input.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Input.update

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### InputText

```python
class InputText(self, text: str, key: str="", **kw)
```

InputText element. (alias of Input)

Create an element.

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
class Multiline(self, default_text: str="", key: str="", **kw)
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
class Text(self, text: str, justify: Literal["left","right","center"]="left", **kw)
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

### Window

```python
class Window(self, title: str, layout: list[list[Any]], size: (tuple[int, int]|None)=None, resizable:bool=False, modal: bool=False, **kw)
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