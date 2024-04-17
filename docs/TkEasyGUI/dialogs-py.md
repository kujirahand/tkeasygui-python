# Module TkEasyGUI.dialogs

TkEasyGUI dialogs

## Functions

### ask_ok_cancel

```python
def ask_ok_cancel(message: str, title: str="Question") -> bool
```

Display a message in a popup window with OK and Cancel buttons. Return True or False. (use Tkinter)

------

### ask_retry_cancel

```python
def ask_retry_cancel(message: str, title: str="Question") -> bool
```

Display a message in a popup window with Retry and Cancel buttons. Return True or False. (use Tkinter)

------

### ask_yes_no

```python
def ask_yes_no(message: str, title: str="Question") -> bool
```

Display a message in a popup window with Yes and No buttons. Return True or False. (use Tkinter)

------

### msgbox

```python
def msgbox(message: str, title: str="Message") -> None
```

show message in a popup window like VB

------

### popup

```python
def popup(message: str, title: str = "") -> str
```

Display a message in a popup window.

#### Example:
```py
eg.popup("I like an apple.", "Information")
```

------

### popup_auto_close

```python
def popup_auto_close(message: str, title: str="", auto_close_duration: int = 3, buttons: list[str] = ["OK", "Cancel"], timeout_key="-TIMEOUT-") -> str
```

Display a message in a popup window that closes automatically after a specified time.

------

### popup_buttons

```python
def popup_buttons(message: str, title: str = "Question", buttons: list[str] = ["OK", "Cancel"], 
    auto_close_duration: int = -1, timeout_key: str="-TIMEOUT-", non_blocking: bool = False) -> str
```

Popup window with user defined buttons. Return button's label.

#### Example:
```py
color = eg.popup_buttons(
    "Which color do you like?", 
    "Question",
    buttons=["red","yellow","green"])
print(color)
```

------

### popup_cancel

```python
def popup_cancel(message: str, title: str="") -> str
```

Display a message in a popup window with OK and Cancel buttons. Return "OK" or "Cancel".

------

### popup_color

```python
def popup_color(title: str="", default_color: Union[str, None]=None) -> (Union[str, None])
```

Popup a color selection dialog. Return the color selected.

------

### popup_error

```python
def popup_error(message: str, title: str="Error") -> None
```

Display a message in a popup window with an error icon.

------

### popup_get_date

```python
def popup_get_date(
    message: str = "",
    title: str = "",
    current_date: Union[datetime, None] = None,
    font: Union[tuple[str, int], None] = None
    ) -> Union[datetime, None]
```

Display a calendar in a popup window. Return the datetime entered or None.

------

### popup_get_file

```python
def popup_get_file(
    message: str="",
    title: Union[str, None] = None,
    initial_folder: str = "",
    save_as: bool = False, # show `save as` dialog
    multiple_files: bool = False, # can select multiple files
    file_types: tuple[tuple[str, str]] = (("All Files", "*.*"),),
    no_window: Union[bool, None] = None, # for compatibility
    **kw) -> Union[str, tuple[str], None]
```

Popup a file selection dialog. Return the file selected.

------

### popup_get_folder

```python
def popup_get_folder(
    message: str = "",
    title: Union[str, None] = None,
    default_path: str = "",
    no_window: Union[bool, None] = None, # for compatibility
    **kw
    ) -> Union[str, None]
```

Popup a folder selection dialog. Return the folder selected.

------

### popup_get_text

```python
def popup_get_text(message: str, title: str = "", default: str = "", font: eg.FontType=None) -> Union[str, None]
```

Display a message in a popup window with a text entry. Return the text entered.

------

### popup_info

```python
def popup_info(message: str, title: str="Warning") -> None
```

Display a message in a popup window with an warning icon.

------

### popup_input

```python
def popup_input(message: str, title: str = "", default: str = "", font: eg.FontType=None) -> Union[str, None]
```

Display a message in a popup window with a text entry. Return the text entered.

------

### popup_listbox

```python
def popup_listbox(
    items: list[str], # list of items
    message: str = "",
    title: str = "",
    size: tuple[int,int] = (20, 7),
    font: Union[FontType, None] = None,
    multiple:bool = False # multiple selection
    ) -> Union[str, None]
```

Display Listbox in a popup window

------

### popup_no_buttons

```python
def popup_no_buttons(message: str, title: str="") -> None
```

------

### popup_no_wait

```python
def popup_no_wait(message: str, title: str="", **kw) -> str
```

Display a message in a popup window without waiting.

------

### popup_non_blocking

```python
def popup_non_blocking(message: str, title: str="", auto_close_duration: int = -1) -> str
```

(TODO) Display a non blocking window

------

### popup_notify

```python
def popup_notify(message: str, title: str="") -> None
```

Popup a information

------

### popup_ok

```python
def popup_ok(message: str, title: str="") -> str
```

Display a message in a popup window.(Alias popup)

------

### popup_ok_cancel

```python
def popup_ok_cancel(message: str, title: str="") -> str
```

Display a message in a popup window with OK and Cancel buttons. Return "OK" or "Cancel".

------

### popup_scrolled

```python
def popup_scrolled(
    message: str,
    title: str = "",
    size: tuple[int,int] = [40, 5],
    readonly: bool = False,
    font: Union[FontType, None] = None
    ) -> Union[str, None]
```

Display a message in a popup window with a text entry. Return the text entered.

------

### popup_warning

```python
def popup_warning(message: str, title: str="Warning") -> None
```

Display a message in a popup window with an warning icon.

------

### popup_yes_no

```python
def popup_yes_no(message: str, title: str = "Question", yes_label: str="Yes", no_label: str="No") -> str
```

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

------

### popup_yes_no_cancel

```python
def popup_yes_no_cancel(message: str, title: str = "Question") -> str
```

Display a message in a popup window with Yes and No buttons. Return "Yes" or "No" or "Cancel".

------

### send_notification_mac

```python
def send_notification_mac(message: str, title: str="")
```

"Send Notification on mac

------

### send_notification_win

```python
def send_notification_win(message: str, title: str="")
```

"Send Notification on win

------

### show_info

```python
def show_info(message: str, title: str="Information") -> None
```

show message in a popup window

------

### show_message

```python
def show_message(message: str, title: str="Information") -> None
```

show message in a popup window