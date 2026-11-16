# SEF7 — Unix System Interfaces

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF3](SEF3.md), [SEF6](SEF6.md)
**Duration:** 7 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

SEF3 already establishes safe shell invocation, process-environment inheritance, command lookup, Bash versus POSIX-sh portability and known GNU-tool dependencies. SEF6 also establishes ISO C11 memory/object lifetime, checked allocation, bounded parsing, manually owned container libraries and reproducible toolchain diagnostics before SEF7 begins. This course instead examines **C and POSIX system interfaces** (file descriptors, fork/exec, directory identity, signals, sockets) with explicit resource ownership; it does not replace the earlier command-line portability assessments. Actual shell behavior is not conflated with the C ABI or operating-system syscall semantics.

Understand how a C program requests Unix operating-system services and handles their failure. Start with file descriptors and partial I/O, then investigate process creation and termination, filesystem identity, signals, pipes, and framed TCP streams. Finish by building a small, reproducible Unix utility that combines these interfaces with explicit resource ownership.

The reference environment is a **nonprivileged local Linux environment**, C11-capable compiler, and available POSIX interfaces. Document actual tool and OS versions, compilation flags and feature-test macros; a typical compiler invocation is `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`. Use a learner-owned temporary tree, controlled child processes, and `127.0.0.1` loopback only. No root account, external network service, production files, real unrelated processes, paid service, or proprietary grader is needed. A correct in-program interface trace is an acceptable alternative when optional kernel tracing software such as `strace` is unavailable; label the evidence accurately.

The course distinguishes a library interface from a kernel system call, a descriptor from its underlying open-file description, and a TCP byte stream from application messages. Code must address partial transfer, `EINTR`, EOF, resource cleanup, and bounded waits. Never assume pathname checks remain true after an object changes, or that signal handlers can safely call arbitrary library functions.

The eight original module subjects remain the instructional sequence. Seven required summative assessments cover the outcomes and may reuse verified components, fixtures and explanations; the old universal checkpoint/lab quota and a duplicate final lab are not imposed. The seven-week workload is provisional and the course remains `draft` pending learner and reviewer evidence.

## Learning outcomes

- **SEF7-O1:** Use POSIX file descriptors and C return/errno contracts for correct partial, interrupted, EOF, and failure-aware I/O.
- **SEF7-O2:** Distinguish per-descriptor flags from shared open-file descriptions and correctly manage dup, redirection, offset and close-on-exec behavior.
- **SEF7-O3:** Launch and reap bounded child processes with fork/exec/waitpid and distinguish exec failure, exit status and signal termination.
- **SEF7-O4:** Respond to signals with bounded async-signal-safe handlers and controlled cleanup of independently verified owned children.
- **SEF7-O5:** Inspect file and directory identity, permissions and symlinks with appropriate stat/lstat/fstat and directory-relative reasoning.
- **SEF7-O6:** Traverse disposable directories safely, handling unpredictable entry order, missing objects and link policies without changes outside the owned tree.
- **SEF7-O7:** Connect child programs with pipes and redirection, ensure EOF by closing unused descriptors, and propagate both sides' failures.
- **SEF7-O8:** Exchange explicitly framed bounded TCP messages over loopback without treating a byte stream as message-delimited.
- **SEF7-O9:** Use poll, nonblocking sockets and finite deadlines while handling EAGAIN/EWOULDBLOCK, EINTR, partial I/O and disconnection.
- **SEF7-O10:** Document the C11/POSIX toolchain, feature-test macros, supported interfaces and differences between library-call and kernel-syscall traces.
- **SEF7-O11:** Define and enforce success/error ownership and cleanup contracts for file descriptors, directory handles, children, buffers and sockets.
- **SEF7-O12:** Test normal, boundary, malformed, interrupted and injected-fault behavior with independent expected results and a repaired regression.
- **SEF7-O13:** Build a self-contained C mini Unix utility combining fixture metadata, controlled processes and bounded loopback network operations.
- **SEF7-O14:** Defend resource and design choices using reproducible build/test evidence and independent review, without asserting unsupported OS guarantees.

## Modules

### Module 1 — System Calls & File Descriptors

#### Outcomes

- SEF7-O1
- SEF7-O2
- SEF7-O11
- SEF7-O12

#### Lessons

1. Course introduction: Unix System Interfaces
2. The user and kernel boundary
3. System calls and error handling
4. File descriptors
5. Reading, writing, and file offsets
6. Descriptors, duplication, and redirection
7. Short reads, partial writes and EINTR handling
8. Descriptor flags, descriptor sharing and close-on-exec
9. Resource ownership and cleanup on failure

*Optional practice:* Draw an open/dup/close descriptor table and inspect shared file offsets using a disposable file.

