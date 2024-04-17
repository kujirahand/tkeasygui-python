# Module TkEasyGUI.widgets

TkEasyGUI Widgets

---------------------------

- [Classes](#classes-of-tkeasygui.widgets)
- [Functions](#functions-of-tkeasygui.widgets)

# Classes of TkEasyGUI.widgets

## Button

Button element.

```py
class Button(
    self,
    button_text: str = "",
    key: Union[str, None] = None,
    disabled: bool = None,
    size: Union[tuple[int, int], None] = None,
    use_ttk_buttons: Union[bool, None] = None,
    tooltip: Union[str, None] = None, # (TODO) tooltip
    button_color: Union[str, tuple[str, str], None] = None,
    # text props
    text_align: Union[TextAlign, None] = "left", # text align
    font: Union[FontType, None] = None, # font
    color: Union[str, None] = None, # text color
    text_color: Union[str, None] = None, # same as color
    background_color: Union[str, None] = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1334)

### Methods of Button

- [bind](#button.bind)
- [bind_events](#button.bind_events)
- [convert_props](#button.convert_props)
- [create](#button.create)
- [disptach_event](#button.disptach_event)
- [get](#button.get)
- [get_name](#button.get_name)
- [get_prev_widget](#button.get_prev_widget)
- [get_text](#button.get_text)
- [post_create](#button.post_create)
- [prepare_create](#button.prepare_create)
- [set_button_color](#button.set_button_color)
- [set_disabled](#button.set_disabled)
- [set_text](#button.set_text)
- [update](#button.update)
- [widget_update](#button.widget_update)

### Button.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Button.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Button.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Button.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1377)

### Button.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Button.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1404)

### Button.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Button.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Button.get_text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1413)

### Button.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Button.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Button.set_button_color

Set the button color.

```py
def set_button_color(self, button_color: Union[str, tuple[str,str]], update: bool = True) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1390)

### Button.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Button.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1408)

### Button.update

Update the widget.

```py
def update(self,
    text: Union[str, None] = None,
    disabled: Union[bool, None] = None,
    button_color: Union[str, tuple[str,str], None] = None,
    **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1416)

### Button.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Canvas

Canvas element.

```py
class Canvas(
    self,
    key: Union[str, None] = None,
    enable_events: bool = False,
    background_color: Union[str, None] = None,
    size: tuple[int, int] = (300, 300),
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2199)

### Methods of Canvas

- [bind](#canvas.bind)
- [bind_events](#canvas.bind_events)
- [convert_props](#canvas.convert_props)
- [create](#canvas.create)
- [disptach_event](#canvas.disptach_event)
- [get](#canvas.get)
- [get_name](#canvas.get_name)
- [get_prev_widget](#canvas.get_prev_widget)
- [post_create](#canvas.post_create)
- [prepare_create](#canvas.prepare_create)
- [set_disabled](#canvas.set_disabled)
- [update](#canvas.update)
- [widget_update](#canvas.widget_update)

### Canvas.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Canvas.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Canvas.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Canvas.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2220)

### Canvas.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Canvas.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2224)

### Canvas.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Canvas.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Canvas.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Canvas.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Canvas.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Canvas.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2228)

### Canvas.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Checkbox

Checkbox element.

```py
class Checkbox(
    self, text: str="",
    default: bool=False,
    key: Union[str, None] = None,
    enable_events: bool=False,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1447)

### Methods of Checkbox

- [bind](#checkbox.bind)
- [bind_events](#checkbox.bind_events)
- [convert_props](#checkbox.convert_props)
- [create](#checkbox.create)
- [disptach_event](#checkbox.disptach_event)
- [get](#checkbox.get)
- [get_name](#checkbox.get_name)
- [get_prev_widget](#checkbox.get_prev_widget)
- [get_value](#checkbox.get_value)
- [post_create](#checkbox.post_create)
- [prepare_create](#checkbox.prepare_create)
- [set_disabled](#checkbox.set_disabled)
- [set_text](#checkbox.set_text)
- [set_value](#checkbox.set_value)
- [update](#checkbox.update)
- [widget_update](#checkbox.widget_update)

### Checkbox.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Checkbox.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Checkbox.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Checkbox.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1466)

### Checkbox.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Checkbox.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1480)

### Checkbox.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Checkbox.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Checkbox.get_value

Get the value of the widget.

```py
def get_value(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1472)

### Checkbox.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Checkbox.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Checkbox.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Checkbox.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1484)

### Checkbox.set_value

Set the value of the widget.

```py
def set_value(self, b: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1476)

### Checkbox.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1489)

### Checkbox.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## ColorBrowse

FolderBrowse element.

```py
class ColorBrowse(
    self,
    button_text: str="...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    default_color: Union[str, None] = None,
    title: str="",
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2914)

### Methods of ColorBrowse

- [bind](#colorbrowse.bind)
- [bind_events](#colorbrowse.bind_events)
- [convert_props](#colorbrowse.convert_props)
- [create](#colorbrowse.create)
- [disptach_event](#colorbrowse.disptach_event)
- [get](#colorbrowse.get)
- [get_name](#colorbrowse.get_name)
- [get_prev_widget](#colorbrowse.get_prev_widget)
- [post_create](#colorbrowse.post_create)
- [prepare_create](#colorbrowse.prepare_create)
- [set_disabled](#colorbrowse.set_disabled)
- [set_text](#colorbrowse.set_text)
- [show_dialog](#colorbrowse.show_dialog)
- [update](#colorbrowse.update)
- [widget_update](#colorbrowse.widget_update)

### ColorBrowse.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### ColorBrowse.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### ColorBrowse.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### ColorBrowse.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2782)

### ColorBrowse.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### ColorBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

### ColorBrowse.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### ColorBrowse.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### ColorBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### ColorBrowse.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### ColorBrowse.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### ColorBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2822)

### ColorBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2931)

### ColorBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2827)

### ColorBrowse.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Column

Frame element.

```py
class Column(
    self,
    layout: list[list[Element]],
    key: str = "",
    background_color: Union[str, None] = None,
    vertical_alignment: TextVAlign="top",
    size: Union[tuple[int, int], None] = None,
    # text props
    text_align: Union[TextAlign, None]="left", # text align
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1120)

### Methods of Column

- [bind](#column.bind)
- [bind_events](#column.bind_events)
- [convert_props](#column.convert_props)
- [create](#column.create)
- [disptach_event](#column.disptach_event)
- [get](#column.get)
- [get_name](#column.get_name)
- [get_prev_widget](#column.get_prev_widget)
- [post_create](#column.post_create)
- [prepare_create](#column.prepare_create)
- [set_disabled](#column.set_disabled)
- [update](#column.update)
- [widget_update](#column.widget_update)

### Column.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Column.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Column.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Column.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1149)

### Column.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Column.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1154)

### Column.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Column.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Column.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Column.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Column.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Column.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1158)

### Column.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Combo

Combo element.

```py
class Combo(
    self,
    values: list[str]=[],
    default_value: str="",
    key: Union[str, None] = None,
    enable_events: bool = False,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2543)

### Methods of Combo

- [bind](#combo.bind)
- [bind_events](#combo.bind_events)
- [convert_props](#combo.convert_props)
- [create](#combo.create)
- [disptach_event](#combo.disptach_event)
- [get](#combo.get)
- [get_name](#combo.get_name)
- [get_prev_widget](#combo.get_prev_widget)
- [post_create](#combo.post_create)
- [prepare_create](#combo.prepare_create)
- [set_disabled](#combo.set_disabled)
- [set_value](#combo.set_value)
- [set_values](#combo.set_values)
- [update](#combo.update)
- [widget_update](#combo.widget_update)

### Combo.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Combo.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Combo.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Combo.create

[Combo.create] create Listbox widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2562)

### Combo.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Combo.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2579)

### Combo.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Combo.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Combo.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Combo.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Combo.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Combo.set_value

Set the value of the widget.

```py
def set_value(self, v: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2575)

### Combo.set_values

Set values to list

```py
def set_values(self, values: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2569)

### Combo.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2585)

### Combo.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Element

Element class.

```py
class Element(
    self,
    element_type: str, # element type
    ttk_style_name: str, # tkinter widget type
    key: Union[str, None], # key
    has_value: bool, # has value
    metadata: Union[dict[str, Any], None] = None, # meta data
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L744)

### Methods of Element

- [bind](#element.bind)
- [bind_events](#element.bind_events)
- [convert_props](#element.convert_props)
- [create](#element.create)
- [disptach_event](#element.disptach_event)
- [get](#element.get)
- [get_name](#element.get_name)
- [get_prev_widget](#element.get_prev_widget)
- [post_create](#element.post_create)
- [prepare_create](#element.prepare_create)
- [set_disabled](#element.set_disabled)
- [update](#element.update)
- [widget_update](#element.widget_update)

### Element.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Element.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Element.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Element.create

Create a widget.

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Element.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Element.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

### Element.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Element.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Element.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Element.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Element.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Element.update

update widget configuration.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1007)

### Element.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## FileBrowse

FileBrowse element.

```py
class FileBrowse(
    self, button_text: str="...",
    key: Union[str, None] = None,
    title: str = "",
    target_key: Union[str, None] = None,
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    multiple_files: bool = False,
    initial_folder: Union[str, None] = None,
    save_as: bool = False,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2756)

### Methods of FileBrowse

- [bind](#filebrowse.bind)
- [bind_events](#filebrowse.bind_events)
- [convert_props](#filebrowse.convert_props)
- [create](#filebrowse.create)
- [disptach_event](#filebrowse.disptach_event)
- [get](#filebrowse.get)
- [get_name](#filebrowse.get_name)
- [get_prev_widget](#filebrowse.get_prev_widget)
- [post_create](#filebrowse.post_create)
- [prepare_create](#filebrowse.prepare_create)
- [set_disabled](#filebrowse.set_disabled)
- [set_text](#filebrowse.set_text)
- [show_dialog](#filebrowse.show_dialog)
- [update](#filebrowse.update)
- [widget_update](#filebrowse.widget_update)

### FileBrowse.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### FileBrowse.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### FileBrowse.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### FileBrowse.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2782)

### FileBrowse.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### FileBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

### FileBrowse.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### FileBrowse.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### FileBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### FileBrowse.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### FileBrowse.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### FileBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2822)

### FileBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2803)

### FileBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2827)

### FileBrowse.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## FileSaveAs

FileSaveAs element. (alias of FileSaveAsBrowse)

```py
class FileSaveAs(
    self, button_text: str="...",
    key: Union[str, None] = None,
    title: str = "",
    target_key: Union[str, None] = None,
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    multiple_files: bool = False,
    initial_folder: Union[str, None] = None,
    save_as: bool = False,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2756)

### Methods of FileSaveAs

- [bind](#filesaveas.bind)
- [bind_events](#filesaveas.bind_events)
- [convert_props](#filesaveas.convert_props)
- [create](#filesaveas.create)
- [disptach_event](#filesaveas.disptach_event)
- [get](#filesaveas.get)
- [get_name](#filesaveas.get_name)
- [get_prev_widget](#filesaveas.get_prev_widget)
- [post_create](#filesaveas.post_create)
- [prepare_create](#filesaveas.prepare_create)
- [set_disabled](#filesaveas.set_disabled)
- [set_text](#filesaveas.set_text)
- [show_dialog](#filesaveas.show_dialog)
- [update](#filesaveas.update)
- [widget_update](#filesaveas.widget_update)

### FileSaveAs.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### FileSaveAs.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### FileSaveAs.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### FileSaveAs.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2782)

### FileSaveAs.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### FileSaveAs.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

### FileSaveAs.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### FileSaveAs.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### FileSaveAs.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### FileSaveAs.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### FileSaveAs.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### FileSaveAs.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2822)

### FileSaveAs.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2803)

### FileSaveAs.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2827)

### FileSaveAs.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## FileSaveAsBrowse

FileSaveAsBrowse element.

```py
class FileSaveAsBrowse(
    self,
    button_text: str="...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    title: str = "",
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2857)

### Methods of FileSaveAsBrowse

- [bind](#filesaveasbrowse.bind)
- [bind_events](#filesaveasbrowse.bind_events)
- [convert_props](#filesaveasbrowse.convert_props)
- [create](#filesaveasbrowse.create)
- [disptach_event](#filesaveasbrowse.disptach_event)
- [get](#filesaveasbrowse.get)
- [get_name](#filesaveasbrowse.get_name)
- [get_prev_widget](#filesaveasbrowse.get_prev_widget)
- [post_create](#filesaveasbrowse.post_create)
- [prepare_create](#filesaveasbrowse.prepare_create)
- [set_disabled](#filesaveasbrowse.set_disabled)
- [set_text](#filesaveasbrowse.set_text)
- [show_dialog](#filesaveasbrowse.show_dialog)
- [update](#filesaveasbrowse.update)
- [widget_update](#filesaveasbrowse.widget_update)

### FileSaveAsBrowse.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### FileSaveAsBrowse.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### FileSaveAsBrowse.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### FileSaveAsBrowse.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2782)

### FileSaveAsBrowse.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### FileSaveAsBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

### FileSaveAsBrowse.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### FileSaveAsBrowse.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### FileSaveAsBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### FileSaveAsBrowse.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### FileSaveAsBrowse.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### FileSaveAsBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2822)

### FileSaveAsBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2803)

### FileSaveAsBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2827)

### FileSaveAsBrowse.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## FilesBrowse

FilesBrowse element.

```py
class FilesBrowse(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    title: str="",
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2835)

### Methods of FilesBrowse

- [bind](#filesbrowse.bind)
- [bind_events](#filesbrowse.bind_events)
- [convert_props](#filesbrowse.convert_props)
- [create](#filesbrowse.create)
- [disptach_event](#filesbrowse.disptach_event)
- [get](#filesbrowse.get)
- [get_name](#filesbrowse.get_name)
- [get_prev_widget](#filesbrowse.get_prev_widget)
- [post_create](#filesbrowse.post_create)
- [prepare_create](#filesbrowse.prepare_create)
- [set_disabled](#filesbrowse.set_disabled)
- [set_text](#filesbrowse.set_text)
- [show_dialog](#filesbrowse.show_dialog)
- [update](#filesbrowse.update)
- [widget_update](#filesbrowse.widget_update)

### FilesBrowse.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### FilesBrowse.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### FilesBrowse.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### FilesBrowse.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2782)

### FilesBrowse.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### FilesBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

### FilesBrowse.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### FilesBrowse.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### FilesBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### FilesBrowse.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### FilesBrowse.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### FilesBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2822)

### FilesBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2803)

### FilesBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2827)

### FilesBrowse.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## FolderBrowse

FolderBrowse element.

```py
class FolderBrowse(
    self,
    button_text: str="...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    default_path: Union[str, None] = None,
    title: str = "",
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2883)

### Methods of FolderBrowse

- [bind](#folderbrowse.bind)
- [bind_events](#folderbrowse.bind_events)
- [convert_props](#folderbrowse.convert_props)
- [create](#folderbrowse.create)
- [disptach_event](#folderbrowse.disptach_event)
- [get](#folderbrowse.get)
- [get_name](#folderbrowse.get_name)
- [get_prev_widget](#folderbrowse.get_prev_widget)
- [post_create](#folderbrowse.post_create)
- [prepare_create](#folderbrowse.prepare_create)
- [set_disabled](#folderbrowse.set_disabled)
- [set_text](#folderbrowse.set_text)
- [show_dialog](#folderbrowse.show_dialog)
- [update](#folderbrowse.update)
- [widget_update](#folderbrowse.widget_update)

### FolderBrowse.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### FolderBrowse.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### FolderBrowse.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### FolderBrowse.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2782)

### FolderBrowse.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### FolderBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

### FolderBrowse.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### FolderBrowse.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### FolderBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### FolderBrowse.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### FolderBrowse.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### FolderBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2822)

### FolderBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2900)

### FolderBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2827)

### FolderBrowse.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Frame

Frame element.

```py
class Frame(
    self,
    title: str,
    layout: list[list[Element]],
    key: str = "",
    size: Union[tuple[int, int], None] = None,
    relief: ReliefType="groove",
    # text props
    font: Union[FontType, None] = None, # font
    color: Union[str, None] = None,
    text_color: Union[str, None] = None,
    background_color: Union[str, None] = None,
    label_outside: bool=False,
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    use_ttk: bool=False,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1057)

### Methods of Frame

- [bind](#frame.bind)
- [bind_events](#frame.bind_events)
- [convert_props](#frame.convert_props)
- [create](#frame.create)
- [disptach_event](#frame.disptach_event)
- [get](#frame.get)
- [get_name](#frame.get_name)
- [get_prev_widget](#frame.get_prev_widget)
- [post_create](#frame.post_create)
- [prepare_create](#frame.prepare_create)
- [set_disabled](#frame.set_disabled)
- [update](#frame.update)
- [widget_update](#frame.widget_update)

### Frame.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Frame.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Frame.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Frame.create

Create a Frame widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1092)

### Frame.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Frame.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1104)

### Frame.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Frame.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Frame.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Frame.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Frame.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Frame.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1108)

### Frame.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Graph

Graph element.

```py
class Graph(
    self, key: Union[str, None] = None,
    background_color: Union[str, None] = None,
    size: tuple[int, int]=(300, 300),
    canvas_size: Union[tuple[int, int], None] = None,
    graph_bottom_left: Union[tuple[int, int], None] = None,
    graph_top_right: Union[tuple[int, int], None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2240)

### Methods of Graph

- [bind](#graph.bind)
- [bind_events](#graph.bind_events)
- [convert_props](#graph.convert_props)
- [create](#graph.create)
- [disptach_event](#graph.disptach_event)
- [draw_arc](#graph.draw_arc)
- [draw_circle](#graph.draw_circle)
- [draw_image](#graph.draw_image)
- [draw_line](#graph.draw_line)
- [draw_lines](#graph.draw_lines)
- [draw_oval](#graph.draw_oval)
- [draw_point](#graph.draw_point)
- [draw_polygon](#graph.draw_polygon)
- [draw_rectangle](#graph.draw_rectangle)
- [draw_text](#graph.draw_text)
- [erase](#graph.erase)
- [get](#graph.get)
- [get_name](#graph.get_name)
- [get_prev_widget](#graph.get_prev_widget)
- [post_create](#graph.post_create)
- [prepare_create](#graph.prepare_create)
- [set_disabled](#graph.set_disabled)
- [update](#graph.update)
- [widget_update](#graph.widget_update)

### Graph.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Graph.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Graph.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Graph.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2265)

### Graph.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Graph.draw_arc

Draw an arc.

```py
def draw_arc(self, top_left: PointType, bottom_right: PointType, extent: Union[int, None] = None, start_angle: Union[int, None] = None, style: Union[str, None] = None, arc_color: Union[str, None] = 'black', line_width: int = 1, fill_color: Union[str, None] = None) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2307)

### Graph.draw_circle

Draw a circle.

```py
def draw_circle(self, center_location: PointType, radius: Union[int, float], fill_color: Union[str, None] = None, line_color: Union[str, None] = 'black', line_width: int = 1) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2298)

### Graph.draw_image

Draw image

```py
def draw_image(self, filename: Union[str, None] = None, data: Union[bytes, None] = None, location: Union[PointType, None] = None) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2329)

### Graph.draw_line

Draw a line.

```py
def draw_line(self, point_from: PointType, point_to: PointType, color: str = 'black', width: int = 1) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2284)

### Graph.draw_lines

Draw lines.

```py
def draw_lines(self, points: list[PointType], color='black', width=1) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2288)

### Graph.draw_oval

Draw an oval.

```py
def draw_oval(self, top_left: PointType, bottom_right: PointType, fill_color: Union[str, None] = None, line_color: Union[str, None] = None, line_width: int = 1):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2303)

### Graph.draw_point

Draw a point.

```py
def draw_point(self, point: PointType, size: int = 2, color: str = 'black') -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2292)

### Graph.draw_polygon

Draw polygon

```py
def draw_polygon(self, points: list[PointType], fill_color: Union[str, None] = None, line_color: Union[str, None] = None, line_width: Union[int, None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2319)

### Graph.draw_rectangle

Draw rectangle

```py
def draw_rectangle(self, top_left: PointType, bottom_right: PointType, fill_color: Union[str, None] = None, line_color: Union[str, None] = None, line_width: Union[int, None] = None) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2315)

### Graph.draw_text

Draw text

```py
def draw_text(self, text: str, location: PointType, color: Union[str, None]='black', font: FontType = None, angle: Union[float, str, None] = 0, text_location: TextAlign = tk.CENTER) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2323)

### Graph.erase

Delete all

```py
def erase(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2311)

### Graph.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2270)

### Graph.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Graph.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Graph.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Graph.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Graph.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Graph.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2274)

### Graph.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## HSeparator

HSeparator element.

```py
class HSeparator(
    self,
    key: Union[str, None] = None,
    background_color: Union[str, None] = None,
    pad: PadType = 5,
    size: tuple[int, int] = (100, 5),
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2442)

### Methods of HSeparator

- [bind](#hseparator.bind)
- [bind_events](#hseparator.bind_events)
- [convert_props](#hseparator.convert_props)
- [create](#hseparator.create)
- [disptach_event](#hseparator.disptach_event)
- [get](#hseparator.get)
- [get_name](#hseparator.get_name)
- [get_prev_widget](#hseparator.get_prev_widget)
- [post_create](#hseparator.post_create)
- [prepare_create](#hseparator.prepare_create)
- [set_disabled](#hseparator.set_disabled)
- [update](#hseparator.update)
- [widget_update](#hseparator.widget_update)

### HSeparator.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### HSeparator.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### HSeparator.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### HSeparator.create

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2460)

### HSeparator.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### HSeparator.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

### HSeparator.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### HSeparator.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### HSeparator.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### HSeparator.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### HSeparator.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### HSeparator.update

update widget configuration.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1007)

### HSeparator.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Image

Image element.

```py
class Image(
    self,
    source: Union[bytes, str, None] = None, # image source
    filename = None, # filen ame
    data: bytes = None, # image data
    key: Union[str, None] = None,
    background_color: Union[str, None] = None,
    size: tuple[int, int] = (300, 300),
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2342)

### Methods of Image

- [bind](#image.bind)
- [bind_events](#image.bind_events)
- [convert_props](#image.convert_props)
- [create](#image.create)
- [disptach_event](#image.disptach_event)
- [erase](#image.erase)
- [get](#image.get)
- [get_name](#image.get_name)
- [get_prev_widget](#image.get_prev_widget)
- [post_create](#image.post_create)
- [prepare_create](#image.prepare_create)
- [set_disabled](#image.set_disabled)
- [set_image](#image.set_image)
- [update](#image.update)
- [widget_update](#image.widget_update)

### Image.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Image.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Image.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Image.create

Create a Image widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2362)

### Image.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Image.erase

Erase image

```py
def erase(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2375)

### Image.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2371)

### Image.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Image.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Image.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Image.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Image.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Image.set_image

```py
def set_image(self,
    source: Union[bytes, str, None] = None,
    filename: Union[str, None] = None,
    data: Union[bytes, None]=None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2379)

### Image.update

Update the widget.

```py
def update(self,
    source: Union[bytes, str, None] = None,
    filename: Union[str, None] = None,
    data: Union[bytes, None] = None,
    size: Union[tuple[int,int], None] = None,
    **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2396)

### Image.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Input

Text input element.

```py
class Input(
    self,
    text: str = "", # default text
    key: Union[str, None] = None, # key
    default_text: Union[str, None] = None, # same as text
    enable_events: bool = False, # enabled events ([enter] or [change])
    enable_key_events: bool = False,  # enabled key events
    enable_focus_events: bool = False, # enabled focus events
    readonly_background_color: Union[str, None] = "silver",
    password_char: Union[str, None] = None, # if you want to use it as a password input box, set "*"
    readonly: bool = False, # read only box
    # text props
    text_align: Union[TextAlign, None] = "left", # text align
    font: Union[FontType, None] = None, # font
    color: Union[str, None] = None, # text color
    text_color: Union[str, None] = None, # same as color
    background_color: Union[str, None] = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### Methods of Input

- [bind](#input.bind)
- [bind_events](#input.bind_events)
- [convert_props](#input.convert_props)
- [copy](#input.copy)
- [copy_selected_text](#input.copy_selected_text)
- [create](#input.create)
- [cut](#input.cut)
- [delete_selected](#input.delete_selected)
- [disptach_event](#input.disptach_event)
- [get](#input.get)
- [get_cursor_pos](#input.get_cursor_pos)
- [get_name](#input.get_name)
- [get_prev_widget](#input.get_prev_widget)
- [get_selected_text](#input.get_selected_text)
- [get_selection_length](#input.get_selection_length)
- [get_selection_pos](#input.get_selection_pos)
- [get_selection_start](#input.get_selection_start)
- [get_text](#input.get_text)
- [paste](#input.paste)
- [post_create](#input.post_create)
- [prepare_create](#input.prepare_create)
- [select_all](#input.select_all)
- [set_cursor_pos](#input.set_cursor_pos)
- [set_disabled](#input.set_disabled)
- [set_readonly](#input.set_readonly)
- [set_selection_start](#input.set_selection_start)
- [set_text](#input.set_text)
- [update](#input.update)
- [widget_update](#input.widget_update)

### Input.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Input.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Input.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Input.copy

copy to clipboard

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1718)

### Input.copy_selected_text

Copy selected text

```py
def copy_selected_text(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1681)

### Input.create

create Input widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1631)

### Input.cut

cut to clipboard

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1726)

### Input.delete_selected

delete selected text

```py
def delete_selected(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1733)

### Input.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Input.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1653)

### Input.get_cursor_pos

get cursor position

```py
def get_cursor_pos(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1767)

### Input.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Input.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Input.get_selected_text

get selected text

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1672)

### Input.get_selection_length

get selection length

```py
def get_selection_length(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1785)

### Input.get_selection_pos

get selection positions

```py
def get_selection_pos(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1756)

### Input.get_selection_start

get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1776)

### Input.get_text

get text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1668)

### Input.paste

paste from clipboard

```py
def paste(self):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1744)

### Input.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Input.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Input.select_all

select_all

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1710)

### Input.set_cursor_pos

set cursor position

```py
def set_cursor_pos(self, index: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1772)

### Input.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Input.set_readonly

set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Input.set_selection_start

set selection start and length

```py
def set_selection_start(self, sel_start: int, sel_length: int=0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1795)

### Input.set_text

set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1657)

### Input.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1692)

### Input.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## InputText

InputText element. (alias of Input)

```py
class InputText(
    self,
    text: str = "", # default text
    key: Union[str, None] = None, # key
    default_text: Union[str, None] = None, # same as text
    enable_events: bool = False, # enabled events ([enter] or [change])
    enable_key_events: bool = False,  # enabled key events
    enable_focus_events: bool = False, # enabled focus events
    readonly_background_color: Union[str, None] = "silver",
    password_char: Union[str, None] = None, # if you want to use it as a password input box, set "*"
    readonly: bool = False, # read only box
    # text props
    text_align: Union[TextAlign, None] = "left", # text align
    font: Union[FontType, None] = None, # font
    color: Union[str, None] = None, # text color
    text_color: Union[str, None] = None, # same as color
    background_color: Union[str, None] = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### Methods of InputText

- [bind](#inputtext.bind)
- [bind_events](#inputtext.bind_events)
- [convert_props](#inputtext.convert_props)
- [copy](#inputtext.copy)
- [copy_selected_text](#inputtext.copy_selected_text)
- [create](#inputtext.create)
- [cut](#inputtext.cut)
- [delete_selected](#inputtext.delete_selected)
- [disptach_event](#inputtext.disptach_event)
- [get](#inputtext.get)
- [get_cursor_pos](#inputtext.get_cursor_pos)
- [get_name](#inputtext.get_name)
- [get_prev_widget](#inputtext.get_prev_widget)
- [get_selected_text](#inputtext.get_selected_text)
- [get_selection_length](#inputtext.get_selection_length)
- [get_selection_pos](#inputtext.get_selection_pos)
- [get_selection_start](#inputtext.get_selection_start)
- [get_text](#inputtext.get_text)
- [paste](#inputtext.paste)
- [post_create](#inputtext.post_create)
- [prepare_create](#inputtext.prepare_create)
- [select_all](#inputtext.select_all)
- [set_cursor_pos](#inputtext.set_cursor_pos)
- [set_disabled](#inputtext.set_disabled)
- [set_readonly](#inputtext.set_readonly)
- [set_selection_start](#inputtext.set_selection_start)
- [set_text](#inputtext.set_text)
- [update](#inputtext.update)
- [widget_update](#inputtext.widget_update)

### InputText.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### InputText.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### InputText.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### InputText.copy

copy to clipboard

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1718)

### InputText.copy_selected_text

Copy selected text

```py
def copy_selected_text(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1681)

### InputText.create

create Input widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1631)

### InputText.cut

cut to clipboard

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1726)

### InputText.delete_selected

delete selected text

```py
def delete_selected(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1733)

### InputText.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### InputText.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1653)

### InputText.get_cursor_pos

get cursor position

```py
def get_cursor_pos(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1767)

### InputText.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### InputText.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### InputText.get_selected_text

get selected text

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1672)

### InputText.get_selection_length

get selection length

```py
def get_selection_length(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1785)

### InputText.get_selection_pos

get selection positions

```py
def get_selection_pos(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1756)

### InputText.get_selection_start

get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1776)

### InputText.get_text

get text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1668)

### InputText.paste

paste from clipboard

```py
def paste(self):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1744)

### InputText.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### InputText.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### InputText.select_all

select_all

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1710)

### InputText.set_cursor_pos

set cursor position

```py
def set_cursor_pos(self, index: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1772)

### InputText.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### InputText.set_readonly

set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### InputText.set_selection_start

set selection start and length

```py
def set_selection_start(self, sel_start: int, sel_length: int=0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1795)

### InputText.set_text

set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1657)

### InputText.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1692)

### InputText.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Label

Label element (alias of Text)

```py
class Label(
    self,
    text: str = "",
    key: Union[str, None] = None,
    enable_events: bool=False, # enabled events (click)
    wrap_length: Union[int, None] = None, # wrap length(unit=pixel)
    # text props
    text_align: Union[TextAlign, None]="left", # text align
    font: Union[FontType, None] = None, # font
    color: Union[str, None] = None, # text color
    text_color: Union[str, None] = None, # same as color
    background_color: Union[str, None] = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None, # user metadata
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1170)

### Methods of Label

- [bind](#label.bind)
- [bind_events](#label.bind_events)
- [convert_props](#label.convert_props)
- [create](#label.create)
- [disptach_event](#label.disptach_event)
- [get](#label.get)
- [get_name](#label.get_name)
- [get_prev_widget](#label.get_prev_widget)
- [get_text](#label.get_text)
- [post_create](#label.post_create)
- [prepare_create](#label.prepare_create)
- [set_disabled](#label.set_disabled)
- [set_text](#label.set_text)
- [update](#label.update)
- [widget_update](#label.widget_update)

### Label.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Label.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Label.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Label.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1199)

### Label.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Label.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1210)

### Label.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Label.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Label.get_text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1214)

### Label.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Label.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Label.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Label.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1217)

### Label.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1222)

### Label.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Listbox

Listbox element.

```py
class Listbox(
    self,
    values: list[str] = [],
    default_values: list[str] = [],
    key: Union[str, None] = None,
    enable_events: bool = False,
    select_mode: ListboxSelectMode = LISTBOX_SELECT_MODE_BROWSE,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2467)

### Methods of Listbox

- [bind](#listbox.bind)
- [bind_events](#listbox.bind_events)
- [convert_props](#listbox.convert_props)
- [create](#listbox.create)
- [disptach_event](#listbox.disptach_event)
- [get](#listbox.get)
- [get_name](#listbox.get_name)
- [get_prev_widget](#listbox.get_prev_widget)
- [post_create](#listbox.post_create)
- [prepare_create](#listbox.prepare_create)
- [select_values](#listbox.select_values)
- [set_disabled](#listbox.set_disabled)
- [set_values](#listbox.set_values)
- [update](#listbox.update)
- [widget_update](#listbox.widget_update)

### Listbox.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Listbox.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Listbox.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Listbox.create

[Listbox.create] create Listbox widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2487)

### Listbox.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Listbox.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2517)

### Listbox.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Listbox.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Listbox.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Listbox.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Listbox.select_values

Select values

```py
def select_values(self, values: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2496)

### Listbox.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Listbox.set_values

Set values to list

```py
def set_values(self, values: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2507)

### Listbox.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2530)

### Listbox.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Menu

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
- "label::-event_name-" is set event name
- "---" is separator

```py
class Menu(
    self,
    items: Union[Any, None] = None,
    menu_definition: Union[list[list[Union[str,list[Any]]]], None] = None,
    key: Union[str, None] = None,
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1249)

### Methods of Menu

- [bind](#menu.bind)
- [bind_events](#menu.bind_events)
- [convert_props](#menu.convert_props)
- [create](#menu.create)
- [disptach_event](#menu.disptach_event)
- [get](#menu.get)
- [get_name](#menu.get_name)
- [get_prev_widget](#menu.get_prev_widget)
- [get_text](#menu.get_text)
- [post_create](#menu.post_create)
- [prepare_create](#menu.prepare_create)
- [set_disabled](#menu.set_disabled)
- [set_text](#menu.set_text)
- [update](#menu.update)
- [widget_update](#menu.widget_update)

### Menu.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Menu.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Menu.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Menu.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1261)

### Menu.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Menu.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1314)

### Menu.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Menu.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Menu.get_text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1318)

### Menu.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Menu.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Menu.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Menu.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Menu.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1326)

### Menu.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Multiline

Multiline text input element.

```py
class Multiline(
    self,
    text: str = "", # default text
    default_text: Union[str, None] = None, # same as text
    key: Union[str, None] = None, # key
    readonly: bool = False,
    enable_events: bool = False,
    enable_key_events: bool = False,
    enable_focus_events: bool = False,
    size: tuple[int, int] = (50, 10), # element size (unit=character)
    # text props
    font: Union[FontType, None] = None, # font
    color: Union[str, None] = None, # text color
    text_color: Union[str, None] = None, # same as color
    background_color: Union[str, None] = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    readonly_background_color: Union[str, None] = None,
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1810)

### Methods of Multiline

- [bind](#multiline.bind)
- [bind_events](#multiline.bind_events)
- [convert_props](#multiline.convert_props)
- [copy](#multiline.copy)
- [create](#multiline.create)
- [cut](#multiline.cut)
- [disptach_event](#multiline.disptach_event)
- [get](#multiline.get)
- [get_cursor_pos](#multiline.get_cursor_pos)
- [get_name](#multiline.get_name)
- [get_prev_widget](#multiline.get_prev_widget)
- [get_selected_text](#multiline.get_selected_text)
- [get_selection_length](#multiline.get_selection_length)
- [get_selection_pos](#multiline.get_selection_pos)
- [get_selection_start](#multiline.get_selection_start)
- [get_text](#multiline.get_text)
- [index_to_pos](#multiline.index_to_pos)
- [paste](#multiline.paste)
- [pos_to_index](#multiline.pos_to_index)
- [post_create](#multiline.post_create)
- [prepare_create](#multiline.prepare_create)
- [print](#multiline.print)
- [select_all](#multiline.select_all)
- [set_cursor_pos](#multiline.set_cursor_pos)
- [set_disabled](#multiline.set_disabled)
- [set_readonly](#multiline.set_readonly)
- [set_selection_pos](#multiline.set_selection_pos)
- [set_selection_start](#multiline.set_selection_start)
- [set_text](#multiline.set_text)
- [update](#multiline.update)
- [widget_update](#multiline.widget_update)

### Multiline.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Multiline.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Multiline.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Multiline.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1898)

### Multiline.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1862)

### Multiline.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1915)

### Multiline.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Multiline.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1875)

### Multiline.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2006)

### Multiline.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Multiline.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Multiline.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1888)

### Multiline.get_selection_length

get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2042)

### Multiline.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1951)

### Multiline.get_selection_start

get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2022)

### Multiline.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1881)

### Multiline.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1988)

### Multiline.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1906)

### Multiline.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1973)

### Multiline.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Multiline.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Multiline.print

Print text.

```py
def print(self, text: str, text_color: Union[str, None] = None, background_color: Union[str, None] = None, end:str="\n") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2061)

### Multiline.select_all

select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2052)

### Multiline.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2016)

### Multiline.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Multiline.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1933)

### Multiline.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### Multiline.set_selection_start

set selection start

```py
def set_selection_start(self, index: int, sel_length: int=0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2033)

### Multiline.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1939)

### Multiline.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1925)

### Multiline.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Output

Output element. (alias of Multiline) TODO: implement

```py
class Output(
    self,
    text: str = "", # default text
    default_text: Union[str, None] = None, # same as text
    key: Union[str, None] = None, # key
    readonly: bool = False,
    enable_events: bool = False,
    enable_key_events: bool = False,
    enable_focus_events: bool = False,
    size: tuple[int, int] = (50, 10), # element size (unit=character)
    # text props
    font: Union[FontType, None] = None, # font
    color: Union[str, None] = None, # text color
    text_color: Union[str, None] = None, # same as color
    background_color: Union[str, None] = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    readonly_background_color: Union[str, None] = None,
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1810)

### Methods of Output

- [bind](#output.bind)
- [bind_events](#output.bind_events)
- [convert_props](#output.convert_props)
- [copy](#output.copy)
- [create](#output.create)
- [cut](#output.cut)
- [disptach_event](#output.disptach_event)
- [get](#output.get)
- [get_cursor_pos](#output.get_cursor_pos)
- [get_name](#output.get_name)
- [get_prev_widget](#output.get_prev_widget)
- [get_selected_text](#output.get_selected_text)
- [get_selection_length](#output.get_selection_length)
- [get_selection_pos](#output.get_selection_pos)
- [get_selection_start](#output.get_selection_start)
- [get_text](#output.get_text)
- [index_to_pos](#output.index_to_pos)
- [paste](#output.paste)
- [pos_to_index](#output.pos_to_index)
- [post_create](#output.post_create)
- [prepare_create](#output.prepare_create)
- [print](#output.print)
- [select_all](#output.select_all)
- [set_cursor_pos](#output.set_cursor_pos)
- [set_disabled](#output.set_disabled)
- [set_readonly](#output.set_readonly)
- [set_selection_pos](#output.set_selection_pos)
- [set_selection_start](#output.set_selection_start)
- [set_text](#output.set_text)
- [update](#output.update)
- [widget_update](#output.widget_update)

### Output.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Output.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Output.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Output.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1898)

### Output.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1862)

### Output.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1915)

### Output.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Output.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1875)

### Output.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2006)

### Output.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Output.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Output.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1888)

### Output.get_selection_length

get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2042)

### Output.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1951)

### Output.get_selection_start

get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2022)

### Output.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1881)

### Output.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1988)

### Output.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1906)

### Output.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1973)

### Output.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Output.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Output.print

Print text.

```py
def print(self, text: str, text_color: Union[str, None] = None, background_color: Union[str, None] = None, end:str="\n") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2061)

### Output.select_all

select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2052)

### Output.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2016)

### Output.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Output.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1933)

### Output.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### Output.set_selection_start

set selection start

```py
def set_selection_start(self, index: int, sel_length: int=0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2033)

### Output.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1939)

### Output.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1925)

### Output.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Radio

Checkbox element.

```py
class Radio(
    self, text: str="",
    group_id: Union[int, str] = "group",
    default: bool = False,
    key: Union[str, None] = None,
    enable_events: bool = False,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1503)

### Methods of Radio

- [bind](#radio.bind)
- [bind_events](#radio.bind_events)
- [convert_props](#radio.convert_props)
- [create](#radio.create)
- [disptach_event](#radio.disptach_event)
- [get](#radio.get)
- [get_name](#radio.get_name)
- [get_prev_widget](#radio.get_prev_widget)
- [get_value](#radio.get_value)
- [is_selected](#radio.is_selected)
- [post_create](#radio.post_create)
- [prepare_create](#radio.prepare_create)
- [select](#radio.select)
- [set_disabled](#radio.set_disabled)
- [set_text](#radio.set_text)
- [update](#radio.update)
- [widget_update](#radio.widget_update)

### Radio.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Radio.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Radio.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Radio.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Radio.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Radio.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1556)

### Radio.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Radio.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Radio.get_value

Get the value of the widget.

```py
def get_value(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1552)

### Radio.is_selected

Check if the radio button is selected.

```py
def is_selected(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1548)

### Radio.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Radio.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Radio.select

Select the radio button.

```py
def select(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1544)

### Radio.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Radio.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1560)

### Radio.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1565)

### Radio.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Slider

Slider element.

```py
class Slider(
    self,
    range: tuple[float, float] = (1, 10), # value range (from, to)
    default_value: Union[float, None] = None, # default value
    resolution: Union[float, None] = None, # value resolution
    orientation: OrientationType = "horizontal", # orientation (h|v|horizontal|vertical)
    tick_interval: Union[float, None] = None, # tick marks interval on the scale
    enable_events: bool = False, # enable changing events
    enable_changed_events: bool = False, # enable changed event
    disable_number_display: bool = False, # hide number display
    size: Union[tuple[int, int], None] = None, # size (unit: character) / horizontal: (bar_length, thumb_size), vertical: (thumb_size, bar_length)
    key: Union[str, None] = None,
    # other
    default: Union[float, None] = None, # same as default_value
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2087)

### Methods of Slider

- [bind](#slider.bind)
- [bind_events](#slider.bind_events)
- [convert_props](#slider.convert_props)
- [create](#slider.create)
- [disptach_event](#slider.disptach_event)
- [get](#slider.get)
- [get_name](#slider.get_name)
- [get_prev_widget](#slider.get_prev_widget)
- [get_range](#slider.get_range)
- [post_create](#slider.post_create)
- [prepare_create](#slider.prepare_create)
- [set](#slider.set)
- [set_disabled](#slider.set_disabled)
- [set_range](#slider.set_range)
- [update](#slider.update)
- [widget_update](#slider.widget_update)

### Slider.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Slider.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Slider.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Slider.create

Create the widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2136)

### Slider.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Slider.get

Return slider value.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2167)

### Slider.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Slider.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Slider.get_range

```py
def get_range(self) -> tuple[float, float]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2179)

### Slider.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Slider.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Slider.set

Set value of Slider

```py
def set(self, value: float) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2171)

### Slider.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Slider.set_range

Set the range of the slider.

```py
def set_range(self, from_: float, to: float) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2175)

### Slider.update

Update the widget.

```py
def update(self,
    value: Union[float, None]=None,
    range: Union[tuple[float, float], None]=None,
    disable_number_display: Union[bool, None]=None,
    **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2182)

### Slider.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Submit

Subtmi element. (Alias of Button) : todo: add submit event

```py
class Submit(
    self,
    button_text: str = "",
    key: Union[str, None] = None,
    disabled: bool = None,
    size: Union[tuple[int, int], None] = None,
    use_ttk_buttons: Union[bool, None] = None,
    tooltip: Union[str, None] = None, # (TODO) tooltip
    button_color: Union[str, tuple[str, str], None] = None,
    # text props
    text_align: Union[TextAlign, None] = "left", # text align
    font: Union[FontType, None] = None, # font
    color: Union[str, None] = None, # text color
    text_color: Union[str, None] = None, # same as color
    background_color: Union[str, None] = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1334)

### Methods of Submit

- [bind](#submit.bind)
- [bind_events](#submit.bind_events)
- [convert_props](#submit.convert_props)
- [create](#submit.create)
- [disptach_event](#submit.disptach_event)
- [get](#submit.get)
- [get_name](#submit.get_name)
- [get_prev_widget](#submit.get_prev_widget)
- [get_text](#submit.get_text)
- [post_create](#submit.post_create)
- [prepare_create](#submit.prepare_create)
- [set_button_color](#submit.set_button_color)
- [set_disabled](#submit.set_disabled)
- [set_text](#submit.set_text)
- [update](#submit.update)
- [widget_update](#submit.widget_update)

### Submit.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Submit.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Submit.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Submit.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1377)

### Submit.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Submit.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1404)

### Submit.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Submit.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Submit.get_text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1413)

### Submit.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Submit.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Submit.set_button_color

Set the button color.

```py
def set_button_color(self, button_color: Union[str, tuple[str,str]], update: bool = True) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1390)

### Submit.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Submit.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1408)

### Submit.update

Update the widget.

```py
def update(self,
    text: Union[str, None] = None,
    disabled: Union[bool, None] = None,
    button_color: Union[str, tuple[str,str], None] = None,
    **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1416)

### Submit.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Table

Table element.

```py
class Table(
    self,
    values: list[list[str]] = [],
    headings: list[str] = [],
    key: Union[str, None] = None,
    justification: TextAlign = "center",
    auto_size_columns: bool = True,
    max_col_width: int = 0,
    col_widths: Union[list[int], None] = None,
    enable_events: bool = False,
    event_returns_values: Union[bool, None] = None, # Returns the table value if set to True, otherwise returns the index.
    select_mode: str="browse",
    # text props
    text_align: Union[TextAlign, None] = "left", # text align
    font: Union[FontType, None] = None, # font
    color: Union[str, None] = None, # text color
    text_color: Union[str, None] = None, # same as color
    background_color: Union[str, None] = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2599)

### Methods of Table

- [bind](#table.bind)
- [bind_events](#table.bind_events)
- [convert_props](#table.convert_props)
- [create](#table.create)
- [disptach_event](#table.disptach_event)
- [get](#table.get)
- [get_name](#table.get_name)
- [get_prev_widget](#table.get_prev_widget)
- [post_create](#table.post_create)
- [prepare_create](#table.prepare_create)
- [set_disabled](#table.set_disabled)
- [set_values](#table.set_values)
- [update](#table.update)
- [widget_update](#table.widget_update)

### Table.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Table.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Table.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Table.create

Create a Table widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2658)

### Table.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Table.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2717)

### Table.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Table.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Table.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Table.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Table.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Table.set_values

Set values to the table.

```py
def set_values(self, values: list[list[str]], headings: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2702)

### Table.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2734)

### Table.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Text

Text element.

```py
class Text(
    self,
    text: str = "",
    key: Union[str, None] = None,
    enable_events: bool=False, # enabled events (click)
    wrap_length: Union[int, None] = None, # wrap length(unit=pixel)
    # text props
    text_align: Union[TextAlign, None]="left", # text align
    font: Union[FontType, None] = None, # font
    color: Union[str, None] = None, # text color
    text_color: Union[str, None] = None, # same as color
    background_color: Union[str, None] = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None, # user metadata
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1170)

### Methods of Text

- [bind](#text.bind)
- [bind_events](#text.bind_events)
- [convert_props](#text.convert_props)
- [create](#text.create)
- [disptach_event](#text.disptach_event)
- [get](#text.get)
- [get_name](#text.get_name)
- [get_prev_widget](#text.get_prev_widget)
- [get_text](#text.get_text)
- [post_create](#text.post_create)
- [prepare_create](#text.prepare_create)
- [set_disabled](#text.set_disabled)
- [set_text](#text.set_text)
- [update](#text.update)
- [widget_update](#text.widget_update)

### Text.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Text.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Text.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Text.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1199)

### Text.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Text.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1210)

### Text.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Text.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Text.get_text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1214)

### Text.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Text.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Text.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Text.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1217)

### Text.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1222)

### Text.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Textarea

Textarea element. (alias of Multiline)

```py
class Textarea(
    self,
    text: str = "", # default text
    default_text: Union[str, None] = None, # same as text
    key: Union[str, None] = None, # key
    readonly: bool = False,
    enable_events: bool = False,
    enable_key_events: bool = False,
    enable_focus_events: bool = False,
    size: tuple[int, int] = (50, 10), # element size (unit=character)
    # text props
    font: Union[FontType, None] = None, # font
    color: Union[str, None] = None, # text color
    text_color: Union[str, None] = None, # same as color
    background_color: Union[str, None] = None, # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    readonly_background_color: Union[str, None] = None,
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1810)

### Methods of Textarea

- [bind](#textarea.bind)
- [bind_events](#textarea.bind_events)
- [convert_props](#textarea.convert_props)
- [copy](#textarea.copy)
- [create](#textarea.create)
- [cut](#textarea.cut)
- [disptach_event](#textarea.disptach_event)
- [get](#textarea.get)
- [get_cursor_pos](#textarea.get_cursor_pos)
- [get_name](#textarea.get_name)
- [get_prev_widget](#textarea.get_prev_widget)
- [get_selected_text](#textarea.get_selected_text)
- [get_selection_length](#textarea.get_selection_length)
- [get_selection_pos](#textarea.get_selection_pos)
- [get_selection_start](#textarea.get_selection_start)
- [get_text](#textarea.get_text)
- [index_to_pos](#textarea.index_to_pos)
- [paste](#textarea.paste)
- [pos_to_index](#textarea.pos_to_index)
- [post_create](#textarea.post_create)
- [prepare_create](#textarea.prepare_create)
- [print](#textarea.print)
- [select_all](#textarea.select_all)
- [set_cursor_pos](#textarea.set_cursor_pos)
- [set_disabled](#textarea.set_disabled)
- [set_readonly](#textarea.set_readonly)
- [set_selection_pos](#textarea.set_selection_pos)
- [set_selection_start](#textarea.set_selection_start)
- [set_text](#textarea.set_text)
- [update](#textarea.update)
- [widget_update](#textarea.widget_update)

### Textarea.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Textarea.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### Textarea.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### Textarea.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1898)

### Textarea.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1862)

### Textarea.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1915)

### Textarea.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Textarea.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1875)

### Textarea.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2006)

### Textarea.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Textarea.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### Textarea.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1888)

### Textarea.get_selection_length

get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2042)

### Textarea.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1951)

### Textarea.get_selection_start

get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2022)

### Textarea.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1881)

### Textarea.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1988)

### Textarea.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1906)

### Textarea.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1973)

### Textarea.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Textarea.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### Textarea.print

Print text.

```py
def print(self, text: str, text_color: Union[str, None] = None, background_color: Union[str, None] = None, end:str="\n") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2061)

### Textarea.select_all

select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2052)

### Textarea.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2016)

### Textarea.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Textarea.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1933)

### Textarea.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### Textarea.set_selection_start

set selection start

```py
def set_selection_start(self, index: int, sel_length: int=0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2033)

### Textarea.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1939)

### Textarea.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1925)

### Textarea.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## TkEasyError



```py
class TkEasyError(self, message="TkEasyError"):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L120)

### Methods of TkEasyError



### TkEasyError.args

### TkEasyError.with_traceback

Exception.with_traceback(tb) --
    set self.__traceback__ to tb and return self.

## VSeparator

VSeparator element.

```py
class VSeparator(
    self,
    key: Union[str, None] = None,
    background_color: Union[str, None] = None,
    pad: PadType = 5,
    size: tuple[int, int]=(5, 100),
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2418)

### Methods of VSeparator

- [bind](#vseparator.bind)
- [bind_events](#vseparator.bind_events)
- [convert_props](#vseparator.convert_props)
- [create](#vseparator.create)
- [disptach_event](#vseparator.disptach_event)
- [get](#vseparator.get)
- [get_name](#vseparator.get_name)
- [get_prev_widget](#vseparator.get_prev_widget)
- [post_create](#vseparator.post_create)
- [prepare_create](#vseparator.prepare_create)
- [set_disabled](#vseparator.set_disabled)
- [update](#vseparator.update)
- [widget_update](#vseparator.widget_update)

### VSeparator.bind

Bind event. @see `Window.bind`

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### VSeparator.bind_events

Bind user events
**Example**
```
# (1) bind events in the constructor
eg.Canvas(key="-canvas-", bind_events={"<ButtonPress>": "on", "<ButtonRelease>": "off"})
# (2) bind events in the method
eg.Canvas(key="-canvas-").bind_events({"<ButtonPress>": "on", "<ButtonRelease>": "off"})
```

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L923)

### VSeparator.convert_props

```py
def convert_props(self, props: dict[str, Any]) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L875)

### VSeparator.create

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2436)

### VSeparator.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### VSeparator.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

### VSeparator.get_name

Get element name.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### VSeparator.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1022)

### VSeparator.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### VSeparator.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L942)

### VSeparator.set_disabled

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### VSeparator.update

update widget configuration.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1007)

### VSeparator.widget_update

```py
def widget_update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1011)

## Window

Main window object in TkEasyGUI

```py
class Window(
    self,
    title: str,
    layout: list[list[Element]], # set elements layout
    size: Union[tuple[str, int], None] = None, # window size
    resizable:bool = False,
    font: Union[FontType, None] = None,
    modal: bool = False, # modal window
    keep_on_top:bool = False, # keep on top
    no_titlebar: bool = False, # hide titlebar
    grab_anywhere: bool = False, # can move window by dragging anywhere
    alpha_channel: float = 1.0, # window alpha channel
    enable_key_events: bool = False, # enable keyboard events
    return_keyboard_events: bool = False, # enable keyboard events (for compatibility)
    use_ttk: bool = False, # use ttk style (default=False) (experimental)
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L190)

### Methods of Window

- [bind](#window.bind)
- [calc_font_size](#window.calc_font_size)
- [cancel_close](#window.cancel_close)
- [close](#window.close)
- [event_iter](#window.event_iter)
- [get_element_by_key](#window.get_element_by_key)
- [get_elements_by_type](#window.get_elements_by_type)
- [get_values](#window.get_values)
- [hide](#window.hide)
- [hide_titlebar](#window.hide_titlebar)
- [is_alive](#window.is_alive)
- [keep_on_top](#window.keep_on_top)
- [maximize](#window.maximize)
- [minimize](#window.minimize)
- [move_to_center](#window.move_to_center)
- [normal](#window.normal)
- [read](#window.read)
- [refresh](#window.refresh)
- [register_event_hooks](#window.register_event_hooks)
- [send_to_back](#window.send_to_back)
- [set_alpha_channel](#window.set_alpha_channel)
- [set_grab_anywhere](#window.set_grab_anywhere)
- [set_title](#window.set_title)
- [show](#window.show)
- [un_hide](#window.un_hide)
- [write_event_value](#window.write_event_value)

### Window.bind

[Window.bind] Bind element event and handler

```py
def bind(self, element: "Element", event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L682)

### Window.calc_font_size

Calculate font size.

```py
def calc_font_size(self, font: FontType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L403)

### Window.cancel_close

Cancel the close event.

```py
def cancel_close(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L622)

### Window.close

Close the window.

```py
def close(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L607)

### Window.event_iter

Return generator with event and values
**Example**
```py
import TkEasyGUI as eg
# create a window
with eg.Window("test", layout=[[eg.Button("Hello")]]) as window:
    # event loop
    for event, values in window.event_iter():
        if event == "Hello":
            eg.popup("Hello, World!")
```

```py
def event_iter(self, timeout: Union[int, None] = None, timeout_key: str=TIMEOUT_KEY) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L472)

### Window.get_element_by_key

Get an element by its key.

```py
def get_element_by_key(self, key: str) -> Union[Element, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L425)

### Window.get_elements_by_type

Get elements by type.

```py
def get_elements_by_type(self, element_type: str) -> list[Element]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L429)

### Window.get_values

Get values from the window.

```py
def get_values(self) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L541)

### Window.hide

Hide the window.

```py
def hide(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L520)

### Window.hide_titlebar

Hide the titlebar.

```py
def hide_titlebar(self, flag: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L599)

### Window.is_alive

Check if the window is alive.

```py
def is_alive(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L618)

### Window.keep_on_top

Set the window to keep on top.

```py
def keep_on_top(self, flag: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L588)

### Window.maximize

Maximize the window. (`resizable` should be set to True)

```py
def maximize(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L531)

### Window.minimize

Minimize the window.

```py
def minimize(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L506)

### Window.move_to_center

Move the window to the center of the screen.

```py
def move_to_center(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L420)

### Window.normal

set normal window.

```py
def normal(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L511)

### Window.read

[Window.read] Read events from the window.

```py
def read(self, timeout: Union[int, None] = None, timeout_key: str="-TIMEOUT-") -> tuple[str, dict[str, Any]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L438)

### Window.refresh

Refresh window

```py
def refresh(self) -> "Window":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L637)

### Window.register_event_hooks

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
- @see `Window.read`

```py
def register_event_hooks(self, hooks: dict[str, list[callable]]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L299)

### Window.send_to_back

Send the window to the back, and make it not keep on top.

```py
def send_to_back(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L593)

### Window.set_alpha_channel

Set the alpha channel of the window.

```py
def set_alpha_channel(self, alpha: float) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L536)

### Window.set_grab_anywhere

Set grab anywhere

```py
def set_grab_anywhere(self, flag: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L645)

### Window.set_title

Set the title of the window.

```py
def set_title(self, title: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L502)

### Window.show

Show hidden window (hide -> show)

```py
def show(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L633)

### Window.un_hide

Un hide the window.

```py
def un_hide(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L525)

### Window.write_event_value

```py
def write_event_value(self, key: str, values: dict[str, Any]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L626)

# Functions of TkEasyGUI.widgets

- [convert_color_html](#convert_color_html)
- [convert_color_rgb16](#convert_color_rgb16)
- [generate_element_id](#generate_element_id)
- [generate_element_style_key](#generate_element_style_key)
- [get_current_theme](#get_current_theme)
- [get_font_list](#get_font_list)
- [get_image_tk](#get_image_tk)
- [get_platform](#get_platform)
- [get_root_window](#get_root_window)
- [get_tnemes](#get_tnemes)
- [get_ttk_style](#get_ttk_style)
- [image_resize](#image_resize)
- [imagedata_to_bytes](#imagedata_to_bytes)
- [imagefile_to_bytes](#imagefile_to_bytes)
- [is_mac](#is_mac)
- [is_win](#is_win)
- [register_element_key](#register_element_key)
- [rgb](#rgb)
- [set_PySimpleGUI_compatibility](#set_pysimplegui_compatibility)
- [set_default_theme](#set_default_theme)
- [set_theme](#set_theme)
- [theme](#theme)
- [time_checker_end](#time_checker_end)
- [time_checker_start](#time_checker_start)

## convert_color_html

Convert RGB color(16bit tuple) to HTML color name.

```py
def convert_color_html(color_name: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L111)

## convert_color_rgb16

Convert color to RGB, return (r, g, b) tuple. range=0-65535

```py
def convert_color_rgb16(color_name: str) -> tuple[int, int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L106)

## generate_element_id

Generate a unique id for a value element.

```py
def generate_element_id() -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2975)

## generate_element_style_key

Get a unique id for an element.

```py
def generate_element_style_key(element_type: str) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2952)

## get_current_theme

Get current theme

```py
def get_current_theme() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L84)

## get_font_list

Get font list

```py
def get_font_list() -> list[str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L155)

## get_image_tk

Get Image for tk

```py
def get_image_tk(
    source: Union[bytes, Union[str, None]] = None,
    filename: Union[str, None] = None,
    data: Union[bytes, None] = None,
    size: Union[tuple[int, int], None] = None) -> Union[tk.PhotoImage, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2996)

## get_platform

get platform

```py
def get_platform() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L47)

## get_root_window

Get root window.

```py
def get_root_window() -> tk.Tk:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L134)

## get_tnemes

Get theme list
```py
print(get_themes())
```

```py
def get_tnemes() -> list[str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L73)

## get_ttk_style

Get ttk style

```py
def get_ttk_style() -> ttk.Style:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L161)

## image_resize



```py
def image_resize(img: PILImage, size: tuple[int, int]) -> PILImage:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2988)

## imagedata_to_bytes

Convert JPEG to PNG

```py
def imagedata_to_bytes(image_data: PILImage) -> bytes:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3032)

## imagefile_to_bytes

Read image file and convert to bytes

```py
def imagefile_to_bytes(filename: str) -> bytes:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3039)

## is_mac

platform : is mac?

```py
def is_mac() -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L51)

## is_win

platform : is Windows?

```py
def is_win() -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L54)

## register_element_key

Register element key.

```py
def register_element_key(key: str) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2967)

## rgb



```py
def rgb(r: int, g: int, b: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2982)

## set_PySimpleGUI_compatibility

Set compatibility with PySimpleGUI (Default=True)

```py
def set_PySimpleGUI_compatibility(flag: bool=True) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L126)

## set_default_theme

Set default theme
```py
print(get_themes())
```

```py
def set_default_theme() -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L88)

## set_theme

Change look and feel

```py
def set_theme(name: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L65)

## theme

Set theme

```py
def theme(name: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L61)

## time_checker_end



```py
def time_checker_end(start_time: datetime) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3050)

## time_checker_start



```py
def time_checker_start() -> datetime:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3047)

