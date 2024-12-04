import glob
import inspect
import json
import os
import re
import types

import TkEasyGUI as eg

SCRIPT_DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "docs", "TkEasyGUI")
DOCS_SCRIPTS_DIR = os.path.join(SCRIPT_DIR, "docs", "scripts")
REPO = "https://github.com/kujirahand/tkeasygui-python/blob/main"
def main():
    package_path = eg.__path__[0]
    print(package_path)
    # print(eg.__doc__)
    root_name = eg.__package__

    # get modules
    files = glob.glob(os.path.join(package_path, "*.py"))
    for file in files:
        read_module(file, root_name)

def read_module(file: str, root_name: str) -> None:
    module_name = os.path.basename(file).replace(".py", "")
    if module_name == "__init__":
        return
    mod = getattr(eg, module_name)
    doc = trim_docstring(str(mod.__doc__))
    print("---------------------------")
    output_file = os.path.join(OUTPUT_DIR, f"{module_name}-py.md")
    result = ""
    head = f"# Module {root_name}.{module_name}\n\n"
    head += doc + "\n\n"
    head += "---------------------------\n\n"
    print(head)
    head_link = []
    # classes
    elements = []
    classes = ""
    for prop in dir(mod):
        if prop.startswith("__"):
            continue
        p = getattr(mod, prop)
        if type(p) is type:
            mod2 = inspect.getmodule(p)
            if mod2 != mod:
                continue
            pclass = p
            class_name = pclass.__name__
            doc = trim_docstring(p.__doc__)
            classes += f"## {prop}\n\n"
            classes += doc + "\n\n"
            elements.append(class_name)
            # get init code
            if p.__init__ is not None:
                print("@@@", prop)
                code_def = get_function_definition(p.__init__, skip_self=True)
                code_def = re.sub("^def __init__", f"class {class_name}", code_def)
                code_def = re.sub(r"->\s*None\s*:", "", code_def)
                if prop == "Button":
                    print("@@@", code_def)
                    # print(inspect.getsource(p.__init__))
                if code_def != "":
                    classes += "```py\n"
                    classes += code_def
                    classes += "```\n\n"
                    code = p.__init__.__code__
                    fname = code.co_filename.replace(SCRIPT_DIR, "")
                    classes += f"- [source]({REPO}{fname}#L{code.co_firstlineno})\n"
                    classes += "\n"
            # get methods
            method_doc = ""
            method_link = []
            methods = inspect.getmembers(pclass)
            for name, method in methods:
                if name.startswith("_"):
                    continue
                print("###", class_name, name)
                method_doc += f"### {class_name}.{name}\n\n"
                doc = trim_docstring(method.__doc__)
                if doc.strip() != "":
                    method_doc += doc.strip() + "\n\n"
                if type(p) is not types.FunctionType:
                    continue
                def_code = get_function_definition(method, skip_self=True)
                method_doc += "```py\n"
                method_doc += def_code
                method_doc += "```\n\n"
                method_doc += f"- [source]({REPO}{fname}#L{code.co_firstlineno})\n"
                method_doc += "\n"
                method_link.append(f"- [{name}](#{class_name.lower()}{name.lower()})")
            if method_doc != "":
                classes += f"### Methods of {class_name}\n\n"
                classes += "\n".join(method_link) + "\n\n"
                classes += method_doc
    if classes:
        result += f"# Classes of {root_name}.{module_name}\n\n"
        if module_name == "widgets":
            class_link = []
            for class_name in elements:
                class_link.append(f"- [{class_name}](#{class_name.lower()})")
            result += "\n".join(class_link) + "\n\n"
        result += classes
        head_link.append(f"- [Classes](#classes-of-{root_name.lower()}{module_name.lower()})")
    # elements
    if len(elements) > 0 and module_name == "widgets":
        print("* elements:\n", elements)
        if "Window" in elements:
            elements.remove("Window")
        if "Element" in elements:
            elements.remove("Element")
        if "TkEasyError" in elements:
            elements.remove("TkEasyError")
        file_elements = os.path.join(DOCS_SCRIPTS_DIR, "elements.json")
        with open(file_elements, "w", encoding="utf-8") as fp:
            elements = list(sorted(elements))
            json.dump(elements, fp, ensure_ascii=False, indent=2)

    # functions
    functions = ""
    function_link = []
    for prop in dir(mod):
        if prop.startswith("_"):
            continue
        p = getattr(mod, prop)
        if type(p) is types.FunctionType:
            doc = trim_docstring(p.__doc__)
            code = p.__code__
            def_code = get_function_definition(p)

            fname = code.co_filename.replace(SCRIPT_DIR, "")
            functions += f"## {prop}\n\n"
            functions += doc + "\n\n"
            functions += "```py\n"
            functions += def_code
            functions += "```\n\n"
            functions += f"- [source]({REPO}{fname}#L{code.co_firstlineno})\n"
            functions += "\n"
            function_link.append(f"- [{prop}](#{prop.lower()})")
    if functions:
        result += f"# Functions of {root_name}.{module_name}\n\n"
        result += "\n".join(function_link) + "\n\n"
        result += functions
        head_link.append(f"- [Functions](#functions-of-{root_name.lower()}{module_name.lower()})")

    print("---------------------------")
    result = head + "\n".join(head_link) + "\n\n" + result
    # print(result)
    with open(output_file, "w", encoding="utf-8") as fp:
        fp.write(result)

def trim_docstring(doc):
    """docstringのインデントを整形する"""
    if not doc or doc == "":
        return ""
    lines = doc.expandtabs().splitlines()
    indent = 0
    stripped = ""
    for line in lines:
        if line.strip() == "":
            continue
        stripped = line.lstrip()
        if stripped:
            indent = line.find(stripped)
            break
    trimmed = [lines[0].strip()] 
    for line in lines[1:]:
        trimmed.append(line[indent:].rstrip())
    res = "\n".join(trimmed).strip()
    return res

def get_function_definition(func, skip_self=False):
    """関数の定義部分を取得する"""
    # 関数のソースコードを取得
    src = str(inspect.getsource(func))
    src = src.strip()
    res = []
    flag = False
    lines = src.split("\n")
    for line in lines:
        if not flag:
            if line.startswith("@"):
                flag = True
            if line.startswith("def "):
                flag = True
        if not flag:
            continue
        line = line.rstrip()
        if line != "" and line[0] == " ":
            line = "    " + line.strip()
        res.append(line)
        if line.endswith(":"):
            break
    return "\n".join(res).strip() + "\n"

if __name__ == "__main__":
    main()
