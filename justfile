# TkEasyGUI task runner
SRC := "TkEasyGUI"

# Install TkEasyGUI in editable mode
install:
    python -m pip uninstall -y TkEasyGUI
    python -m pip install -e .

# Install development dependencies
install-dev:
    python -m pip install -U pip setuptools wheel twine
    python -m pip install -r requirements.txt
    python -m pip install pylint black isort mypy

# Run linters and formatters check
lint:
    ruff check
    pylint {{SRC}}
    black --check {{SRC}}
    mypy {{SRC}}

# Format code using black
format:
    black {{SRC}} tests/

# Check formatting using black
format-check:
    black --check {{SRC}} tests/

# Format and run linters
lint-and-format:
    black {{SRC}} tests/
    pylint {{SRC}}
    mypy {{SRC}}

# Update version and generate documentation
doc:
    python update_version.py
    python makedoc.py
    python docs/scripts/readme_maker.py
    @echo "ok"

# Build documentation (alias for doc)
build-docs: doc

# Update version in files
version:
    python update_version.py

# Clean build and temporary files
clean:
    @echo "=== clean ==="
    rm -rf dist
    rm -rf TkEasyGUI.egg-info
    rm -rf TkEasyGUI/__pycache__
    rm -rf TkEasyGUI/TkEasyGUI.egg-info

# Print the directory containing the justfile
print-script-dir:
    @echo {{justfile_directory()}}

# Build package without deploying
deploy-build-only: clean build-docs
    python -m build

# Deploy to TestPyPI
deploy-test:
    python -m pip install build twine
    just deploy-build-only
    python -m twine upload --repository testpypi dist/* --verbose
    @echo "[TRY] task install test"

# Deploy to PyPI
deploy-main:
    python -m pip install build twine
    just deploy-build-only
    python -m twine upload dist/* --verbose

# Create package
package:
    @echo "=== MAKE PACKAGE ==="
    # ------------------
    just deploy-build-only
    # ------------------
    just clean
    @echo "* uninstall TkEasyGUI"
    python -m pip uninstall -y TkEasyGUI
    # ------------------
    just build-docs
    # ------------------
    @echo "* update_version"
    python update_version.py
    # ------------------
    @echo "* build"
    python -m build

# Package and deploy to TestPyPI
package-test:
    # ------------------
    just package
    python -m twine upload --repository testpypi dist/* --verbose
    # ------------------
    @echo "* install test pypi"
    @echo "[TRY]: python -m pip install -U --index-url https://test.pypi.org/simple/ --no-deps TkEasyGUI"

# Package and publish to PyPI
package-publish:
    # ------------------
    just package
    @echo "* publish"
    python -m twine upload dist/* --verbose
    # ------------------
    @echo "* install pypi"
    @echo "[TRY]: python -m pip install -U TkEasyGUI"

# Run file viewer test
run:
    python tests/file_viewer.py

# Check codebase quality
check:
    ruff check TkEasyGUI/*.py
    mypy TkEasyGUI/*.py

# Test TkEasyGUI elements
test_elements:
    python element2json.py
    python elements_test.py

# Run tests with pytest
test:
    python -m pytest
