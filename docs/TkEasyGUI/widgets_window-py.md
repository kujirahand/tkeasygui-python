# Module TkEasyGUI.widgets_window

TkEasyGUI Window management functions.

---------------------------

- [Classes](#classes-of-tkeasyguiwidgets_window)
- [Functions](#functions-of-tkeasyguiwidgets_window)

# Classes of TkEasyGUI.widgets_window

## TkWindowManager

Manage tkinter root window.

```py
class TkWindowManager(self):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L34)

### Methods of TkWindowManager

- [destroy_root](#tkwindowmanagerdestroy_root)
- [generate_element_id](#tkwindowmanagergenerate_element_id)
- [generate_element_style_key](#tkwindowmanagergenerate_element_style_key)
- [get_root](#tkwindowmanagerget_root)
- [get_sg_compatibility](#tkwindowmanagerget_sg_compatibility)
- [get_theme](#tkwindowmanagerget_theme)
- [get_tk_version](#tkwindowmanagerget_tk_version)
- [get_tkk_style](#tkwindowmanagerget_tkk_style)
- [register_element_key](#tkwindowmanagerregister_element_key)
- [remove_element_key](#tkwindowmanagerremove_element_key)
- [set_sg_compatibility](#tkwindowmanagerset_sg_compatibility)
- [set_theme](#tkwindowmanagerset_theme)
- [set_tkk_style](#tkwindowmanagerset_tkk_style)

### TkWindowManager.destroy_root

Destroy root window.

```py
def destroy_root(self) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L75)

### TkWindowManager.generate_element_id

Generate a unique id for an element.

```py
def generate_element_id(self) -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L113)

### TkWindowManager.generate_element_style_key

Get a unique id for an element.

```py
def generate_element_style_key(self, element_type: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L118)

### TkWindowManager.get_root

Get root window.

```py
def get_root(self) -> tk.Tk:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L63)

### TkWindowManager.get_sg_compatibility

Get compatibility with PySimpleGUI

```py
def get_sg_compatibility(self) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L85)

### TkWindowManager.get_theme

Get current theme name

```py
def get_theme(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L109)

### TkWindowManager.get_tk_version

Get tkinter version.

```py
def get_tk_version(self) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L69)

### TkWindowManager.get_tkk_style

Get ttk style

```py
def get_tkk_style(self) -> ttk.Style:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L89)

### TkWindowManager.register_element_key

Register element key.

```py
def register_element_key(self, key: KeyType) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L133)

### TkWindowManager.remove_element_key

Remove element key.

```py
def remove_element_key(self, key: KeyType) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L140)

### TkWindowManager.set_sg_compatibility

Set compatibility with PySimpleGUI (Default=True)

```py
def set_sg_compatibility(self, flag: bool = True) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L81)

### TkWindowManager.set_theme

Set theme for ttk style

```py
def set_theme(self, name: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L101)

### TkWindowManager.set_tkk_style

Set ttk style

```py
def set_tkk_style(self, style: ttk.Style) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L95)

# Functions of TkEasyGUI.widgets_window

- [generate_element_id](#generate_element_id)
- [generate_element_style_key](#generate_element_style_key)
- [get_active_eg_window](#get_active_eg_window)
- [get_eg_window_count](#get_eg_window_count)
- [get_last_eg_window](#get_last_eg_window)
- [get_root_window](#get_root_window)
- [get_ttk_style](#get_ttk_style)
- [pop_easy_window](#pop_easy_window)
- [push_easy_window](#push_easy_window)
- [register_element_key](#register_element_key)
- [remove_element_key](#remove_element_key)
- [set_pysimplegui_compatibility](#set_pysimplegui_compatibility)
- [set_theme](#set_theme)

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

## get_eg_window_count

Get the number of windows.

```py
def get_eg_window_count() -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L221)

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

## set_pysimplegui_compatibility

Set compatibility with PySimpleGUI (Default=True)

```py
def set_pysimplegui_compatibility(flag: bool = True) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L166)

## set_theme

Change look and feel

- macOS --- ('aqua', 'clam', 'alt', 'default', 'classic')
- Windows --- ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
- Linux --- ('clam', 'alt', 'default', 'classic')

```py
def set_theme(name: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L176)

