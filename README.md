# RCTab Documentations

This project documents RCTab, an open source application for tabulating ranked choice voting elections.

## Prerequisites

This project uses [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) to manage and build RCTab's
documentation.

Before you can run and use MkDoc's features in this project, you need to have the following software installed:

- Python (version 3.11 or higher)
- Poetry (version 1.8 or higher)
- `vim` and `vimdiff` (required to run an optional script)

### Installing Python

You can download and install Python from the [official Python website](https://www.python.org/downloads/).

### Installing Poetry

To install Poetry, you can follow the instructions from the
[official Poetry documentation](https://python-poetry.org/docs/#installation).

## Running and Using Poetry

Once you have Python and Poetry installed, you can start using Poetry to manage your project's dependencies and
environment.

### Cloning the Repo and Setting Up the Project

Run these shell commands:
```shell
git clone https://github.com/BrightSpots/rctab-docs.git # clones the repo
cd ./rctab-docs # navigates to the local repo
poetry install # installs the dependencies
cp .githooks/* .git/hooks/ # installs the git hooks
```

## Using MkDocs in the Virtual Environment

Poetry automatically creates a virtual environment for your project.

To preview and serve MkDocs locally:
```shell
poetry run mkdocs serve
```

To build MkDocs as a static site:
```shell
poetry run mkdocs build
```

## Useful scripts:

### Compare specific ranges of lines between two files using `vimdiff`

Run:
```shell
./scripts/compare_parts.sh
```
#### Some useful `vimdiff` commands to use in `./scripts/compare_parts.sh`:

| Action                                                        | `vimdiff` command                                       |
|---------------------------------------------------------------|---------------------------------------------------------|
| Switch between files being compared                           | `ctrl`+`w`+`w` while in vim's `INSERT` mode             |
| Wrap lines in a window pane                                   | `setlocal wrap linebreak` while in vim's `COMMAND` mode |
| Copy a the selected window pane's file to the MacOS clipboard | `w !pbcopy` while in vim's `COMMNAND` mode              |

### Copy specific ranges of lines from one file into another file

Run:
```shell
./scripts/insert_lines.sh
```

Recommend testing this out on some small test files to understand how it works before running it on larger files. Alternatively, you can use a version management  tool like `git`.