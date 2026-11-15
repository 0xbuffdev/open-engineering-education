# SEF3 — Linux & the Command Line

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 8 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Develop the ability to explain and safely automate work in a Linux shell. Starting from the basic terminal skills introduced by SEF2, investigate files, links, expansion, redirection, pipelines, permissions, processes, and the shell's inherited environment. Then use Bash scripts to search and transform local data, handle failures, and deliver a small tested command-line toolkit.

Bash 5.x and common Linux command-line tools are the reference environment. Use a Linux workstation or an already available free Linux virtual machine, container, or equivalent local environment with a nonprivileged shell. Record the actual Bash, operating-system, and utility versions. Bash arrays, `[[ ... ]]`, `pipefail`, and NUL-delimited `read` options are **Bash features**, not claims about generic POSIX `sh`. Where GNU and POSIX utilities differ, document the dependency or use a supported equivalent.

All assessed work uses synthetic data, explicitly owned temporary directories, and only processes started by the learner for the exercise. No root privileges, `sudo`, system-wide package changes, real scheduled jobs, external network access, personal-file manipulation, or paid service are required. Package-management and network tools can be studied using local documentation and available loopback diagnostics; their presence is not a hidden installation gate.

The 11-module learning sequence is preserved as a guide, not a quota of per-module tests or labs. Six required assessments integrate connected capabilities and can reuse already verified scripts, fixtures, and explanations. **Published outcomes, assessment criteria, and evidence determine course completion**, not attendance or the number of activities performed.

The 8-week duration is a planning estimate. The course remains `draft` until the applicable learner and reviewer evidence justifies a readiness promotion.

## Learning outcomes

- **SEF3-O1:** Safely inspect, create, reorganize, and remove files and directories within an explicitly owned working tree; predict and explain hard-link and symbolic-link behavior.
- **SEF3-O2:** Predict and verify Bash argument vectors resulting from quoting, parameter substitution, pathname matching, and other shell expansions, including spaces, newlines, and unmatched patterns.
- **SEF3-O3:** Identify shell built-ins and external commands, consult their documentation, and explain stdin, stdout, stderr, redirection, pipelines, and exit-status behavior.
- **SEF3-O4:** Diagnose file and directory permission failures and control only explicitly owned child processes using observable process, job, and signal evidence.
- **SEF3-O5:** Use a terminal editor and user-controlled configuration, and diagnose differences in command lookup, environment variables, shell startup, and installed local tools without changing system configuration.
- **SEF3-O6:** Search, filter, and summarize locally generated files and logs using regular expressions and text-processing tools, checking deterministic results against independent reference counts.
- **SEF3-O7:** Write and explain Bash scripts using documented arguments, functions, branching, loops, arrays where appropriate, input validation, and explicit success or failure behavior.
- **SEF3-O8:** Diagnose an unfamiliar shell or automation failure with a minimal reproduction, recorded observations, a causal hypothesis, a bounded repair, and a regression test.
- **SEF3-O9:** Handle arbitrary fixture pathnames and temporary working directories without uncontrolled word splitting, unintended symlink traversal, or changes outside an owned data boundary.
- **SEF3-O10:** Detect and report pipeline and subprocess failures, use narrowly scoped cleanup traps, and explain which interruptions and durability outcomes cannot be guaranteed.
- **SEF3-O11:** Reproduce and explain a noninteractive or restricted-environment failure, distinguishing Bash-specific features from POSIX-sh behavior and documenting platform, locale, path, and tool assumptions.
- **SEF3-O12:** Deliver, verify, and defend a small offline shell toolkit that safely coordinates multiple scripts, preserves unrelated files, handles required error cases, and reproduces its claims from clean fixtures.

## Modules

### Module 1 — Files & Directories

#### Outcomes

- SEF3-O1
- SEF3-O2

#### Lessons

1. Course introduction: Linux & the Command Line
2. The filesystem tree
3. Copying, moving, and removing
4. Wildcards
5. Hard links and symbolic links

*Optional practice:* Predict the tree before moving and renaming mock files; experiment with links and a hidden filename inside the owned fixture directory only.

### Module 2 — Commands & Redirection

#### Outcomes

- SEF3-O3
- SEF3-O10

#### Lessons

1. Kinds of commands
2. Getting help
3. Aliases
4. Standard input, output, and error
5. Pipelines and filters

*Optional practice:* Identify built-ins and external commands with the shell's documentation tools; compare stdout, stderr, and status for a harmless failing helper.

### Module 3 — Expansion & the Keyboard

#### Outcomes

- SEF3-O2
- SEF3-O8

#### Lessons

1. Pathname, tilde, arithmetic, and brace expansion
2. Parameter and command substitution
3. Quoting
4. Command-line editing and history

