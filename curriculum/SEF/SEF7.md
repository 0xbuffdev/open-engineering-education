# SEF7 — Unix System Interfaces

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF3](SEF3.md), [SEF6](SEF6.md)
**Duration:** 7 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course investigates how C programs use Unix/POSIX interfaces to request file, process and network services. Learners reason about file descriptors, process lifetime, signal safety, directory identity, pipes and bounded TCP streams, and reproduce normal and failure behavior in disposable Linux environments. The focus is on observable interface contracts, system-call error handling and resource ownership, rather than kernel implementation internals.

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
   - A short note on three C memory or integer-safety hazards, how this project guards against them, and how these differ from recoverable system-call errors
   - A bounded loopback TCP exchange and a safe, controlled child-process fixture
   - A clean-checkout reproducibility and resource-ownership report

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

**Required checkpoint and lab contracts:**

Every module has two reasoning questions and one required practical lab below. The questions include expected answers and acceptance guidance; instructors may substitute equivalent unseen cases assessing the same outcomes. Successful completion requires correct syscall and resource-lifetime reasoning, executable evidence and safe cleanup. Memorizing the supplied answer text is insufficient. Remediate and reassess incorrect foundational concepts.

**Shared safe laboratory environment:**

Use a disposable Linux user-space environment (local machine, VM or container) with a C11-capable compiler and POSIX interfaces; record the Linux distribution/kernel, compiler version, feature-test macros and build commands. Prefer `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`. Use temp directories, fixture child processes and 127.0.0.1 loopback only. No root permissions, external network hosts, real user files or production services are required. Optional `strace` is for observation, with an equivalent documented in-program trace permitted.

**Shared review and acceptance rules:**

- For each checkpoint, explain the relevant OS semantics and boundary/failure cases; a correct result without justification is insufficient.
- Each lab requires a normal path, at least one reproducible fault/boundary path, an exact build/run recipe, and objective comparisons of expected versus observed results.
- Never run examples against unrelated host processes, privileged device nodes, production files or public network endpoints. Only signal PIDs belonging to the disposable test fixture.
- Record the exact source revision, compiler flags, fixture commands, trace or diagnostic output and a retrospective documenting an observed failure and correction.
- Trace-based evidence must distinguish C library calls from actual kernel syscalls; strace or equivalent tooling is useful but not mandatory.

**Module 1 — System Calls & File Descriptors: checkpoint** — Required assessment details

- **Q1 (free):** A C program reads from a pipe. Explain the meaning of read returning 7, 0, or -1 with errno=EINTR. What changes for an O_NONBLOCK descriptor with EAGAIN?
  - Expected answer and scoring: A positive count means 7 bytes were transferred (not necessarily the number requested); 0 means end-of-file for a pipe after all write ends close; -1/EINTR means interrupted before data was returned and the caller normally retries if its policy permits. -1/EAGAIN or EWOULDBLOCK means no bytes currently available on a nonblocking descriptor, not EOF. A retry loop must preserve completed bytes and have a stop/cancellation policy.
- **Q2 (free):** A file is opened and its descriptor duplicated with dup(). What happens to the file offset if one descriptor reads five bytes? Which close-on-exec property is shared?
  - Expected answer and scoring: Both descriptors refer to the same open file description and therefore share its file offset and file status flags. The descriptor flag FD_CLOEXEC is per descriptor rather than shared; dup() produces a new descriptor whose close-on-exec flag is off, so the program must set it or use an appropriate atomic duplication interface if needed.

**Module 1 — Trace file descriptors: required lab** — Required assessment details

