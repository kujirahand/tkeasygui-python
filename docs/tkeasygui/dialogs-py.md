# Module tkeasygui.dialogs

## Functions

### ask_ok_cancel {: #ask_ok_cancel }

```python
def ask_ok_cancel(message: str, title: str="Question") -> bool
```

Display a message in a popup window with OK and Cancel buttons. Return True or False.

------

### ask_retry_cancel {: #ask_retry_cancel }

```python
def ask_retry_cancel(message: str, title: str="Question") -> bool
```

Display a message in a popup window with Retry and Cancel buttons. Return True or False.

------

### ask_yes_no {: #ask_yes_no }

```python
def ask_yes_no(message: str, title: str="Question") -> bool
```

Display a message in a popup window with Yes and No buttons. Return True or False.

------

### popup {: #popup }

```python
def popup(message: str, title: str = "") -> None
```

Display a message in a popup window.

------

### popup_error {: #popup_error }

```python
def popup_error(message: str, title: str="Error") -> None
```

Display a message in a popup window with an error icon.

------

### popup_get_file {: #popup_get_file }

```python
def popup_get_file(title: str="", initial_folder: str="", save_as: bool=False, multiple_files: bool=False, file_types: tuple[tuple[str, str]]=(("All Files", "*.*"),), **kw) -> (str|tuple[str]|None)
```

Popup a file selection dialog. Return the file selected.

------

### popup_get_folder {: #popup_get_folder }

```python
def popup_get_folder(title: str="", default_path: str="", **kw) -> (str|None)
```

Popup a folder selection dialog. Return the folder selected.

------

### popup_get_text {: #popup_get_text }

```python
def popup_get_text(message: str, title: str = "", default: str = "") -> (str|None)
```

Display a message in a popup window with a text entry. Return the text entered.

------

### popup_ok {: #popup_ok }

```python
def popup_ok(message: str, title: str="") -> None
```

Display a message in a popup window.

------

### popup_yes_no {: #popup_yes_no }

```python
def popup_yes_no(message: str, title: str = "Question") -> str
```

Display a message in a popup window with Yes and No buttons. Return "Yes" or "No".

------

### popup_yes_no_cancel {: #popup_yes_no_cancel }

```python
def popup_yes_no_cancel(message: str, title: str = "Question") -> str
```

Display a message in a popup window with Yes and No buttons. Return "Yes" or "No" or "Cancel".