# SEF3 — Linux & the Command Line

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 8 weeks
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
- Build defensive shell automation with safe quoting, controlled temporary files and explicit exit/error behavior.

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
7. **Reorganize a directory tree** — `lab`

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
7. **Build a pipeline** — `lab`

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
6. **Predict and verify expansions** — `lab`

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
7. **Diagnose two failures** — `lab`

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
7. **Configure an environment** — `lab`

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
8. **Extract a report from logs** — `lab`

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
7. **Write a first script** — `lab`

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
8. **Repair a broken script** — `lab`

### Module 9 — Shell Safety & Process Boundaries

#### Outcomes

- Handle interrupts and unsafe pathnames predictably in scripts.
- Diagnose an unexpected result using observable evidence.

#### Lessons

1. **Pipeline exit status and command failures** — `lesson`
2. **Signals and trap cleanup** — `lesson`
3. **Safe temporary files** — `lesson`
4. **Pathnames with whitespace and newlines** — `lesson`
5. **Subshell scope and environment** — `lesson`
6. **When shell is the wrong tool** — `lesson`
7. **Shell Safety & Process Boundaries reasoning** — `test`
8. **Build a safe batch processor** — `lab`

### Module 10 — Automation Diagnostics & Portability

#### Outcomes

- Diagnose a scheduled script failure from environment and process evidence.
- Diagnose an unexpected result using observable evidence.

#### Lessons

1. **System logs and process inspection** — `lesson`
2. **Scheduled jobs and PATH assumptions** — `lesson`
3. **Process and socket diagnostics** — `lesson`
4. **POSIX versus Bash portability** — `lesson`
5. **Structured command-line status reporting** — `lesson`
6. **Automation Diagnostics & Portability reasoning** — `test`
7. **Repair a restricted-environment task** — `lab`

### Module 11 — Shell Toolkit

#### Outcomes

- Complete and explain the **Shell Toolkit** integration lab, demonstrating the relevant course outcomes and retained evidence.

#### Lessons

1. **Shell Toolkit reliability and portability** — `test`
2. **Build, test, and document the Shell Toolkit** — `lab`

   **Final integration lab — required work**

   **Shell Toolkit**

   Build a small set of related shell scripts that automate a real task, such as organizing downloads, backing up a directory with rotation, or summarizing logs. The toolkit must include:

   - Argument and option handling with a usage message
   - Input validation and clear error messages with correct exit status
   - At least one pipeline and one regular expression
   - A test script that exercises success and failure paths
   - A README with installation and usage examples
   - Unprivileged, bounded filesystem operations with safe cleanup
   - Reproducible checks for unusual filenames, pipeline failures and restricted environments

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

Complete these required exercises:

**Practical practice:**

- Restructure a directory tree using only commands.
- Answer a data question with a pipeline.
- Predict shell expansions, then verify them.
- Diagnose a permission failure and a runaway process.
- Extract a report from log files.
- Write and debug a script that takes options and handles errors.

**Required module checkpoints and practical lab contracts:**

All eleven modules require two explained conceptual checkpoints and one practical lab. Questions can be replaced by equivalent unfamiliar examples assessing the same outcomes. Learners must predict shell behavior, observe results and explain discrepancies; copying displayed answers without evidence is insufficient.

**Shared lab environment:**

Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.

**Shared evaluation requirements:**

- Use controlled, user-owned fixture directories for filesystem changes and only explicitly owned child PIDs for process-control exercises.
- Record source revision, exact commands, Bash/tool versions, fixtures, predicted versus observed results, relevant exit statuses and an investigated error with repair.
- Demonstrate normal, boundary and failure cases required for each lab; unsafe broad cleanup, unintended user-file changes or unsupported portability claims block completion.
- Keep optional networking and package management inspection unprivileged. No learner is required to install software system-wide or alter their login environment.

**Module 1 — Files & Directories: checkpoint** — Required assessment details

- **Q1 (free):** What happens to a hard link and a symbolic link after the original filename is removed?
  - Expected answer and scoring: The hard link remains a name for the same inode on that filesystem; a symlink holding the removed pathname becomes dangling unless another object exists at its target path.
- **Q2 (free):** Does quoting a pathname make a recursive remove command safe?
  - Expected answer and scoring: No. Quoting prevents splitting and globbing but does not establish that the path is the intended disposable directory. Check the owned fixture root and delete only explicitly controlled files.

**Module 1 — Reorganize a directory tree: required lab** — Required assessment details

