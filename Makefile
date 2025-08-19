# TkEasyGUI task runner

SRC=TkEasyGUI

.PHONY: install lint format clean

install:
	pip install -U pip setuptools wheel
	pip install -r requirements.txt
	pip install pylint black isort mypy

lint:
	pylint $(SRC)
	black --check $(SRC)
	isort --check-only $(SRC)

format:
	black $(SRC)
	isort $(SRC)

clean:
	rm -rf TkEasyGUI.egg-info TkEasyGUI/__pycache__ TkEasyGUI/TkEasyGUI.egg-info


