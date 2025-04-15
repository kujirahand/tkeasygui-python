#!/bin/sh

# pip install ruff
ruff check TkEasyGUI/*.py
mypy TkEasyGUI/*.py
