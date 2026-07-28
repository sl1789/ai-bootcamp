# VS Code Setup for Python

## Recommended Extensions

-   Python
-   Pylance
-   Ruff (optional)
-   Docker (optional)
-   GitHub Pull Requests (optional)

## Settings

-   Use PowerShell as default terminal.
-   Select `.venv\Scripts\python.exe` as interpreter.
-   Enable automatic environment activation.

## Create a project

``` powershell
uv venv
.\.venv\Scripts\Activate.ps1
uv sync
```

## Common Commands

-   Ctrl+Shift+P → Python: Select Interpreter
-   Ctrl+\` → Toggle terminal

## Troubleshooting

-   Wrong interpreter: reselect interpreter.
-   Execution policy:
    `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
-   Recreate venv if switching Python versions.