- **Objective:** Trace descriptor ownership, shared offsets, EOF and partial I/O and make safe error decisions.
- **Prerequisites:** Complete this module's teaching lessons and explain the relevant conceptual checkpoint. Demonstrate the SEF3 shell and SEF6 C skills required by the task.
- **Environment:** Use a disposable Linux user-space environment (local machine, VM or container) with a C11-capable compiler and POSIX interfaces; record the Linux distribution/kernel, compiler version, feature-test macros and build commands. Prefer `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`. Use temp directories, fixture child processes and 127.0.0.1 loopback only. No root permissions, external network hosts, real user files or production services are required. Optional `strace` is for observation, with an equivalent documented in-program trace permitted.
- **Procedure:**
  1. Write a small C program that creates a temporary file in its own test directory; write known bytes, seek, duplicate a descriptor and demonstrate that the duplicate observes the shared offset.
  2. Record a descriptor ownership table before and after open, dup, close, and an optional explicit redirection using dup2; explain what the new descriptor refers to.
  3. Use a local pipe with a writer that emits a known payload in multiple chunks. Implement a read loop that accumulates the requested number of bytes or stops at EOF, rather than assuming a single read delivers the message.
  4. Use a small injected I/O wrapper or scripted fault harness to simulate a single EINTR and a short write; show the retry logic preserves completed bytes. Explain that natural signal interruption is not deterministic on all runs.
  5. Close all owned descriptors on both success and failure; verify the temporary file content and the expected EOF after the pipe's write descriptors close.
- **Expected result:** File offsets after duplicated reads match the predicted shared position; chunked pipe input is assembled exactly, simulated interruptions do not corrupt output, and open descriptors are closed.
- **Verification:** Compare byte-for-byte output with a fixed fixture, inspect descriptor and offset traces, run normal/empty/short/error cases, and optionally inspect syscalls with strace when available.
- **Evidence:** C source and test harness, descriptor/offset diagram, actual syscall or in-process trace, byte fixtures, error-case tests and final cleanup record.
- **Failure analysis:** Explain why using read once is incorrect, treating EINTR as EOF, overlooking FD_CLOEXEC on dup, or leaking a descriptor; show one reproducible failing case.
- **Acceptance:** All required observable behaviors and fault cases are met; descriptor, process and socket resources are accounted for; the result is independently reproducible under the recorded assumptions. Unmet safety or correctness checks block the lab.

**Module 2 — Processes: checkpoint** — Required assessment details

- **Q1 (free):** What do fork return values mean in parent, child and failure cases, and how must a parent interpret waitpid status?
  - Expected answer and scoring: fork returns positive child PID in the parent, 0 in the child, and -1 on failure. After successful waitpid, use WIFEXITED then WEXITSTATUS for normal exit, or WIFSIGNALED then WTERMSIG for signal termination; never interpret WEXITSTATUS when the child did not exit normally.
- **Q2 (free):** A launcher calls fork then execvp. The target command does not exist. Can child exit code 127 alone prove that exec failed? How can the launcher distinguish failure?
  - Expected answer and scoring: No: a successfully executed program may also exit 127. Use a close-on-exec error-reporting pipe (or an equivalent explicit handshake) to report exec failure errno from the child; on successful exec the pipe closes automatically. Handle fork, pipe, exec and wait errors explicitly.

**Module 2 — Start a child process: required lab** — Required assessment details

- **Objective:** Launch and reap bounded child processes with correctly classified exit and exec-failure evidence.
- **Prerequisites:** Complete this module's teaching lessons and explain the relevant conceptual checkpoint. Demonstrate the SEF3 shell and SEF6 C skills required by the task.
- **Environment:** Use a disposable Linux user-space environment (local machine, VM or container) with a C11-capable compiler and POSIX interfaces; record the Linux distribution/kernel, compiler version, feature-test macros and build commands. Prefer `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`. Use temp directories, fixture child processes and 127.0.0.1 loopback only. No root permissions, external network hosts, real user files or production services are required. Optional `strace` is for observation, with an equivalent documented in-program trace permitted.
- **Procedure:**
  1. Write a C launcher that accepts a fixed, documented command-and-arguments fixture; use fork, an exec-family function and waitpid without evaluating input through a shell.
  2. Implement an exec-error reporting channel that is closed on successful exec, and distinguish nonexistent command from a real command that intentionally returns status 127.
  3. Demonstrate one successful child, one nonzero normal exit, one missing executable and one child terminated by a signal sent only to that test child.
  4. Show each waitpid result including interrupted wait handling; record how the launcher avoids unreaped children and closes inherited descriptors.
  5. Limit child run time and implement graceful cleanup if a controlled fixture stalls; never target unrelated system processes.
