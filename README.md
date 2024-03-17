# TkEasyGUI

`TkEasyGUI` is a Python library that allows for the easy and simple creation of GUI applications.
In the event model, it is compatible with the well-known GUI library `PySimpleGUI`.

Python's standard UI library `Tkinter`, is often considered to have a high barrier to entry and to be difficult to use. By using this library, you can create GUI applications easily and intuitively.

## Install

Install from pypi


```sh
python -m pip install tkeasygui
```

Install from GitHub Repository


```sh
python -m pip install git+https://github.com/kujirahand/tkeasygui-python
```

## How to use

To create a simple window with only labels and buttons, you would write as follows:

```py
import tkeasygui as eg

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

Please see [tests](tests/).

## Documents

- [docs](docs/README.md)

## Regarding the relationship with PySimpleGUI

This was developed with reference to PySimpleGUI, but has been re-implemented from scratch.
While its usage is similar to PySimpleGUI, it has been expanded with unique features.

## Link

- [pypi.org > TkEasyGUI](https://pypi.org/project/tkeasygui/)
- [GitHub > TkEasyGUI](https://github.com/kujirahand/tkeasygui-python/)

