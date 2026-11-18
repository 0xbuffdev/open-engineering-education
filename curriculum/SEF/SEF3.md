# SEF3 — Linux & the Command Line

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 10–12 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Develop the ability to explain and safely automate work in a Linux shell. Starting from the basic terminal skills introduced by SEF2, investigate files, links, expansion, redirection, pipelines, permissions, processes, and the shell's inherited environment. Then use Bash scripts to search and transform local data, handle failures, and deliver a small tested command-line toolkit.

Bash 5.x and common Linux command-line tools are the reference environment. Distinguish **three contracts**: POSIX shell language and semantics, Bash extensions, and external POSIX/GNU/other utility implementations. A Bash script is not automatically portable to `sh`, and portable shell syntax does not make GNU-specific flags portable. Use a Linux workstation or an already available free Linux virtual machine, container, or equivalent local environment with a nonprivileged shell. Record the actual Bash, operating-system, and utility versions. Bash arrays, `[[ ... ]]`, and NUL-delimited `read -d` are **Bash-specific interfaces**, not generic POSIX `sh` requirements. **`set -o pipefail` is now part of POSIX.1-2024 (Issue 8)**, but older standard editions and installed `sh` implementations may lack it; verify actual support before using it. Likewise, `find -print0` and `xargs -0` were added to POSIX.1-2024, whereas Bash `read -d` is a separate shell feature. Where GNU and POSIX utilities differ, document the exact standard edition or local implementation/version, demonstrate a supported alternative, or explicitly constrain the supported platform. Running `bash --posix` is not independent proof of portability to another shell; a second shell such as `dash` is optional if already available, not an installation gate. A local `sh` may itself be Bash: document that limitation.

All assessed work uses synthetic data, explicitly owned temporary directories, and only processes started by the learner for the exercise. No root privileges, `sudo`, system-wide package changes, real scheduled jobs, external network access, personal-file manipulation, or paid service are required. Package-management and network tools can be studied using local documentation and available loopback diagnostics; their presence is not a hidden installation gate.

The learning sequence is derived from necessary shell competencies, not a predetermined number of modules, lessons, tests or labs. Seven required assessments integrate connected capabilities and may reuse earlier verified scripts, fixtures and explanations. The portability assessment extends the same shell toolkit, not a separate application. **Published outcomes, assessment criteria, and evidence determine course completion**, not attendance or the number of activities performed.

The 10–12-week duration is a provisional estimate for the additional environment and portability investigations; it is not validated learner study-time evidence. The course remains `draft` until the applicable learner and reviewer evidence justifies a readiness promotion.