### Module 2 — Processes

#### Outcomes

- SEF7-O3
- SEF7-O4
- SEF7-O11
- SEF7-O12

#### Lessons

1. The process abstraction
2. Creating processes with `fork`
3. Running programs with `exec`
4. Waiting for children and exit status
5. What a child inherits
6. Process exit versus signal termination
7. Environment and argument inheritance
8. Zombie processes, reaping and failure cases

*Optional practice:* Reap a controlled child with a deliberately nonzero exit status and compare it with a missing executable.

### Module 3 — Files, Directories & Permissions

#### Outcomes

- SEF7-O5
- SEF7-O6
- SEF7-O11
- SEF7-O12

#### Lessons

1. File metadata
2. Permission bits in code
3. Directories
4. Hard and symbolic links in code
5. Pathnames versus inode identities
6. Directory traversal and symlink safety
7. Permission failures and race conditions

*Optional practice:* Compare stat, lstat and fstat for regular, symlink and dangling-link fixture entries.

### Module 4 — Networking Basics

#### Outcomes

- SEF7-O8
- SEF7-O10
- SEF7-O12

#### Lessons

1. Client and server
2. TCP/IP basics
3. The sockets interface
4. A minimal TCP server and client
5. Blocking sockets and message framing
6. Connection timeout and disconnection
7. Network byte order and partial I/O

*Optional practice:* Send two framed messages using a small local client and inspect their length prefixes.

### Module 5 — Signals & Process Coordination

#### Outcomes

- SEF7-O3
- SEF7-O4
- SEF7-O11
- SEF7-O12

#### Lessons

1. Signal disposition and default actions
2. Safe signal-handler behavior
3. Process groups and terminal control
4. Wait status, zombies and reaping
5. Cancellation and graceful shutdown

*Optional practice:* Use an owned process to observe a graceful termination request and a bounded wait.

### Module 6 — Pipes, Redirection & IPC

#### Outcomes

- SEF7-O2
- SEF7-O7
- SEF7-O11
- SEF7-O12

#### Lessons

1. Anonymous pipes and byte streams
2. Duplication, inheritance and descriptor closure
3. Producer-consumer pipelines and EOF
4. Deadlock and pipe-buffer behavior
5. IPC error handling and bounded data

*Optional practice:* Explain why an inherited extra write end delays a pipe reader's EOF.

### Module 7 — Nonblocking I/O & Socket Reliability

#### Outcomes

- SEF7-O8
- SEF7-O9
- SEF7-O11
- SEF7-O12

#### Lessons

1. Blocking versus nonblocking descriptors
2. Readiness notification principles with poll
3. Partial reads and writes over sockets
4. Network message framing and malformed peers
5. Timeouts and bounded buffers

*Optional practice:* Trace a header split across writes and predict how poll and recv interleave.

### Module 8 — Mini Unix Utility

#### Outcomes

- SEF7-O10
- SEF7-O11
- SEF7-O12
- SEF7-O13
- SEF7-O14

#### Lessons

1. Mini utility behavior and resource contracts
2. Directory inspection and file identity
3. Owned child launcher and termination
4. Loopback TCP message exchange
5. Failure and cleanup test harness
6. Interface trace and independent technical defense

*Optional practice:* Sketch mini utility commands, error outcomes and an independent reviewer evidence map.

## Completion requirements

### Assessment environment and evaluation

Use a documented, nonprivileged C11/POSIX toolchain and disposable Linux fixtures. Record the exact revision, build flags, OS/compiler/libc assumptions, relevant feature-test macros, expected and actual values, errno immediately after a failing interface, and commands used to reproduce the result. A provided deterministic fault wrapper may simulate short transfers or EINTR where scheduling would make an authentic failure nondeterministic. Keep transferred bytes already accepted by the interface; do not restart a partially completed operation from byte zero.

Every assessment requires explicit resource ownership and test boundaries. All filesystem changes remain inside an owned fixture directory, child signals target only a process this test created, and sockets bind to 127.0.0.1 only. No root privileges, external network connections, real user files, production process or paid grader are required. Bound potentially blocked reads, waits and peer connections with test deadlines. A syscall tracer is optional: an in-program call/return trace must not be mislabeled as proof of individual kernel syscalls.

Review decisions depend on demonstrated behavior, explicit failure handling, inspected artifacts and technical explanations, not checkmarks or a green badge alone. A reviewer may vary synthetic inputs without changing the published success criteria. An uncorrected descriptor leak, unsafe process signal, missing limit, inaccurate POSIX assumption, or unreproduced critical failure prevents passing until repaired. Assessment artifacts and tested helpers may be reused.

### Required summative assessments

