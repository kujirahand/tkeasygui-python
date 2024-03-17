# Module tkeasygui.widgets

## Classes

### Button {: #Button }

```python
class Button(self, text: str="", key: str="", **kw)
```

Button element.

Create an element.

------

#### Base classes {: #Button-bases }

* [`Element `](#Element)

------

#### Methods {: #Button-methods }

[**create**](#Button.create){: #Button.create }

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

[**get**](#Button.get){: #Button.get }

```python
def get(self) -> Any
```

Get the value of the widget.

------

### Element {: #Element }

```python
class Element(self, element_type, key: str="", **kw)
```

Element class.

Create an element.

------

#### Methods {: #Element-methods }

[**GetText**](#Element.GetText){: #Element.GetText }

```python
def GetText(self) -> Any
```

Get the text of the widget. (for Button)

------

[**create**](#Element.create){: #Element.create }

```python
def create(self, win: Window, parent: tk.Widget) -> Any
```

Create a widget.

------

[**get**](#Element.get){: #Element.get }

```python
def get(self) -> Any
```

Get the value of the widget.

------

[**prepare_create**](#Element.prepare_create){: #Element.prepare_create }

```python
def prepare_create(self, win: Window) -> None
```

------

[**update**](#Element.update){: #Element.update }

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Input {: #Input }

```python
class Input(self, text: str, key: str="", **kw)
```

Text input element.

Create an element.

------

#### Base classes {: #Input-bases }

* [`Element `](#Element)

------

#### Methods {: #Input-methods }

[**create**](#Input.create){: #Input.create }

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

[**get**](#Input.get){: #Input.get }

```python
def get(self) -> Any
```

Get the value of the widget.

------

[**update**](#Input.update){: #Input.update }

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### InputText {: #InputText }

```python
class InputText(self, text: str, key: str="", **kw)
```

InputText element. (alias of Input)

Create an element.

------

#### Base classes {: #InputText-bases }

* [`Input `](#Input)

------

### Listbox {: #Listbox }

```python
class Listbox(self, values: list[str]=[], key: str="", enable_events: bool=False, select_mode: str="browse", **kw)
```

Listbox element.

Create an element.

------

#### Base classes {: #Listbox-bases }

* [`Element `](#Element)

------

#### Methods {: #Listbox-methods }

[**create**](#Listbox.create){: #Listbox.create }

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

[**get**](#Listbox.get){: #Listbox.get }

```python
def get(self) -> Any
```

Get the value of the widget.

------

[**update**](#Listbox.update){: #Listbox.update }

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Multiline {: #Multiline }

```python
class Multiline(self, default_text: str="", key: str="", **kw)
```

Multiline text input element.

Create an element.

------

#### Base classes {: #Multiline-bases }

* [`Element `](#Element)

------

#### Methods {: #Multiline-methods }

[**create**](#Multiline.create){: #Multiline.create }

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

[**get**](#Multiline.get){: #Multiline.get }

```python
def get(self) -> Any
```

Get the value of the widget.

------

[**update**](#Multiline.update){: #Multiline.update }

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Table {: #Table }

```python
class Table(
    self, values: list[list[str]]=[], headings: list[str]=[], key: str="", justification: Literal["right","left","center",""]="",
     auto_size_columns: bool = True, max_col_width: int = 0, font: tuple[str, int]|None=None,
     enable_events: bool=False, select_mode: str="browse", **kw)
```

Table element.

Create a table.

------

#### Base classes {: #Table-bases }

* [`Element `](#Element)

------

#### Methods {: #Table-methods }

[**create**](#Table.create){: #Table.create }

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a Table widget.

------

[**get**](#Table.get){: #Table.get }

```python
def get(self) -> Any
```

Get the value of the widget.

------

[**set_values**](#Table.set_values){: #Table.set_values }

```python
def set_values(self, values: list[list[str]], headings: list[str]) -> None
```

Set values to the table.

------

[**update**](#Table.update){: #Table.update }

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Text {: #Text }

```python
class Text(self, text: str, justify: Literal["left","right","center"]="left", **kw)
```

Text element.

Create an element.

------

#### Base classes {: #Text-bases }

* [`Element `](#Element)

------

#### Methods {: #Text-methods }

[**create**](#Text.create){: #Text.create }

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a Text widget.

------

[**get**](#Text.get){: #Text.get }

```python
def get(self) -> Any
```

Get the value of the widget.

------

[**update**](#Text.update){: #Text.update }

```python
def update(self, *args, **kw) -> None
```

Update the widget.

------

### Window {: #Window }

```python
class Window(self, title: str, layout: list[list[Any]], size: (tuple[int, int]|None)=None, resizable:bool=True, **kw)
```

Main window object in TkEasyGUI

Examples:
    >>> # Create window
    >>> layout = [
    >>>     [eg.Text("Hello, World!")],
    >>>     [eg.Button("OK")]
    >>> ]
    >>> window = eg.Window("Hello", layout=layout)
    >>> # Event loop
    >>> while window.is_alive():
    >>>     # get event
    >>>     event, values = window.read()
    >>>     # check event
    >>>     if event == "OK":
    >>>         eg.popup("Pushed OK Button")
    >>>         break
    >>> window.close()

Create a window with a layout of widgets.

------

#### Methods {: #Window-methods }

[**cancel_close**](#Window.cancel_close){: #Window.cancel_close }

```python
def cancel_close(self) -> None
```

Cancel the close event.

------

[**close**](#Window.close){: #Window.close }

```python
def close(self) -> None
```

Close the window.

------

[**get_values**](#Window.get_values){: #Window.get_values }

```python
def get_values(self) -> dict[str, Any]
```

Get values from the window.

------

[**is_alive**](#Window.is_alive){: #Window.is_alive }

```python
def is_alive(self) -> bool
```

Check if the window is alive.

------

[**read**](#Window.read){: #Window.read }

```python
def read(self, timeout: int|None=None, timeout_key: str="-TIMEOUT-") -> tuple[str, dict[str, Any]]
```

Read events from the window.

------

[**write_event_value**](#Window.write_event_value){: #Window.write_event_value }

```python
def write_event_value(self, key: str, values: dict[str, Any]) -> None
```

## Functions

### get_element_id {: #get_element_id }

```python
def get_element_id() -> int
```

Get a unique id for an element.