- **Expected result:** Launcher reports normal exit codes and signal termination separately, identifies exec failure independently of child exit status, reaps every child and releases owned descriptors.
- **Verification:** Compare four fixture outcomes with expected status and error-pipe observations; check waitpid/child accounting and repeat runs under a timeout.
- **Evidence:** Launcher and fixtures, status table, process trace, cleanup/timeout logs and regression tests.
- **Failure analysis:** Explain a child accidentally falling through into parent code, waiting on the wrong PID, status misclassification or treating exit 127 as definitive exec failure.
- **Acceptance:** All required observable behaviors and fault cases are met; descriptor, process and socket resources are accounted for; the result is independently reproducible under the recorded assumptions. Unmet safety or correctness checks block the lab.

**Module 3 — Files, Directories & Permissions: checkpoint** — Required assessment details

- **Q1 (free):** A symbolic link points to a nonexistent path. Compare stat and lstat on the link. What does readdir guarantee about directory-entry order?
  - Expected answer and scoring: stat follows the link and fails with ENOENT when the target is missing; lstat reports the symbolic-link object itself (when accessible). readdir does not promise any sort order, so code requiring sorted display must sort explicitly.
- **Q2 (free):** A program checks a filename with stat, then opens the same path later. Why is this vulnerable to time-of-check/time-of-use changes? What evidence should be checked on the opened object?
  - Expected answer and scoring: The pathname may refer to a different object between operations. For object properties required by the program, open with appropriate flags/policies and inspect the resulting descriptor with fstat; use directory-relative or no-follow interfaces when applicable, while explaining that flags have platform and race-condition limits.

**Module 3 — Read file metadata: required lab** — Required assessment details

- **Objective:** Inspect filesystem objects with correct symlink, error and directory-order handling.
- **Prerequisites:** Complete this module's teaching lessons and explain the relevant conceptual checkpoint. Demonstrate the SEF3 shell and SEF6 C skills required by the task.
- **Environment:** Use a disposable Linux user-space environment (local machine, VM or container) with a C11-capable compiler and POSIX interfaces; record the Linux distribution/kernel, compiler version, feature-test macros and build commands. Prefer `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`. Use temp directories, fixture child processes and 127.0.0.1 loopback only. No root permissions, external network hosts, real user files or production services are required. Optional `strace` is for observation, with an equivalent documented in-program trace permitted.
- **Procedure:**
  1. Create all fixtures inside a disposable directory: regular files, a subdirectory, a valid symlink and a dangling symlink. Do not traverse unrelated directories.
  2. Implement a C metadata lister using opendir/readdir, lstat and carefully formatted type, size and permission fields. Sort entries if output order is part of its contract.
  3. Contrast lstat and stat on both valid and dangling links; explicitly handle missing objects, unreadable entries where reproducible, and malformed/overlong path inputs.
  4. Use an opened descriptor plus fstat for one fixture to demonstrate why a prior pathname check cannot prove later descriptor identity.
  5. Test empty directories, hidden entries, symlinks and a changing-directory fixture without following links into untrusted paths.
- **Expected result:** The lister reports fixture types, sizes and permissions correctly, retains deterministic ordering where promised, and handles dangling symlinks without an uncontrolled traversal.
- **Verification:** Compare selected metadata to a portable reference such as Python os.stat/os.lstat or a documented system tool; assert link type and directory entry sets.
- **Evidence:** Source, fixture creator/cleanup, expected-versus-observed metadata table, error tests and a path-identity note.
- **Failure analysis:** Explain accidental symlink following, assuming readdir order, or relying on permission-denial tests while running with elevated privileges.
- **Acceptance:** All required observable behaviors and fault cases are met; descriptor, process and socket resources are accounted for; the result is independently reproducible under the recorded assumptions. Unmet safety or correctness checks block the lab.

**Module 4 — Networking Basics: checkpoint** — Required assessment details

