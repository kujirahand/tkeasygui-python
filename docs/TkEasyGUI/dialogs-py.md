# Module TkEasyGUI.dialogs

TkEasyGUI dialogs

---------------------------

- [Functions](#functions-of-tkeasyguidialogs)

# Functions of TkEasyGUI.dialogs

- [ask_ok_cancel](#ask_ok_cancel)
- [ask_retry_cancel](#ask_retry_cancel)
- [ask_yes_no](#ask_yes_no)
- [confirm](#confirm)
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
def ask_ok_cancel(message: str, title: str="Question") -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L825)

## ask_retry_cancel

Display a message in a popup window with Retry and Cancel buttons. Return True or False. (use Tkinter)

```py
def ask_retry_cancel(message: str, title: str="Question") -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L829)

## ask_yes_no

Display a message in a popup window with Yes and No buttons. Return True or False. (use Tkinter)

```py
def ask_yes_no(message: str, title: str="Question") -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L821)

## confirm

Display a message in a popup window with Yes and No buttons. Return True or False.

```py
def confirm(
    question: str,
    title: Union[str,None] = None
    ) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L885)

## get_root_window

Get root window.

```py
def get_root_window() -> tk.Tk:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L116)

## input

Display a message in a popup window with a text entry. Return the text entered.

```py
def input(
    message: str,
    title: Union[str,None] = None,
    default: str = "",
    only_number: bool = False
    ) -> Union[str, float]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L860)

## input_number

Display a message in a popup window with a number entry. Return the text entered.

```py
def input_number(
    message: str,
    title: Union[str,None] = None,
    default: str = ""
    ) -> float:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L877)

## is_mac

platform : is mac?

```py
def is_mac() -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L53)

## is_win

platform : is Windows?

```py
def is_win() -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L57)

## msgbox

show message in a popup window like VB

```py
def msgbox(
    message: str, # message
    title: Union[str,None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L849)

## popup

Display a message in a popup window.

#### Example:
```py
eg.popup("I like an apple.", "Information")
```

```py
def popup(message: str, title: str = "") -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L80)

## popup_auto_close

Display a message in a popup window that closes automatically after a specified time.

```py
def popup_auto_close(message: str, title: str="", auto_close_duration: int = 3, buttons: list[str] = ["OK", "Cancel"], timeout_key="-TIMEOUT-") -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L100)

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
    title: Union[str,None] = None,
    buttons: list[str] = ["OK", "Cancel"],
    auto_close_duration: int = -1, # auto close duration (msec)
    timeout_key: str="-TIMEOUT-", # timeout key
    non_blocking: bool = False
    ) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L29)

## popup_cancel

Display a message in a popup window with OK and Cancel buttons. Return "Cancel" or eg.WINDOW_CLOSED.

```py
def popup_cancel(message: str, title: str="") -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L200)

## popup_color

Popup a color selection dialog. Return the color selected.

```py
def popup_color(title: str="", default_color: Union[str, None]=None) -> (Union[str, None]):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L736)

## popup_error

Display a message in a popup window with an error icon.

```py
def popup_error(message: str, title: Union[str,None]=None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L257)

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
    sunday_first: bool = False, # Sunday is the first day of the week
    ) -> Union[datetime, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L396)

## popup_get_file

Popup a file selection dialog. Return the file selected.

```py
def popup_get_file(
    message: str="",
    title: Union[str, None] = None,
    initial_folder: Union[str, None] = None,
    save_as: bool = False, # show `save as` dialog
    multiple_files: bool = False, # can select multiple files
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    default_extension: Union[str, None] = None,
    no_window: Union[bool, None] = None, # for compatibility
    **kw) -> Union[str, tuple[str], None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L277)

## popup_get_folder

Popup a folder selection dialog. Return the folder selected.

```py
def popup_get_folder(
    message: str = "",
    title: Union[str, None] = None,
    default_path: Union[str, None] = None,
    no_window: Union[bool, None] = None, # for compatibility
    **kw
    ) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L328)

## popup_get_form

Displays a form that allows multiple items to be entered.
By specifying the labels and input types for each item, the form is automatically generated and displayed in a dialog.
When the user enters the items and clicks [OK], it returns `{label: value}`. If the user clicks [Cancel], it returns `None`.

The `form_items` argument can specify input fields simply as `[label1, label2, label3, ...]`.
Alternatively, you can specify labels, types, and default values as `[(label1, type1, default1), (label2, type2, default2), ...]`.
The following values can be specified for the type: `text`, `number`, `password`, `combo`, `list`, `date`, `file`, `files`, `folder`, `color`.

@see [tests/popup_get_form.py](/tests/popup_get_form.py)

