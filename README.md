# TkEasyGUI - the easiest library for GUI

[![PyPI Downloads](https://static.pepy.tech/badge/tkeasygui)](https://pepy.tech/projects/tkeasygui)
[![PyPI Version](https://img.shields.io/pypi/v/tkeasygui)](https://pypi.org/project/tkeasygui/)
[![GitHub License](https://img.shields.io/github/license/kujirahand/tkeasygui-python)](https://github.com/kujirahand/kudb-python/blob/main/LICENSE)

`TkEasyGUI` is the easiest library for creating GUIs in Python.

This library allows you to easily create GUI applications with Python.
Since it is based on Tkinter, it runs consistently on Windows, macOS, and Linux.
With a variety of built-in dialogs and customizable forms, you can develop applications effortlessly.

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/tkeasygui-shot1000.jpg" width="500" alt="TkEasyGUI Screenshot">

- [👉日本語](https://github.com/kujirahand/tkeasygui-python/blob/main/README-ja.md) / [👉中文](https://github.com/kujirahand/tkeasygui-python/blob/main/README-zh.md) / [👉한국어](https://github.com/kujirahand/tkeasygui-python/blob/main/README-ko.md)

## Platform

- Windows / macOS / Linux (Tkinter required)


## Install

Install package from [PyPI](https://pypi.org/project/TkEasyGUI/).

```sh
pip install TkEasyGUI
# or
python -m pip install TkEasyGUI
```

Install package from [GitHub Repository](https://github.com/kujirahand/tkeasygui-python).

```sh
python -m pip install git+https://github.com/kujirahand/tkeasygui-python
```

## Features of This Library

- Python's standard UI library `Tkinter`, is often considered to have a high barrier to entry and to be difficult to use. By using this library, you can create GUI applications easily and intuitively.
- This package supports type hints, allowing property selection via code completion. `Python 3.9 or later` is required.
- In the event model, it is compatible with the well-known GUI library `PySimpleGUI`.
- This project adopts the lenient MIT license. This license will not change in the future. Let's enjoy creating GUI programs.

## How to use - popup dialogs

Using TkEasyGUI is simple. If you only want to display a dialog, it requires just two lines of code.

```py
import TkEasyGUI as eg
# Show Text dialog
eg.print("A joyful heart is good medicine.")
```

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/sample1.png" width="300" alt="TkEasyGUI">


Ask the user for their name and display that name in the window.

```py
import TkEasyGUI as eg
# Show Input dialog
name = eg.input("What is your name?")
eg.print(f"Hello, {name}.")
```

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/sample2.png" width="300" alt="TkEasyGUI">

Furthermore, a dialog is available that allows specifying multiple input fields.

```py
import TkEasyGUI as eg
# Show Form dialog
form = eg.popup_get_form(["Name", "Age", "Hobbies"])
if form:
    name = form["Name"]
    age = form["Age"]
    hobbies = form["Hobbies"]
    eg.print(f"name={name}, age={age}, hobby={hobbies}")
```

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/sample3.png" width="300" alt="TkEasyGUI">

### More Dialogs

`TkEasyGUI` provides a variety of dialogs. For example, a color selection dialog, a file selection dialog, and a calendar dialog.

- [Docs > Dialogs](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/dialogs-py.md)

## How to use - widgets

To create a simple window with only labels and buttons, you would write as follows:

```py
import TkEasyGUI as eg
# define layout
layout = [
    [eg.Text("Hello, World!")],
    [eg.Button("OK")]
]
# create a window
with eg.Window("Hello App", layout) as window:
    # event loop
    for event, values in window.event_iter():
        if event == "OK":
            eg.print("Thank you.")
            break
```


You can describe it using an event model similar to the famous GUI library, PySimpleGUI.

```py
import TkEasyGUI as eg

# define layout
layout = [
    [eg.Text("Hello, World!")],
    [eg.Button("OK")]
]
# create a window
window = eg.Window("Hello App", layout)
# event loop
while True:
    event, values = window.read()
    if event in ["OK", eg.WINDOW_CLOSED]:
        eg.popup("Thank you.")
        break
# close window
window.close()
```

- [Docs > What kind of elements can be used?](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/README.md#tkeasygui-elements-list)

## Samples

We have prepared a selection of samples to demonstrate simple usage. Please check them out.

- [samples](https://github.com/kujirahand/tkeasygui-python/tree/main/tests).

Running `tests/file_viewer.py` allows all samples to be easily launched.

## Documents

Below is a detailed list of classes and methods.

- [docs](https://github.com/kujirahand/tkeasygui-python/tree/main/docs)
  - [Dialogs](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/dialogs-py.md)
  - [Elements](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/widgets-py.md)
  - [Utilities](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/utils-py.md)

## Tutorial

Japanese tutorials:

- [TkEasyGUI - Pythonで最も素早くデスクトップアプリを創るライブラリ](https://note.com/kujirahand/n/n33a2df3aa3e5)
- [マイナビニュースPython連載116回目 - 合計/整形/コピーのツールを作ろう](https://news.mynavi.jp/techplus/article/zeropython-116/)
- [(Book) Pythonでつくるデスクトップアプリ メモ帳からスクレイピング・生成AI利用まで](https://amzn.to/45R2NSH)
- [(Magazine) 日経ソフトウエア2025年5月号の特集記事 - TkEasyGUIを使ってみよう](https://amzn.to/4j1lj0c)

There are other helpful articles as well.

- [TkEasyGUI - 目的別ダイアログ完全ガイド](https://note.com/sirodon_256/n/n4138ebf4877f)
- [TkEasyGUIライブラリの基本とサンプルコード解説](https://note.com/sirodon_256/n/na73d3fdac68d)

## Compatibility with PySimpleGUI

- When using basic functionalities, it is compatible with PySimpleGUI. Programs can be written using the same event-driven model as PySimpleGUI.  
- The names of basic GUI components are kept the same, but some property names differ.  
- TkEasyGUI has been completely reimplemented from scratch and is licensed under the MIT License.
- However, full compatibility with PySimpleGUI is not intended.

## TkEasyGUI features:

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/logo-button.jpg" width="180" alt="TkEasyGUI Logo">

- Using a `for` loop and `window.event_iter()` enables straightforward event processing.
- Custom popup dialogs, such as a color selection dialog(`eg.popup_color`), a list dialog(`eg.popup_listbox`), form dialog(`eg.popup_get_form`) are available.
- The `Image` class supports not only PNG but also JPEG formats.
- Convenient event hooks and features for bulk event registration are provided - [docs/custom_events](docs/custom_events.md).
- Methods such as Copy, Paste, and Cut are added to text boxes (Multiline/Input).
- The system's default color scheme is utilized.

## Link

- [pypi.org > TkEasyGUI](https://pypi.org/project/tkeasygui/)
- [GitHub > TkEasyGUI](https://github.com/kujirahand/tkeasygui-python/)
- [Discord > TkEasyGUI](https://discord.gg/NX8WEQd42S)
