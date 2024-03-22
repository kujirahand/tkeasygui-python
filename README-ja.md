# TkEasyGUI

`TkEasyGUI`は、PythonでのGUIアプリケーション開発の敷居を大幅に下げるライブラリです。`Tkinter`のような従来のUIライブラリが持つ複雑さを解消し、より多くの開発者がGUIアプリの開発を楽しめます。本ライブラリは、簡単にGUIを構築できるライブラリ`PySimpleGUI`の概念を引き継ぎつつ、独自の機能を追加しています。

## TkEasyGUIの特徴:

- `TkEasyGUI`は、GUIアプリケーションを簡単かつシンプルに作成することができるPythonライブラリです。
- イベントモデルでは、よく知られたGUIライブラリ`PySimpleGUI`と互換性があります。
- Pythonの標準UIライブラリ`Tkinter`は、学習障壁が高と考えられていますが、このライブラリを使用すると、GUIアプリケーションを直感的に作成できます。
- ライセンスには比較的緩い`MITライセンス`を採用しています。将来このライセンスを変えることはありません。

## インストール:

pypiからインストールします。

```sh
python -m pip install tkeasygui
```

GitHubリポジトリからインストールします。

```sh
python -m pip install git+https://github.com/kujirahand/tkeasygui-python
```

## 簡単な使い方

ラベルとボタンのみを持つシンプルなウィンドウを作成するには、以下のように記述します。

```py
import tkeasygui as eg

# ウィンドウの作成
layout = [
    [eg.Text("Hello, World!")],
    [eg.Button("OK")]
]
window = eg.Window("Hello", layout=layout)

# イベントループ
while window.is_alive():
    # イベントの取得
    event, values = window.read()
    # イベントの確認
    if event == "OK":
        eg.popup("Pushed OK Button")
        break
window.close()
```

## サンプル

簡単な使い方を示すサンプルを取りそろえています。確認してみてください。

- [samples](https://github.com/kujirahand/tkeasygui-python/tree/main/tests).

## ドキュメント

ライブラリの詳細なクラスやメソッドの一覧です。

- [docs](https://github.com/kujirahand/tkeasygui-python/tree/main/docs)

## PySimpleGUIとの関係について

基本的に、PySimpleGUIと互換性があります。それと同じイベントモデルでプログラムを記述できます。
なお、PySimpleGUIを参考に開発されましたが、ゼロから再実装されています。多くの独自の機能が拡張されています。
基本的なElementも同じ名前にしてあります。しかし、いくつかのプロパティの名前が異なっています。

PySimpleGUIと完全な互換性は考えていません。

## リンク

- [pypi.org > TkEasyGUI](https://pypi.org/project/tkeasygui/)
- [GitHub > TkEasyGUI](https://github.com/kujirahand/tkeasygui-python/)


## 今後の予定

- sg.ListBrowse (select item from listbox)
- sg.MulitilineBrowse
- Window作成時の配置モード
- 絶対座標でのElementの配置 / Gridレイアウト
- HTMLっぽく？一次元のElementの配置 eg.Window(layout=[eg.Button(), eg.Button(), eg.BR(), eg.Button()])
- test --- Window.readでイベントの値を読むが、更新されていないものがないか、チェックする
- test --- fontを自動的に全部適用する設定にしたので、すべてのエレメントが実行できるかテスト
- widgets.pyからElementを継承しているものを列挙して、全部を配置して作るテスト
