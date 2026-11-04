> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

# SEF3 — Linux & the Command Line

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** SEF2
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

## Overview

This course develops fluency with the Linux command line: managing files, composing commands with redirection and pipes, understanding how the shell expands what is typed, controlling permissions and processes, configuring the environment, searching and transforming text, and automating work with shell scripts. SEF2 introduced the terminal; this course teaches the shell as a programming and investigation environment that every later program assumes.

## Course brief

The course introduction is the first lesson of the first module. It combines the overview above with these fields.

- **Introduction:** Servers, containers, cloud platforms, and developer machines run Linux, and the command line is how people operate them. This course makes the shell a tool the learner controls, not a place to paste commands.
- **History:** Ken Thompson and Dennis Ritchie began Unix at Bell Labs in 1969. Richard Stallman started the GNU project in 1983 to build a free Unix-like system, and Linus Torvalds released the Linux kernel in 1991. Linux now runs most web servers and cloud infrastructure and is the kernel of Android.
- **Usage:** The learner works at the command line, composes commands, edits files in the terminal, and writes scripts.
- **Applications:** Operating servers, deploying software, processing data, automating work, and investigating security incidents.
- **Strengths:** Small tools combine, everything can be scripted, and the same skills work on any Linux system, including remote ones.
- **Limitations:** Commands are terse and unforgiving, behavior varies slightly between distributions and shells, and few commands can be undone.
- **Key concepts:** shell; filesystem hierarchy; redirection; pipe; expansion; permission; process; environment; regular expression; script

## Prerequisites

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

#### Module brief

- **Introduction:** Everything in Linux is organized as files in one tree. This module teaches how to move, copy, and arrange them safely from the command line.
- **Overview:** It covers the filesystem layout, copying, moving and removing, wildcards, and hard and symbolic links.
- **Key concepts:** filesystem hierarchy; path; wildcard; copy and move; hard link; symbolic link

#### Module outcomes

By the end of this module, the learner can:

- Create, copy, move, rename, and remove files and directories, and predict the result before running the command.
- Use wildcards to select groups of files and explain the difference between hard links and symbolic links.

1. **Course introduction: Linux & the Command Line** — what the subject is, where it came from, where it is used, and its strengths and limits
2. **Introduction: Files & Directories** — what the topic is, where it is used, and its strengths and limits
3. **The filesystem tree**
4. **Copying, moving, and removing**
5. **Wildcards**
6. **Hard links and symbolic links**
7. **Files and directories**
   - kind: `test`
8. **Reorganize a directory tree** — restructure a deliberately messy tree using only commands, predicting each result before running it
   - kind: `lab`

### Module 2 — Commands & Redirection

#### Module brief

- **Introduction:** Unix tools are small and do one thing each, and the shell connects them. This module teaches how commands work and how to combine them.
- **Overview:** It covers kinds of commands, getting help, aliases, standard input, output, and error, redirection, and pipelines.
- **History:** Doug McIlroy proposed connecting programs with pipes, and Ken Thompson added them to Unix in 1973.
- **Strengths:** Small tools combine in ways their authors never planned, and text is a universal interface.
- **Limitations:** Parsing text is fragile, long pipelines are hard to read, and a failure in the middle of a pipeline is easy to miss.
- **Key concepts:** standard input, output, and error; redirection; pipe; filter; command types; help

#### Module outcomes

By the end of this module, the learner can:

- Identify what kind of command is being run and find its documentation.
- Redirect standard input, standard output, and standard error, and connect commands with pipelines.

1. **Introduction: Commands & Redirection** — what the topic is, where it is used, and its strengths and limits
2. **Kinds of commands**
3. **Getting help**
4. **Aliases**
5. **Standard input, output, and error**
6. **Pipelines and filters**
7. **Commands and redirection**
   - kind: `test`
8. **Build a pipeline** — answer a question about a data file using a pipeline of standard tools, then change one stage and explain the effect
   - kind: `lab`

### Module 3 — Expansion & the Keyboard

#### Module brief

- **Introduction:** The shell rewrites what you type before it runs anything. Understanding that rewriting explains most surprises in command-line use.
- **Overview:** It covers pathname, tilde, arithmetic, brace, and parameter expansion, command substitution, quoting, and command-line editing and history.
- **Limitations:** Unquoted values break on spaces, the order of expansions is subtle, and the same command line can behave differently in different shells.
- **Key concepts:** expansion; quoting; command substitution; word splitting; history