- **Objective:** Demonstrate the module outcomes and explain normal and failure conditions in a safely bounded Linux shell task.
- **Prerequisites:** Complete module lessons and explain the associated checkpoint questions; reuse earlier validated artifacts only when their assumptions hold.
- **Environment:** Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.
- **Procedure:**
  1. Create an isolated directory with inbox, work and archive areas, and files including one with spaces.
  2. Predict the tree after copy, move, rename and targeted removal, then execute each operation against the fixture only.
  3. Create hard and symbolic links, remove their original named target, and compare the remaining link behavior.
  4. Test missing source, hidden file and space-containing path; record clear errors and verify unrelated files were not changed.
- **Expected result:** The recorded tree and file content match predictions; link outcomes distinguish inode identity from target path.
- **Verification:** Compare sorted inventories, metadata and file contents before and after each action.
- **Evidence:** Versioned scripts or command transcript, generated fixtures, expected/actual output and exit status, environmental assumptions and reproducible negative-path tests.
- **Failure analysis:** Explain accidental glob expansion, a wrong working directory or an incorrect link prediction.
- **Acceptance:** All documented operations succeed or fail as specified, the learner explains the shell mechanics, and the commands can be reproduced safely from fresh fixtures. Required safety or correctness failures block completion.

**Module 2 — Commands & Redirection: checkpoint** — Required assessment details

- **Q1 (free):** Where do standard output and standard error go when redirected separately? How does redirection order affect descriptor duplication?
  - Expected answer and scoring: stdout and stderr are independent streams. In Bash, redirecting stderr to the current stdout before redirecting stdout to a file does not subsequently move stderr into that file; redirections are evaluated in order.
- **Q2 (free):** What status does Bash normally report for a pipeline whose middle stage fails and last stage succeeds? What does pipefail change?
  - Expected answer and scoring: Default status is the final command status. With Bash pipefail enabled, the rightmost nonzero command status is returned, or zero if all stages succeed.

**Module 2 — Build a pipeline: required lab** — Required assessment details

- **Objective:** Demonstrate the module outcomes and explain normal and failure conditions in a safely bounded Linux shell task.
- **Prerequisites:** Complete module lessons and explain the associated checkpoint questions; reuse earlier validated artifacts only when their assumptions hold.
- **Environment:** Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.
- **Procedure:**
  1. Create a small line-based fixture with a known number of warning and error records.
  2. Use grep, sort and wc in a pipeline to compute a summary and predict the manual count.
  3. Run a harmless helper emitting separate stdout and stderr, then change redirection order to inspect where bytes go.
  4. Inject one failing middle stage, compare default and pipefail statuses, and keep all output under the fixture directory.
- **Expected result:** The report matches manual counts and each stream and failure status follows the stated Bash semantics.
- **Verification:** Compare expected counts, captured streams and the exact pipeline exit statuses.
- **Evidence:** Versioned scripts or command transcript, generated fixtures, expected/actual output and exit status, environmental assumptions and reproducible negative-path tests.
- **Failure analysis:** Explain redirected stderr appearing in the terminal or an upstream error masked by the final command.
- **Acceptance:** All documented operations succeed or fail as specified, the learner explains the shell mechanics, and the commands can be reproduced safely from fresh fixtures. Required safety or correctness failures block completion.

**Module 3 — Expansion & the Keyboard: checkpoint** — Required assessment details

- **Q1 (free):** How does quoted parameter expansion differ from unquoted expansion for a variable containing two words?
  - Expected answer and scoring: Unquoted expansion can undergo word splitting and pathname expansion, while a double-quoted expansion preserves the value as one argument. Exact results depend on Bash settings and IFS.
- **Q2 (free):** What do the Bash expansions quoted at-sign positional parameters and quoted asterisk positional parameters preserve?
  - Expected answer and scoring: Quoted at-sign preserves each argument as a distinct word, including spaces. Quoted asterisk joins positional parameters into one word using the first IFS character.

**Module 3 — Predict and verify expansions: required lab** — Required assessment details

- **Objective:** Demonstrate the module outcomes and explain normal and failure conditions in a safely bounded Linux shell task.
- **Prerequisites:** Complete module lessons and explain the associated checkpoint questions; reuse earlier validated artifacts only when their assumptions hold.
- **Environment:** Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.
- **Procedure:**
  1. Create filename fixtures with spaces, wildcard characters and an ordinary .txt suffix in a disposable directory.
  2. Predict ten harmless Bash command argument vectors involving tilde, braces, variables, globs, arithmetic and positional parameters.
  3. Use a display-arguments function with printf to record argument count and exact values, rather than echo or eval.
  4. Test an empty variable, an unmatched pattern and a quoted literal wildcard; retain one corrected wrong prediction.
