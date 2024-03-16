from setuptools import setup # skip
import tkeasygui

DESCRIPTION: str = "A simple wrapper around tkinter for easy GUI creation."
NAME: str = "tkeasygui"
AUTHOR: str = "kujirahand"
AUTHOR_EMAIL: str = "web@kujirahand.com"
URL: str = "https://github.com/kujirahand/tkeasygui-python"
LICENSE: str = "MIT"
DOWNLOAD_URL: str = "https://github.com/kujirahand/tkeasygui-python"
VERSION: str = tkeasygui.__version__
PYTHON_REQUIRES: str = ">=3.8"
INSTALL_REQUIRES: list[str] = []
EXTRAS_REQUIRE:dict[str, str] = {}
PACKAGES: list[str] = ["tkeasygui"]
CLASSIFIERS: list[str] = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Software Development :: User Interfaces",
]

with open("README.md", "r", encoding="utf-8") as fp:
    readme = fp.read()
long_description = readme

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    license=LICENSE,
    url=URL,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=PACKAGES,
    classifiers=CLASSIFIERS
)