- **Q1 (free):** A client sends the six bytes ABCDEF once over TCP. Is one recv call at the server guaranteed to return all six bytes? Explain how a four-byte length prefix changes the application.
  - Expected answer and scoring: TCP is a byte stream with no record boundary guarantee: recv may yield fewer than six bytes even when the sender used one send. A network-byte-order four-byte length prefix lets the receiver accumulate exactly a bounded header and payload, handling EOF and errors explicitly.
- **Q2 (free):** Explain the distinction between a successful TCP connection and a valid authorized application request. What should a server do with an unexpected length field?
  - Expected answer and scoring: A TCP handshake does not validate an application protocol or user permission. Reject an unsupported or oversized length before allocating large memory; define bounds and error behavior. This beginner lab uses loopback only and is not a production authorization system.

**Module 4 — Connect two programs over TCP: required lab** — Required assessment details

- **Objective:** Exchange bounded framed data over a local TCP connection while recording transport and application-layer outcomes.
- **Prerequisites:** Complete this module's teaching lessons and explain the relevant conceptual checkpoint. Demonstrate the SEF3 shell and SEF6 C skills required by the task.
- **Environment:** Use a disposable Linux user-space environment (local machine, VM or container) with a C11-capable compiler and POSIX interfaces; record the Linux distribution/kernel, compiler version, feature-test macros and build commands. Prefer `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`. Use temp directories, fixture child processes and 127.0.0.1 loopback only. No root permissions, external network hosts, real user files or production services are required. Optional `strace` is for observation, with an equivalent documented in-program trace permitted.
- **Procedure:**
  1. Implement a minimal C TCP server bound only to 127.0.0.1 on an available unprivileged port, and a matching client; document how the chosen port is passed to the client.
  2. Define a protocol with a four-byte unsigned big-endian payload length and a maximum message size; implement read-exact and write-all helpers that handle positive short results and relevant errors.
  3. Send several small messages, including a zero-length payload if permitted by the protocol; verify the server reports the exact bytes and sends an explicit reply.
  4. Send a message in deliberately fragmented writes from the client, then a clean premature close in another test; demonstrate partial-header and partial-body handling.
  5. Send an oversized length prefix and verify bounded rejection without allocating attacker-controlled memory; use timeout and cleanup limits so no test hangs.
- **Expected result:** Valid frames round-trip byte-for-byte; fragmented writes reconstruct correctly; truncated and oversized frames receive a documented failure outcome and bounded cleanup.
- **Verification:** Compare actual payload bytes, encoded lengths, responses and error logs; run tests only on loopback and record server shutdown.
- **Evidence:** Protocol definition, client/server source, payload fixtures, frame trace, loopback test output and negative cases.
- **Failure analysis:** Explain confusing TCP segments with messages, missing length endian conversion, treating a zero-byte recv as progress, or trusting an unchecked advertised length.
- **Acceptance:** All required observable behaviors and fault cases are met; descriptor, process and socket resources are accounted for; the result is independently reproducible under the recorded assumptions. Unmet safety or correctness checks block the lab.

**Module 5 — Signals & Process Coordination: checkpoint** — Required assessment details

- **Q1 (free):** Why is a printf call or malloc allocation unsafe inside a general asynchronous signal handler? What should the handler do instead?
  - Expected answer and scoring: Functions not specified as async-signal-safe can use nonreentrant state or locks. A handler may set a volatile sig_atomic_t flag, or use an appropriate async-signal-safe notification operation; mainline code should perform complex logging and cleanup. Also understand that signal dispositions/restart settings affect interrupted waits.
- **Q2 (free):** How does waitpid distinguish normal exit from signal termination, and why should a launcher restrict signals to children or process groups it owns?
  - Expected answer and scoring: Use WIFEXITED/WEXITSTATUS versus WIFSIGNALED/WTERMSIG after a successful waitpid, and account for EINTR and ECHILD. Signals to unrelated PIDs/groups could disrupt the host; a safe test targets only recorded child PIDs or an explicitly owned process group.

**Module 5 — Build a signal-aware process launcher: required lab** — Required assessment details