- **Expected result:** All ten predictions match the observed argument count and values under documented Bash and glob settings.
- **Verification:** Compare expected versus observed argument tables and Bash configuration.
- **Evidence:** Versioned scripts or command transcript, generated fixtures, expected/actual output and exit status, environmental assumptions and reproducible negative-path tests.
- **Failure analysis:** Explain a mistaken split, glob interpretation, collapsed argument boundary or reliance on eval.
- **Acceptance:** All documented operations succeed or fail as specified, the learner explains the shell mechanics, and the commands can be reproduced safely from fresh fixtures. Required safety or correctness failures block completion.

**Module 4 — Permissions & Processes: checkpoint** — Required assessment details

- **Q1 (free):** A file is group-readable but cannot be opened. What additional permissions might matter?
  - Expected answer and scoring: Directory search permission on every ancestor is needed, and ACL/MAC or other policy can restrict access. Unprivileged testing may differ from running as root.
- **Q2 (free):** Why should learners only signal a child PID they have just launched and verified?
  - Expected answer and scoring: PIDs can be reused or refer to unrelated processes. Send graceful termination to the controlled fixture and wait for that child instead of targeting arbitrary system processes.

**Module 4 — Diagnose two failures: required lab** — Required assessment details

- **Objective:** Demonstrate the module outcomes and explain normal and failure conditions in a safely bounded Linux shell task.
- **Prerequisites:** Complete module lessons and explain the associated checkpoint questions; reuse earlier validated artifacts only when their assumptions hold.
- **Environment:** Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.
- **Procedure:**
  1. Create permission fixtures inside an unprivileged temporary directory; record modes, ownership and expected access.
  2. Reproduce a denial by restricting a fixture directory or file, then diagnose using mode and directory permissions and repair the fixture.
  3. Launch one bounded background sleep/test fixture, capture its PID and verify that it is the owned process.
  4. Send it SIGTERM, wait for completion and record status; never modify unrelated accounts or processes.
- **Expected result:** The access error is explained and repaired, and the owned background process is terminated and reaped.
- **Verification:** Record before/after modes, access attempts, PID ownership and wait result.
- **Evidence:** Versioned scripts or command transcript, generated fixtures, expected/actual output and exit status, environmental assumptions and reproducible negative-path tests.
- **Failure analysis:** Explain a missing directory-search bit, privilege assumptions or an unverified process identifier.
- **Acceptance:** All documented operations succeed or fail as specified, the learner explains the shell mechanics, and the commands can be reproduced safely from fresh fixtures. Required safety or correctness failures block completion.

**Module 5 — Environment, Editing & System Tasks: checkpoint** — Required assessment details

- **Q1 (free):** Why might a command work in an interactive shell yet fail in a scheduled or noninteractive environment?
  - Expected answer and scoring: Different PATH, startup files, current directory, exported variables and permissions may apply. The command must be resolved and environment assumptions stated.
- **Q2 (free):** Do shell startup files and exported variables retroactively change already running processes?
  - Expected answer and scoring: No. Exported values are inherited by new child processes where passed; startup files are interpreted by shells that read them, not retroactively by existing processes.

**Module 5 — Configure an environment: required lab** — Required assessment details

- **Objective:** Demonstrate the module outcomes and explain normal and failure conditions in a safely bounded Linux shell task.
- **Prerequisites:** Complete module lessons and explain the associated checkpoint questions; reuse earlier validated artifacts only when their assumptions hold.
- **Environment:** Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.
- **Procedure:**
  1. Record Bash version, PATH, present working directory and selected environment variables in a disposable workspace.
  2. Edit a text configuration file using a terminal editor, verify its contents and avoid changing the real home startup files.
  3. Write a command-lookup script, then run it normally and in a restricted environment using env -i and an explicitly provided minimal PATH.
  4. Inspect package manager help and available loopback networking tools without installing software or requiring privileged access.
