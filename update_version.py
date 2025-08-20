#!/usr/bin/env python
"""Update TkEasyGUI version from pyproject.toml"""
# pyprojet.tomlを見てパッケージのバージョンを更新する
# 使い方: python update_version.py
import sys

import toml

# read
with open("pyproject.toml", "r", encoding="utf-8") as f:
    data = toml.load(f)
version = data["project"]["version"]
versions = version.split(".")
if int(versions[0]) == 0 or int(versions[2]) == 0:
    print("---------------------------------------", file=sys.stderr)
    print("!!! BROKEN VERSION INFO", file=sys.stderr)
    print("!!! Please check : `update_version.py` & `pyproject.toml`", file=sys.stderr)
    print("---------------------------------------", file=sys.stderr)
    sys.exit(1) # 異常終了
# write
with open("TkEasyGUI/version.py", "w", encoding="utf-8") as f:
    f.write(f"""\
# pylint: disable=line-too-long
\"\"\"
# TkEasyGUI version {version}

audo generated from [pyproject.toml](https://github.com/kujirahand/tkeasygui-python/blob/main/pyproject.toml) by update_version.py
\"\"\"
__version__ = \"{version}\"
""")
print(version)
