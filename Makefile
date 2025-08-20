# TkEasyGUI task runner

SRC=TkEasyGUI
SCRIPT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

.PHONY: install install-dev lint format clean check

install:
	pip install -e .

install-dev:
	pip install -U pip setuptools wheel twine
	pip install -r requirements.txt
	pip install pylint black isort mypy

lint:
	pylint $(SRC)
	black --check $(SRC)
	isort --check-only $(SRC)
	ruff check
	mypy TkEasyGUI/

format:
	black $(SRC)
	isort $(SRC)

build-docs:
	python update_version.py
	python makedoc.py
	python docs/scripts/readme_maker.py
	@echo "ok"

clean:
	@echo "=== clean ==="
	cd $(SCRIPT_DIR)
	rm -f -r dist
	rm -f -r TkEasyGUI.egg-info
	rm -f -r TkEasyGUI/__pycache__ 
	rm -f -r TkEasyGUI/TkEasyGUI.egg-info

print-script-dir:
	@echo $(SCRIPT_DIR)

deploy-build-only:
	make clean
	make build-docs
	python -m build

deploy-test:
	make deploy-build-only
	python -m twine upload --repository testpypi dist/* --verbose
	@echo "[TRY] task install test"

deploy-main:
	make deploy-build-only
	python -m twine upload dist/* --verbose

package:
	@echo "=== MAKE PACKAGE ==="
	# ------------------
	make clean
	@echo "* uninstall TkEasyGUI"
	python -m pip uninstall -y TkEasyGUI
	# ------------------
	@echo "* build-docs"
	make build-docs
	# ------------------
	@echo "* update_version"
	python update_version.py
	# ------------------
	@echo "* build"
	python -m build

package-test:
	# ------------------
	make package
	python -m twine upload --repository testpypi dist/* --verbose
	# ------------------
	@echo "* install test pypi"
	@echo "[TRY]: python -m pip install -U --index-url https://test.pypi.org/simple/ --no-deps TkEasyGUI"

package-publish:
	# ------------------
	make package
	@echo "* publish"
	python -m twine upload dist/* --verbose
	# ------------------
	@echo "* install pypi"
	@echo "[TRY]: python -m pip install -U TkEasyGUI"

run:
	cd $(SCRIPT_DIR)
	python tests/file_viewer.py


check:
	cd $(SCRIPT_DIR)
	ruff check TkEasyGUI/*.py
	mypy TkEasyGUI/*.py
