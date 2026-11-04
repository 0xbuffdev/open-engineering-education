# SEF7 — Unix System Interfaces

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF3](SEF3.md), [SEF6](SEF6.md)
**Duration:** 4 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course shows how programs ask the operating system for services. Learners write C programs that use system calls to work with files, directories, and processes, and a minimal client and server that communicate over TCP. The emphasis is on the interface between a program and the kernel, observed from the user's side of the boundary.

- [**SEF3 — Linux & the Command Line**](SEF3.md)
- [**SEF6 — C Programming & Machine Memory**](SEF6.md)

## Learning outcomes

By the end of the course, the learner will be able to:

- Explain what a system call is and use system calls from C with correct error handling.
- Use file descriptors for file input and output, and explain how redirection works at the system-call level.
- Create, run, and wait for processes with `fork`, `exec`, and `wait`.
- Read file and directory metadata, including permissions.
- Explain the client/server model and TCP/IP at a basic level, and write a minimal TCP client and server.
- Build a small Unix command-line utility and explain which system calls it makes.

## Modules

### Module 1 — System Calls & File Descriptors

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Course introduction: Unix System Interfaces** — `lesson` — what the subject is, where it came from, where it is used, and its strengths and limits
2. **The user and kernel boundary** — `lesson`
3. **System calls and error handling** — `lesson`
4. **File descriptors** — `lesson`
5. **Reading, writing, and file offsets** — `lesson`
6. **Descriptors, duplication, and redirection** — `lesson`
7. **System interfaces** — `test`
8. **Trace file descriptors** — `lab` — trace the system calls made by a small program, predict which descriptors exist at each step, and explain how shell redirection changes them

### Module 2 — Processes

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **The process abstraction** — `lesson`
2. **Creating processes with `fork`** — `lesson`
3. **Running programs with `exec`** — `lesson`
4. **Waiting for children and exit status** — `lesson`
5. **What a child inherits** — `lesson`
6. **Processes** — `test`
7. **Start a child process** — `lab` — write a launcher that starts a program, waits for it, and reports how it ended, including a deliberate failure case

### Module 3 — Files, Directories & Permissions

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **File metadata** — `lesson`
2. **Permission bits in code** — `lesson`
3. **Directories** — `lesson`
4. **Hard and symbolic links in code** — `lesson`
5. **Files and directories** — `test`
6. **Read file metadata** — `lab` — build a small program that lists directory entries with type, size, and permissions, matching the output of a standard tool

### Module 4 — Networking Basics

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Client and server** — `lesson`
2. **TCP/IP basics** — `lesson`
3. **The sockets interface** — `lesson`
4. **A minimal TCP server and client** — `lesson`
5. **OS and network boundaries** — `test`
6. **Connect two programs over TCP** — `lab` — build a client and a server that exchange one message, trace the connection, and explain what each system call does

### Module 5 — Mini Unix Utility

#### Outcomes

- Integrate and demonstrate the course capabilities through the module's final practical work.

#### Lessons

1. **Build, test, and defend the Mini Unix Utility** — `lab`

## Completion requirements

- Complete the required exercises and checkpoints described in the [public course requirements](requirements/SEF7.md).
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).
