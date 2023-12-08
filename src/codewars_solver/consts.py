"""Constants for the project."""
from pathlib import Path

from platformdirs import user_config_dir
from platformdirs import user_data_dir
from platformdirs import user_log_dir

from . import PACKAGE


NAME = PACKAGE  # Path(__file__).name.split(".")[0]
CONFIG_PATH = user_config_dir(appname=NAME, ensure_exists=True)
CONFIG_FILE = Path(CONFIG_PATH).resolve() / f"{NAME}.ini"
DATA_PATH = user_data_dir(appname=NAME, ensure_exists=True)
LOG_PATH = user_log_dir(appname=NAME, ensure_exists=True)
LOG_FILE = Path(LOG_PATH).resolve() / f"{NAME}.log"

DEFAULT_SRC_PATH = Path(DATA_PATH).resolve() / "instagram"
DEFAULT_DEST_PATH = Path(DATA_PATH).resolve() / "move"

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

DEBUG = False
PROFILE = False
