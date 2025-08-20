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
# TARGET_DIR = os.path.join(ROOT_DIR, "tests")
TARGET_DIR = ROOT_DIR
# get font
font = ("Arial", 20 if eg.is_mac() else 12)


def get_program_files():
    """Get Python files in the target directory."""
    target_files = []
    for root, _dirs, file_list in os.walk(TARGET_DIR):
        for a_file in file_list:
            full = os.path.join(root, a_file)
            parts = full[len(TARGET_DIR) + 1 :]
            target_files.append(parts)
            print("-", parts)
    target_files = [f for f in target_files if f.endswith(".py")]  # filter
    target_files = list(sorted(target_files))
    return target_files


def run_program(target_file: str):
    """Run the selected Python file."""
    file_dir = os.path.dirname(target_file)
    subprocess.run([sys.executable, target_file], cwd=file_dir, check=False)


def main():
    """Main function to run the File Viewer."""
    layout = [
        [eg.Text("TkEasyGUI samples:"), eg.Text(f"(TkEasyGUI v.{eg.__version__})")],
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
            eg.Multiline(size=(40, 20), key="-body-", expand_y=True, expand_x=True),
        ],
        [eg.HSeparator(pad=5)],
        [
            eg.Push(),
            eg.Button(eg.get_text("Run"), key="-run-", width=10),
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


if __name__ == "__main__":
    main()
