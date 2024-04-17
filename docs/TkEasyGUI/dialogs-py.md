# Module TkEasyGUI.dialogs

TkEasyGUI dialogs

---------------------------

- [Functions](#functions-of-tkeasygui.dialogs)

# Functions of TkEasyGUI.dialogs

- [ask_ok_cancel](#ask_ok_cancel)
- [ask_retry_cancel](#ask_retry_cancel)
- [ask_yes_no](#ask_yes_no)
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
- [popup_get_text](#popup_get_text)
- [popup_info](#popup_info)
- [popup_input](#popup_input)
- [popup_listbox](#popup_listbox)
- [popup_no_buttons](#popup_no_buttons)
- [popup_no_wait](#popup_no_wait)
- [popup_non_blocking](#popup_non_blocking)
- [popup_notify](#popup_notify)
- [popup_ok](#popup_ok)
- [popup_ok_cancel](#popup_ok_cancel)
- [popup_scrolled](#popup_scrolled)
- [popup_warning](#popup_warning)
- [popup_yes_no](#popup_yes_no)
- [popup_yes_no_cancel](#popup_yes_no_cancel)
- [send_notification_mac](#send_notification_mac)
- [send_notification_win](#send_notification_win)
- [show_info](#show_info)
- [show_message](#show_message)

## ask_ok_cancel

Display a message in a popup window with OK and Cancel buttons. Return True or False. (use Tkinter)

```py
def ask_ok_cancel(message: str, title: str="Question") -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L415)

## ask_retry_cancel

Display a message in a popup window with Retry and Cancel buttons. Return True or False. (use Tkinter)

```py
def ask_retry_cancel(message: str, title: str="Question") -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L419)

## ask_yes_no

Display a message in a popup window with Yes and No buttons. Return True or False. (use Tkinter)

```py
def ask_yes_no(message: str, title: str="Question") -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L411)

## msgbox

show message in a popup window like VB

```py
def msgbox(
    message: str, # message
    title: str="Message" # dialog title
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L434)

## popup

Display a message in a popup window.

#### Example:
```py
eg.popup("I like an apple.", "Information")
```

```py
def popup(message: str, title: str = "") -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L57)

## popup_auto_close

Display a message in a popup window that closes automatically after a specified time.

```py
def popup_auto_close(message: str, title: str="", auto_close_duration: int = 3, buttons: list[str] = ["OK", "Cancel"], timeout_key="-TIMEOUT-") -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L76)

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
def popup_buttons(message: str, title: str = "Question", buttons: list[str] = ["OK", "Cancel"],
    auto_close_duration: int = -1, timeout_key: str="-TIMEOUT-", non_blocking: bool = False) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L19)

## popup_cancel

Display a message in a popup window with OK and Cancel buttons. Return "OK" or "Cancel".

```py
def popup_cancel(message: str, title: str="") -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L115)

## popup_color

Popup a color selection dialog. Return the color selected.

```py
def popup_color(title: str="", default_color: Union[str, None]=None) -> (Union[str, None]):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L370)

## popup_error

Display a message in a popup window with an error icon.

```py
def popup_error(message: str, title: str="Error") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L142)

## popup_get_date

Display a calendar in a popup window. Return the datetime entered or None.

```py
def popup_get_date(
    message: str = "",
    title: str = "",
    current_date: Union[datetime, None] = None,
    font: Union[tuple[str, int], None] = None
    ) -> Union[datetime, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L217)

## popup_get_file

Popup a file selection dialog. Return the file selected.

```py
def popup_get_file(
    message: str="",
    title: Union[str, None] = None,
    initial_folder: str = "",
    save_as: bool = False, # show `save as` dialog
    multiple_files: bool = False, # can select multiple files
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    no_window: Union[bool, None] = None, # for compatibility
    **kw) -> Union[str, tuple[str], None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L155)

## popup_get_folder

Popup a folder selection dialog. Return the folder selected.

```py
def popup_get_folder(
    message: str = "",
    title: Union[str, None] = None,
    default_path: str = "",
    no_window: Union[bool, None] = None, # for compatibility
    **kw
    ) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L182)

## popup_get_text

Display a message in a popup window with a text entry. Return the text entered.

```py
def popup_get_text(message: str, title: str = "", default: str = "", font: eg.FontType=None) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L119)

## popup_info

Display a message in a popup window with an warning icon.

```py
def popup_info(message: str, title: str="Warning") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L151)

## popup_input

Display a message in a popup window with a text entry. Return the text entered.

```py
def popup_input(message: str, title: str = "", default: str = "", font: eg.FontType=None) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L124)

## popup_listbox

Display Listbox in a popup window

```py
def popup_listbox(
    items: list[str], # list of items
    message: str = "",
    title: str = "",
    size: tuple[int,int] = (20, 7),
    font: Union[FontType, None] = None,
    multiple:bool = False # multiple selection
    ) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L377)

## popup_no_buttons



```py
def popup_no_buttons(message: str, title: str="") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L73)

## popup_no_wait

Display a message in a popup window without waiting.

```py
def popup_no_wait(message: str, title: str="", **kw) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L80)

## popup_non_blocking

(TODO) Display a non blocking window

```py
def popup_non_blocking(message: str, title: str="", auto_close_duration: int = -1) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L69)

## popup_notify

Popup a information

```py
def popup_notify(message: str, title: str="") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L331)

## popup_ok

Display a message in a popup window.(Alias popup)

```py
def popup_ok(message: str, title: str="") -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L84)

## popup_ok_cancel

Display a message in a popup window with OK and Cancel buttons. Return "OK" or "Cancel".

```py
def popup_ok_cancel(message: str, title: str="") -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L88)

## popup_scrolled

Display a message in a popup window with a text entry. Return the text entered.

```py
def popup_scrolled(
    message: str,
    title: str = "",
    size: tuple[int,int] = [40, 5],
    readonly: bool = False,
    font: Union[FontType, None] = None
    ) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L194)

## popup_warning

Display a message in a popup window with an warning icon.

```py
def popup_warning(message: str, title: str="Warning") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L147)

## popup_yes_no

Display a message in a popup window with Yes and No buttons. Return "Yes" or "No".

#### Example:
Ask user question, [Yes] or [No]
```py
a = eg.popup_yes_no("Do you like Sushi?", "Question")
print(a) # "Yes" or "No"
```
Ask user question in Japanes [はい] or [いいえ]
```py
ja_a = eg.popup_yes_no("寿司は好き?", "質問", yes_label="はい", no_label="いいえ")
print(ja_a) # "はい" or "いいえ"
```

```py
def popup_yes_no(message: str, title: str = "Question", yes_label: str="Yes", no_label: str="No") -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L92)

## popup_yes_no_cancel

Display a message in a popup window with Yes and No buttons. Return "Yes" or "No" or "Cancel".

```py
def popup_yes_no_cancel(message: str, title: str = "Question") -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L111)

## send_notification_mac

"Send Notification on mac

```py
def send_notification_mac(message: str, title: str=""):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L340)

## send_notification_win

"Send Notification on win

```py
def send_notification_win(message: str, title: str=""):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L347)

## show_info

show message in a popup window

```py
def show_info(message: str, title: str="Information") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L430)

## show_message

show message in a popup window

```py
def show_message(
    message: str,
    title: str="Information"
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L423)

