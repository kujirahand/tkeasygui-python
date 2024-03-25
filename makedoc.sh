#!/bin/bash
SCRIPT_DIR=$(cd $(dirname $0); pwd)
# pip install inari
python -m inari TkEasyGUI docs
python $SCRIPT_DIR/docs/format_docs.py