*Optional practice:* Use a safe argument-display function rather than `eval` to compare quoted and unquoted expansions, including an empty value and an unmatched glob.

### Module 4 — Permissions & Processes

#### Outcomes

- SEF3-O4

#### Lessons

1. Users and groups
2. File modes
3. Changing modes, owners, and the default mask
4. Processes and the process table
5. Signals, job control, and foreground and background work

*Optional practice:* Investigate directory search bits and file modes on disposable files; start, inspect, and wait for one clearly owned short-lived child.

### Module 5 — Environment, Editing & System Tasks

#### Outcomes

- SEF3-O5
- SEF3-O11

#### Lessons

1. Environment variables and `PATH`
2. Shell startup files
3. Editing files with vi(m)
4. Package management
5. Networking tools

*Optional practice:* Edit a local configuration example in a terminal editor; compare a normal shell with a restricted environment using explicit command paths.

### Module 6 — Searching & Text Processing

#### Outcomes

- SEF3-O6
- SEF3-O3

#### Lessons

1. Finding files
2. Archiving and compression
3. Regular expressions
4. Searching text
5. Sorting, cutting, and comparing
6. Stream editing

*Optional practice:* Build a reference count by hand, then search and sort synthetic log records; test empty input and malformed lines.

### Module 7 — Shell Scripts: Foundations

#### Outcomes

- SEF3-O7

#### Lessons

1. A script is a file of commands
2. Variables and constants in scripts
3. Shell functions and top-down design
4. Testing conditions with `if`
5. Reading input

*Optional practice:* Write a small script with help, functions, argument validation, and meaningful nonzero errors for rejected inputs.

### Module 8 — Shell Scripts: Control Flow & Robustness

#### Outcomes

- SEF3-O7
- SEF3-O8

#### Lessons

1. Loops with `while`, `until`, and `for`
2. Branching with `case`
3. Positional parameters and options
4. Strings and numbers
5. Arrays
6. Troubleshooting scripts

*Optional practice:* Seed a quoting or argument-handling defect in a copy, capture the bad output, correct it, and retain a regression test.

### Module 9 — Shell Safety & Process Boundaries

#### Outcomes

- SEF3-O9
- SEF3-O10

#### Lessons

1. Pipeline exit status and command failures
2. Signals and trap cleanup
3. Safe temporary files
4. Pathnames with whitespace and newlines
5. Subshell scope and environment
6. When shell is the wrong tool

*Optional practice:* Use a disposable directory containing filenames with whitespace and newlines; compare NUL-delimited iteration with the unsafe line-splitting example without deleting real files.

### Module 10 — Automation Diagnostics & Portability

#### Outcomes

- SEF3-O5
- SEF3-O8
- SEF3-O11

#### Lessons

1. System logs and process inspection
2. Scheduled jobs and PATH assumptions
3. Process and socket diagnostics
4. POSIX versus Bash portability
5. Structured command-line status reporting

*Optional practice:* Compare a clean environment with the interactive one, then simulate the actual PATH and working-directory assumptions of a scheduled task.

### Module 11 — Shell Toolkit

#### Outcomes

- SEF3-O6
- SEF3-O7
- SEF3-O8
- SEF3-O9
- SEF3-O10
- SEF3-O11
- SEF3-O12

#### Lessons

1. Toolkit contract and bounded fixture layout
2. Report pipeline and staging design
3. Failure-path test harness
4. Clean-start documentation and engineering defense

*Optional practice:* Sketch a two-script log-reporting toolkit and plan its clean-checkout reproduction, failure cases, safety boundary, and technical defense.

## Completion requirements

### Assessment environment and safety

Complete the six required assessments with a documented nonprivileged Bash 5.x (or compatible Bash) environment and generated, non-sensitive fixtures. Specify the shell, operating-system/tool versions, locale when output ordering matters, exact commands, expected results, and actual results. Run all mutating tests inside a verified learner-owned fixture root, never through a broad cleanup command pointed at a home directory or unknown path. Do not use `sudo`, install packages system-wide, alter real startup files or crontabs, fetch remote data, or signal unrelated processes.

Some exercises use unusual pathnames, symlinks, redirection, signals, and injected failures. For each, establish the expected boundaries **before** executing commands; demonstrate that unrelated sentinel data remains unchanged. Where a platform lacks an optional diagnostic utility, document the limitation and use a reproducible equivalent, not an undisclosed dependency. A separate network namespace or administrative capabilities are not needed.

For each assessment, provide inspectable scripts or command transcripts, the input and expected-output fixtures, the actual outputs and exit statuses, and a concise explanation tying observations to the claimed outcomes. A reviewer may choose equivalent unfamiliar fixture values under the published criteria to check independent understanding. Code and output must be reproducible without paid tools or a proprietary grader. Safety-critical failures cannot be excused by extra optional practice or a passing unrelated check.