- **SEF7-AS1** (required descriptor identity and partial i/o)
  - Outcomes: SEF7-O1, SEF7-O2, SEF7-O10, SEF7-O11, SEF7-O12
  - Work: In a disposable C fixture, open a known file, duplicate its descriptor, trace shared offsets and compare shared file status flags with per-descriptor FD_CLOEXEC. Perform one bounded dup2 redirection and maintain an ownership table across open/dup/close. Implement byte-stream read/write loops and inject a short read, partial write and EINTR with a deterministic wrapper. Demonstrate a complete payload, empty input and failing open/write without discarding previously transferred bytes.
  - Criteria: Predicted offsets and descriptor identities agree with observed state; dup does not create an independent offset, and close-on-exec is treated as a per-descriptor property. Byte output matches the independent oracle; loops advance after positive transfers, retry appropriate EINTR cases, distinguish EOF from nonblocking EAGAIN, and close owned resources on every demonstrated path. The learner does not blindly retry close after EINTR where a descriptor number might have been reused.
  - Evidence: Source and exact build/test commands, ownership and offset diagrams, fixture bytes and expected/actual output, flags/status logs, short-transfer/EINTR fault records and cleanup checks.

- **SEF7-AS2** (required child execution, signals and reaping)
  - Outcomes: SEF7-O3, SEF7-O4, SEF7-O10, SEF7-O11, SEF7-O12
  - Work: Write a C launcher for fixed local child fixtures using fork, exec and waitpid without invoking a shell to interpret untrusted strings. Use a close-on-exec error pipe to distinguish a failed exec from an actual program deliberately exiting 127. Test success, nonzero exit, nonexistent executable and a child terminated by a signal sent only to a verified owned PID. Use sigaction with a volatile sig_atomic_t flag for minimal handler work; implement bounded mainline cleanup, EINTR-aware waiting and reaping.
  - Criteria: Fork and exec failures, WIFEXITED/WEXITSTATUS and WIFSIGNALED outcomes are classified correctly; exit code 127 alone is not treated as proof of exec failure. The handler performs no unsupported async-signal-unsafe operations, and all owned children and descriptors are accounted for on success, failure, early exit and timeout. The procedure neither signals unrelated PIDs nor assumes deterministic signal delivery order.
  - Evidence: Launcher and fixture source, child/status matrix, error-pipe and close-on-exec demonstration, handler and wait logs, bounded failure cases, corrected lifecycle defect and cleanup verification.

- **SEF7-AS3** (required directory identity, links and permissions)
  - Outcomes: SEF7-O5, SEF7-O6, SEF7-O10, SEF7-O11, SEF7-O12
  - Work: Create a temporary directory with regular and hidden files, a subdirectory, a symlink and a dangling symlink. Implement a metadata listing operation using opendir/readdir and lstat or descriptor-relative alternatives, documenting type, size, permissions, ordering and link policy. Compare stat, lstat and fstat on selected fixtures, including a pathname replaced after an earlier check; demonstrate why an opened descriptor's identity is authoritative for the object actually used. Exercise empty, missing and dangling paths and a permission-denial case where the unprivileged environment permits one.
  - Criteria: Metadata agrees with independently checked fixture values, link targets are not followed against policy, and declared ordering is deterministic rather than inferred from readdir. No stale pathname inspection is claimed to authenticate a later open; any opened-object and no-follow checks are documented. The program reports missing and unsupported cases truthfully and releases directory handles without touching objects outside the owned fixture root.
  - Evidence: C source, fixture inventory and independent metadata oracle, stat/lstat/fstat observations, path-change and failure transcripts, order/link policy, actual permissions and ownership/cleanup records.

- **SEF7-AS4** (required two-process pipes and eof)
  - Outcomes: SEF7-O1, SEF7-O2, SEF7-O3, SEF7-O7, SEF7-O11, SEF7-O12
  - Work: Implement a two-child pipeline with pipe, fork, dup2, exec and waitpid. Pass a finite known byte fixture from a producer to a consumer that counts or transforms the stream. Diagram all inherited pipe ends and close unused ends promptly. Test normal data, an empty producer, absent child executable and early consumer exit. In a bounded faulty copy, retain an extra write end and observe delayed EOF; then repair it. Handle SIGPIPE/EPIPE and child failure reporting without unexpectedly terminating the coordinator.
  - Criteria: Expected output matches an independent byte oracle; EOF arrives after all write ends are closed, not simply when the producer finishes. No child or descriptor remains unaccounted for, both child statuses are checked, and broken-pipe or missing-executable outcomes cannot masquerade as success. A finite harness aborts the deliberately faulty wait and never signals unrelated processes.
  - Evidence: Source, descriptor/ownership table, known payload and oracle, statuses and timeout observations for each failure case, reproduced EOF defect and corrected regression.

