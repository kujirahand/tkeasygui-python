#!/bin/sh

echo "[Package]"
echo "https://packaging.python.org/en/latest/tutorials/packaging-projects/"

# make manual
echo "--- makedoc.sh ---"
./makedoc.sh

# clean
rm -f -r dist
rm -f -r tkeasygui.egg-info
python3 -m pip uninstall -y tkeasygui

# build
echo "--- build ---"
python3 -m build

# test install
echo "--- upload test repo ---"
python3 -m twine upload --repository testpypi dist/* --verbose
echo "--- wait ---"
sleep 3
echo "--- install test repo ---"
python3 -m pip install -U --index-url https://test.pypi.org/simple/ --no-deps tkeasygui

echo "--- upload pypi ---"
echo "[TRY]: python3 -m twine upload dist/* --verbose"


