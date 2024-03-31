# TkEasyGUI

`TkEasyGUI` is a Python library that allows for the easy and simple creation of GUI applications.
In the event model, it is compatible with the well-known GUI library `PySimpleGUI`.

Python's standard UI library `Tkinter`, is often considered to have a high barrier to entry and to be difficult to use. By using this library, you can create GUI applications easily and intuitively.

This project adopts the lenient MIT license. This license will not change in the future. Let's enjoy creating GUI programs.

- [👉日本語のREADME](https://github.com/kujirahand/tkeasygui-python/blob/main/README-ja.md)
  - [(注意) パッケージ名が大文字込みの`TkEasyGUI`に変わりました](https://github.com/kujirahand/tkeasygui-python/blob/main/README-ja.md#%E3%83%A1%E3%83%A2---v0224)

## Platform

- Windows / macOS / Linux (tkinter required)

## Install

Install from pypi


```sh
python -m pip install TkEasyGUI
```

Install from GitHub Repository


```sh
python -m pip install git+https://github.com/kujirahand/tkeasygui-python
```

### Install memo

- From version 0.2.24, the package name has also been changed from `tkeasygui` to `TkEasyGUI`.
  - If you have used a previous version, you will see `ModuleNotFoundError: No module named 'TKEasyGUI'`.
  - Please run the command below to completely remove the old `tkeasygui` package.
  - It seems that cache files remain even if you use the `pip uninstall tkeasygui` command.
  - Start the `python` command or `IDLE` and execute the following command.

```py:remove_old_package.py
# remove old package directory
import os, shutil, PIL
packages = os.path.dirname(PIL.__path__[0])
old_package = os.path.join(packages, "tkeasygui")
print(f"Remove: {old_package}")
shutil.rmtree(old_package)
```

## How to use

To create a simple window with only labels and buttons, you would write as follows:

```py
import TkEasyGUI as eg

# Create window
layout = [
    [eg.Text("Hello, World!")],
    [eg.Button("OK")]
]
window = eg.Window("Hello", layout=layout)

# Event loop
while window.is_alive():
    # get event
    event, values = window.read()
    # check event
    if event == "OK":
        eg.popup("Pushed OK Button")
        break
window.close()
```

## Samples

We have prepared a selection of samples to demonstrate simple usage. Please check them out.

- [samples](https://github.com/kujirahand/tkeasygui-python/tree/main/tests).

## Documents

Below is a detailed list of classes and methods.

- [docs](https://github.com/kujirahand/tkeasygui-python/tree/main/docs)

## About the relationship with PySimpleGUI

- When utilizing basic features, it is compatible with PySimpleGUI. You can write programs using the same event model as PySimpleGUI.
- The names of basic GUI components are also kept the same. However, while some property names differ, many unique features have been implemented.
- This project was developed with PySimpleGUI in mind, but has been implemented entirely from scratch. There are no licensing issues.
- We are not considering full compatibility with PySimpleGUI.

## Link

- [pypi.org > TkEasyGUI](https://pypi.org/project/tkeasygui/)
- [GitHub > TkEasyGUI](https://github.com/kujirahand/tkeasygui-python/)

