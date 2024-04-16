# TkEasyGUI - Installation troubles

### (ja) インストールのトラブルについて

- 0.2.24以降、パッケージ名が、全部小文字の`tkeasygui`から大文字込みの`TkEasyGUI`に変わりました。
  - その影響で古いバージョンからアップデートしようとすると、`ModuleNotFoundError: No module named 'TKEasyGUI'`というエラーが発生します。
  - これを防ぐために、`pip uninstall tkeasygui`実行後に、下記のPythonコードをIDLEやREPL(`python`コマンドで起動するインタプリタ)で実行してください。
  - その後、`pip install TkEasyGUI`を実行して最新版をインストールしてください。
  
```py:remove_old_package.py
# 古いTkEasyGUIパッケージを完全に削除するプログラム
import os, shutil, PIL
packages = os.path.dirname(PIL.__path__[0])
old_package = os.path.join(packages, "tkeasygui")
print(f"Remove: {old_package}")
if os.path.exists(old_package): shutil.rmtree(old_package)
print("ok")
```

### 上記手順がうまくいかない場合

(1) 一度、TkEasyGUIがインストールできるか確認しましょう。

```sh
python -m pip install tkeasygui
```

(2) 続いて、インストールパスを調べます。

```sh
python -m pip show tkeasygui
```

(3) 表示された情報の中に下記のようなLocation情報があります。

```
Location: C:\Users\<username>\AppData\Local\Programs\Python\Python312\Lib\site-packages
```

(4) そこで、エクスプローラーかFinderを使って、上記フォルダを開きます。

(5) ターミナル(PowerShell/ターミナル.app)を開いて、下記のコマンドを実行して、一度、古いtkeasyguiを削除します。

```sh
pip uninstall tkeasygui
```

(6) site-packages以下にある「tkeasygui」フォルダを完全に削除します。

(7) その後で、改めて、TkEasyGUIをインストールします。

```sh
pip install TkEasyGUI
```


### (en) Installation troubles

- From version 0.2.24, the package name has also been changed from `tkeasygui` to `TkEasyGUI`.
  - Updating from older versions (less than 0.2.24) will fail. 
  - If you have used a previous version, you will see `ModuleNotFoundError: No module named 'TKEasyGUI'`.
  - Please run the command below to completely remove the old `tkeasygui` package.
  - It seems that cache files remain even if you use the `pip uninstall tkeasygui` command.
  - Start the `python` command or `IDLE` and execute the following command.
  - Then run `pip install TkEasyGUI` to install the latest version.

```py:remove_old_package.py
# remove old package directory
import os, shutil, PIL
packages = os.path.dirname(PIL.__path__[0])
old_package = os.path.join(packages, "tkeasygui")
print(f"Remove: {old_package}")
if os.path.exists(old_package): shutil.rmtree(old_package)
print("ok")
```
