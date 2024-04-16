# TkEasyGUI

`TkEasyGUI`は、PythonでのGUIアプリケーション開発の敷居を大幅に下げるライブラリです。`Tkinter`のような従来のUIライブラリが持つ複雑さを解消し、より多くの開発者がGUIアプリの開発を楽しめます。本ライブラリは、簡単にGUIを構築できるライブラリ`PySimpleGUI`の概念を引き継ぎつつ、独自の機能を追加しています。

- [👉English](https://github.com/kujirahand/tkeasygui-python/blob/main/README.md)

## TkEasyGUIの特徴:

- `TkEasyGUI`は、GUIアプリケーションを簡単かつシンプルに作成することができるPythonライブラリです。
- イベントモデルでは、よく知られたGUIライブラリ`PySimpleGUI`と互換性があります。
- Pythonの標準UIライブラリ`Tkinter`は、学習障壁が高と考えられていますが、このライブラリを使用すると、GUIアプリケーションを直感的に作成できます。
- ライセンスには比較的緩い`MITライセンス`を採用しています。将来このライセンスを変えることはありません。

## 対象プラットフォーム

- Windows / macOS / Linux (Tkinterが動く環境)

## インストール:

pypiからインストールします。

```sh
python -m pip install TkEasyGUI
```

GitHubリポジトリからインストールします。

```sh
python -m pip install git+https://github.com/kujirahand/tkeasygui-python
```

- (memo) v0.2.24未満のバージョンからのインストールに失敗する場合があります。その場合、[こちら](docs/installation_trouble.md)を確認してください。

## 簡単な使い方

ラベルとボタンのみを持つシンプルなウィンドウを作成するには、以下のように記述します。

```py
import TkEasyGUI as eg
# define layout
layout = [[eg.Text("Hello, World!")],
          [eg.Button("Exit")]]
# create a window
with eg.Window("test", layout) as window:
    # event loop
    for event, values in window.event_iter():
        if event == "Exit":
            eg.popup("Thank you.")
            break
```

PySimpleGUIと同じイベントモデルの使い勝手で記述できます。

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

## サンプル

簡単な使い方を示すサンプルを揃えました。確認してみてください。

- [samples](https://github.com/kujirahand/tkeasygui-python/tree/main/tests).

`tests/file_viewer.py`を実行することで、すべてのサンプルを手軽に起動できます。

## ドキュメント

ライブラリの詳細なクラスやメソッドの一覧です。

- [docs](https://github.com/kujirahand/tkeasygui-python/tree/main/docs)

## PySimpleGUIとの関係について

- 基本機能を使う場合、PySimpleGUIと互換性があります。PySimpleGUIと同じイベントモデルでプログラムを記述できます。
- 基本的なGUI部品の名前も同じにしてあります。しかし、いくつかのプロパティの名前が異なっていますが、多くの独自機能が実装されています。
- 本プロジェクトは、PySimpleGUIの存在を意識して開発しましたが、完全にゼロから実装しています。ライセンス的にも問題はありません。

PySimpleGUIと完全な互換性は考えていません。

### TkEasyGUI独自の機能

- for文と `window.event_iter()` を使って気軽にイベント処理が可能
- 色選択ダイアログ(eg.popup_color)など、独自のポップアップダイアログを用意
- ImageはPNGだけでなくJPEGも読み込み可能
- 便利なイベントフックや一括イベント登録機能 - [docs/custom_events](docs/custom_events.md)
- テキストボックス(Muliline/Input)に便利なCopy/Paste/Cutなどのメソッドを追加
- OSの配色をデフォルトで利用

## リンク

- [pypi.org > TkEasyGUI](https://pypi.org/project/tkeasygui/)
- [GitHub > TkEasyGUI](https://github.com/kujirahand/tkeasygui-python/)

## TkEasyGUIパッケージ開発者用のツール

全てのElementを列挙して、`elements_test.py`を生成するツール:

```sh
./element2json.py
```

## 今後の予定

- sg.MulitilineBrowse
- Window作成時の配置モード
  - 絶対座標でのElementの配置 / Gridレイアウト
  - HTMLっぽく？一次元のElementの配置 eg.Window(layout=[eg.Button(), eg.Button(), eg.BR(), eg.Button()])
- test --- Window.readでイベントの値を読むが、更新されていないものがないか、チェックする
