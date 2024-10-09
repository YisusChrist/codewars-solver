"""Constants for the project."""

from pathlib import Path

from core_helpers.xdg_paths import get_user_path

try:
    from importlib import metadata
except ImportError:  # for Python < 3.8
    import importlib_metadata as metadata  # type: ignore

__version__ = metadata.version(__package__ or __name__)
__desc__ = metadata.metadata(__package__ or __name__)["Summary"]
GITHUB = metadata.metadata(__package__ or __name__)["Home-page"]
PACKAGE = metadata.metadata(__package__ or __name__)["Name"]

CONFIG_PATH: Path = get_user_path(PACKAGE, "config")
CONFIG_FILE: Path = CONFIG_PATH / f"{PACKAGE}.ini"
DATA_PATH: Path = get_user_path(PACKAGE, "data")
LOG_PATH: Path = get_user_path(PACKAGE, "log")
LOG_FILE: Path = LOG_PATH / f"{PACKAGE}.log"

MAX_TIMEOUT = 5

DEFAULT_SRC_PATH: Path = DATA_PATH
DEFAULT_DEST_PATH: Path = DATA_PATH

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

DEBUG = False
PROFILE = False
