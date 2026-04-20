# TkEasyGUI Theme Guide

This document explains how to use themes and how to change theme-related defaults in TkEasyGUI.

## Overview

TkEasyGUI uses `ttk` themes for modern widget rendering.
You can switch themes at runtime using `set_theme()` or `theme()`.

Default theme by platform:

- macOS: `aqua`
- Windows: `vista`
- Linux/others: `clam`

## Basic theme usage

### Change theme with `set_theme`

```python
import TkEasyGUI as eg

eg.set_theme("clam")
window = eg.Window("Theme sample", [[eg.Button("OK", use_ttk_buttons=True)]])
window.read()
window.close()
```

### Alias: `theme`

`theme()` is an alias of `set_theme()`.

```python
import TkEasyGUI as eg

eg.theme("default")
```

## List available themes

Use `get_tnemes()` to inspect themes available in your current Tk runtime.

```python
import TkEasyGUI as eg

print(eg.get_tnemes())
```

Note:
- Function name is `get_tnemes()` in current API.

## Change button style behavior

`Button` can render with `ttk.Button` (modern) or `tk.Button` (classic).

- `use_ttk_buttons=True` (default): use `ttk.Button`
- `use_ttk_buttons=False`: use `tk.Button`

```python
import TkEasyGUI as eg

layout = [
    [eg.Button("Modern", use_ttk_buttons=True)],
    [eg.Button("Classic", use_ttk_buttons=False)],
]
window = eg.Window("Buttons", layout)
window.read()
window.close()
```

Note:
- If you set `use_ttk_buttons=True`, explicit button height settings are ignored.
- This is a limitation of `ttk`.
- If you need to control button height, use `use_ttk_buttons=False`.




## How to customize defaults

### Global theme default

If you want to change the default theme for your app, call `set_theme()` before creating windows.

```python
import TkEasyGUI as eg

eg.set_theme("winnative")
```

### Revert to old Windows look

If you want behavior close to older Windows appearance:

```python
import TkEasyGUI as eg

eg.set_theme("vista")
layout = [[eg.Button("OK", use_ttk_buttons=False)]]
window = eg.Window("Legacy look", layout)
window.read()
window.close()
```

## Recommended test scripts

After changing theme defaults, validate with:

```bash
python tests/file_viewer.py
python tests/theme/ttk_button.py
python tests/ui_test.py
python tests/many_buttons.py
```
