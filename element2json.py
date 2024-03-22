#!/usr/bin/env python
"""
Test all elements of tkeasygui
"""
import json
import re
import os
TEST_FILENAME="elements_test.py"
def read_file() -> str:
    with open("tkeasygui/widgets.py", "r", encoding="utf-8") as f:
        lines = f.readlines()
    lines_org = lines.copy()
    # Element
    elements = []
    while len(lines) > 0:
        line = lines.pop(0)
        # enum Element
        r = re.match(r"^class ([a-zA-Z]+)\(Element\)", line)
        if r:
            klass = r.group(1)
            elements.append(klass)
    # print(elements)
    elements2 = []
    pat_elements = "|".join(elements)
    pat_re = f"^class ([a-zA-Z]+)\({pat_elements}\)"
    lines = lines_org.copy()
    # print("***", pat_re)
    while len(lines) > 0:
        line = lines.pop(0).strip()
        if "class" not in line:
            continue
        # print("==", line)
        r = re.match(r"^class ([a-zA-Z]+)\((.+?)\)", line)
        if r:
            klass = r.group(1)
            pklass = r.group(2)
            class_name = klass
            # print("*", pklass)
            if pklass != "Element":
                if pklass in elements:
                    elements2.append(klass)
            continue
    # --- __init__ ---
    class_name = ""
    init_args = {}
    lines = lines_org.copy()
    while len(lines) > 0:
        line = lines.pop(0).strip()
        if ("class " in line) and ("(" in line):
            class_name = re.split(r"(\s+|\(|\))", line)[2]
            continue
        if "def __init__" not in line:
            continue
        # print("==", class_name, "=>")
        r = re.match(f"def __init__\((.+)", line)
        if r:
            # args
            args = r.group(1)
            if class_name not in init_args:
                init_args[class_name] = []
            if "layout:" in args:
                init_args[class_name].append("layout=[[]]")
            if "text:" in args:
                init_args[class_name].append("text='text'")
            if "title:" in args:
                init_args[class_name].append("title='title'")
            if "default_text:" in args:
                init_args[class_name].append("default_text='default_text'")
            # extra
            if class_name == "Button":
                init_args[class_name].append("button_text='OK'")
            if class_name == "Table":
                init_args[class_name].append("values=[[1,2,3],[4,5,6],[7,8,9]]")
                init_args[class_name].append("headings=['aaa', 'bbb', 'ccc']")
            if class_name == "Image":
                init_args[class_name].append("filename='a.png'")
                init_args[class_name].append("size=(100,100)")
            if class_name == "Canvas":
                init_args[class_name].append("size=(100,100)")
            if class_name == "Graph":
                init_args[class_name].append("size=(100,100)")
            if class_name == "Combo":
                init_args[class_name].append("values=['combo1', 'combo2', 'combo3']")
                init_args[class_name].append("default_value='combo1'")
    print(init_args)
    return [elements, elements2, init_args]
 
def make_json():
    elements, ex_elements, _ = read_file()
    print(elements)
    with open("docs/elements.json", "w", encoding="utf-8") as f:
        json.dump(elements + ex_elements, f, indent=4, ensure_ascii=False)

def make_code():
    elements, ex_elements, init_args = read_file()
    src = "import tkeasygui as eg\n\n" + \
            "layout = [\n"
    src += "    [\n"
    for i, e in enumerate(elements):
        args = init_args.get(e, [])
        args_s = ",".join(args)
        src += f"        eg.{e}({args_s}),\n"
        if i % 5 == 4:
            src += "    ],\n"
            src += "    [\n"
    src += "    ],\n"
    src += "]\n"
    src += """
window = eg.Window("Title", layout=layout, font=("Arial", 12))
while window.is_alive():
    event, values = window.read()
"""
    print(f"==={TEST_FILENAME}===")
    print(src)
    with open("elements_test.py", "w", encoding="utf-8") as f:
        f.write(src)
    os.system("python elements_test.py")
if __name__ == "__main__":
    make_json()
    make_code()