- **Expected result:** The script detects missing commands in a restricted environment and succeeds with documented paths; no system settings change.
- **Verification:** Compare interpreter and PATH reports and capture error statuses from both environments.
- **Evidence:** Versioned scripts or command transcript, generated fixtures, expected/actual output and exit status, environmental assumptions and reproducible negative-path tests.
- **Failure analysis:** Explain assuming interactive aliases, shell startup behavior or installed packages are present.
- **Acceptance:** All documented operations succeed or fail as specified, the learner explains the shell mechanics, and the commands can be reproduced safely from fresh fixtures. Required safety or correctness failures block completion.

**Module 6 — Searching & Text Processing: checkpoint** — Required assessment details

- **Q1 (free):** How does extended regular expression mode differ from default basic grep syntax for grouping and alternation?
  - Expected answer and scoring: Extended syntax enables unescaped grouping and alternation such as the WARN-or-ERROR pattern. State the selected regex dialect and locale.
- **Q2 (free):** Why is a newline-separated list of filenames unsafe for arbitrary Unix pathnames?
  - Expected answer and scoring: Newlines can occur in filenames. Use NUL-delimited find output with a compatible reader or use find -exec with correct argument passing.

**Module 6 — Extract a report from logs: required lab** — Required assessment details

- **Objective:** Demonstrate the module outcomes and explain normal and failure conditions in a safely bounded Linux shell task.
- **Prerequisites:** Complete module lessons and explain the associated checkpoint questions; reuse earlier validated artifacts only when their assumptions hold.
- **Environment:** Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.
- **Procedure:**
  1. Create local INFO, WARN and ERROR log fixtures with independently counted totals and a documented delimiter.
  2. Use grep -E, cut, sort and uniq or a comparable documented pipeline to summarize severity by category.
  3. Alter a fixture with a missing field and define whether to reject it or record it in an error summary.
  4. Test empty files, no matches and filenames containing whitespace/newlines without splitting paths by lines.
- **Expected result:** Sorted severity counts equal the manual reference table, and malformed input follows the declared policy.
- **Verification:** Compare fixture-by-fixture expected counts and observed output with a stable locale.
- **Evidence:** Versioned scripts or command transcript, generated fixtures, expected/actual output and exit status, environmental assumptions and reproducible negative-path tests.
- **Failure analysis:** Explain regex dialect confusion, wrong field selection or unsafe pathname splitting.
- **Acceptance:** All documented operations succeed or fail as specified, the learner explains the shell mechanics, and the commands can be reproduced safely from fresh fixtures. Required safety or correctness failures block completion.

**Module 7 — Shell Scripts: Foundations: checkpoint** — Required assessment details

- **Q1 (free):** Why can referencing a missing first positional parameter fail under Bash nounset, and how is that avoided?
  - Expected answer and scoring: With nounset, expansion of an unset positional parameter can fail before testing. Validate the argument count first or use an intentional default expression.
- **Q2 (free):** How does explicitly running a script with bash differ from direct execution as an executable file?
  - Expected answer and scoring: An explicit bash invocation reads the script as an argument; direct execution depends on execute permissions and an interpreter declaration or equivalent system mechanism.

**Module 7 — Write a first script: required lab** — Required assessment details

- **Objective:** Demonstrate the module outcomes and explain normal and failure conditions in a safely bounded Linux shell task.
- **Prerequisites:** Complete module lessons and explain the associated checkpoint questions; reuse earlier validated artifacts only when their assumptions hold.
- **Environment:** Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.
- **Procedure:**
  1. Write a Bash line-count script in a disposable directory with a usage message and one required file argument.
  2. Validate argument count and file readability before invoking a counting command and use quoted paths.
  3. Test valid, empty, missing and space-containing input names; capture stdout, stderr and exit codes.
  4. Remove one quote or validation check in a copy, reproduce the issue and repair it.
- **Expected result:** Correct counts on valid input, clear nonzero errors on invalid input and no unintended file changes.
- **Verification:** Compare outputs with independent line counts and rerun all fixtures after repair.
- **Evidence:** Versioned scripts or command transcript, generated fixtures, expected/actual output and exit status, environmental assumptions and reproducible negative-path tests.
- **Failure analysis:** Explain an unset parameter, invalid file handling or a usage message that incorrectly exits successfully.
- **Acceptance:** All documented operations succeed or fail as specified, the learner explains the shell mechanics, and the commands can be reproduced safely from fresh fixtures. Required safety or correctness failures block completion.

**Module 8 — Shell Scripts: Control Flow & Robustness: checkpoint** — Required assessment details

