# GitHub over SSH (Windows + PowerShell)

## 1. Check Git

``` powershell
git --version
```

If Git is missing, install it from https://git-scm.com/downloads.

## 2. Configure Git

``` powershell
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
git config --global --list
```

## 3. Check for an existing SSH key

``` powershell
dir $HOME\.ssh
```

If `id_ed25519` and `id_ed25519.pub` exist, you can reuse them.

## 4. Create an SSH key

``` powershell
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Accept the default location:

`C:\Users\<username>\.ssh\id_ed25519`

Choose a passphrase (recommended) or press Enter for none.

## 5. Configure the SSH agent (optional but recommended)

Check the service:

``` powershell
Get-Service ssh-agent
```

### If it is already running

``` powershell
ssh-add $HOME\.ssh\id_ed25519
```

### If it is stopped

Open **PowerShell as Administrator** once and run:

``` powershell
Set-Service ssh-agent -StartupType Automatic
Start-Service ssh-agent
```

Then, in a normal PowerShell:

``` powershell
ssh-add $HOME\.ssh\id_ed25519
```

> If you receive **Access is denied**, you were not running PowerShell
> as Administrator. Alternatively, you can skip the SSH agent entirely.
> Git can still use `~/.ssh/id_ed25519`; you'll simply enter the
> passphrase (if any) when needed.

## 6. Copy your public key

``` powershell
Get-Content $HOME\.ssh\id_ed25519.pub
```

Copy the entire line beginning with `ssh-ed25519`.

## 7. Add the key to GitHub

Go to **GitHub → Settings → SSH and GPG keys → New SSH key**.

Give it a title (e.g. *My Windows Laptop*), paste the public key, and
save.

## 8. Test the connection

``` powershell
ssh -T git@github.com
```

The first time, answer:

``` text
yes
```

You should eventually see:

``` text
Hi <your-username>! You've successfully authenticated...
```

## 9. Create a GitHub repository

Create a new empty repository.

Do **not** initialize it with:

-   README
-   .gitignore
-   License

if your project already exists locally.

## 10. Connect the local repository

``` powershell
git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPOSITORY.git
git remote -v
```

## 11. First push

``` powershell
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

Future pushes:

``` powershell
git add .
git commit -m "Describe your changes"
git push
```

## Useful commands

``` powershell
git status
git pull
git push
```

## Suggested `.gitignore`

``` text
.venv/
__pycache__/
.pytest_cache/
.mypy_cache/
.env
.vscode/
```

## Typical workflow

1.  Modify your code.
2.  `git status`
3.  `git add .`
4.  `git commit -m "Meaningful message"`
5.  `git push`
