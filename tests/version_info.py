"""
# Version info

This script shows the version information of TkEasyGUI and system information.
"""

import subprocess

import TkEasyGUI as eg

WEB_SITE = "https://github.com/kujirahand/tkeasygui-python/"
S_COPY = eg.get_text("Copy")
S_CLOSE = eg.get_text("Close")
# define layout
layout = [
    [eg.Text(f"{eg.__doc__.strip()}", color="navy")],
    [
        eg.Frame(
            "Version",
            expand_x=True,
            layout=[
                [
                    eg.Text("TkEasyGUI:"),
                    eg.Button(f"v{eg.__version__}", key="-b1-"),
                    eg.Button("Web"),
                ],
            ],
        )
    ],
    [
        eg.Frame(
            "System info:",
            layout=[
                [
                    eg.Multiline(
                        f"{eg.get_system_info()}",
                        key="-sys-info-",
                        size=(60, 5),
                        expand_x=True,
                    )
                ],
                [eg.Button(S_COPY), eg.Button("Copy as Markdown")],
            ],
        )
    ],
    [
        eg.Column(
            layout=[[eg.Button("OK", width=10), eg.Button(S_CLOSE)]],
            text_align="right",
            expand_x=True,
        ),
    ],
]
# window create
window = eg.Window(
    "Version info", layout=layout, font=("", 14 if eg.is_mac() else 9), row_padding=5
)
# event loop
for event, values in window.event_iter():
    print("#", event, values)
    if event == "OK":
        eg.popup("Thank you.")
        break
    if event == S_CLOSE:
        break
    if event in ["-b1-", "-b2-", "-b3-"]:
        btn: eg.Button = window[event]
        label = btn.get_text()
        eg.set_clipboard(label)
        eg.popup(f"Copied to clipboard:\n{label}")
    if event == S_COPY:
        text = window["-sys-info-"].get_text()
        eg.set_clipboard(text)
        eg.popup("Copied to clipboard.")
    if event == "Copy as Markdown":
        markdown_text = window["-sys-info-"].get_text()
        markdown_text = f"```\n{markdown_text}\n```\n"
        eg.set_clipboard(markdown_text)
        eg.popup("Copied markdown to clipboard.")
    if event == "Web":
        if eg.is_mac():
            subprocess.call(f"open {WEB_SITE}", shell=True)
        else:
            subprocess.call(f"start {WEB_SITE}", shell=True)