- **Objective:** Handle termination signals and child lifecycle without unsafe handlers or orphaned test processes.
- **Prerequisites:** Complete this module's teaching lessons and explain the relevant conceptual checkpoint. Demonstrate the SEF3 shell and SEF6 C skills required by the task.
- **Environment:** Use a disposable Linux user-space environment (local machine, VM or container) with a C11-capable compiler and POSIX interfaces; record the Linux distribution/kernel, compiler version, feature-test macros and build commands. Prefer `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`. Use temp directories, fixture child processes and 127.0.0.1 loopback only. No root permissions, external network hosts, real user files or production services are required. Optional `strace` is for observation, with an equivalent documented in-program trace permitted.
- **Procedure:**
  1. Implement a launcher with sigaction registering a SIGINT or SIGTERM handler that sets a volatile sig_atomic_t flag only; mainline code responds to the flag.
  2. Spawn a controlled child fixture that exits normally, and a second that runs until a bounded termination event; record their PIDs in the launcher.
  3. Send a termination signal only to the controlled launcher/child PIDs, and show graceful child cleanup and reaping using waitpid.
  4. Test a child that exits before the termination signal and one that is deliberately interrupted; handle EINTR and ECHILD without spinning forever.
  5. Demonstrate one unsafe handler misconception in a written explanation rather than executing unsafe code; clean up only owned resources.
- **Expected result:** Signal handling keeps non-async-signal-safe work outside the handler, all child processes are accounted for, normal/signal outcomes are reported correctly and no controlled test process is left running.
- **Verification:** Record handler flag transitions, signal/exit status, waitpid results and repeatable timeout-driven test results; avoid tests depending on exact signal scheduling.
- **Evidence:** C implementation, signal setup, PID ownership table, process traces, test commands and cleanup demonstration.
- **Failure analysis:** Explain handler reentrancy, a race between signal and wait, incorrect process-group targeting, or child reaping omission.
- **Acceptance:** All required observable behaviors and fault cases are met; descriptor, process and socket resources are accounted for; the result is independently reproducible under the recorded assumptions. Unmet safety or correctness checks block the lab.

**Module 6 — Pipes, Redirection & IPC: checkpoint** — Required assessment details

- **Q1 (free):** A reader has consumed all bytes from an anonymous pipe but never receives EOF after the writer exits. What is the likely descriptor-lifetime error?
  - Expected answer and scoring: Some process still holds a write end of the pipe open, possibly due to inheritance or a forgotten close after dup2. EOF occurs only once no write descriptor remains open and buffered bytes are consumed.
- **Q2 (free):** How do dup2 and exec permit a pipeline between two programs? Describe one failure when a downstream consumer closes early.
  - Expected answer and scoring: dup2 replaces the intended standard-input/output descriptor before exec; close unused originals in both parent and children, then wait/reap. If the reader closes, a subsequent write may raise SIGPIPE (default action terminates) or return EPIPE if SIGPIPE is ignored/handled; the launcher must define and report behavior.

**Module 6 — Implement a two-process pipeline: required lab** — Required assessment details

- **Objective:** Connect two bounded local processes with a pipe, correct redirection and deterministic EOF behavior.
- **Prerequisites:** Complete this module's teaching lessons and explain the relevant conceptual checkpoint. Demonstrate the SEF3 shell and SEF6 C skills required by the task.
- **Environment:** Use a disposable Linux user-space environment (local machine, VM or container) with a C11-capable compiler and POSIX interfaces; record the Linux distribution/kernel, compiler version, feature-test macros and build commands. Prefer `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`. Use temp directories, fixture child processes and 127.0.0.1 loopback only. No root permissions, external network hosts, real user files or production services are required. Optional `strace` is for observation, with an equivalent documented in-program trace permitted.
- **Procedure:**
  1. Create a local producer fixture that writes a finite known text payload and a consumer fixture that transforms or counts bytes.
  2. Build a C launcher using pipe, fork, dup2, exec and waitpid to route producer standard output to consumer standard input.
  3. Close unused read/write ends in every process immediately after duplication and document a descriptor-ownership table.
  4. Test normal output, empty producer, consumer exiting early and a nonexistent child executable. Bound all waits and avoid invoking an arbitrary shell.
  5. Intentionally leave a write end open in a disposable demonstration to show delayed EOF, then repair descriptor cleanup and verify termination.
