# Module TkEasyGUI.widgets

TkEasyGUI Widgets

## Classes

### Button

```python
class Button(
    self,
    button_text: str="",
    key: str|None = None,
    disabled: bool=None,
    size: tuple[int, int]|None=None,
    use_ttk_buttons: bool=False,
    tooltip: str|None=None, # (TODO) tooltip
    button_color: str|tuple[str, str]|None=None,
    # text props
    text_align: TextAlign|None="left", # text align
    font: FontType|None=None, # font
    color: str|None=None, # text color
    text_color: str|None=None, # same as color
    background_color: str|None=None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: PadType|None = None,
    # other
    metadata: dict[str, Any]|None=None,
    **kw)
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

##### Button.get_text

```python
def get_text(self) -> str
```

------

##### Button.set_button_color

```python
def set_button_color(self, button_color: str|tuple[str,str], update: bool=True) -> None
```

Set the button color.

------

##### Button.set_text

```python
def set_text(self, text: str) -> None
```

Set the text of the widget.

------

##### Button.update

```python
def update(self, text: str|None=None, disabled: bool|None=None, button_color: str|tuple[str,str]|None=None, **kw) -> None
```

Update the widget.

------

### Canvas

```python
class Canvas(
    self,
    key: str|None = None,
    enable_events: bool = False,
    background_color: str|None = None,
    size: tuple[int, int] = (300, 300),
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
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
class Checkbox(
    self, text: str="",
    default: bool=False,
    key: str|None = None,
    enable_events: bool=False,
    # other
    metadata: dict[str, Any]|None=None,
    **kw)
```

Checkbox element.

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

### ColorBrowse

```python
class ColorBrowse(
    self,
    button_text: str="...",
    key: str|None = None,
    target_key: str|None = None,
    default_color: str|None = None,
    title: str="",
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
```

FolderBrowse element.

Create an element.

------

#### Base classes

* [`FileBrowse `](#FileBrowse)

------

#### Methods

##### ColorBrowse.show_dialog

```python
def show_dialog(self, *args) -> str|None
```

Show file dialog

------

### Column

```python
class Column(
    self,
    layout: list[list[Element]],
    key: str = "",
    background_color: str|None=None,
    vertical_alignment: TextVAlign="top",
    size: tuple[int, int]|None=None,
    # text props
    text_align: TextAlign|None="left", # text align
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: PadType|None = None,
    # other
    metadata: dict[str, Any]|None=None,
    **kw)
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
class Combo(
    self,
    values: list[str]=[],
    default_value: str="",
    key: str|None = None,
    enable_events: bool = False,
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
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
class Element(
    self,
    element_type: str, # element type
    ttk_style_name: str, # tkinter widget type
    key: str|None, # key
    has_value: bool, # has value
    metadata: dict[str, Any]|None=None, # meta data
    **kw)
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

##### Element.convert_props

```python
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]
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

##### Element.get_name

```python
def get_name(self) -> str
```

Get element name.

------

##### Element.get_prev_widget

```python
def get_prev_widget(self, target_key: str|None=None) -> tk.Widget
```

Get the previous widget.

------

##### Element.post_create

```python
def post_create(self, win: Window, parent: tk.Widget) -> None
```

Post create widget.

------

##### Element.prepare_create

```python
def prepare_create(self, win: Window) -> None
```

------

##### Element.set_disabled

```python
def set_disabled(self, disabled: bool) -> None
```

------

##### Element.update

```python
def update(self, *args, **kw) -> None
```

update widget configuration.

------

##### Element.widget_update

```python
def widget_update(self, **kw) -> None
```

------

### FileBrowse

```python
class FileBrowse(
    self, button_text: str="...",
    key: str|None = None,
    title: str = "",
    target_key: str|None = None,
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    multiple_files: bool = False,
    initial_folder: str|None = None,
    save_as: bool = False,
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
```

FileBrowse element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### FileBrowse.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

##### FileBrowse.set_text

```python
def set_text(self, text: str) -> None
```

Set the text of the button.

------

##### FileBrowse.show_dialog

```python
def show_dialog(self, *args) -> str|None
```

Show file dialog

------

##### FileBrowse.update

```python
def update(self, text: str|None=None, **kw) -> None
```

Update the widget.

------

### FileSaveAs

```python
class FileSaveAs(button_text: str = '...', key: str | None = None, title: str = '', target_key: str | None = None, file_types: tuple[tuple[str, str]] = (('All Files', '*.*'),), multiple_files: bool = False, initial_folder: str | None = None, save_as: bool = False, metadata: dict[str, typing.Any] | None = None, **kw)
```

FileSaveAs element. (alias of FileSaveAsBrowse)

------

#### Base classes

* [`FileBrowse `](#FileBrowse)

------

### FileSaveAsBrowse

```python
class FileSaveAsBrowse(
    self,
    button_text: str="...",
    key: str|None = None,
    target_key: str|None = None,
    title: str = "",
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
```

FileSaveAsBrowse element.

Create an element.

------

#### Base classes

* [`FileBrowse `](#FileBrowse)

------

### FilesBrowse

```python
class FilesBrowse(
    self,
    button_text: str = "...",
    key: str|None = None,
    target_key: str|None = None,
    title: str="",
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
```

FilesBrowse element.

Create an element.

------

#### Base classes

* [`FileBrowse `](#FileBrowse)

------

### FolderBrowse

```python
class FolderBrowse(
    self,
    button_text: str="...",
    key: str|None = None,
    target_key: str|None = None,
    default_path: str|None = None,
    title: str = "",
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
```

FolderBrowse element.

Create an element.

------

#### Base classes

* [`FileBrowse `](#FileBrowse)

------

#### Methods

##### FolderBrowse.show_dialog

```python
def show_dialog(self, *args) -> str|None
```

Show file dialog

------

### Frame

```python
class Frame(
    self,
    title: str,
    layout: list[list[Element]],
    key: str = "",
    size: tuple[int, int]|None=None,
    relief: ReliefType="groove",
    # text props
    font: FontType|None=None, # font
    color: str|None=None,
    text_color: str|None=None,
    background_color: str|None=None,
    label_outside: bool=False,
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: PadType|None = None,
    # other
    metadata: dict[str, Any]|None=None,
    use_ttk: bool=False,
    **kw)
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

Create a Frame widget.

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
    self, key: str|None = None,
    background_color: str|None = None,
    size: tuple[int, int]=(300, 300),
    canvas_size: tuple[int, int]|None = None,
    graph_bottom_left: tuple[int, int]|None = None,
    graph_top_right: tuple[int, int]|None = None,
    # other
    metadata: dict[str, Any]|None = None,
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

### HSeparator

```python
class HSeparator(
    self,
    key: str|None = None,
    background_color: str|None = None,
    pad: PadType = 5,
    size: tuple[int, int] = (100, 5),
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
```

HSeparator element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### HSeparator.create

```python
def create(self, win: Window, parent: tk.Widget) -> Any
```

Create a widget.

------

### Image

```python
class Image(
    self,
    source: bytes|str|None = None, # image source
    filename = None, # filen ame
    data: bytes = None, # image data
    key: str|None = None,
    background_color: str|None = None,
    size: tuple[int, int] = (300, 300),
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
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

##### Image.erase

```python
def erase(self) -> None
```

Erase image

------

##### Image.get

```python
def get(self) -> Any
```

Return Widget

------

##### Image.set_image

```python
def set_image(self, source: bytes|str=None, filename: str|None=None, data: bytes|None=None) -> None
```

------

##### Image.update

```python
def update(self, source: bytes|str=None, filename: str|None=None, data: bytes|None=None, size: tuple[int,int]|None=None, **kw) -> None
```

Update the widget.

------

### Input

```python
class Input(
    self,
    text: str = "", # default text
    key: str|None = None, # key
    default_text: str|None = None, # same as text
    enable_events: bool = False, # enabled events ([enter] or [change])
    enable_key_events: bool = False,  # enabled key events
    enable_focus_events: bool = False, # enabled focus events
    readonly_background_color: str|None = "silver",
    password_char: str|None = None, # if you want to use it as a password input box, set "*"
    readonly: bool = False, # read only box
    # text props
    text_align: TextAlign|None = "left", # text align
    font: FontType|None = None, # font
    color: str|None = None, # text color
    text_color: str|None = None, # same as color
    background_color: str|None = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: PadType|None = None,
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
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

##### Input.get_text

```python
def get_text(self) -> str
```

------

##### Input.set_readonly

```python
def set_readonly(self, readonly: bool) -> None
```

set readonly

------

##### Input.set_text

```python
def set_text(self, text: str) -> None
```

------

##### Input.update

```python
def update(self, text: str|None=None, readonly: bool|None=None, **kw) -> None
```

Update the widget.

------

### InputText

```python
class InputText(text: str = '', key: str | None = None, default_text: str | None = None, enable_events: bool = False, enable_key_events: bool = False, enable_focus_events: bool = False, readonly_background_color: str | None = 'silver', password_char: str | None = None, readonly: bool = False, text_align: Optional[Literal['left', 'right', 'center']] = 'left', font: tuple[str, int] | tuple[str, int, str] | None = None, color: str | None = None, text_color: str | None = None, background_color: str | None = None, expand_x: bool = False, expand_y: bool = False, pad: int | tuple[int, int] | tuple[tuple[int, int], tuple[int, int]] | None = None, metadata: dict[str, typing.Any] | None = None, **kw)
```

InputText element. (alias of Input)

------

#### Base classes

* [`Input `](#Input)

------

### Label

```python
class Label(text: str = '', key: str | None = None, enable_events: bool = False, wrap_length: int | None = None, text_align: Optional[Literal['left', 'right', 'center']] = 'left', font: tuple[str, int] | tuple[str, int, str] | None = None, color: str | None = None, text_color: str | None = None, background_color: str | None = None, expand_x: bool = False, expand_y: bool = False, pad: int | tuple[int, int] | tuple[tuple[int, int], tuple[int, int]] | None = None, metadata: dict[str, typing.Any] | None = None, **kw)
```

Label element (alias of Text)

------

#### Base classes

* [`Text `](#Text)

------

### Listbox

```python
class Listbox(
    self,
    values: list[str] = [],
    default_values: list[str] = [],
    key: str|None = None,
    enable_events: bool = False,
    select_mode: ListboxSelectMode = LISTBOX_SELECT_MODE_BROWSE,
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
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

##### Listbox.select_values

```python
def select_values(self, values: list[str]) -> None
```

Select values

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

### Menu

```python
class Menu(
    self,
    items:Any|None=None,
    menu_definition:list[list[str|list[Any]]]|None=None,
    key: str|None=None,
    metadata: dict[str, Any]|None=None,
    **kw)
```

Menu element.
**Example**
```
menu = eg.Menu([
    ["File", ["Open", "Save", "---","Exit"]],
    ["Edit", ["Copy", "Paste"]],
])
```
**Note**
- "!label" is disabled
- **"label**: :-event_name-" is set event name
- "---" is separator

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Menu.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a Text widget.

------

##### Menu.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Menu.get_text

```python
def get_text(self) -> str
```

------

##### Menu.set_text

```python
def set_text(self, text: str) -> None
```

Set the text of the widget.

------

##### Menu.update

```python
def update(self, text: str|None=None, *args, **kw) -> None
```

Update the widget.

------

### Multiline

```python
class Multiline(
    self,
    text: str = "", # default text
    default_text: str|None = None, # same as text
    key: str|None = None, # key
    readonly: bool = False,
    enable_events: bool = False, 
    enable_key_events: bool = False,
    enable_focus_events: bool = False,
    size: tuple[int, int] = (50, 10), # element size (unit=character)
    # text props
    font: FontType|None = None, # font
    color: str|None = None, # text color
    text_color: str|None = None, # same as color
    background_color: str|None = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: PadType|None = None,
    # other
    readonly_background_color: str|None = None,
    metadata: dict[str, Any]|None = None,
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

##### Multiline.get_text

```python
def get_text(self) -> str
```

------

##### Multiline.print

```python
def print(self, text: str, text_color: str|None=None, background_color: str|None=None, end:str="\n") -> None
```

Print text.

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
def update(self, text: str|None = None, readonly: bool|None = None, **kw) -> None
```

Update the widget.

------

### Output

```python
class Output(text: str = '', default_text: str | None = None, key: str | None = None, readonly: bool = False, enable_events: bool = False, enable_key_events: bool = False, enable_focus_events: bool = False, size: tuple[int, int] = (50, 10), font: tuple[str, int] | tuple[str, int, str] | None = None, color: str | None = None, text_color: str | None = None, background_color: str | None = None, expand_x: bool = False, expand_y: bool = False, pad: int | tuple[int, int] | tuple[tuple[int, int], tuple[int, int]] | None = None, readonly_background_color: str | None = None, metadata: dict[str, typing.Any] | None = None, **kw)
```

Output element. (alias of Multiline) TODO: implement

------

#### Base classes

* [`Multiline `](#Multiline)

------

### Radio

```python
class Radio(
    self, text: str="",
    group_id: int|str="group",
    default: bool=False,
    key: str|None = None,
    enable_events: bool=False,
    # other
    metadata: dict[str, Any]|None=None,
    **kw)
```

Checkbox element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### Radio.create

```python
def create(self, win: Window, parent: tk.Widget) -> tk.Widget
```

Create a widget.

------

##### Radio.get

```python
def get(self) -> Any
```

Get the value of the widget.

------

##### Radio.get_value

```python
def get_value(self) -> bool
```

Get the value of the widget.

------

##### Radio.is_selected

```python
def is_selected(self) -> bool
```

Check if the radio button is selected.

------

##### Radio.select

```python
def select(self) -> None
```

Select the radio button.

------

##### Radio.set_text

```python
def set_text(self, text: str) -> None
```

Set the text of the widget.

------

##### Radio.update

```python
def update(self, text: str|None=None, **kw) -> None
```

Update the widget.

------

### Slider

```python
class Slider(
    self,
    key: str|None = None,
    range: tuple[float, float] = (1, 10),
    orientation: OrientationType = "horizontal",
    resolution: float|None = None,
    default_value: float|None = None,
    enable_events: bool = False,
    # other
    metadata: dict[str, Any]|None = None,
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

### Submit

```python
class Submit(button_text: str = '', key: str | None = None, disabled: bool = None, size: tuple[int, int] | None = None, use_ttk_buttons: bool = False, tooltip: str | None = None, button_color: str | tuple[str, str] | None = None, text_align: Optional[Literal['left', 'right', 'center']] = 'left', font: tuple[str, int] | tuple[str, int, str] | None = None, color: str | None = None, text_color: str | None = None, background_color: str | None = None, expand_x: bool = False, expand_y: bool = False, pad: int | tuple[int, int] | tuple[tuple[int, int], tuple[int, int]] | None = None, metadata: dict[str, typing.Any] | None = None, **kw)
```

Subtmi element. (Alias of Button) : todo: add submit event

------

#### Base classes

* [`Button `](#Button)

------

### Table

```python
class Table(
    self,
    values: list[list[str]] = [],
    headings: list[str] = [],
    key: str|None = None,
    justification: TextAlign = "center",
    auto_size_columns: bool = True,
    max_col_width: int = 0,
    col_widths: list[int]|None = None,
    enable_events: bool = False,
    event_returns_values: bool|None = None, # Returns the table value if set to True, otherwise returns the index.
    select_mode: str="browse",
    # text props
    text_align: TextAlign|None = "left", # text align
    font: FontType|None = None, # font
    color: str|None = None, # text color
    text_color: str|None = None, # same as color
    background_color: str|None = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: PadType|None = None,
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
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
class Text(
    self,
    text: str = "",
    key: str|None=None,
    enable_events: bool=False, # enabled events (click)
    wrap_length: int|None=None, # wrap length(unit=pixel)
    # text props
    text_align: TextAlign|None="left", # text align
    font: FontType|None=None, # font
    color: str|None=None, # text color
    text_color: str|None=None, # same as color
    background_color: str|None=None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: PadType|None = None,
    # other
    metadata: dict[str, Any]|None=None, # user metadata
    **kw)
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

##### Text.get_text

```python
def get_text(self) -> str
```

------

##### Text.set_text

```python
def set_text(self, text: str) -> None
```

Set the text of the widget.

------

##### Text.update

```python
def update(self, text: str|None=None, *args, **kw) -> None
```

Update the widget.

------

### Textarea

```python
class Textarea(text: str = '', default_text: str | None = None, key: str | None = None, readonly: bool = False, enable_events: bool = False, enable_key_events: bool = False, enable_focus_events: bool = False, size: tuple[int, int] = (50, 10), font: tuple[str, int] | tuple[str, int, str] | None = None, color: str | None = None, text_color: str | None = None, background_color: str | None = None, expand_x: bool = False, expand_y: bool = False, pad: int | tuple[int, int] | tuple[tuple[int, int], tuple[int, int]] | None = None, readonly_background_color: str | None = None, metadata: dict[str, typing.Any] | None = None, **kw)
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

### VSeparator

```python
class VSeparator(
    self,
    key: str|None = None,
    background_color: str|None = None,
    pad: PadType = 5,
    size: tuple[int, int]=(5, 100),
    # other
    metadata: dict[str, Any]|None = None,
    **kw)
```

VSeparator element.

Create an element.

------

#### Base classes

* [`Element `](#Element)

------

#### Methods

##### VSeparator.create

```python
def create(self, win: Window, parent: tk.Widget) -> Any
```

Create a widget.

------

### Window

```python
class Window(
    self,
    title: str,
    layout: list[list[ElementType]],
    size: tuple[str, int]|None=None, 
    resizable:bool=False,
    font:FontType|None=None,
    modal: bool=False, 
    keep_on_top:bool=False, # keep on top
    no_titlebar: bool=False, # hide titlebar
    grab_anywhere: bool=False, # can move window by dragging anywhere
    alpha_channel: float=1.0,
    **kw)
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

##### Window.get_element_by_key

```python
def get_element_by_key(self, key: str) -> Union[ElementType, None]
```

Get an element by its key.

------

##### Window.get_elements_by_type

```python
def get_elements_by_type(self, element_type: str) -> list[ElementType]
```

Get elements by type.

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

Hide the window.

------

##### Window.hide_titlebar

```python
def hide_titlebar(self, flag: bool) -> None
```

Hide the titlebar.

------

##### Window.is_alive

```python
def is_alive(self) -> bool
```

Check if the window is alive.

------

##### Window.keep_on_top

```python
def keep_on_top(self, flag: bool) -> None
```

Set the window to keep on top.

------

##### Window.maximize

```python
def maximize(self) -> None
```

Maximize the window. (`resizable` should be set to True)

------

##### Window.minimize

```python
def minimize(self) -> None
```

Minimize the window.

------

##### Window.move_to_center

```python
def move_to_center(self) -> None
```

Move the window to the center of the screen.

------

##### Window.normal

```python
def normal(self) -> None
```

set normal window.

------

##### Window.read

```python
def read(self, timeout: int|None=None, timeout_key: str="-TIMEOUT-") -> tuple[str, dict[str, Any]]
```

[Window.read] Read events from the window.

------

##### Window.refresh

```python
def refresh(self) -> "Window"
```

Refresh window

------

##### Window.register_event_hooks

```python
def register_event_hooks(self, hooks: dict[str, list[callable]]) -> None
```

[Window.register_event_hooks] Register event hooks. (append events)
**Example**
```
window.register_event_hooks({
    "-input-": [
        lambda event, values: print("1", event, values),
        lambda event, values: print("2", event, values),
        lambda event, values: True, # stop event propagation
        lambda event, values: print("3", event, values),
    ],
```
**Note**
- If you specify a function that returns True, it changes the event name to f"{event}-stopped" and then re-collects the values associated with keys that occur afterwards.
- **@see** `Window.read`

------

##### Window.send_to_back

```python
def send_to_back(self) -> None
```

Send the window to the back, and make it not keep on top.

------

##### Window.set_alpha_channel

```python
def set_alpha_channel(self, alpha: float) -> None
```

Set the alpha channel of the window.

------

##### Window.set_grab_anywhere

```python
def set_grab_anywhere(self, flag: bool) -> None
```

Set grab anywhere

------

##### Window.set_title

```python
def set_title(self, title: str) -> None
```

Set the title of the window.

------

##### Window.show

```python
def show(self) -> None
```

Show hidden window (hide -> show)

------

##### Window.un_hide

```python
def un_hide(self) -> None
```

Un hide the window.

------

##### Window.write_event_value

```python
def write_event_value(self, key: str, values: dict[str, Any]) -> None
```

## Functions

### generate_element_id

```python
def generate_element_id() -> int
```

Generate a unique id for a value element.

------

### generate_element_style_key

```python
def generate_element_style_key(element_type: str) -> int
```

Get a unique id for an element.

------

### get_current_theme

```python
def get_current_theme() -> str
```

Get current theme

------

### get_font_list

```python
def get_font_list() -> list[str]
```

Get font list

------

### get_image_tk

```python
def get_image_tk(source: bytes|str|None=None, filename: str|None = None, data: bytes|None = None, size: tuple[int, int]|None = None) -> tk.PhotoImage|None
```

Get Image for tk

------

### get_platform

```python
def get_platform() -> str
```

get platform

------

### get_root_window

```python
def get_root_window() -> tk.Tk
```

Get root window.

------

### get_tnemes

```python
def get_tnemes() -> list[str]
```

Get themes

------

### get_ttk_style

```python
def get_ttk_style() -> ttk.Style
```

Get ttk style

------

### image_resize

```python
def image_resize(img: PILImage, size: tuple[int, int]) -> PILImage
```

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

### is_mac

```python
def is_mac() -> bool
```

platform : is mac?

------

### is_win

```python
def is_win() -> bool
```

platform : is Windows?

------

### register_element_key

```python
def register_element_key(key: str) -> bool
```

Register element key.

------

### rgb

```python
def rgb(r: int, g: int, b: int) -> str
```

------

### set_PySimpleGUI_compatibility

```python
def set_PySimpleGUI_compatibility(flag: bool=True) -> None
```

Set compatibility with PySimpleGUI (Default=True)

------

### set_default_theme

```python
def set_default_theme() -> None
```

Set default theme

------

### set_theme

```python
def set_theme(name: str) -> None
```

Change look and feel

------

### theme

```python
def theme(name: str) -> None
```

Set theme

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