- **Q1 (free):** What is the difference between correctly quoted Bash array element expansion and unquoted expansion?
  - Expected answer and scoring: Quoted array-at expansion preserves elements and spaces; unquoted forms can undergo splitting and pathname expansion and lose argument boundaries. Bash arrays are not a POSIX sh requirement.
- **Q2 (free):** What is the limitation of reading file lines with a for-loop over command substitution?
  - Expected answer and scoring: Shell splitting and pathname expansion may destroy original lines; use a line-oriented while-read loop with IFS and -r for text, while acknowledging it cannot represent arbitrary binary NUL input.

**Module 8 — Repair a broken script: required lab** — Required assessment details

- **Objective:** Demonstrate the module outcomes and explain normal and failure conditions in a safely bounded Linux shell task.
- **Prerequisites:** Complete module lessons and explain the associated checkpoint questions; reuse earlier validated artifacts only when their assumptions hold.
- **Environment:** Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.
- **Procedure:**
  1. Use a deliberately broken Bash fixture script with five defects: quoting, array expansion, argument validation, loop boundary and masked command failure.
  2. Run it only on temporary fixtures with spaces and wildcard characters, collecting differences from expected results.
  3. Use Bash tracing without secrets and repair each defect in a separate logical step.
  4. Exercise case-based options and test valid, empty, missing and malformed input; document Bash-only behavior.
- **Expected result:** All five defect categories are corrected and failure statuses are neither lost nor mislabeled.
- **Verification:** Keep before/after outputs, exit statuses and fixture inventory for every seeded defect.
- **Evidence:** Versioned scripts or command transcript, generated fixtures, expected/actual output and exit status, environmental assumptions and reproducible negative-path tests.
- **Failure analysis:** Explain why set -e alone is not sufficient and why unquoted arrays corrupt filename boundaries.
- **Acceptance:** All documented operations succeed or fail as specified, the learner explains the shell mechanics, and the commands can be reproduced safely from fresh fixtures. Required safety or correctness failures block completion.

**Module 9 — Shell Safety & Process Boundaries: checkpoint** — Required assessment details

- **Q1 (free):** How should Bash consume filenames that may include spaces, tabs or newlines?
  - Expected answer and scoring: Use NUL-delimited paths, such as GNU find -print0 with a Bash read loop using -d for the NUL separator, or an appropriate find -exec operation. State platform dependencies.
- **Q2 (free):** What cleanup scope should an EXIT trap have, and does it run after SIGKILL?
  - Expected answer and scoring: Remove only a validated, unique temporary directory owned by the script; broad globs and a shared TMPDIR are unsafe. SIGKILL cannot be trapped, so cleanup is best-effort.

**Module 9 — Build a safe batch processor: required lab** — Required assessment details

- **Objective:** Demonstrate the module outcomes and explain normal and failure conditions in a safely bounded Linux shell task.
- **Prerequisites:** Complete module lessons and explain the associated checkpoint questions; reuse earlier validated artifacts only when their assumptions hold.
- **Environment:** Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.
- **Procedure:**
  1. Create an isolated input tree with spaces, tabs, wildcard symbols and a newline in filenames plus an unrelated sentinel.
  2. Iterate paths with NUL-safe processing and copy or summarize files into a tracked mktemp-created output staging directory.
  3. Use guarded trap cleanup for only that temporary directory; document known signal limitations.
  4. Inject a normal processing failure and an interrupt to the owned script fixture, check status/cleanup and verify a second run is safe.
- **Expected result:** All filenames are handled as distinct paths; source and unrelated files remain intact; normal failure cleanup is bounded.
- **Verification:** Compare before/after inventories and checksums, success/failure statuses and temporary-directory state.
- **Evidence:** Versioned scripts or command transcript, generated fixtures, expected/actual output and exit status, environmental assumptions and reproducible negative-path tests.
- **Failure analysis:** Explain unsafe splitting, a broad cleanup glob or assuming a trap handles uncatchable termination.
- **Acceptance:** All documented operations succeed or fail as specified, the learner explains the shell mechanics, and the commands can be reproduced safely from fresh fixtures. Required safety or correctness failures block completion.

**Module 10 — Automation Diagnostics & Portability: checkpoint** — Required assessment details

- **Q1 (free):** A script runs interactively but fails in a task runner. Which environment differences should be investigated?
  - Expected answer and scoring: Check PATH, cwd, interpreter, argument quoting, exported variables, permissions and startup-file assumptions in the actual execution environment.
