"""
Main module of the package.

This module contains the main function of the package.

Functions:
    main() -> int: Main function.

TODO:
    * Add support for multiple source paths.
"""
from pathlib import Path

from codewars_api_py import CodewarsAPI
from requests import RequestException
from rich import print
from rich.traceback import install

from .cli import check_updates
from .cli import exit_session
from .cli import get_parsed_args
from .consts import DEBUG
from .consts import EXIT_SUCCESS
from .consts import PROFILE
from .logs import logger


def main() -> None:
    """
    Main function
    """
    install(show_locals=DEBUG)
    get_parsed_args()  # args = get_parsed_args()

    logger.info("Start of session")

    check_updates()

    # Initialize the Codewars API wrapper
    codewars_api = CodewarsAPI()  # type: ignore

    challenge_id = input("Introduce the challenge id: ")

    try:
        challenge = codewars_api.get_code_challenge(challenge_id)
    except RequestException as e:
        print(e)
        exit_session(EXIT_SUCCESS)
        return

    if not challenge:
        print("Challenge not found")
        exit_session(EXIT_SUCCESS)
        return

    print(challenge)

    text = f"""# Challenge: {challenge['name']}

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
    # Enable rich error formatting in debug mode
    if DEBUG:
        print("[yellow]Debug mode is enabled[/yellow]")
    if PROFILE:
        import cProfile

        print("[yellow]Profiling is enabled[/yellow]")
        cProfile.run("main()")
    else:
        main()