#### Module outcomes

By the end of this module, the learner can:

- Explain the order in which the shell performs expansions and the effect of each kind of quoting.
- Use command-line editing and history to work faster and to repeat commands accurately.

1. **Introduction: Expansion & the Keyboard** — what the topic is, where it is used, and its strengths and limits
2. **Pathname, tilde, arithmetic, and brace expansion**
3. **Parameter and command substitution**
4. **Quoting**
5. **Command-line editing and history**
6. **Expansion and quoting**
   - kind: `test`
7. **Predict and verify expansions** — predict what the shell passes to a command for ten tricky command lines, then verify with a harmless echo-based tool
   - kind: `lab`

### Module 4 — Permissions & Processes

#### Module brief

- **Introduction:** Linux is a multi-user system, and every file and every running program belongs to someone. This module explains who may do what.
- **Overview:** It covers users and groups, file modes, changing modes and ownership, the default mask, processes, signals, and job control.
- **Limitations:** Three classes and three permissions cannot express every policy, which is why access control lists exist, and a wrongly set mode can silently expose or block data.
- **Key concepts:** user; group; mode; owner; umask; process; signal; job control

#### Module outcomes

By the end of this module, the learner can:

- Read and change file modes and ownership, and explain how a permission denial arises.
- List, control, and end processes, and explain signals and job control at the command line.

1. **Introduction: Permissions & Processes** — what the topic is, where it is used, and its strengths and limits
2. **Users and groups**
3. **File modes**
4. **Changing modes, owners, and the default mask**
5. **Processes and the process table**
6. **Signals, job control, and foreground and background work**
7. **Permissions and processes**
   - kind: `test`
8. **Diagnose two failures** — find and fix a permission problem and a runaway process on a prepared system, recording the evidence for each
   - kind: `lab`

### Module 5 — Environment, Editing & System Tasks

#### Module brief

- **Introduction:** A shell session carries settings, and real work needs editing and installing. This module covers all three.
- **Overview:** It covers environment variables and PATH, startup files, editing with vi(m), package management, and basic networking tools.
- **History:** Bill Joy wrote vi in 1976, and Vim, released by Bram Moolenaar in 1991, is its descendant.
- **Key concepts:** environment variable; PATH; startup file; modal editing; package manager; network diagnostics

#### Module outcomes

By the end of this module, the learner can:

- Explain environment variables, `PATH`, and shell startup files, and configure a shell environment.
- Edit files with vi(m), install and remove software with a package manager, and use basic networking tools to inspect connectivity.

1. **Introduction: Environment, Editing & System Tasks** — what the topic is, where it is used, and its strengths and limits
2. **Environment variables and `PATH`**
3. **Shell startup files**
4. **Editing files with vi(m)**
5. **Package management**
6. **Networking tools**
7. **Environment and tools**
   - kind: `test`
8. **Configure an environment** — build a reproducible shell setup in a fresh account, install a tool, and verify connectivity
   - kind: `lab`

### Module 6 — Searching & Text Processing

#### Module brief

- **Introduction:** Most information in Linux is text, so the ability to search and transform text is a core skill.
- **Overview:** It covers finding files, archives and compression, regular expressions, searching text, sorting and cutting, and stream editing.
- **History:** Stephen Kleene described regular expressions mathematically in 1951, and Ken Thompson brought them to Unix tools, including grep, in the early 1970s.
- **Strengths:** A few tools cover a very wide range of text tasks quickly and without writing a program.
- **Limitations:** Regular expressions are hard to read and cannot parse nested structures, and tool options differ between versions.
- **Key concepts:** find; archive; regular expression; grep; sort; cut; sed

#### Module outcomes

By the end of this module, the learner can:

- Find files by name, type, time, and size, and act on the results safely.
- Write regular expressions and use standard tools to extract, sort, compare, and transform text.

1. **Introduction: Searching & Text Processing** — what the topic is, where it is used, and its strengths and limits
2. **Finding files**
3. **Archiving and compression**
4. **Regular expressions**
5. **Searching text**
6. **Sorting, cutting, and comparing**
7. **Stream editing**
8. **Search and text processing**
   - kind: `test`
