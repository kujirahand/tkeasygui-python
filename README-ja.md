# TkEasyGUI

`TkEasyGUI`は、PythonでのGUIアプリケーション開発の敷居を大幅に下げるライブラリです。`Tkinter`のような従来のUIライブラリが持つ複雑さを解消し、より多くの開発者がGUIアプリの開発を楽しめます。本ライブラリは、簡単にGUIを構築できるライブラリ`PySimpleGUI`の概念を引き継ぎつつ、独自の機能を追加しています。

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

### メモ - v0.2.24

- バージョン0.2.24から、パッケージ名も`tkeasygui`から`TkEasyGUI`と修正しました。
  - もし以前のバージョンを使ったことがある場合、`ModuleNotFoundError: No module named 'TKEasyGUI'`が表示されます。
  - うまくパッケージがインポートできなくなった場合、下記のコマンドを実行して、古い`tkeasygui`パッケージを完全に削除してください。
  - `python`コマンドや`IDLE`などを起動して以下のコマンドを実行してください。

```py:remove_old_package
# remove old package
import os, shutil, PIL
packages = os.path.dirname(PIL.__path__[0])
old_package = os.path.join(packages, "tkeasygui")
print(f"Remove: {old_package}")
shutil.rmtree(old_package)
```


## 簡単な使い方

ラベルとボタンのみを持つシンプルなウィンドウを作成するには、以下のように記述します。

```py
import TkEasyGUI as eg

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

### TkEasyGUI独自の機能

- 色選択ダイアログ(eg.popup_color)など、独自のポップアップ
- ImageはPNGだけでなくJPEGも読み込み可能
- OSの配色をデフォルトで利用
- 便利なイベントフックや一括イベント登録機能 - [docs/custom_events](docs/custom_events.md)

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
