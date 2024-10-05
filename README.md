<p align="center">
    <a href="https://github.com/yisuschrist/codewars-solver/issues">
        <img src="https://img.shields.io/github/issues/yisuschrist/codewars-solver?color=171b20&label=Issues%20%20&logo=gnubash&labelColor=e05f65&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/codewars-solver/forks">
        <img src="https://img.shields.io/github/forks/yisuschrist/codewars-solver?color=171b20&label=Forks%20%20&logo=git&labelColor=f1cf8a&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/codewars-solver/stargazers">
        <img src="https://img.shields.io/github/stars/yisuschrist/codewars-solver?color=171b20&label=Stargazers&logo=octicon-star&labelColor=70a5eb">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/codewars-solver/actions">
        <img alt="Tests Passing" src="https://github.com/yisuschrist/codewars-solver/actions/workflows/github-code-scanning/codeql/badge.svg">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/yisuschrist/codewars-solver/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/yisuschrist/codewars-solver?color=0088ff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://opensource.org/license/gpl-3-0/">
        <img alt="License" src="https://img.shields.io/github/license/yisuschrist/codewars-solver?color=0088ff">
    </a>
</p>

<br>

<p align="center">
    <a href="https://github.com/yisuschrist/codewars-solver/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/yisuschrist/codewars-solver/issues/new/choose">Request Feature</a>
    ·
    <a href="https://github.com/yisuschrist/codewars-solver/discussions">Ask Question</a>
    ·
    <a href="https://github.com/yisuschrist/codewars-solver/security/policy#reporting-a-vulnerability">Report security bug</a>
</p>

<br>

![Alt](https://repobeats.axiom.co/api/embed/35569e3c284b5b783757493946440a1c6e080da1.svg "Repobeats analytics image")

<br>

`codewars-solver` is a Python package that allows you to solve [Codewars](https://www.codewars.com) katas from the command line and automatically submit them to the platform. Once the kata is solved, the program will automatically create a new file with the solution in the appropriate directory. It also allows you to upload the solution to your personal GitHub repository to keep track of your progress, share your solutions with the community and store your collection of solved katas.

All the functionalities can be described in the following steps:

- [ ] 1. The program will ask you to enter your `Codewars username` and `API key`. This information will be stored in a configuration file in your system's configuration directory. This information is required to submit the solutions to the platform.

- [x] 2. The program will ask you to select the programming language you want to use to solve the kata. The program will then create a new file with the kata's name in the appropriate directory. The file will contain the kata's description and a template with the function to be implemented.

- [ ] 3. Once the kata is solved, the program will automatically submit the solution to the platform and create a new file with the solution in the appropriate directory. The program will also ask you if you want to upload the solution to your personal GitHub repository. If you choose to do so, the program will create a new branch with the solution and open a pull request to merge the branch with the main branch.

<br>

<details>
<summary>Table of Contents</summary>

- [Requirements](#requirements)
- [Installation](#installation)
  - [From PyPI](#from-pypi)
  - [Manual installation](#manual-installation)
  - [Uninstall](#uninstall)
- [Usage](#usage)
  - [Example of execution](#example-of-execution)
- [Contributors](#contributors)
  - [How do I contribute to codewars-solver?](#how-do-i-contribute-to-codewars-solver)
- [License](#license)
- [Credits](#credits)

</details>

## Requirements

Here's a breakdown of the packages needed and their versions:

- [platformdirs](https://pypi.org/project/platformdirs) - 3.10.0
- [rich](https://pypi.org/project/rich) - 13.5.2
- [rich-argparse-plus](https://pypi.org/project/rich-argparse-plus) - 0.3.1.4
- [tqdm](https://pypi.org/project/tqdm) - 4.66.1

> [!NOTE]
> The software has been developed and tested using Python 3.11.4. The minimum required version to run the software is Python 3.6. Although the software may work with previous versions, it is not guaranteed.

## Installation

### From PyPI

`codewars-solver` can be installed easily as a PyPI package. Just run the following command:

```bash
pip3 install codewars-solver
```

> [!IMPORTANT]
> For best practices and to avoid potential conflicts with your global Python environment, it is strongly recommended to install this program within a virtual environment. Avoid using the --user option for global installations. We highly recommend using [pipx](https://pypi.org/project/pipx) for a safe and isolated installation experience. Therefore, the appropriate command to install `codewars-solver` would be:
>
> ```bash
> pipx install codewars-solver
> ```

The program can now be ran from a terminal with the `codewars-solver` command.

### Manual installation

If you prefer to install the program manually, follow these steps:

> [!WARNING]
> This will install the version from the latest commit, not the latest release.

1. Download the latest version of [codewars-solver](https://github.com/yisuschrist/codewars-solver) from this repository:

   ```bash
   git clone https://github.com/yisuschrist/codewars-solver
   cd codewars-solver
   ```

2. Install the dependencies:

   ```bash
   poetry install --only main
   ```

3. Run the following commands to install codewars-solver in your `/usr/bin/` directory:

   ```bash
   poetry run codewars-solver
   ```

The program can now be ran from a terminal with the `codewars-solver` command.

### Uninstall

If you installed it from PyPI, you can use the following command:

```bash
pipx uninstall codewars-solver
```

## Usage

To run the `codewars-solver` script, you can use the following command:

```bash
codewars-solver [OPTIONS]
```

where `[OPTIONS]` are the command line options described below:

```

```

### Example of execution

## Contributors

<a href="https://github.com/yisuschrist/codewars-solver/graphs/contributors"><img src="https://contrib.rocks/image?repo=yisuschrist/codewars-solver" /></a>

### How do I contribute to codewars-solver?

Before you participate in our delightful community, please read the [code of conduct](https://github.com/YisusChrist/.github/blob/main/CODE_OF_CONDUCT.md).

I'm far from being an expert and suspect there are many ways to improve – if you have ideas on how to make the configuration easier to maintain (and faster), don't hesitate to fork and send pull requests!

We also need people to test out pull requests. So take a look through [the open issues](https://github.com/yisuschrist/codewars-solver/issues) and help where you can.

See [Contributing Guidelines](https://github.com/YisusChrist/.github/blob/main/CONTRIBUTING.md) for more details.

## License

`codewars-solver` is released under the [GPL-3.0 License](https://opensource.org/licenses/GPL-3.0).

## Credits

This package was partially created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and adapted from the [@cjolowicz](https://github.com/cjolowicz)'s [Hypermodern Python Cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python) project template.
