# SEF7 — Unix System Interfaces

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF3](SEF3.md), [SEF6](SEF6.md)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

SEF3 already establishes safe shell invocation, process-environment inheritance, command lookup, Bash versus POSIX-sh portability and known GNU-tool dependencies. SEF6 also establishes ISO C11 memory/object lifetime, checked allocation, bounded parsing, manually owned container libraries and reproducible toolchain diagnostics before SEF7 begins. This course instead examines **C and POSIX system interfaces** (file descriptors, fork/exec, directory identity, signals, sockets) with explicit resource ownership; it does not replace the earlier command-line portability assessments. Actual shell behavior is not conflated with the C ABI or operating-system syscall semantics.

Understand how a C program requests Unix operating-system services and handles their failure. Start with file descriptors and partial I/O, then investigate process creation and termination, filesystem identity, signals, pipes, and framed TCP streams. Finish by building a small, reproducible Unix utility that combines these interfaces with explicit resource ownership.

The reference environment is a **nonprivileged local Linux environment**, C11-capable compiler, and available POSIX interfaces. Document actual tool and OS versions, compilation flags and feature-test macros; a typical compiler invocation is `cc -std=c11 -D_POSIX_C_SOURCE=200809L -Wall -Wextra -Wpedantic`. Use a learner-owned temporary tree, controlled child processes, and `127.0.0.1` loopback only. No root account, external network service, production files, real unrelated processes, paid service, or proprietary grader is needed. A correct in-program interface trace is an acceptable alternative when optional kernel tracing software such as `strace` is unavailable; label the evidence accurately.

The course distinguishes **ISO C11**, **POSIX application interfaces**, Linux implementation details and actual kernel syscall events. It distinguishes a descriptor from its underlying **open-file description**, and a TCP byte stream from application messages. Code must address partial transfer, `EINTR`, EOF, resource cleanup, and bounded waits. Never assume pathname checks remain true after an object changes, or that signal handlers can safely call arbitrary library functions.

**Standards and safety limits:** `close` interrupted by a signal has platform- and POSIX-edition-sensitive semantics, including a known Linux/POSIX.1-2024 divergence. The Linux implementation can release a descriptor before returning some errors; blindly retrying `close(fd)` may close a newly reused descriptor. Learners must record actual target behavior and must not claim a universal retry rule. Similarly, a prior check that a PID belongs to an owned child is not proof against every possible PID reuse or process-lifetime race. Use controlled children, bounded waits and clear ownership while stating the remaining limitations.

The original eight subject areas now form **eleven progressively ordered modules**, separating foundational POSIX contracts, directory-traversal guarantees, and integrated failure/ownership investigation before the existing mini utility. The **same seven required summative assessments** measure all 14 outcomes and may reuse verified components, fixtures and explanations. No per-module graded quota, duplicate capstone, mandatory tracer, Rust requirement, paid product, external host or proprietary grader is added.

**Provisional duration:** 12–16 weeks at 10–15 focused hours per week (about 120–240 focused hours before individual remediation). The old seven-week estimate compressed descriptor/process lifetimes, filesystem identity hazards, and two distinct stages of TCP reliability. This estimate is **not** validated learner-time evidence, and course status remains `draft`.

**SEF/SYS scope:** The [SEF7–SYS destination map](UNIX-SYS-BOUNDARY.md) maps every current SEF7 outcome and assessment to candidate advanced SYS courses. The nine published SYS courses are still **legacy drafts**, not verified `v0.2.0` evidence successors. Therefore no SEF7 outcome, assessment or existing learner completion is transferred or removed here. Future [SYS2](../SYS/SYS2.md) owns advanced C/Rust comparisons and low-level system-resource work, while [SYS4](../SYS/SYS4.md) owns multi-client/concurrent networking, service backpressure and reliability. Rust is not silently introduced as a SEF7 prerequisite.