- **Q2 (free):** Can a Bash script with arrays and double-bracket tests be assumed to run under every system bin/sh?
  - Expected answer and scoring: No. Declare Bash explicitly and test supported behavior; Bash arrays and double brackets are not mandatory POSIX sh features.

**Module 10 — Repair a restricted-environment task: required lab** — Required assessment details

- **Objective:** Demonstrate the module outcomes and explain normal and failure conditions in a safely bounded Linux shell task.
- **Prerequisites:** Complete module lessons and explain the associated checkpoint questions; reuse earlier validated artifacts only when their assumptions hold.
- **Environment:** Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.
- **Procedure:**
  1. Create a local report script with documented input/output directories and required commands.
  2. Use env -i in a test harness to simulate restricted scheduling; do not install a real cron task or change system crontab.
  3. Seed a bad working-directory assumption and short PATH lookup failure, record each with sanitized logs.
  4. Repair using explicit paths and documented shell requirements, and compare interactive versus restricted outputs.
- **Expected result:** The failure reproduces under the harness and the corrected script behaves consistently under documented conditions.
- **Verification:** Compare exact output files, exit codes, interpreter/PATH logs and clean-start instructions.
- **Evidence:** Versioned scripts or command transcript, generated fixtures, expected/actual output and exit status, environmental assumptions and reproducible negative-path tests.
- **Failure analysis:** Explain reliance on aliases, implicit current directory or Bash syntax invoked through sh.
- **Acceptance:** All documented operations succeed or fail as specified, the learner explains the shell mechanics, and the commands can be reproduced safely from fresh fixtures. Required safety or correctness failures block completion.

**Module 11 — Shell Toolkit: checkpoint** — Required assessment details

- **Q1 (free):** Which checks should a backup script perform before accepting a user-provided directory and cleanup destination?
  - Expected answer and scoring: Validate type, allowed workspace boundary, symlinks, destination overlap, and safe scope. Quoting alone cannot prevent a correctly quoted but unintended destructive target.
- **Q2 (free):** Why must a shell toolkit be tested with failures, unusual filenames and repeated invocation?
  - Expected answer and scoring: Happy-path output does not prove correct exit codes, pathname preservation, bounded cleanup or idempotence. Independent fixtures and expected results are necessary.

**Module 11 — Build, test, and document the Shell Toolkit: required lab** — Required assessment details

- **Objective:** Demonstrate the module outcomes and explain normal and failure conditions in a safely bounded Linux shell task.
- **Prerequisites:** Complete module lessons and explain the associated checkpoint questions; reuse earlier validated artifacts only when their assumptions hold.
- **Environment:** Use a nonprivileged disposable Linux environment (VM, container or user-owned test directory), Bash 5.x or a documented compatible version and commonly available GNU/POSIX command-line tools. Record actual Bash and utility versions. Run against generated fixtures only; never modify real home files, system configuration or unrelated processes. No sudo, system-wide package installation, external network, real cron modifications or root access is required. Bash arrays, double-bracket tests, pipefail and read with NUL delimiter must not be misrepresented as POSIX-sh portable.
- **Procedure:**
  1. Create a small toolkit for summarizing mock logs and staging reports, defining accepted inputs, outputs, file boundaries and Bash assumptions.
  2. Implement at least two related scripts, one using a regex and pipeline and one preparing results in a unique temporary staging directory.
  3. Provide usage/help, input validation, safe quoting, a dry-run where data is replaced, and explicit failure statuses.
  4. Write a self-contained shell test harness covering valid/empty input, filename spaces/newlines, pipeline failure, repeated runs and an injected interrupt.
  5. Record actual environment, exact commands, outputs and one reviewed defect; verify from a fresh disposable checkout.
- **Expected result:** The toolkit generates the independently counted report, rejects invalid input and modifies only its declared fixture output.
- **Verification:** Compare counts, output files, exit status, sentinel integrity and cleanup across repeated runs.
- **Evidence:** Versioned scripts or command transcript, generated fixtures, expected/actual output and exit status, environmental assumptions and reproducible negative-path tests.
- **Failure analysis:** Explain masked pipeline failure, unsafe cleanup, non-portable syntax or an undocumented environment dependency.
- **Acceptance:** All documented operations succeed or fail as specified, the learner explains the shell mechanics, and the commands can be reproduced safely from fresh fixtures. Required safety or correctness failures block completion.

**Exit demonstration:**

Given an unfamiliar task, the learner can solve it at the command line, turn the solution into a script that handles bad input, and explain what the shell does with each part of the command line.
