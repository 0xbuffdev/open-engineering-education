# SEF3 — Lesson authoring notes

> Optional instructional context preserved from the original source. These are not required course metadata, assessments or module briefs.

## Course orientation

- **Introduction:** Servers, containers, cloud platforms, and developer machines run Linux, and the command line is how people operate them. This course makes the shell a tool the learner controls, not a place to paste commands.
- **History:** Ken Thompson and Dennis Ritchie began Unix at Bell Labs in 1969. Richard Stallman started the GNU project in 1983 to build a free Unix-like system, and Linus Torvalds released the Linux kernel in 1991. Linux now runs most web servers and cloud infrastructure and is the kernel of Android.
- **Usage:** The learner works at the command line, composes commands, edits files in the terminal, and writes scripts.
- **Applications:** Operating servers, deploying software, processing data, automating work, and investigating security incidents.
- **Strengths:** Small tools combine, everything can be scripted, and the same skills work on any Linux system, including remote ones.
- **Limitations:** Commands are terse and unforgiving, behavior varies slightly between distributions and shells, and few commands can be undone.
- **Key concepts:** shell; filesystem hierarchy; redirection; pipe; expansion; permission; process; environment; regular expression; script

## Module 1 — Files & Directories

- **Introduction:** Everything in Linux is organized as files in one tree. This module teaches how to move, copy, and arrange them safely from the command line.
- **Overview:** It covers the filesystem layout, copying, moving and removing, wildcards, and hard and symbolic links.
- **Key concepts:** filesystem hierarchy; path; wildcard; copy and move; hard link; symbolic link

## Module 2 — Commands & Redirection

- **Introduction:** Unix tools are small and do one thing each, and the shell connects them. This module teaches how commands work and how to combine them.
- **Overview:** It covers kinds of commands, getting help, aliases, standard input, output, and error, redirection, and pipelines.
- **History:** Doug McIlroy proposed connecting programs with pipes, and Ken Thompson added them to Unix in 1973.
- **Strengths:** Small tools combine in ways their authors never planned, and text is a universal interface.
- **Limitations:** Parsing text is fragile, long pipelines are hard to read, and a failure in the middle of a pipeline is easy to miss.
- **Key concepts:** standard input, output, and error; redirection; pipe; filter; command types; help

## Module 3 — Expansion & the Keyboard

- **Introduction:** The shell rewrites what you type before it runs anything. Understanding that rewriting explains most surprises in command-line use.
- **Overview:** It covers pathname, tilde, arithmetic, brace, and parameter expansion, command substitution, quoting, and command-line editing and history.
- **Limitations:** Unquoted values break on spaces, the order of expansions is subtle, and the same command line can behave differently in different shells.
- **Key concepts:** expansion; quoting; command substitution; word splitting; history

## Module 4 — Permissions & Processes

- **Introduction:** Linux is a multi-user system, and every file and every running program belongs to someone. This module explains who may do what.
- **Overview:** It covers users and groups, file modes, changing modes and ownership, the default mask, processes, signals, and job control.
- **Limitations:** Three classes and three permissions cannot express every policy, which is why access control lists exist, and a wrongly set mode can silently expose or block data.
- **Key concepts:** user; group; mode; owner; umask; process; signal; job control

## Module 5 — Environment, Editing & System Tasks

- **Introduction:** A shell session carries settings, and real work needs editing and installing. This module covers all three.
- **Overview:** It covers environment variables and PATH, startup files, editing with vi(m), package management, and basic networking tools.
- **History:** Bill Joy wrote vi in 1976, and Vim, released by Bram Moolenaar in 1991, is its descendant.
- **Key concepts:** environment variable; PATH; startup file; modal editing; package manager; network diagnostics

## Module 6 — Searching & Text Processing

- **Introduction:** Most information in Linux is text, so the ability to search and transform text is a core skill.
- **Overview:** It covers finding files, archives and compression, regular expressions, searching text, sorting and cutting, and stream editing.
- **History:** Stephen Kleene described regular expressions mathematically in 1951, and Ken Thompson brought them to Unix tools, including grep, in the early 1970s.
- **Strengths:** A few tools cover a very wide range of text tasks quickly and without writing a program.
- **Limitations:** Regular expressions are hard to read and cannot parse nested structures, and tool options differ between versions.
- **Key concepts:** find; archive; regular expression; grep; sort; cut; sed

## Module 7 — Shell Scripts: Foundations

- **Introduction:** A script records what you did so that it can be repeated. This module turns commands into programs.
- **Overview:** It covers writing and running a script, variables and constants, functions, top-down design, testing conditions, and reading input.
- **Key concepts:** script; shebang; variable; function; exit status; test; read

## Module 8 — Shell Scripts: Control Flow & Robustness

- **Introduction:** Useful scripts must loop, branch on many cases, accept options, and fail clearly. This module covers those abilities.
- **Overview:** It covers loops, case, positional parameters, strings and numbers, arrays, and troubleshooting.
- **Limitations:** Quoting mistakes and silent failures are common, and unset variables and word splitting cause subtle bugs.
- **Key concepts:** while; until; for; case; positional parameter; string operation; array; tracing

## Module 9 — Shell Toolkit

- **Introduction:** This lab integrates the course. The learner builds a set of scripts that automates a real task and can be trusted by other people.
- **Overview:** The toolkit combines file handling, pipelines, text processing, option handling, error handling, and tests in one documented deliverable.
- **Applications:** Operations work, release automation, and data preparation all begin as scripts like these.
- **Key concepts integrated:** pipelines; expansion and quoting; permissions; regular expressions; scripting; exit status; testing

1. **Build, test, and document the Shell Toolkit**
   - kind: `lab`

## Original topic inventory

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
