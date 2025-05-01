# RCTab Documentation

This GitHub project documents [RCTab](https://rcvresources.org/rctab), an open source application for tabulating ranked choice voting elections. This README is intended for developers and maintainers of the RCTab documentation. It provides instructions on how to set up the project, run tests, and release new documentation versions.

If you are an actual user of RCTab and are looking for the documentation itself, those versions are released at the [RCTab documentation homepage](https://rctab-docs.readthedocs.io/).

## Setting Up the Project

### Software Prerequisites
This project uses [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) to manage and build RCTab's
documentation.

Before you can run and use MkDoc's features in this project, you need to have the following software installed:

- [Python](https://www.python.org/downloads/) (version 3.11 or higher)

### Cloning the Repo

To clone the repo:
```shell
git clone https://github.com/BrightSpots/rctab-docs.git
```

### Installing Python Dependencies

First, navigate to the directory where the repository has been cloned (e.g. `cd ./rctab-docs`).

Then, run these commands:
```shell
pip install -r requirements.txt
pip install -e scripts/mkdocs_plugins/link_stripper
```

## Using MkDocs in the Virtual Environment

Feel free to create a virtualenv using standard virtualenv tools.

To preview and serve MkDocs locally:
```shell
python -m mkdocs serve
```

To build MkDocs as a static site:
```shell
python -m mkdocs build
```

## Getting a print version of the documentation

ReadTheDocs hosts both HTML and PDF formats.

## Running Tests

```shell
python -m pytest
```


## Releasing New Documentation Versions

### Overview

We use a documentation versioning scheme that aligns with, but remains independent of, the [RCTab software versioning](https://github.com/BrightSpots/rcv/wiki/RCTab-Versioning). This allows for multiple documentation versions per RCTab release.

**Documentation Versioning Scheme**: `RCTab v[RCTAB_VERSION_NUMBER]-docX.Y`

- **X**: Incremented for major documentation changes (e.g., from `doc1.0` to `doc2.0`).
  - **Triggers**: Certification and laboratory testing approvals, major content overhauls, new sections, significant updates.
- **Y**: Incremented for minor documentation changes (e.g., from `doc2.0` to `doc2.1`).
  - **Triggers**: Minor edits, typo corrections, small updates.

### Steps to Create a New Documentation Version

1. **Determine the New Documentation Version**

   For the example commands in this `readme` we'll use version 2.0.1-doc1.0

2. **Create a New Release Branch or Tag**

   Create a new branch or tag in the repository for the new documentation version.
   Branch from the most recent documentation version for the version of RCTab you're creating documentation for. 
     
   **Branch Naming Convention**: `releases/[RCTAB_VERSION_NUMBER]/docX.Y`

   **Example Commands**:

   ```
   git checkout -b releases/2.0.1/doc1.0
   git push -u origin releases/2.0.1/doc1.0
   ```

3. **Update the Documentation Content**

   - **Modify the documentation source files** as needed.

4. **Commit and Push Changes**
   ```
   git add .
   git commit -m "Add documentation version 2.0.1-doc1.0"
   git push origin releases/2.0.1/doc1.0
   ```
   This will trigger a build on readthedocs.

5. **Create a new documentation version on readthedocs**

   Check out the [Read The Docs documentation](https://docs.readthedocs.com/platform/stable/versions.html) to manage RCTab docs mapping to Read The Docs versions. 