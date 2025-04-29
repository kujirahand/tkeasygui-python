# Module TkEasyGUI.utils

TkEasyGUI utilities functions.

---------------------------

- [Functions](#functions-of-tkeasyguiutils)

# Functions of TkEasyGUI.utils

- [append_text_file](#append_text_file)
- [convert_color_html](#convert_color_html)
- [convert_color_rgb16](#convert_color_rgb16)
- [copy_to_clipboard](#copy_to_clipboard)
- [generate_element_id](#generate_element_id)
- [generate_element_style_key](#generate_element_style_key)
- [get_clipboard](#get_clipboard)
- [get_current_theme](#get_current_theme)
- [get_platform](#get_platform)
- [get_root_window](#get_root_window)
- [get_scaling](#get_scaling)
- [get_screen_dpi](#get_screen_dpi)
- [get_screen_size](#get_screen_size)
- [get_tnemes](#get_tnemes)
- [get_ttk_style](#get_ttk_style)
- [is_mac](#is_mac)
- [is_win](#is_win)
- [load_json_file](#load_json_file)
- [load_text_file](#load_text_file)
- [paste_from_clipboard](#paste_from_clipboard)
- [register_element_key](#register_element_key)
- [remove_element_key](#remove_element_key)
- [save_json_file](#save_json_file)
- [save_text_file](#save_text_file)
- [screenshot](#screenshot)
- [set_PySimpleGUI_compatibility](#set_pysimplegui_compatibility)
- [set_clipboard](#set_clipboard)
- [set_default_theme](#set_default_theme)
- [set_theme](#set_theme)
- [str_to_float](#str_to_float)
- [theme](#theme)

## append_text_file

Append text file.

```py
def append_text_file(filename: str, text: str, encoding: str = "utf-8") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L147)

## convert_color_html

Convert RGB color(16bit tuple) to HTML color name.

```py
def convert_color_html(color_name: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L303)

## convert_color_rgb16

Convert color to RGB, return (r, g, b) tuple. range=0-65535

```py
def convert_color_rgb16(color_name: str) -> tuple[int, int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L297)

## copy_to_clipboard

Copy text to clipboard

```py
def copy_to_clipboard(text):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L74)

## generate_element_id

Generate a unique id for a value element.

```py
def generate_element_id() -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L353)

## generate_element_style_key

Get a unique id for an element.

```py
def generate_element_style_key(element_type: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L318)

## get_clipboard

Get text from clipboard

```py
def get_clipboard():
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L69)

## get_current_theme

Get current theme

```py
def get_current_theme() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L272)

## get_platform

Get platform

```py
def get_platform() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L87)

## get_root_window

Get root window.

```py
def get_root_window() -> tk.Tk:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L192)

## get_scaling

Get scaling factor.

```py
def get_scaling() -> float:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L121)

## get_screen_dpi

Get screen DPI.

```py
def get_screen_dpi() -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L115)

## get_screen_size

Get screen size.

```py
def get_screen_size() -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L108)

## get_tnemes

Get theme list

```py
print(get_themes())
```

```py
def get_tnemes() -> tuple[str, ...]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L254)

## get_ttk_style

Get ttk style

```py
def get_ttk_style() -> ttk.Style:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L225)

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

## load_json_file

Load JSON file.

```py
def load_json_file(filename: str, default_value: Any = None) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L153)

## load_text_file

Load text file.

```py
def load_text_file(
    filename: str, encoding: str = "utf-8", default_value: str = ""
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L130)

## paste_from_clipboard

Get text from clipboard

```py
def paste_from_clipboard():
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L79)

## register_element_key

Register element key.

```py
def register_element_key(key: KeyType) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L334)

## remove_element_key

Remove element key.

```py
def remove_element_key(key: KeyType) -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L342)

## save_json_file

Save JSON file.

```py
def save_json_file(filename: str, data: Any) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L164)

## save_text_file

Save text file.

```py
def save_text_file(filename: str, text: str, encoding: str = "utf-8") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L141)

## screenshot

Take a screenshot.

```py
def screenshot() -> PIL.Image.Image:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L101)

## set_PySimpleGUI_compatibility

Set compatibility with PySimpleGUI (Default=True)

```py
def set_PySimpleGUI_compatibility(flag: bool = True) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L219)

## set_clipboard

Copy text to clipboard

```py
def set_clipboard(text):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L64)

## set_default_theme

Set default theme

```py
print(get_themes())
```

```py
def set_default_theme() -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L277)

## set_theme

Change look and feel

- macOS --- ('aqua', 'clam', 'alt', 'default', 'classic')
- Windows --- ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
- Linux --- ('clam', 'alt', 'default', 'classic')

```py
def set_theme(name: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L238)

## str_to_float

Convert string to float.

```py
def str_to_float(value: str, default_value: float = 0) -> float:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L175)

## theme

Set theme (alias of set_theme)

```py
def theme(name: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L267)

