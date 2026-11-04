# SEF7 — Required practical work and evaluation

> Public draft requirements preserved from the source. Independent learners can use these without a 0xNAND subscription. Detailed lab procedures and verification fields still require conformance review.

## Practical exercises

- Trace the system calls of a program.
- Trace file-descriptor behavior and redirection.
- Start a child process with `fork()` and `exec`.
- List a directory with metadata.
- Connect two programs over TCP.

## Course lab

### Mini Unix Utility

Build a small C command-line utility that uses files, directories, and processes through system calls, such as a simplified `ls`, `cp`, or process launcher. The utility must include:

- Correct error handling for every system call
- A test script that checks behavior and failure cases
- A trace of the system calls it makes, with a short explanation
- A short note identifying three failures that C permits and Python would reject, and how the utility guards against them

## Exit check

The learner can explain what happens between a user's command and the operating system's work, and can demonstrate it with a Linux program that makes system calls.
