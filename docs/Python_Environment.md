# Python Environment Guide

## Recommended Stack

-   Windows Python 3.13/3.14
-   PowerShell
-   uv
-   VS Code
-   Git + GitHub SSH

## Create a New Project

``` powershell
mkdir my_project
cd my_project
uv init
uv venv --python 3.14
.\.venv\Scripts\Activate.ps1
uv sync
```

## Verify

``` powershell
python --version
where python
pip --version
```

## Project Layout

``` text
my_project/
├── .venv/
├── src/
├── tests/
├── pyproject.toml
├── uv.lock
└── README.md
```

## Best Practices

-   One virtual environment per project.
-   Never commit `.venv/`.
-   Pin dependencies with `uv.lock`.
-   Store secrets in `.env`.
