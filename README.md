# tkeasygui

Easy and Simple GUI Library for Python.
Take it Easy to develop GUI apps.

The usability of the GUI library PySimpleGUI allows for the easy creation of applications.

## Install

Install from https://pypi.org/


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
while True:
    # get window event
    event, values = window.read()
    # close button
    if event == eg.WINDOW_CLOSED:
        break
    # check OK Button
    if event == "OK":
        eg.popup("Pushed OK Button")
        break
window.close()
```


## Samples

Please see [tests](tests/).

## Regarding the relationship with PySimpleGUI

This was developed with reference to PySimpleGUI, but has been re-implemented from scratch.
While its usage is similar to PySimpleGUI, it has been expanded with unique features.

## Link

- [pypi.org > tkeasygui](https://pypi.org/project/tkeasygui/)
- [GitHub > tkeasygui](https://github.com/kujirahand/tkeasygui-python/)

