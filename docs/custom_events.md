# TkEasyGUI > Custom Events

In addition to the unique events of the element, you can use **custom events** available in `Tkinter`.
There are several ways to bind them.

## Simple bind

After creating the element, bind the event with the bind method.
The event name will be in the format of "f{key}{handle_name}".

```py
import TkEasyGUI as sg
# (1) create Element
canvas = sg.Canvas(size=(400, 400), key="-canvas-")
window = sg.Window("Canvas", layout=[[canvas]], finalize=True)

# (2) bind custom events
canvas.bind("<ButtonPress>", "press")
canvas.bind("<ButtonRelease>", "release")
canvas.bind("<Motion>", "motion")

# (3) event loop
while True:
    event, values = window.read()
    if event == "-canvas-press":
        print(canvas.user_bind_event) # get event data
        print("x=", canvas.user_bind_event.x)
        print("y=", canvas.user_bind_event.y)
        break
    elif event == "-canvas-relase":
        pass
    elif event == "-canvas-motion":
        pass
```

## Multiple bind - using `bind_events` method

When creating an element, you can specify multiple events using the bind_events method.

```py
canvas = sg.Canvas(size=(400, 400), key="-canvas-").bind_events({
    "<ButtonPress>": "press",
    "<ButtonRelease>": "release",
    "<Motion>": "motion",
})
```

## Set custom events in constructor

Within the constructor, you can specify bind_events as an argument.

```py
canvas = sg.Canvas(
    size=(400, 400),
    key="-canvas-",
    bind_events={
        "<ButtonPress>": "mousedown",
        "<ButtonRelease>": "mouseup",
        "<Motion>": "mousemove"
    }
)
```

## Samples:

- [/tests/paint_eg.py](https://github.com/kujirahand/tkeasygui-python/blob/main/tests/paint_eg.py)
- [/tests/paint_compatible.py](https://github.com/kujirahand/tkeasygui-python/blob/main/tests/paint_compatible.py)


# Event Hook

You can hook an event before a system event occurs.
This mechanism is utilized within elements like `FileBrowse`.

```py
import TkEasyGUI as eg

window = eg.Window("Event Hook Test", layout=[
    [eg.Button("OK")],
    [eg.Button("Cancel")],
])
# register event hook
window.register_event_hooks({
    "OK": [
        lambda event, values: print("#OK#hook1:", event, values),
        lambda event, values: print("#OKhook#2:", event, values),
        lambda event, values: print("#OKhook#3:", event, values),
    ],
    "Cancel": [
        lambda event, values: print("#Cancel#hook#1:", event, values),
        lambda event, values: print("#Cancel#hook#2:", event, values),
        lambda event, values: True, # stop event propagation
        lambda event, values: print("#Cancel#hook#3:", event, values),
    ]
})
while window.is_alive():
    event, values = window.read()
    print(event, values)
    if event == "OK":
        break
    elif event == "Cancel":
        break
    elif event == "Cancel-stopped":
        break
window.close()
```

## Samples:

- [/tests/event_hooks.py](https://github.com/kujirahand/tkeasygui-python/blob/main/tests/event_hooks.py)
