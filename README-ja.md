# TkEasyGUI

`TkEasyGUI`は、PythonでのGUIアプリケーション開発の敷居を大幅に下げるライブラリです。`Tkinter`のような従来のUIライブラリが持つ複雑さを解消し、より多くの開発者がGUIアプリの開発を楽しめます。本ライブラリは、簡単にGUIを構築できるライブラリ`PySimpleGUI`の概念を引き継ぎつつ、独自の機能を追加しています。

## TkEasyGUIの特徴:

- `TkEasyGUI`は、GUIアプリケーションを簡単かつシンプルに作成することができるPythonライブラリです。
- イベントモデルでは、よく知られたGUIライブラリ`PySimpleGUI`と互換性があります。
- Pythonの標準UIライブラリ`Tkinter`は、学習障壁が高と考えられていますが、このライブラリを使用すると、GUIアプリケーションを直感的に作成できます。
- ライセンスには比較的緩い`MITライセンス`を採用しています。

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

## リンク

- [pypi.org > TkEasyGUI](https://pypi.org/project/tkeasygui/)
- [GitHub > TkEasyGUI](https://github.com/kujirahand/tkeasygui-python/)

