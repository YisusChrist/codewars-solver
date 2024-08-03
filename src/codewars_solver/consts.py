"""Constants for the project."""

from pathlib import Path

from platformdirs import user_config_dir
from platformdirs import user_data_dir
from platformdirs import user_log_dir


try:
    from importlib import metadata
except ImportError:  # for Python < 3.8
    import importlib_metadata as metadata  # type: ignore

__version__ = metadata.version(__package__ or __name__)
__desc__ = metadata.metadata(__package__ or __name__)["Summary"]
PACKAGE = metadata.metadata(__package__ or __name__)["Name"]
GITHUB = metadata.metadata(__package__ or __name__)["Home-page"]

CONFIG_PATH: str = user_config_dir(appname=PACKAGE, ensure_exists=True)
CONFIG_FILE: Path = Path(CONFIG_PATH).resolve() / f"{PACKAGE}.ini"
DATA_PATH: str = user_data_dir(appname=PACKAGE, ensure_exists=True)
LOG_PATH: str = user_log_dir(appname=PACKAGE, ensure_exists=True)
LOG_FILE: Path = Path(LOG_PATH).resolve() / f"{PACKAGE}.log"

MAX_TIMEOUT = 5

DEFAULT_SRC_PATH: Path = Path(DATA_PATH).resolve()
DEFAULT_DEST_PATH: Path = Path(DATA_PATH).resolve()

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

DEBUG = False
PROFILE = False
