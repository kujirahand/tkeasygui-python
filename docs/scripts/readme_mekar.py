# foramt documents script
import glob
import os
import re

# path
SCRIPT_DIR = os.path.dirname(__file__)
DOCS_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(DOCS_DIR)
TEMPLATE_DIR = os.path.join(DOCS_DIR, "template")

print("TEMPLATE_DIR=", TEMPLATE_DIR)
print("DOCS_DIR=", DOCS_DIR)

# read
with open(os.path.join(TEMPLATE_DIR, "README.md"), "r", encoding="utf-8") as fp:
    readme = fp.read()

# write
with open(os.path.join(DOCS_DIR, "README.md"), "w", encoding="utf-8") as fp:
    fp.write(readme)
