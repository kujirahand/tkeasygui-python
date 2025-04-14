# Module TkEasyGUI.widgets

TkEasyGUI Widgets.

---------------------------

- [Classes](#classes-of-tkeasyguiwidgets)
- [Functions](#functions-of-tkeasyguiwidgets)

# Classes of TkEasyGUI.widgets

- [Button](#button)
- [CalendarBrowse](#calendarbrowse)
- [CalendarButton](#calendarbutton)
- [Canvas](#canvas)
- [Checkbox](#checkbox)
- [CloseButton](#closebutton)
- [ColorBrowse](#colorbrowse)
- [Column](#column)
- [Combo](#combo)
- [Element](#element)
- [FileBrowse](#filebrowse)
- [FileSaveAs](#filesaveas)
- [FileSaveAsBrowse](#filesaveasbrowse)
- [FilesBrowse](#filesbrowse)
- [FolderBrowse](#folderbrowse)
- [Frame](#frame)
- [Graph](#graph)
- [HSeparator](#hseparator)
- [Image](#image)
- [Input](#input)
- [InputText](#inputtext)
- [Label](#label)
- [ListBrowse](#listbrowse)
- [Listbox](#listbox)
- [Menu](#menu)
- [Multiline](#multiline)
- [MultilineBrowse](#multilinebrowse)
- [Output](#output)
- [Push](#push)
- [Radio](#radio)
- [Slider](#slider)
- [Submit](#submit)
- [Tab](#tab)
- [TabGroup](#tabgroup)
- [Table](#table)
- [Text](#text)
- [Textarea](#textarea)
- [TkEasyError](#tkeasyerror)
- [VPush](#vpush)
- [VSeparator](#vseparator)
- [Window](#window)

## Button

Button element

**Example**
The program below changes the button's label to "Pushed" when the button is pressed.
```python
import TkEasyGUI as eg
button:eg.Button = eg.Button("Push me")
with eg.Window("Title", layout=[[button]]) as window:
    for event, values in window.event_iter():
        if event == button.get_text():
            button.set_text("Pushed")
            break
```

```py
class Button(
    self,
    button_text: str = "Button",
    key: Union[str, None] = None,
    disabled: bool = False,
    size: Union[tuple[int, int], None] = None,
    tooltip: Union[str, None] = None,  # (TODO) tooltip
    button_color: Union[str, tuple[str, str], None] = None,
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[
    str, None
    ] = None,  # background color (not supported on macOS)
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    use_ttk_buttons: bool = False,
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Methods of Button

- [bind](#buttonbind)
- [bind_events](#buttonbind_events)
- [create](#buttoncreate)
- [disptach_event](#buttondisptach_event)
- [get](#buttonget)
- [get_height](#buttonget_height)
- [get_name](#buttonget_name)
- [get_prev_element](#buttonget_prev_element)
- [get_text](#buttonget_text)
- [get_width](#buttonget_width)
- [post_create](#buttonpost_create)
- [prepare_create](#buttonprepare_create)
- [set_button_color](#buttonset_button_color)
- [set_cursor](#buttonset_cursor)
- [set_disabled](#buttonset_disabled)
- [set_text](#buttonset_text)
- [update](#buttonupdate)

### Button.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.create

Create a Button widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.get

Returns the text of the button..

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.get_text

Get the text of the button.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.set_button_color

Set the button color.

```py
def set_button_color(
    self, button_color: Union[str, tuple[str, str]], update: bool = True
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Button.update

Update the widget.

```py
def update(
    self,
    text: Union[str, None] = None,
    disabled: Union[bool, None] = None,
    button_color: Union[str, tuple[str, str], None] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

## CalendarBrowse

CalendarBrowse element.

```py
class CalendarBrowse(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    default_date: Union[datetime, None] = None,
    date_format: str = "%Y-%m-%d",
    title: str = "",
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### Methods of CalendarBrowse

- [bind](#calendarbrowsebind)
- [bind_events](#calendarbrowsebind_events)
- [create](#calendarbrowsecreate)
- [disptach_event](#calendarbrowsedisptach_event)
- [get](#calendarbrowseget)
- [get_height](#calendarbrowseget_height)
- [get_name](#calendarbrowseget_name)
- [get_prev_element](#calendarbrowseget_prev_element)
- [get_width](#calendarbrowseget_width)
- [post_create](#calendarbrowsepost_create)
- [prepare_create](#calendarbrowseprepare_create)
- [set_cursor](#calendarbrowseset_cursor)
- [set_disabled](#calendarbrowseset_disabled)
- [set_text](#calendarbrowseset_text)
- [show_dialog](#calendarbrowseshow_dialog)
- [update](#calendarbrowseupdate)

### CalendarBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[datetime, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

## CalendarButton

CalendarButton element. (alias of CalendarBrowse)

```py
class CalendarButton(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    default_date: Union[datetime, None] = None,
    date_format: str = "%Y-%m-%d",
    title: str = "",
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### Methods of CalendarButton

- [bind](#calendarbuttonbind)
- [bind_events](#calendarbuttonbind_events)
- [create](#calendarbuttoncreate)
- [disptach_event](#calendarbuttondisptach_event)
- [get](#calendarbuttonget)
- [get_height](#calendarbuttonget_height)
- [get_name](#calendarbuttonget_name)
- [get_prev_element](#calendarbuttonget_prev_element)
- [get_width](#calendarbuttonget_width)
- [post_create](#calendarbuttonpost_create)
- [prepare_create](#calendarbuttonprepare_create)
- [set_cursor](#calendarbuttonset_cursor)
- [set_disabled](#calendarbuttonset_disabled)
- [set_text](#calendarbuttonset_text)
- [show_dialog](#calendarbuttonshow_dialog)
- [update](#calendarbuttonupdate)

### CalendarButton.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[datetime, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

### CalendarButton.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4535)

## Canvas

Canvas element.

This widget provides the same drawing methods as [tk.Canvas](https://tkdocs.com/tutorial/canvas.html).
methods: create_line/create_rectangle/create_oval/create_polygon/create_arc/create_image/delete etc...

```py
class Canvas(
    self,
    key: Union[str, None] = None,
    enable_events: bool = False,
    background_color: Union[str, None] = None,
    size: tuple[int, int] = (300, 300),
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Methods of Canvas

- [bind](#canvasbind)
- [bind_events](#canvasbind_events)
- [clear](#canvasclear)
- [create](#canvascreate)
- [disptach_event](#canvasdisptach_event)
- [get](#canvasget)
- [get_height](#canvasget_height)
- [get_name](#canvasget_name)
- [get_prev_element](#canvasget_prev_element)
- [get_width](#canvasget_width)
- [post_create](#canvaspost_create)
- [prepare_create](#canvasprepare_create)
- [set_cursor](#canvasset_cursor)
- [set_disabled](#canvasset_disabled)
- [update](#canvasupdate)

### Canvas.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.clear

Clear the canvas.

```py
def clear(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.create

Create Canvas widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

### Canvas.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3245)

## Checkbox

Checkbox element.

```py
class Checkbox(
    self,
    text: str = "",
    default: bool = False,
    key: Union[str, None] = None,
    enable_events: bool = False,
    group_id: Union[
    str, None
    ] = None,  # If a group_id is provided, the values will contain key's list of True
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Methods of Checkbox

- [bind](#checkboxbind)
- [bind_events](#checkboxbind_events)
- [create](#checkboxcreate)
- [disptach_event](#checkboxdisptach_event)
- [get](#checkboxget)
- [get_height](#checkboxget_height)
- [get_name](#checkboxget_name)
- [get_prev_element](#checkboxget_prev_element)
- [get_value](#checkboxget_value)
- [get_width](#checkboxget_width)
- [post_create](#checkboxpost_create)
- [prepare_create](#checkboxprepare_create)
- [set_cursor](#checkboxset_cursor)
- [set_disabled](#checkboxset_disabled)
- [set_text](#checkboxset_text)
- [set_value](#checkboxset_value)
- [update](#checkboxupdate)

### Checkbox.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.create

Create a Checkbox widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.get_value

Get the value of the widget.

```py
def get_value(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.set_value

Set the value of the widget.

```py
def set_value(self, b: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

### Checkbox.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2271)

## CloseButton

CloseButton element.

```py
class CloseButton(
    self,
    button_text: str = "Close",
    key: Union[str, None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### Methods of CloseButton

- [bind](#closebuttonbind)
- [bind_events](#closebuttonbind_events)
- [close_window](#closebuttonclose_window)
- [create](#closebuttoncreate)
- [disptach_event](#closebuttondisptach_event)
- [get](#closebuttonget)
- [get_height](#closebuttonget_height)
- [get_name](#closebuttonget_name)
- [get_prev_element](#closebuttonget_prev_element)
- [get_text](#closebuttonget_text)
- [get_width](#closebuttonget_width)
- [post_create](#closebuttonpost_create)
- [prepare_create](#closebuttonprepare_create)
- [set_button_color](#closebuttonset_button_color)
- [set_cursor](#closebuttonset_cursor)
- [set_disabled](#closebuttonset_disabled)
- [set_text](#closebuttonset_text)
- [update](#closebuttonupdate)

### CloseButton.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.close_window

Close the window.

```py
def close_window(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.create

Create a Button widget.

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.get

Returns the text of the button..

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.get_text

Get the text of the button.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.set_button_color

Set the button color.

```py
def set_button_color(
    self, button_color: Union[str, tuple[str, str]], update: bool = True
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

### CloseButton.update

Update the widget.

```py
def update(
    self,
    text: Union[str, None] = None,
    disabled: Union[bool, None] = None,
    button_color: Union[str, tuple[str, str], None] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2238)

## ColorBrowse

ColorBrowse element.

```py
class ColorBrowse(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    default_color: Union[str, None] = None,
    title: str = "",
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### Methods of ColorBrowse

- [bind](#colorbrowsebind)
- [bind_events](#colorbrowsebind_events)
- [create](#colorbrowsecreate)
- [disptach_event](#colorbrowsedisptach_event)
- [get](#colorbrowseget)
- [get_height](#colorbrowseget_height)
- [get_name](#colorbrowseget_name)
- [get_prev_element](#colorbrowseget_prev_element)
- [get_width](#colorbrowseget_width)
- [post_create](#colorbrowsepost_create)
- [prepare_create](#colorbrowseprepare_create)
- [set_cursor](#colorbrowseset_cursor)
- [set_disabled](#colorbrowseset_disabled)
- [set_text](#colorbrowseset_text)
- [show_dialog](#colorbrowseshow_dialog)
- [update](#colorbrowseupdate)

### ColorBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

### ColorBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4389)

## Column

Frame element.

```py
class Column(
    self,
    layout: LayoutType,
    key: str = "",
    background_color: Union[str, None] = None,
    vertical_alignment: TextVAlign = "top",
    size: Union[tuple[int, int], None] = None,  # set (width, height) pixel size
    width: Union[int, None] = None,  # set pixel width
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Methods of Column

- [bind](#columnbind)
- [bind_events](#columnbind_events)
- [create](#columncreate)
- [disptach_event](#columndisptach_event)
- [get](#columnget)
- [get_height](#columnget_height)
- [get_name](#columnget_name)
- [get_prev_element](#columnget_prev_element)
- [get_width](#columnget_width)
- [post_create](#columnpost_create)
- [prepare_create](#columnprepare_create)
- [set_cursor](#columnset_cursor)
- [set_disabled](#columnset_disabled)
- [update](#columnupdate)

### Column.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.create

Create a Column element

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

### Column.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1600)

## Combo

Combo element.

```py
class Combo(
    self,
    values: list[str] = [],
    default_value: str = "",
    key: Union[str, None] = None,
    enable_events: bool = False,
    readonly: bool = False,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Methods of Combo

- [bind](#combobind)
- [bind_events](#combobind_events)
- [create](#combocreate)
- [disptach_event](#combodisptach_event)
- [get](#comboget)
- [get_height](#comboget_height)
- [get_name](#comboget_name)
- [get_prev_element](#comboget_prev_element)
- [get_width](#comboget_width)
- [post_create](#combopost_create)
- [prepare_create](#comboprepare_create)
- [set_cursor](#comboset_cursor)
- [set_disabled](#comboset_disabled)
- [set_readonly](#comboset_readonly)
- [set_value](#comboset_value)
- [set_values](#comboset_values)
- [update](#comboupdate)

### Combo.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.create

[Combo.create] create Listbox widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.set_value

Set the value of the widget.

```py
def set_value(self, v: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.set_values

Set values to list

```py
def set_values(self, values: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

### Combo.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3847)

## Element

Element class.

```py
class Element(
    self,
    element_type: str,  # element type
    ttk_style_name: str,  # tkinter widget type
    key: Optional[KeyType],  # key
    has_value: bool,  # has value
    metadata: Union[dict[str, Any], None] = None,  # meta data
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Methods of Element

- [bind](#elementbind)
- [bind_events](#elementbind_events)
- [create](#elementcreate)
- [disptach_event](#elementdisptach_event)
- [get](#elementget)
- [get_height](#elementget_height)
- [get_name](#elementget_name)
- [get_prev_element](#elementget_prev_element)
- [get_width](#elementget_width)
- [post_create](#elementpost_create)
- [prepare_create](#elementprepare_create)
- [set_cursor](#elementset_cursor)
- [set_disabled](#elementset_disabled)
- [update](#elementupdate)

### Element.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.create

Create a widget.

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

### Element.update

Update widget configuration.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1148)

## FileBrowse

FileBrowse element.

```py
class FileBrowse(
    self,
    button_text: str = "...",
    key: Union[str, int, None] = None,
    title: str = "",
    target_key: Union[str, None] = None,
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    multiple_files: bool = False,
    initial_folder: Union[str, None] = None,
    save_as: bool = False,
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### Methods of FileBrowse

- [bind](#filebrowsebind)
- [bind_events](#filebrowsebind_events)
- [create](#filebrowsecreate)
- [disptach_event](#filebrowsedisptach_event)
- [get](#filebrowseget)
- [get_height](#filebrowseget_height)
- [get_name](#filebrowseget_name)
- [get_prev_element](#filebrowseget_prev_element)
- [get_width](#filebrowseget_width)
- [post_create](#filebrowsepost_create)
- [prepare_create](#filebrowseprepare_create)
- [set_cursor](#filebrowseset_cursor)
- [set_disabled](#filebrowseset_disabled)
- [set_text](#filebrowseset_text)
- [show_dialog](#filebrowseshow_dialog)
- [update](#filebrowseupdate)

### FileBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[Any, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

### FileBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4194)

## FileSaveAs

FileSaveAs element. (alias of FileSaveAsBrowse)

```py
class FileSaveAs(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    title: str = "",
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### Methods of FileSaveAs

- [bind](#filesaveasbind)
- [bind_events](#filesaveasbind_events)
- [create](#filesaveascreate)
- [disptach_event](#filesaveasdisptach_event)
- [get](#filesaveasget)
- [get_height](#filesaveasget_height)
- [get_name](#filesaveasget_name)
- [get_prev_element](#filesaveasget_prev_element)
- [get_width](#filesaveasget_width)
- [post_create](#filesaveaspost_create)
- [prepare_create](#filesaveasprepare_create)
- [set_cursor](#filesaveasset_cursor)
- [set_disabled](#filesaveasset_disabled)
- [set_text](#filesaveasset_text)
- [show_dialog](#filesaveasshow_dialog)
- [update](#filesaveasupdate)

### FileSaveAs.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[Any, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAs.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

## FileSaveAsBrowse

FileSaveAsBrowse element.

```py
class FileSaveAsBrowse(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    title: str = "",
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### Methods of FileSaveAsBrowse

- [bind](#filesaveasbrowsebind)
- [bind_events](#filesaveasbrowsebind_events)
- [create](#filesaveasbrowsecreate)
- [disptach_event](#filesaveasbrowsedisptach_event)
- [get](#filesaveasbrowseget)
- [get_height](#filesaveasbrowseget_height)
- [get_name](#filesaveasbrowseget_name)
- [get_prev_element](#filesaveasbrowseget_prev_element)
- [get_width](#filesaveasbrowseget_width)
- [post_create](#filesaveasbrowsepost_create)
- [prepare_create](#filesaveasbrowseprepare_create)
- [set_cursor](#filesaveasbrowseset_cursor)
- [set_disabled](#filesaveasbrowseset_disabled)
- [set_text](#filesaveasbrowseset_text)
- [show_dialog](#filesaveasbrowseshow_dialog)
- [update](#filesaveasbrowseupdate)

### FileSaveAsBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[Any, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

### FileSaveAsBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4315)

## FilesBrowse

FilesBrowse element.

```py
class FilesBrowse(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    title: str = "",
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### Methods of FilesBrowse

- [bind](#filesbrowsebind)
- [bind_events](#filesbrowsebind_events)
- [create](#filesbrowsecreate)
- [disptach_event](#filesbrowsedisptach_event)
- [get](#filesbrowseget)
- [get_height](#filesbrowseget_height)
- [get_name](#filesbrowseget_name)
- [get_prev_element](#filesbrowseget_prev_element)
- [get_width](#filesbrowseget_width)
- [post_create](#filesbrowsepost_create)
- [prepare_create](#filesbrowseprepare_create)
- [set_cursor](#filesbrowseset_cursor)
- [set_disabled](#filesbrowseset_disabled)
- [set_text](#filesbrowseset_text)
- [show_dialog](#filesbrowseshow_dialog)
- [update](#filesbrowseupdate)

### FilesBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[Any, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

### FilesBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4288)

## FolderBrowse

FolderBrowse element.

```py
class FolderBrowse(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    default_path: Union[str, None] = None,
    title: str = "",
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### Methods of FolderBrowse

- [bind](#folderbrowsebind)
- [bind_events](#folderbrowsebind_events)
- [create](#folderbrowsecreate)
- [disptach_event](#folderbrowsedisptach_event)
- [get](#folderbrowseget)
- [get_height](#folderbrowseget_height)
- [get_name](#folderbrowseget_name)
- [get_prev_element](#folderbrowseget_prev_element)
- [get_width](#folderbrowseget_width)
- [post_create](#folderbrowsepost_create)
- [prepare_create](#folderbrowseprepare_create)
- [set_cursor](#folderbrowseset_cursor)
- [set_disabled](#folderbrowseset_disabled)
- [set_text](#folderbrowseset_text)
- [show_dialog](#folderbrowseshow_dialog)
- [update](#folderbrowseupdate)

### FolderBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

### FolderBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4348)

## Frame

Frame element.

```py
class Frame(
    self,
    title: str,
    layout: LayoutType,
    key: str = "",
    size: Union[tuple[int, int], None] = None,
    relief: ReliefType = "groove",
    # text props
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,
    text_color: Union[str, None] = None,
    background_color: Union[str, None] = None,  # background_color
    # pack props
    label_outside: bool = False,
    vertical_alignment: TextVAlign = "top",  # vertical alignment
    text_align: Union[TextAlign, None] = "left",  # text align
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    use_ttk: bool = False,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Methods of Frame

- [bind](#framebind)
- [bind_events](#framebind_events)
- [create](#framecreate)
- [disptach_event](#framedisptach_event)
- [get](#frameget)
- [get_height](#frameget_height)
- [get_name](#frameget_name)
- [get_prev_element](#frameget_prev_element)
- [get_width](#frameget_width)
- [post_create](#framepost_create)
- [prepare_create](#frameprepare_create)
- [set_cursor](#frameset_cursor)
- [set_disabled](#frameset_disabled)
- [update](#frameupdate)

### Frame.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.create

Create a Frame widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

### Frame.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1525)

## Graph

Graph element.

```py
class Graph(
    self,
    key: Union[str, None] = None,
    background_color: Union[str, None] = None,
    size: tuple[int, int] = (300, 300),
    canvas_size: Union[tuple[int, int], None] = None,
    graph_bottom_left: Union[tuple[int, int], None] = None,
    graph_top_right: Union[tuple[int, int], None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

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
- [get_height](#graphget_height)
- [get_name](#graphget_name)
- [get_prev_element](#graphget_prev_element)
- [get_width](#graphget_width)
- [post_create](#graphpost_create)
- [prepare_create](#graphprepare_create)
- [set_cursor](#graphset_cursor)
- [set_disabled](#graphset_disabled)
- [update](#graphupdate)

### Graph.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.create

Create Graph widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.draw_arc

Draw an arc.

```py
def draw_arc(
    self,
    top_left: PointType,
    bottom_right: PointType,
    extent: Union[int, None] = None,
    start_angle: Union[int, None] = None,
    style: Union[str, None] = None,
    arc_color: Union[str, None] = "black",
    line_width: int = 1,
    fill_color: Union[str, None] = None,
    ) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.draw_circle

Draw a circle.

```py
def draw_circle(
    self,
    center_location: PointType,
    radius: Union[int, float],
    fill_color: Union[str, None] = None,
    line_color: Union[str, None] = "black",
    line_width: int = 1,
    ) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.draw_image

Draw image

```py
def draw_image(
    self,
    filename: Union[str, None] = None,
    data: Union[bytes, None] = None,
    location: Union[PointType, None] = None,
    ) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.draw_line

Draw a line.

```py
def draw_line(
    self,
    point_from: PointType,
    point_to: PointType,
    color: str = "black",
    width: int = 1,
    ) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.draw_lines

Draw lines.

```py
def draw_lines(self, points: list[PointType], color="black", width=1) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.draw_oval

Draw an oval.

```py
def draw_oval(
    self,
    top_left: PointType,
    bottom_right: PointType,
    fill_color: Union[str, None] = None,
    line_color: Union[str, None] = None,
    line_width: int = 1,
    ):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.draw_point

Draw a point.

```py
def draw_point(self, point: PointType, size: int = 2, color: str = "black") -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.draw_polygon

Draw polygon

```py
def draw_polygon(
    self,
    points: list[PointType],
    fill_color: Union[str, None] = None,
    line_color: Union[str, None] = None,
    line_width: Union[int, None] = None,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.draw_rectangle

Draw rectangle

```py
def draw_rectangle(
    self,
    top_left: PointType,
    bottom_right: PointType,
    fill_color: Union[str, None] = None,
    line_color: Union[str, None] = None,
    line_width: Union[int, None] = None,
    ) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.draw_text

Draw text

```py
def draw_text(
    self,
    text: str,
    location: PointType,
    color: Union[str, None] = "black",
    font: Union[FontType, None] = None,
    angle: Union[float, str, None] = 0,
    text_location: TextAlign = tk.CENTER,
    ) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.erase

Delete all

```py
def erase(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

### Graph.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3302)

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
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### Methods of HSeparator

- [bind](#hseparatorbind)
- [bind_events](#hseparatorbind_events)
- [create](#hseparatorcreate)
- [disptach_event](#hseparatordisptach_event)
- [get](#hseparatorget)
- [get_height](#hseparatorget_height)
- [get_name](#hseparatorget_name)
- [get_prev_element](#hseparatorget_prev_element)
- [get_width](#hseparatorget_width)
- [post_create](#hseparatorpost_create)
- [prepare_create](#hseparatorprepare_create)
- [set_cursor](#hseparatorset_cursor)
- [set_disabled](#hseparatorset_disabled)
- [update](#hseparatorupdate)

### HSeparator.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.create

Create HSeparator widget.

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

### HSeparator.update

Update widget configuration.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3676)

## Image

Image element.

```py
class Image(
    self,
    source: Union[bytes, str, None] = None,  # image source
    filename=None,  # filen ame
    data: Union[bytes, PILImage.Image, None] = None,  # image data
    key: Union[str, None] = None,
    background_color: Union[
    tuple[int, int, int], str, None
    ] = None,  # background color (example) "red", "#FF0000"
    size: tuple[int, int] = (300, 300),
    resize_type: ImageResizeType = ImageResizeType.FIT_BOTH,
    enable_events: bool = False,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Methods of Image

- [bind](#imagebind)
- [bind_events](#imagebind_events)
- [create](#imagecreate)
- [disptach_event](#imagedisptach_event)
- [erase](#imageerase)
- [get](#imageget)
- [get_height](#imageget_height)
- [get_name](#imageget_name)
- [get_prev_element](#imageget_prev_element)
- [get_width](#imageget_width)
- [post_create](#imagepost_create)
- [prepare_create](#imageprepare_create)
- [screenshot](#imagescreenshot)
- [set_cursor](#imageset_cursor)
- [set_disabled](#imageset_disabled)
- [set_image](#imageset_image)
- [update](#imageupdate)

### Image.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.create

Create a Image widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.erase

Erase image

```py
def erase(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.screenshot

Take a screenshot

```py
def screenshot(self) -> PILImage.Image:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.set_image

Set image to Image widget.

- ImageResizeType is NO_RESIZE/FIT_HEIGHT/FIT_WIDTH/FIT_BOTH/IGNORE_ASPECT_RATIO/CROP_TO_SQUARE

```py
def set_image(
    self,
    source: Union[bytes, str, None] = None,
    filename: Union[str, None] = None,
    data: Union[bytes, PILImage.Image, None] = None,
    size: Union[tuple[int, int], None] = None,
    resize_type: ImageResizeType = ImageResizeType.FIT_BOTH,
    background_color: Union[
    tuple[int, int, int], str, None
    ] = None,  # background color (example) "red", "#FF0000"
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

### Image.update

Update the widget.

```py
def update(
    self,
    source: Union[bytes, str, None] = None,
    filename: Union[str, None] = None,
    data: Union[bytes, None] = None,
    size: Union[tuple[int, int], None] = None,
    resize_type: ImageResizeType = ImageResizeType.FIT_BOTH,
    background_color: Union[tuple[int, int, int], str, None] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3488)

## Input

Text input element.

```py
class Input(
    self,
    text: str = "",  # default text
    key: Union[str, None] = None,  # key
    default_text: Union[str, None] = None,  # same as text
    enable_events: bool = False,  # enabled events ([enter] or [change])
    enable_key_events: bool = False,  # enabled key events
    enable_focus_events: bool = False,  # enabled focus events
    readonly_background_color: Union[str, None] = "silver",
    password_char: Union[
    str, None
    ] = None,  # if you want to use it as a password input box, set "*"
    readonly: bool = False,  # read only box
    size: Union[
    tuple[int, int], None
    ] = None,  # set (width, height) character size (only width is supported)
    width: Union[int, None] = None,  # set width character size
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[str, None] = None,  # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

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
- [get_height](#inputget_height)
- [get_name](#inputget_name)
- [get_prev_element](#inputget_prev_element)
- [get_selected_text](#inputget_selected_text)
- [get_selection_length](#inputget_selection_length)
- [get_selection_pos](#inputget_selection_pos)
- [get_selection_start](#inputget_selection_start)
- [get_text](#inputget_text)
- [get_width](#inputget_width)
- [paste](#inputpaste)
- [post_create](#inputpost_create)
- [prepare_create](#inputprepare_create)
- [select_all](#inputselect_all)
- [set_cursor](#inputset_cursor)
- [set_cursor_pos](#inputset_cursor_pos)
- [set_disabled](#inputset_disabled)
- [set_readonly](#inputset_readonly)
- [set_selection_start](#inputset_selection_start)
- [set_text](#inputset_text)
- [update](#inputupdate)

### Input.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.copy

Copy to clipboard

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.copy_selected_text

Copy selected text

```py
def copy_selected_text(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.create

Create Input widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.cut

Cut to clipboard

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.delete_selected

Delete selected text

```py
def delete_selected(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.get_cursor_pos

Get cursor position

```py
def get_cursor_pos(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.get_selected_text

Get selected text

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.get_selection_length

Get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.get_selection_pos

Get selection positions

```py
def get_selection_pos(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.get_selection_start

Get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.get_text

Get text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.paste

Paste from clipboard

```py
def paste(self):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.select_all

select_all

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.set_cursor_pos

Set cursor position

```py
def set_cursor_pos(self, index: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.set_selection_start

Set selection start and length

```py
def set_selection_start(self, sel_start: int, sel_length: int = 0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### Input.update

Update the widget.

```py
def update(
    self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

## InputText

InputText element. (alias of Input)

```py
class InputText(
    self,
    text: str = "",  # default text
    key: Union[str, None] = None,  # key
    default_text: Union[str, None] = None,  # same as text
    enable_events: bool = False,  # enabled events ([enter] or [change])
    enable_key_events: bool = False,  # enabled key events
    enable_focus_events: bool = False,  # enabled focus events
    readonly_background_color: Union[str, None] = "silver",
    password_char: Union[
    str, None
    ] = None,  # if you want to use it as a password input box, set "*"
    readonly: bool = False,  # read only box
    size: Union[
    tuple[int, int], None
    ] = None,  # set (width, height) character size (only width is supported)
    width: Union[int, None] = None,  # set width character size
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[str, None] = None,  # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

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
- [get_height](#inputtextget_height)
- [get_name](#inputtextget_name)
- [get_prev_element](#inputtextget_prev_element)
- [get_selected_text](#inputtextget_selected_text)
- [get_selection_length](#inputtextget_selection_length)
- [get_selection_pos](#inputtextget_selection_pos)
- [get_selection_start](#inputtextget_selection_start)
- [get_text](#inputtextget_text)
- [get_width](#inputtextget_width)
- [paste](#inputtextpaste)
- [post_create](#inputtextpost_create)
- [prepare_create](#inputtextprepare_create)
- [select_all](#inputtextselect_all)
- [set_cursor](#inputtextset_cursor)
- [set_cursor_pos](#inputtextset_cursor_pos)
- [set_disabled](#inputtextset_disabled)
- [set_readonly](#inputtextset_readonly)
- [set_selection_start](#inputtextset_selection_start)
- [set_text](#inputtextset_text)
- [update](#inputtextupdate)

### InputText.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.copy

Copy to clipboard

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.copy_selected_text

Copy selected text

```py
def copy_selected_text(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.create

Create Input widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.cut

Cut to clipboard

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.delete_selected

Delete selected text

```py
def delete_selected(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.get_cursor_pos

Get cursor position

```py
def get_cursor_pos(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.get_selected_text

Get selected text

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.get_selection_length

Get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.get_selection_pos

Get selection positions

```py
def get_selection_pos(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.get_selection_start

Get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.get_text

Get text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.paste

Paste from clipboard

```py
def paste(self):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.select_all

select_all

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.set_cursor_pos

Set cursor position

```py
def set_cursor_pos(self, index: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.set_selection_start

Set selection start and length

```py
def set_selection_start(self, sel_start: int, sel_length: int = 0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

### InputText.update

Update the widget.

```py
def update(
    self, text: Union[str, None] = None, readonly: Union[bool, None] = None, **kw
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2461)

## Label

Label element (alias of Text)

```py
class Label(
    self,
    text: str = "",
    key: Union[str, None] = None,
    enable_events: bool = False,  # enabled events (click)
    wrap_length: Union[int, None] = None,  # wrap length(unit=pixel)
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[str, None] = None,  # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,  # user metadata
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Methods of Label

- [bind](#labelbind)
- [bind_events](#labelbind_events)
- [create](#labelcreate)
- [disptach_event](#labeldisptach_event)
- [get](#labelget)
- [get_height](#labelget_height)
- [get_name](#labelget_name)
- [get_prev_element](#labelget_prev_element)
- [get_text](#labelget_text)
- [get_width](#labelget_width)
- [post_create](#labelpost_create)
- [prepare_create](#labelprepare_create)
- [set_cursor](#labelset_cursor)
- [set_disabled](#labelset_disabled)
- [set_text](#labelset_text)
- [update](#labelupdate)

### Label.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Label.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

## ListBrowse

ListBrowse element.

```py
class ListBrowse(
    self,
    values: list[str] = [],
    message: str = "",
    button_text: str = "...",
    default_value: Union[str, None] = None,  # default value
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    title: str = "",
    font: Union[FontType, None] = None,
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### Methods of ListBrowse

- [bind](#listbrowsebind)
- [bind_events](#listbrowsebind_events)
- [create](#listbrowsecreate)
- [disptach_event](#listbrowsedisptach_event)
- [get](#listbrowseget)
- [get_height](#listbrowseget_height)
- [get_name](#listbrowseget_name)
- [get_prev_element](#listbrowseget_prev_element)
- [get_width](#listbrowseget_width)
- [post_create](#listbrowsepost_create)
- [prepare_create](#listbrowseprepare_create)
- [set_cursor](#listbrowseset_cursor)
- [set_disabled](#listbrowseset_disabled)
- [set_text](#listbrowseset_text)
- [show_dialog](#listbrowseshow_dialog)
- [update](#listbrowseupdate)

### ListBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.show_dialog

Show Listbox dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

### ListBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4430)

## Listbox

Listbox element.

```py
class Listbox(
    self,
    values: list[str] = [],
    default_values: Union[list[str], None] = None,  # selected values
    default_value: Union[str, None] = None,  # a default value
    key: Union[str, None] = None,
    enable_events: bool = False,
    select_mode: ListboxSelectMode = LISTBOX_SELECT_MODE_BROWSE,
    # other
    metadata: Union[dict[str, Any], None] = None,
    items: Union[list[str], None] = None,  # same as values (alias values)
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Methods of Listbox

- [bind](#listboxbind)
- [bind_events](#listboxbind_events)
- [create](#listboxcreate)
- [disptach_event](#listboxdisptach_event)
- [get](#listboxget)
- [get_cursor_index](#listboxget_cursor_index)
- [get_height](#listboxget_height)
- [get_name](#listboxget_name)
- [get_prev_element](#listboxget_prev_element)
- [get_selected_items](#listboxget_selected_items)
- [get_width](#listboxget_width)
- [post_create](#listboxpost_create)
- [prepare_create](#listboxprepare_create)
- [select_values](#listboxselect_values)
- [set_cursor](#listboxset_cursor)
- [set_cursor_index](#listboxset_cursor_index)
- [set_disabled](#listboxset_disabled)
- [set_values](#listboxset_values)
- [update](#listboxupdate)

### Listbox.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.create

[Listbox.create] create Listbox widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.get_cursor_index

Get cursor index (return -1 if not selected)

```py
def get_cursor_index(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.get_selected_items

Get selected items

```py
def get_selected_items(self) -> list[str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.select_values

Select values in Listbox.

**example**
```py
import TkEasyGUI as eg
with eg.Window("Sample", layout=[
    [eg.Listbox(["A", "B", "C"], key="a_list", select_mode="multiple")],
    [eg.Button("Select")],
]) as win:
    for event, values in win.event_iter():
        if event == "Select":
            win["a_list"].select_values(["A", "B"]) # select A and B
```

```py
def select_values(self, values: Union[list[str], None]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.set_cursor_index

Set cursor index

```py
def set_cursor_index(self, index: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.set_values

Set values to list

```py
def set_values(self, values: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

### Listbox.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3704)

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
    items: Union[list[list[Union[str, list[Any]]]], None] = None,
    menu_definition: Union[list[list[Union[str, list[Any]]]], None] = None,
    key: Union[str, None] = None,
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Methods of Menu

- [bind](#menubind)
- [bind_events](#menubind_events)
- [create](#menucreate)
- [disptach_event](#menudisptach_event)
- [get](#menuget)
- [get_height](#menuget_height)
- [get_name](#menuget_name)
- [get_prev_element](#menuget_prev_element)
- [get_text](#menuget_text)
- [get_width](#menuget_width)
- [post_create](#menupost_create)
- [prepare_create](#menuprepare_create)
- [set_cursor](#menuset_cursor)
- [set_disabled](#menuset_disabled)
- [set_text](#menuset_text)
- [update](#menuupdate)

### Menu.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

### Menu.update

Update the widget.

```py
def update(
    self,
    menu_definition: Union[list[list[Union[str, list[Any]]]], None] = None,
    *args,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1992)

## Multiline

Multiline text input element.

```py
class Multiline(
    self,
    text: str = "",  # default text
    default_text: Union[str, None] = None,  # same as text
    key: Union[str, None] = None,  # key
    readonly: bool = False,
    enable_events: bool = False,
    enable_key_events: bool = False,
    enable_focus_events: bool = False,
    size: tuple[int, int] = (50, 10),  # element size (unit=character)
    # text props
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[str, None] = None,  # background color
    text_align: Union[TextAlign, None] = None,  # text align
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    autoscroll: bool = False,  # When autoscroll is set to True, it scrolls to the end with text changes.
    readonly_background_color: Union[str, None] = None,
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Methods of Multiline

- [bind](#multilinebind)
- [bind_events](#multilinebind_events)
- [copy](#multilinecopy)
- [create](#multilinecreate)
- [cut](#multilinecut)
- [disptach_event](#multilinedisptach_event)
- [get](#multilineget)
- [get_cursor_pos](#multilineget_cursor_pos)
- [get_height](#multilineget_height)
- [get_name](#multilineget_name)
- [get_prev_element](#multilineget_prev_element)
- [get_selected_text](#multilineget_selected_text)
- [get_selection_length](#multilineget_selection_length)
- [get_selection_pos](#multilineget_selection_pos)
- [get_selection_start](#multilineget_selection_start)
- [get_text](#multilineget_text)
- [get_width](#multilineget_width)
- [index_to_pos](#multilineindex_to_pos)
- [paste](#multilinepaste)
- [pos_to_index](#multilinepos_to_index)
- [post_create](#multilinepost_create)
- [prepare_create](#multilineprepare_create)
- [print](#multilineprint)
- [select_all](#multilineselect_all)
- [set_cursor](#multilineset_cursor)
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
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.get_selection_length

Get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.get_selection_start

Get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.print

Print text.

```py
def print(
    self,
    text: str,
    text_color: Union[str, None] = None,
    background_color: Union[str, None] = None,
    end: str = "\n",
    autoscroll: bool = False,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.select_all

Select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.set_selection_start

Set selection start

```py
def set_selection_start(self, index: int, sel_length: int = 0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Multiline.update

Update the widget.

```py
def update(
    self,
    text: Union[str, None] = None,
    readonly: Union[bool, None] = None,
    autoscroll: Union[
    bool, None
    ] = None,  # When autoscroll is set to True, it scrolls to the end with text changes.
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

## MultilineBrowse

MultilineBrowse element.

```py
class MultilineBrowse(
    self,
    message: str = "",
    key: Union[str, None] = None,
    button_text: str = "...",
    target_key: Union[str, None] = None,
    title: str = "",
    font: Union[FontType, None] = None,
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### Methods of MultilineBrowse

- [bind](#multilinebrowsebind)
- [bind_events](#multilinebrowsebind_events)
- [create](#multilinebrowsecreate)
- [disptach_event](#multilinebrowsedisptach_event)
- [get](#multilinebrowseget)
- [get_height](#multilinebrowseget_height)
- [get_name](#multilinebrowseget_name)
- [get_prev_element](#multilinebrowseget_prev_element)
- [get_width](#multilinebrowseget_width)
- [post_create](#multilinebrowsepost_create)
- [prepare_create](#multilinebrowseprepare_create)
- [set_cursor](#multilinebrowseset_cursor)
- [set_disabled](#multilinebrowseset_disabled)
- [set_text](#multilinebrowseset_text)
- [show_dialog](#multilinebrowseshow_dialog)
- [update](#multilinebrowseupdate)

### MultilineBrowse.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.show_dialog

Show Listbox dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

### MultilineBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4484)

## Output

Output element. (alias of Multiline) TODO: implement

```py
class Output(
    self,
    text: str = "",  # default text
    default_text: Union[str, None] = None,  # same as text
    key: Union[str, None] = None,  # key
    readonly: bool = False,
    enable_events: bool = False,
    enable_key_events: bool = False,
    enable_focus_events: bool = False,
    size: tuple[int, int] = (50, 10),  # element size (unit=character)
    # text props
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[str, None] = None,  # background color
    text_align: Union[TextAlign, None] = None,  # text align
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    autoscroll: bool = False,  # When autoscroll is set to True, it scrolls to the end with text changes.
    readonly_background_color: Union[str, None] = None,
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Methods of Output

- [bind](#outputbind)
- [bind_events](#outputbind_events)
- [copy](#outputcopy)
- [create](#outputcreate)
- [cut](#outputcut)
- [disptach_event](#outputdisptach_event)
- [get](#outputget)
- [get_cursor_pos](#outputget_cursor_pos)
- [get_height](#outputget_height)
- [get_name](#outputget_name)
- [get_prev_element](#outputget_prev_element)
- [get_selected_text](#outputget_selected_text)
- [get_selection_length](#outputget_selection_length)
- [get_selection_pos](#outputget_selection_pos)
- [get_selection_start](#outputget_selection_start)
- [get_text](#outputget_text)
- [get_width](#outputget_width)
- [index_to_pos](#outputindex_to_pos)
- [paste](#outputpaste)
- [pos_to_index](#outputpos_to_index)
- [post_create](#outputpost_create)
- [prepare_create](#outputprepare_create)
- [print](#outputprint)
- [select_all](#outputselect_all)
- [set_cursor](#outputset_cursor)
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
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.get_selection_length

Get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.get_selection_start

Get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.print

Print text.

```py
def print(
    self,
    text: str,
    text_color: Union[str, None] = None,
    background_color: Union[str, None] = None,
    end: str = "\n",
    autoscroll: bool = False,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.select_all

Select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.set_selection_start

Set selection start

```py
def set_selection_start(self, index: int, sel_length: int = 0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Output.update

Update the widget.

```py
def update(
    self,
    text: Union[str, None] = None,
    readonly: Union[bool, None] = None,
    autoscroll: Union[
    bool, None
    ] = None,  # When autoscroll is set to True, it scrolls to the end with text changes.
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

## Push

An element for achieving right alignment and center alignment.

**Example**
```py
win = sg.Window(
    title="Hello World",
    layout=[
        [sg.Text("=" * 50)],
        [sg.Push(), sg.Button("Hello World")],  # right alignment
        [sg.Push(), sg.Button("OK"), sg.Push()], # center alignment
    ])
while win.is_running():
    event, values = win.read()
```

```py
class Push(
    self, metadata: Union[dict[str, Any], None] = None, **kw  # user metadata
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Methods of Push

- [bind](#pushbind)
- [bind_events](#pushbind_events)
- [create](#pushcreate)
- [disptach_event](#pushdisptach_event)
- [get](#pushget)
- [get_height](#pushget_height)
- [get_name](#pushget_name)
- [get_prev_element](#pushget_prev_element)
- [get_text](#pushget_text)
- [get_width](#pushget_width)
- [post_create](#pushpost_create)
- [prepare_create](#pushprepare_create)
- [set_cursor](#pushset_cursor)
- [set_disabled](#pushset_disabled)
- [set_text](#pushset_text)
- [update](#pushupdate)

### Push.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

### Push.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1932)

## Radio

Checkbox element.

```py
class Radio(
    self,
    text: str = "",
    group_id: Union[int, str] = "group",
    default: bool = False,
    key: Union[str, None] = None,
    enable_events: bool = False,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Methods of Radio

- [bind](#radiobind)
- [bind_events](#radiobind_events)
- [create](#radiocreate)
- [disptach_event](#radiodisptach_event)
- [get](#radioget)
- [get_height](#radioget_height)
- [get_name](#radioget_name)
- [get_prev_element](#radioget_prev_element)
- [get_value](#radioget_value)
- [get_width](#radioget_width)
- [is_selected](#radiois_selected)
- [post_create](#radiopost_create)
- [prepare_create](#radioprepare_create)
- [select](#radioselect)
- [set_cursor](#radioset_cursor)
- [set_disabled](#radioset_disabled)
- [set_text](#radioset_text)
- [update](#radioupdate)

### Radio.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.create

Create a Radio widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.get_value

Returns the id of an element within a group.

```py
def get_value(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.is_selected

Check if the radio button is selected.

```py
def is_selected(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.select

Select the radio button.

```py
def select(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

### Radio.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2356)

## Slider

Slider element.

```py
class Slider(
    self,
    range: tuple[float, float] = (1, 10),  # value range (from, to)
    default_value: Union[float, None] = None,  # default value
    resolution: float = 1,  # value resolution
    orientation: OrientationType = "horizontal",  # orientation (h|v|horizontal|vertical)
    tick_interval: Union[float, None] = None,  # tick marks interval on the scale
    enable_events: bool = False,  # enable changing events
    enable_changed_events: bool = False,  # enable changed event
    disable_number_display: bool = False,  # hide number display
    size: Union[
    tuple[int, int], None
    ] = None,  # size (unit: character) / horizontal: (bar_length, thumb_size), vertical: (thumb_size, bar_length)
    key: Union[str, None] = None,
    # other
    default: Union[float, None] = None,  # same as default_value
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Methods of Slider

- [bind](#sliderbind)
- [bind_events](#sliderbind_events)
- [create](#slidercreate)
- [disptach_event](#sliderdisptach_event)
- [get](#sliderget)
- [get_height](#sliderget_height)
- [get_name](#sliderget_name)
- [get_prev_element](#sliderget_prev_element)
- [get_range](#sliderget_range)
- [get_width](#sliderget_width)
- [post_create](#sliderpost_create)
- [prepare_create](#sliderprepare_create)
- [set](#sliderset)
- [set_cursor](#sliderset_cursor)
- [set_disabled](#sliderset_disabled)
- [set_range](#sliderset_range)
- [update](#sliderupdate)

### Slider.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.create

Create the widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.get

Return slider value.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.get_range

Get the range of the slider.

```py
def get_range(self) -> tuple[float, float]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.set

Set value of Slider

```py
def set(self, value: float) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.set_range

Set the range of the slider.

```py
def set_range(self, from_: float, to: float) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

### Slider.update

Update the widget.

```py
def update(
    self,
    value: Union[float, None] = None,
    range: Union[tuple[float, float], None] = None,
    disable_number_display: Union[bool, None] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3112)

## Submit

Subtmi element. (Alias of Button) : todo: add submit event

```py
class Submit(
    self,
    button_text: str = "Button",
    key: Union[str, None] = None,
    disabled: bool = False,
    size: Union[tuple[int, int], None] = None,
    tooltip: Union[str, None] = None,  # (TODO) tooltip
    button_color: Union[str, tuple[str, str], None] = None,
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[
    str, None
    ] = None,  # background color (not supported on macOS)
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    use_ttk_buttons: bool = False,
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Methods of Submit

- [bind](#submitbind)
- [bind_events](#submitbind_events)
- [create](#submitcreate)
- [disptach_event](#submitdisptach_event)
- [get](#submitget)
- [get_height](#submitget_height)
- [get_name](#submitget_name)
- [get_prev_element](#submitget_prev_element)
- [get_text](#submitget_text)
- [get_width](#submitget_width)
- [post_create](#submitpost_create)
- [prepare_create](#submitprepare_create)
- [set_button_color](#submitset_button_color)
- [set_cursor](#submitset_cursor)
- [set_disabled](#submitset_disabled)
- [set_text](#submitset_text)
- [update](#submitupdate)

### Submit.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.create

Create a Button widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.get

Returns the text of the button..

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.get_text

Get the text of the button.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.set_button_color

Set the button color.

```py
def set_button_color(
    self, button_color: Union[str, tuple[str, str]], update: bool = True
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

### Submit.update

Update the widget.

```py
def update(
    self,
    text: Union[str, None] = None,
    disabled: Union[bool, None] = None,
    button_color: Union[str, tuple[str, str], None] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2108)

## Tab

(experimental) Tab element - Tab is used together with TabGroup.

**Example:**
```py
import TkEasyGUI as sg
# Tab's Layout
tab1_layout = [[sg.Text("Tab1")], [sg.Input(key="input1")], [sg.Button("Read1")]]
tab2_layout = [[sg.Text("Tab2")], [sg.Input(key="input2")], [sg.Button("Read2")]]
# Main Layout
layout = [[
    sg.TabGroup([[
        sg.Tab("Tab title1", tab1_layout),
        sg.Tab("Tab title2", tab2_layout),
    ]])],
    [sg.Button("Quit")]]
# create window and event loop
with sg.Window("Tab Demo", layout) as window:
    for event, values in window:
        pass
```

```py
class Tab(
    self,
    title: str,
    layout: LayoutType,
    key: str = "",
    background_color: Union[str, None] = None,
    vertical_alignment: TextVAlign = "top",
    size: Union[tuple[int, int], None] = None,
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Methods of Tab

- [bind](#tabbind)
- [bind_events](#tabbind_events)
- [create](#tabcreate)
- [disptach_event](#tabdisptach_event)
- [get](#tabget)
- [get_height](#tabget_height)
- [get_name](#tabget_name)
- [get_prev_element](#tabget_prev_element)
- [get_width](#tabget_width)
- [post_create](#tabpost_create)
- [prepare_create](#tabprepare_create)
- [set_cursor](#tabset_cursor)
- [set_disabled](#tabset_disabled)
- [update](#tabupdate)

### Tab.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.create

Create a Tab element.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.get

Return Widget title

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

### Tab.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1686)

## TabGroup

(experimental) TabGroup element - Specify the Tab element for the child elements.

**Example:**
```py
import TkEasyGUI as sg
# Tab's Layout
tab1_layout = [[sg.Text("Tab1")], [sg.Input(key="input1")], [sg.Button("Read1")]]
tab2_layout = [[sg.Text("Tab2")], [sg.Input(key="input2")], [sg.Button("Read2")]]
# Main Layout
layout = [[
    sg.TabGroup([[
        sg.Tab("Tab title1", tab1_layout),
        sg.Tab("Tab title2", tab2_layout),
    ]])],
    [sg.Button("Quit")]]
# create window and event loop
with sg.Window("Tab Demo", layout) as window:
    for event, values in window:
        pass
```

```py
class TabGroup(
    self,
    layout: Union[list[list[Tab]], list[Tab]],
    key: str = "",
    background_color: Union[str, None] = None,
    vertical_alignment: TextVAlign = "top",
    size: Union[tuple[int, int], None] = None,
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    # pack props
    expand_x: bool = True,
    expand_y: bool = True,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### Methods of TabGroup

- [bind](#tabgroupbind)
- [bind_events](#tabgroupbind_events)
- [create](#tabgroupcreate)
- [disptach_event](#tabgroupdisptach_event)
- [get](#tabgroupget)
- [get_height](#tabgroupget_height)
- [get_name](#tabgroupget_name)
- [get_prev_element](#tabgroupget_prev_element)
- [get_width](#tabgroupget_width)
- [post_create](#tabgrouppost_create)
- [prepare_create](#tabgroupprepare_create)
- [set_cursor](#tabgroupset_cursor)
- [set_disabled](#tabgroupset_disabled)
- [update](#tabgroupupdate)

### TabGroup.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.create

Create a TabGroup element.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

### TabGroup.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1770)

## Table

Table element.

```py
class Table(
    self,
    values: list[list[str]] = [],  # Specify the table values as 2D list.
    headings: list[str] = [],  # Specify the table header as a list.
    key: Union[str, None] = None,
    justification: TextAlign = "center",
    auto_size_columns: bool = True,
    max_col_width: int = 0,
    col_widths: Union[list[int], None] = None,
    enable_events: bool = False,
    event_returns_values: Union[
    bool, None
    ] = None,  # Returns the table value if set to True, otherwise returns the index.
    select_mode: str = "browse",
    max_columns: int = 20,  # This property cannot be changed later. It is advisable to set a larger value.
    vertical_scroll_only: bool = True,  # vertical scroll only
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[str, None] = None,  # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Methods of Table

- [bind](#tablebind)
- [bind_events](#tablebind_events)
- [create](#tablecreate)
- [disptach_event](#tabledisptach_event)
- [get](#tableget)
- [get_height](#tableget_height)
- [get_name](#tableget_name)
- [get_prev_element](#tableget_prev_element)
- [get_width](#tableget_width)
- [load_from_file](#tableload_from_file)
- [post_create](#tablepost_create)
- [prepare_create](#tableprepare_create)
- [set_cursor](#tableset_cursor)
- [set_disabled](#tableset_disabled)
- [set_values](#tableset_values)
- [update](#tableupdate)

### Table.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.create

Create a Table widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.load_from_file

Load data from a file.

```py
def load_from_file(
    self,
    filename: str,
    delimiter: str = ",",
    encoding: str = "UTF-8",
    use_header: bool = True,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.set_values

Set values to the table.

```py
def set_values(
    self, values: list[list[str]], headings: Union[list[str], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

### Table.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3927)

## Text

Text element.

```py
class Text(
    self,
    text: str = "",
    key: Union[str, None] = None,
    enable_events: bool = False,  # enabled events (click)
    wrap_length: Union[int, None] = None,  # wrap length(unit=pixel)
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[str, None] = None,  # background color
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,  # user metadata
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Methods of Text

- [bind](#textbind)
- [bind_events](#textbind_events)
- [create](#textcreate)
- [disptach_event](#textdisptach_event)
- [get](#textget)
- [get_height](#textget_height)
- [get_name](#textget_name)
- [get_prev_element](#textget_prev_element)
- [get_text](#textget_text)
- [get_width](#textget_width)
- [post_create](#textpost_create)
- [prepare_create](#textprepare_create)
- [set_cursor](#textset_cursor)
- [set_disabled](#textset_disabled)
- [set_text](#textset_text)
- [update](#textupdate)

### Text.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

### Text.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1842)

## Textarea

Textarea element. (alias of Multiline)

```py
class Textarea(
    self,
    text: str = "",  # default text
    default_text: Union[str, None] = None,  # same as text
    key: Union[str, None] = None,  # key
    readonly: bool = False,
    enable_events: bool = False,
    enable_key_events: bool = False,
    enable_focus_events: bool = False,
    size: tuple[int, int] = (50, 10),  # element size (unit=character)
    # text props
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[str, None] = None,  # background color
    text_align: Union[TextAlign, None] = None,  # text align
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    autoscroll: bool = False,  # When autoscroll is set to True, it scrolls to the end with text changes.
    readonly_background_color: Union[str, None] = None,
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Methods of Textarea

- [bind](#textareabind)
- [bind_events](#textareabind_events)
- [copy](#textareacopy)
- [create](#textareacreate)
- [cut](#textareacut)
- [disptach_event](#textareadisptach_event)
- [get](#textareaget)
- [get_cursor_pos](#textareaget_cursor_pos)
- [get_height](#textareaget_height)
- [get_name](#textareaget_name)
- [get_prev_element](#textareaget_prev_element)
- [get_selected_text](#textareaget_selected_text)
- [get_selection_length](#textareaget_selection_length)
- [get_selection_pos](#textareaget_selection_pos)
- [get_selection_start](#textareaget_selection_start)
- [get_text](#textareaget_text)
- [get_width](#textareaget_width)
- [index_to_pos](#textareaindex_to_pos)
- [paste](#textareapaste)
- [pos_to_index](#textareapos_to_index)
- [post_create](#textareapost_create)
- [prepare_create](#textareaprepare_create)
- [print](#textareaprint)
- [select_all](#textareaselect_all)
- [set_cursor](#textareaset_cursor)
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
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.get_selection_length

Get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.get_selection_start

Get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.print

Print text.

```py
def print(
    self,
    text: str,
    text_color: Union[str, None] = None,
    background_color: Union[str, None] = None,
    end: str = "\n",
    autoscroll: bool = False,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.select_all

Select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.set_selection_start

Set selection start

```py
def set_selection_start(self, index: int, sel_length: int = 0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

### Textarea.update

Update the widget.

```py
def update(
    self,
    text: Union[str, None] = None,
    readonly: Union[bool, None] = None,
    autoscroll: Union[
    bool, None
    ] = None,  # When autoscroll is set to True, it scrolls to the end with text changes.
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2753)

## TkEasyError

TkEasyError Exception class.

```py
class TkEasyError(self, message="TkEasyError"):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L83)

### Methods of TkEasyError



### TkEasyError.add_note

Exception.add_note(note) --
    add a note to the exception

### TkEasyError.args

### TkEasyError.with_traceback

Exception.with_traceback(tb) --
    set self.__traceback__ to tb and return self.

## VPush

An element that inserts flexible space above or below to shift the layout to the center or bottom.

**Example**
```py
import TkEasyGUI as eg

layout = [
    [eg.VPush()],
    [eg.Push(), eg.Text("== Middle =="), eg.Push()],
    [eg.Push(), eg.Button("OK"), eg.Push()],
    [eg.VPush()],
]

window = eg.Window(title="VPush Test", layout=layout, size=(400, 350))
while window.is_alive():
    event, values = window.read(timeout=1000)
    if event == eg.WIN_CLOSED or event == "OK":
        break
```

```py
class VPush(
    self, metadata: Union[dict[str, Any], None] = None, **kw  # user metadata
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### Methods of VPush

- [bind](#vpushbind)
- [bind_events](#vpushbind_events)
- [create](#vpushcreate)
- [disptach_event](#vpushdisptach_event)
- [get](#vpushget)
- [get_height](#vpushget_height)
- [get_name](#vpushget_name)
- [get_prev_element](#vpushget_prev_element)
- [get_text](#vpushget_text)
- [get_width](#vpushget_width)
- [post_create](#vpushpost_create)
- [prepare_create](#vpushprepare_create)
- [set_cursor](#vpushset_cursor)
- [set_disabled](#vpushset_disabled)
- [set_text](#vpushset_text)
- [update](#vpushupdate)

### VPush.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

### VPush.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1962)

## VSeparator

VSeparator element.

```py
class VSeparator(
    self,
    key: Union[str, None] = None,
    background_color: Union[str, None] = None,
    pad: PadType = 5,
    size: tuple[int, int] = (5, 100),
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### Methods of VSeparator

- [bind](#vseparatorbind)
- [bind_events](#vseparatorbind_events)
- [create](#vseparatorcreate)
- [disptach_event](#vseparatordisptach_event)
- [get](#vseparatorget)
- [get_height](#vseparatorget_height)
- [get_name](#vseparatorget_name)
- [get_prev_element](#vseparatorget_prev_element)
- [get_width](#vseparatorget_width)
- [post_create](#vseparatorpost_create)
- [prepare_create](#vseparatorprepare_create)
- [set_cursor](#vseparatorset_cursor)
- [set_disabled](#vseparatorset_disabled)
- [update](#vseparatorupdate)

### VSeparator.bind

Bind event. @see [Window.bind](#windowbind)

```py
def bind(
    self,
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.create

Create VSeparator widget.

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

### VSeparator.update

Update widget configuration.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3648)

## Window

Main window object in TkEasyGUI

```py
class Window(
    self,
    title: str,
    layout: LayoutType,  # set elements layout
    size: Union[tuple[int, int], None] = None,  # window size
    resizable: bool = False,
    font: Optional[FontType] = None,
    modal: bool = False,  # modal window
    keep_on_top: bool = False,  # keep on top
    no_titlebar: bool = False,  # hide titlebar
    grab_anywhere: bool = False,  # can move window by dragging anywhere
    alpha_channel: float = 1.0,  # window alpha channel
    enable_key_events: bool = False,  # enable keyboard events (post WINDOW_KEY_EVENT)
    enable_show_events: bool = False,  # enable window show/hide events (post WINDOW_SHOW_EVENT)
    enable_mouse_events: bool = False,  # enable mouse events (post WINDOW_MOUSE_EVENT)
    enable_resize_events: bool = False,  # enable resize events (post WINDOW_RESIZE_EVENT)
    return_keyboard_events: bool = False,  # enable keyboard events (for compatibility)
    location: Union[tuple[int, int], None] = None,  # window location
    center_window: bool = True,  # move window to center
    row_padding: int = 2,  # row padding
    padding_x: int = 8,  # x padding around the window
    padding_y: int = 8,  # y padding around the window
    icon: Optional[str] = None,  # window icon, specify filename
    key: Optional[str] = None,  # window key for enable_show_events
    is_hidden: bool = False,  # hidden window
    element_justification: ElementJustifcation = "left",  # element justification
    show_scrollbar: bool = False,  # show scrollbar (Experimental)
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Methods of Window

- [bind](#windowbind)
- [cancel_close](#windowcancel_close)
- [close](#windowclose)
- [event_iter](#windowevent_iter)
- [focus](#windowfocus)
- [focus_element](#windowfocus_element)
- [get_center_location](#windowget_center_location)
- [get_element_by_key](#windowget_element_by_key)
- [get_elements_by_type](#windowget_elements_by_type)
- [get_location](#windowget_location)
- [get_screen_size](#windowget_screen_size)
- [get_size](#windowget_size)
- [get_values](#windowget_values)
- [hide](#windowhide)
- [hide_titlebar](#windowhide_titlebar)
- [is_alive](#windowis_alive)
- [is_running](#windowis_running)
- [keep_on_top](#windowkeep_on_top)
- [maximize](#windowmaximize)
- [minimize](#windowminimize)
- [move](#windowmove)
- [move_to_center](#windowmove_to_center)
- [normal](#windownormal)
- [post_event](#windowpost_event)
- [post_event_after](#windowpost_event_after)
- [read](#windowread)
- [refresh](#windowrefresh)
- [register_event_hooks](#windowregister_event_hooks)
- [send_to_back](#windowsend_to_back)
- [set_alpha_channel](#windowset_alpha_channel)
- [set_grab_anywhere](#windowset_grab_anywhere)
- [set_location](#windowset_location)
- [set_size](#windowset_size)
- [set_timeout](#windowset_timeout)
- [set_title](#windowset_title)
- [show](#windowshow)
- [start_thread](#windowstart_thread)
- [un_hide](#windowun_hide)
- [update_idle_tasks](#windowupdate_idle_tasks)

### Window.bind

[Window.bind] Bind element event and handler

```py
def bind(
    self,
    element: "Element",
    event_name: str,
    handle_name: str,
    propagate: bool = True,
    event_mode: EventMode = "user",
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.cancel_close

Cancel the close event.

```py
def cancel_close(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.close

Close the window.

```py
def close(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

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
def event_iter(
    self, timeout: Union[int, None] = None, timeout_key: str = TIMEOUT_KEY
    ) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.focus

Focus the window.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.focus_element

Focus the element.

```py
def focus_element(self, key: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.get_center_location

Get center location.

```py
def get_center_location(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.get_element_by_key

Get an element by its key.

```py
def get_element_by_key(self, key: str) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.get_elements_by_type

Get elements by type.

```py
def get_elements_by_type(self, element_type: str) -> list["Element"]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.get_location

Get window location.

```py
def get_location(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.get_screen_size

Get the screen size.

```py
def get_screen_size(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.get_size

Get the window size.

```py
def get_size(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.get_values

Get values from the window.

```py
def get_values(self) -> dict[KeyType, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.hide

Hide the window.

```py
def hide(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.hide_titlebar

Hide the titlebar.

```py
def hide_titlebar(self, flag: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.is_alive

Check if the window is alive.

```py
def is_alive(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.is_running

Check if the window is running. (alias as is_alive)

```py
def is_running(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.keep_on_top

Set the window to keep on top.

```py
def keep_on_top(self, flag: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.maximize

Maximize the window. (`resizable` should be set to True)

```py
def maximize(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.minimize

Minimize the window.

```py
def minimize(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.move

Move the window. (same as set_location)

```py
def move(self, x: int, y: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.move_to_center

Move the window to the center of the screen.

```py
def move_to_center(self, center_pos: Union[tuple[int, int], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.normal

Set normal window.

```py
def normal(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.post_event

Post an event.

```py
def post_event(self, key: KeyType, values: dict[KeyType, Any]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.post_event_after

Post an event after msec.

```py
def post_event_after(
    self, msec: int, key: KeyType, values: dict[KeyType, Any]
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.read

Read events from the window.

```py
def read(
    self, timeout: Union[int, None] = None, timeout_key: str = WINDOW_TIMEOUT
    ) -> tuple[KeyType, dict[KeyType, Any]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.refresh

Refresh window

```py
def refresh(self) -> "Window":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.register_event_hooks

Register event hooks. (append hook events)

**Example**
```py
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
- @see [Window.read](#windowread)

```py
def register_event_hooks(self, hooks: dict[str, list[Callable]]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.send_to_back

Send the window to the back, and make it not keep on top.

```py
def send_to_back(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.set_alpha_channel

Set the alpha channel of the window.

```py
def set_alpha_channel(self, alpha: float) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.set_grab_anywhere

Set grab anywhere

```py
def set_grab_anywhere(self, flag: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.set_location

Set window location.

```py
def set_location(self, xy: tuple[int, int]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.set_size

Set the window size.

```py
def set_size(self, size: tuple[int, int]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.set_timeout

Set a timeout event.

```py
def set_timeout(self, callback: Callable, msec: int, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.set_title

Set the title of the window.

```py
def set_title(self, title: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.show

Show hidden window (hide -> show)

```py
def show(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.start_thread

Start a thread.

### Example
```py
import TkEasyGUI as eg
# long-running process sample
def long_running_process(wait):
    print("sleep start")
    time.sleep(wait)
    return f"done {wait}"
# create a window
with eg.Window("threading", layout=[[eg.Button("Run")]]) as window:
    # event loop
    for event, values in window.event_iter():
        if event == "Run":
            window.start_thread(long_running_process, end_key="-threadend-", wait=3)
        if event == "-threadend-":
            result = values["-threadend-"]
            eg.print("Thread end", result)
```

```py
def start_thread(
    self,
    target: Callable,
    end_key: str = WINDOW_THREAD_END,  # the thread processing is complete, end_key will be released
    *args,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.un_hide

Un hide the window.

```py
def un_hide(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

### Window.update_idle_tasks

Update idle tasks.

```py
def update_idle_tasks(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L92)

# Functions of TkEasyGUI.widgets

- [align_center](#align_center)
- [align_left](#align_left)
- [align_right](#align_right)
- [cast](#cast)
- [generate_element_id](#generate_element_id)
- [generate_element_style_key](#generate_element_style_key)
- [get_current_theme](#get_current_theme)
- [get_font_list](#get_font_list)
- [get_image_tk](#get_image_tk)
- [get_root_window](#get_root_window)
- [get_system_info](#get_system_info)
- [get_tcl_version](#get_tcl_version)
- [get_tk_version](#get_tk_version)
- [get_ttk_style](#get_ttk_style)
- [image_resize](#image_resize)
- [imagedata_to_bytes](#imagedata_to_bytes)
- [imagefile_to_bytes](#imagefile_to_bytes)
- [register_element_key](#register_element_key)
- [rgb](#rgb)
- [time_checker_end](#time_checker_end)
- [time_checker_start](#time_checker_start)
- [valign_bottom](#valign_bottom)
- [valign_middle](#valign_middle)
- [valign_top](#valign_top)

## align_center

Align center : layout helper

```py
def align_center(parts: list[Element]) -> list[Element]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4592)

## align_left

Align left : layout helper

```py
def align_left(parts: list[Element]) -> list[Element]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4606)

## align_right

Align right : layout helper

```py
def align_right(parts: list[Element]) -> list[Element]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4599)

## cast

Cast a value to a type.

    This returns the value unchanged.  To the type checker this
    signals that the return value has the designated type, but at
    runtime we intentionally don't check anything (we want this
    to be as fast as possible).

```py
def cast(typ, val):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/typing.py#L2183)

## generate_element_id

Generate a unique id for a value element.

```py
def generate_element_id() -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L336)

## generate_element_style_key

Get a unique id for an element.

```py
def generate_element_style_key(element_type: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L301)

## get_current_theme

Get current theme

```py
def get_current_theme() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L255)

## get_font_list

Get font list

```py
def get_font_list() -> list[str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4799)

## get_image_tk

Get Image for tk

```py
def get_image_tk(
    source: Union[bytes, Union[str, None]] = None,
    filename: Union[str, None] = None,
    data: Union[bytes, PILImage.Image, None] = None,
    size: Union[tuple[int, int], None] = None,
    resize_type: ImageResizeType = ImageResizeType.FIT_BOTH,
    background_color: Union[str, None] = None,  # color (example) "red" or "#FF0000"
) -> Union[ImageTk.PhotoImage, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4704)

## get_root_window

Get root window.

```py
def get_root_window() -> tk.Tk:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L175)

## get_system_info

Get system info

```py
def get_system_info():
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4806)

## get_tcl_version

Get tcl version

```py
def get_tcl_version() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4792)

## get_tk_version

Get tk version

```py
def get_tk_version() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4785)

## get_ttk_style

Get ttk style

```py
def get_ttk_style() -> ttk.Style:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L208)

## image_resize

Resize image

```py
def image_resize(
    img: PILImage.Image,
    size: Union[tuple[int, int], None],
    resize_type: ImageResizeType = ImageResizeType.FIT_BOTH,
    background_color: Union[str, None] = None,  # color (example) "red" or "#FF0000"
) -> PILImage.Image:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4642)

## imagedata_to_bytes

Convert JPEG to PNG

```py
def imagedata_to_bytes(image_data: PILImage.Image) -> bytes:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4755)

## imagefile_to_bytes

Read image file and convert to bytes

```py
def imagefile_to_bytes(filename: str) -> bytes:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4763)

## register_element_key

Register element key.

```py
def register_element_key(key: KeyType) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L317)

## rgb

Convert RGB to Hex

```py
def rgb(r: int, g: int, b: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4634)

## time_checker_end

Timer end

```py
def time_checker_end(start_time: datetime) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4777)

## time_checker_start

Timer start

```py
def time_checker_start() -> datetime:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4772)

## valign_bottom

Vertical align bottom : layout helper

```py
def valign_bottom(grid: list[list[Element]]) -> list[list[Element]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4627)

## valign_middle

Vertical align middle : layout helper

```py
def valign_middle(grid: list[list[Element]]) -> list[list[Element]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4616)

## valign_top

Vertical align top : layout helper

```py
def valign_top(grid: list[list[Element]]) -> list[list[Element]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4611)

