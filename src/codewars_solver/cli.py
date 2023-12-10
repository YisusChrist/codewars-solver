"""Command-line interface for the project."""
import sys
from argparse import ArgumentParser
from argparse import Namespace

import requests
from rich import print
from rich_argparse_plus import RichHelpFormatterPlus

from . import GITHUB
from . import __desc__ as DESC
from . import __version__ as VERSION
from .consts import EXIT_FAILURE
from .consts import LOG_PATH
from .consts import MAX_TIMEOUT
from .consts import NAME
from .logs import logger


def get_parsed_args() -> Namespace:
    """
    Parse and return command-line arguments.

    Returns:
        The parsed arguments as a Namespace object.
    """
    logger.debug("Parsing command-line arguments")

    RichHelpFormatterPlus.choose_theme("grey_area")

    parser = ArgumentParser(
        description=DESC,  # Program description
        formatter_class=RichHelpFormatterPlus,  # Disable line wrapping
        allow_abbrev=False,  # Disable abbreviations
        add_help=False,  # Disable default help
    )

    g_main = parser.add_argument_group("Main Options")
    # Source path argument
    # g_main.add_argument(...)

    # Config file argument
    g_main.add_argument(
        "-c",
        "--config",
        dest="config_file",
        type=str,
        help="Specify a configuration file.",
    )
    # Create config file interactive
    g_main.add_argument(
        "-i",
        "--interactive",
        dest="interactive",
        action="store_true",
        default=False,
        help="Create a configuration file interactively.",
    )

    g_misc = parser.add_argument_group("Miscellaneous Options")
    # Help
    g_misc.add_argument(
        "-h", "--help", action="help", help="Show this help message and exit."
    )
    # Verbose
    g_misc.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="Show log messages on screen. Default is False.",
    )
    # Debug
    g_misc.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        help="Activate debug logs. Default is False.",
    )
    g_misc.add_argument(
        "-V",
        "--version",
        action="version",
        help="Show version number and exit.",
        version=f"[argparse.prog]{NAME}[/] version [i]{VERSION}[/]",
    )

    return parser.parse_args()


def exit_session(exit_value: int) -> None:
    """
    Exit the program with the given exit value.

    Args:
        exit_value (int): The POSIX exit value to exit with.
    """
    logger.info("End of session")

    # Check if the exit_value is a valid POSIX exit value
    if not 0 <= exit_value <= 255:
        exit_value = EXIT_FAILURE

    if exit_value == EXIT_FAILURE:
        print(
            "\n[red]There were errors during the execution of the script. "
            f"Check the logs at '{LOG_PATH}' for more information.[/]"
        )

    # Exit the program with the given exit value
    sys.exit(exit_value)


def check_updates() -> None:
    """
    Check if there is a newer version of the script available in the GitHub repository.
    """
    logger.debug("Checking for updates...")

    project = GITHUB.split("https://github.com/")[1]
    repo_url = f"https://api.github.com/repos/{project}/releases/latest"

    try:
        response = requests.get(repo_url, timeout=MAX_TIMEOUT)
        response.raise_for_status()

        latest_version = response.json()["tag_name"]
        if latest_version != VERSION:
            print(
                f"\n[yellow]Newer version of the script available: {latest_version}.\n"
                "Please consider updating your version.[/yellow]"
            )

            logger.warning("Newer version of the script available: %s", latest_version)
        else:
            logger.info("Script is at the latest version")
    except requests.exceptions.RequestException:
        logger.error("Could not check for updates")
