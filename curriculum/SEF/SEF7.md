# SEF7 — Unix System Interfaces

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF3](SEF3.md), [SEF6](SEF6.md)
**Duration:** 7 weeks
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
- Use Unix system interfaces safely for robust file, process, signal, and basic TCP programs while documenting partial failures and resource ownership.

## Modules

### Module 1 — System Calls & File Descriptors

#### Outcomes

- Explain what a system call is, what happens when one fails, and how to check for failure.
- Use file descriptors to read, write, and reposition within files.

- Reproduce interrupted I/O and show correct loops for partial reads and writes.

#### Lessons

1. **Course introduction: Unix System Interfaces** — `lesson`

   All software ultimately asks the operating system for services. This course shows that interface from the program's side: system calls for files, processes, and networking.
2. **The user and kernel boundary** — `lesson`
3. **System calls and error handling** — `lesson`
4. **File descriptors** — `lesson`
5. **Reading, writing, and file offsets** — `lesson`
6. **Descriptors, duplication, and redirection** — `lesson`
7. **Short reads, partial writes and EINTR handling** — `lesson`
8. **Descriptor flags, descriptor sharing and close-on-exec** — `lesson`
9. **Resource ownership and cleanup on failure** — `lesson`
10. **System interfaces** — `test`
11. **Trace file descriptors** — `lab`

### Module 2 — Processes

#### Outcomes

- Create a child process, run another program in it, and collect its exit status.
- Explain what a child inherits from its parent.

- Prove children are reaped and distinguish a failed exec from a nonzero child exit.

#### Lessons

1. **The process abstraction** — `lesson`
2. **Creating processes with `fork`** — `lesson`
3. **Running programs with `exec`** — `lesson`
4. **Waiting for children and exit status** — `lesson`
5. **What a child inherits** — `lesson`
6. **Process exit versus signal termination** — `lesson`
7. **Environment and argument inheritance** — `lesson`
8. **Zombie processes, reaping and failure cases** — `lesson`
9. **Processes** — `test`
10. **Start a child process** — `lab`

### Module 3 — Files, Directories & Permissions

#### Outcomes

- Read file metadata and interpret type, size, ownership, and permission bits in code.
- Walk a directory and handle links correctly.

- Test incorrect permissions, broken symlinks and unpredictable directory order.

#### Lessons

1. **File metadata** — `lesson`
2. **Permission bits in code** — `lesson`
3. **Directories** — `lesson`
4. **Hard and symbolic links in code** — `lesson`
5. **Pathnames versus inode identities** — `lesson`
6. **Directory traversal and symlink safety** — `lesson`
7. **Permission failures and race conditions** — `lesson`
8. **Files and directories** — `test`
9. **Read file metadata** — `lab`

### Module 4 — Networking Basics

#### Outcomes

- Explain the client/server model, ports, and the TCP connection lifecycle.
- Write a minimal TCP client and server and trace one connection.

- Demonstrate complete framed delivery over TCP despite short reads and disconnects.

#### Lessons

1. **Client and server** — `lesson`
2. **TCP/IP basics** — `lesson`
3. **The sockets interface** — `lesson`
4. **A minimal TCP server and client** — `lesson`
5. **Blocking sockets and message framing** — `lesson`
6. **Connection timeout and disconnection** — `lesson`
7. **Network byte order and partial I/O** — `lesson`
8. **OS and network boundaries** — `test`
9. **Connect two programs over TCP** — `lab`

### Module 5 — Signals & Process Coordination

#### Outcomes

- Handle process termination and child reaping correctly while avoiding unsafe signal-handler operations.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Signal disposition and default actions** — `lesson`
2. **Safe signal-handler behavior** — `lesson`
3. **Process groups and terminal control** — `lesson`
4. **Wait status, zombies and reaping** — `lesson`
5. **Cancellation and graceful shutdown** — `lesson`
6. **Signals & Process Coordination reasoning and diagnosis** — `test`
7. **Build a signal-aware process launcher** — `lab`

### Module 6 — Pipes, Redirection & IPC

#### Outcomes