- **Expected result:** Normal pipeline output matches the reference, the reader sees EOF when all writers close, child failures and early consumer exit are handled without hanging, and both children are reaped.
- **Verification:** Compare exact transformed payload or byte counts and run bounded timeout tests for EOF and failure conditions; inspect recorded descriptor closures.
- **Evidence:** Launcher and fixtures, descriptor diagram, output checks, failure/timeout traces and before/after cleanup evidence.
- **Failure analysis:** Explain inherited pipe ends, blocked readers, SIGPIPE/EPIPE interpretation or a missed waitpid.
- **Acceptance:** All required observable behaviors and fault cases are met; descriptor, process and socket resources are accounted for; the result is independently reproducible under the recorded assumptions. Unmet safety or correctness checks block the lab.

**Module 7 — Nonblocking I/O & Socket Reliability: checkpoint** — Required assessment details

- **Q1 (free):** On a nonblocking socket, a recv call returns -1 with EAGAIN or EWOULDBLOCK. Does that mean the peer disconnected? What does poll report?
  - Expected answer and scoring: EAGAIN/EWOULDBLOCK means the operation would block now, not that the peer closed; poll can report readiness and error/hangup indications but the program must still perform I/O and handle races, partial transfers and EOF. A successful recv returning 0 on a stream socket indicates orderly shutdown of the peer's sending direction.
- **Q2 (free):** A four-byte big-endian frame length advertises 5,000,000 bytes, but the server allows at most 4096 bytes. What is safe behavior? Why does a single send not prove the entire frame was transmitted?
  - Expected answer and scoring: Reject the oversized length before allocating or reading the payload; report protocol failure and close cleanly. send can return a positive short count; a correct sender tracks the remaining bytes and waits/retries according to readiness, timeout and cancellation policy.

**Module 7 — Handle fragmented TCP messages: required lab** — Required assessment details

- **Objective:** Implement a bounded, timeout-aware framed connection that handles fragmented data and nonblocking readiness correctly.
- **Prerequisites:** Complete this module's teaching lessons and explain the relevant conceptual checkpoint. Demonstrate the SEF3 shell and SEF6 C skills required by the task.
- **Environment:** Use a disposable Linux user-space environment (local machine, VM or container) with a C11-capable compiler and POSIX interfaces; record the Linux distribution/kernel, compiler version, feature-test macros and build commands. Prefer `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`. Use temp directories, fixture child processes and 127.0.0.1 loopback only. No root permissions, external network hosts, real user files or production services are required. Optional `strace` is for observation, with an equivalent documented in-program trace permitted.
- **Procedure:**
  1. Reuse the Module 4 loopback protocol, set accepted sockets to nonblocking mode, and use poll with a finite deadline to wait for readable/writable states.
  2. Implement a finite receive-state machine for four-byte header and payload, tracking accumulated bytes and rejecting any advertised length above 4096 before allocating.
  3. Implement a bounded send loop and deterministic handling for EAGAIN/EWOULDBLOCK, EINTR, EOF, partial writes and poll timeout.
  4. Test a header split across four writes, a payload split across many writes, a peer that closes mid-frame, a malformed length and an idle peer that exceeds the deadline.
  5. Run repeatable test cases over 127.0.0.1 only, report the maximum buffer size and verify cleanup after every failure.
- **Expected result:** Valid frames are reconstructed exactly; the implementation does not busy-spin or allocate unbounded memory; malformed, idle and disconnected peers are rejected within a finite deadline.
- **Verification:** Check complete payload bytes, timestamps or bounded timeout behavior, buffer bounds, connection closure and repeated clean runs, including a deliberately short send demonstration.
- **Evidence:** Protocol/state diagram, source, poll traces, tests and timing limits, explicit failure cases and measured buffer use.
- **Failure analysis:** Explain confusing readiness with a guaranteed complete operation, treating EAGAIN as EOF, retrying forever or trusting peer-controlled lengths.
- **Acceptance:** All required observable behaviors and fault cases are met; descriptor, process and socket resources are accounted for; the result is independently reproducible under the recorded assumptions. Unmet safety or correctness checks block the lab.

