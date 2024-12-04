# Module TkEasyGUI.widgets

TkEasyGUI Widgets

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
- [Radio](#radio)
- [Slider](#slider)
- [Submit](#submit)
- [Tab](#tab)
- [TabGroup](#tabgroup)
- [Table](#table)
- [Text](#text)
- [Textarea](#textarea)
- [TkEasyError](#tkeasyerror)
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
    background_color: Union[str, None] = None,  # background color (not supported on macOS)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1775)

### Methods of Button



### Button.bind

Bind event. @see [Window.bind](#windowbind)

### Button.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Button.create

Create a Button widget.

### Button.disptach_event

Dispatch event

### Button.get

Returns the text of the button..

### Button.get_height

Get height of element.

### Button.get_name

Get key of element.

### Button.get_prev_widget

Get the previous widget.

### Button.get_text

Get the text of the button.

### Button.get_width

Get width of element.

### Button.post_create

Post create widget.

### Button.prepare_create

### Button.set_button_color

Set the button color.

### Button.set_disabled

Set disabled widgets state

### Button.set_text

Set the text of the button.

### Button.update

Update the widget.

## CalendarBrowse

CalendarBrowse element.

```py
class CalendarBrowse(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    default_date: Union[datetime, None] = None,
    date_format: Union[str, None] = "%Y-%m-%d",
    title: str = "",
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3785)

### Methods of CalendarBrowse



### CalendarBrowse.bind

Bind event. @see [Window.bind](#windowbind)

### CalendarBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### CalendarBrowse.create

### CalendarBrowse.disptach_event

Dispatch event

### CalendarBrowse.get

Get the value of the widget.

### CalendarBrowse.get_height

Get height of element.

### CalendarBrowse.get_name

Get key of element.

### CalendarBrowse.get_prev_widget

Get the previous widget.

### CalendarBrowse.get_width

Get width of element.

### CalendarBrowse.post_create

Post create widget.

### CalendarBrowse.prepare_create

### CalendarBrowse.set_disabled

Set disabled widgets state

### CalendarBrowse.set_text

Set the text of the button.

### CalendarBrowse.show_dialog

Show file dialog

### CalendarBrowse.update

Update the widget.

## CalendarButton

CalendarButton element. (alias of CalendarBrowse)

```py
class CalendarButton(
    self,
    button_text: str = "...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    default_date: Union[datetime, None] = None,
    date_format: Union[str, None] = "%Y-%m-%d",
    title: str = "",
    enable_events: bool = False,  # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3785)

### Methods of CalendarButton



### CalendarButton.bind

Bind event. @see [Window.bind](#windowbind)

### CalendarButton.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### CalendarButton.create

### CalendarButton.disptach_event

Dispatch event

### CalendarButton.get

Get the value of the widget.

### CalendarButton.get_height

Get height of element.

### CalendarButton.get_name

Get key of element.

### CalendarButton.get_prev_widget

Get the previous widget.

### CalendarButton.get_width

Get width of element.

### CalendarButton.post_create

Post create widget.

### CalendarButton.prepare_create

### CalendarButton.set_disabled

Set disabled widgets state

### CalendarButton.set_text

Set the text of the button.

### CalendarButton.show_dialog

Show file dialog

### CalendarButton.update

Update the widget.

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
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2747)

### Methods of Canvas



### Canvas.bind

Bind event. @see [Window.bind](#windowbind)

### Canvas.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Canvas.clear

Clear the canvas.

### Canvas.create

### Canvas.disptach_event

Dispatch event

### Canvas.get

Return Widget

### Canvas.get_height

Get height of element.

### Canvas.get_name

Get key of element.

### Canvas.get_prev_widget

Get the previous widget.

### Canvas.get_width

Get width of element.

### Canvas.post_create

Post create widget.

### Canvas.prepare_create

### Canvas.set_disabled

Set disabled widgets state

### Canvas.update

Update the widget.

## Checkbox

Checkbox element.

```py
class Checkbox(
    self, text: str="",
    default: bool=False,
    key: Union[str, None] = None,
    enable_events: bool=False,
    group_id: Union[str, None] = None, # If a group_id is provided, the values will contain key's list of True
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1914)

### Methods of Checkbox



### Checkbox.bind

Bind event. @see [Window.bind](#windowbind)

### Checkbox.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Checkbox.create

### Checkbox.disptach_event

Dispatch event

### Checkbox.get

Get the value of the widget.

### Checkbox.get_height

Get height of element.

### Checkbox.get_name

Get key of element.

### Checkbox.get_prev_widget

Get the previous widget.

### Checkbox.get_value

Get the value of the widget.

### Checkbox.get_width

Get width of element.

### Checkbox.post_create

Post create widget.

### Checkbox.prepare_create

### Checkbox.set_disabled

Set disabled widgets state

### Checkbox.set_text

Set the text of the widget.

### Checkbox.set_value

Set the value of the widget.

### Checkbox.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1885)

### Methods of CloseButton



### CloseButton.bind

Bind event. @see [Window.bind](#windowbind)

### CloseButton.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### CloseButton.close_window

Close the window.

### CloseButton.create

Create a Button widget.

### CloseButton.disptach_event

Dispatch event

### CloseButton.get

Returns the text of the button..

### CloseButton.get_height

Get height of element.

### CloseButton.get_name

Get key of element.

### CloseButton.get_prev_widget

Get the previous widget.

### CloseButton.get_text

Get the text of the button.

### CloseButton.get_width

Get width of element.

### CloseButton.post_create

Post create widget.

### CloseButton.prepare_create

### CloseButton.set_button_color

Set the button color.

### CloseButton.set_disabled

Set disabled widgets state

### CloseButton.set_text

Set the text of the button.

### CloseButton.update

Update the widget.

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
    enable_events: bool = False, # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3651)

### Methods of ColorBrowse



### ColorBrowse.bind

Bind event. @see [Window.bind](#windowbind)

### ColorBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### ColorBrowse.create

### ColorBrowse.disptach_event

Dispatch event

### ColorBrowse.get

Get the value of the widget.

### ColorBrowse.get_height

Get height of element.

### ColorBrowse.get_name

Get key of element.

### ColorBrowse.get_prev_widget

Get the previous widget.

### ColorBrowse.get_width

Get width of element.

### ColorBrowse.post_create

Post create widget.

### ColorBrowse.prepare_create

### ColorBrowse.set_disabled

Set disabled widgets state

### ColorBrowse.set_text

Set the text of the button.

### ColorBrowse.show_dialog

Show file dialog

### ColorBrowse.update

Update the widget.

## Column

Frame element.

```py
class Column(
    self,
    layout: list[list[Element]],
    key: str = "",
    background_color: Union[str, None] = None,
    vertical_alignment: TextVAlign="top",
    size: Union[tuple[int, int], None] = None, # set (width, height) pixel size
    width: Union[int, None] = None, # set pixel width
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1367)

### Methods of Column



### Column.bind

Bind event. @see [Window.bind](#windowbind)

### Column.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Column.create

### Column.disptach_event

Dispatch event

### Column.get

Return Widget

### Column.get_height

Get height of element.

### Column.get_name

Get key of element.

### Column.get_prev_widget

Get the previous widget.

### Column.get_width

Get width of element.

### Column.post_create

Post create widget.

### Column.prepare_create

### Column.set_disabled

Set disabled widgets state

### Column.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3183)

### Methods of Combo



### Combo.bind

Bind event. @see [Window.bind](#windowbind)

### Combo.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Combo.create

[Combo.create] create Listbox widget

### Combo.disptach_event

Dispatch event

### Combo.get

Get the value of the widget.

### Combo.get_height

Get height of element.

### Combo.get_name

Get key of element.

### Combo.get_prev_widget

Get the previous widget.

### Combo.get_width

Get width of element.

### Combo.post_create

Post create widget.

### Combo.prepare_create

### Combo.set_disabled

Set disabled widgets state

### Combo.set_readonly

set readonly

### Combo.set_value

Set the value of the widget.

### Combo.set_values

Set values to list

### Combo.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L963)

### Methods of Element



### Element.bind

Bind event. @see [Window.bind](#windowbind)

### Element.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Element.create

Create a widget.

### Element.disptach_event

Dispatch event

### Element.get

Get the value of the widget.

### Element.get_height

Get height of element.

### Element.get_name

Get key of element.

### Element.get_prev_widget

Get the previous widget.

### Element.get_width

Get width of element.

### Element.post_create

Post create widget.

### Element.prepare_create

### Element.set_disabled

Set disabled widgets state

### Element.update

update widget configuration.

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
    enable_events: bool = False, # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3478)

### Methods of FileBrowse



### FileBrowse.bind

Bind event. @see [Window.bind](#windowbind)

### FileBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### FileBrowse.create

### FileBrowse.disptach_event

Dispatch event

### FileBrowse.get

Get the value of the widget.

### FileBrowse.get_height

Get height of element.

### FileBrowse.get_name

Get key of element.

### FileBrowse.get_prev_widget

Get the previous widget.

### FileBrowse.get_width

Get width of element.

### FileBrowse.post_create

Post create widget.

### FileBrowse.prepare_create

### FileBrowse.set_disabled

Set disabled widgets state

### FileBrowse.set_text

Set the text of the button.

### FileBrowse.show_dialog

Show file dialog

### FileBrowse.update

Update the widget.

## FileSaveAs

FileSaveAs element. (alias of FileSaveAsBrowse)

```py
class FileSaveAs(
    self,
    button_text: str="...",
    key: Union[str, None] = None,
    target_key: Union[str, None] = None,
    title: str = "",
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    enable_events: bool = False, # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3588)

### Methods of FileSaveAs



### FileSaveAs.bind

Bind event. @see [Window.bind](#windowbind)

### FileSaveAs.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### FileSaveAs.create

### FileSaveAs.disptach_event

Dispatch event

### FileSaveAs.get

Get the value of the widget.

### FileSaveAs.get_height

Get height of element.

### FileSaveAs.get_name

Get key of element.

### FileSaveAs.get_prev_widget

Get the previous widget.

### FileSaveAs.get_width

Get width of element.

### FileSaveAs.post_create

Post create widget.

### FileSaveAs.prepare_create

### FileSaveAs.set_disabled

Set disabled widgets state

### FileSaveAs.set_text

Set the text of the button.

### FileSaveAs.show_dialog

Show file dialog

### FileSaveAs.update

Update the widget.

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
    enable_events: bool = False, # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3588)

### Methods of FileSaveAsBrowse



### FileSaveAsBrowse.bind

Bind event. @see [Window.bind](#windowbind)

### FileSaveAsBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### FileSaveAsBrowse.create

### FileSaveAsBrowse.disptach_event

Dispatch event

### FileSaveAsBrowse.get

Get the value of the widget.

### FileSaveAsBrowse.get_height

Get height of element.

### FileSaveAsBrowse.get_name

Get key of element.

### FileSaveAsBrowse.get_prev_widget

Get the previous widget.

### FileSaveAsBrowse.get_width

Get width of element.

### FileSaveAsBrowse.post_create

Post create widget.

### FileSaveAsBrowse.prepare_create

### FileSaveAsBrowse.set_disabled

Set disabled widgets state

### FileSaveAsBrowse.set_text

Set the text of the button.

### FileSaveAsBrowse.show_dialog

Show file dialog

### FileSaveAsBrowse.update

Update the widget.

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
    enable_events: bool = False, # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3564)

### Methods of FilesBrowse



### FilesBrowse.bind

Bind event. @see [Window.bind](#windowbind)

### FilesBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### FilesBrowse.create

### FilesBrowse.disptach_event

Dispatch event

### FilesBrowse.get

Get the value of the widget.

### FilesBrowse.get_height

Get height of element.

### FilesBrowse.get_name

Get key of element.

### FilesBrowse.get_prev_widget

Get the previous widget.

### FilesBrowse.get_width

Get width of element.

### FilesBrowse.post_create

Post create widget.

### FilesBrowse.prepare_create

### FilesBrowse.set_disabled

Set disabled widgets state

### FilesBrowse.set_text

Set the text of the button.

### FilesBrowse.show_dialog

Show file dialog

### FilesBrowse.update

Update the widget.

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
    enable_events: bool = False, # enable changing events
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3616)

### Methods of FolderBrowse



### FolderBrowse.bind

Bind event. @see [Window.bind](#windowbind)

### FolderBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### FolderBrowse.create

### FolderBrowse.disptach_event

Dispatch event

### FolderBrowse.get

Get the value of the widget.

### FolderBrowse.get_height

Get height of element.

### FolderBrowse.get_name

Get key of element.

### FolderBrowse.get_prev_widget

Get the previous widget.

### FolderBrowse.get_width

Get width of element.

### FolderBrowse.post_create

Post create widget.

### FolderBrowse.prepare_create

### FolderBrowse.set_disabled

Set disabled widgets state

### FolderBrowse.set_text

Set the text of the button.

### FolderBrowse.show_dialog

Show file dialog

### FolderBrowse.update

Update the widget.

## Frame

Frame element.

```py
class Frame(
    self,
    title: str,
    layout: list[list[Element]],
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1298)

### Methods of Frame



### Frame.bind

Bind event. @see [Window.bind](#windowbind)

### Frame.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Frame.create

Create a Frame widget.

### Frame.disptach_event

Dispatch event

### Frame.get

Return Widget

### Frame.get_height

Get height of element.

### Frame.get_name

Get key of element.

### Frame.get_prev_widget

Get the previous widget.

### Frame.get_width

Get width of element.

### Frame.post_create

Post create widget.

### Frame.prepare_create

### Frame.set_disabled

Set disabled widgets state

### Frame.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2792)

### Methods of Graph



### Graph.bind

Bind event. @see [Window.bind](#windowbind)

### Graph.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Graph.create

### Graph.disptach_event

Dispatch event

### Graph.draw_arc

Draw an arc.

### Graph.draw_circle

Draw a circle.

### Graph.draw_image

Draw image

### Graph.draw_line

Draw a line.

### Graph.draw_lines

Draw lines.

### Graph.draw_oval

Draw an oval.

### Graph.draw_point

Draw a point.

### Graph.draw_polygon

Draw polygon

### Graph.draw_rectangle

Draw rectangle

### Graph.draw_text

Draw text

### Graph.erase

Delete all

### Graph.get

Return Widget

### Graph.get_height

Get height of element.

### Graph.get_name

Get key of element.

### Graph.get_prev_widget

Get the previous widget.

### Graph.get_width

Get width of element.

### Graph.post_create

Post create widget.

### Graph.prepare_create

### Graph.set_disabled

Set disabled widgets state

### Graph.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3040)

### Methods of HSeparator



### HSeparator.bind

Bind event. @see [Window.bind](#windowbind)

### HSeparator.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### HSeparator.create

### HSeparator.disptach_event

Dispatch event

### HSeparator.get

Get the value of the widget.

### HSeparator.get_height

Get height of element.

### HSeparator.get_name

Get key of element.

### HSeparator.get_prev_widget

Get the previous widget.

### HSeparator.get_width

Get width of element.

### HSeparator.post_create

Post create widget.

### HSeparator.prepare_create

### HSeparator.set_disabled

Set disabled widgets state

### HSeparator.update

update widget configuration.

## Image

Image element.

```py
class Image(
    self,
    source: Union[bytes, str, None] = None, # image source
    filename = None, # filen ame
    data: bytes = None, # image data
    key: Union[str, None] = None,
    background_color: Union[str, None] = None, # background color (example) "red", "#FF0000"
    size: tuple[int, int] = (300, 300),
    enable_events: bool = False,
    # other
    metadata: Union[dict[str, Any], None] = None,
    **kw) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2903)

### Methods of Image



### Image.bind

Bind event. @see [Window.bind](#windowbind)

### Image.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Image.create

Create a Image widget.

### Image.disptach_event

Dispatch event

### Image.erase

Erase image

### Image.get

Return Widget

### Image.get_height

Get height of element.

### Image.get_name

Get key of element.

### Image.get_prev_widget

Get the previous widget.

### Image.get_width

Get width of element.

### Image.post_create

Post create widget.

### Image.prepare_create

### Image.screenshot

Take a screenshot

### Image.set_disabled

Set disabled widgets state

### Image.set_image

Set image to Image widget.
- ImageResizeType is NO_RESIZE/FIT_HEIGHT/FIT_WIDTH/FIT_BOTH/IGNORE_ASPECT_RATIO/CROP_TO_SQUARE

### Image.update

Update the widget.

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
    size: Union[tuple[int, int], None] = None, # set (width, height) character size (only width is supported)
    width: Union[int, None] = None, # set width character size
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2067)

### Methods of Input



### Input.bind

Bind event. @see [Window.bind](#windowbind)

### Input.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Input.copy

copy to clipboard

### Input.copy_selected_text

Copy selected text

### Input.create

create Input widget

### Input.cut

cut to clipboard

### Input.delete_selected

delete selected text

### Input.disptach_event

Dispatch event

### Input.get

Get the value of the widget.

### Input.get_cursor_pos

get cursor position

### Input.get_height

Get height of element.

### Input.get_name

Get key of element.

### Input.get_prev_widget

Get the previous widget.

### Input.get_selected_text

get selected text

### Input.get_selection_length

get selection length

### Input.get_selection_pos

get selection positions

### Input.get_selection_start

get selection start

### Input.get_text

get text

### Input.get_width

Get width of element.

### Input.paste

paste from clipboard

### Input.post_create

Post create widget.

### Input.prepare_create

### Input.select_all

select_all

### Input.set_cursor_pos

set cursor position

### Input.set_disabled

Set disabled widgets state

### Input.set_readonly

set readonly

### Input.set_selection_start

set selection start and length

### Input.set_text

set text

### Input.update

Update the widget.

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
    size: Union[tuple[int, int], None] = None, # set (width, height) character size (only width is supported)
    width: Union[int, None] = None, # set width character size
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2067)

### Methods of InputText



### InputText.bind

Bind event. @see [Window.bind](#windowbind)

### InputText.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### InputText.copy

copy to clipboard

### InputText.copy_selected_text

Copy selected text

### InputText.create

create Input widget

### InputText.cut

cut to clipboard

### InputText.delete_selected

delete selected text

### InputText.disptach_event

Dispatch event

### InputText.get

Get the value of the widget.

### InputText.get_cursor_pos

get cursor position

### InputText.get_height

Get height of element.

### InputText.get_name

Get key of element.

### InputText.get_prev_widget

Get the previous widget.

### InputText.get_selected_text

get selected text

### InputText.get_selection_length

get selection length

### InputText.get_selection_pos

get selection positions

### InputText.get_selection_start

get selection start

### InputText.get_text

get text

### InputText.get_width

Get width of element.

### InputText.paste

paste from clipboard

### InputText.post_create

Post create widget.

### InputText.prepare_create

### InputText.select_all

select_all

### InputText.set_cursor_pos

set cursor position

### InputText.set_disabled

Set disabled widgets state

### InputText.set_readonly

set readonly

### InputText.set_selection_start

set selection start and length

### InputText.set_text

set text

### InputText.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1594)

### Methods of Label



### Label.bind

Bind event. @see [Window.bind](#windowbind)

### Label.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Label.create

Create a Text widget.

### Label.disptach_event

Dispatch event

### Label.get

Get the value of the widget.

### Label.get_height

Get height of element.

### Label.get_name

Get key of element.

### Label.get_prev_widget

Get the previous widget.

### Label.get_text

### Label.get_width

Get width of element.

### Label.post_create

Post create widget.

### Label.prepare_create

### Label.set_disabled

Set disabled widgets state

### Label.set_text

Set the text of the widget.

### Label.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3687)

### Methods of ListBrowse



### ListBrowse.bind

Bind event. @see [Window.bind](#windowbind)

### ListBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### ListBrowse.create

### ListBrowse.disptach_event

Dispatch event

### ListBrowse.get

Get the value of the widget.

### ListBrowse.get_height

Get height of element.

### ListBrowse.get_name

Get key of element.

### ListBrowse.get_prev_widget

Get the previous widget.

### ListBrowse.get_width

Get width of element.

### ListBrowse.post_create

Post create widget.

### ListBrowse.prepare_create

### ListBrowse.set_disabled

Set disabled widgets state

### ListBrowse.set_text

Set the text of the button.

### ListBrowse.show_dialog

Show Listbox dialog

### ListBrowse.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3065)

### Methods of Listbox



### Listbox.bind

Bind event. @see [Window.bind](#windowbind)

### Listbox.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Listbox.create

[Listbox.create] create Listbox widget

### Listbox.disptach_event

Dispatch event

### Listbox.get

Get the value of the widget.

### Listbox.get_cursor_index

Get cursor index (return -1 if not selected)

### Listbox.get_height

Get height of element.

### Listbox.get_name

Get key of element.

### Listbox.get_prev_widget

Get the previous widget.

### Listbox.get_selected_items

Get selected items

### Listbox.get_width

Get width of element.

### Listbox.post_create

Post create widget.

### Listbox.prepare_create

### Listbox.select_values

Select values

### Listbox.set_cursor_index

Set cursor index

### Listbox.set_disabled

Set disabled widgets state

### Listbox.set_values

Set values to list

### Listbox.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1673)

### Methods of Menu



### Menu.bind

Bind event. @see [Window.bind](#windowbind)

### Menu.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Menu.create

Create a Text widget.

### Menu.disptach_event

Dispatch event

### Menu.get

Get the value of the widget.

### Menu.get_height

Get height of element.

### Menu.get_name

Get key of element.

### Menu.get_prev_widget

Get the previous widget.

### Menu.get_text

### Menu.get_width

Get width of element.

### Menu.post_create

Post create widget.

### Menu.prepare_create

### Menu.set_disabled

Set disabled widgets state

### Menu.set_text

Set the text of the widget.

### Menu.update

Update the widget.

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
    autoscroll: bool = False, # When autoscroll is set to True, it scrolls to the end with text changes.
    readonly_background_color: Union[str, None] = None,
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2310)

### Methods of Multiline



### Multiline.bind

Bind event. @see [Window.bind](#windowbind)

### Multiline.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Multiline.copy

Copy the selected text.

### Multiline.create

Create a Multiline widget.

### Multiline.cut

Cut the selected text.

### Multiline.disptach_event

Dispatch event

### Multiline.get

Get the value of the widget.

### Multiline.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

### Multiline.get_height

Get height of element.

### Multiline.get_name

Get key of element.

### Multiline.get_prev_widget

Get the previous widget.

### Multiline.get_selected_text

Get the selected text.

### Multiline.get_selection_length

get selection length

### Multiline.get_selection_pos

Get selection position, returns (start_pos, end_pos).

### Multiline.get_selection_start

get selection start

### Multiline.get_text

Get the text of the widget.

### Multiline.get_width

Get width of element.

### Multiline.index_to_pos

Convert index to postion.

### Multiline.paste

Paste the text.

### Multiline.pos_to_index

Convert position to index.

### Multiline.post_create

Post create widget.

### Multiline.prepare_create

### Multiline.print

Print text.

### Multiline.select_all

select all text

### Multiline.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

### Multiline.set_disabled

Set disabled widgets state

### Multiline.set_readonly

Set readonly

### Multiline.set_selection_pos

Set selection position.

### Multiline.set_selection_start

set selection start

### Multiline.set_text

Set text

### Multiline.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3736)

### Methods of MultilineBrowse



### MultilineBrowse.bind

Bind event. @see [Window.bind](#windowbind)

### MultilineBrowse.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### MultilineBrowse.create

### MultilineBrowse.disptach_event

Dispatch event

### MultilineBrowse.get

Get the value of the widget.

### MultilineBrowse.get_height

Get height of element.

### MultilineBrowse.get_name

Get key of element.

### MultilineBrowse.get_prev_widget

Get the previous widget.

### MultilineBrowse.get_width

Get width of element.

### MultilineBrowse.post_create

Post create widget.

### MultilineBrowse.prepare_create

### MultilineBrowse.set_disabled

Set disabled widgets state

### MultilineBrowse.set_text

Set the text of the button.

### MultilineBrowse.show_dialog

Show Listbox dialog

### MultilineBrowse.update

Update the widget.

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
    autoscroll: bool = False, # When autoscroll is set to True, it scrolls to the end with text changes.
    readonly_background_color: Union[str, None] = None,
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2310)

### Methods of Output



### Output.bind

Bind event. @see [Window.bind](#windowbind)

### Output.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Output.copy

Copy the selected text.

### Output.create

Create a Multiline widget.

### Output.cut

Cut the selected text.

### Output.disptach_event

Dispatch event

### Output.get

Get the value of the widget.

### Output.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

### Output.get_height

Get height of element.

### Output.get_name

Get key of element.

### Output.get_prev_widget

Get the previous widget.

### Output.get_selected_text

Get the selected text.

### Output.get_selection_length

get selection length

### Output.get_selection_pos

Get selection position, returns (start_pos, end_pos).

### Output.get_selection_start

get selection start

### Output.get_text

Get the text of the widget.

### Output.get_width

Get width of element.

### Output.index_to_pos

Convert index to postion.

### Output.paste

Paste the text.

### Output.pos_to_index

Convert position to index.

### Output.post_create

Post create widget.

### Output.prepare_create

### Output.print

Print text.

### Output.select_all

select all text

### Output.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

### Output.set_disabled

Set disabled widgets state

### Output.set_readonly

Set readonly

### Output.set_selection_pos

Set selection position.

### Output.set_selection_start

set selection start

### Output.set_text

Set text

### Output.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1978)

### Methods of Radio



### Radio.bind

Bind event. @see [Window.bind](#windowbind)

### Radio.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Radio.create

### Radio.disptach_event

Dispatch event

### Radio.get

Get the value of the widget.

### Radio.get_height

Get height of element.

### Radio.get_name

Get key of element.

### Radio.get_prev_widget

Get the previous widget.

### Radio.get_value

Get the value of the widget.

### Radio.get_width

Get width of element.

### Radio.is_selected

Check if the radio button is selected.

### Radio.post_create

Post create widget.

### Radio.prepare_create

### Radio.select

Select the radio button.

### Radio.set_disabled

Set disabled widgets state

### Radio.set_text

Set the text of the widget.

### Radio.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2627)

### Methods of Slider



### Slider.bind

Bind event. @see [Window.bind](#windowbind)

### Slider.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Slider.create

Create the widget.

### Slider.disptach_event

Dispatch event

### Slider.get

Return slider value.

### Slider.get_height

Get height of element.

### Slider.get_name

Get key of element.

### Slider.get_prev_widget

Get the previous widget.

### Slider.get_range

### Slider.get_width

Get width of element.

### Slider.post_create

Post create widget.

### Slider.prepare_create

### Slider.set

Set value of Slider

### Slider.set_disabled

Set disabled widgets state

### Slider.set_range

Set the range of the slider.

### Slider.update

Update the widget.

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
    background_color: Union[str, None] = None,  # background color (not supported on macOS)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1775)

### Methods of Submit



### Submit.bind

Bind event. @see [Window.bind](#windowbind)

### Submit.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Submit.create

Create a Button widget.

### Submit.disptach_event

Dispatch event

### Submit.get

Returns the text of the button..

### Submit.get_height

Get height of element.

### Submit.get_name

Get key of element.

### Submit.get_prev_widget

Get the previous widget.

### Submit.get_text

Get the text of the button.

### Submit.get_width

Get width of element.

### Submit.post_create

Post create widget.

### Submit.prepare_create

### Submit.set_button_color

Set the button color.

### Submit.set_disabled

Set disabled widgets state

### Submit.set_text

Set the text of the button.

### Submit.update

Update the widget.

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
    layout: list[list[Element]],
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1446)

### Methods of Tab



### Tab.bind

Bind event. @see [Window.bind](#windowbind)

### Tab.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Tab.create

### Tab.disptach_event

Dispatch event

### Tab.get

Return Widget title

### Tab.get_height

Get height of element.

### Tab.get_name

Get key of element.

### Tab.get_prev_widget

Get the previous widget.

### Tab.get_width

Get width of element.

### Tab.post_create

Post create widget.

### Tab.prepare_create

### Tab.set_disabled

Set disabled widgets state

### Tab.update

Update the widget.

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
    layout: Union[list[list["TabGroup"]], list["TabGroup"]],
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1526)

### Methods of TabGroup



### TabGroup.bind

Bind event. @see [Window.bind](#windowbind)

### TabGroup.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### TabGroup.create

### TabGroup.disptach_event

Dispatch event

### TabGroup.get

Return Widget

### TabGroup.get_height

Get height of element.

### TabGroup.get_name

Get key of element.

### TabGroup.get_prev_widget

Get the previous widget.

### TabGroup.get_width

Get width of element.

### TabGroup.post_create

### TabGroup.prepare_create

### TabGroup.set_disabled

Set disabled widgets state

### TabGroup.update

Update the widget.

## Table

Table element.

```py
class Table(
    self,
    values: list[list[str]] = [], # Specify the table values as 2D list.
    headings: list[str] = [], # Specify the table header as a list.
    key: Union[str, None] = None,
    justification: TextAlign = "center",
    auto_size_columns: bool = True,
    max_col_width: int = 0,
    col_widths: Union[list[int], None] = None,
    enable_events: bool = False,
    event_returns_values: Union[bool, None] = None, # Returns the table value if set to True, otherwise returns the index.
    select_mode: str="browse",
    max_columns: int = 20, # This property cannot be changed later. It is advisable to set a larger value.
    vertical_scroll_only: bool = True, # vertical scroll only
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3254)

### Methods of Table



### Table.bind

Bind event. @see [Window.bind](#windowbind)

### Table.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Table.create

Create a Table widget.

### Table.disptach_event

Dispatch event

### Table.get

Get the value of the widget.

### Table.get_height

Get height of element.

### Table.get_name

Get key of element.

### Table.get_prev_widget

Get the previous widget.

### Table.get_width

Get width of element.

### Table.load_from_file

Load data from a file.

### Table.post_create

Post create widget.

### Table.prepare_create

### Table.set_disabled

Set disabled widgets state

### Table.set_values

Set values to the table.

### Table.update

Update the widget.

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L1594)

### Methods of Text



### Text.bind

Bind event. @see [Window.bind](#windowbind)

### Text.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Text.create

Create a Text widget.

### Text.disptach_event

Dispatch event

### Text.get

Get the value of the widget.

### Text.get_height

Get height of element.

### Text.get_name

Get key of element.

### Text.get_prev_widget

Get the previous widget.

### Text.get_text

### Text.get_width

Get width of element.

### Text.post_create

Post create widget.

### Text.prepare_create

### Text.set_disabled

Set disabled widgets state

### Text.set_text

Set the text of the widget.

### Text.update

Update the widget.

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
    autoscroll: bool = False, # When autoscroll is set to True, it scrolls to the end with text changes.
    readonly_background_color: Union[str, None] = None,
    metadata: Union[dict[str, Any], None] = None,
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L2310)

### Methods of Textarea



### Textarea.bind

Bind event. @see [Window.bind](#windowbind)

### Textarea.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### Textarea.copy

Copy the selected text.

### Textarea.create

Create a Multiline widget.

### Textarea.cut

Cut the selected text.

### Textarea.disptach_event

Dispatch event

### Textarea.get

Get the value of the widget.

### Textarea.get_cursor_pos

Get Cursor position. liek `3.0` row=3, col=0

### Textarea.get_height

Get height of element.

### Textarea.get_name

Get key of element.

### Textarea.get_prev_widget

Get the previous widget.

### Textarea.get_selected_text

Get the selected text.

### Textarea.get_selection_length

get selection length

### Textarea.get_selection_pos

Get selection position, returns (start_pos, end_pos).

### Textarea.get_selection_start

get selection start

### Textarea.get_text

Get the text of the widget.

### Textarea.get_width

Get width of element.

### Textarea.index_to_pos

Convert index to postion.

### Textarea.paste

Paste the text.

### Textarea.pos_to_index

Convert position to index.

### Textarea.post_create

Post create widget.

### Textarea.prepare_create

### Textarea.print

Print text.

### Textarea.select_all

select all text

### Textarea.set_cursor_pos

Set cursor position. (like `3.0`, row=3, col=0)

### Textarea.set_disabled

Set disabled widgets state

### Textarea.set_readonly

Set readonly

### Textarea.set_selection_pos

Set selection position.

### Textarea.set_selection_start

set selection start

### Textarea.set_text

Set text

### Textarea.update

Update the widget.

## TkEasyError



```py
class TkEasyError(self, message="TkEasyError"):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L74)

### Methods of TkEasyError



### TkEasyError.add_note

Exception.add_note(note) --
    add a note to the exception

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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3016)

### Methods of VSeparator



### VSeparator.bind

Bind event. @see [Window.bind](#windowbind)

### VSeparator.bind_events

Bind user events. @see [custom events](/docs/custom_events.md)
The specification is such that if the suffix "/hide" is attached to an event key, that event key will not be returned to the user.
@see [Window.read](#windowread)

### VSeparator.create

### VSeparator.disptach_event

Dispatch event

### VSeparator.get

Get the value of the widget.

### VSeparator.get_height

Get height of element.

### VSeparator.get_name

Get key of element.

### VSeparator.get_prev_widget

Get the previous widget.

### VSeparator.get_width

Get width of element.

### VSeparator.post_create

Post create widget.

### VSeparator.prepare_create

### VSeparator.set_disabled

Set disabled widgets state

### VSeparator.update

update widget configuration.

## Window

Main window object in TkEasyGUI

```py
class Window(
    self,
    title: str,
    layout: list[list[Element]],  # set elements layout
    size: Union[tuple[int, int], None] = None,  # window size
    resizable: bool = False,
    font: Union[FontType, None] = None,
    modal: bool = False,  # modal window
    keep_on_top: bool = False,  # keep on top
    no_titlebar: bool = False,  # hide titlebar
    grab_anywhere: bool = False,  # can move window by dragging anywhere
    alpha_channel: float = 1.0,  # window alpha channel
    enable_key_events: bool = False,  # enable keyboard events
    return_keyboard_events: bool = False,  # enable keyboard events (for compatibility)
    location: Union[tuple[int, int], None] = None,  # window location
    center_window: bool = True,  # move window to center
    row_padding: int = 2,  # row padding
    padding_x: int = 8,  # x padding around the window
    padding_y: int = 8,  # y padding around the window
    icon: Union[str, None] = None,  # window icon, specify filename (Experimental)
    show_scrollbar: bool = False,  # show scrollbar (Experimental)
    **kw,
    ) 
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L82)

### Methods of Window



### Window.bind

[Window.bind] Bind element event and handler

### Window.cancel_close

Cancel the close event.

### Window.close

Close the window.

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

### Window.focus

Focus the window.

### Window.focus_element

Focus the element.

### Window.get_center_location

Get center location.

### Window.get_element_by_key

Get an element by its key.

### Window.get_elements_by_type

Get elements by type.

### Window.get_location

Get window location.

### Window.get_screen_size

Get the screen size.

### Window.get_size

Get the window size.

### Window.get_values

Get values from the window.

### Window.hide

Hide the window.

### Window.hide_titlebar

Hide the titlebar.

### Window.is_alive

Check if the window is alive.

### Window.is_running

Check if the window is running. (alias as is_alive)

### Window.keep_on_top

Set the window to keep on top.

### Window.maximize

Maximize the window. (`resizable` should be set to True)

### Window.minimize

Minimize the window.

### Window.move

Move the window. (same as set_location)

### Window.move_to_center

Move the window to the center of the screen.

### Window.normal

set normal window.

### Window.post_event

Post an event.

### Window.post_event_after

Post an event after msec.

### Window.read

Read events from the window.

### Window.refresh

Refresh window

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

### Window.send_to_back

Send the window to the back, and make it not keep on top.

### Window.set_alpha_channel

Set the alpha channel of the window.

### Window.set_grab_anywhere

Set grab anywhere

### Window.set_icon

Set the icon for the window.

### Window.set_location

Set window location.

### Window.set_size

Set the window size.

### Window.set_timeout

Set a timeout event.

### Window.set_title

Set the title of the window.

### Window.show

Show hidden window (hide -> show)

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

### Window.un_hide

Un hide the window.

### Window.update_idle_tasks

Update idle tasks.

# Functions of TkEasyGUI.widgets

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

## generate_element_id

Generate a unique id for a value element.

```py
def generate_element_id() -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L289)

## generate_element_style_key

Get a unique id for an element.

```py
def generate_element_style_key(element_type: str) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L259)

## get_current_theme

Get current theme

```py
def get_current_theme() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L220)

## get_font_list

Get font list

```py
def get_font_list() -> list[str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3977)

## get_image_tk

Get Image for tk

```py
def get_image_tk(
    source: Union[bytes, Union[str, None]] = None,
    filename: Union[str, None] = None,
    data: Union[bytes, None] = None,
    size: Union[tuple[int, int], None] = None,
    resize_type: ImageResizeType = ImageResizeType.FIT_BOTH,
    background_color: Union[str, None] = None, # color (example) "red" or "#FF0000"
    ) -> Union[tk.PhotoImage, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3891)

## get_root_window

Get root window.

```py
def get_root_window() -> tk.Tk:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L121)

## get_system_info



```py
def get_system_info():
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3983)

## get_tcl_version

Get tcl version

```py
def get_tcl_version() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3971)

## get_tk_version

Get tk version

```py
def get_tk_version() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3965)

## get_ttk_style

Get ttk style

```py
def get_ttk_style() -> ttk.Style:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L151)

## image_resize

Resize image

```py
def image_resize(
    img: PIL.Image,
    size: Union[tuple[int, int], None],
    resize_type: ImageResizeType = ImageResizeType.FIT_BOTH,
    background_color: Union[str, None] = None, # color (example) "red" or "#FF0000"
) -> PIL.Image:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3834)

## imagedata_to_bytes

Convert JPEG to PNG

```py
def imagedata_to_bytes(image_data: PIL.Image) -> bytes:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3938)

## imagefile_to_bytes

Read image file and convert to bytes

```py
def imagefile_to_bytes(filename: str) -> bytes:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3945)

## register_element_key

Register element key.

```py
def register_element_key(key: str) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L274)

## rgb

Convert RGB to Hex

```py
def rgb(r: int, g: int, b: int) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3827)

## time_checker_end

timer end

```py
def time_checker_end(start_time: datetime) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3957)

## time_checker_start

timer start

```py
def time_checker_start() -> datetime:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets.py#L3953)

