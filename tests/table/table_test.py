"""Table Test Example"""

import TkEasyGUI as eg

data = [
    ["名前", "年齢", "住所"],
    ["山田", "25", "東京"],
    ["鈴木", "30", "大阪"],
    ["佐藤", "35", "名古屋"],
    ["山田", "25", "東京"],
    ["鈴木", "30", "大阪"],
    ["佐藤", "35", "名古屋"],
    ["山田", "25", "東京"],
    ["鈴木", "30", "大阪"],
    ["佐藤", "35", "名古屋"],
    ["山田", "25", "東京"],
]

# create window
layout = [
    [
        eg.Table(
            key="-table-",
            values=data[1:],  # テーブルに表示するデータ(ヘッダ行を含まない)を指定
            headings=data[0],  # ヘッダ行を指定
            expand_x=True,  # ウィンドウのX方向にサイズを合わせる
            expand_y=True,  # ウィンドウのY方向にサイズを合わせる
            justification="center",  # セルを中央揃えにする
            auto_size_columns=True,  # 自動的にカラムを大きくする
            max_col_width=30,  # 最大カラムサイズを指定
            enable_events=True,  # イベントを有効にする
            font=("Arial", 14),
        )
    ],
    [eg.Button("Close", expand_x=True), eg.Button("Update")],
]
win = eg.Window("Table test", layout)
# event loop
while True:
    event, values = win.read()
    print(event, values)
    if event == eg.WIN_CLOSED:
        break
    if event == "Close":
        break
    if event == "Update":
        win["-table-"].update([["aaa", "bbb", "ccc"], ["ddd", "eee", "fff"]])
win.close()