For optional standards cross-checks, consult the freely accessible [POSIX.1-2024 Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html), [Bash Startup Files](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html), [Bash POSIX Mode](https://www.gnu.org/software/bash/manual/html_node/Bash-POSIX-Mode.html) and [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/). These free references clarify implementation details but are not substitutes for the complete public learning outcomes and assessment criteria below.

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
- **SEF3-O13:** Build and actually exercise a small POSIX-sh-compatible helper and a deliberately Bash-specific alternative; distinguish shell syntax from external utility portability, explain real interpreter/version behavior, and defend a verified compatibility boundary rather than assuming portability from a shebang or a single Bash run.
- **SEF3-O14:** Predict and reproduce exported versus shell-local variable inheritance, child/subshell effects, login/interactive/noninteractive startup behavior, working directory, command lookup, and locale-dependent output in controlled environments without modifying real user configuration.

## Modules

### Module 1 — Shell Execution and Command Identity

#### Outcomes

- SEF3-O3
- SEF3-O5

#### Lessons

1. **What the shell executes** — Connect SEF2's terminal introduction to shell parsing, built-ins and externally launched processes; distinguish shell syntax from the programs it invokes.
2. **Reproducible command context** — Record Bash, Linux and selected utility versions, a working directory and command status without exposing private environment variables.
3. **Absolute and relative paths** — Predict resolution from a particular working directory and reproduce a wrong-directory failure in a deliberately owned fixture.
4. **Command lookup and help** — Distinguish reserved words, functions, built-ins, aliases and executables using appropriate `type`, `command -v`, `help` and local manuals; explain why aliases depend on invocation context.
5. **Three independent compatibility contracts** — Identify POSIX shell syntax, the actual Bash interpreter and available external utilities as separate claims requiring evidence.

*Optional practice:* Predict a harmless command's identity and failure status under two explicitly controlled working directories and lookup paths.

### Module 2 — Filesystem Objects, Links and Access

#### Outcomes

- SEF3-O1
- SEF3-O4

#### Lessons

1. **Tree, names and objects** — Inspect a disposable filesystem tree and distinguish a pathname/directory entry from the object it names, with ordinary and dot-prefixed names.
2. **Bounded file manipulation** — Create, copy, rename, move and remove individually chosen fixtures; compare predicted and actual inventories and confirm an unrelated sentinel is unchanged.
3. **Unusual operands** — Inspect filenames containing spaces, literal wildcards, newlines and a leading dash without treating line-formatted terminal output as proof of exact filename identity.
4. **Hard links and symbolic links** — Compare identity, link counts, link-target path resolution, dangling links and what removing an original name does to each.
5. **Users, groups and effective permissions** — Predict read/write/search failures using the effective unprivileged identity, mode bits and parent-directory search requirements; distinguish a permission denied on a directory from a file's own mode.
6. **Mode changes and umask** — Observe the actual creation masks and mode changes on owned fixtures only, restore the state afterward and acknowledge ACL/mount-policy effects where relevant.
7. **A scoped mutation decision** — Define the target path, allowed object and fixture boundary before each operation; explain why quoting and lexical containment checks alone cannot establish a race-free security boundary.

*Optional practice:* Predict which links remain valid after deleting one original filename and demonstrate a directory-search failure without modifying system-wide permissions.

### Module 3 — Expansion, Quoting and Arguments

#### Outcomes

- SEF3-O2
- SEF3-O8

#### Lessons

1. **Arguments as actual values** — Display each argument and its boundary using a harmless numbered-argument helper; distinguish the original command text from the resulting argv.
2. **Variables, empty and unset parameters** — Compare quoted/unquoted expansion, word splitting and an unset variable with an explicitly empty one; diagnose arguments unexpectedly disappearing.
3. **Quotes and positional parameters** — Trace single and double quoting, escaping, `"$@"` and `"$*"` for spaces, empty elements and newlines without conflating their argument counts.
4. **Globbing and other expansions** — Predict pathname matching (hidden and unmatched names) separately from Bash brace, tilde and arithmetic expansion; record the actual shell options that affect matching.
5. **Command substitution** — Trace captured stdout and removed trailing newlines, distinguish a Bash subshell effect and explain why command substitution is not a safe arbitrary-filename transport.
6. **Expansion defect and regression** — Seed unquoted expansion in a read-only script, predict its failing argv, correct it without `eval`, and verify with an unfamiliar filename.

*Optional practice:* Compare a literal wildcard filename with a pattern that matches several files, using an argument display rather than a mutating shell command.

### Module 4 — Streams, Pipelines and Error Semantics

#### Outcomes

- SEF3-O3
- SEF3-O10

#### Lessons

1. **Three standard streams** — Demonstrate stdin, stdout and stderr using local synthetic input and a helper that deliberately emits different output and error messages.
2. **Redirection is ordered** — Predict and verify the different destinations produced by `2>&1 >out` versus `>out 2>&1`, and distinguish file creation from a successful pipeline.
3. **Pipeline dataflow** — Trace filters and stream connections across stages, identifying which process consumes and produces each observed record.
4. **Detect hidden upstream failure** — Compare Bash default pipeline status to `pipefail` after a middle-stage failure; distinguish POSIX.1-2024's standardized option from an older shell's actual support.
5. **Why `set -e` is not a complete contract** — Reproduce failures in a condition, AND/OR list and subshell, documenting when the shell continues and why deliberate status checks remain necessary.
6. **Do not publish a partial report** — Independently derive expected output from a small input fixture, inject a failing stage, and verify that a plausible-but-incomplete result is not treated as success.

*Optional practice:* Capture pipeline output and the actual status separately for both a valid record fixture and a failing command inside a pipeline.

### Module 5 — Owned Processes, Jobs and Signals

#### Outcomes

- SEF3-O4
- SEF3-O10

#### Lessons

1. **Process state and identity** — Identify a specific child started by the learner, distinguishing process identity, PID, shell job number, foreground/background status and program name.
2. **Start, observe and wait** — Launch a bounded helper, inspect it and collect its actual exit or wait status; explain why visible output does not prove successful completion.
3. **Signal a verified child** — Send a catchable signal only to the explicitly identified owned process; distinguish normal exit from signal termination and avoid unsafe broad PID/name selection.
4. **Ownership and reuse hazards** — Explain why PIDs may be reused and why a recorded number alone is not a secure ownership capability against hostile concurrency; record the narrow nonadversarial exercise boundary.
5. **Process cleanup and limits** — Reap or wait for owned children, restore disposable state and explain when abrupt termination or a signal prevents a cleanup path.

*Optional practice:* Predict the status and observable state of an owned background child after one graceful termination, then compare with a real observation.

### Module 6 — Inherited Environments and Startup

#### Outcomes

- SEF3-O5
- SEF3-O8
- SEF3-O11
- SEF3-O14

#### Lessons

1. **Export and inherited state** — Compare shell-local, exported and one-command environment assignments using a child; identify which values stay confined to the parent.
2. **Functions, sourced code and subshells** — Trace variable and directory changes through a shell function, `( ... )`, `$(...)` and an external process without falsely attributing child changes to the parent.
3. **PATH and command lookup** — Reproduce an unavailable-command failure under a deliberately restricted PATH, then repair it with a documented executable path or actual dependency.
4. **Bash startup modes** — Explain login versus non-login, interactive versus noninteractive invocation and `BASH_ENV` using trusted disposable startup files, not real user profiles.
5. **Editing user-controlled configuration** — Use an available terminal editor on a local fixture and distinguish program availability from its configuration; consult package-manager help without installing a package.
6. **Simulated scheduled execution** — Model a scheduler's missing PATH, locale and working directory using bounded `env -i` and explicit command paths without creating a real cron job.
7. **Locale and observable output** — Compare a supported locale with `LC_ALL=C` for sorting or regex classification, recording encoding assumptions instead of assuming all hosts share a locale.
8. **A causal environment investigation** — Predict, reproduce and correct an unfamiliar lookup, startup or inherited-variable defect while reporting only selected non-sensitive environment evidence.

*Optional practice:* Compare two children, one inheriting an exported variable and another observing a one-command assignment, then verify that the parent is unchanged.

### Module 7 — Searching, Text Processing and Reports

#### Outcomes

- SEF3-O3
- SEF3-O6

#### Lessons

1. **Choose files from a bounded tree** — Inspect `find` predicates, input roots and symlink policy, distinguishing traversal from an unsafe newline-delimited filename list.
2. **Specify a record and error contract** — Define a small local log format, accepted severities, malformed-record handling and an independently calculated count-by-category oracle.
3. **Regular expressions with an edition** — Distinguish basic/extended expressions and local tool behavior, test anchored matches and interpret no-match versus tool-error exit codes.
4. **Filter and transform records** — Combine documented `grep`, `cut` and `sed` (or equivalents) with explicit delimiters, handling empty and malformed lines.
5. **Order and count deterministically** — Use `sort`, `uniq` and `wc` under a stated locale; verify output independently and diagnose duplicate or missing groups.
6. **Archive/help boundaries** — Inspect optional local archive, compression and networking diagnostics from help pages or loopback state; do not install tools or assume extracting an untrusted archive is safe.

*Optional practice:* Create a local log with a malformed row, predict the count table, then test the empty and no-match cases without contacting any network service.

### Module 8 — Bash Script Contracts and Debugging

#### Outcomes

- SEF3-O7
- SEF3-O8

#### Lessons

1. **Write a public CLI contract** — Define accepted arguments, mode, input/output format, success and nonzero error statuses for one reusable read-only Bash helper.
2. **Functions and control flow** — Decompose parsing, validation, transformation and reporting; select `if`, `case`, `while`, `until` or `for` based on real control requirements.
3. **Dynamic arguments and Bash arrays** — Use positional parameters and arrays to preserve real argument boundaries, distinguishing Bash constructs from portable `sh` syntax.
4. **Input validation and standard input** — Use `read -r` for a declared line-oriented data format; distinguish a record delimiter from arbitrary filename bytes and reject invalid input deliberately.
5. **Meaningful command failure** — Keep important subprocess errors and nonzero statuses visible instead of hiding them with a successful echo, broad catch or assumption that `set -e` solves every case.
6. **Minimal reproductions and corrective reasoning** — Reproduce a quoting bug, a missing argument and a swallowed external failure in an owned script; state the hypothesis and the precise bounded change.
7. **Independent regression cases** — Run normal, empty, odd-name, malformed and injected-error examples with expected values derived separately from the implementation.

*Optional practice:* Repair a supplied Bash helper that mishandles `"$@"`, then demonstrate the repaired argument count for an unfamiliar input.

### Module 9 — Safe Path Batches, Temporary State and Cleanup

#### Outcomes

- SEF3-O8
- SEF3-O9
- SEF3-O10

#### Lessons

1. **Define allowed mutations** — Establish an owned input/output root and sentinel fixtures before any batch action; distinguish lexical path checks from underlying filesystem identity.
2. **Arbitrary filenames** — Show why `for f in $(find ...)` breaks on spaces, newlines and wildcards; represent names with precise argument boundaries, not human-oriented lines.
3. **NUL-delimited enumeration** — Use a locally verified `find -print0` with Bash `read -r -d ''` or a supported equivalent; distinguish the POSIX.1-2024 `find`/`xargs` options from Bash-only `read -d` and earlier implementations.
4. **Symlink and concurrency policy** — Reject or explicitly handle symlinks, leading-dash operands and unsafe output destinations; explain why check-then-use logic does not protect against an adversarial directory swap.
5. **Owned staging and safe publication** — Create uniquely named staging under a verified fixture root and require successful validation and processing before replacing a report; do not delete an old valid output on a new failure.
6. **Traps, signals and repetition** — Limit traps to the recorded staging location, preserve original failure status, repeat a run and explain the cleanup limits of `SIGKILL`, crashes and power loss.
7. **Fault and sentinel verification** — Inject a processing error and catchable interruption, inspect exact results/exit status and compare unaffected fixture bytes and staging inventories to independent expectations.

*Optional practice:* Inspect a path list containing whitespace and a newline without mutation; predict which unsafe loop would split the entries before checking the actual result.

### Module 10 — POSIX, Bash and Utility Compatibility

#### Outcomes

- SEF3-O3
- SEF3-O7
- SEF3-O11
- SEF3-O13
- SEF3-O14

#### Lessons

1. **Standard editions versus installations** — Compare POSIX.1-2024 requirements, older target editions, the observed `sh` and Bash implementations and external utilities instead of treating one environment as every target.
2. **Implement a POSIX-sh helper** — Use documented quoting, `case`, `test`, `printf`, standard loops and explicit error status in a bounded read-only script with independently checkable results.
3. **Interpreter selection** — Compare direct shebang invocation, `sh script` and `bash script`; identify the real `sh` implementation and avoid claiming independent-shell verification when it is Bash.
4. **Bash-only counterpart** — Exercise arrays or `[[ ... ]]` under Bash and the installed `sh`, reporting actual behavior rather than assuming every Bash-backed `sh` must reject the feature.
5. **Pipeline edition and failure control** — Recognize that `pipefail` is **POSIX.1-2024**, not POSIX.1-2017; inspect actual interpreter support and explain `set -e`, substitution and pipeline failure exceptions.
6. **Utility provenance and locale** — Compare `find`, `xargs`, `grep`, `sed`, `sort` and `date` options with the declared target edition; identify Issue 8 `-print0`/`-0`, GNU-only options and locale-sensitive behavior.
7. **Operand and path portability** — Check leading-dash names, utility-specific `--`, symlink policies and the limits of pathname quoting; distinguish compatibility from hostile-filesystem security.
8. **Evidence-backed compatibility decision** — Build an observed helper/interpreter/tool/locale matrix, preserve failing-case diagnostics and defend a constrained portable subset or intentional Bash/GNU dependency.

*Optional practice:* Run a portable `case` helper and Bash-array alternative under both available interpreters, noting any untested shell and utility versions.

### Module 11 — Integrated Offline Shell Toolkit and Defense

#### Outcomes

- SEF3-O6
- SEF3-O7
- SEF3-O8
- SEF3-O9
- SEF3-O10
- SEF3-O11
- SEF3-O12
- SEF3-O13
- SEF3-O14

#### Lessons

1. **Define the two-script toolkit** — State log syntax, report contract, input/output fixture boundaries and independently derived counts; reuse the preceding read-only reporting function.
2. **Coordinate stages and publish safely** — Join parser and staged-report coordinator with explicit argument, output and status contracts, refusing partial publication after any required failed stage.
3. **Test success and failure** — Verify clean, repeated, empty, malformed, odd-name and injected-failure runs against expected status and exact report/sentinel bytes.
4. **Exercise environments and compatibility** — Reuse the toolkit to test restricted `env -i` execution and a POSIX-sh helper versus Bash-specific equivalent, recording interpreter and external utility assumptions.
5. **Find and repair an unfamiliar defect** — Distinguish a quoting, data, permissions, shell-status, startup or utility-option cause with an isolated reproduction and independently checkable fix.
6. **Independent technical defense** — Provide reproducible instructions and an outcome-to-evidence map, explain one design trade-off and model limitation, and defend a reviewer-selected changed fixture.

*Optional practice:* Have a peer reproduce the bounded toolkit with a changed log input and an intentionally failed command, without any paid tool or real customer data.

## Completion requirements

### Assessment environment and safety

Complete the seven required assessments with a documented nonprivileged Bash 5.x (or compatible Bash) environment and generated, non-sensitive fixtures. Specify the shell, operating-system/tool versions, locale when output ordering matters, exact commands, expected results, and actual results. Run all mutating tests inside a verified learner-owned fixture root, never through a broad cleanup command pointed at a home directory or unknown path. Do not use `sudo`, install packages system-wide, alter real startup files or crontabs, fetch remote data, or signal unrelated processes.

Some exercises use unusual pathnames, symlinks, redirection, signals, and injected failures. For each, establish the expected boundaries **before** executing commands; demonstrate that unrelated sentinel data remains unchanged. Filesystem exercises use learner-controlled, **nonadversarial fixtures**: quoting, path normalization and pre-operation checks do not provide race-free guarantees if another actor concurrently replaces a directory or symlink. Do not test on unrelated personal data or claim unsupported protection against hostile filesystem changes. Where a platform lacks an optional diagnostic utility, document the limitation and use a reproducible equivalent, not an undisclosed dependency. A separate network namespace or administrative capabilities are not needed.

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

- **SEF3-AS7** (required shell portability and process-environment verification)
  - Outcomes: SEF3-O3, SEF3-O5, SEF3-O7, SEF3-O8, SEF3-O11, SEF3-O12, SEF3-O13, SEF3-O14
  - Work: Reuse the existing SEF3-AS6 toolkit and extract one read-only report helper, not an unrelated new program. Implement a small POSIX-sh-compatible variant using quoted positional parameters, `case`, `test`, `printf`, standard loops, and explicit error checking. Exercise it under the available `sh` and Bash with a normal fixture, a path containing whitespace, an invalid argument and a deliberately failing command; record the actual `sh` implementation. Add or isolate a deliberately Bash-only variant using `[[ ... ]]` or arrays, run it under Bash and `sh`, and report the actual syntax/behavior difference; if `sh` is Bash, disclose that no independent shell was tested. Identify the `find`, `grep`, `sed` or other external utility flags required by these helpers, classify portability against an identified standard edition and local implementation (including whether the POSIX.1-2024 `pipefail`, `find -print0` and `xargs -0` requirements are used and actually supported), and demonstrate one meaningful supported option or interpretation difference or explain why a comparison is unavailable. Do not label `pipefail` unconditionally Bash-only or assume that an older installed `sh` implements the newest edition. Reproduce a controlled `env -i` invocation with explicit safe `PATH`, locale and changed working directory; show an unexported shell value absent in a child, a one-command assignment, and at least one expected command-lookup or startup assumption failure and its repair. Present an interpreter/tool/locale compatibility matrix and defend the intended portability boundary under an unfamiliar reviewer-provided fixture.
  - Criteria: The claimed portable helper uses an appropriate POSIX-sh subset and documented external options; real runs correctly handle whitespace, known invalid inputs and intentional command failures without touching unrelated files. A Bash-only feature is identified as such, not mislabeled POSIX portable; `bash --posix` or a Bash-backed `sh` is never claimed to prove independent portability. Predictions accurately separate exported variables from shell-local state, child/subshell effects, startup mode, working directory, `PATH`, locale, and observed process status. Utility provenance and unknown versions are transparently documented; portability does not rest on an assumption that a GNU option works everywhere. Input/sentinel safety and failure propagation remain intact, and a new or seeded defect is diagnosed and repaired. No root privileges, extra package installation, real cron modification, real startup-file edits, external network access or proprietary tools are needed.
  - Evidence: Reused toolkit and two small helper variants, interpreter/shebang and external-utility compatibility matrix, actual `sh` identity, versions and optional reference documentation, scripts and reproducible fixture commands, before/after sentinel checks, stdout/stderr/status for normal and failing cases, controlled-environment and locale trace without sensitive variables, independent reference counts, a defect/fix regression, and an accessible technical defense.

### Completion decision

A learner completes SEF3 when **all seven required summative assessments** meet their published criteria and collectively demonstrate SEF3-O1 through SEF3-O14. Assessed source and fixture work may be reused and expanded across the seven assessments; learners are not required to write six unrelated utilities or duplicate a quiz and lab in every module. Optional practice and course lessons support learning but are not unannounced completion gates.

A reviewer records each assessment decision with the required inspectable evidence and may request bounded clarification on unfamiliar, but equivalent, inputs under the published criteria. Safety-critical mistakes, hidden dependencies, and non-reproducible output must be corrected before a passing decision. Learner work stays under learner control; sharing raw private machine state, production credentials, or sensitive data is never required. The course itself remains `draft`; an automated structural pass does not satisfy the learner-feedback and reviewer thresholds in [Status Labels](../../spec/status-labels.md).

### Revision history and evidence compatibility

[Accepted RFC 0003](../../rfcs/0003-sef-academic-progression.md) authorized focused SEF3 educational hardening. The historical reference is [SEF3 at commit `1fb369a251a093736f63fa1cfa95656ded87ad99`](https://github.com/0xbuffdev/open-engineering-education/blob/1fb369a251a093736f63fa1cfa95656ded87ad99/curriculum/SEF/SEF3.md) and must remain immutable when interpreting old work.

- **Unchanged:** `SEF3-O1`–`O12` retain their original descriptions, and `SEF3-AS1`–`AS6` retain their original Work, Criteria, Evidence and review variation. Existing completion claims remain pinned to that source revision.
- **Added:** `SEF3-O13` establishes demonstrated shell and utility portability, and `SEF3-O14` establishes reproducible environment reasoning. They are assessed by the new `SEF3-AS7` using the existing shell toolkit, not a new independent project.
- **Earlier study-plan extension:** A previous revision introduced two instructional modules for explicit environment and portability reasoning and provisionally increased duration from eight to 10–12 weeks. The present competency-derived realignment consolidates overlapping instruction without removing these competencies or adding mandatory labs or quizzes.
- **No automatic equivalence:** Prior learner completion is neither deleted nor silently marked complete against new outcomes; an evidence-based review must establish current readiness for the new requirements. The course still has `draft` status, and the downstream SEF7 C/POSIX system-interface assessment remains unchanged.

The current editorial review retains all fourteen existing outcome statements, seven assessment identities, prerequisite and `draft` status. POSIX.1-2024 clarifications refine the examples within the published shell-compatibility competency; historical evidence stays tied to its assessed course revision. No earlier pass is automatically treated as proof of newly explicit edition-specific cases.