- Explain and implement pipelines using descriptors, pipes and exec.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Anonymous pipes and byte streams** — `lesson`
2. **Duplication, inheritance and descriptor closure** — `lesson`
3. **Producer-consumer pipelines and EOF** — `lesson`
4. **Deadlock and pipe-buffer behavior** — `lesson`
5. **IPC error handling and bounded data** — `lesson`
6. **Pipes, Redirection & IPC reasoning and diagnosis** — `test`
7. **Implement a two-process pipeline** — `lab`

### Module 7 — Nonblocking I/O & Socket Reliability

#### Outcomes

- Build a bounded network loop without treating TCP as a message protocol.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Blocking versus nonblocking descriptors** — `lesson`
2. **Readiness notification principles with poll** — `lesson`
3. **Partial reads and writes over sockets** — `lesson`
4. **Network message framing and malformed peers** — `lesson`
5. **Timeouts and bounded buffers** — `lesson`
6. **Nonblocking I/O & Socket Reliability reasoning and diagnosis** — `test`
7. **Handle fragmented TCP messages** — `lab`

### Module 8 — Mini Unix Utility

#### Outcomes

- Complete and explain the **Mini Unix Utility** integration lab, demonstrating the relevant course outcomes and retained evidence.

#### Lessons

1. **Build, test, and defend the Mini Unix Utility** — `lab`

   **Final integration lab — required work**

   **Mini Unix Utility**

   Build a small C command-line utility that uses files, directories, and processes through system calls, such as a simplified `ls`, `cp`, or process launcher. The utility must include:

   - Correct error handling for every system call
   - A test script that checks behavior and failure cases
   - A trace of the system calls it makes, with a short explanation
   - A short note identifying three failures that C permits and Python would reject, and how the utility guards against them

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

Complete these required exercises:

**Practical practice:**

- Trace the system calls of a program.
- Trace file-descriptor behavior and redirection.
- Start a child process with `fork()` and `exec`.
- List a directory with metadata.
- Connect two programs over TCP.

**Additional required micro-lab steps:**

- **Trace file descriptors:** Trace the system calls made by a small program, predict which descriptors exist at each step, and explain how shell redirection changes them.
- **Start a child process:** Write a launcher that starts a program, waits for it, and reports how it ended, including a deliberate failure case.
- **Read file metadata:** Build a small program that lists directory entries with type, size, and permissions, matching the output of a standard tool.
- **Connect two programs over TCP:** Build a client and a server that exchange one message, trace the connection, and explain what each system call does.

**Expanded assessment and lab criteria:**

- **Module 1 checkpoint:** Reproduce interrupted I/O and show correct loops for partial reads and writes.
- **Module 2 checkpoint:** Prove children are reaped and distinguish a failed exec from a nonzero child exit.
- **Module 3 checkpoint:** Test incorrect permissions, broken symlinks and unpredictable directory order.
- **Module 4 checkpoint:** Demonstrate complete framed delivery over TCP despite short reads and disconnects.

- **Module 5 — Build a signal-aware process launcher:**
  - Objective: Handle process termination and child reaping correctly while avoiding unsafe signal-handler operations.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Start child processes, capture normal and signal termination, and terminate cleanly after a signal.
  - Verification: All children are reaped, file descriptors close and exit states are reported correctly.
  - Evidence: Process traces, signal tests and shutdown transcript.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 6 — Implement a two-process pipeline:**
  - Objective: Explain and implement pipelines using descriptors, pipes and exec.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Connect two child programs by a pipe and inject a process failure and missing-reader case.
  - Verification: EOF arrives when expected, descriptor leaks are absent and failure paths terminate.
  - Evidence: Source, descriptor table, tests and syscall trace.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 7 — Handle fragmented TCP messages:**
  - Objective: Build a bounded network loop without treating TCP as a message protocol.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Write a small protocol that reconstructs frames from partial reads, limits maximum frame size and times out stalled clients.
  - Verification: Fragmented inputs round-trip correctly, oversize frames fail safely and disconnections release resources.
  - Evidence: Protocol spec, traces and fault tests.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.

**Final integration lab extension:**

- The final integrated lab must demonstrate the existing course outcomes and the additional outcomes in this expanded Unix interface pathway.
- Provide explicit negative tests, clean-checkout reproduction, explanation of assumptions, and a technical retrospective.

**Exit demonstration:**

The learner can explain what happens between a user's command and the operating system's work, and can demonstrate it with a Linux program that makes system calls.
