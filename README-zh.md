# TkEasyGUI

`TkEasyGUI` 是一个 Python 库，允许轻松简单地创建 GUI 应用程序。在事件模型中，它与著名的 GUI 库 `PySimpleGUI` 兼容。

Python 的标准 UI 库 `Tkinter`，通常被认为入门门槛高且难以使用。通过使用这个库，你可以轻松直观地创建 GUI 应用程序。

此项目采用宽松的 MIT 许可证。这个许可证将来不会更改。让我们享受创建 GUI 程序的乐趣。

## 平台

- Windows / macOS / Linux（需要 tkinter）

## 安装

从 pypi 安装


```sh
python -m pip install TkEasyGUI
```

从 GitHub 仓库安装


```sh
python -m pip install git+https://github.com/kujirahand/tkeasygui-python
```

- （备忘）从旧版本更新（小于 0.2.24）将失败。([查看解决方案](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/installation_trouble.md))

## 如何使用

要创建一个只有标签和按钮的简单窗口，你可以这样写：

```py
import TkEasyGUI as eg

# 创建窗口
layout = [
    [eg.Text("Hello, World!")],
    [eg.Button("OK")]
]
window = eg.Window("Hello", layout=layout)

# 事件循环
while window.is_alive():
    # 获取事件
    event, values = window.read()
    # 检查事件
    if event == "OK":
        eg.popup("按下了 OK 按钮")
        break
window.close()
```

## 示例

我们准备了一系列示例以展示简单的使用方式。请查看。

- [示例](https://github.com/kujirahand/tkeasygui-python/tree/main/tests).

## 文档

下面是类和方法的详细列表。

- [文档](https://github.com/kujirahand/tkeasygui-python/tree/main/docs)

## 关于与 PySimpleGUI 的关系

- 在使用基本功能时，它与 PySimpleGUI 兼容。你可以使用与 PySimpleGUI 相同的事件模型编写程序。
- 基本 GUI 组件的名称也保持一致。然而，虽然一些属性名称不同，但实现了许多独特的功能。
- 本项目是以 PySimpleGUI 为思路开发的，但完全从头开始实现。不存在许可问题。
- 我们不考虑与 PySimpleGUI 完全兼容。

## 链接

- [pypi.org > TkEasyGUI](https://pypi.org/project/tkeasygui/)
- [GitHub > TkEasyGUI](https://github.com/kujirahand/tkeasygui-python/)
- [Discord > TkEasyGUI](https://discord.gg/G2JXaRft)
