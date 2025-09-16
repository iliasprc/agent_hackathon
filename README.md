# agent_hackathon

# Overview

This repository contains the code for the Google ADK Hackathon 


# Getting Started
## Prerequisites
- Python 3.12 or higher


### Uv setup (Recommended)
Install uv with our standalone installers:

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or, from [PyPI](https://pypi.org/project/uv/):

```bash
# With pip.
pip install uv
```

```bash
# Or pipx.
pipx install uv
```


## Installation

### Create a virtualenv
uv supports creating virtual environments, e.g., to create a virtual environment at .venv:

```bash
uv venv --python 3.12
```

###  Install the required packages
```bash
uv pip install -r pyproject.toml
```
or

```bash
uv sync
```

### Python dependencies
When adding new Python packages to the project, use `uv add <package_name>` to add the package and update the `pyproject.toml`

