# Git Workflow Notes

Status: Draft

## Git stages

Git has three stages:

Working Directory
    ↓
Staging Area
    ↓
Commit History


## Meaning of git add

git add does NOT necessarily mean:

"Start tracking a file"

It usually means:

"Move current modifications into staging area"


## PyCharm equivalent

PyCharm GUI              Git CLI

Check a file         →   git add file.py

Uncheck a file       →   git restore --staged file.py

Commit button        →   git commit -m "..."

Push button          →   git push


## File colors in PyCharm

Red:
Untracked file

Blue:
Tracked file with modifications

Green:
Newly added file

Gray:
Ignored file