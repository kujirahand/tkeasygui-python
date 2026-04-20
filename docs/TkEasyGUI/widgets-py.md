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
- [FrameScrollable](#framescrollable)
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
- [Progressbar](#progressbar)
- [Push](#push)
- [Radio](#radio)
- [Slider](#slider)
- [Submit](#submit)
- [Tab](#tab)
- [TabGroup](#tabgroup)
- [Table](#table)
- [Text](#text)
- [Textarea](#textarea)
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
    key: Optional[str] = None,
    disabled: bool = False,
    size: Optional[tuple[int, int]] = None,
    tooltip: Optional[str] = None,  # (TODO) tooltip
    button_color: Optional[Union[str, tuple[str, str]]] = None,
    width: Optional[int] = None,  # set characters width
    # text props
    text_align: Optional[TextAlign] = "center",  # text align
    font: Optional[FontType] = None,  # font
    color: Optional[str] = None,  # text color
    text_color: Optional[str] = None,  # same as color
    background_color: Optional[
    str
    ] = None,  # background color (not supported on macOS)
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Optional[PadType] = None,
    # other
    use_ttk_buttons: bool = False,
    metadata: Optional[dict[str, Any]] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2352)

### Methods of Button

- [bind](#buttonbind)
- [bind_events](#buttonbind_events)
- [create](#buttoncreate)
- [disptach_event](#buttondisptach_event)
- [focus](#buttonfocus)
- [focus_set](#buttonfocus_set)
- [get](#buttonget)
- [get_bind_dict](#buttonget_bind_dict)
- [get_height](#buttonget_height)
- [get_name](#buttonget_name)
- [get_pack_props](#buttonget_pack_props)
- [get_prev_element](#buttonget_prev_element)
- [get_text](#buttonget_text)
- [get_width](#buttonget_width)
- [is_disabled](#buttonis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Button.create

Create a Button widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2409)

### Button.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Button.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Button.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Button.get

Returns the text of the button..

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2442)

### Button.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Button.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Button.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Button.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Button.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Button.get_text

Get the text of the button.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2451)

### Button.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Button.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Button.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Button.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Button.set_button_color

Set the button color.

```py
def set_button_color(
    self, button_color: Union[str, tuple[str, str]], update: bool = True
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2426)

### Button.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Button.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Button.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2446)

### Button.update

Update the widget.

```py
def update(
    self,
    text: Optional[str] = None,
    disabled: Optional[bool] = None,
    button_color: Optional[Union[str, tuple[str, str]]] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2455)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5068)

### Methods of CalendarBrowse

- [bind](#calendarbrowsebind)
- [bind_events](#calendarbrowsebind_events)
- [create](#calendarbrowsecreate)
- [disptach_event](#calendarbrowsedisptach_event)
- [focus](#calendarbrowsefocus)
- [focus_set](#calendarbrowsefocus_set)
- [get](#calendarbrowseget)
- [get_bind_dict](#calendarbrowseget_bind_dict)
- [get_height](#calendarbrowseget_height)
- [get_name](#calendarbrowseget_name)
- [get_pack_props](#calendarbrowseget_pack_props)
- [get_prev_element](#calendarbrowseget_prev_element)
- [get_width](#calendarbrowseget_width)
- [is_disabled](#calendarbrowseis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### CalendarBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4716)

### CalendarBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### CalendarBrowse.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### CalendarBrowse.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### CalendarBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### CalendarBrowse.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### CalendarBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### CalendarBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### CalendarBrowse.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### CalendarBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### CalendarBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### CalendarBrowse.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### CalendarBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### CalendarBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### CalendarBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### CalendarBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### CalendarBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4776)

### CalendarBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[datetime, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5098)

### CalendarBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4781)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5068)

### Methods of CalendarButton

- [bind](#calendarbuttonbind)
- [bind_events](#calendarbuttonbind_events)
- [create](#calendarbuttoncreate)
- [disptach_event](#calendarbuttondisptach_event)
- [focus](#calendarbuttonfocus)
- [focus_set](#calendarbuttonfocus_set)
- [get](#calendarbuttonget)
- [get_bind_dict](#calendarbuttonget_bind_dict)
- [get_height](#calendarbuttonget_height)
- [get_name](#calendarbuttonget_name)
- [get_pack_props](#calendarbuttonget_pack_props)
- [get_prev_element](#calendarbuttonget_prev_element)
- [get_width](#calendarbuttonget_width)
- [is_disabled](#calendarbuttonis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### CalendarButton.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4716)

### CalendarButton.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### CalendarButton.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### CalendarButton.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### CalendarButton.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### CalendarButton.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### CalendarButton.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### CalendarButton.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### CalendarButton.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### CalendarButton.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### CalendarButton.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### CalendarButton.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### CalendarButton.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### CalendarButton.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### CalendarButton.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### CalendarButton.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### CalendarButton.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4776)

### CalendarButton.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[datetime, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5098)

### CalendarButton.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4781)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3680)

### Methods of Canvas

- [bind](#canvasbind)
- [bind_events](#canvasbind_events)
- [clear](#canvasclear)
- [create](#canvascreate)
- [disptach_event](#canvasdisptach_event)
- [focus](#canvasfocus)
- [focus_set](#canvasfocus_set)
- [get](#canvasget)
- [get_bind_dict](#canvasget_bind_dict)
- [get_height](#canvasget_height)
- [get_name](#canvasget_name)
- [get_pack_props](#canvasget_pack_props)
- [get_prev_element](#canvasget_prev_element)
- [get_width](#canvasget_width)
- [is_disabled](#canvasis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Canvas.clear

Clear the canvas.

```py
def clear(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3711)

### Canvas.create

Create Canvas widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3706)

### Canvas.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Canvas.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Canvas.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Canvas.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3715)

### Canvas.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Canvas.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Canvas.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Canvas.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Canvas.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Canvas.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Canvas.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Canvas.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Canvas.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Canvas.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Canvas.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Canvas.update

Update the widget.

```py
def update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3719)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2517)

### Methods of Checkbox

- [bind](#checkboxbind)
- [bind_events](#checkboxbind_events)
- [create](#checkboxcreate)
- [disptach_event](#checkboxdisptach_event)
- [focus](#checkboxfocus)
- [focus_set](#checkboxfocus_set)
- [get](#checkboxget)
- [get_bind_dict](#checkboxget_bind_dict)
- [get_height](#checkboxget_height)
- [get_name](#checkboxget_name)
- [get_pack_props](#checkboxget_pack_props)
- [get_prev_element](#checkboxget_prev_element)
- [get_value](#checkboxget_value)
- [get_width](#checkboxget_width)
- [is_disabled](#checkboxis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Checkbox.create

Create a Checkbox widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2542)

### Checkbox.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Checkbox.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Checkbox.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Checkbox.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2577)

### Checkbox.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Checkbox.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Checkbox.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Checkbox.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Checkbox.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Checkbox.get_value

Get the value of the widget.

```py
def get_value(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2569)

### Checkbox.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Checkbox.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Checkbox.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Checkbox.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Checkbox.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Checkbox.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Checkbox.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2581)

### Checkbox.set_value

Set the value of the widget.

```py
def set_value(self, b: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2573)

### Checkbox.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2586)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2486)

### Methods of CloseButton

- [bind](#closebuttonbind)
- [bind_events](#closebuttonbind_events)
- [close_window](#closebuttonclose_window)
- [create](#closebuttoncreate)
- [disptach_event](#closebuttondisptach_event)
- [focus](#closebuttonfocus)
- [focus_set](#closebuttonfocus_set)
- [get](#closebuttonget)
- [get_bind_dict](#closebuttonget_bind_dict)
- [get_height](#closebuttonget_height)
- [get_name](#closebuttonget_name)
- [get_pack_props](#closebuttonget_pack_props)
- [get_prev_element](#closebuttonget_prev_element)
- [get_text](#closebuttonget_text)
- [get_width](#closebuttonget_width)
- [is_disabled](#closebuttonis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### CloseButton.close_window

Close the window.

```py
def close_window(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2504)

### CloseButton.create

Create a Button widget.

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2496)

### CloseButton.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### CloseButton.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### CloseButton.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### CloseButton.get

Returns the text of the button..

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2442)

### CloseButton.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### CloseButton.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### CloseButton.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### CloseButton.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### CloseButton.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### CloseButton.get_text

Get the text of the button.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2451)

### CloseButton.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### CloseButton.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### CloseButton.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### CloseButton.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### CloseButton.set_button_color

Set the button color.

```py
def set_button_color(
    self, button_color: Union[str, tuple[str, str]], update: bool = True
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2426)

### CloseButton.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### CloseButton.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### CloseButton.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2446)

### CloseButton.update

Update the widget.

```py
def update(
    self,
    text: Optional[str] = None,
    disabled: Optional[bool] = None,
    button_color: Optional[Union[str, tuple[str, str]]] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2455)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4905)

### Methods of ColorBrowse

- [bind](#colorbrowsebind)
- [bind_events](#colorbrowsebind_events)
- [create](#colorbrowsecreate)
- [disptach_event](#colorbrowsedisptach_event)
- [focus](#colorbrowsefocus)
- [focus_set](#colorbrowsefocus_set)
- [get](#colorbrowseget)
- [get_bind_dict](#colorbrowseget_bind_dict)
- [get_height](#colorbrowseget_height)
- [get_name](#colorbrowseget_name)
- [get_pack_props](#colorbrowseget_pack_props)
- [get_prev_element](#colorbrowseget_prev_element)
- [get_width](#colorbrowseget_width)
- [is_disabled](#colorbrowseis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### ColorBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4716)

### ColorBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### ColorBrowse.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### ColorBrowse.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### ColorBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### ColorBrowse.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### ColorBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### ColorBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### ColorBrowse.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### ColorBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### ColorBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### ColorBrowse.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### ColorBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### ColorBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### ColorBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### ColorBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### ColorBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4776)

### ColorBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4925)

### ColorBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4781)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1825)

### Methods of Column

- [bind](#columnbind)
- [bind_events](#columnbind_events)
- [create](#columncreate)
- [disptach_event](#columndisptach_event)
- [focus](#columnfocus)
- [focus_set](#columnfocus_set)
- [get](#columnget)
- [get_bind_dict](#columnget_bind_dict)
- [get_height](#columnget_height)
- [get_name](#columnget_name)
- [get_pack_props](#columnget_pack_props)
- [get_prev_element](#columnget_prev_element)
- [get_width](#columnget_width)
- [is_disabled](#columnis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Column.create

Create a Column element

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1863)

### Column.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Column.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Column.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Column.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1872)

### Column.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Column.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Column.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Column.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Column.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Column.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Column.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Column.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Column.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Column.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Column.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Column.update

Update the widget.

```py
def update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1876)

## Combo

Combo element.

```py
class Combo(
    self,
    values: Optional[list[str]] = None,  # list of values
    default_value: str = "",
    key: Union[str, None] = None,
    enable_events: bool = False,
    readonly: bool = False,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4301)

### Methods of Combo

- [bind](#combobind)
- [bind_events](#combobind_events)
- [create](#combocreate)
- [disptach_event](#combodisptach_event)
- [focus](#combofocus)
- [focus_set](#combofocus_set)
- [get](#comboget)
- [get_bind_dict](#comboget_bind_dict)
- [get_height](#comboget_height)
- [get_name](#comboget_name)
- [get_pack_props](#comboget_pack_props)
- [get_prev_element](#comboget_prev_element)
- [get_width](#comboget_width)
- [is_disabled](#combois_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Combo.create

[Combo.create] create Listbox widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4322)

### Combo.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Combo.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Combo.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Combo.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4349)

### Combo.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Combo.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Combo.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Combo.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Combo.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Combo.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Combo.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Combo.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Combo.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Combo.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Combo.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Combo.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4357)

### Combo.set_value

Set the value of the widget.

```py
def set_value(self, v: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4343)

### Combo.set_values

Set values to list

```py
def set_values(self, values: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4337)

### Combo.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4363)

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
    )   # pylint: disable=too-many-arguments,too-many-positional-arguments
    """Create an element."""
    # define properties
    # check key
    self.has_value: bool = has_value
    self.key: Union[str, int] = ""
    if key is not None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1238)

### Methods of Element

- [bind](#elementbind)
- [bind_events](#elementbind_events)
- [create](#elementcreate)
- [disptach_event](#elementdisptach_event)
- [focus](#elementfocus)
- [focus_set](#elementfocus_set)
- [get](#elementget)
- [get_bind_dict](#elementget_bind_dict)
- [get_height](#elementget_height)
- [get_name](#elementget_name)
- [get_pack_props](#elementget_pack_props)
- [get_prev_element](#elementget_prev_element)
- [get_width](#elementget_width)
- [is_disabled](#elementis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Element.create

Create a widget.

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1507)

### Element.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Element.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Element.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Element.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### Element.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Element.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Element.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Element.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Element.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Element.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Element.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Element.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Element.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Element.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Element.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Element.update

Update widget configuration.

```py
def update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1579)

## FileBrowse

FileBrowse element.

```py
class FileBrowse(
    self,
    button_text: str = "...",
    key: Union[str, int, None] = None,
    title: str = "",
    target_key: Union[str, None] = None,
    file_types: Optional[FileTypeList] = None,
    multiple_files: bool = False,
    initial_folder: Union[str, None] = None,
    save_as: bool = False,
    enable_events: bool = False,  # enable changing events
    # other
    files_delimiter: Optional[str] = FILES_DELIMITER,
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4682)

### Methods of FileBrowse

- [bind](#filebrowsebind)
- [bind_events](#filebrowsebind_events)
- [create](#filebrowsecreate)
- [disptach_event](#filebrowsedisptach_event)
- [focus](#filebrowsefocus)
- [focus_set](#filebrowsefocus_set)
- [get](#filebrowseget)
- [get_bind_dict](#filebrowseget_bind_dict)
- [get_height](#filebrowseget_height)
- [get_name](#filebrowseget_name)
- [get_pack_props](#filebrowseget_pack_props)
- [get_prev_element](#filebrowseget_prev_element)
- [get_width](#filebrowseget_width)
- [is_disabled](#filebrowseis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### FileBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4716)

### FileBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### FileBrowse.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### FileBrowse.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### FileBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### FileBrowse.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### FileBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### FileBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### FileBrowse.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### FileBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### FileBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### FileBrowse.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### FileBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### FileBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### FileBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### FileBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### FileBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4776)

### FileBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[Any, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4744)

### FileBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4781)

## FileSaveAs

FileSaveAs element. (alias of FileSaveAsBrowse)

```py
class FileSaveAs(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    title: str = "",
    file_types: Optional[FileTypeList] = None,
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4825)

### Methods of FileSaveAs

- [bind](#filesaveasbind)
- [bind_events](#filesaveasbind_events)
- [create](#filesaveascreate)
- [disptach_event](#filesaveasdisptach_event)
- [focus](#filesaveasfocus)
- [focus_set](#filesaveasfocus_set)
- [get](#filesaveasget)
- [get_bind_dict](#filesaveasget_bind_dict)
- [get_height](#filesaveasget_height)
- [get_name](#filesaveasget_name)
- [get_pack_props](#filesaveasget_pack_props)
- [get_prev_element](#filesaveasget_prev_element)
- [get_width](#filesaveasget_width)
- [is_disabled](#filesaveasis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### FileSaveAs.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4716)

### FileSaveAs.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### FileSaveAs.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### FileSaveAs.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### FileSaveAs.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### FileSaveAs.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### FileSaveAs.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### FileSaveAs.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### FileSaveAs.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### FileSaveAs.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### FileSaveAs.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### FileSaveAs.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### FileSaveAs.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### FileSaveAs.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### FileSaveAs.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### FileSaveAs.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### FileSaveAs.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4776)

### FileSaveAs.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[Any, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4744)

### FileSaveAs.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4781)

## FileSaveAsBrowse

FileSaveAsBrowse element.

```py
class FileSaveAsBrowse(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    title: str = "",
    file_types: Optional[FileTypeList] = None,
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4825)

### Methods of FileSaveAsBrowse

- [bind](#filesaveasbrowsebind)
- [bind_events](#filesaveasbrowsebind_events)
- [create](#filesaveasbrowsecreate)
- [disptach_event](#filesaveasbrowsedisptach_event)
- [focus](#filesaveasbrowsefocus)
- [focus_set](#filesaveasbrowsefocus_set)
- [get](#filesaveasbrowseget)
- [get_bind_dict](#filesaveasbrowseget_bind_dict)
- [get_height](#filesaveasbrowseget_height)
- [get_name](#filesaveasbrowseget_name)
- [get_pack_props](#filesaveasbrowseget_pack_props)
- [get_prev_element](#filesaveasbrowseget_prev_element)
- [get_width](#filesaveasbrowseget_width)
- [is_disabled](#filesaveasbrowseis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### FileSaveAsBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4716)

### FileSaveAsBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### FileSaveAsBrowse.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### FileSaveAsBrowse.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### FileSaveAsBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### FileSaveAsBrowse.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### FileSaveAsBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### FileSaveAsBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### FileSaveAsBrowse.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### FileSaveAsBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### FileSaveAsBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### FileSaveAsBrowse.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### FileSaveAsBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### FileSaveAsBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### FileSaveAsBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### FileSaveAsBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### FileSaveAsBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4776)

### FileSaveAsBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[Any, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4744)

### FileSaveAsBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4781)

## FilesBrowse

FilesBrowse element.

```py
class FilesBrowse(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    title: str = "",
    file_types: Optional[FileTypeList] = None,
    files_delimiter: Optional[str] = FILES_DELIMITER,
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4791)

### Methods of FilesBrowse

- [bind](#filesbrowsebind)
- [bind_events](#filesbrowsebind_events)
- [create](#filesbrowsecreate)
- [disptach_event](#filesbrowsedisptach_event)
- [focus](#filesbrowsefocus)
- [focus_set](#filesbrowsefocus_set)
- [get](#filesbrowseget)
- [get_bind_dict](#filesbrowseget_bind_dict)
- [get_height](#filesbrowseget_height)
- [get_name](#filesbrowseget_name)
- [get_pack_props](#filesbrowseget_pack_props)
- [get_prev_element](#filesbrowseget_prev_element)
- [get_width](#filesbrowseget_width)
- [is_disabled](#filesbrowseis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### FilesBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4716)

### FilesBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### FilesBrowse.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### FilesBrowse.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### FilesBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### FilesBrowse.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### FilesBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### FilesBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### FilesBrowse.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### FilesBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### FilesBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### FilesBrowse.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### FilesBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### FilesBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### FilesBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### FilesBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### FilesBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4776)

### FilesBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[Any, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4744)

### FilesBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4781)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4858)

### Methods of FolderBrowse

- [bind](#folderbrowsebind)
- [bind_events](#folderbrowsebind_events)
- [create](#folderbrowsecreate)
- [disptach_event](#folderbrowsedisptach_event)
- [focus](#folderbrowsefocus)
- [focus_set](#folderbrowsefocus_set)
- [get](#folderbrowseget)
- [get_bind_dict](#folderbrowseget_bind_dict)
- [get_height](#folderbrowseget_height)
- [get_name](#folderbrowseget_name)
- [get_pack_props](#folderbrowseget_pack_props)
- [get_prev_element](#folderbrowseget_prev_element)
- [get_width](#folderbrowseget_width)
- [is_disabled](#folderbrowseis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### FolderBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4716)

### FolderBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### FolderBrowse.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### FolderBrowse.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### FolderBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### FolderBrowse.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### FolderBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### FolderBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### FolderBrowse.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### FolderBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### FolderBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### FolderBrowse.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### FolderBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### FolderBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### FolderBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### FolderBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### FolderBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4776)

### FolderBrowse.show_dialog

Show file dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4878)

### FolderBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4781)

## Frame

Frame element.

```py
class Frame(
    self,
    title: str,
    layout: LayoutType,
    key: str = "",
    size: Optional[tuple[int, int]] = None,
    relief: ReliefType = "groove",
    # text props
    font: Optional[FontType] = None,  # font
    color: Optional[str] = None,
    text_color: Optional[str] = None,
    background_color: Optional[str] = None,  # background_color
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1659)

### Methods of Frame

- [bind](#framebind)
- [bind_events](#framebind_events)
- [create](#framecreate)
- [disptach_event](#framedisptach_event)
- [focus](#framefocus)
- [focus_set](#framefocus_set)
- [get](#frameget)
- [get_bind_dict](#frameget_bind_dict)
- [get_height](#frameget_height)
- [get_name](#frameget_name)
- [get_pack_props](#frameget_pack_props)
- [get_prev_element](#frameget_prev_element)
- [get_width](#frameget_width)
- [is_disabled](#frameis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Frame.create

Create a Frame widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1706)

### Frame.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Frame.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Frame.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Frame.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1716)

### Frame.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Frame.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Frame.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Frame.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Frame.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Frame.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Frame.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Frame.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Frame.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Frame.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Frame.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Frame.update

Update the widget.

```py
def update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1720)

## FrameScrollable

Scrollable　Frame element.

```py
class FrameScrollable(
    self,
    title: str,
    layout: LayoutType,
    key: str = "",
    size: Optional[tuple[int, int]] = None,
    relief: ReliefType = "groove",
    # text props
    font: Optional[FontType] = None,  # font
    color: Optional[str] = None,
    text_color: Optional[str] = None,
    background_color: Optional[str] = None,  # background_color
    # pack props
    label_outside: bool = False,
    vertical_alignment: TextVAlign = "top",  # vertical alignment
    text_align: Union[TextAlign, None] = "left",  # text align
    # scroll props
    horizontal_scroll: bool = True,  # enable horizontal scrollbar
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1735)

### Methods of FrameScrollable

- [bind](#framescrollablebind)
- [bind_events](#framescrollablebind_events)
- [create](#framescrollablecreate)
- [disptach_event](#framescrollabledisptach_event)
- [focus](#framescrollablefocus)
- [focus_set](#framescrollablefocus_set)
- [get](#framescrollableget)
- [get_bind_dict](#framescrollableget_bind_dict)
- [get_height](#framescrollableget_height)
- [get_name](#framescrollableget_name)
- [get_pack_props](#framescrollableget_pack_props)
- [get_prev_element](#framescrollableget_prev_element)
- [get_width](#framescrollableget_width)
- [is_disabled](#framescrollableis_disabled)
- [post_create](#framescrollablepost_create)
- [prepare_create](#framescrollableprepare_create)
- [set_cursor](#framescrollableset_cursor)
- [set_disabled](#framescrollableset_disabled)
- [update](#framescrollableupdate)

### FrameScrollable.bind

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

### FrameScrollable.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### FrameScrollable.create

Create a Frame widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1783)

### FrameScrollable.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### FrameScrollable.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### FrameScrollable.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### FrameScrollable.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1807)

### FrameScrollable.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### FrameScrollable.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### FrameScrollable.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### FrameScrollable.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### FrameScrollable.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### FrameScrollable.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### FrameScrollable.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### FrameScrollable.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### FrameScrollable.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### FrameScrollable.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### FrameScrollable.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### FrameScrollable.update

Update the widget.

```py
def update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1811)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3737)

### Methods of Graph

- [bind](#graphbind)
- [bind_events](#graphbind_events)
- [clear_all](#graphclear_all)
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
- [focus](#graphfocus)
- [focus_set](#graphfocus_set)
- [get](#graphget)
- [get_bind_dict](#graphget_bind_dict)
- [get_height](#graphget_height)
- [get_name](#graphget_name)
- [get_pack_props](#graphget_pack_props)
- [get_prev_element](#graphget_prev_element)
- [get_width](#graphget_width)
- [is_disabled](#graphis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Graph.clear_all

Delete all

```py
def clear_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3855)

### Graph.create

Create Graph widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3765)

### Graph.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3828)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3805)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3894)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3785)

### Graph.draw_lines

Draw lines.

```py
def draw_lines(self, points: list[PointType], color="black", width=1) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3795)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3817)

### Graph.draw_point

Draw a point.

```py
def draw_point(self, point: PointType, size: int = 2, color: str = "black") -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3799)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3870)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3859)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3880)

### Graph.erase

Delete all

```py
def erase(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3851)

### Graph.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Graph.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Graph.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3771)

### Graph.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Graph.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Graph.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Graph.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Graph.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Graph.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Graph.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Graph.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Graph.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Graph.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Graph.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Graph.update

Update the widget.

```py
def update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3775)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4104)

### Methods of HSeparator

- [bind](#hseparatorbind)
- [bind_events](#hseparatorbind_events)
- [create](#hseparatorcreate)
- [disptach_event](#hseparatordisptach_event)
- [focus](#hseparatorfocus)
- [focus_set](#hseparatorfocus_set)
- [get](#hseparatorget)
- [get_bind_dict](#hseparatorget_bind_dict)
- [get_height](#hseparatorget_height)
- [get_name](#hseparatorget_name)
- [get_pack_props](#hseparatorget_pack_props)
- [get_prev_element](#hseparatorget_prev_element)
- [get_width](#hseparatorget_width)
- [is_disabled](#hseparatoris_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### HSeparator.create

Create HSeparator widget.

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4123)

### HSeparator.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### HSeparator.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### HSeparator.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### HSeparator.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### HSeparator.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### HSeparator.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### HSeparator.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### HSeparator.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### HSeparator.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### HSeparator.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### HSeparator.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### HSeparator.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### HSeparator.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### HSeparator.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### HSeparator.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### HSeparator.update

Update widget configuration.

```py
def update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1579)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3916)

### Methods of Image

- [bind](#imagebind)
- [bind_events](#imagebind_events)
- [create](#imagecreate)
- [disptach_event](#imagedisptach_event)
- [erase](#imageerase)
- [focus](#imagefocus)
- [focus_set](#imagefocus_set)
- [get](#imageget)
- [get_bind_dict](#imageget_bind_dict)
- [get_height](#imageget_height)
- [get_name](#imageget_name)
- [get_pack_props](#imageget_pack_props)
- [get_prev_element](#imageget_prev_element)
- [get_width](#imageget_width)
- [is_disabled](#imageis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Image.create

Create a Image widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3960)

### Image.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Image.erase

Erase image

```py
def erase(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3975)

### Image.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Image.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Image.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3971)

### Image.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Image.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Image.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Image.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Image.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Image.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Image.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Image.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Image.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Image.screenshot

Take a screenshot

```py
def screenshot(self) -> PILImage.Image:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3979)

### Image.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Image.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3985)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4033)

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
    disabled: Optional[bool] = None,  # disabled box
    size: Union[
    tuple[int, int], None
    ] = None,  # set (width, _) character size (only width is supported)
    width: Union[int, None] = None,  # set width character size
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[str, None] = None,  # background color
    # validation
    validation: Union[
    str, Pattern[str], None
    ] = None,  # regex pattern for validation (fullmatch)
    validation_message: Union[
    str, None
    ] = None,  # message shown when validation fails
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2694)

### Methods of Input

- [bind](#inputbind)
- [bind_events](#inputbind_events)
- [copy](#inputcopy)
- [copy_selected_text](#inputcopy_selected_text)
- [create](#inputcreate)
- [cut](#inputcut)
- [delete_selected](#inputdelete_selected)
- [disptach_event](#inputdisptach_event)
- [focus](#inputfocus)
- [focus_set](#inputfocus_set)
- [get](#inputget)
- [get_bind_dict](#inputget_bind_dict)
- [get_cursor_pos](#inputget_cursor_pos)
- [get_height](#inputget_height)
- [get_name](#inputget_name)
- [get_pack_props](#inputget_pack_props)
- [get_prev_element](#inputget_prev_element)
- [get_selected_text](#inputget_selected_text)
- [get_selection_length](#inputget_selection_length)
- [get_selection_pos](#inputget_selection_pos)
- [get_selection_start](#inputget_selection_start)
- [get_text](#inputget_text)
- [get_width](#inputget_width)
- [is_disabled](#inputis_disabled)
- [is_valid](#inputis_valid)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Input.copy

Copy to clipboard

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2949)

### Input.copy_selected_text

Copy selected text

```py
def copy_selected_text(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2897)

### Input.create

Create Input widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2809)

### Input.cut

Cut to clipboard

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2957)

### Input.delete_selected

Delete selected text

```py
def delete_selected(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2964)

### Input.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Input.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Input.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Input.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2869)

### Input.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Input.get_cursor_pos

Get cursor position

```py
def get_cursor_pos(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3000)

### Input.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Input.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Input.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Input.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Input.get_selected_text

Get selected text

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2888)

### Input.get_selection_length

Get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3024)

### Input.get_selection_pos

Get selection positions

```py
def get_selection_pos(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2987)

### Input.get_selection_start

Get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3013)

### Input.get_text

Get text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2884)

### Input.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Input.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Input.is_valid

Verifies whether the validation is correct and returns the result.

```py
def is_valid(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3047)

### Input.paste

Paste from clipboard

```py
def paste(self):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2975)

### Input.post_create

Post create: attach validation binds after Window.bind registrations.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2837)

### Input.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Input.select_all

select_all

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2941)

### Input.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Input.set_cursor_pos

Set cursor position

```py
def set_cursor_pos(self, index: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3007)

### Input.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Input.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2902)

### Input.set_selection_start

Set selection start and length

```py
def set_selection_start(self, sel_start: int, sel_length: int = 0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3036)

### Input.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2873)

### Input.update

Update the widget.

```py
def update(
    self,
    text: Union[str, None] = None,
    readonly: Union[bool, None] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2908)

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
    disabled: Optional[bool] = None,  # disabled box
    size: Union[
    tuple[int, int], None
    ] = None,  # set (width, _) character size (only width is supported)
    width: Union[int, None] = None,  # set width character size
    # text props
    text_align: Union[TextAlign, None] = "left",  # text align
    font: Union[FontType, None] = None,  # font
    color: Union[str, None] = None,  # text color
    text_color: Union[str, None] = None,  # same as color
    background_color: Union[str, None] = None,  # background color
    # validation
    validation: Union[
    str, Pattern[str], None
    ] = None,  # regex pattern for validation (fullmatch)
    validation_message: Union[
    str, None
    ] = None,  # message shown when validation fails
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Union[PadType, None] = None,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2694)

### Methods of InputText

- [bind](#inputtextbind)
- [bind_events](#inputtextbind_events)
- [copy](#inputtextcopy)
- [copy_selected_text](#inputtextcopy_selected_text)
- [create](#inputtextcreate)
- [cut](#inputtextcut)
- [delete_selected](#inputtextdelete_selected)
- [disptach_event](#inputtextdisptach_event)
- [focus](#inputtextfocus)
- [focus_set](#inputtextfocus_set)
- [get](#inputtextget)
- [get_bind_dict](#inputtextget_bind_dict)
- [get_cursor_pos](#inputtextget_cursor_pos)
- [get_height](#inputtextget_height)
- [get_name](#inputtextget_name)
- [get_pack_props](#inputtextget_pack_props)
- [get_prev_element](#inputtextget_prev_element)
- [get_selected_text](#inputtextget_selected_text)
- [get_selection_length](#inputtextget_selection_length)
- [get_selection_pos](#inputtextget_selection_pos)
- [get_selection_start](#inputtextget_selection_start)
- [get_text](#inputtextget_text)
- [get_width](#inputtextget_width)
- [is_disabled](#inputtextis_disabled)
- [is_valid](#inputtextis_valid)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### InputText.copy

Copy to clipboard

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2949)

### InputText.copy_selected_text

Copy selected text

```py
def copy_selected_text(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2897)

### InputText.create

Create Input widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2809)

### InputText.cut

Cut to clipboard

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2957)

### InputText.delete_selected

Delete selected text

```py
def delete_selected(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2964)

### InputText.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### InputText.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### InputText.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### InputText.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2869)

### InputText.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### InputText.get_cursor_pos

Get cursor position

```py
def get_cursor_pos(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3000)

### InputText.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### InputText.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### InputText.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### InputText.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### InputText.get_selected_text

Get selected text

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2888)

### InputText.get_selection_length

Get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3024)

### InputText.get_selection_pos

Get selection positions

```py
def get_selection_pos(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2987)

### InputText.get_selection_start

Get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3013)

### InputText.get_text

Get text

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2884)

### InputText.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### InputText.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### InputText.is_valid

Verifies whether the validation is correct and returns the result.

```py
def is_valid(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3047)

### InputText.paste

Paste from clipboard

```py
def paste(self):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2975)

### InputText.post_create

Post create: attach validation binds after Window.bind registrations.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2837)

### InputText.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### InputText.select_all

select_all

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2941)

### InputText.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### InputText.set_cursor_pos

Set cursor position

```py
def set_cursor_pos(self, index: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3007)

### InputText.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### InputText.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2902)

### InputText.set_selection_start

Set selection start and length

```py
def set_selection_start(self, sel_start: int, sel_length: int = 0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3036)

### InputText.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2873)

### InputText.update

Update the widget.

```py
def update(
    self,
    text: Union[str, None] = None,
    readonly: Union[bool, None] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2908)

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
    # validation
    validation: Union[
    str, Pattern[str], None
    ] = None,  # regex pattern for validation (fullmatch)
    validation_message: Union[
    str, None
    ] = None,  # message shown when validation fails
    # other
    metadata: Union[dict[str, Any], None] = None,  # user metadata
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2069)

### Methods of Label

- [bind](#labelbind)
- [bind_events](#labelbind_events)
- [create](#labelcreate)
- [disptach_event](#labeldisptach_event)
- [focus](#labelfocus)
- [focus_set](#labelfocus_set)
- [get](#labelget)
- [get_bind_dict](#labelget_bind_dict)
- [get_height](#labelget_height)
- [get_name](#labelget_name)
- [get_pack_props](#labelget_pack_props)
- [get_prev_element](#labelget_prev_element)
- [get_text](#labelget_text)
- [get_width](#labelget_width)
- [is_disabled](#labelis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Label.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2114)

### Label.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Label.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Label.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Label.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2134)

### Label.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Label.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Label.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Label.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Label.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Label.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2138)

### Label.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Label.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Label.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Label.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Label.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Label.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Label.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2144)

### Label.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2149)

## ListBrowse

ListBrowse element.

```py
class ListBrowse(
    self,
    values: Optional[list[str]] = None,  # list of values
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4952)

### Methods of ListBrowse

- [bind](#listbrowsebind)
- [bind_events](#listbrowsebind_events)
- [create](#listbrowsecreate)
- [disptach_event](#listbrowsedisptach_event)
- [focus](#listbrowsefocus)
- [focus_set](#listbrowsefocus_set)
- [get](#listbrowseget)
- [get_bind_dict](#listbrowseget_bind_dict)
- [get_height](#listbrowseget_height)
- [get_name](#listbrowseget_name)
- [get_pack_props](#listbrowseget_pack_props)
- [get_prev_element](#listbrowseget_prev_element)
- [get_width](#listbrowseget_width)
- [is_disabled](#listbrowseis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### ListBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4716)

### ListBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### ListBrowse.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### ListBrowse.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### ListBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### ListBrowse.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### ListBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### ListBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### ListBrowse.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### ListBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### ListBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### ListBrowse.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### ListBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### ListBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### ListBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### ListBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### ListBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4776)

### ListBrowse.show_dialog

Show Listbox dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4978)

### ListBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4781)

## Listbox

Listbox element.

```py
class Listbox(
    self,
    values: Optional[list[str]] = None,  # list of values
    default_values: Union[list[str], None] = None,  # selected values
    default_value: Union[str, None] = None,  # a default value
    default_index: Optional[
    int
    ] = None,  # a default index (deprecated, use default_value)
    key: Union[str, None] = None,
    enable_events: bool = False,
    select_mode: Optional[
    ListboxSelectMode
    ] = None,  # default is LISTBOX_SELECT_MODE_BROWSE
    # other
    metadata: Union[dict[str, Any], None] = None,
    items: Union[list[str], None] = None,  # same as values (alias values)
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4132)

### Methods of Listbox

- [bind](#listboxbind)
- [bind_events](#listboxbind_events)
- [create](#listboxcreate)
- [disptach_event](#listboxdisptach_event)
- [focus](#listboxfocus)
- [focus_set](#listboxfocus_set)
- [get](#listboxget)
- [get_bind_dict](#listboxget_bind_dict)
- [get_cursor_index](#listboxget_cursor_index)
- [get_height](#listboxget_height)
- [get_name](#listboxget_name)
- [get_pack_props](#listboxget_pack_props)
- [get_prev_element](#listboxget_prev_element)
- [get_selected_indices](#listboxget_selected_indices)
- [get_selected_items](#listboxget_selected_items)
- [get_width](#listboxget_width)
- [is_disabled](#listboxis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Listbox.create

[Listbox.create] create Listbox widget

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4174)

### Listbox.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Listbox.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Listbox.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Listbox.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4256)

### Listbox.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Listbox.get_cursor_index

Get cursor index (return -1 if not selected)

```py
def get_cursor_index(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4235)

### Listbox.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Listbox.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Listbox.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Listbox.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Listbox.get_selected_indices

Get selected indices

```py
def get_selected_indices(self) -> list[int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4273)

### Listbox.get_selected_items

Get selected items

```py
def get_selected_items(self) -> list[str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4260)

### Listbox.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Listbox.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Listbox.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Listbox.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4198)

### Listbox.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Listbox.set_cursor_index

Set cursor index

```py
def set_cursor_index(self, index: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4245)

### Listbox.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Listbox.set_values

Set values to list

```py
def set_values(self, values: list[str]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4225)

### Listbox.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4286)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2236)

### Methods of Menu

- [bind](#menubind)
- [bind_events](#menubind_events)
- [create](#menucreate)
- [disptach_event](#menudisptach_event)
- [focus](#menufocus)
- [focus_set](#menufocus_set)
- [get](#menuget)
- [get_bind_dict](#menuget_bind_dict)
- [get_height](#menuget_height)
- [get_name](#menuget_name)
- [get_pack_props](#menuget_pack_props)
- [get_prev_element](#menuget_prev_element)
- [get_text](#menuget_text)
- [get_width](#menuget_width)
- [is_disabled](#menuis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Menu.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2250)

### Menu.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Menu.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Menu.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Menu.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2304)

### Menu.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Menu.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Menu.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Menu.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Menu.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Menu.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2308)

### Menu.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Menu.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Menu.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Menu.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Menu.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Menu.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Menu.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2314)

### Menu.update

Update the widget.

```py
def update(
    self,
    menu_definition: Optional[list[list[Union[str, list[Any]]]]] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2319)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3067)

### Methods of Multiline

- [bind](#multilinebind)
- [bind_events](#multilinebind_events)
- [copy](#multilinecopy)
- [create](#multilinecreate)
- [cut](#multilinecut)
- [disptach_event](#multilinedisptach_event)
- [focus](#multilinefocus)
- [focus_set](#multilinefocus_set)
- [get](#multilineget)
- [get_bind_dict](#multilineget_bind_dict)
- [get_cursor_pos](#multilineget_cursor_pos)
- [get_height](#multilineget_height)
- [get_name](#multilineget_name)
- [get_pack_props](#multilineget_pack_props)
- [get_prev_element](#multilineget_prev_element)
- [get_selected_text](#multilineget_selected_text)
- [get_selection_length](#multilineget_selection_length)
- [get_selection_pos](#multilineget_selection_pos)
- [get_selection_start](#multilineget_selection_start)
- [get_text](#multilineget_text)
- [get_width](#multilineget_width)
- [index_to_pos](#multilineindex_to_pos)
- [is_disabled](#multilineis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Multiline.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3201)

### Multiline.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3139)

### Multiline.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3218)

### Multiline.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Multiline.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Multiline.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Multiline.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3178)

### Multiline.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Multiline.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3327)

### Multiline.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Multiline.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Multiline.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Multiline.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Multiline.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3191)

### Multiline.get_selection_length

Get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3366)

### Multiline.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3272)

### Multiline.get_selection_start

Get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3343)

### Multiline.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3184)

### Multiline.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Multiline.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3309)

### Multiline.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Multiline.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3209)

### Multiline.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3294)

### Multiline.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Multiline.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3385)

### Multiline.select_all

Select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3376)

### Multiline.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Multiline.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3337)

### Multiline.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Multiline.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3246)

### Multiline.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3283)

### Multiline.set_selection_start

Set selection start

```py
def set_selection_start(self, index: int, sel_length: int = 0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3357)

### Multiline.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3252)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3228)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5012)

### Methods of MultilineBrowse

- [bind](#multilinebrowsebind)
- [bind_events](#multilinebrowsebind_events)
- [create](#multilinebrowsecreate)
- [disptach_event](#multilinebrowsedisptach_event)
- [focus](#multilinebrowsefocus)
- [focus_set](#multilinebrowsefocus_set)
- [get](#multilinebrowseget)
- [get_bind_dict](#multilinebrowseget_bind_dict)
- [get_height](#multilinebrowseget_height)
- [get_name](#multilinebrowseget_name)
- [get_pack_props](#multilinebrowseget_pack_props)
- [get_prev_element](#multilinebrowseget_prev_element)
- [get_width](#multilinebrowseget_width)
- [is_disabled](#multilinebrowseis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### MultilineBrowse.create

Create a FileBrowse widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4716)

### MultilineBrowse.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### MultilineBrowse.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### MultilineBrowse.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### MultilineBrowse.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### MultilineBrowse.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### MultilineBrowse.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### MultilineBrowse.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### MultilineBrowse.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### MultilineBrowse.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### MultilineBrowse.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### MultilineBrowse.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### MultilineBrowse.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### MultilineBrowse.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### MultilineBrowse.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### MultilineBrowse.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### MultilineBrowse.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4776)

### MultilineBrowse.show_dialog

Show Listbox dialog

```py
def show_dialog(self, *args) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5034)

### MultilineBrowse.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4781)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3067)

### Methods of Output

- [bind](#outputbind)
- [bind_events](#outputbind_events)
- [copy](#outputcopy)
- [create](#outputcreate)
- [cut](#outputcut)
- [disptach_event](#outputdisptach_event)
- [focus](#outputfocus)
- [focus_set](#outputfocus_set)
- [get](#outputget)
- [get_bind_dict](#outputget_bind_dict)
- [get_cursor_pos](#outputget_cursor_pos)
- [get_height](#outputget_height)
- [get_name](#outputget_name)
- [get_pack_props](#outputget_pack_props)
- [get_prev_element](#outputget_prev_element)
- [get_selected_text](#outputget_selected_text)
- [get_selection_length](#outputget_selection_length)
- [get_selection_pos](#outputget_selection_pos)
- [get_selection_start](#outputget_selection_start)
- [get_text](#outputget_text)
- [get_width](#outputget_width)
- [index_to_pos](#outputindex_to_pos)
- [is_disabled](#outputis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Output.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3201)

### Output.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3139)

### Output.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3218)

### Output.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Output.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Output.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Output.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3178)

### Output.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Output.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3327)

### Output.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Output.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Output.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Output.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Output.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3191)

### Output.get_selection_length

Get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3366)

### Output.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3272)

### Output.get_selection_start

Get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3343)

### Output.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3184)

### Output.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Output.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3309)

### Output.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Output.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3209)

### Output.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3294)

### Output.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Output.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3385)

### Output.select_all

Select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3376)

### Output.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Output.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3337)

### Output.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Output.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3246)

### Output.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3283)

### Output.set_selection_start

Set selection start

```py
def set_selection_start(self, index: int, sel_length: int = 0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3357)

### Output.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3252)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3228)

## Progressbar

Progressbar element.

```py
class Progressbar(
    self,
    value_range: tuple[int, int] = (1, 10),  # value range (from, to)
    default_value: Optional[int] = None,  # default value
    orientation: OrientationType = "horizontal",  # orientation (h|v|horizontal|vertical)
    thickness: Optional[int] = None,  # thickness of the bar
    length: Optional[int] = None,  # length of the bar (unit: pixel)
    key: Optional[str] = None,
    mode: ProgressbarMode = "determinate",  # mode of the progressbar (determinate|indeterminate)
    metadata: Optional[dict[str, Any]] = None,
    # other
    default: Optional[int] = None,  # same as default_value
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3563)

### Methods of Progressbar

- [bind](#progressbarbind)
- [bind_events](#progressbarbind_events)
- [create](#progressbarcreate)
- [disptach_event](#progressbardisptach_event)
- [focus](#progressbarfocus)
- [focus_set](#progressbarfocus_set)
- [get](#progressbarget)
- [get_bind_dict](#progressbarget_bind_dict)
- [get_height](#progressbarget_height)
- [get_name](#progressbarget_name)
- [get_pack_props](#progressbarget_pack_props)
- [get_prev_element](#progressbarget_prev_element)
- [get_range](#progressbarget_range)
- [get_width](#progressbarget_width)
- [is_disabled](#progressbaris_disabled)
- [post_create](#progressbarpost_create)
- [prepare_create](#progressbarprepare_create)
- [set](#progressbarset)
- [set_cursor](#progressbarset_cursor)
- [set_disabled](#progressbarset_disabled)
- [set_range](#progressbarset_range)
- [start](#progressbarstart)
- [update](#progressbarupdate)

### Progressbar.bind

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

### Progressbar.bind_events

Bind user events.

@see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

```py
def bind_events(
    self, events: dict[str, str], event_mode: EventMode = "user"
    ) -> "Element":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Progressbar.create

Create the widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3612)

### Progressbar.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Progressbar.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Progressbar.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Progressbar.get

Return bar value.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3633)

### Progressbar.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Progressbar.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Progressbar.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Progressbar.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Progressbar.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Progressbar.get_range

Get the range of the bar.

```py
def get_range(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3645)

### Progressbar.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Progressbar.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Progressbar.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Progressbar.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Progressbar.set

Set value of bar

```py
def set(self, value: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3637)

### Progressbar.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Progressbar.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Progressbar.set_range

Set the range of the bar.

```py
def set_range(self, from_: int, to: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3641)

### Progressbar.start

Start the indeterminate progressbar.

```py
def start(self, interval: int = 100) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3663)

### Progressbar.update

Update the widget.

```py
def update(
    self,
    value: Optional[int] = None,
    value_range: Optional[tuple[int, int]] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3649)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2178)

### Methods of Push

- [bind](#pushbind)
- [bind_events](#pushbind_events)
- [create](#pushcreate)
- [disptach_event](#pushdisptach_event)
- [focus](#pushfocus)
- [focus_set](#pushfocus_set)
- [get](#pushget)
- [get_bind_dict](#pushget_bind_dict)
- [get_height](#pushget_height)
- [get_name](#pushget_name)
- [get_pack_props](#pushget_pack_props)
- [get_prev_element](#pushget_prev_element)
- [get_text](#pushget_text)
- [get_width](#pushget_width)
- [is_disabled](#pushis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Push.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2114)

### Push.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Push.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Push.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Push.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2134)

### Push.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Push.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Push.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Push.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Push.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Push.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2138)

### Push.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Push.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Push.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Push.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Push.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Push.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Push.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2144)

### Push.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2149)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2602)

### Methods of Radio

- [bind](#radiobind)
- [bind_events](#radiobind_events)
- [create](#radiocreate)
- [disptach_event](#radiodisptach_event)
- [focus](#radiofocus)
- [focus_set](#radiofocus_set)
- [get](#radioget)
- [get_bind_dict](#radioget_bind_dict)
- [get_height](#radioget_height)
- [get_name](#radioget_name)
- [get_pack_props](#radioget_pack_props)
- [get_prev_element](#radioget_prev_element)
- [get_value](#radioget_value)
- [get_width](#radioget_width)
- [is_disabled](#radiois_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Radio.create

Create a Radio widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2627)

### Radio.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Radio.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Radio.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Radio.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2675)

### Radio.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Radio.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Radio.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Radio.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Radio.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Radio.get_value

Returns the id of an element within a group.

```py
def get_value(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2671)

### Radio.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Radio.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Radio.is_selected

Check if the radio button is selected.

```py
def is_selected(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2665)

### Radio.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Radio.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Radio.select

Select the radio button.

```py
def select(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2659)

### Radio.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Radio.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Radio.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2679)

### Radio.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2684)

## Slider

Slider element.

```py
class Slider(
    self,
    value_range: Optional[
    tuple[float, float]
    ] = None,  # value range (from, to) (deprecated, use `range`)
    default_value: Optional[float] = None,  # default value
    resolution: float = 1,  # value resolution
    orientation: OrientationType = "horizontal",  # orientation (h|v|horizontal|vertical)
    tick_interval: Optional[float] = None,  # tick marks interval on the scale
    enable_events: bool = False,  # enable changing events
    enable_changed_events: bool = False,  # enable changed event
    disable_number_display: bool = False,  # hide number display
    size: Optional[
    tuple[int, int]
    ] = None,  # size (unit: character) / horizontal: (bar_length, thumb_size), vertical: (thumb_size, bar_length)
    key: Optional[str] = None,
    # other
    # pylint: disable=redefined-builtin
    range: Optional[tuple[float, float]] = None,  # value range (from, to)
    default: Optional[float] = None,  # same as default_value
    metadata: Optional[dict[str, Any]] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3422)

### Methods of Slider

- [bind](#sliderbind)
- [bind_events](#sliderbind_events)
- [create](#slidercreate)
- [disptach_event](#sliderdisptach_event)
- [focus](#sliderfocus)
- [focus_set](#sliderfocus_set)
- [get](#sliderget)
- [get_bind_dict](#sliderget_bind_dict)
- [get_height](#sliderget_height)
- [get_name](#sliderget_name)
- [get_pack_props](#sliderget_pack_props)
- [get_prev_element](#sliderget_prev_element)
- [get_range](#sliderget_range)
- [get_width](#sliderget_width)
- [is_disabled](#slideris_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Slider.create

Create the widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3489)

### Slider.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Slider.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Slider.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Slider.get

Return slider value.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3525)

### Slider.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Slider.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Slider.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Slider.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Slider.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Slider.get_range

Get the range of the slider.

```py
def get_range(self) -> tuple[float, float]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3537)

### Slider.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Slider.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Slider.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Slider.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Slider.set

Set value of Slider

```py
def set(self, value: float) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3529)

### Slider.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Slider.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Slider.set_range

Set the range of the slider.

```py
def set_range(self, from_: float, to: float) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3533)

### Slider.update

Update the widget.

```py
def update(
    self,
    value: Union[float, None] = None,
    # pylint: disable=redefined-builtin
    range: Union[tuple[float, float], None] = None,
    disable_number_display: Union[bool, None] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3541)

## Submit

Subtmi element. (Alias of Button) : todo: add submit event

```py
class Submit(
    self,
    button_text: str = "Button",
    key: Optional[str] = None,
    disabled: bool = False,
    size: Optional[tuple[int, int]] = None,
    tooltip: Optional[str] = None,  # (TODO) tooltip
    button_color: Optional[Union[str, tuple[str, str]]] = None,
    width: Optional[int] = None,  # set characters width
    # text props
    text_align: Optional[TextAlign] = "center",  # text align
    font: Optional[FontType] = None,  # font
    color: Optional[str] = None,  # text color
    text_color: Optional[str] = None,  # same as color
    background_color: Optional[
    str
    ] = None,  # background color (not supported on macOS)
    # pack props
    expand_x: bool = False,
    expand_y: bool = False,
    pad: Optional[PadType] = None,
    # other
    use_ttk_buttons: bool = False,
    metadata: Optional[dict[str, Any]] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2352)

### Methods of Submit

- [bind](#submitbind)
- [bind_events](#submitbind_events)
- [create](#submitcreate)
- [disptach_event](#submitdisptach_event)
- [focus](#submitfocus)
- [focus_set](#submitfocus_set)
- [get](#submitget)
- [get_bind_dict](#submitget_bind_dict)
- [get_height](#submitget_height)
- [get_name](#submitget_name)
- [get_pack_props](#submitget_pack_props)
- [get_prev_element](#submitget_prev_element)
- [get_text](#submitget_text)
- [get_width](#submitget_width)
- [is_disabled](#submitis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Submit.create

Create a Button widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2409)

### Submit.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Submit.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Submit.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Submit.get

Returns the text of the button..

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2442)

### Submit.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Submit.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Submit.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Submit.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Submit.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Submit.get_text

Get the text of the button.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2451)

### Submit.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Submit.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Submit.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Submit.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Submit.set_button_color

Set the button color.

```py
def set_button_color(
    self, button_color: Union[str, tuple[str, str]], update: bool = True
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2426)

### Submit.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Submit.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Submit.set_text

Set the text of the button.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2446)

### Submit.update

Update the widget.

```py
def update(
    self,
    text: Optional[str] = None,
    disabled: Optional[bool] = None,
    button_color: Optional[Union[str, tuple[str, str]]] = None,
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2455)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1911)

### Methods of Tab

- [bind](#tabbind)
- [bind_events](#tabbind_events)
- [create](#tabcreate)
- [disptach_event](#tabdisptach_event)
- [focus](#tabfocus)
- [focus_set](#tabfocus_set)
- [get](#tabget)
- [get_bind_dict](#tabget_bind_dict)
- [get_height](#tabget_height)
- [get_name](#tabget_name)
- [get_pack_props](#tabget_pack_props)
- [get_prev_element](#tabget_prev_element)
- [get_width](#tabget_width)
- [is_disabled](#tabis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Tab.create

Create a Tab element.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1951)

### Tab.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Tab.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Tab.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Tab.get

Return Widget title

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1956)

### Tab.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Tab.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Tab.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Tab.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Tab.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Tab.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Tab.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Tab.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Tab.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Tab.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Tab.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Tab.update

Update the widget.

```py
def update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1960)

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
    size: Optional[tuple[int, int]] = None,
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1995)

### Methods of TabGroup

- [bind](#tabgroupbind)
- [bind_events](#tabgroupbind_events)
- [create](#tabgroupcreate)
- [disptach_event](#tabgroupdisptach_event)
- [focus](#tabgroupfocus)
- [focus_set](#tabgroupfocus_set)
- [get](#tabgroupget)
- [get_bind_dict](#tabgroupget_bind_dict)
- [get_height](#tabgroupget_height)
- [get_name](#tabgroupget_name)
- [get_pack_props](#tabgroupget_pack_props)
- [get_prev_element](#tabgroupget_prev_element)
- [get_width](#tabgroupget_width)
- [is_disabled](#tabgroupis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### TabGroup.create

Create a TabGroup element.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2038)

### TabGroup.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### TabGroup.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### TabGroup.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### TabGroup.get

Return Widget

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2050)

### TabGroup.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### TabGroup.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### TabGroup.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### TabGroup.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### TabGroup.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### TabGroup.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### TabGroup.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### TabGroup.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2044)

### TabGroup.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### TabGroup.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### TabGroup.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### TabGroup.update

Update the widget.

```py
def update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2054)

## Table

Table element.

```py
class Table(
    self,
    values: Optional[
    list[list[str]]
    ] = None,  # Specify the table values as 2D list.
    headings: Optional[list[str]] = None,  # Specify the table header as a list.
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4381)

### Methods of Table

- [bind](#tablebind)
- [bind_events](#tablebind_events)
- [create](#tablecreate)
- [disptach_event](#tabledisptach_event)
- [focus](#tablefocus)
- [focus_set](#tablefocus_set)
- [get](#tableget)
- [get_bind_dict](#tableget_bind_dict)
- [get_cursor_index](#tableget_cursor_index)
- [get_height](#tableget_height)
- [get_name](#tableget_name)
- [get_pack_props](#tableget_pack_props)
- [get_prev_element](#tableget_prev_element)
- [get_width](#tableget_width)
- [is_disabled](#tableis_disabled)
- [load_from_file](#tableload_from_file)
- [post_create](#tablepost_create)
- [prepare_create](#tableprepare_create)
- [set_cursor](#tableset_cursor)
- [set_cursor_index](#tableset_cursor_index)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Table.create

Create a Table widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4454)

### Table.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Table.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Table.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Table.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4574)

### Table.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Table.get_cursor_index

Get cursor index (return -1 if not selected)

```py
def get_cursor_index(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4595)

### Table.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Table.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Table.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Table.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Table.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Table.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4649)

### Table.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Table.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Table.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Table.set_cursor_index

Set cursor index

```py
def set_cursor_index(self, index: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4611)

### Table.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Table.set_values

Set values to the table.

```py
def set_values(
    self, values: list[list[str]], headings: Union[list[str], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4550)

### Table.update

Update the widget.

```py
def update(self, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4621)

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
    # validation
    validation: Union[
    str, Pattern[str], None
    ] = None,  # regex pattern for validation (fullmatch)
    validation_message: Union[
    str, None
    ] = None,  # message shown when validation fails
    # other
    metadata: Union[dict[str, Any], None] = None,  # user metadata
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2069)

### Methods of Text

- [bind](#textbind)
- [bind_events](#textbind_events)
- [create](#textcreate)
- [disptach_event](#textdisptach_event)
- [focus](#textfocus)
- [focus_set](#textfocus_set)
- [get](#textget)
- [get_bind_dict](#textget_bind_dict)
- [get_height](#textget_height)
- [get_name](#textget_name)
- [get_pack_props](#textget_pack_props)
- [get_prev_element](#textget_prev_element)
- [get_text](#textget_text)
- [get_width](#textget_width)
- [is_disabled](#textis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Text.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2114)

### Text.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Text.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Text.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Text.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2134)

### Text.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Text.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Text.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Text.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Text.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Text.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2138)

### Text.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Text.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Text.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Text.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### Text.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Text.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Text.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2144)

### Text.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2149)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3067)

### Methods of Textarea

- [bind](#textareabind)
- [bind_events](#textareabind_events)
- [copy](#textareacopy)
- [create](#textareacreate)
- [cut](#textareacut)
- [disptach_event](#textareadisptach_event)
- [focus](#textareafocus)
- [focus_set](#textareafocus_set)
- [get](#textareaget)
- [get_bind_dict](#textareaget_bind_dict)
- [get_cursor_pos](#textareaget_cursor_pos)
- [get_height](#textareaget_height)
- [get_name](#textareaget_name)
- [get_pack_props](#textareaget_pack_props)
- [get_prev_element](#textareaget_prev_element)
- [get_selected_text](#textareaget_selected_text)
- [get_selection_length](#textareaget_selection_length)
- [get_selection_pos](#textareaget_selection_pos)
- [get_selection_start](#textareaget_selection_start)
- [get_text](#textareaget_text)
- [get_width](#textareaget_width)
- [index_to_pos](#textareaindex_to_pos)
- [is_disabled](#textareais_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### Textarea.copy

Copy the selected text.

```py
def copy(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3201)

### Textarea.create

Create a Multiline widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3139)

### Textarea.cut

Cut the selected text.

```py
def cut(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3218)

### Textarea.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### Textarea.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### Textarea.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### Textarea.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3178)

### Textarea.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### Textarea.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

```py
def get_cursor_pos(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3327)

### Textarea.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### Textarea.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### Textarea.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### Textarea.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### Textarea.get_selected_text

Get the selected text.

```py
def get_selected_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3191)

### Textarea.get_selection_length

Get selection length

```py
def get_selection_length(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3366)

### Textarea.get_selection_pos

Get selection position, returns (start_pos, end_pos).

```py
def get_selection_pos(self) -> tuple[str, str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3272)

### Textarea.get_selection_start

Get selection start

```py
def get_selection_start(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3343)

### Textarea.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3184)

### Textarea.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### Textarea.index_to_pos

Convert index to postion.

```py
def index_to_pos(self, index: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3309)

### Textarea.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### Textarea.paste

Paste the text.

```py
def paste(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3209)

### Textarea.pos_to_index

Convert position to index.

```py
def pos_to_index(self, pos: str) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3294)

### Textarea.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### Textarea.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3385)

### Textarea.select_all

Select all text

```py
def select_all(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3376)

### Textarea.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### Textarea.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

```py
def set_cursor_pos(self, pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3337)

### Textarea.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### Textarea.set_readonly

Set readonly

```py
def set_readonly(self, readonly: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3246)

### Textarea.set_selection_pos

Set selection position.

```py
def set_selection_pos(self, start_pos: str, end_pos: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3283)

### Textarea.set_selection_start

Set selection start

```py
def set_selection_start(self, index: int, sel_length: int = 0) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3357)

### Textarea.set_text

Set text

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3252)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3228)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2208)

### Methods of VPush

- [bind](#vpushbind)
- [bind_events](#vpushbind_events)
- [create](#vpushcreate)
- [disptach_event](#vpushdisptach_event)
- [focus](#vpushfocus)
- [focus_set](#vpushfocus_set)
- [get](#vpushget)
- [get_bind_dict](#vpushget_bind_dict)
- [get_height](#vpushget_height)
- [get_name](#vpushget_name)
- [get_pack_props](#vpushget_pack_props)
- [get_prev_element](#vpushget_prev_element)
- [get_text](#vpushget_text)
- [get_width](#vpushget_width)
- [is_disabled](#vpushis_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### VPush.create

Create a Text widget.

```py
def create(self, win: Window, parent: tk.Widget) -> tk.Widget:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2114)

### VPush.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### VPush.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### VPush.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### VPush.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2134)

### VPush.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### VPush.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### VPush.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### VPush.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### VPush.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### VPush.get_text

Get the text of the widget.

```py
def get_text(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2138)

### VPush.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### VPush.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### VPush.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### VPush.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### VPush.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### VPush.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### VPush.set_text

Set the text of the widget.

```py
def set_text(self, text: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2144)

### VPush.update

Update the widget.

```py
def update(self, text: Union[str, None] = None, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2149)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4076)

### Methods of VSeparator

- [bind](#vseparatorbind)
- [bind_events](#vseparatorbind_events)
- [create](#vseparatorcreate)
- [disptach_event](#vseparatordisptach_event)
- [focus](#vseparatorfocus)
- [focus_set](#vseparatorfocus_set)
- [get](#vseparatorget)
- [get_bind_dict](#vseparatorget_bind_dict)
- [get_height](#vseparatorget_height)
- [get_name](#vseparatorget_name)
- [get_pack_props](#vseparatorget_pack_props)
- [get_prev_element](#vseparatorget_prev_element)
- [get_width](#vseparatorget_width)
- [is_disabled](#vseparatoris_disabled)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1325)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1492)

### VSeparator.create

Create VSeparator widget.

```py
def create(self, win: Window, parent: tk.Widget) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L4095)

### VSeparator.disptach_event

Dispatch event

```py
def disptach_event(
    self, values: Union[dict[Union[str, int], Any], None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1344)

### VSeparator.focus

Set focus to the element.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1313)

### VSeparator.focus_set

Set focus to the element.

```py
def focus_set(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1321)

### VSeparator.get

Get the value of the widget.

```py
def get(self) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1575)

### VSeparator.get_bind_dict

Get bind dict.

```py
def get_bind_dict(self) -> dict[str, tuple[str, bool, EventMode]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1289)

### VSeparator.get_height

Get height of element.

```py
def get_height(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1307)

### VSeparator.get_name

Get key of element.

```py
def get_name(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1295)

### VSeparator.get_pack_props

Get the fill property in `pack` method.

```py
def get_pack_props(
    self,
    align: str = "left",
    valign: str = "top",  # pylint:disable=unused-argument
    ) -> dict[str, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1403)

### VSeparator.get_prev_element

Get the previous widget.

```py
def get_prev_element(
    self, target_key: Union[str, None] = None
    ) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1601)

### VSeparator.get_width

Get width of element.

```py
def get_width(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1301)

### VSeparator.is_disabled

Check if the widget is disabled.

```py
def is_disabled(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1618)

### VSeparator.post_create

Post create widget.

```py
def post_create(self, win: Window, parent: tk.Widget) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1572)

### VSeparator.prepare_create

Prepare to create a widget.

```py
def prepare_create(self, win: Window) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1530)

### VSeparator.set_cursor

Set the cursor.

```py
def set_cursor(self, cursor: CursorType) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1582)

### VSeparator.set_disabled

Set disabled widgets state

```py
def set_disabled(self, disabled: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1486)

### VSeparator.update

Update widget configuration.

```py
def update(self, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1579)

## Window

Main window object in TkEasyGUI

```py
class Window(
    self,
    title: str,
    layout: LayoutType,  # set elements layout
    size: Optional[tuple[int, int]] = None,  # window size
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
    location: Optional[tuple[int, int]] = None,  # window location
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L111)

### Methods of Window

- [bind](#windowbind)
- [cancel_close](#windowcancel_close)
- [close](#windowclose)
- [dispatch_event](#windowdispatch_event)
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
- [screenshot](#windowscreenshot)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1075)

### Window.cancel_close

Cancel the close event.

```py
def cancel_close(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1010)

### Window.close

Close the window.

```py
def close(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L943)

### Window.dispatch_event

Dispatch an event to the window.

**Example**
```py
window.dispatch_event("hoge", {"name": "World"})
```

```py
def dispatch_event(
    self,
    key: Union[str, int],
    values: Union[dict[Union[str, int], Any], None] = None,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L880)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L768)

### Window.focus

Focus the window.

```py
def focus(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L336)

### Window.focus_element

Focus the element.

```py
def focus_element(self, key: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L340)

### Window.get_center_location

Get center location.

```py
def get_center_location(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L392)

### Window.get_element_by_key

Get an element by its key.

```py
def get_element_by_key(self, key: str) -> Union["Element", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L639)

### Window.get_elements_by_type

Get elements by type.

```py
def get_elements_by_type(self, element_type: str) -> list["Element"]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L643)

### Window.get_location

Get window location.

```py
def get_location(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L387)

### Window.get_screen_size

Get the screen size.

```py
def get_screen_size(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L599)

### Window.get_size

Get the window size.

```py
def get_size(self) -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L634)

### Window.get_values

Get values from the window.

```py
def get_values(self) -> dict[KeyType, Any]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L847)

### Window.hide

Hide the window.

```py
def hide(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L826)

### Window.hide_titlebar

Hide the titlebar.

```py
def hide_titlebar(self, flag: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L935)

### Window.is_alive

Check if the window is alive.

```py
def is_alive(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1002)

### Window.is_running

Check if the window is running. (alias as is_alive)

```py
def is_running(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1006)

### Window.keep_on_top

Set the window to keep on top.

```py
def keep_on_top(self, flag: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L924)

### Window.maximize

Maximize the window. (`resizable` should be set to True)

```py
def maximize(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L837)

### Window.minimize

Minimize the window.

```py
def minimize(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L812)

### Window.move

Move the window. (same as set_location)

```py
def move(self, x: int, y: int) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L595)

### Window.move_to_center

Move the window to the center of the screen.

```py
def move_to_center(self, center_pos: Union[tuple[int, int], None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L607)

### Window.normal

Set normal window.

```py
def normal(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L817)

### Window.post_event

Post an event.

```py
def post_event(self, key: KeyType, values: dict[KeyType, Any]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L346)

### Window.post_event_after

Post an event after msec.

```py
def post_event_after(
    self, msec: int, key: KeyType, values: dict[KeyType, Any]
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L350)

### Window.read

Read events from the window.

```py
def read(
    self, timeout: Union[int, None] = None, timeout_key: str = WINDOW_TIMEOUT
    ) -> tuple[KeyType, dict[KeyType, Any]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L652)

### Window.refresh

Refresh window

```py
def refresh(self) -> "Window":
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1026)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L406)

### Window.screenshot

Take a screenshot of the window.

```py
def screenshot(self) -> PILImage.Image:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1122)

### Window.send_to_back

Send the window to the back, and make it not keep on top.

```py
def send_to_back(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L929)

### Window.set_alpha_channel

Set the alpha channel of the window.

```py
def set_alpha_channel(self, alpha: float) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L842)

### Window.set_grab_anywhere

Set grab anywhere

```py
def set_grab_anywhere(self, flag: bool) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1034)

### Window.set_location

Set window location.

```py
def set_location(self, xy: tuple[int, int]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L383)

### Window.set_size

Set the window size.

```py
def set_size(self, size: tuple[int, int]) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L802)

### Window.set_timeout

Set a timeout event.

```py
def set_timeout(self, callback: Callable, msec: int, *args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L356)

### Window.set_title

Set the title of the window.

```py
def set_title(self, title: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L807)

### Window.show

Show hidden window (hide -> show)

```py
def show(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1018)

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
    *args,
    end_key: str = WINDOW_THREAD_END,  # the thread processing is complete, end_key will be released
    **kw,
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L726)

### Window.un_hide

Un hide the window.

```py
def un_hide(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L831)

### Window.update_idle_tasks

Update idle tasks.

```py
def update_idle_tasks(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L603)

# Functions of TkEasyGUI.widgets

- [align_center](#align_center)
- [align_left](#align_left)
- [align_right](#align_right)
- [cast](#cast)
- [generate_element_id](#generate_element_id)
- [generate_element_style_key](#generate_element_style_key)
- [get_active_eg_window](#get_active_eg_window)
- [get_current_theme](#get_current_theme)
- [get_eg_window_count](#get_eg_window_count)
- [get_image_tk](#get_image_tk)
- [get_last_eg_window](#get_last_eg_window)
- [get_root_window](#get_root_window)
- [get_ttk_style](#get_ttk_style)
- [pop_easy_window](#pop_easy_window)
- [push_easy_window](#push_easy_window)
- [register_element_key](#register_element_key)
- [remove_element_key](#remove_element_key)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5128)

## align_left

Align left : layout helper

```py
def align_left(parts: list[Element]) -> list[Element]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5142)

## align_right

Align right : layout helper

```py
def align_right(parts: list[Element]) -> list[Element]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5135)

## cast

Cast a value to a type.

This returns the value unchanged.  To the type checker this
signals that the return value has the designated type, but at
runtime we intentionally don't check anything (we want this
to be as fast as possible).

```py
def cast(typ, val):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/Users/kujirahand/.pyenv/versions/3.13.9/lib/python3.13/typing.py#L2371)

## generate_element_id

Generate a unique id for a value element.

```py
def generate_element_id() -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L202)

## generate_element_style_key

Get a unique id for an element.

```py
def generate_element_style_key(element_type: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L187)

## get_active_eg_window

Get the active window.

```py
def get_active_eg_window() -> Union[tk.Toplevel, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L207)

## get_current_theme

Get current theme

```py
def get_current_theme() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L244)

## get_eg_window_count

Get the number of windows.

```py
def get_eg_window_count() -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L221)

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_image.py#L15)

## get_last_eg_window

Get the parent window.

```py
def get_last_eg_window() -> Union["Window", None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L214)

## get_root_window

Get root window.

```py
def get_root_window() -> tk.Tk:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L161)

## get_ttk_style

Get ttk style

```py
def get_ttk_style() -> ttk.Style:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L171)

## pop_easy_window

Pop a window from the list.

```py
def pop_easy_window(win: "Window") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L231)

## push_easy_window

Push a window to the list.

```py
def push_easy_window(win: "Window") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L226)

## register_element_key

Register element key.

```py
def register_element_key(key: KeyType) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L192)

## remove_element_key

Remove element key.

```py
def remove_element_key(key: KeyType) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L197)

## rgb

Convert RGB to Hex

```py
def rgb(r: int, g: int, b: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5170)

## time_checker_end

Timer end

```py
def time_checker_end(start_time: datetime) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5183)

## time_checker_start

Timer start

```py
def time_checker_start() -> datetime:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5178)

## valign_bottom

Vertical align bottom : layout helper

```py
def valign_bottom(grid: list[list[Element]]) -> list[list[Element]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5163)

## valign_middle

Vertical align middle : layout helper

```py
def valign_middle(grid: list[list[Element]]) -> list[list[Element]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5152)

## valign_top

Vertical align top : layout helper

```py
def valign_top(grid: list[list[Element]]) -> list[list[Element]]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L5147)

