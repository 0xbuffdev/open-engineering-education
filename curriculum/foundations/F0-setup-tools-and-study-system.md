# F0 — Setup, Tools & Study System

**Track:** Foundations · **Prerequisite:** none · **Core** · **Time:** 1 week, 15 hours · **Project:** none
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Build a reproducible working environment and a study system you can trust for the next two to three years. Most learners lose weeks to broken environments, missing backups, and unstructured notes. This course prevents that.

## Outcomes

You can:

- open a terminal and navigate the filesystem without a GUI;
- create, edit, run, and debug a small Python program;
- use Git to commit, inspect, branch, and recover a file;
- create and restore a backup;
- keep secrets out of Git;
- explain your weekly study block and review cadence;
- reproduce your environment from a written manifest.

## Required setup

Choose one and record the exact versions:

- **Linux:** Ubuntu/Debian, Fedora, or Arch. A VM or bare metal is preferred for the Systems track.
- **Windows:** WSL2 with Ubuntu. Do not use only PowerShell for Linux labs.
- **macOS:** acceptable for Foundations, but you still need a Linux VM/container before S1.
- **Editor:** VS Code, Neovim, JetBrains, or equivalent. Learn its debugger and terminal.
- **Tools:** Git, Python 3.11+, pip, venv, a C compiler (`gcc` or `clang`), `make`, `gdb`/`lldb`, `strace`, `perf` (Linux), Rust via `rustup` (before F5).
- **Accounts:** a private Git remote (GitHub/GitLab/Codeberg), a password manager, and 2FA.

## Required reading

Read these before Lab 1. They are short and directly usable; do not substitute a long video series.

- **The Missing Semester:** “Course overview + the shell”, “Shell Tools and Scripting”, “Version Control (Git)”, and “Debugging and Profiling”.
- **Pro Git:** Chapters 1–3 (or the Git Book's “Getting Started”, “Git Basics”, and “Git Branching”).
- **Python Tutorial:** “Virtual Environments and Packages” and “Errors and Exceptions”.

**Time:** 4 hours. Record the exact lectures/chapters and access date in `notes/foundations/F0/resources.md`.

## Modules

### 1. Terminal and filesystem

- absolute vs relative paths, `pwd`, `ls`, `cd`, `cp`, `mv`, `rm`, `mkdir`, `find`, `grep`, `less`, `man`;
- permissions, owners, `chmod`, `chown`, `sudo` risks;
- pipes, redirection, environment variables, `PATH`, shell profiles;
- processes, signals, job control, `ps`, `top`, `kill`;
- archives, checksums, `tar`, `sha256sum`;
- SSH keys and remote access.

### 2. Git and backup

- repository, working tree, index, commit, branch, merge, remote;
- `status`, `diff`, `log`, `show`, `restore`, `revert`, `reset`, `reflog`;
- `.gitignore`, secrets, large files;
- a private remote and a second backup location;
- commit messages that explain why, not just what.

### 3. Python and editor

- install Python, create a virtual environment, install a package;
- run a script, use the REPL, read a traceback;
- set up formatting/linting (`ruff`), type checking (`mypy` or `pyright`), and tests (`pytest`);
- configure the editor's debugger and terminal.

### 4. Security hygiene

- disk encryption;
- password manager and unique passwords;
- 2FA and recovery codes;
- SSH key passphrase;
- no secrets in Git, screenshots, or notebooks;
- least-privilege accounts;
- a plan for lost devices and revoked credentials.

### 5. Study system

- a calendar block of 15 hours/week;
- a notes directory and naming convention;
- a lab notebook template;
- a weekly review slot;
- a progress log and a "blockers" list;
- a spaced-review schedule (day 1, day 3, week 2, month 1).

## Labs

### Lab 1 — Reproducible environment manifest

Create `notes/foundations/F0/environment.md` with OS, kernel, CPU, memory, disk, shell, editor, Python, pip, Git, C compiler, Rust, and key tool versions. Include the commands used to obtain each value. Add a `setup.sh` or `setup.md` that a new machine could follow.

**Evidence:** manifest plus a screenshot or transcript of the commands.

### Lab 2 — Git recovery drill

In a disposable repository:

1. create three commits;
2. create a branch, edit a file, merge it;
3. make an intentional merge conflict and resolve it;
4. delete a committed file and restore it with `git restore`;
5. use `git reflog` to recover a commit that is no longer on a branch;
6. create a `.gitignore` that excludes a fake secret file.

**Evidence:** `git log --graph --oneline --all` and a short explanation of each recovery command.

### Lab 3 — Backup and restore

Create a small project, back it up to a second location (external drive or private remote), delete the local copy, and restore it. Record the restore time and what was missing.

**Evidence:** backup command, restore command, checksum comparison.

### Lab 4 — Study block

Plan four weeks of study blocks in your calendar. Include reading, lab, exercise, review, and buffer. Log the first week's actual hours.

**Evidence:** calendar export/screenshot and an hours table.

## Exercises

1. From a blank terminal, create a directory tree, create a file, list hidden files, print it, and remove only the test file. Write each command and its purpose.
2. Explain the difference between `>` and `>>`, and between `2>` and `&>`.
3. Create a Git repository with two focused commits and inspect the diff between them.
4. Recover a deleted tracked file without using a backup.
5. Write a one-page personal runbook: backups, updates, where environments live, how secrets are stored, and what to do if a laptop is lost.
6. Write a one-page study contract: weekly hours, rest day, review day, and what you will do when you fall behind.

## Project increment

None. F0 produces the environment, backup, and study system that P1 depends on. Do not start P1 until the exit check is demonstrable.

## Exit check

Without notes, demonstrate:

- [ ] open a terminal, create a directory, create and run a Python file;
- [ ] inspect `git status`, make a commit, show the log, and restore a previous version;
- [ ] create and activate a virtual environment;
- [ ] run a test and read a traceback;
- [ ] show your environment manifest and backup/restore evidence;
- [ ] explain how you will keep secrets and private data out of Git;
- [ ] state your weekly study block and review cadence.

## Common failure modes

- Spending a week choosing the "perfect" editor or Linux distribution. Pick a mainstream default and move on.
- Installing tools globally and breaking the system Python. Use virtual environments.
- Committing a `.env`, API key, or SSH key. Rotate it immediately if you do.
- Studying without a calendar block. The curriculum will lose to everything else.
- Backing up only to the same disk. A backup is not a backup until restore is tested.

## Evidence to commit

- `notes/foundations/F0/environment.md`
- `notes/foundations/F0/summary.md`
- a small `setup/` script or runbook
- the Git recovery transcript
- the four-week study plan

## Optional depth

- Learn `tmux` and a terminal multiplexer workflow.
- Set up a dotfiles repository with secrets excluded.
- Learn `ssh-agent`, `~/.ssh/config`, and key rotation.
- Read the Git book chapters on branching and reset.
