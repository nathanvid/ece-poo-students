# Git and GitHub

Git keeps the history of a folder: each **commit** is a saved version, with a
message saying what changed. GitHub hosts a copy of that history online, to
share it and hand in the project.

## Install and configure (once)

- Windows: install [Git for Windows](https://git-scm.com/download/win), keep
  the default options, then open a new terminal.
- macOS: type `git --version` in a terminal; if Git is missing, macOS offers
  to install it.

```bash
git --version
git config --global user.name "Firstname Lastname"
git config --global user.email "the.email@of.your.github.account"
git config --global init.defaultBranch main
```

Create an account on <https://github.com> with the same email.

## A first repository

```bash
cd path/to/deauville-festival     # the project folder, outside the course folder
git init                          # once: the folder becomes a repository
git status                        # what changed since the last commit
git add festival.py programme.json
git commit -m "Load and save the programme in JSON"
git log --oneline                 # the history
```

`git status` after each step: red files are changed but not added, green
files will go into the next commit.

A good commit is a small step that works, with a message saying what it does:
`Add the venue rule`, not `update` or `fix`.

## Files Git must ignore

A file named `.gitignore` at the root of the repository:

```
__pycache__/
.venv/
.pytest_cache/
.ruff_cache/
.DS_Store
```

## Sending the repository to GitHub

1. On GitHub: **New repository**, name `deauville-festival`, **Private**, no
   README, no `.gitignore` (the folder already has them).
2. GitHub shows the commands for "an existing repository":

   ```bash
   git remote add origin https://github.com/<your-login>/deauville-festival.git
   git push -u origin main
   ```

3. The first `push` opens a window to sign in to GitHub (on Windows, Git
   Credential Manager; on macOS, the browser or VS Code). Sign in with the
   browser; do not type a password in the terminal.
4. **Settings → Collaborators → Add people**: add the trainer's GitHub account.

Afterwards, each time a step works:

```bash
git add .
git commit -m "What this step does"
git push
```

## In VS Code

The **Source Control** panel (third icon on the left) does the same:
`+` next to a file is `git add`, the message box and **Commit** is
`git commit`, **Sync Changes** is `git push`. **Publish Branch** creates the
GitHub repository and pushes in one go.

## When something goes wrong

| Message                       | Meaning                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------------ |
| `fatal: not a git repository` | the terminal is not in the repository folder: `cd`                                         |
| `Author identity unknown`     | the two `git config --global` lines are missing                                            |
| `nothing added to commit`     | `git add` before `git commit`                                                              |
| `rejected ... fetch first`    | GitHub has commits you do not have (made on another computer): `git pull`, then `git push` |
| `Permission denied` / `403`   | signed in with another account: sign out in the credential manager and push again          |
