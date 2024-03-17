# foramt documents script
import os
import glob
import re
SCRIPT_DIR = os.path.dirname(__file__)
DOCS_DIR = os.path.join(SCRIPT_DIR, "tkeasygui")
print(DOCS_DIR)
# 指定のディレクトリ以下のmdファイルを列挙
files = glob.glob(os.path.join(DOCS_DIR, "*.md"), recursive=True)
for f in files:
    print("===", f, "===")
    result = []
    with open(f, "r", encoding="utf-8") as fp:
        text = fp.read()
        lines = text.split("\n")
        for line in lines:
            # (ex) ### ask_ok_cancel {: #ask_ok_cancel }
            r = re.match(r'^(###{0,3}) ([a-zA-Z_\.\-\s]+) \{\:.+\}', line)
            if r:
                result.append(f"{r[1]} {r[2]}")
                continue
            # (ex) [**close**](#Window.close){: #Window.close }
            r = re.match(r'^\[\*\*.+\*\*\]\(\#([a-zA-Z\.\_\-]+)\)', line)
            if r:
                result.append(f"##### {r[1]}")
                continue
            result.append(line)
    # save
    sss = "\n".join(result)
    with open(f, "w", encoding="utf-8") as fp:
        fp.write(sss)

