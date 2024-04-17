#!/bin/bash
SCRIPT_DIR=$(cd $(dirname $0); pwd)
# pip install inari
echo "--- inari ---"
python -m inari TkEasyGUI docs
echo "--- format ---"
python $SCRIPT_DIR/docs/scripts/format_docs.py
echo "--- make docs/README.md ---"
python $SCRIPT_DIR/docs/scripts/readme_mekar.py
echo "ok"

