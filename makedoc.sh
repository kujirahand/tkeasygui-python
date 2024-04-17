#!/bin/bash
SCRIPT_DIR=$(cd $(dirname $0); pwd)
# pip install inari
python -m inari TkEasyGUI docs
python $SCRIPT_DIR/docs/scripts/format_docs.py
python $SCRIPT_DIR/docs/scripts/readme_mekar.py

