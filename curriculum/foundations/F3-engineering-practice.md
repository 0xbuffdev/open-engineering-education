# F3 — Engineering Practice: Git, Testing, Debugging, C & Linux

**Track:** Foundations · **Prerequisite:** F1, F2 · **Core** · **Time:** 8 weeks, 120 hours · **Project:** P1 hardened + P2 sysprobe (C)
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

This is the craft course. You will learn how professional code is versioned, tested, debugged, built, and run on Linux, then learn C well enough to see the machine underneath Python. C is not optional for the Systems and Security tracks; it is the language of pointers, memory, syscalls, and exploitation.

## Outcomes

You can:

- use Git branches, merges, rebases, bisect, and reflog without fear;
- write unit, integration, and property-based tests;
- debug with a debugger, sanitizers, `strace`, and core dumps;
- compile C with strict warnings and explain undefined behaviour;
- use pointers, arrays, strings, structs, unions, and manual memory correctly;
- read a linker error and explain the compilation/linking pipeline;
- use the Linux shell, permissions, processes, signals, and job control;
- add CI that runs tests, lint, and type checks.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B2 *The C Programming Language* | Ch. **1–3**, §§**5.1–5.4** | C syntax, types, control flow, functions, pointers |
| B2 | Ch. **4**, §§**5.5–5.12**, Ch. **6** | Recommended: scope, preprocessor, strings, function pointers, structs |
| B2 | §§**7.5–7.8**, §§**8.1–8.4**, §**8.7** | File access, errors, syscalls, allocator |
| B1 *But How Do It Know?* | “Hardware and Software” through “Boots” | Programs, OS, files, errors, firmware, boot |
| B5 *The Linux Programming Interface* | Ch. **2–3** | OS concepts, syscalls vs library functions, errors |
| [Pro Git](https://git-scm.com/book/en/v2) | Ch. 2–3, 6–7 | Branching, merging, rebasing, recovery |
| [pytest](https://docs.pytest.org/) and [Hypothesis](https://hypothesis.readthedocs.io/) | Get started, fixtures, parametrization, property tests | Testing practice |
| [GDB documentation](https://sourceware.org/gdb/current/onlinedocs/gdb/) | Breakpoints, watchpoints, backtrace, core files | Debugging |

## Modules

### 1. Git as a tool, not a ritual

- objects, refs, index, working tree;
- commit graph, merge vs rebase, fast-forward;
- conflict resolution and merge base;
- `bisect`, `reflog`, `restore`, `revert`, `reset` (soft/mixed/hard);
- tags, releases, hooks;
- code review: small diffs, clear messages, review comments;
- `.gitignore`, large files, secrets, signed commits (optional).

### 2. Testing

- unit vs integration vs end-to-end;
- arrange–act–assert, fixtures, parametrization;
- boundary, invalid, and property-based tests;
- mocking and when not to mock;
- coverage as a diagnostic, not a target;
- flaky tests and determinism;
- test data and golden files;
- CI: run tests, lint, type check, and build on every push.

### 3. Debugging

- reproduce, minimize, hypothesize, observe, fix, regress;
- `gdb`/`lldb`: breakpoints, watchpoints, stepping, backtrace, frame inspection;
- core dumps and `ulimit`;
- AddressSanitizer, UndefinedBehaviorSanitizer, ThreadSanitizer;
- `valgrind` for leaks;
- `strace`/`ltrace` for syscalls and library calls;
- logging vs printing;
- bisection and differential debugging.

### 4. C foundations

- translation units, declarations, definitions, linkage;
- types, sizes, signed/unsigned, integer promotion;
- operators, precedence, bitwise operations;
- control flow, functions, recursion;
- arrays, strings, null termination;
- pointers: values, addresses, dereference, arithmetic, `const`;
- pointers vs arrays, pointer-to-pointer, function pointers;
- structs, unions, bit-fields, alignment, padding;
- dynamic allocation: `malloc`, `calloc`, `realloc`, `free`;
- common bugs: leak, double free, use-after-free, out-of-bounds, dangling pointer, uninitialized read;
- undefined behaviour and why "it works on my machine" is not correctness;
- preprocessor, header guards, `static`, `extern`;
- build: `gcc -Wall -Wextra -Werror -std=c17`, `make`, intro to CMake;
- compile → assemble → link → load; symbols, relocations, shared libraries;
- ABI and calling conventions (preview of S1/S2).

### 5. Linux CLI and environment

- files, permissions, users, groups;
- processes, `fork`/`exec`, signals, job control;
- pipes, redirection, `xargs`, `find`, `grep`, `sed`, `awk`;
- environment variables, `PATH`, shell startup;
- package management, services, logs;
- SSH, `scp`/`rsync`, `tmux`;
- `/proc`, `/sys`, `man`, `--help`.

## Labs

### Lab 1 — Git recovery lab

Create a disposable repository with a merge conflict, a bad rebase, and an accidentally deleted commit. Recover each using a non-destructive command. Record the command log and explain why each choice was safe.

### Lab 2 — Test suite for F2

Add tests to two F2 implementations. Include normal, boundary, invalid, and one property-based test. Measure coverage and explain one uncovered branch that matters.

### Lab 3 — C drills (30 programs)

Write 30 small C programs:

1. declarations and sizes;
2. integer/float conversion;
3. bitwise operations;
4. control flow;
5. functions and recursion;
6. arrays and strings;
7. string library reimplementation (`strlen`, `strcpy`, `strcmp`);
8. structs and alignment;
9. unions and bit-fields;
10. file read/write;
11. `argc`/`argv`;
12. pointer arithmetic;
13. pointer-to-pointer;
14. function pointers;
15. `malloc`/`free`;
16. `realloc` growth;
17. error returns and `errno`;
18. a unit-test harness;
19. a Makefile;
20. a multi-file program with headers;
21. a linked list;
22. a hash table (reuse F2);
23. a dynamic array;
24. a binary search;
25. a sorting algorithm;
26. a small parser;
27. a signal handler;
28. a `fork`/`exec` wrapper;
29. a file-copy program with partial I/O;
30. a deliberately buggy program you diagnose and fix.

All compile with `-Wall -Wextra -Werror`.

### Lab 4 — Debugging investigation

Write a program with a null/dangling-pointer or bounds bug in an isolated local environment. Compile with sanitizers, capture the diagnosis, repair it, add a regression test, and write symptom → root cause → fix → prevention.

### Lab 5 — CI pipeline

Add a CI workflow that runs formatter check, linter, tests, and a build on push. Make it fail intentionally once, then fix it.

## Exercises

- 15 additional C exercises covering the topics above.
- 5 Git scenarios: undo a commit, recover a branch, split a commit, squash, resolve a conflict.
- 5 debugging scenarios: segfault, leak, race, infinite loop, wrong output.
- 3 written explanations: pointer vs object, undefined behaviour, why `-Werror` is useful.
- 1 code review of a peer or your own old code with at least five actionable comments.

## Project increment — P1 hardened + P2 sysprobe (C)

**P1:** add tests, CI, packaging, error handling, and a clean-install check.

**P2 start:** build a C program that prints its process ID, memory maps, open file descriptors, and the result of one syscall (`getpid`, `mmap`, `open`, or `fork`). This becomes the first module of the systems project.

**Brief:** [P1 — ledgerlab](../projects/project-ladder.md#p1--ledgerlab) · [P2 — sysprobe](../projects/project-ladder.md#p2--sysprobe)

## Exit check

- [ ] compile, test, and debug a C program from Linux;
- [ ] explain the difference between a pointer value and the object it addresses;
- [ ] demonstrate a Git merge conflict and a safe recovery;
- [ ] use a debugger to inspect a crash and a sanitizer to find a memory bug;
- [ ] explain the compile → link → load pipeline;
- [ ] show a CI run that executes tests and lint;
- [ ] read a man page and use a syscall correctly.

## Common failure modes

- Learning Git commands without understanding the commit graph.
- Chasing 100% coverage instead of testing failure modes.
- Ignoring compiler warnings.
- Using `gets`, `strcpy`, or unchecked `scanf`.
- Freeing memory twice or using it after `free`.
- Assuming `int` is 32 bits or `char` is signed everywhere.
- Debugging by random edits. Form a hypothesis first.

## Evidence to commit

- `labs/foundations/F3/` with C drills, debugging report, and CI config
- `exercises/foundations/F3/` with Git and debugging scenarios
- P1 hardened repository
- P2 sysprobe initial module
- `notes/foundations/F3/summary.md`

## Optional depth

- *Modern C* (Gustedt, free) for a more modern treatment.
- *Computer Systems: A Programmer's Perspective* Ch. 2–3, 7, 9 for data representation, assembly, linking, and memory.
- `cmake`, `pkg-config`, and shared-library versioning.
- `rr` or `perf` for record/replay debugging.
