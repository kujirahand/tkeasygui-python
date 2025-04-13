# TkEasyGUI

`TkEasyGUI`は、**Pythonで最も簡単にGUIアプリが開発できるライブラリ**です。`Tkinter`のような従来のUIライブラリが持つ複雑さを解消し、シンプルな使い勝手を実現しました。手軽に使える豊富なダイアログを用意しています。本ライブラリは、簡単にGUIを構築できるライブラリ`PySimpleGUI`の概念を引き継ぎつつ、独自の機能を追加しています。

- [👉English](https://github.com/kujirahand/tkeasygui-python/blob/main/README.md)

## TkEasyGUIの特徴:

- `TkEasyGUI`は、GUIアプリケーションを簡単かつシンプルに作成することができるPythonライブラリです。
- Pythonの標準UIライブラリ`Tkinter`は、学習障壁が高いと考えられていますが、このライブラリを使用すると、GUIアプリケーションを直感的に作成できます。
- イベントモデルや基本部品では、よく知られたGUIライブラリ`PySimpleGUI`と互換性があります。
- 型ヒントに対応しているので、コード補完でプロパティを選択できます。(本パッケージの利用には、`Python 3.9以降`が必要です。)
- ライセンスには比較的緩い`MITライセンス`を採用しています。将来このライセンスを変えることはありません。

## 対象プラットフォーム

- Windows / macOS / Linux (Tkinterが動く環境)

## インストール:

[PyPI](https://pypi.org/project/TkEasyGUI/)からインストールできます。

```sh
python -m pip install TkEasyGUI
```

[GitHubリポジトリ](https://github.com/kujirahand/tkeasygui-python)からインストールできます。

```sh
python -m pip install git+https://github.com/kujirahand/tkeasygui-python
```

- (メモ) v0.2.24未満からのアップデートに失敗する場合は[こちら](docs/installation_trouble.md)を確認してください。

## 簡単な使い方 - ポップアップダイアログを使う

TkEasyGUIの使い方は簡単です。もし、ダイアログにメッセージを表示したい場合、次のように記述します。

```py
import TkEasyGUI as eg
eg.print("A joyful heart is good medicine.")
```

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/sample1.png" width="300" alt="TkEasyGUI">


入力ボックス付きのダイアログで尋ねることもできます。次のコードは、名前を尋ねて、続くダイアログに名前を表示します。

```py
import TkEasyGUI as eg
name = eg.input("What is your name?")
eg.print(f"Hello, {name}.")
```

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/sample2.png" width="300" alt="TkEasyGUI">

さらに、複数入力が可能なフォームダイアログも手軽に表示できます。

```py
import TkEasyGUI as eg
# フォームダイアログを表示
form = eg.popup_get_form(["名前", "年齢", "趣味"], title="プロフィールの入力")
if form:
    name = form["名前"]
    age = form["年齢"]
    hobbies = form["趣味"]
    eg.print(f"name={name}, age={age}, hobby={hobbies}")
```

<img src="https://github.com/kujirahand/tkeasygui-python/raw/main/docs/image/sample3.png" width="300" alt="TkEasyGUI">

### バラエティ豊かなダイアログを提供

`TkEasyGUI` はさまざまなダイアログを提供します。
たとえば、色選択ダイアログ、ファイル選択ダイアログ、カレンダーダイアログなどです。

- [Docs > Dialogs](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/dialogs-py.md)


## 簡単な使い方 - カスタムウィンドウを定義して使う

ラベルとボタンのみを持つシンプルなウィンドウを作成するには、以下のように記述します。`with`文を使うことで、イベントループを抜けると自動的にウィンドウが閉じるように指定できます。

```py
import TkEasyGUI as eg
# 画面レイアウトの定義
layout = [
    [eg.Text("Hello, World!")],
    [eg.Button("OK")]
]
# ウィンドウを表示する
with eg.Window("Hello App", layout) as window:
    # イベントループを処理する
    for event, values in window.event_iter():
        if event == "OK":
            eg.print("Thank you.")
            break # ループを抜ける
```

有名GUIライブラリの`PySimpleGUI`と同じイベントモデルの使い勝手で記述できます。（多くのGUI部品でPySimpleGUIと互換性を持たせています。）

```py
import TkEasyGUI as eg
# define layout
layout = [[eg.Text("Hello, World!")],
          [eg.Button("Exit")]]
# create a window
window = eg.Window("test", layout)
# event loop
while True:
    event, values = window.read()
    if event in ["Exit", eg.WINDOW_CLOSED]:
        eg.popup("Thank you.")
        break
# close window
window.close()
```

- [Docs > どんなElementが使えますか？](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/README.md#tkeasygui-elements-list)

## チュートリアル

- [TkEasyGUI - Pythonで最も素早くデスクトップアプリを創るライブラリ](https://note.com/kujirahand/n/n33a2df3aa3e5)
- [マイナビニュースPython連載116回目 - 合計/整形/コピーのツールを作ろう](https://news.mynavi.jp/techplus/article/zeropython-116/)
- [(書籍) Pythonでつくるデスクトップアプリ メモ帳からスクレイピング・生成AI利用まで](https://amzn.to/45R2NSH)
- [(特集記事) 日経ソフトウエア2025年5月号の特集記事 - TkEasyGUIを使ってみよう](https://amzn.to/4j1lj0c)

公式ではないですが、役立つ技術記事があります！

- [TkEasyGUI - 目的別ダイアログ完全ガイド](https://note.com/sirodon_256/n/n4138ebf4877f)
- [TkEasyGUIライブラリの基本とサンプルコード解説](https://note.com/sirodon_256/n/na73d3fdac68d)

## サンプル

簡単な使い方を示すサンプルを揃えました。確認してみてください。

- [samples](https://github.com/kujirahand/tkeasygui-python/tree/main/tests).

`tests/file_viewer.py`を実行することで、すべてのサンプルを手軽に起動できます。

## ドキュメント

ライブラリの詳細なクラスやメソッドの一覧です。

- [マニュアル](https://github.com/kujirahand/tkeasygui-python/tree/main/docs)
  - [ダイアログの一覧](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/dialogs-py.md)
  - [カスタム要素の一覧](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/widgets-py.md)
  - [便利なユーティリティ関数群](https://github.com/kujirahand/tkeasygui-python/blob/main/docs/TkEasyGUI/utils-py.md)

## PySimpleGUIとの互換性について

- 基本機能を使う場合、PySimpleGUIと互換性があります。PySimpleGUIと同じイベントモデルでプログラムを記述できます。
- 基本的なGUI部品の名前も同じにしてありますが、いくつかのプロパティ名は異なります。
- TkEasyGUIは完全にゼロから実装しなおしており、MITライセンスを採用しています。
- ただし、PySimpleGUIと完全な互換性は考えていません。

### TkEasyGUI独自の機能

- for文と `window.event_iter()` を使って気軽にイベント処理が可能
- 任意のボタンを持つダイアログ(`eg.popup_buttons`)や色選択ダイアログ(`eg.popup_color`)、複数項目を入力するダイアログ(`eg.popup_get_form`)など、独自のポップアップダイアログを用意
- ImageはPNGだけでなくJPEGも読み込み可能
- 便利なイベントフックや一括イベント登録機能 - [docs/custom_events](docs/custom_events.md)
- テキストボックス(Muliline/Input)に便利なCopy/Paste/Cutなどのメソッドを追加

## リンク

- [pypi.org > TkEasyGUI](https://pypi.org/project/tkeasygui/)
- [GitHub > TkEasyGUI](https://github.com/kujirahand/tkeasygui-python/)
- [Discord > TkEasyGUI](https://discord.gg/NX8WEQd42S)