```py
def popup_get_form(
    form_items: list[Union[str, tuple[str, str], tuple[str, str, Any]]], # list of form items(label, type [, default])
    title: str = "Form" # window title
) -> Union[dict[str, Any], None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L597)

## popup_get_text

Display a message in a popup window with a text entry. Return the text entered.

```py
def popup_get_text(
    message: str,
    title: Union[str,None] = None,
    default: Union[str, None] = None,
    default_text: Union[str, None] = None, # same as default for compatibility
    font: FontType=None) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L206)

## popup_image

Display an image in a popup window. Return the text entered.

```py
def popup_image(
    message: str,
    title: Union[str,None] = None,
    image_path: Union[str,None] = None,
    image_data: Union[bytes,None] = None,
    size: tuple[int,int] = (400, 300),
    ok_label: Union[str, None] = None,
    ok_value: str = "OK",
    cancel_label: Union[str, None] = None,
    cancel_value: str = "Cancel",
    font: Union[FontType, None] = None,
    ) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L782)

## popup_info

Display a message in a popup window with an warning icon.

```py
def popup_info(message: str, title: Union[str,None]=None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L271)

## popup_input

Display a message in a popup window with a text entry. Return the text entered. if canceled, return cancel_value.

```py
def popup_input(
    message: str,
    title: Union[str,None] = None,
    default: str = "",
    ok_label: Union[str, None] = None,
    cancel_label: Union[str, None] = None,
    cancel_value: Any = None,
    only_number: bool = False,
    font: FontType=None) -> Union[str, float, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L218)

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
) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L743)

## popup_memo

Display a multiline message in a popup window. Return the text entered. if canceled, return cancel_value.

```py
def popup_memo(
    message: str,
    title: Union[str, None] = None,
    size: tuple[int,int] = [60, 8],
    readonly: bool = False,
    ok_label: Union[str, None] = None,
    cancel_label: Union[str, None] = None,
    cancel_value: Union[str,None] = None,
    font: Union[FontType, None] = None
    ) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L342)

## popup_no_buttons

Display a message in a popup window without buttons.

```py
def popup_no_buttons(message: str, title: str="") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L96)

## popup_no_wait

Display a message in a popup window without waiting.

```py
def popup_no_wait(message: str, title: str="", **kw) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L104)

## popup_non_blocking

(TODO) Display a non blocking window

```py
def popup_non_blocking(message: str, title: str="", auto_close_duration: int = -1) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L92)

## popup_notify

Popup a information

```py
def popup_notify(message: str, title: str="") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L696)

## popup_ok

Display a message in a popup window.(Alias popup)

```py
def popup_ok(message: str, title: str="") -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L108)

## popup_ok_cancel

Display a message in a popup window with OK and Cancel buttons. Return "OK" or "Cancel" or eg.WINDOW_CLOSED.

```py
def popup_ok_cancel(
    message: str,
    title: Union[str,None] = None,
    ok_label: Union[str, None] = None,
    cancel_label: Union[str, None] = None,
    ok_value: str = "OK",
    cancel_value: str = "Cancel",
    ) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L112)

## popup_scrolled

Display a multiline message in a popup window. Return the text entered. if canceled, return cancel_value.
#### Example:
```py
import TkEasyGUI as eg
text = eg.popup_scrolled("This is a long text.", "Information")
eg.print(text)
```

```py
def popup_scrolled(
    message: str,
    title: tuple[str, None] = None,
    size: tuple[int,int] = [40, 5],
    readonly: bool = False,
    ok_label: Union[str, None] = None,
    cancel_label: Union[str, None] = None,
    cancel_value: Union[str,None] = None,
    font: Union[FontType, None] = None
    ) -> Union[str, None]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L355)

## popup_warning

Display a message in a popup window with an warning icon.

```py
def popup_warning(message: str, title: Union[str,None]=None) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L265)

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
    message: str, # question message
    title: Union[str,None] = None, # window title
    yes_label: Union[str,None]=None, # label for yes button
    no_label: Union[str,None]=None, # label for no button
    yes_value: str = "Yes", # return value for yes
    no_value: str = "No" # return value for no
    ) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L132)

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
    cancel_value: str = "Cancel"
    ) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L172)

## print

Print message to popup window.(call default print function if no_window is True)

```py
def print(*args, **kw) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L869)

## send_notification_mac

"Send Notification on mac

```py
def send_notification_mac(message: str, title: str=""):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L705)

## send_notification_win

"Send Notification on win

```py
def send_notification_win(message: str, title: str=""):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L712)

## show_info

show message in a popup window

```py
def show_info(
    message: str,
    title: Union[str,None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L841)

## show_message

show message in a popup window

```py
def show_message(
    message: str,
    title: Union[str,None] = None
    ) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/dialogs.py#L833)

