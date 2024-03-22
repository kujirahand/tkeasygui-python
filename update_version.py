# pyprojet.tomlを見てパッケージのバージョンを更新する
# 使い方: python update_version.py

import toml
# read
with open("pyproject.toml", "r", encoding="utf-8") as f:
    data = toml.load(f)
version = data["project"]["version"]
versions = version.split(".")
if int(versions[1]) == 0 or int(versions[2]) == 0:
    print("BROKEN VERSION!!")
    quit()
# write
with open("tkeasygui/tkeasygui_version.py", "w", encoding="utf-8") as f:
    f.write(f"# TkEasyGUI version\n__version__ = \"{version}\"\n")
print(version)
