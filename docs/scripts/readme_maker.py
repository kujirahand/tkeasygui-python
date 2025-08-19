"""foramt documents script"""
import json
import os

# path
SCRIPT_DIR = os.path.dirname(__file__)
DOCS_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(DOCS_DIR)
TEMPLATE_DIR = os.path.join(SCRIPT_DIR, "template")
ELEMENTS_JSON = os.path.join(SCRIPT_DIR, "elements.json")

REPO = "https://github.com/kujirahand/tkeasygui-python/blob/main"

print("TEMPLATE_DIR=", TEMPLATE_DIR)
print("DOCS_DIR=", DOCS_DIR)

# read
with open(os.path.join(TEMPLATE_DIR, "README.md"), "r", encoding="utf-8") as fp:
    readme = fp.read()

with open(ELEMENTS_JSON, "r", encoding="utf-8") as fp:
    elements = json.load(fp)
    result = []
    for name in elements:
        name2 = name.replace(" ", "-").lower()
        result.append(f"- [{name}]({REPO}/docs/TkEasyGUI/widgets-py.md#{name2})")
    readme = readme.replace("__ELEMENTS__", "\n".join(result))

# write
with open(os.path.join(DOCS_DIR, "README.md"), "w", encoding="utf-8") as fp:
    fp.write(readme)
