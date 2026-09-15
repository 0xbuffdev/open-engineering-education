# Foundations Practice Guide

Use these briefs after checking the corresponding section of [curriculum.md](../curriculum.md#track-1--foundations). Make one numbered lab directory per experiment and one file/subdirectory per exercise in the generated course workspace.

## F0 — Foundation Setup

### Labs

1. **Environment recovery drill.** Record OS, editor, Git, Python, and shell versions; create `hello.py`; then deliberately restore a changed file with Git. Evidence: terminal transcript and a clean `git status`.
2. **Scratch-repository workflow.** Make a private scratch repository with a branch, a small edit, a merge, and a tagged checkpoint. Evidence: `git log --graph` screenshot/text and a one-paragraph explanation of each command.

### Exercises

1. From a blank terminal, create a directory, create a text file, list hidden files, print a file, and remove only the test file. Write the commands and what each does.
2. Initialise a repository, make two focused commits, inspect a diff, and restore one file version without deleting the repository.
3. Write a one-page personal setup/runbook: backups, update cadence, where project environments live, and how you will keep secrets out of Git.

**Ready when:** you can repeat either lab without notes and fill in the F0 resource log.

## F1 — Computing and Programming Foundations (Python)

### Labs

1. **Bits to bytes.** Encode a short ASCII/UTF-8 message by hand, inspect its bytes with a tool, and show how an intentional invalid byte sequence fails or is replaced. Do not use this as a Unicode standard study; focus on representation.
2. **Habit tracker CLI.** Build a command-line tracker that can add, list, mark, and persist habits in JSON or CSV. Include malformed-file handling, a help command, and a manual test transcript.

### Exercises

Implement these as twelve small programs, each with a normal and invalid/boundary example:

1. unit conversion and integer/float edge cases;
2. grade or tariff calculation with conditionals;
3. loop-driven number statistics;
4. string normalization and word counting;
5. list/dictionary aggregation;
6. a pure function with docstring and tests;
7. a function that raises a useful exception;
8. CSV reader that rejects malformed rows;
9. JSON round trip with a schema check;
10. command-line argument parsing without global state;
11. a deliberately broken off-by-one program and diagnosis; and
12. a deliberately broken file-handling program and diagnosis.

**Ready when:** the tracker can be cloned/run on a clean environment and you can explain the path from source file to running process.

## F2 — Data Structures and Algorithms

### Labs

1. **Structure-choice study.** Implement a contact/index lookup using a list, sorted list, and hash map. Count operations or time sufficiently large deterministic inputs; explain when each choice is appropriate.
2. **Graph route finder.** Use an adjacency-list graph and BFS to find the shortest unweighted path. Include an unreachable target and a malformed graph case.

### Exercises

Implement and test, without substituting a ready-made equivalent:

1. stack and queue with underflow behaviour;
2. singly linked list with insert, delete, and invariant checks;
3. binary-search tree with traversal and duplicate-key policy;
4. recursive and iterative binary search;
5. merge sort and quicksort with duplicate-heavy input;
6. BFS and DFS with visited-set reasoning;
7. complexity traces for common operations; and
8. 30 labelled practice problems: 10 arrays/strings, 8 maps/sets, 6 recursion/trees, and 6 graphs/search. Record the first failed approach for at least five.

**Ready when:** you can defend a structure choice, give operation costs, and trace recursion by hand.

## F3 — Engineering Practice: Git, Testing, Debugging, C, and Linux CLI

### Labs

1. **Git recovery lab.** In a disposable repository create a merge conflict, resolve it intentionally, inspect the merge base, and recover one accidental change using a non-destructive Git command. Keep the command log and explain the recovery choice.
2. **C failure investigation.** Write a small C program with a null/dangling-pointer or bounds bug in an isolated local program. Compile with strict warnings and sanitizers where available, capture the diagnosis, repair it, and add a regression test. Never run untrusted binaries.

### Exercises

Complete 15 small C drills: declarations/types, control flow, functions, arrays, strings, structs, files, `argc`/`argv`, pointers, pointer arithmetic, heap allocation, freeing, error returns, a unit-test harness, and a Makefile or documented compile command. Also:

1. add tests to two F2 implementations;
2. reproduce and explain one compiler warning before fixing it;
3. inspect a binary with `file`, `nm`, and a debugger; and
4. write a debugging note that distinguishes symptom, root cause, fix, and prevention.

**Ready when:** your C drills compile with `-Wall -Wextra -Werror`, tests run from a documented command, and the pointer model is clear.

## F4 — Mathematics for Computing and AI

### Labs

1. **Simulation versus theory.** Simulate dice/coin experiments with a fixed seed, compare empirical and expected probabilities at increasing sample sizes, and plot or tabulate convergence.
2. **Numerical gradient check.** Implement a small scalar/vector loss, derive its gradient, compare it with a finite-difference approximation across several step sizes, and explain the error curve.

### Exercises

1. translate logic statements into truth tables and simple set operations;
2. count arrangements with permutations/combinations and state assumptions;
3. hand-compute vector operations and two small matrix products;
4. solve a small linear system and identify singular/non-invertible cases;
5. differentiate polynomials and use the chain rule;
6. calculate conditional probability and Bayes’ rule from a contingency table;
7. compute mean, median, variance, and standard deviation for a tiny sample; and
8. read and explain summation, gradient, and Big-O notation from one selected formula per symbol.

**Ready when:** the worked solutions show assumptions, not only answers, and the code checks agree with hand calculations.