- **SEF7-AS5** (required blocking loopback tcp and framing)
  - Outcomes: SEF7-O1, SEF7-O8, SEF7-O10, SEF7-O11, SEF7-O12
  - Work: Build a local C server bound only to 127.0.0.1 with a client using an available unprivileged port. Define a protocol of four network-order length bytes followed by at most 4096 payload bytes, explicitly allowing or forbidding empty frames. Implement full-frame receive and send loops with checked bounds. Deliver known messages, fragment a header and payload across writes, close during the header and body, advertise an oversized length, and test connection failure under a finite timeout.
  - Criteria: Valid frames round-trip byte-for-byte independent of segmentation; network-order conversion and size limits are correct before buffer allocation. Positive short transfers preserve progress; EOF, EINTR, EPIPE or other documented connection errors lead to bounded failure rather than a false completed message. Truncated or oversized peers are rejected without excessive memory use or indefinite waits. All listeners and sockets remain on loopback and are closed after tests.
  - Evidence: Protocol and buffer contract, C source, expected/actual encoded frames, fragmented, truncated and oversized test results, listener address, status/timeout and cleanup logs.

- **SEF7-AS6** (required poll-driven nonblocking tcp reliability)
  - Outcomes: SEF7-O1, SEF7-O8, SEF7-O9, SEF7-O11, SEF7-O12
  - Work: Extend the same protocol with a nonblocking socket and poll-based state machine that tracks partial header, body and output offsets. Use an end-to-end finite monotonic deadline, re-evaluating remaining time after EINTR. Handle EAGAIN/EWOULDBLOCK, readiness followed by an incomplete operation, POLLHUP/POLLERR, EOF and short writes. Test a header split into four sends, a body split into many sends, early disconnect, oversized frame, idle peer and repeated valid exchanges.
  - Criteria: Reconstructed frames match the independent oracle and buffers remain bounded at 4096 payload bytes plus framing. EAGAIN is not EOF, poll readiness is not a guarantee of complete I/O, and progress cannot spin indefinitely or reset the total deadline. Every malformed or idle peer fails in finite time, and all allocated buffers and sockets are released or explicitly tracked after fault cases.
  - Evidence: State-machine source and diagram, byte-progress traces, fixed fragment and timeout fixtures, exact outputs and error statuses, bounded-memory and cleanup checks, a repaired failure and platform notes.

- **SEF7-AS7** (required integrated mini unix utility and independent defense)
  - Outcomes: SEF7-O1, SEF7-O2, SEF7-O3, SEF7-O4, SEF7-O5, SEF7-O6, SEF7-O7, SEF7-O8, SEF7-O9, SEF7-O10, SEF7-O11, SEF7-O12, SEF7-O13, SEF7-O14
  - Work: Combine already assessed components into a small C utility offering inspect for fixture metadata, run for a controlled child and net-demo for a bounded loopback TCP exchange. Reuse descriptor, signal, pipe and networking helpers instead of reimplementing them without reason. Provide a clean C11/POSIX build, Makefile or equivalent, README, automated normal/negative fixtures and resource-ownership matrix. Demonstrate missing/dangling files, child exec failure or signal termination, truncated/oversized frame and finite timeout. Explain three C language hazards separately from recoverable POSIX errors. Supply an accurately labeled in-program or kernel trace. Have an independent reviewer reproduce a normal case and a fault case and defend a trade-off on an unfamiliar fixture.
  - Criteria: The independently reviewed source builds and documented operations behave as stated without privileged, paid or external services. No fixture escapes the owned tree, no unintended PID is signaled and all networking stays on loopback. Source, tests, output, ownership and failure cleanup support every claimed outcome; missing or uncorrected resource and error failures block completion. The reviewer can follow commands without hidden setup and the defense does not claim untested syscall behavior or memory safety.
  - Evidence: Versioned portable source, README and build/test commands, Makefile, fixture and oracle outputs, expected/actual status and cleanup matrix, trace provenance, documented defect/repair, outcome-to-evidence map, independent reviewer notes and accessible technical defense.

### Completion decision

All **seven required assessments** must satisfy their criteria and together demonstrate SEF7-O1 through SEF7-O14. The final utility may reuse previously verified source and evidence; the learner is not required to complete an additional checkpoint-and-lab pair in each module or build a second standalone project. Optional lesson exercises are formative.

Reviewers retain inspectable decisions, source revisions and evidence for each claimed outcome. Any uncorrected failure in descriptor ownership, child reaping, signal safety, directory identity, message framing or bounded retries blocks the relevant assessment. A learner must not be asked to use privileged accounts, unrelated processes or external hosts. The course remains `draft`; validation of this document does not establish `tested` or `verified` readiness under [Status Labels](../../spec/status-labels.md).
