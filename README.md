# RCTab Documentations

Welcome to the Poetry Project! This project uses Poetry for dependency management and packaging in Python.

## Prerequisites

Before you can run and use Poetry in this project, you need to have the following software installed:

- Python (version 3.11 or higher)
- Poetry (version 1.8 or higher)

### Installing Python

You can download and install Python from the [official Python website](https://www.python.org/downloads/).

### Installing Poetry

To install Poetry, you can follow the instructions from the
[official Poetry documentation](https://python-poetry.org/docs/#installation).

## Running and Using Poetry

Once you have Python and Poetry installed, you can start using Poetry to manage your project's dependencies and
environment.

### Setting Up the Project

First, navigate to the root directory of your project and install the dependencies:
```
cd path/to/rctab-docs
poetry install
```

### Activating the Virtual Environment

Poetry automatically creates a virtual environment for your project. To activate this environment, run:
```
poetry shell
```

### Adding Dependencies

To add a new dependency to your project, you can use the `poetry add` command:
```
poetry add requests
```

### Running Scripts

Although there is no `main.py` file right now, you can still run individual scripts or modules using Poetry:
```
poetry run python path/to/your/script.py
```