### Required summative assessments

- **SEF3-AS1** (required files, links, expansion, and stream investigation)
  - Outcomes: SEF3-O1, SEF3-O2, SEF3-O3
  - Work: Create an isolated fixture tree with ordinary names, a hidden file, a name containing spaces, a literal wildcard character, and a name containing a newline. Predict and then demonstrate bounded copy, move, rename, and targeted removal; compare hard-link and symbolic-link behavior before and after removing an original filename. For a supplied set of Bash tokens using variables, pathname patterns, brace expansion, and quoted positional parameters, record the predicted number and values of arguments and compare with a harmless argument-display function. Explain one command's origin or builtin status and route a small helper's stdout and stderr to separate captures.
  - Criteria: Every mutation stays inside the owned fixture tree; the before/after tree and file-content changes match documented predictions or a corrected explanation; hard links and symlinks are distinguished by inode identity versus target pathname. Quotes preserve intended argument boundaries, including spaces and newlines; wildcard and unmatched-pattern behavior is explained with the actual shell settings. Stream captures, documentation lookup, and any nonzero statuses are interpreted correctly. A quoted pathname alone is not mistaken for proof that a deletion target is safe.
  - Evidence: Fixture creation notes, predicted and actual inventories, link metadata observations, argument-vector comparison table, shell configuration, command origin/help observation, separate stream outputs, and a short explanation of any corrected prediction.

- **SEF3-AS2** (required reproducible log and pipeline analysis)
  - Outcomes: SEF3-O3, SEF3-O6, SEF3-O10
  - Work: Produce a local log fixture with a documented delimiter, record types such as `INFO`, `WARN`, and `ERROR`, and an independently computed count-by-type reference. Create a Bash pipeline using suitable regular expressions, filters, sorting, and counting commands to generate a deterministically ordered summary. Decide and document how a malformed record and a no-match case behave. Inject a failure into a middle pipeline stage; compare the default Bash exit status with `pipefail` enabled, and demonstrate an error path that cannot silently publish a plausible but incomplete report.
  - Criteria: Counts and ordering match the independent fixture oracle with the declared locale and regex dialect; empty input, malformed records, and missing matches follow the published output/error policy. Redirection and pipeline behavior are explained accurately; a failed upstream stage is detectable rather than reported as a successful report. The script never overwrites unrelated data or hides the original nonzero status with a trailing successful command.
  - Evidence: Synthetic log fixtures, manual reference counts, documented parsing policy, pipeline/script source, expected/actual reports, stdout/stderr and exit-code comparison for normal and injected-error cases, and a short account of the repaired failure.
  - Review variation: A reviewer may alter a severity count or insert a malformed record, then ask for a predicted summary or error before execution.

- **SEF3-AS3** (required permissions, child process, and environment diagnosis)
  - Outcomes: SEF3-O4, SEF3-O5, SEF3-O11
  - Work: On disposable files and directories, predict and reproduce a permissions failure involving a file mode or a missing directory search permission; inspect user/group identity and explain the failure without requiring ownership changes or privileged operations. Start a bounded background helper, record and verify its child PID, send it a graceful signal, and collect its wait result. Edit a local test configuration with a terminal editor, then run a command-lookup helper in both the ordinary shell and a deliberately restricted environment with an explicit `PATH` and working directory. Inspect a locally available package-manager help page and network diagnostic help or loopback state without changing installed software or contacting an outside network.
  - Criteria: Diagnosis separates file permission from directory traversal and recognizes the role of process identity; the original mode and fixture behavior can be restored. Only the verified owned child process is signaled and reaped. The restricted-environment failure is reproduced and repaired through explicit paths or documented dependencies, not by modifying real login profiles. Editing and local tool inspection are reproducible, with unavailable optional utilities disclosed rather than silently made prerequisites.
  - Evidence: Before/after mode and identity records, attempted access and repair, verified PID and wait observations, edited disposable configuration, environment/`PATH` comparison and diagnostic output, and a brief account of tool and platform limits.

