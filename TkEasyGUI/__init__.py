"""
TkEasyGUI - A simple GUI library for Python using tkinter.
"""

from .version import __version__
from .utils import *  # noqa: F403
from .widgets import *  # noqa: F403
from .dialogs import *  # noqa: F403

if __name__ == "__main__":
    print(__doc__)
    print("Version: ", __version__)
