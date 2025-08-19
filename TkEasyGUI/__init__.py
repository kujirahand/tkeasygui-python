"""TkEasyGUI - A simple GUI library for Python using tkinter."""
# pylint: disable=invalid-name, unused-import, unused-wildcard-import, wildcard-import

from .version import __version__  # noqa: F401, I001
from .locale_easy import *  # noqa: F403, I001
from .utils import *  # noqa: F403, I001
from .widgets import *  # noqa: F403, I001
from .dialogs import *  # noqa: F403, I001 # pylint: disable=redefined-builtin

if __name__ == "__main__":
    print(__doc__)
    print("Version: ", __version__)
