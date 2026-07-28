# uv Cheat Sheet

## Install

``` powershell
pip install uv
```

## Python Management

``` powershell
uv python list
uv python install 3.14
```

## Virtual Environments

``` powershell
uv venv
uv venv --python 3.14
.\.venv\Scripts\Activate.ps1
```

## Dependencies

``` powershell
uv add pandas
uv remove pandas
uv sync
uv lock
```

## Run

``` powershell
uv run python main.py
uv run pytest
```

## Tips

-   `.python-version` pins Python.
-   `pyproject.toml` defines project metadata.
-   `uv.lock` locks dependency versions.
