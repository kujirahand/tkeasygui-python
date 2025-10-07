# Module TkEasyGUI.utils

TkEasyGUI utilities functions.

---------------------------

- [Classes](#classes-of-tkeasyguiutils)
- [Functions](#functions-of-tkeasyguiutils)

# Classes of TkEasyGUI.utils

## ImageResizeType

Image resize type.

### Methods of ImageResizeType



### ImageResizeType.name

The name of the Enum member.

### ImageResizeType.value

The value of the Enum member.

## TkEasyError

TkEasyError Exception class.

```py
class TkEasyError(self, message="TkEasyError"):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L82)

### Methods of TkEasyError



### TkEasyError.args

### TkEasyError.with_traceback

Exception.with_traceback(tb) --
    set self.__traceback__ to tb and return self.

# Functions of TkEasyGUI.utils

- [append_text_file](#append_text_file)
- [convert_color_html](#convert_color_html)
- [convert_color_rgb16](#convert_color_rgb16)
- [copy_to_clipboard](#copy_to_clipboard)
- [get_clipboard](#get_clipboard)
- [get_current_theme](#get_current_theme)
- [get_font_list](#get_font_list)
- [get_platform](#get_platform)
- [get_root_window](#get_root_window)
- [get_scaling](#get_scaling)
- [get_screen_dpi](#get_screen_dpi)
- [get_screen_size](#get_screen_size)
- [get_system_info](#get_system_info)
- [get_tcl_version](#get_tcl_version)
- [get_tk_version](#get_tk_version)
- [get_tnemes](#get_tnemes)
- [is_mac](#is_mac)
- [is_win](#is_win)
- [load_json_file](#load_json_file)
- [load_text_file](#load_text_file)
- [paste_from_clipboard](#paste_from_clipboard)
- [save_json_file](#save_json_file)
- [save_text_file](#save_text_file)
- [screenshot](#screenshot)
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

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L188)

## convert_color_html

Convert RGB color(16bit tuple) to HTML color name.

```py
def convert_color_html(color_name: str) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L275)

## convert_color_rgb16

Convert color to RGB, return (r, g, b) tuple. range=0-65535

```py
def convert_color_rgb16(color_name: str) -> tuple[int, int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L269)

## copy_to_clipboard

Copy text to clipboard

```py
def copy_to_clipboard(text):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L112)

## get_clipboard

Get text from clipboard

```py
def get_clipboard():
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L107)

## get_current_theme

Get current theme

```py
def get_current_theme() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L244)

## get_font_list

Get font list

```py
def get_font_list() -> list[str]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L295)

## get_platform

Get platform

```py
def get_platform() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L125)

## get_root_window

Get root window.

```py
def get_root_window() -> tk.Tk:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L161)

## get_scaling

Get scaling factor.

```py
def get_scaling() -> float:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L161)

## get_screen_dpi

Get screen DPI.

```py
def get_screen_dpi() -> int:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L154)

## get_screen_size

Get screen size.

```py
def get_screen_size() -> tuple[int, int]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L146)

## get_system_info

Get system info

```py
def get_system_info():
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L302)

## get_tcl_version

Get tcl version

```py
def get_tcl_version() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L288)

## get_tk_version

Get tk version

```py
def get_tk_version() -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L281)

## get_tnemes

Get theme list

```py
print(get_themes())
```

```py
def get_tnemes() -> tuple[str, ...]:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L226)

## is_mac

Platform : is mac?

```py
def is_mac() -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L130)

## is_win

Platform : is Windows?

```py
def is_win() -> bool:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L135)

## load_json_file

Load JSON file.

```py
def load_json_file(filename: str, default_value: Any = None) -> Any:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L194)

## load_text_file

Load text file.

```py
def load_text_file(
    filename: str, encoding: str = "utf-8", default_value: str = ""
) -> str:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L171)

## paste_from_clipboard

Get text from clipboard

```py
def paste_from_clipboard():
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L117)

## save_json_file

Save JSON file.

```py
def save_json_file(filename: str, data: Any) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L203)

## save_text_file

Save text file.

```py
def save_text_file(filename: str, text: str, encoding: str = "utf-8") -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L182)

## screenshot

Take a screenshot.

```py
def screenshot() -> PILImage.Image:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L140)

## set_clipboard

Copy text to clipboard

```py
def set_clipboard(text):
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L102)

## set_default_theme

Set default theme

```py
print(get_themes())
```

```py
def set_default_theme() -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L249)

## set_theme

Change look and feel

- macOS --- ('aqua', 'clam', 'alt', 'default', 'classic')
- Windows --- ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
- Linux --- ('clam', 'alt', 'default', 'classic')

```py
def set_theme(name: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/widgets_window.py#L176)

## str_to_float

Convert string to float.

```py
def str_to_float(value: str, default_value: float = 0) -> float:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L212)

## theme

Set theme (alias of set_theme)

```py
def theme(name: str) -> None:
```

- [source](https://github.com/kujirahand/tkeasygui-python/blob/main/TkEasyGUI/utils.py#L239)

