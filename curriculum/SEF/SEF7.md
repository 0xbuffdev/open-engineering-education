> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

# SEF7 — Unix System Interfaces

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** SEF3, SEF6
**Duration:** 4 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

## Overview

This course shows how programs ask the operating system for services. Learners write C programs that use system calls to work with files, directories, and processes, and a minimal client and server that communicate over TCP. The emphasis is on the interface between a program and the kernel, observed from the user's side of the boundary.

## Course brief

The course introduction is the first lesson of the first module. It combines the overview above with these fields.

- **Introduction:** All software ultimately asks the operating system for services. This course shows that interface from the program's side: system calls for files, processes, and networking.
- **History:** The system-call interface of Unix took its form between 1969 and 1973. The Berkeley sockets interface for networking appeared in 4.2BSD in 1983, and POSIX standardized the core interface in 1988.
- **Usage:** The learner calls the kernel directly from C and traces the calls a program makes.
- **Applications:** Shells, servers, build tools, file utilities, and every program that runs on a Unix-like system.
- **Strengths:** A small, uniform, well-documented interface gives access to the whole operating system.
- **Limitations:** Calls fail in many ways, return partial results, and are easy to misuse, which is why the SYS program teaches robust techniques and safer languages.
- **Key concepts:** system call; file descriptor; process; fork; exec; wait; metadata; permission bits; client and server; socket

## Prerequisites

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

#### Module brief

- **Introduction:** A program cannot touch hardware directly. It asks the kernel through system calls.
- **Overview:** It covers the boundary between user space and the kernel, system calls and error handling, file descriptors, reading and writing, and redirection.
- **History:** Unix's small set of system calls and the file descriptor abstraction date from 1969 to 1973, and POSIX standardized them in 1988.
- **Limitations:** Each call has a cost, can fail in many ways, and can be interrupted or return less data than requested.
- **Key concepts:** system call; errno; file descriptor; offset; read and write; duplication of descriptors

#### Module outcomes

By the end of this module, the learner can:

- Explain what a system call is, what happens when one fails, and how to check for failure.
- Use file descriptors to read, write, and reposition within files.

1. **Course introduction: Unix System Interfaces** — what the subject is, where it came from, where it is used, and its strengths and limits
2. **Introduction: System Calls & File Descriptors** — what the topic is, where it is used, and its strengths and limits
3. **The user and kernel boundary**
4. **System calls and error handling**
5. **File descriptors**
6. **Reading, writing, and file offsets**
7. **Descriptors, duplication, and redirection**
8. **System interfaces**
   - kind: `test`
9. **Trace file descriptors** — trace the system calls made by a small program, predict which descriptors exist at each step, and explain how shell redirection changes them
   - kind: `lab`

### Module 2 — Processes

#### Module brief

- **Introduction:** Every running program is a process. This module shows how Unix creates and ends them.
- **Overview:** It covers the process abstraction, fork, exec, waiting for children, exit status, and what a child inherits.
- **History:** The fork and exec model was part of the first Unix and separates creating a process from running a program.
- **Limitations:** Forking a large process is costly, and zombie and orphan processes need care.
- **Key concepts:** process; process ID; fork; exec; wait; exit status; inheritance

#### Module outcomes

By the end of this module, the learner can:

- Create a child process, run another program in it, and collect its exit status.
- Explain what a child inherits from its parent.

1. **Introduction: Processes** — what the topic is, where it is used, and its strengths and limits
2. **The process abstraction**
3. **Creating processes with `fork`**
4. **Running programs with `exec`**
5. **Waiting for children and exit status**
6. **What a child inherits**
7. **Processes**
   - kind: `test`
8. **Start a child process** — write a launcher that starts a program, waits for it, and reports how it ended, including a deliberate failure case
   - kind: `lab`

### Module 3 — Files, Directories & Permissions

#### Module brief

- **Introduction:** Files carry metadata, and directories are special files. This module shows how programs read them.
- **Overview:** It covers file metadata, permission bits in code, directories, and hard and symbolic links.
- **Limitations:** A file can change between a check and its use, which creates race conditions, and links create surprising paths.
- **Key concepts:** inode; metadata; mode bits; directory entry; link

#### Module outcomes

By the end of this module, the learner can:

- Read file metadata and interpret type, size, ownership, and permission bits in code.
- Walk a directory and handle links correctly.

1. **Introduction: Files, Directories & Permissions** — what the topic is, where it is used, and its strengths and limits
2. **File metadata**
3. **Permission bits in code**
4. **Directories**
5. **Hard and symbolic links in code**
6. **Files and directories**
   - kind: `test`
7. **Read file metadata** — build a small program that lists directory entries with type, size, and permissions, matching the output of a standard tool
   - kind: `lab`

### Module 4 — Networking Basics

#### Module brief

- **Introduction:** Programs on different machines talk over networks. This module introduces the client and server model and sockets.
- **Overview:** It covers the client and server roles, TCP/IP basics, the sockets interface, and a minimal TCP client and server.
- **History:** The ARPANET switched to TCP/IP on 1 January 1983, and the same year Berkeley's 4.2BSD introduced the sockets interface.
- **Limitations:** Networks lose, delay, and reorder data, and TCP's byte stream has no message boundaries.
- **Key concepts:** client; server; port; TCP; socket; listen, accept, and connect

#### Module outcomes

By the end of this module, the learner can:

- Explain the client/server model, ports, and the TCP connection lifecycle.
- Write a minimal TCP client and server and trace one connection.

1. **Introduction: Networking Basics** — what the topic is, where it is used, and its strengths and limits
2. **Client and server**
3. **TCP/IP basics**
4. **The sockets interface**
5. **A minimal TCP server and client**
6. **OS and network boundaries**
   - kind: `test`
7. **Connect two programs over TCP** — build a client and a server that exchange one message, trace the connection, and explain what each system call does
   - kind: `lab`

### Module 5 — Mini Unix Utility

#### Module brief

- **Introduction:** This lab integrates the course. The learner builds a small C utility on top of system calls and explains each one it makes.
- **Overview:** It combines file descriptors, processes, directory and metadata access, error handling, and tests.
- **Applications:** Command-line tools such as ls, cp, and shells are built from exactly these calls.
- **Key concepts integrated:** system calls; descriptors; processes; metadata; error handling; tracing

1. **Build, test, and defend the Mini Unix Utility**
   - kind: `lab`

## Topics

- System calls
- User space and kernel space
- File descriptors
- Low-level file I/O
- Error handling with system calls
- Process creation and execution
- Waiting for children
- File and directory metadata
- Permission bits
- Client/server model
- TCP/IP basics
- Sockets

## Practical exercises

2. Trace the system calls of a program.
3. Trace file-descriptor behavior and redirection.
4. Start a child process with `fork()` and `exec`.
5. List a directory with metadata.
6. Connect two programs over TCP.

## Course lab

**Mini Unix Utility**

Build a small C command-line utility that uses files, directories, and processes through system calls, such as a simplified `ls`, `cp`, or process launcher. The utility must include:

- Correct error handling for every system call
- A test script that checks behavior and failure cases
- A trace of the system calls it makes, with a short explanation
- A short note identifying three failures that C permits and Python would reject, and how the utility guards against them

## Exit check

The learner can explain what happens between a user's command and the operating system's work, and can demonstrate it with a Linux program that makes system calls.