- **SEF3-AS4** (required robust Bash command and defect repair)
  - Outcomes: SEF3-O2, SEF3-O7, SEF3-O8
  - Work: Build a small command-line script that accepts a source pathname and a documented `--mode` or equivalent option, then chooses between two read-only transformations of fixture data. Separate parsing, validation, transformation, and reporting into functions. Use `case`, a loop, and a Bash array where it improves argument handling. Deliberately reproduce at least three distinct bugs affecting a quoted pathname, an unset or missing argument, and a swallowed command failure. Trace and repair the defects in isolated script revisions without using `eval` or an assumption that `set -e` alone prevents errors.
  - Criteria: Help and option validation are predictable; required arguments produce correct output for ordinary names, spaces, and empty inputs, while invalid arguments fail with useful stderr and a nonzero status. Quoting, array boundaries, conditional flow, and interpreter requirements are explained accurately. Each seeded defect has a minimal failing case, causal diagnosis, bounded correction, and passing regression check; no corrected script silently accepts the original failure.
  - Evidence: Published CLI contract, original and repaired Bash source, fixture input/expected output, command and status transcripts, trace excerpts that exclude secrets, and regression test results identifying each repair.

- **SEF3-AS5** (required safe batch paths and bounded cleanup)
  - Outcomes: SEF3-O8, SEF3-O9, SEF3-O10
  - Work: Build a batch summarizer for an owned input tree containing names with spaces, tabs, wildcard characters, and newlines. Enumerate arbitrary fixture names without line-splitting, using a suitable NUL-delimited technique such as `find -print0` with Bash `read -r -d ''`. Reject or explicitly handle symbolic links and unsafe output locations; stage all temporary output in a unique `mktemp` directory underneath a verified owned fixture root. Install narrowly scoped trap cleanup for that staging directory. Inject an ordinary processing error and a catchable interrupt into a script process that the learner started; compare success, failure, repeated-run and cleanup behavior without affecting a separately recorded sentinel file.
  - Criteria: Every fixture pathname remains a distinct argument; no processing or cleanup escapes the owned boundary, follows an uncontrolled symlink, or damages unrelated sentinel data. Partial results are not represented as success; failure statuses remain visible and owned staging is cleaned up when the supported traps execute. A repeated run produces the expected result without stale state. The learner explains that traps cannot handle `SIGKILL` and does not claim complete cleanup or crash durability after every termination.
  - Evidence: Synthetic tree and sentinel checks, source and justified path policies, NUL-safe filename observations, expected/actual success and fault outputs, exit statuses, verified post-run staging inventories, and one reproducible diagnosis and fix.

- **SEF3-AS6** (required offline shell toolkit and restricted-environment defense)
  - Outcomes: SEF3-O5, SEF3-O6, SEF3-O7, SEF3-O8, SEF3-O9, SEF3-O10, SEF3-O11, SEF3-O12
  - Work: Deliver two related Bash scripts as an offline toolkit for producing a summary of mock logs and staging a report: one parses and counts the supplied log records, and the other coordinates safe output preparation and a documented publish or dry-run action. Define input roots, output roots, allowed mutations, log format, option syntax, shell requirements, output schema, success and error codes, and cleanup behavior. Reuse validated components from earlier assessments rather than invent unrelated projects. Test a clean fixture run, a second run, no-match and malformed records, odd filenames, invalid options, upstream pipeline failure, and a deliberately restricted `env -i` / changed-working-directory invocation. Record one real or deliberately introduced defect and its regression repair; explain Bash versus POSIX-sh and relevant GNU-tool assumptions in a reviewable technical defense.
  - Criteria: Both scripts run independently from documented clean-start commands with no privilege, paid resource, or network dependency. Reports match independently checked reference counts; help, input validation, dry-run, safe staging, declared mutations, and nonzero failures behave as specified. Neither an invalid request nor an injected interruption deletes unrelated inputs or silently replaces a valid report with partial output. The restricted-environment run uses explicit, documented dependencies and distinguishes environment defects from data defects. The learner can explain command expansion, functions/control flow, failure propagation, portability limits, and one concrete design trade-off using the submitted evidence, not merely a passing test claim.
  - Evidence: Source or portable archive for both scripts and test harness, README with fixtures and reproducible commands, input/output and status contract, independent count oracle, normal/negative/repeated-run logs, before/after sentinel and report-byte checks, environment/locale/version matrix, repaired-defect record, and a concise written, recorded, live, or otherwise accessible technical defense.

### Completion decision

A learner completes SEF3 when **all six required summative assessments** meet their published criteria and collectively demonstrate SEF3-O1 through SEF3-O12. Assessed source and fixture work may be reused and expanded across the six assessments; learners are not required to write six unrelated utilities or duplicate a quiz and lab in every module. Optional practice and course lessons support learning but are not unannounced completion gates.

A reviewer records each assessment decision with the required inspectable evidence and may request bounded clarification on unfamiliar, but equivalent, inputs under the published criteria. Safety-critical mistakes, hidden dependencies, and non-reproducible output must be corrected before a passing decision. Learner work stays under learner control; sharing raw private machine state, production credentials, or sensitive data is never required. The course itself remains `draft`; an automated structural pass does not satisfy the learner-feedback and reviewer thresholds in [Status Labels](../../spec/status-labels.md).
