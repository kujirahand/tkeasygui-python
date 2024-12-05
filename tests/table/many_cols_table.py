import TkEasyGUI as eg

# make dummy data
data = []
for row in range(500):
    rows = []
    for col in range(30):
        rows.append(f"@{row:03}x{col:03}")
    data.append(rows)

# create window
tbl = eg.Table(
    key="-table-",
    values=data[1:],  # テーブルに表示するデータ(ヘッダ行を含まない)を指定
    headings=data[0],  # ヘッダ行を指定
    expand_x=True,  # ウィンドウのX方向にサイズを合わせる
    expand_y=True,  # ウィンドウのY方向にサイズを合わせる
    justification="center",  # セルを中央揃えにする
    auto_size_columns=False,  # 自動的にカラムを大きくする
    max_col_width=30,  # 最大カラムサイズを指定
    enable_events=True,  # イベントを有効にする
    vertical_scroll_only=False,  # 垂直スクロールバーを表示する
    font=("Arial", 12),
)
layout = [[tbl], [eg.Button("Update", expand_x=True), eg.Button("Close")]]
# create window
win = eg.Window("Table test", layout, font=("Arial", 12), resizable=True, size=(800, 600))
is_fruits = False
# event loop
while True:
    event, values = win.read()
    print("@@@", event, values)
    if event == eg.WIN_CLOSED:
        break
    if event == "Close":
        break
    if event == "Update":
        if not is_fruits:
            tbl.load_from_file("fruits.csv", use_header=True)
        else:
            tbl.set_values(data[1:], data[0])
        is_fruits = not is_fruits
win.close()
