# SEF7 — Lesson authoring notes

> Optional instructional context preserved from the original source. These are not required course metadata, assessments or module briefs.

## Course orientation

- **Introduction:** All software ultimately asks the operating system for services. This course shows that interface from the program's side: system calls for files, processes, and networking.
- **History:** The system-call interface of Unix took its form between 1969 and 1973. The Berkeley sockets interface for networking appeared in 4.2BSD in 1983, and POSIX standardized the core interface in 1988.
- **Usage:** The learner calls the kernel directly from C and traces the calls a program makes.
- **Applications:** Shells, servers, build tools, file utilities, and every program that runs on a Unix-like system.
- **Strengths:** A small, uniform, well-documented interface gives access to the whole operating system.
- **Limitations:** Calls fail in many ways, return partial results, and are easy to misuse, which is why the SYS program teaches robust techniques and safer languages.
- **Key concepts:** system call; file descriptor; process; fork; exec; wait; metadata; permission bits; client and server; socket

## Module 1 — System Calls & File Descriptors

- **Introduction:** A program cannot touch hardware directly. It asks the kernel through system calls.
- **Overview:** It covers the boundary between user space and the kernel, system calls and error handling, file descriptors, reading and writing, and redirection.
- **History:** Unix's small set of system calls and the file descriptor abstraction date from 1969 to 1973, and POSIX standardized them in 1988.
- **Limitations:** Each call has a cost, can fail in many ways, and can be interrupted or return less data than requested.
- **Key concepts:** system call; errno; file descriptor; offset; read and write; duplication of descriptors

## Module 2 — Processes

- **Introduction:** Every running program is a process. This module shows how Unix creates and ends them.
- **Overview:** It covers the process abstraction, fork, exec, waiting for children, exit status, and what a child inherits.
- **History:** The fork and exec model was part of the first Unix and separates creating a process from running a program.
- **Limitations:** Forking a large process is costly, and zombie and orphan processes need care.
- **Key concepts:** process; process ID; fork; exec; wait; exit status; inheritance

## Module 3 — Files, Directories & Permissions

- **Introduction:** Files carry metadata, and directories are special files. This module shows how programs read them.
- **Overview:** It covers file metadata, permission bits in code, directories, and hard and symbolic links.
- **Limitations:** A file can change between a check and its use, which creates race conditions, and links create surprising paths.
- **Key concepts:** inode; metadata; mode bits; directory entry; link

## Module 4 — Networking Basics

- **Introduction:** Programs on different machines talk over networks. This module introduces the client and server model and sockets.
- **Overview:** It covers the client and server roles, TCP/IP basics, the sockets interface, and a minimal TCP client and server.
- **History:** The ARPANET switched to TCP/IP on 1 January 1983, and the same year Berkeley's 4.2BSD introduced the sockets interface.
- **Limitations:** Networks lose, delay, and reorder data, and TCP's byte stream has no message boundaries.
- **Key concepts:** client; server; port; TCP; socket; listen, accept, and connect

## Module 5 — Mini Unix Utility

- **Introduction:** This lab integrates the course. The learner builds a small C utility on top of system calls and explains each one it makes.
- **Overview:** It combines file descriptors, processes, directory and metadata access, error handling, and tests.
- **Applications:** Command-line tools such as ls, cp, and shells are built from exactly these calls.
- **Key concepts integrated:** system calls; descriptors; processes; metadata; error handling; tracing

1. **Build, test, and defend the Mini Unix Utility**
   - kind: `lab`

## Original topic inventory

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
