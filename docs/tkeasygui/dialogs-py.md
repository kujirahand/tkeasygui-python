# Module tkeasygui.dialogs

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
def popup(message: str, title: str = "") -> None
```

Display a message in a popup window.

#### Example:
```py
eg.popup("I like an apple.", "Information")
```

------

### popup_buttons

```python
def popup_buttons(message: str, title: str = "Question", buttons: list[str] = ["OK", "Cancel"]) -> str
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

### popup_color

```python
def popup_color(title: str="", default_color: str|None=None) -> (str|None)
```

Popup a color selection dialog. Return the color selected.

------

### popup_error

```python
def popup_error(message: str, title: str="Error") -> None
```

Display a message in a popup window with an error icon.

------

### popup_get_file

```python
def popup_get_file(message: str="", title: str|None=None, initial_folder: str="", save_as: bool=False, multiple_files: bool=False, file_types: tuple[tuple[str, str]]=(("All Files", "*.*"),), no_window: bool|None=None, **kw) -> (str|tuple[str]|None)
```

Popup a file selection dialog. Return the file selected.

------

### popup_get_folder

```python
def popup_get_folder(message: str="", title: str|None=None, default_path: str="", no_window: bool|None=None, **kw) -> (str|None)
```

Popup a folder selection dialog. Return the folder selected.

------

### popup_get_text

```python
def popup_get_text(message: str, title: str = "", default: str = "") -> (str|None)
```

Display a message in a popup window with a text entry. Return the text entered.

------

### popup_input

```python
def popup_input(message: str, title: str = "", default: str = "") -> (str|None)
```

Display a message in a popup window with a text entry. Return the text entered.

------

### popup_notify

```python
def popup_notify(message: str, title: str="Notification") -> None
```

Popup a information

------

### popup_ok

```python
def popup_ok(message: str, title: str="") -> None
```

Display a message in a popup window.(Alias popup)

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