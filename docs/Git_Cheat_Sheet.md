# Git Cheat Sheet

## Repository Setup

``` bash
git init
git clone <url>
git remote -v
git remote add origin <url>
```

## Daily Workflow

``` bash
git status
git add .
git commit -m "Meaningful message"
git push
```

## Branches

``` bash
git branch
git switch -c feature/my-feature
git switch main
git branch -d feature/my-feature
```

## Sync

``` bash
git pull
git fetch
git push
```

## History

``` bash
git log --oneline --graph --decorate --all
git diff
git diff --staged
```

## Undo Changes

Discard unstaged changes:

``` bash
git restore file.py
```

Unstage a file:

``` bash
git restore --staged file.py
```

Restore all files:

``` bash
git restore .
```

Revert a commit (safe):

``` bash
git revert <commit>
```

Reset local branch (destructive):

``` bash
git reset --hard HEAD
```

## Stashing

``` bash
git stash
git stash list
git stash pop
```

## Tags

``` bash
git tag v1.0.0
git push origin v1.0.0
```

## .gitignore

Typical Python:

``` text
.venv/
__pycache__/
.pytest_cache/
.mypy_cache/
.env
.vscode/
```

## SSH

Test:

``` bash
ssh -T git@github.com
```

## Helpful Aliases

``` bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.sw switch
git config --global alias.br branch
git config --global alias.lg "log --oneline --graph --decorate --all"
```

## Common Problems

### Wrong commit message

``` bash
git commit --amend -m "New message"
```

### Forgot to add a file

``` bash
git add missing.py
git commit --amend --no-edit
```

### Accidentally committed secrets

Remove them, rotate credentials, then rewrite history only if necessary.

## Recommended Learning Order

1.  init / clone
2.  status
3.  add
4.  commit
5.  push
6.  pull
7.  branches
8.  merge
9.  restore
10. revert
11. stash
12. rebase (later)
