# SEF3 — Linux & the Command Line

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course develops fluency with the Linux command line: managing files, composing commands with redirection and pipes, understanding how the shell expands what is typed, controlling permissions and processes, configuring the environment, searching and transforming text, and automating work with shell scripts. SEF2 introduced the terminal; this course teaches the shell as a programming and investigation environment that every later program assumes.

- [**SEF2 — Programming & Computational Thinking**](SEF2.md)

## Learning outcomes

By the end of the course, the learner will be able to:

- Manage files, directories, and links from the command line.
- Compose commands with redirection, pipes, and filters, and explain what the shell does before a command runs.
- Read and change file permissions and explain how users, groups, and processes interact.
- Inspect and control running processes, and explain the environment a process inherits.
- Search for files and transform text with standard tools and regular expressions.
- Edit files with a terminal editor and install software with a package manager.
- Write, debug, and structure shell scripts that handle arguments, input, errors, and control flow.
- Build a tested, documented command-line toolkit that automates a real task.

## Modules

### Module 1 — Files & Directories

#### Outcomes

- Create, copy, move, rename, and remove files and directories, and predict the result before running the command.
- Use wildcards to select groups of files and explain the difference between hard links and symbolic links.

#### Lessons

1. **Course introduction: Linux & the Command Line** — `lesson`

   Servers, containers, cloud platforms, and developer machines run Linux, and the command line is how people operate them. This course makes the shell a tool the learner controls, not a place to paste commands.
2. **The filesystem tree** — `lesson`
3. **Copying, moving, and removing** — `lesson`
4. **Wildcards** — `lesson`
5. **Hard links and symbolic links** — `lesson`
6. **Files and directories** — `test`
7. **Reorganize a directory tree** — `lab` — restructure a deliberately messy tree using only commands, predicting each result before running it

### Module 2 — Commands & Redirection

#### Outcomes

- Identify what kind of command is being run and find its documentation.
- Redirect standard input, standard output, and standard error, and connect commands with pipelines.

#### Lessons

1. **Kinds of commands** — `lesson`
2. **Getting help** — `lesson`
3. **Aliases** — `lesson`
4. **Standard input, output, and error** — `lesson`
5. **Pipelines and filters** — `lesson`
6. **Commands and redirection** — `test`
7. **Build a pipeline** — `lab` — answer a question about a data file using a pipeline of standard tools, then change one stage and explain the effect

### Module 3 — Expansion & the Keyboard

#### Outcomes

- Explain the order in which the shell performs expansions and the effect of each kind of quoting.
- Use command-line editing and history to work faster and to repeat commands accurately.

#### Lessons

1. **Pathname, tilde, arithmetic, and brace expansion** — `lesson`
2. **Parameter and command substitution** — `lesson`
3. **Quoting** — `lesson`
4. **Command-line editing and history** — `lesson`
5. **Expansion and quoting** — `test`
6. **Predict and verify expansions** — `lab` — predict what the shell passes to a command for ten tricky command lines, then verify with a harmless echo-based tool

### Module 4 — Permissions & Processes

#### Outcomes

- Read and change file modes and ownership, and explain how a permission denial arises.
- List, control, and end processes, and explain signals and job control at the command line.

#### Lessons

1. **Users and groups** — `lesson`
2. **File modes** — `lesson`
3. **Changing modes, owners, and the default mask** — `lesson`
4. **Processes and the process table** — `lesson`
5. **Signals, job control, and foreground and background work** — `lesson`
6. **Permissions and processes** — `test`
7. **Diagnose two failures** — `lab` — find and fix a permission problem and a runaway process on a prepared system, recording the evidence for each

### Module 5 — Environment, Editing & System Tasks

#### Outcomes

- Explain environment variables, `PATH`, and shell startup files, and configure a shell environment.
- Edit files with vi(m), install and remove software with a package manager, and use basic networking tools to inspect connectivity.

#### Lessons

1. **Environment variables and `PATH`** — `lesson`
2. **Shell startup files** — `lesson`
3. **Editing files with vi(m)** — `lesson`
4. **Package management** — `lesson`
5. **Networking tools** — `lesson`
6. **Environment and tools** — `test`
7. **Configure an environment** — `lab` — build a reproducible shell setup in a fresh account, install a tool, and verify connectivity

### Module 6 — Searching & Text Processing

#### Outcomes

- Find files by name, type, time, and size, and act on the results safely.
- Write regular expressions and use standard tools to extract, sort, compare, and transform text.

#### Lessons

1. **Finding files** — `lesson`
2. **Archiving and compression** — `lesson`
3. **Regular expressions** — `lesson`
4. **Searching text** — `lesson`
5. **Sorting, cutting, and comparing** — `lesson`
6. **Stream editing** — `lesson`
7. **Search and text processing** — `test`
8. **Extract a report from logs** — `lab` — produce a summary report from a set of log files using only command-line tools, then adapt it to a changed log format

### Module 7 — Shell Scripts: Foundations

#### Outcomes

- Write an executable script and explain how the shell finds and runs it.
- Use conditions and input to make a script behave differently, and design a script top-down from functions.

#### Lessons

1. **A script is a file of commands** — `lesson`
2. **Variables and constants in scripts** — `lesson`
3. **Shell functions and top-down design** — `lesson`
4. **Testing conditions with `if`** — `lesson`
5. **Reading input** — `lesson`
6. **Script foundations** — `test`
7. **Write a first script** — `lab` — turn a repeated manual task into a script with a usage message, input checks, and a deliberately injected failure to diagnose

### Module 8 — Shell Scripts: Control Flow & Robustness

#### Outcomes

- Use loops, `case`, positional parameters, strings, arithmetic, and arrays in scripts.
- Find and fix script defects with tracing and defensive checks.

#### Lessons

1. **Loops with `while`, `until`, and `for`** — `lesson`
2. **Branching with `case`** — `lesson`
3. **Positional parameters and options** — `lesson`
4. **Strings and numbers** — `lesson`
5. **Arrays** — `lesson`
6. **Troubleshooting scripts** — `lesson`
7. **Script control flow** — `test`
8. **Repair a broken script** — `lab` — diagnose and fix five seeded defects in a script, using tracing, and add checks so each failure is reported clearly

### Module 9 — Shell Toolkit

#### Outcomes

- Complete and explain the **Shell Toolkit** integration lab, demonstrating the relevant course outcomes and retained evidence.

#### Lessons

1. **Build, test, and document the Shell Toolkit** — `lab`

   **Final integration lab — required work**

   **Shell Toolkit**

   Build a small set of related shell scripts that automate a real task, such as organizing downloads, backing up a directory with rotation, or summarizing logs. The toolkit must include:

   - Argument and option handling with a usage message
   - Input validation and clear error messages with correct exit status
   - At least one pipeline and one regular expression
   - A test script that exercises success and failure paths
   - A README with installation and usage examples

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required exercises**

**Practical practice:**

- Restructure a directory tree using only commands.
- Answer a data question with a pipeline.
- Predict shell expansions, then verify them.
- Diagnose a permission failure and a runaway process.
- Extract a report from log files.
- Write and debug a script that takes options and handles errors.

**Exit demonstration:**

Given an unfamiliar task, the learner can solve it at the command line, turn the solution into a script that handles bad input, and explain what the shell does with each part of the command line.
