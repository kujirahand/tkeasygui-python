# TkEasyGUI task runner

SRC=TkEasyGUI
SCRIPT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

.PHONY: install lint format clean

install:
	pip install -e .

install-dev:
	pip install -U pip setuptools wheel
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
	rm -rf TkEasyGUI.egg-info TkEasyGUI/__pycache__ TkEasyGUI/TkEasyGUI.egg-info

print-script-dir:
	@echo $(SCRIPT_DIR)

deploy-build-only:
	make build-docs
	python -m build
	rm -f -r dist
	rm -f -r tkeasygui.egg-info

deploy-test:
	make deploy-build-only
	python -m twine upload --repository testpypi dist/* --verbose
	@echo "[TRY] task install test"

deploy-main:
	make deploy-build-only
	python -m twine upload dist/* --verbose
