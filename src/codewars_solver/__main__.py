"""
Main module of the package.

This module contains the main function of the package.

Functions:
    main() -> int: Main function.

TODO:
    * Add support for multiple source paths.
"""

from argparse import Namespace
from pathlib import Path

from codewars_api_py import CodewarsAPI  # type: ignore
from core_helpers.logs import logger
from core_helpers.updates import check_updates
from requests import RequestException  # type: ignore
from rich import print
from rich.traceback import install

from codewars_solver.cli import exit_session, get_parsed_args
from codewars_solver.consts import EXIT_SUCCESS, GITHUB, LOG_FILE, PACKAGE
from codewars_solver.consts import __version__ as VERSION


def main() -> None:
    """
    Main function
    """
    args: Namespace = get_parsed_args()
    install(show_locals=args.debug)
    logger.setup_logger(PACKAGE, LOG_FILE, args.debug, args.verbose)

    logger.info("Start of session")

    if GITHUB:
        check_updates(GITHUB, VERSION)

    # Pending katas:
    # - https://www.codewars.com/kata/52742f58faf5485cae000b9a
    # - https://www.codewars.com/kata/563b662a59afc2b5120000c6
    # - https://www.codewars.com/kata/546f922b54af40e1e90001da

    # Initialize the Codewars API wrapper
    codewars_api = CodewarsAPI()

    challenge_id = input("Introduce the challenge id: ")

    try:
        challenge = codewars_api.get_code_challenge(challenge_id)
    except RequestException as e:
        print(e)
        exit_session(EXIT_SUCCESS)

    if not challenge:
        print("Challenge not found")
        exit_session(EXIT_SUCCESS)

    print(challenge)

    text: str = f"""\
# Challenge: {challenge['name']}

**Difficulty:** {challenge['rank']['name']}

**Reference:** {challenge['url']}

## Description

{challenge['description']}
"""

    # Find the folder to save the challenge
    difficulty_folder = Path("out") / challenge["rank"]["name"].replace(" ", "")
    out_folder = difficulty_folder / challenge["slug"]

    # Create the folder if it doesn't exist
    Path.mkdir(out_folder, exist_ok=True, parents=True)

    with open(f"{out_folder}/README.md", "w", encoding="utf-8") as f:
        f.write(text)

    with open(f"{out_folder}/solution.py", "w", encoding="utf-8") as f:
        f.write("")

    exit_session(EXIT_SUCCESS)


if __name__ == "__main__":
    main()