**Module 8 — Mini Unix Utility: checkpoint** — Required assessment details

- **Q1 (free):** A mini Unix CLI reports that a file can be safely opened because a pathname check succeeded, but the pathname changes before open. Why is that evidence insufficient?
  - Expected answer and scoring: A pathname check and subsequent open are separate operations: the referenced object can change, so checking the opened descriptor with fstat and using appropriate constrained directory-relative/no-follow APIs is safer for a stated policy. One successful run does not eliminate a possible race.
- **Q2 (free):** How would you defend a tool that handles files, child processes and TCP against a reviewer who only saw its happy-path demo?
  - Expected answer and scoring: Present documented syscall/resource ownership, normal and negative tests, failure classification and bounded cleanup, plus exact build/run commands, trace evidence and a technical retrospective. Show that file descriptor leaks, unreaped children, malformed network frames and unjustified error assumptions are tested rather than ignored.

**Module 8 — Build, test, and defend the Mini Unix Utility: required lab** — Required assessment details

- **Objective:** Integrate file descriptors, directory metadata, process lifecycle and loopback socket I/O in a bounded, independently reproducible C project.
- **Prerequisites:** Complete this module's teaching lessons and explain the relevant conceptual checkpoint. Demonstrate the SEF3 shell and SEF6 C skills required by the task.
- **Environment:** Use a disposable Linux user-space environment (local machine, VM or container) with a C11-capable compiler and POSIX interfaces; record the Linux distribution/kernel, compiler version, feature-test macros and build commands. Prefer `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`. Use temp directories, fixture child processes and 127.0.0.1 loopback only. No root permissions, external network hosts, real user files or production services are required. Optional `strace` is for observation, with an equivalent documented in-program trace permitted.
- **Procedure:**
  1. Build one small C command-line project with an `inspect` operation that lists a disposable directory's metadata, a `run` operation that launches an explicitly supplied test fixture with fork/exec/wait, and a documented local TCP client/server demo or subcommand that exchanges a bounded frame.
  2. Use correct errno-aware handling for supported system calls, explicit descriptor ownership, safe path/link policy, bounded read/write loops, defined process exit-status reporting and complete cleanup.
  3. Provide a repeatable POSIX/Linux build invocation with feature-test macros and warning flags, such as `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`, and record compiler and OS versions.
  4. Test normal behavior, missing file, dangling symlink, missing executable, signaled child, truncated TCP frame, oversized length and timeout. Keep all filesystem fixtures in a temporary directory and sockets on loopback.
  5. Record a syscall trace with strace where available, or a documented in-program call/return log when tracing is unavailable. Explain the boundary between C library functions and actual kernel syscalls.
  6. Write a README with clean-checkout build, run and test commands; create an outcomes-to-evidence matrix and have a reviewer reproduce at least one failure case.
  7. Explain three C language hazards (for example, out-of-bounds access, use-after-free and unchecked integer conversion), distinguishing language undefined behavior from recoverable operating-system error returns.
- **Expected result:** The tool reports correct metadata and child termination status and successfully exchanges a bounded loopback frame, while failure cases produce documented outcomes without leaks, stuck processes or uncontrolled resource use.
- **Verification:** Build from a clean checkout, run automated fixtures and a reviewer demonstration, compare expected/observed statuses and bytes, inspect resource cleanup and link each course outcome to evidence.
- **Evidence:** Versioned C sources, build/test scripts, test fixture generator, syscall/operation logs, error matrix, review record, README and retrospective.
- **Failure analysis:** Explain at least one real defect or incorrect assumption, its minimal reproduction, a repair and regression test. Explicitly disclose unsupported platform behavior or unresolved limitations.
- **Acceptance:** All required observable behaviors and fault cases are met; descriptor, process and socket resources are accounted for; the result is independently reproducible under the recorded assumptions. Unmet safety or correctness checks block the lab.

**Exit demonstration:**

The learner can explain what happens between a user's command and the operating system's work, and can demonstrate it with a Linux program that makes system calls.
