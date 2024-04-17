#!/bin/bash
SCRIPT_DIR=$(cd $(dirname $0); pwd)
# pip install inari
echo "--- makedoc.py ---"
python makedoc.py
echo "--- make docs/README.md ---"
python $SCRIPT_DIR/docs/scripts/readme_mekar.py
echo "ok"

