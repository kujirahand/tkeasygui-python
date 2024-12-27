#!/bin/sh

# pip install ruff
ruff check
mypy TkEasyGUI/*.py