Optional public references include the [Linux `close(2)` manual](https://man7.org/linux/man-pages/man2/close.2.html), [POSIX.1-2024 online standard](https://pubs.opengroup.org/onlinepubs/9799919799/), and [Linux signal-safety guidance](https://man7.org/linux/man-pages/man7/signal-safety.7.html). They are free cross-checks, not hidden mandatory course materials.

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

### Module 1 — POSIX System Model and Resource Contracts

#### Outcomes

- SEF7-O1
- SEF7-O10
- SEF7-O11
- SEF7-O12

#### Lessons

1. **From C11 to POSIX** — Distinguish C language and standard-library guarantees from POSIX interfaces, Linux details, and actual kernel syscalls; a libc function call is not necessarily one kernel event.
2. **Feature-test macros and environment** — Record Linux/libc/compiler versions, _POSIX_C_SOURCE and applicable headers, and identify optional Linux-only facilities.
3. **Return values and errno** — Check each interface's success/error convention; capture errno promptly after failure and avoid reading a stale value after success.
4. **Bounded fixture ownership** — Use only disposable owned files, known child processes and 127.0.0.1 loopback; prohibit altering unrelated user resources.
5. **Resource ownership and state** — Describe ownership and cleanup of descriptors, directory handles, child PIDs, buffers, and sockets on normal and partial-error paths.
6. **Independent output oracles** — Derive expected bytes, exit codes, directory identities and frame encodings separately from the tested implementation.
7. **Partial progress and failure** — Distinguish positive transfers, EOF, EINTR and EAGAIN, and do not reset progress on a partially successful operation.
8. **Portable claim boundaries** — Separate POSIX-conforming source from Linux-specific observed behavior, including the version-sensitive semantics of close.
9. **Diagnostic provenance** — State whether observations are source-level logs, supplied traces, optional syscall traces or actual kernel evidence.

*Optional practice:* Draft an ownership/return/error table for a small disposable file operation and identify which assumptions depend on Linux.

### Module 2 — Descriptors, Open-File Descriptions and Reliable Byte I/O

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

10. **Return conventions and partial progress** — Check ssize_t and status results, advance after positive partial writes, retry only appropriate zero-progress EINTR errors, and preserve transferred bytes.
11. **EOF, would-block and close** — Distinguish read EOF from EAGAIN/EWOULDBLOCK, and explain Linux close/EINTR descriptor-number reuse hazards and standards differences.
12. **Descriptor versus open-file flags** — Compare FD_CLOEXEC per-descriptor with shared file-status flags including O_APPEND/O_NONBLOCK; record fcntl observations.
13. **Independent descriptor oracle** — Predict offsets after dup and inspect a disposable file rather than assuming each integer descriptor has an independent file offset.

*Optional practice:* Draw an open/dup/close descriptor table and inspect shared file offsets using a disposable file.

### Module 3 — Fork, Exec and Owned Child Processes

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

9. **Exec-error evidence** — Use a close-on-exec error pipe or equivalent explicit launch-error protocol to distinguish exec failure from a child deliberately exiting with code 127.
10. **Bounded child lifecycle** — Explain interrupted waitpid, controlled child cleanup, zombie avoidance and why PID identity checks alone have concurrency limits.
11. **Multithreaded fork caveat** — Describe why executing unsafe library operations in a forked child of a multithreaded parent is hazardous; a single-threaded teaching fixture avoids this added system complexity.

*Optional practice:* Reap a controlled child with a deliberately nonzero exit status and compare it with a missing executable.

### Module 4 — Signals, Handler Safety and Child Coordination

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

6. **sigaction and signal masks** — Describe signal registration, restart behavior, EINTR and why a handler should not assume a deterministic delivery order.
7. **Async-signal-safe code** — Use volatile sig_atomic_t to record a flag; leave printf, malloc, complex logging and resource cleanup to the normal program flow.
8. **Owned PID restrictions** — Terminate only a known test-owned process, track reaping and report residual PID-reuse safety limitations instead of claiming complete race freedom.
9. **Reproducible signal faults** — Use bounded controlled children, a supplied trace when needed, and an independently predicted wait-status matrix.

*Optional practice:* Use an owned process to observe a graceful termination request and a bounded wait.

### Module 5 — Filesystem Identity, Links and Permission Models

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

8. **Object identity after open** — Compare stale pathname stat with fstat on the actual opened object after a fixture rename/replacement.
9. **Directory-relative identity** — Introduce openat/fstatat and no-follow flags where supported, stating their real guarantees and remaining race limits.
10. **Permission and access caveats** — Differentiate observed permission failures from a guarantee that an unprivileged environment can reproduce EACCES consistently.

*Optional practice:* Compare stat, lstat and fstat for regular, symlink and dangling-link fixture entries.

### Module 6 — Directory Traversal and Race-Aware Fixture Safety

#### Outcomes

- SEF7-O5
- SEF7-O6
- SEF7-O11
- SEF7-O12

#### Lessons

1. **Directory handles and ownership** — Use opendir, readdir and closedir with proper success/EOF/error interpretation and owned cleanup.
2. **Nondeterministic entry order** — Define and implement a stable presentation order; do not assume readdir enumeration order is portable.
3. **Metadata without unsupported assumptions** — Check directory entry identity and optional d_type handling rather than trusting unsupported entry type hints.
4. **Symbolic links and directory boundaries** — Apply a published link-follow policy, including dangling and outside-root symlink fixtures without modifying external targets.
5. **Directory-relative interfaces** — Compare fstatat/openat with string-concatenated paths and accurately describe remaining symlink/TOCTOU risks.
6. **Disappearing entries** — Handle a filename removed or renamed between enumeration and inspection without silently inventing a successful result.
7. **Permissions and missing objects** — Exercise empty, hidden, missing, dangling and permission-denied fixtures when the local environment supports the denial.
8. **Bounded traversal and cycles** — Prevent accidental recursive symlink cycles and avoid treating a string prefix as a sufficient hostile-filesystem security boundary.
9. **Teardown and independent evidence** — Preserve unrelated sentinel files, release directory handles and compare a separately prepared fixture manifest.

*Optional practice:* Inspect an owned directory with a dangling and outside-root symlink and explain why a nonadversarial fixture does not prove adversarial containment.

### Module 7 — Pipes, Redirection and Two-Child IPC

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

6. **Pipe EOF proof** — Explain why EOF requires every writer descriptor copy in parent and children to be closed.
7. **SIGPIPE and EPIPE** — Demonstrate a documented broken-pipe signal policy and explicitly report both child results.
8. **Bounded failure diagnosis** — Use a finite harness for a deliberately forgotten write end, then fix the owner/cleanup defect without signalling unrelated processes.
9. **Byte oracle and stream framing** — Treat pipes as byte streams, retain partial transfer progress, and independently check the producer-consumer result.

*Optional practice:* Explain why an inherited extra write end delays a pipe reader's EOF.

### Module 8 — Bounded Blocking TCP and Framing

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

8. **Local port discovery** — Bind to loopback using a controlled available unprivileged port and inspect getsockname; never connect to external peers.
9. **Four-octet length prefix** — Describe network byte order and the four eight-bit-octet protocol header; declare compatibility assumptions of the reference Linux environment.
10. **Frame limits and truncation** — Reject payloads above 4096 before allocation, and distinguish early EOF in header/body from a valid empty frame.
11. **Segmentation versus message identity** — Test one length header split across writes and demonstrate that TCP does not preserve send boundaries.
12. **Basic service versus SYS4** — Distinguish a bounded local single-peer experiment from advanced multi-client, concurrent, backpressure-aware service work.

*Optional practice:* Send two framed messages using a small local client and inspect their length prefixes.

### Module 9 — poll-Driven Nonblocking I/O and Monotonic Deadlines

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

6. **End-to-end timeout invariant** — Base the overall deadline on CLOCK_MONOTONIC and recompute remaining time after EINTR; never reset it on every successful fragment.
7. **Partial-frame state machine** — Track header/body and send offsets and distinguish readiness from completion of a full frame.
8. **POLLHUP and POLLERR** — Handle disconnection, would-block, and actual read/write results rather than treating revents as proof of payload arrival.
9. **No busy spins** — Wait for readiness after EAGAIN and prove malformed/idle peers fail in finite time.
10. **Advanced reliability destination** — Explain why multi-connection fairness, overload/backpressure and production shutdown are assessed later in SYS4.

*Optional practice:* Trace a header split across writes and predict how poll and recv interleave.

### Module 10 — Resource Lifecycle, Fault Models and Reviewable Evidence

#### Outcomes

- SEF7-O2
- SEF7-O3
- SEF7-O4
- SEF7-O5
- SEF7-O6
- SEF7-O7
- SEF7-O8
- SEF7-O9
- SEF7-O10
- SEF7-O11
- SEF7-O12
- SEF7-O14

#### Lessons

1. **Complete ownership ledger** — Track every descriptor, directory handle, child process and socket on both success and failure paths.
2. **Partial success and rollback** — Distinguish partial byte transfers, already-started children, replaced file names and partially received frames.
3. **Deterministic fault injection** — Use injected EINTR/short transfer, missing executable, early peer close and timeout fixtures instead of waiting for rare scheduling accidents.
4. **Source trace versus syscall trace** — Label in-program logs, wrapper returns and optional strace output accurately without equating them.
5. **Independent fixtures** — Retain byte oracle, child status table, filesystem metadata manifest and frame encoding independently from tested functions.
6. **Nonprivileged cleanup** — Stop only test-owned children, release all owned resources, and retain a sentinel showing unrelated files were unchanged.
7. **Portability disclosure** — Document libc, Linux version, feature macros, supported options and standards/implementation differences.
8. **Real reviewer evidence** — Record source locations, a reproduced defect, corrective tests and an explicit incomplete-coverage statement.

*Optional practice:* Create a resource state table linking an already assessed descriptor, child, directory, pipe and socket failure to the same final utility.

### Module 11 — Integrated Mini Unix Utility and Technical Defense

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

7. **One reusable artifact** — Carry assessed AS1–AS6 helpers into the inspect/run/net-demo commands instead of building independent capstones.
8. **Safe fixture and host boundaries** — Verify owned directories, test children, loopback-only sockets and bounded input/waits during clean setup.
9. **Accessible independent review** — Use plain-text or semantic Markdown evidence and ask the reviewer to reproduce an unfamiliar normal/failure case.
10. **SEF/SYS boundary in defense** — Explain why Rust comparisons, concurrent multi-client networking, storage durability and production observability belong in SYS.

*Optional practice:* Sketch mini utility commands, error outcomes and an independent reviewer evidence map.

## Completion requirements

### Existing assessment evidence by instructional stage

This table is a **teaching/evidence crosswalk**, not a new grading contract. The original Work, Criteria, Evidence and review conditions below remain unchanged, and the same tested helper may satisfy more than one existing assessed requirement.

| Assessment | New module stages | Already required evidence |
| --- | --- | --- |
| `SEF7-AS1` | Modules 1–2 | Descriptor offsets/flags, partial I/O, EINTR and ownership |
| `SEF7-AS2` | Modules 3–4 | fork/exec error pipe, signals, waitpid and bounded child cleanup |
| `SEF7-AS3` | Modules 5–6 | Stat/link/permission behavior and race-aware directory inspection |
| `SEF7-AS4` | Module 7 | Two-child pipes, SIGPIPE/EPIPE, EOF and independent byte checks |
| `SEF7-AS5` | Module 8 | Bounded blocking loopback TCP with four-octet framing |
| `SEF7-AS6` | Module 9 | Nonblocking poll state machine, EINTR, EAGAIN and deadlines |
| `SEF7-AS7` | Modules 10–11 | Single integrated Unix utility, independent failure/cleanup defense |

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

### Historical evidence and SEF/SYS transition

This review implements the SEF7 academic-boundary follow-up in [accepted RFC 0003](../../rfcs/0003-sef-academic-progression.md). The earlier [SEF7 curriculum at commit `635661746826e00751315a42ec39c4938f417f67`](https://github.com/0xbuffdev/open-engineering-education/blob/635661746826e00751315a42ec39c4938f417f67/curriculum/SEF/SEF7.md) remains the authoritative historical evidence contract for previously assessed work.

**All fourteen original `SEF7-O1`–`SEF7-O14` definitions and seven original `SEF7-AS1`–`SEF7-AS7` blocks (including Work, Criteria, Evidence and review variations) are preserved exactly.** There is no new, removed, renumbered or automatically reassessed learner requirement. The eleven modules and 12–16-week provisional estimate adjust instruction and disclosure, not completion. The [explicit SEF7–SYS map](UNIX-SYS-BOUNDARY.md) is a proposal for later SYS redesign, **not an enacted transfer**: the mapped SYS courses are legacy drafts and cannot yet replace any SEF7 assessment. No Rust requirement, extra capstone, fixed lab count, global OEE specification or readiness-status promotion has been introduced.
