# Module TkEasyGUI.widgets

TkEasyGUI Widgets

---------------------------

- [Classes](#classes-of-tkeasyguiwidgets)
- [Functions](#functions-of-tkeasyguiwidgets)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1330)

### Methods of Button

- [bind](#buttonbind)
- [bind_events](#buttonbind_events)
- [create](#buttoncreate)
- [disptach_event](#buttondisptach_event)
- [get](#buttonget)
- [get_name](#buttonget_name)
- [get_prev_widget](#buttonget_prev_widget)
- [get_text](#buttonget_text)
- [post_create](#buttonpost_create)
- [prepare_create](#buttonprepare_create)
- [set_button_color](#buttonset_button_color)
- [set_disabled](#buttonset_disabled)
- [set_text](#buttonset_text)
- [update](#buttonupdate)

### Button.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Button.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Button.create

Create a Button widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1373)

### Button.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Button.get

Returns the text of the button..

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1401)

### Button.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Button.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Button.get_text

Get the text of the button.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1410)

### Button.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Button.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Button.set_button_color

Set the button color.

```py
def set_button_color(self, button_color: Union[str, tuple[str,str]], update: bool = True) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1387)

### Button.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Button.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1405)

### Button.update

Update the widget.

```py
def update(self,
    text: Union[str, None] = None,
    disabled: Union[bool, None] = None,
    button_color: Union[str, tuple[str,str], None] = None,
    **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1414)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2197)

### Methods of Canvas

- [bind](#canvasbind)
- [bind_events](#canvasbind_events)
- [create](#canvascreate)
- [disptach_event](#canvasdisptach_event)
- [get](#canvasget)
- [get_name](#canvasget_name)
- [get_prev_widget](#canvasget_prev_widget)
- [post_create](#canvaspost_create)
- [prepare_create](#canvasprepare_create)
- [set_disabled](#canvasset_disabled)
- [update](#canvasupdate)

### Canvas.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Canvas.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Canvas.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2218)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2222)

### Canvas.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Canvas.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Canvas.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Canvas.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Canvas.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Canvas.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2226)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1445)

### Methods of Checkbox

- [bind](#checkboxbind)
- [bind_events](#checkboxbind_events)
- [create](#checkboxcreate)
- [disptach_event](#checkboxdisptach_event)
- [get](#checkboxget)
- [get_name](#checkboxget_name)
- [get_prev_widget](#checkboxget_prev_widget)
- [get_value](#checkboxget_value)
- [post_create](#checkboxpost_create)
- [prepare_create](#checkboxprepare_create)
- [set_disabled](#checkboxset_disabled)
- [set_text](#checkboxset_text)
- [set_value](#checkboxset_value)
- [update](#checkboxupdate)

### Checkbox.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Checkbox.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Checkbox.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1464)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1478)

### Checkbox.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Checkbox.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Checkbox.get_value

Get the value of the widget.

```py
def get_value(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1470)

### Checkbox.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Checkbox.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Checkbox.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Checkbox.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1482)

### Checkbox.set_value

Set the value of the widget.

```py
def set_value(self, b: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1474)

### Checkbox.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1487)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2912)

### Methods of ColorBrowse

- [bind](#colorbrowsebind)
- [bind_events](#colorbrowsebind_events)
- [create](#colorbrowsecreate)
- [disptach_event](#colorbrowsedisptach_event)
- [get](#colorbrowseget)
- [get_name](#colorbrowseget_name)
- [get_prev_widget](#colorbrowseget_prev_widget)
- [post_create](#colorbrowsepost_create)
- [prepare_create](#colorbrowseprepare_create)
- [set_disabled](#colorbrowseset_disabled)
- [set_text](#colorbrowseset_text)
- [show_dialog](#colorbrowseshow_dialog)
- [update](#colorbrowseupdate)

### ColorBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### ColorBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### ColorBrowse.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2780)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### ColorBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### ColorBrowse.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### ColorBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### ColorBrowse.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### ColorBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### ColorBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2820)

### ColorBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2929)

### ColorBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2825)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1116)

### Methods of Column

- [bind](#columnbind)
- [bind_events](#columnbind_events)
- [create](#columncreate)
- [disptach_event](#columndisptach_event)
- [get](#columnget)
- [get_name](#columnget_name)
- [get_prev_widget](#columnget_prev_widget)
- [post_create](#columnpost_create)
- [prepare_create](#columnprepare_create)
- [set_disabled](#columnset_disabled)
- [update](#columnupdate)

### Column.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Column.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Column.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1145)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1150)

### Column.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Column.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Column.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Column.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Column.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Column.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1154)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2541)

### Methods of Combo

- [bind](#combobind)
- [bind_events](#combobind_events)
- [create](#combocreate)
- [disptach_event](#combodisptach_event)
- [get](#comboget)
- [get_name](#comboget_name)
- [get_prev_widget](#comboget_prev_widget)
- [post_create](#combopost_create)
- [prepare_create](#comboprepare_create)
- [set_disabled](#comboset_disabled)
- [set_value](#comboset_value)
- [set_values](#comboset_values)
- [update](#comboupdate)

### Combo.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Combo.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Combo.create

[Combo.create] create Listbox widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2560)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2577)

### Combo.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Combo.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Combo.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Combo.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Combo.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Combo.set_value

Set the value of the widget.

```py
def set_value(self, v: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2573)

### Combo.set_values

Set values to list

```py
def set_values(self, values: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2567)

### Combo.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2583)

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

- [bind](#elementbind)
- [bind_events](#elementbind_events)
- [create](#elementcreate)
- [disptach_event](#elementdisptach_event)
- [get](#elementget)
- [get_name](#elementget_name)
- [get_prev_widget](#elementget_prev_widget)
- [post_create](#elementpost_create)
- [prepare_create](#elementprepare_create)
- [set_disabled](#elementset_disabled)
- [update](#elementupdate)

### Element.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Element.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Element.create

Create a widget.

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L934)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### Element.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Element.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Element.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Element.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Element.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Element.update

update widget configuration.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2754)

### Methods of FileBrowse

- [bind](#filebrowsebind)
- [bind_events](#filebrowsebind_events)
- [create](#filebrowsecreate)
- [disptach_event](#filebrowsedisptach_event)
- [get](#filebrowseget)
- [get_name](#filebrowseget_name)
- [get_prev_widget](#filebrowseget_prev_widget)
- [post_create](#filebrowsepost_create)
- [prepare_create](#filebrowseprepare_create)
- [set_disabled](#filebrowseset_disabled)
- [set_text](#filebrowseset_text)
- [show_dialog](#filebrowseshow_dialog)
- [update](#filebrowseupdate)

### FileBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### FileBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### FileBrowse.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2780)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### FileBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### FileBrowse.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### FileBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### FileBrowse.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### FileBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### FileBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2820)

### FileBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2801)

### FileBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2825)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2754)

### Methods of FileSaveAs

- [bind](#filesaveasbind)
- [bind_events](#filesaveasbind_events)
- [create](#filesaveascreate)
- [disptach_event](#filesaveasdisptach_event)
- [get](#filesaveasget)
- [get_name](#filesaveasget_name)
- [get_prev_widget](#filesaveasget_prev_widget)
- [post_create](#filesaveaspost_create)
- [prepare_create](#filesaveasprepare_create)
- [set_disabled](#filesaveasset_disabled)
- [set_text](#filesaveasset_text)
- [show_dialog](#filesaveasshow_dialog)
- [update](#filesaveasupdate)

### FileSaveAs.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### FileSaveAs.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### FileSaveAs.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2780)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### FileSaveAs.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### FileSaveAs.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### FileSaveAs.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### FileSaveAs.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### FileSaveAs.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### FileSaveAs.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2820)

### FileSaveAs.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2801)

### FileSaveAs.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2825)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2855)

### Methods of FileSaveAsBrowse

- [bind](#filesaveasbrowsebind)
- [bind_events](#filesaveasbrowsebind_events)
- [create](#filesaveasbrowsecreate)
- [disptach_event](#filesaveasbrowsedisptach_event)
- [get](#filesaveasbrowseget)
- [get_name](#filesaveasbrowseget_name)
- [get_prev_widget](#filesaveasbrowseget_prev_widget)
- [post_create](#filesaveasbrowsepost_create)
- [prepare_create](#filesaveasbrowseprepare_create)
- [set_disabled](#filesaveasbrowseset_disabled)
- [set_text](#filesaveasbrowseset_text)
- [show_dialog](#filesaveasbrowseshow_dialog)
- [update](#filesaveasbrowseupdate)

### FileSaveAsBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### FileSaveAsBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### FileSaveAsBrowse.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2780)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### FileSaveAsBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### FileSaveAsBrowse.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### FileSaveAsBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### FileSaveAsBrowse.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### FileSaveAsBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### FileSaveAsBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2820)

### FileSaveAsBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2801)

### FileSaveAsBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2825)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2833)

### Methods of FilesBrowse

- [bind](#filesbrowsebind)
- [bind_events](#filesbrowsebind_events)
- [create](#filesbrowsecreate)
- [disptach_event](#filesbrowsedisptach_event)
- [get](#filesbrowseget)
- [get_name](#filesbrowseget_name)
- [get_prev_widget](#filesbrowseget_prev_widget)
- [post_create](#filesbrowsepost_create)
- [prepare_create](#filesbrowseprepare_create)
- [set_disabled](#filesbrowseset_disabled)
- [set_text](#filesbrowseset_text)
- [show_dialog](#filesbrowseshow_dialog)
- [update](#filesbrowseupdate)

### FilesBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### FilesBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### FilesBrowse.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2780)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### FilesBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### FilesBrowse.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### FilesBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### FilesBrowse.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### FilesBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### FilesBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2820)

### FilesBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2801)

### FilesBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2825)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2881)

### Methods of FolderBrowse

- [bind](#folderbrowsebind)
- [bind_events](#folderbrowsebind_events)
- [create](#folderbrowsecreate)
- [disptach_event](#folderbrowsedisptach_event)
- [get](#folderbrowseget)
- [get_name](#folderbrowseget_name)
- [get_prev_widget](#folderbrowseget_prev_widget)
- [post_create](#folderbrowsepost_create)
- [prepare_create](#folderbrowseprepare_create)
- [set_disabled](#folderbrowseset_disabled)
- [set_text](#folderbrowseset_text)
- [show_dialog](#folderbrowseshow_dialog)
- [update](#folderbrowseupdate)

### FolderBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### FolderBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### FolderBrowse.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2780)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### FolderBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### FolderBrowse.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### FolderBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### FolderBrowse.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### FolderBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### FolderBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2820)

### FolderBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2898)

### FolderBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2825)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1053)

### Methods of Frame

- [bind](#framebind)
- [bind_events](#framebind_events)
- [create](#framecreate)
- [disptach_event](#framedisptach_event)
- [get](#frameget)
- [get_name](#frameget_name)
- [get_prev_widget](#frameget_prev_widget)
- [post_create](#framepost_create)
- [prepare_create](#frameprepare_create)
- [set_disabled](#frameset_disabled)
- [update](#frameupdate)

### Frame.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Frame.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Frame.create

Create a Frame widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1088)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1100)

### Frame.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Frame.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Frame.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Frame.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Frame.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Frame.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1104)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### Methods of Graph

- [bind](#graphbind)
- [bind_events](#graphbind_events)
- [create](#graphcreate)
- [disptach_event](#graphdisptach_event)
- [draw_arc](#graphdraw_arc)
- [draw_circle](#graphdraw_circle)
- [draw_image](#graphdraw_image)
- [draw_line](#graphdraw_line)
- [draw_lines](#graphdraw_lines)
- [draw_oval](#graphdraw_oval)
- [draw_point](#graphdraw_point)
- [draw_polygon](#graphdraw_polygon)
- [draw_rectangle](#graphdraw_rectangle)
- [draw_text](#graphdraw_text)
- [erase](#grapherase)
- [get](#graphget)
- [get_name](#graphget_name)
- [get_prev_widget](#graphget_prev_widget)
- [post_create](#graphpost_create)
- [prepare_create](#graphprepare_create)
- [set_disabled](#graphset_disabled)
- [update](#graphupdate)

### Graph.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Graph.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Graph.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2263)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2305)

### Graph.draw_circle

Draw a circle.

```py
def draw_circle(self, center_location: PointType, radius: Union[int, float], fill_color: Union[str, None] = None, line_color: Union[str, None] = 'black', line_width: int = 1) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2296)

### Graph.draw_image

Draw image

```py
def draw_image(self, filename: Union[str, None] = None, data: Union[bytes, None] = None, location: Union[PointType, None] = None) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2327)

### Graph.draw_line

Draw a line.

```py
def draw_line(self, point_from: PointType, point_to: PointType, color: str = 'black', width: int = 1) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2282)

### Graph.draw_lines

Draw lines.

```py
def draw_lines(self, points: list[PointType], color='black', width=1) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2286)

### Graph.draw_oval

Draw an oval.

```py
def draw_oval(self, top_left: PointType, bottom_right: PointType, fill_color: Union[str, None] = None, line_color: Union[str, None] = None, line_width: int = 1):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2301)

### Graph.draw_point

Draw a point.

```py
def draw_point(self, point: PointType, size: int = 2, color: str = 'black') -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2290)

### Graph.draw_polygon

Draw polygon

```py
def draw_polygon(self, points: list[PointType], fill_color: Union[str, None] = None, line_color: Union[str, None] = None, line_width: Union[int, None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2317)

### Graph.draw_rectangle

Draw rectangle

```py
def draw_rectangle(self, top_left: PointType, bottom_right: PointType, fill_color: Union[str, None] = None, line_color: Union[str, None] = None, line_width: Union[int, None] = None) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2313)

### Graph.draw_text

Draw text

```py
def draw_text(self, text: str, location: PointType, color: Union[str, None]='black', font: FontType = None, angle: Union[float, str, None] = 0, text_location: TextAlign = tk.CENTER) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2321)

### Graph.erase

Delete all

```py
def erase(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2309)

### Graph.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2268)

### Graph.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Graph.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Graph.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Graph.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Graph.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Graph.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2272)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2440)

### Methods of HSeparator

- [bind](#hseparatorbind)
- [bind_events](#hseparatorbind_events)
- [create](#hseparatorcreate)
- [disptach_event](#hseparatordisptach_event)
- [get](#hseparatorget)
- [get_name](#hseparatorget_name)
- [get_prev_widget](#hseparatorget_prev_widget)
- [post_create](#hseparatorpost_create)
- [prepare_create](#hseparatorprepare_create)
- [set_disabled](#hseparatorset_disabled)
- [update](#hseparatorupdate)

### HSeparator.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### HSeparator.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### HSeparator.create

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2458)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### HSeparator.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### HSeparator.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### HSeparator.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### HSeparator.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### HSeparator.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### HSeparator.update

update widget configuration.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2340)

### Methods of Image

- [bind](#imagebind)
- [bind_events](#imagebind_events)
- [create](#imagecreate)
- [disptach_event](#imagedisptach_event)
- [erase](#imageerase)
- [get](#imageget)
- [get_name](#imageget_name)
- [get_prev_widget](#imageget_prev_widget)
- [post_create](#imagepost_create)
- [prepare_create](#imageprepare_create)
- [set_disabled](#imageset_disabled)
- [set_image](#imageset_image)
- [update](#imageupdate)

### Image.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Image.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Image.create

Create a Image widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2360)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2373)

### Image.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2369)

### Image.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Image.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Image.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Image.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Image.set_disabled

Set disabled widgets state

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2377)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2394)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1573)

### Methods of Input

- [bind](#inputbind)
- [bind_events](#inputbind_events)
- [copy](#inputcopy)
- [copy_selected_text](#inputcopy_selected_text)
- [create](#inputcreate)
- [cut](#inputcut)
- [delete_selected](#inputdelete_selected)
- [disptach_event](#inputdisptach_event)
- [get](#inputget)
- [get_cursor_pos](#inputget_cursor_pos)
- [get_name](#inputget_name)
- [get_prev_widget](#inputget_prev_widget)
- [get_selected_text](#inputget_selected_text)
- [get_selection_length](#inputget_selection_length)
- [get_selection_pos](#inputget_selection_pos)
- [get_selection_start](#inputget_selection_start)
- [get_text](#inputget_text)
- [paste](#inputpaste)
- [post_create](#inputpost_create)
- [prepare_create](#inputprepare_create)
- [select_all](#inputselect_all)
- [set_cursor_pos](#inputset_cursor_pos)
- [set_disabled](#inputset_disabled)
- [set_readonly](#inputset_readonly)
- [set_selection_start](#inputset_selection_start)
- [set_text](#inputset_text)
- [update](#inputupdate)

### Input.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Input.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Input.copy

copy to clipboard

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1716)

### Input.copy_selected_text

Copy selected text

```py
def copy_selected_text(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1679)

### Input.create

create Input widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1629)

### Input.cut

cut to clipboard

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1724)

### Input.delete_selected

delete selected text

```py
def delete_selected(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1731)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1651)

### Input.get_cursor_pos

get cursor position

```py
def get_cursor_pos(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1765)

### Input.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Input.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Input.get_selected_text

get selected text

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1670)

### Input.get_selection_length

get selection length

```py
def get_selection_length(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1783)

### Input.get_selection_pos

get selection positions

```py
def get_selection_pos(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1754)

### Input.get_selection_start

get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1774)

### Input.get_text

get text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1666)

### Input.paste

paste from clipboard

```py
def paste(self):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1742)

### Input.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Input.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Input.select_all

select_all

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1708)

### Input.set_cursor_pos

set cursor position

```py
def set_cursor_pos(self, index: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### Input.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Input.set_readonly

set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1684)

### Input.set_selection_start

set selection start and length

```py
def set_selection_start(self, sel_start: int, sel_length: int=0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1793)

### Input.set_text

set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1655)

### Input.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1690)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1573)

### Methods of InputText

- [bind](#inputtextbind)
- [bind_events](#inputtextbind_events)
- [copy](#inputtextcopy)
- [copy_selected_text](#inputtextcopy_selected_text)
- [create](#inputtextcreate)
- [cut](#inputtextcut)
- [delete_selected](#inputtextdelete_selected)
- [disptach_event](#inputtextdisptach_event)
- [get](#inputtextget)
- [get_cursor_pos](#inputtextget_cursor_pos)
- [get_name](#inputtextget_name)
- [get_prev_widget](#inputtextget_prev_widget)
- [get_selected_text](#inputtextget_selected_text)
- [get_selection_length](#inputtextget_selection_length)
- [get_selection_pos](#inputtextget_selection_pos)
- [get_selection_start](#inputtextget_selection_start)
- [get_text](#inputtextget_text)
- [paste](#inputtextpaste)
- [post_create](#inputtextpost_create)
- [prepare_create](#inputtextprepare_create)
- [select_all](#inputtextselect_all)
- [set_cursor_pos](#inputtextset_cursor_pos)
- [set_disabled](#inputtextset_disabled)
- [set_readonly](#inputtextset_readonly)
- [set_selection_start](#inputtextset_selection_start)
- [set_text](#inputtextset_text)
- [update](#inputtextupdate)

### InputText.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### InputText.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### InputText.copy

copy to clipboard

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1716)

### InputText.copy_selected_text

Copy selected text

```py
def copy_selected_text(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1679)

### InputText.create

create Input widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1629)

### InputText.cut

cut to clipboard

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1724)

### InputText.delete_selected

delete selected text

```py
def delete_selected(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1731)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1651)

### InputText.get_cursor_pos

get cursor position

```py
def get_cursor_pos(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1765)

### InputText.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### InputText.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### InputText.get_selected_text

get selected text

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1670)

### InputText.get_selection_length

get selection length

```py
def get_selection_length(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1783)

### InputText.get_selection_pos

get selection positions

```py
def get_selection_pos(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1754)

### InputText.get_selection_start

get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1774)

### InputText.get_text

get text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1666)

### InputText.paste

paste from clipboard

```py
def paste(self):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1742)

### InputText.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### InputText.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### InputText.select_all

select_all

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1708)

### InputText.set_cursor_pos

set cursor position

```py
def set_cursor_pos(self, index: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### InputText.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### InputText.set_readonly

set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1684)

### InputText.set_selection_start

set selection start and length

```py
def set_selection_start(self, sel_start: int, sel_length: int=0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1793)

### InputText.set_text

set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1655)

### InputText.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1690)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1166)

### Methods of Label

- [bind](#labelbind)
- [bind_events](#labelbind_events)
- [create](#labelcreate)
- [disptach_event](#labeldisptach_event)
- [get](#labelget)
- [get_name](#labelget_name)
- [get_prev_widget](#labelget_prev_widget)
- [get_text](#labelget_text)
- [post_create](#labelpost_create)
- [prepare_create](#labelprepare_create)
- [set_disabled](#labelset_disabled)
- [set_text](#labelset_text)
- [update](#labelupdate)

### Label.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Label.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Label.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1195)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1206)

### Label.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Label.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Label.get_text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1210)

### Label.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Label.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Label.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Label.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1213)

### Label.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1218)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2465)

### Methods of Listbox

- [bind](#listboxbind)
- [bind_events](#listboxbind_events)
- [create](#listboxcreate)
- [disptach_event](#listboxdisptach_event)
- [get](#listboxget)
- [get_name](#listboxget_name)
- [get_prev_widget](#listboxget_prev_widget)
- [post_create](#listboxpost_create)
- [prepare_create](#listboxprepare_create)
- [select_values](#listboxselect_values)
- [set_disabled](#listboxset_disabled)
- [set_values](#listboxset_values)
- [update](#listboxupdate)

### Listbox.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Listbox.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Listbox.create

[Listbox.create] create Listbox widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2485)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2515)

### Listbox.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Listbox.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Listbox.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Listbox.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Listbox.select_values

Select values

```py
def select_values(self, values: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2494)

### Listbox.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Listbox.set_values

Set values to list

```py
def set_values(self, values: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2505)

### Listbox.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2528)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1245)

### Methods of Menu

- [bind](#menubind)
- [bind_events](#menubind_events)
- [create](#menucreate)
- [disptach_event](#menudisptach_event)
- [get](#menuget)
- [get_name](#menuget_name)
- [get_prev_widget](#menuget_prev_widget)
- [get_text](#menuget_text)
- [post_create](#menupost_create)
- [prepare_create](#menuprepare_create)
- [set_disabled](#menuset_disabled)
- [set_text](#menuset_text)
- [update](#menuupdate)

### Menu.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Menu.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Menu.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1257)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1310)

### Menu.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Menu.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Menu.get_text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1314)

### Menu.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Menu.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Menu.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Menu.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1317)

### Menu.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1322)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1808)

### Methods of Multiline

- [bind](#multilinebind)
- [bind_events](#multilinebind_events)
- [copy](#multilinecopy)
- [create](#multilinecreate)
- [cut](#multilinecut)
- [disptach_event](#multilinedisptach_event)
- [get](#multilineget)
- [get_cursor_pos](#multilineget_cursor_pos)
- [get_name](#multilineget_name)
- [get_prev_widget](#multilineget_prev_widget)
- [get_selected_text](#multilineget_selected_text)
- [get_selection_length](#multilineget_selection_length)
- [get_selection_pos](#multilineget_selection_pos)
- [get_selection_start](#multilineget_selection_start)
- [get_text](#multilineget_text)
- [index_to_pos](#multilineindex_to_pos)
- [paste](#multilinepaste)
- [pos_to_index](#multilinepos_to_index)
- [post_create](#multilinepost_create)
- [prepare_create](#multilineprepare_create)
- [print](#multilineprint)
- [select_all](#multilineselect_all)
- [set_cursor_pos](#multilineset_cursor_pos)
- [set_disabled](#multilineset_disabled)
- [set_readonly](#multilineset_readonly)
- [set_selection_pos](#multilineset_selection_pos)
- [set_selection_start](#multilineset_selection_start)
- [set_text](#multilineset_text)
- [update](#multilineupdate)

### Multiline.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Multiline.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Multiline.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1896)

### Multiline.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1860)

### Multiline.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1913)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1873)

### Multiline.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2004)

### Multiline.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Multiline.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Multiline.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1886)

### Multiline.get_selection_length

get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2040)

### Multiline.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1949)

### Multiline.get_selection_start

get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2020)

### Multiline.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1879)

### Multiline.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1986)

### Multiline.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1904)

### Multiline.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1971)

### Multiline.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Multiline.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Multiline.print

Print text.

```py
def print(self, text: str, text_color: Union[str, None] = None, background_color: Union[str, None] = None, end:str="\n") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2059)

### Multiline.select_all

select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2050)

### Multiline.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2014)

### Multiline.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Multiline.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1931)

### Multiline.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1960)

### Multiline.set_selection_start

set selection start

```py
def set_selection_start(self, index: int, sel_length: int=0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2031)

### Multiline.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1937)

### Multiline.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1923)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1808)

### Methods of Output

- [bind](#outputbind)
- [bind_events](#outputbind_events)
- [copy](#outputcopy)
- [create](#outputcreate)
- [cut](#outputcut)
- [disptach_event](#outputdisptach_event)
- [get](#outputget)
- [get_cursor_pos](#outputget_cursor_pos)
- [get_name](#outputget_name)
- [get_prev_widget](#outputget_prev_widget)
- [get_selected_text](#outputget_selected_text)
- [get_selection_length](#outputget_selection_length)
- [get_selection_pos](#outputget_selection_pos)
- [get_selection_start](#outputget_selection_start)
- [get_text](#outputget_text)
- [index_to_pos](#outputindex_to_pos)
- [paste](#outputpaste)
- [pos_to_index](#outputpos_to_index)
- [post_create](#outputpost_create)
- [prepare_create](#outputprepare_create)
- [print](#outputprint)
- [select_all](#outputselect_all)
- [set_cursor_pos](#outputset_cursor_pos)
- [set_disabled](#outputset_disabled)
- [set_readonly](#outputset_readonly)
- [set_selection_pos](#outputset_selection_pos)
- [set_selection_start](#outputset_selection_start)
- [set_text](#outputset_text)
- [update](#outputupdate)

### Output.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Output.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Output.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1896)

### Output.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1860)

### Output.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1913)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1873)

### Output.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2004)

### Output.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Output.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Output.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1886)

### Output.get_selection_length

get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2040)

### Output.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1949)

### Output.get_selection_start

get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2020)

### Output.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1879)

### Output.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1986)

### Output.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1904)

### Output.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1971)

### Output.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Output.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Output.print

Print text.

```py
def print(self, text: str, text_color: Union[str, None] = None, background_color: Union[str, None] = None, end:str="\n") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2059)

### Output.select_all

select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2050)

### Output.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2014)

### Output.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Output.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1931)

### Output.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1960)

### Output.set_selection_start

set selection start

```py
def set_selection_start(self, index: int, sel_length: int=0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2031)

### Output.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1937)

### Output.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1923)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1501)

### Methods of Radio

- [bind](#radiobind)
- [bind_events](#radiobind_events)
- [create](#radiocreate)
- [disptach_event](#radiodisptach_event)
- [get](#radioget)
- [get_name](#radioget_name)
- [get_prev_widget](#radioget_prev_widget)
- [get_value](#radioget_value)
- [is_selected](#radiois_selected)
- [post_create](#radiopost_create)
- [prepare_create](#radioprepare_create)
- [select](#radioselect)
- [set_disabled](#radioset_disabled)
- [set_text](#radioset_text)
- [update](#radioupdate)

### Radio.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Radio.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Radio.create

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1523)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1554)

### Radio.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Radio.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Radio.get_value

Get the value of the widget.

```py
def get_value(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1550)

### Radio.is_selected

Check if the radio button is selected.

```py
def is_selected(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1546)

### Radio.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Radio.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Radio.select

Select the radio button.

```py
def select(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1542)

### Radio.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Radio.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1558)

### Radio.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1563)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2085)

### Methods of Slider

- [bind](#sliderbind)
- [bind_events](#sliderbind_events)
- [create](#slidercreate)
- [disptach_event](#sliderdisptach_event)
- [get](#sliderget)
- [get_name](#sliderget_name)
- [get_prev_widget](#sliderget_prev_widget)
- [get_range](#sliderget_range)
- [post_create](#sliderpost_create)
- [prepare_create](#sliderprepare_create)
- [set](#sliderset)
- [set_disabled](#sliderset_disabled)
- [set_range](#sliderset_range)
- [update](#sliderupdate)

### Slider.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Slider.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Slider.create

Create the widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2134)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2165)

### Slider.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Slider.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Slider.get_range

```py
def get_range(self) -> tuple[float, float]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2177)

### Slider.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Slider.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Slider.set

Set value of Slider

```py
def set(self, value: float) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2169)

### Slider.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Slider.set_range

Set the range of the slider.

```py
def set_range(self, from_: float, to: float) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2173)

### Slider.update

Update the widget.

```py
def update(self,
    value: Union[float, None]=None,
    range: Union[tuple[float, float], None]=None,
    disable_number_display: Union[bool, None]=None,
    **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2180)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1330)

### Methods of Submit

- [bind](#submitbind)
- [bind_events](#submitbind_events)
- [create](#submitcreate)
- [disptach_event](#submitdisptach_event)
- [get](#submitget)
- [get_name](#submitget_name)
- [get_prev_widget](#submitget_prev_widget)
- [get_text](#submitget_text)
- [post_create](#submitpost_create)
- [prepare_create](#submitprepare_create)
- [set_button_color](#submitset_button_color)
- [set_disabled](#submitset_disabled)
- [set_text](#submitset_text)
- [update](#submitupdate)

### Submit.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Submit.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Submit.create

Create a Button widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1373)

### Submit.disptach_event

Dispatch event

```py
def disptach_event(self, values: Union[dict[str, Any], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L799)

### Submit.get

Returns the text of the button..

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1401)

### Submit.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Submit.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Submit.get_text

Get the text of the button.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1410)

### Submit.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Submit.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Submit.set_button_color

Set the button color.

```py
def set_button_color(self, button_color: Union[str, tuple[str,str]], update: bool = True) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1387)

### Submit.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Submit.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1405)

### Submit.update

Update the widget.

```py
def update(self,
    text: Union[str, None] = None,
    disabled: Union[bool, None] = None,
    button_color: Union[str, tuple[str,str], None] = None,
    **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1414)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2597)

### Methods of Table

- [bind](#tablebind)
- [bind_events](#tablebind_events)
- [create](#tablecreate)
- [disptach_event](#tabledisptach_event)
- [get](#tableget)
- [get_name](#tableget_name)
- [get_prev_widget](#tableget_prev_widget)
- [post_create](#tablepost_create)
- [prepare_create](#tableprepare_create)
- [set_disabled](#tableset_disabled)
- [set_values](#tableset_values)
- [update](#tableupdate)

### Table.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Table.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Table.create

Create a Table widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2656)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2715)

### Table.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Table.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Table.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Table.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Table.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Table.set_values

Set values to the table.

```py
def set_values(self, values: list[list[str]], headings: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2700)

### Table.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2732)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1166)

### Methods of Text

- [bind](#textbind)
- [bind_events](#textbind_events)
- [create](#textcreate)
- [disptach_event](#textdisptach_event)
- [get](#textget)
- [get_name](#textget_name)
- [get_prev_widget](#textget_prev_widget)
- [get_text](#textget_text)
- [post_create](#textpost_create)
- [prepare_create](#textprepare_create)
- [set_disabled](#textset_disabled)
- [set_text](#textset_text)
- [update](#textupdate)

### Text.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Text.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Text.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1195)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1206)

### Text.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Text.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Text.get_text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1210)

### Text.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Text.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Text.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Text.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1213)

### Text.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1218)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1808)

### Methods of Textarea

- [bind](#textareabind)
- [bind_events](#textareabind_events)
- [copy](#textareacopy)
- [create](#textareacreate)
- [cut](#textareacut)
- [disptach_event](#textareadisptach_event)
- [get](#textareaget)
- [get_cursor_pos](#textareaget_cursor_pos)
- [get_name](#textareaget_name)
- [get_prev_widget](#textareaget_prev_widget)
- [get_selected_text](#textareaget_selected_text)
- [get_selection_length](#textareaget_selection_length)
- [get_selection_pos](#textareaget_selection_pos)
- [get_selection_start](#textareaget_selection_start)
- [get_text](#textareaget_text)
- [index_to_pos](#textareaindex_to_pos)
- [paste](#textareapaste)
- [pos_to_index](#textareapos_to_index)
- [post_create](#textareapost_create)
- [prepare_create](#textareaprepare_create)
- [print](#textareaprint)
- [select_all](#textareaselect_all)
- [set_cursor_pos](#textareaset_cursor_pos)
- [set_disabled](#textareaset_disabled)
- [set_readonly](#textareaset_readonly)
- [set_selection_pos](#textareaset_selection_pos)
- [set_selection_start](#textareaset_selection_start)
- [set_text](#textareaset_text)
- [update](#textareaupdate)

### Textarea.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### Textarea.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### Textarea.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1896)

### Textarea.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1860)

### Textarea.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1913)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1873)

### Textarea.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2004)

### Textarea.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### Textarea.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### Textarea.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1886)

### Textarea.get_selection_length

get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2040)

### Textarea.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1949)

### Textarea.get_selection_start

get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2020)

### Textarea.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1879)

### Textarea.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1986)

### Textarea.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1904)

### Textarea.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1971)

### Textarea.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### Textarea.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### Textarea.print

Print text.

```py
def print(self, text: str, text_color: Union[str, None] = None, background_color: Union[str, None] = None, end:str="\n") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2059)

### Textarea.select_all

select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2050)

### Textarea.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2014)

### Textarea.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### Textarea.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1931)

### Textarea.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1960)

### Textarea.set_selection_start

set selection start

```py
def set_selection_start(self, index: int, sel_length: int=0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2031)

### Textarea.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1937)

### Textarea.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1923)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2416)

### Methods of VSeparator

- [bind](#vseparatorbind)
- [bind_events](#vseparatorbind_events)
- [create](#vseparatorcreate)
- [disptach_event](#vseparatordisptach_event)
- [get](#vseparatorget)
- [get_name](#vseparatorget_name)
- [get_prev_widget](#vseparatorget_prev_widget)
- [post_create](#vseparatorpost_create)
- [prepare_create](#vseparatorprepare_create)
- [set_disabled](#vseparatorset_disabled)
- [update](#vseparatorupdate)

### VSeparator.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(self, event_name: str, handle_name: str, propagate: bool=True, event_mode: EventMode = "user") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L791)

### VSeparator.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)

```py
def bind_events(self, events: dict[str, str], event_mode: EventMode="user") -> Element:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L926)

### VSeparator.create

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2434)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L999)

### VSeparator.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L785)

### VSeparator.get_prev_widget

Get the previous widget.

```py
def get_prev_widget(self, target_key: Union[str, None] = None) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

### VSeparator.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L995)

### VSeparator.prepare_create

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L938)

### VSeparator.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L918)

### VSeparator.update

update widget configuration.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1003)

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

- [bind](#windowbind)
- [calc_font_size](#windowcalc_font_size)
- [cancel_close](#windowcancel_close)
- [close](#windowclose)
- [event_iter](#windowevent_iter)
- [get_element_by_key](#windowget_element_by_key)
- [get_elements_by_type](#windowget_elements_by_type)
- [get_values](#windowget_values)
- [hide](#windowhide)
- [hide_titlebar](#windowhide_titlebar)
- [is_alive](#windowis_alive)
- [keep_on_top](#windowkeep_on_top)
- [maximize](#windowmaximize)
- [minimize](#windowminimize)
- [move_to_center](#windowmove_to_center)
- [normal](#windownormal)
- [read](#windowread)
- [refresh](#windowrefresh)
- [register_event_hooks](#windowregister_event_hooks)
- [send_to_back](#windowsend_to_back)
- [set_alpha_channel](#windowset_alpha_channel)
- [set_grab_anywhere](#windowset_grab_anywhere)
- [set_title](#windowset_title)
- [show](#windowshow)
- [un_hide](#windowun_hide)
- [write_event_value](#windowwrite_event_value)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2973)

## generate_element_style_key

Get a unique id for an element.

```py
def generate_element_style_key(element_type: str) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2950)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2994)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2986)

## imagedata_to_bytes

Convert JPEG to PNG

```py
def imagedata_to_bytes(image_data: PILImage) -> bytes:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3030)

## imagefile_to_bytes

Read image file and convert to bytes

```py
def imagefile_to_bytes(filename: str) -> bytes:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3037)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2965)

## rgb



```py
def rgb(r: int, g: int, b: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2980)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3048)

## time_checker_start



```py
def time_checker_start() -> datetime:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3045)