9. **Extract a report from logs** — produce a summary report from a set of log files using only command-line tools, then adapt it to a changed log format
   - kind: `lab`

### Module 7 — Shell Scripts: Foundations

#### Module brief

- **Introduction:** A script records what you did so that it can be repeated. This module turns commands into programs.
- **Overview:** It covers writing and running a script, variables and constants, functions, top-down design, testing conditions, and reading input.
- **Key concepts:** script; shebang; variable; function; exit status; test; read

#### Module outcomes

By the end of this module, the learner can:

- Write an executable script and explain how the shell finds and runs it.
- Use conditions and input to make a script behave differently, and design a script top-down from functions.

1. **Introduction: Shell Scripts: Foundations** — what the topic is, where it is used, and its strengths and limits
2. **A script is a file of commands**
3. **Variables and constants in scripts**
4. **Shell functions and top-down design**
5. **Testing conditions with `if`**
6. **Reading input**
7. **Script foundations**
   - kind: `test`
8. **Write a first script** — turn a repeated manual task into a script with a usage message, input checks, and a deliberately injected failure to diagnose
   - kind: `lab`

### Module 8 — Shell Scripts: Control Flow & Robustness

#### Module brief

- **Introduction:** Useful scripts must loop, branch on many cases, accept options, and fail clearly. This module covers those abilities.
- **Overview:** It covers loops, case, positional parameters, strings and numbers, arrays, and troubleshooting.
- **Limitations:** Quoting mistakes and silent failures are common, and unset variables and word splitting cause subtle bugs.
- **Key concepts:** while; until; for; case; positional parameter; string operation; array; tracing

#### Module outcomes

By the end of this module, the learner can:

- Use loops, `case`, positional parameters, strings, arithmetic, and arrays in scripts.
- Find and fix script defects with tracing and defensive checks.

1. **Introduction: Shell Scripts: Control Flow & Robustness** — what the topic is, where it is used, and its strengths and limits
2. **Loops with `while`, `until`, and `for`**
3. **Branching with `case`**
4. **Positional parameters and options**
5. **Strings and numbers**
6. **Arrays**
7. **Troubleshooting scripts**
8. **Script control flow**
   - kind: `test`
9. **Repair a broken script** — diagnose and fix five seeded defects in a script, using tracing, and add checks so each failure is reported clearly
   - kind: `lab`

### Module 9 — Shell Toolkit

#### Module brief

- **Introduction:** This lab integrates the course. The learner builds a set of scripts that automates a real task and can be trusted by other people.
- **Overview:** The toolkit combines file handling, pipelines, text processing, option handling, error handling, and tests in one documented deliverable.
- **Applications:** Operations work, release automation, and data preparation all begin as scripts like these.
- **Key concepts integrated:** pipelines; expansion and quoting; permissions; regular expressions; scripting; exit status; testing

1. **Build, test, and document the Shell Toolkit**
   - kind: `lab`

## Topics

- The filesystem hierarchy
- Files, directories, and links
- Wildcards and expansion
- Quoting
- Redirection and pipelines
- Permissions and ownership
- Processes, signals, and job control
- The environment and `PATH`
- Terminal editing with vi(m)
- Package management
- Basic networking tools
- Searching for files
- Regular expressions
- Text processing
- Archiving
- Shell scripting: variables, functions, conditions, loops, arguments, arrays
- Script troubleshooting

## Practical exercises

2. Restructure a directory tree using only commands.
3. Answer a data question with a pipeline.
4. Predict shell expansions, then verify them.
5. Diagnose a permission failure and a runaway process.
6. Extract a report from log files.
7. Write and debug a script that takes options and handles errors.

## Course lab

**Shell Toolkit**

Build a small set of related shell scripts that automate a real task, such as organizing downloads, backing up a directory with rotation, or summarizing logs. The toolkit must include:

- Argument and option handling with a usage message
- Input validation and clear error messages with correct exit status
- At least one pipeline and one regular expression
- A test script that exercises success and failure paths
- A README with installation and usage examples

## Exit check

Given an unfamiliar task, the learner can solve it at the command line, turn the solution into a script that handles bad input, and explain what the shell does with each part of the command line.
