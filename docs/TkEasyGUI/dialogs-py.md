# Module TkEasyGUI.dialogs

TkEasyGUI dialogs.

---------------------------

- [Functions](#functions-of-tkeasyguidialogs)

# Functions of TkEasyGUI.dialogs

- [ask_ok_cancel](#ask_ok_cancel)
- [ask_retry_cancel](#ask_retry_cancel)
- [ask_yes_no](#ask_yes_no)
- [cast](#cast)
- [confirm](#confirm)
- [copy_to_clipboard](#copy_to_clipboard)
- [get_root_window](#get_root_window)
- [input](#input)
- [input_number](#input_number)
- [is_mac](#is_mac)
- [is_win](#is_win)
- [msgbox](#msgbox)
- [popup](#popup)
- [popup_auto_close](#popup_auto_close)
- [popup_buttons](#popup_buttons)
- [popup_cancel](#popup_cancel)
- [popup_color](#popup_color)
- [popup_error](#popup_error)
- [popup_get_date](#popup_get_date)
- [popup_get_file](#popup_get_file)
- [popup_get_folder](#popup_get_folder)
- [popup_get_form](#popup_get_form)
- [popup_get_text](#popup_get_text)
- [popup_image](#popup_image)
- [popup_info](#popup_info)
- [popup_input](#popup_input)
- [popup_listbox](#popup_listbox)
- [popup_memo](#popup_memo)
- [popup_no_buttons](#popup_no_buttons)
- [popup_no_wait](#popup_no_wait)
- [popup_non_blocking](#popup_non_blocking)
- [popup_notify](#popup_notify)
- [popup_ok](#popup_ok)
- [popup_ok_cancel](#popup_ok_cancel)
- [popup_scrolled](#popup_scrolled)
- [popup_set_options](#popup_set_options)
- [popup_warning](#popup_warning)
- [popup_yes_no](#popup_yes_no)
- [popup_yes_no_cancel](#popup_yes_no_cancel)
- [print](#print)
- [send_notification_mac](#send_notification_mac)
- [send_notification_win](#send_notification_win)
- [show_info](#show_info)
- [show_message](#show_message)

## ask_ok_cancel

Display a message in a popup window with OK and Cancel buttons. Return True or False. (use Tkinter)

```py
def ask_ok_cancel(message: str, title: str = "Question") -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1439)

## ask_retry_cancel

Display a message in a popup window with Retry and Cancel buttons. Return True or False. (use Tkinter)

```py
def ask_retry_cancel(message: str, title: str = "Question") -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1444)

## ask_yes_no

Display a message in a popup window with Yes and No buttons. Return True or False. (use Tkinter)

```py
def ask_yes_no(message: str, title: str = "Question") -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1434)

## cast

Cast a value to a type.

    This returns the value unchanged.  To the type checker this
    signals that the return value has the designated type, but at
    runtime we intentionally don't check anything (we want this
    to be as fast as possible).

```py
def cast(typ, val):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/Users/kujirahand/.pyenv/versions/3.11.12/lib/python3.11/typing.py#L2287)

## confirm

Display a message in a popup window with Yes and No buttons. Return True or False.

```py
def confirm(question: str, title: Union[str, None] = None) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1503)

## copy_to_clipboard

Copy text to clipboard

```py
def copy_to_clipboard(text):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L74)

## get_root_window

Get root window.

```py
def get_root_window() -> tk.Tk:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L192)

## input

Display a message in a popup window with a text entry. Return the text entered.

```py
def input(
    message: str,
    title: Union[str, None] = None,
    default: str = "",
    only_number: bool = False,
    window_icon: Optional[str] = None,  # window icon, specify filename
) -> Union[str, float, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1470)

## input_number

Display a message in a popup window with a number entry. Return the text entered.

```py
def input_number(
    message: str,
    title: Union[str, None] = None,
    default: str = "",
    window_icon: Optional[str] = None,  # window icon, specify filename
) -> Union[float, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1490)

## is_mac

Platform : is mac?

```py
def is_mac() -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L92)

## is_win

Platform : is Windows?

```py
def is_win() -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L97)

## msgbox

Show message in a popup window like VB

```py
def msgbox(message: str, title: Union[str, None] = None) -> None:  # message
    """Show message in a popup window like VB"""
    title = title if title is not None else le.get_text("Information")
    messagebox.showinfo(title, message)
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1461)

## popup

Display a message in a popup window.

#### Example:
```py
eg.popup("I like an apple.", "Information")
```

```py
def popup(
    message: str,
    title: str = "",
    size: Union[tuple[int, int], None] = None,
    icon: str = "",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message: bool = True,
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L177)

## popup_auto_close

Display a message in a popup window that closes automatically after a specified time.

```py
def popup_auto_close(
    message: str,
    title: str = "",
    auto_close_duration: int = 3, # auto close duration (sec)
    buttons: list[str] = ["OK", "Cancel"],
    timeout_key="-TIMEOUT-",
    size: Union[tuple[int, int], None] = None,
    icon: str = "information",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message: bool = True,
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L254)

## popup_buttons

Popup window with user defined buttons. Return button's label.

#### Example:
```py
color = eg.popup_buttons(
    "Which color do you like?",
    "Question",
    buttons=["red","yellow","green"])
print(color)
```

```py
def popup_buttons(
    message: str,
    title: Union[str, None] = None,
    buttons: list[str] = ["OK", "Cancel"],
    auto_close_duration: int = -1,  # auto close duration (sec)
    timeout_key: str = "-TIMEOUT-",  # if auto_close_duration > 0, return this key
    non_blocking: bool = False,
    default: str = "",
    size: Union[tuple[int, int], None] = None,
    icon: str = "",  # filename or icon name(information/info, warning, error, question/?)
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message: bool = True, # show copy message in popup menu
    use_ttk_buttons: bool = POPUP_TTK_BUTTONS,  # use ttk buttons
    auto_locale: bool = True,  # auto locale
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L69)

## popup_cancel

Display a message in a popup window with OK and Cancel buttons. Return "Cancel" or eg.WINDOW_CLOSED.

```py
def popup_cancel(
    message: str,
    title: str = "",
    size: Union[tuple[int, int], None] = None,
    icon: str = "information",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message: bool = True,
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L459)

## popup_color

Popup a color selection dialog. Return the color selected.

format: "html", "rgb", "tuple"

```py
def popup_color(
    title: str = "",
    default_color: Union[str, None] = None,
    format: ColorFormatType = "html",
) -> Union[str, tuple[int, int, int], None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1287)

## popup_error

Display a message in a popup window with an error icon.

```py
def popup_error(
    message: str,
    title: Union[str, None] = None,
    size: Union[tuple[int, int], None] = None,
    icon: str = "error",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message: bool = True,
    use_tk_dialog: bool = False,
) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L573)

## popup_get_date

Display a calendar in a popup window. Return the datetime entered or None.

```py
def popup_get_date(
    message: str = "",
    title: Union[str, None] = None,
    current_date: Union[datetime, None] = None,
    font: Union[tuple[str, int], None] = None,
    ok_label: Union[str, None] = None,
    cancel_label: Union[str, None] = None,
    date_format: Union[str, None] = None,
    close_when_date_chosen: bool = False,
    sunday_first: bool = False,  # Sunday is the first day of the week
    window_icon: Optional[str] = None,  # window icon, specify filename
) -> Union[datetime, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L812)

## popup_get_file

Popup a file selection dialog. Return the file selected.

```py
def popup_get_file(
    message: str = "",
    title: Union[str, None] = None,
    initial_folder: Union[str, None] = None,
    save_as: bool = False,  # show `save as` dialog
    multiple_files: bool = False,  # can select multiple files
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    default_extension: Union[str, None] = None,
    no_window: Union[bool, None] = None,  # for compatibility
    **kw,
) -> Union[str, tuple[str], None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L659)

## popup_get_folder

Popup a folder selection dialog. Return the folder selected.

```py
def popup_get_folder(
    message: str = "",
    title: Union[str, None] = None,
    default_path: Union[str, None] = None,
    no_window: Union[bool, None] = None,  # for compatibility
    **kw,
) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L714)

## popup_get_form

Displays a form that allows multiple items to be entered.

By specifying the labels and input types for each item, the form is automatically generated and displayed in a dialog.
When the user enters the items and clicks [OK], it returns `{label: value}`. If the user clicks [Cancel], it returns `None`.

### Arguments:
- `form_items` (list): A list of form items. Each item can be:
  - A string (label only, default type is "text").
  - A tuple of `(label, default_value)` (default type is "text").
  - A tuple of `(label, default_value, type)` where `type` can be:
    - `"text"`: Single-line text input.
    - `"number"`: Numeric input.
    - `"password"`: Password input (masked).
    - `"combo"`: Dropdown menu.
    - `"list"`: List selection.
    - `"date"`: Date picker.
    - `"file"`: File selection.
    - `"files"`: Multiple file selection.
    - `"folder"`: Folder selection.
    - `"color"`: Color picker.

- `title` (str): The title of the form window. Default is "Form".
- `size` (tuple[int, int] | None): The size of the form window. Default is `None`.

### Returns:
- `dict[str, Any] | None`: A dictionary with `{label: value}` pairs if the user clicks [OK]. Returns `None` if the user clicks [Cancel].

### Examples:
#### Simple Example:
```python
import TkEasyGUI as eg
form = eg.popup_get_form(["Name", "Hobbies"])
if form:
    name = form["Name"]
    hobbies = form["Hobbies"]
    eg.print(f"name={name}, hobbies={hobbies}")
```

```py
def popup_get_form(
    form_items: list[
    Union[str, tuple[str, Any], tuple[str, Any, str]]
    ],  # list of form items(label[,selection or default][,type])
    title: str = "Form",  # window title
    size: Union[tuple[int, int], None] = None,
    window_icon: Optional[str] = None,  # window icon, specify filename
) -> Union[dict[str, Any], None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1023)

## popup_get_text

Display a message in a popup window with a text entry. Return the text entered.

```py
def popup_get_text(
    message: str,
    title: Union[str, None] = None,
    default: Union[str, None] = None,
    default_text: Union[str, None] = None,  # same as default for compatibility
    font: Optional[FontType] = None,
    size: Union[tuple[int, int], None] = None,
    window_icon: Optional[str] = None,  # window icon, specify filename
) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L483)

## popup_image

Display an image in a popup window. Return the pushed Button("OK" or None).

```py
def popup_image(
    message: str,
    title: Union[str, None] = None,
    image_path: Union[str, None] = None,
    image_data: Union[bytes, None] = None,
    size: tuple[int, int] = (400, 300),
    ok_label: Union[str, None] = None,
    ok_value: str = "OK",
    cancel_label: Union[str, None] = None,
    cancel_value: Union[str, None] = None,
    font: Union[FontType, None] = None,
    window_icon: Optional[str] = None,  # window icon, specify filename
    auto_close_duration: int = -1,  # auto close duration in seconds
    timeout_key: str = "-TIMEOUT-",  # timeout key if auto_close_duration > 0
) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1371)

## popup_info

Display a message in a popup window with an warning icon.

```py
def popup_info(
    message: str,
    title: Union[str, None] = None,
    size: Union[tuple[int, int], None] = None,
    icon: str = "information",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message: bool = True,
    use_tk_dialog: bool = False,
) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L631)

## popup_input

Display a message in a popup window with a text entry. Return the text entered. if canceled, return cancel_value.

```py
def popup_input(
    message: str,
    title: Optional[str] = None,
    default: str = "",
    ok_label: Optional[str] = None,
    cancel_label: Optional[str] = None,
    cancel_value: Any = None,
    only_number: bool = False,
    font: Optional[FontType] = None,
    size: Union[tuple[int, int], None] = None,
    window_icon: Optional[str] = None,  # window icon, specify filename
) -> Union[str, float, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L512)

## popup_listbox

Display Listbox in a popup window

```py
def popup_listbox(
    values: list[str],  # list of items
    message: str = "",
    title: str = "",
    size: tuple[int, int] = (20, 7),
    font: Union[FontType, None] = None,
    default_value: Union[str, None] = None,  # default value
    multiple: bool = False,  # multiple selection
    resizable: bool = True,  # resizable
    window_icon: Optional[str] = None,  # window icon, specify filename
) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1310)

## popup_memo

Display a multiline message in a popup window. Return the text entered. if canceled, return cancel_value(default is None).

```py
def popup_memo(
    message: str,  # Text to enter in a multi-line text box
    title: Union[str, None] = None,  # Window title
    size: tuple[int, int] = (60, 8),  # Size of the text box
    readonly: bool = False,  # Read-only mode
    header: str = "",  # Label displayed above the text box
    resizable: bool = True,  # resizable
    window_icon: Optional[str] = None,  # window icon, specify filename
    ok_label: Union[str, None] = None,
    cancel_label: Union[str, None] = None,
    cancel_value: Union[str, None] = None,
    font: Union[FontType, None] = None,
) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L729)

## popup_no_buttons

Display a message in a popup window without buttons.

```py
def popup_no_buttons(
    message: str,
    title: str = "",
    icon: str = "",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    size: Union[tuple[int, int], None] = None,
    can_copy_message: bool = True,
) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L232)

## popup_no_wait

Display a message in a popup window without waiting.

```py
def popup_no_wait(
    message: str,
    title: str = "",
    size: Union[tuple[int, int], None] = None,
    icon: str = "information",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    **kw,
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L281)

## popup_non_blocking

(TODO) Display a non blocking window

```py
def popup_non_blocking(
    message: str,
    title: str = "",
    auto_close_duration: int = -1,
    size: Union[tuple[int, int], None] = None,
    icon: str = "",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message=True,
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L207)

## popup_notify

Popup a information

```py
def popup_notify(message: str, title: str = "") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1189)

## popup_ok

Display a message in a popup window.(Alias popup)

```py
def popup_ok(
    message: str,
    title: str = "",
    size: Union[tuple[int, int], None] = None,
    icon: str = "information",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message: bool = True,
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L303)

## popup_ok_cancel

Display a message in a popup window with OK and Cancel buttons. Return "OK" or "Cancel" or eg.WINDOW_CLOSED.

```py
def popup_ok_cancel(
    message: str,
    title: Union[str, None] = None,
    ok_label: Union[str, None] = None,
    cancel_label: Union[str, None] = None,
    ok_value: str = "OK",
    cancel_value: str = "Cancel",
    size: Union[tuple[int, int], None] = None,
    icon: str = "?",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message: bool = True,
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L325)

## popup_scrolled

Display a multiline message in a popup window. Return the text entered. if canceled, return cancel_value(default is None).

#### Example:
```py
import TkEasyGUI as eg
text = eg.popup_scrolled("This is a long text.", "Information")
eg.print(text)
```

```py
def popup_scrolled(
    message: str,  # Text to enter in a multi-line text box
    title: Union[str, None] = None,  # Window title
    size: tuple[int, int] = (40, 5),  # Size of the text box
    readonly: bool = False,  # Read-only mode
    header: str = "",  # Label displayed above the text box
    resizable: bool = True,  # resizable
    window_icon: Optional[str] = None,  # window icon, specify filename
    ok_label: Union[str, None] = None,
    cancel_label: Union[str, None] = None,
    cancel_value: Union[str, None] = None,
    font: Union[FontType, None] = None,
) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L758)

## popup_set_options

Set auto screenshot values.

```py
def popup_set_options(
    auto_screenshot: bool = POPUP_AUTO_SCREENSHOT,
    auto_screenshot_duration: int = POPUP_AUTO_SCREENSHOT_DURATION,  # auto close duration (msec)
    auto_screenshot_filename: str = POPUP_AUTO_SCREENSHOT_FILENAME,
    ok_button_width: int = POPUP_OK_BUTTON_WIDTH,
    cancel_button_width: int = POPUP_CANCEL_BUTTON_WIDTH,
    ttk_buttons: bool = POPUP_TTK_BUTTONS,  # use ttk buttons
) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L44)

## popup_warning

Display a message in a popup window with an warning icon.

```py
def popup_warning(
    message: str,
    title: Union[str, None] = None,
    size: Union[tuple[int, int], None] = None,
    icon: str = "warning",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message: bool = True,
    use_tk_dialog: bool = False,
) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L603)

## popup_yes_no

Display a message in a popup window with Yes and No buttons. Return "Yes" or "No" (or eg.WINDOW_CLOSED).

@see [tests/localize_test.py](https://github.com/kujirahand/tkeasygui-python/blob/main/tests/localize_test.py)
#### Example - simple:
Ask user question, [Yes] or [No] buttons.
```py
ans = eg.popup_yes_no("Do you like Sushi?", "Question")
print(ans) # "Yes" or "No"
```
#### Eample - custom label:
Ask user question in special button
```py
ans = eg.popup_yes_no("Do you eat Sushi?", yes_label="EAT", no_label="no")
print(ans) # "Yes" or "No"
```
#### Example - custom return value:
ans = eg.popup_yes_no("Can you speak Japanese?", yes_value="can", no_value="no")
print(ans) # "can" or "no"

```py
def popup_yes_no(
    message: str,  # question message
    title: Union[str, None] = None,  # window title
    yes_label: Union[str, None] = None,  # label for yes button
    no_label: Union[str, None] = None,  # label for no button
    yes_value: str = "Yes",  # return value for yes
    no_value: str = "No",  # return value for no
    size: Union[tuple[int, int], None] = None,
    icon: str = "?",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message: bool = True,
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L360)

## popup_yes_no_cancel

Display a message in a popup window with Yes and No buttons. Return "Yes" or "No" or "Cancel".

```py
def popup_yes_no_cancel(
    message: str,
    title: Union[str, None] = None,
    yes_label: Union[str, None] = None,
    no_label: Union[str, None] = None,
    cancel_label: Union[str, None] = None,
    yes_value: str = "Yes",
    no_value: str = "No",
    cancel_value: str = "Cancel",
    size: Union[tuple[int, int], None] = None,
    icon: str = "?",
    icon_size: tuple[int, int] = (48, 48),
    window_icon: Optional[str] = None,  # window icon, specify filename
    can_copy_message: bool = True,
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L416)

## print

Print message to popup window.(call default print function if no_window is True)

```py
def print(*args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1481)

## send_notification_mac

Send Notification on mac

```py
def send_notification_mac(message: str, title: str = "") -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1200)

## send_notification_win

Send Notification on Windows using PowerShell

```py
def send_notification_win(message: str, title: str = "") -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1223)

## show_info

Show message in a popup window

```py
def show_info(message: str, title: Union[str, None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1455)

## show_message

Show message in a popup window

```py
def show_message(message: str, title: Union[str, None] = None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L1449)

