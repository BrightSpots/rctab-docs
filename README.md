# RCTab Documentations

This GitHub project documents [RCTab](rcvresources.org/rctab), an open source application for tabulating ranked choice voting elections. This README is intended for developers and maintainers of the RCTab documentation. It provides instructions on how to set up the project, run tests, and release new documentation versions.

If you are an actual user of RCTab and are looking for the documentation itself, those versions are released at the [RCTab documentation homepage](https://brightspots.github.io/rctab-docs/index.html).

## Setting Up the Project

### Software Prerequisites
This project uses [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) to manage and build RCTab's
documentation.

Before you can run and use MkDoc's features in this project, you need to have the following software installed:

- [Python](https://www.python.org/downloads/) (version 3.11 or higher)
- [Poetry](https://python-poetry.org/docs/#installation) (version 1.8 or higher)

### Cloning the Repo

To clone the repo:
```shell
git clone https://github.com/BrightSpots/rctab-docs.git
```

### Installing Python Dependencies and Git Hooks

First, navigate to the directory where the repository has been cloned (e.g. `cd ./rctab-docs`).

Then, run these commands:
```shell
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

## Getting a print version of the documentation

1. Either run `poetry run mkdocs build` or `poetry run mkdocs serve` to generate the documentation.
2. Open Chrome and navigate to either the MKDocs server or static site with the following path at the end: `./tdp/print-page.html`. (Chrome is recommended because each browser's print to PDF feature handles HTML and CSS differently.)
3. Print the page to a PDF file.

## Running Tests

```shell
poetry run pytest
```


## Releasing New Documentation Versions

### Overview

We use a documentation versioning scheme that aligns with, but remains independent from, the [RCTab software versioning](https://github.com/BrightSpots/rcv/wiki/RCTab-Versioning). This allows for multiple documentation versions per RCTab release.

**Documentation Versioning Scheme**: `RCTab v[RCTAB_VERSION_NUMBER]-docX.Y`

- **X**: Incremented for major documentation changes (e.g., from `doc1.0` to `doc2.0`).
  - **Triggers**: Certification and laboratory testing approvals, major content overhauls, new sections, significant updates.
- **Y**: Incremented for minor documentation changes (e.g., from `doc2.0` to `doc2.1`).
  - **Triggers**: Minor edits, typo corrections, small updates.

### Steps to Create a New Documentation Version

1. **Determine the New Documentation Version**

   Decide on the new documentation version number based on the changes:

   - **Major Changes**: Increment `X`.
   - **Minor Changes**: Increment `Y`.
   - **Pre-release Versions**: Use `[RCTab MAJOR.UPDATE_PATH.PATCH]-doc0.b` until `[RCTab MAJOR.UPDATE_PATH.PATCH]-doc1.0`.

   **Examples**:

   - For a **pre-release** of RCTab version `1.999`, the documentation version would be `1.999-doc0.1`.
   - For **pre-release documentation updates** to version `2.0.0`, the new version would be `2.0.0-doc0.1`.
   - For a **minor update** to documentation version `1.3.2-doc2.0`, the new version would be `1.3.2-doc2.1`.

2. **Create a New Release Branch**

   Create a new branch in the repository for the new documentation version.

   **Branch Naming Convention**: `releases/[RCTab_Version]/docX.Y`

   **Example Commands**:

   ```
   git checkout -b releases/2.0.1/doc1.0
   git push -u origin releases/2.0.1/doc1.0
   ```

3. **Update the Documentation Content**

   - **Modify the documentation source files** as needed.
   - **Update `mkdocs.yml`** with the correct site name and version:

     ```yaml
     site_name: 'RCTab Documentation (version 2.0.1/doc1.0)'
     site_url: 'https://brightspots.github.io/rctab-docs/2.0.1/doc1.0/'
     ```
   
   - **Update the `index.md` file** with the new documentation version:

     ```markdown
     # RCTab Docs (version 2.0.1-doc1.0)

     RCTab is an open source tabulator for running ranked choice voting elections.

     Here are some of our technical documents:

     - [TDP](tdp/00_documentation_abstracts.md)
     - [User Guide](user_guide/user_guide.md)
     ```

   - **Build the documentation**:

     ```shell
     poetry run mkdocs build
     ```

     This will generate the `site` directory containing the static files.

4. **Commit and Push Changes**

   ```
   git add .
   git commit -m "Add documentation version 2.0.1-doc1.0"
   git push origin releases/2.0.1/doc1.0
   ```

5. **Update the GitHub Actions Workflow**

   Update the `.github/workflows/deploy-prebuilt-sites.yml` file to include the new documentation version.

   **Note**: The GitHub action should be updated prior to the final commit on a release of the documentation.

   **Example**:

   In the **Set Variables** step, add the new mapping:

   ```yaml
   - name: Set Variables
     id: vars
     run: |
       echo "GITHUB_REF=${GITHUB_REF}"
       BRANCH_NAME="${GITHUB_REF#refs/heads/}"
       echo "Branch name: $BRANCH_NAME"

       # Manual mapping
       if [ "$BRANCH_NAME" == "releases/1.3.2/doc2.0" ]; then
         DEPLOY_DIR="1.3.2/doc2.0"
       elif [ "$BRANCH_NAME" == "releases/1.999/doc0.1" ]; then
         DEPLOY_DIR="1.999/doc0.1"
       elif [ "$BRANCH_NAME" == "releases/2.0.1/doc1.0" ]; then
         DEPLOY_DIR="2.0.1/doc1.0"
       else
         echo "Branch $BRANCH_NAME is not configured for deployment."
         exit 0  # Exit gracefully if the branch is not in the mapping
       fi

       echo "Deployment directory: $DEPLOY_DIR"

       # Set outputs
       echo "branch_name=$BRANCH_NAME" >> $GITHUB_OUTPUT
       echo "deploy_dir=$DEPLOY_DIR" >> $GITHUB_OUTPUT
   ```

   **Commit and Push the Workflow Update**:

   ```
   git add .github/workflows/deploy-prebuilt-sites.yml
   git commit -m "Update workflow to include documentation version 2.0.1-doc1.0"
   git push origin main
   ```

6. **Update the `index.html` File on the `gh-pages` Branch**

   The `index.html` file in the root of the `gh-pages` branch needs to be updated to include the new documentation version.

   **Example Updated `index.html`**:

   ```html
   <html>
   <head></head>
   <body>
     <h1>RCTab Docs</h1>

     <h2>RCTab 1.3.2 Documentation</h2>
     <a href="./1.3.2/doc2.0/">version 1.3.2-doc2.0</a>

     <h2>RCTab 1.999 Documentation</h2>
     <a href="./1.999/doc0.1/">version 1.999-doc0.1</a>

     <h2>RCTab 2.0.1 Documentation</h2>
     <a href="./2.0.1/doc1.0/">version 2.0.1-doc1.0</a>
   </body>
   </html>
   ```

   **Commit and Push Changes**:

   ```
   git add index.html
   git commit -m "Update index.html with documentation version 2.0.1-doc1.0"
   git push origin gh-pages
   ```
   
7. **Commit Final Documentation Changes**

   Once the GitHub action is updated, commit any final changes to the documentation:

   ```
   git add .
   git commit -m "Finalize documentation for version 2.0.1-doc1.0"
   git push origin releases/2.0.1/doc1.0
   ```
   
   > **Note**: To trigger the redeployment it is necessary to push the changes to the `releases/[RCTab_Version]/docX.Y` branch as the last step.

8. **Verify the Deployment**

   - **Access the documentation URL**:

     > https://brightspots.github.io/rctab-docs/2.0.1/doc1.0/index.html

   - **Check the landing page** to ensure the new version is listed:

     > https://brightspots.github.io/rctab-docs/


## How to Obtain a Permalink

When linking to specific sections or pages within your MkDocs documentation, you can create permalinks that allow users to access the content directly. Be aware that these permalinks may change across different documentation versions.

You can obtain a permalink by navigating to the desired section or page in the documentation and copying the URL from the browser's address bar. The paragraph symbol (`¶`) to the right of the section subheading can be used to change the URL in hte address bar to the specific section.

**Example Permalinks**:

- **Version 1.3.2-doc2.0**: https://brightspots.github.io/rctab-docs/1.3.2/doc2.0/tdp/software_design_and_specifications.html#open-source
- ** Version 1.999-doc0.1**: https://brightspots.github.io/rctab-docs/1.999/doc0.1/tdp/software_design_and_specifications.html#open-source


## Useful scripts:

### Compare specific ranges of lines between two files using `vimdiff`
requires `vim` and `vimdiff`

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
