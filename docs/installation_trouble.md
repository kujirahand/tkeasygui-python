# TkEasyGUI - Installation troubles

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
shutil.rmtree(old_package)
```

### (ja) インストールのトラブルについて

- 0.2.24以降、パッケージ名が、全部小文字の`tkeasygui`から大文字込みの`TkEasyGUI`に変わりました。
  - その影響で古いバージョンからアップデートしようとすると、`ModuleNotFoundError: No module named 'TKEasyGUI'`というエラーが発生します。これを防ぐために、上記のPythonコードをIDLEやREPL(`python`コマンドで起動するインタプリタ)で実行してください。
  - その後、`pip install TkEasyGUI`を実行して最新版をインストールしてください。
  
