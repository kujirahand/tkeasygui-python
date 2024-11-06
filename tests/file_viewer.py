#!/usr/bin/env python
"""
### File Viewer

The File Viewer is a simple program that allows you to view and run Python files in a directory.
"""
import os
import subprocess
import sys
from threading import Thread

# import PySimpleGUI as sg
import TkEasyGUI as eg

# set path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#TARGET_DIR = os.path.join(ROOT_DIR, "tests")
TARGET_DIR = ROOT_DIR
# get font
font = ("Arial", 20 if eg.is_mac() else 12)

def get_program_files():
    # files = os.listdir(ROOT_DIR)
    files = []
    for root, dirs, file_list in os.walk(TARGET_DIR):
        for f in file_list:
            full = os.path.join(root, f)
            parts = full[len(TARGET_DIR)+1:]
            files.append(parts)
            print("-", parts)
    files = [f for f in files if f.endswith('.py')] # filter
    files = list(sorted(files))
    return files

def run_program(filename):
    file_dir = os.path.dirname(filename)
    subprocess.run([sys.executable, filename], cwd=file_dir)

layout = [
    [
        eg.Text("TkEasyGUI samples:"),
        eg.Text(f"(TkEasyGUI v.{eg.__version__})")
    ],
    [
        # left sizde listbox
        eg.Listbox( 
            values=get_program_files(), 
            size=(30, 20), 
            key="-files-", 
            enable_events=True,
        ),
        eg.VSeparator(pad=5),
        # right side textbox
        eg.Multiline(size=(40, 20), key="-body-", expand_y=True, expand_x=True)
    ],
    [eg.HSeparator(pad=5)],
    [
        eg.Button(eg.get_text("Run"), key="-run-", size=(10, 1)),
        eg.Button(eg.get_text("Close"), key="-close-"),
    ],
]
window = eg.Window("Python Viewer", layout, font=font)
# event loop
while True:
    event, values = window.read()
    print("#", event, values)
    if event in [eg.WINDOW_CLOSED, "-close-"]:
        break
    if event == "-run-":
        files = values["-files-"]
        if len(files) > 0:
            filename = values["-files-"][0]
            fullpath = os.path.join(TARGET_DIR, filename)
            Thread(target=run_program, args=(fullpath,)).start()
    if event == "-files-":
        files = values["-files-"]
        if len(files) > 0:
            filename = values["-files-"][0]
            fullpath = os.path.join(TARGET_DIR, filename)
            with open(fullpath, "r", encoding="utf-8") as f:
                text = f.read()
                window["-body-"].update(text)
window.close()
