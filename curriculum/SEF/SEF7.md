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

The instruction now follows the distinct competencies of descriptor and byte-stream ownership; bounded child processes and signals; filesystem identity and directory traversal; two-child pipe EOF; blocking framed TCP; nonblocking readiness and deadlines; and one integrated Unix utility. Generic resource and evidence principles are introduced once and then applied at each interface's new failure boundary, not repeated as standalone topic surveys. The **same seven required summative assessments** measure all 14 outcomes and may reuse verified components, fixtures and explanations. No fixed module or lesson count defines proficiency. No per-module graded quota, duplicate capstone, mandatory tracer, Rust requirement, paid product, external host or proprietary grader is added.

**Provisional duration:** 12–16 weeks at 10–15 focused hours per week (about 120–240 focused hours before individual remediation). The old seven-week estimate compressed descriptor/process lifetimes, filesystem identity hazards, and two distinct stages of TCP reliability. This estimate is **not** validated learner-time evidence, and course status remains `draft`.

**SEF/SYS scope:** SEF7 assesses C/POSIX descriptors, processes, local IPC, signals, file identity and single-peer loopback TCP. [SYS2](../SYS/SYS2.md) adds Rust resource ownership and C/Rust interface reasoning; [SYS10](../SYS/SYS10.md) studies kernel mechanisms; [SYS3](../SYS/SYS3.md) and [SYS4](../SYS/SYS4.md) develop concurrency and multi-client networking. **No SEF7 outcome or assessment is transferred** to SYS. Learners complete SEF7 under its own criteria.

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

### Module 1 — POSIX Resource Model, Descriptors and Reliable Byte I/O

#### Outcomes

- SEF7-O1
- SEF7-O2
- SEF7-O10
- SEF7-O11
- SEF7-O12

#### Lessons

1. **From C11 to actual POSIX calls** — Build on SEF6 ownership to distinguish ISO C11, POSIX interfaces, Linux behavior and a verified kernel-syscall trace; a libc wrapper call alone is not proof of one kernel event.
2. **Feature-test and toolchain assumptions** — Compile a bounded fixture with declared POSIX headers/macros, and record Linux, libc, C compiler, supported features and exact commands before claiming portability.
3. **Descriptor and open-file-description identity** — Draw owned integer descriptors and shared underlying open-file descriptions, specifying the lifetime and cleanup responsibility for each.
4. **Return and errno contracts** — Interpret positive byte counts, zero, -1 and EOF for specific calls; capture errno promptly on failure rather than reading a stale errno after success.
5. **Partial read/write loops** — Maintain a byte-progress invariant across short transfers and retry appropriate interrupted no-progress operations without duplicating previously transferred data.
6. **EOF and would-block distinctions** — Distinguish an actual read EOF from EINTR, EAGAIN and EWOULDBLOCK, documenting the blocking mode and avoiding a false successful complete read.
7. **dup, dup2 and shared offsets** — Predict a known file's offsets after duplication and bounded redirection, and validate observed bytes and offsets independently without touching real user files.
8. **Descriptor flags versus file status** — Observe FD_CLOEXEC per descriptor against O_APPEND/O_NONBLOCK on the shared open-file description, recording effects of duplication and later exec.
9. **Correct descriptor inheritance** — Specify the intended descriptors across exec, the special dup2 same-descriptor case and when closing unused inherited handles prevents leaks.
10. **close, EINTR and descriptor reuse** — Explain the documented Linux/POSIX.1-2024 distinction for close interrupted by a signal and why blindly retrying a descriptor number can close an unrelated reused handle.
11. **Owned failure and oracle cases** — Test clean, empty, short, interrupted, failed-open and invalid-target paths with independent expected bytes, flags, errors and a preserved sentinel.
12. **Actual versus simulated diagnostic evidence** — Label direct call/return logs, deterministic fault wrappers and optional kernel tracer evidence accurately, then repair one defined-behavior descriptor bug.

*Optional practice:* Predict the shared file offset of two duplicated handles, then verify it in a disposable file and explain the separate close-on-exec flag.

### Module 2 — Fork, Exec, Signals and Owned Child Lifecycles

#### Outcomes

- SEF7-O3
- SEF7-O4
- SEF7-O10
- SEF7-O11
- SEF7-O12

#### Lessons

1. **Child process and inherited resources** — Trace copied memory state, the environment and duplicated descriptor references after fork; do not mistake a new process for a new underlying open-file description.
2. **Bounded fork and exec setup** — Launch only fixed local child fixtures from a single-threaded process, handle fork failure and avoid executing untrusted shell input.
3. **Exec failure versus normal exit 127** — Use a close-on-exec error pipe to distinguish exec failure from a genuine program deliberately exiting with code 127.
4. **Wait status and reaping** — Use waitpid and WIFEXITED/WEXITSTATUS/WIFSIGNALED to distinguish success, nonzero exit and signal termination, and prevent zombie children.
5. **Signal disposition and sigaction** — Install a controlled handler and explain masks, signal order and interrupted calls without relying on deterministic scheduling or delivery order.
6. **Async-signal-safe handler limitations** — Set a volatile sig_atomic_t flag in a handler and move logging, allocation, resource release and child coordination to safe normal flow.
7. **Verified owned-child signalling** — Target only a child this test started, and explain why a stored PID alone is not a general capability against concurrent PID reuse.
8. **Interrupted waits and finite shutdown** — Handle EINTR while preserving finite wait deadlines; reap or terminate only owned children and identify which cleanup conditions can fail.
9. **Multithreaded-fork caveat and bounded environment** — Describe why arbitrary library calls in the child of a multithreaded parent are risky, without making multithreaded process supervision a new SEF prerequisite.
10. **Independent lifecycle fault matrix** — Compare intended output and child status for success, missing exec target, exit 127, controlled signal termination and timeout, then repair one lifecycle error.

*Optional practice:* Compare a deliberately missing executable with a child returning 127 and explain how the error pipe disambiguates the outcomes.

### Module 3 — Filesystem Identity, Permissions and Race-Aware Directory Traversal

#### Outcomes

- SEF7-O5
- SEF7-O6
- SEF7-O10
- SEF7-O11
- SEF7-O12

#### Lessons

1. **Pathnames versus object identity** — Compare stat, lstat and fstat on a synthetic regular file, symlink, dangling link and renamed entry, distinguishing a name from the object actually opened.
2. **Directory search and permission reality** — Predict mode/owner access with the actual unprivileged process and note ACL, filesystem, container and capability effects on expected permission failures.
3. **Replace-after-check counterexample** — Change a fixture name after metadata inspection and show why the previously checked pathname cannot authenticate a later open, while fstat identifies an already-opened object.
4. **Owned DIR streams and readdir errors** — Acquire opendir/closedir handles and set errno before readdir to distinguish end-of-directory from errors without assuming stable enumeration order.
5. **Deterministic listing and entry types** — Use a declared stable sorting policy for names; do not trust optional dirent.d_type hints as universally populated metadata.
6. **Symlink-follow and traversal policy** — Distinguish internal, dangling and outside-root links, and apply a documented no-follow or bounded-follow policy without altering external targets.
7. **Directory-relative identity checks** — Use fstatat/openat where supported and explain what AT_SYMLINK_NOFOLLOW or O_NOFOLLOW protects, and what it does not guarantee about ancestor components.
8. **Disappearing entries and denied access** — Handle deletion/rename between readdir and inspection; report missing, empty or unsupported permission-denial cases honestly.
9. **Bounded tree walk and TOCTOU limits** — Limit entries/depth, avoid symlink cycles and explain why string-prefix tests or check-then-open logic are not a hostile concurrent-filesystem security proof against time-of-check/time-of-use (TOCTOU) replacement.
10. **Independent metadata and cleanup evidence** — Compare a hand-built manifest with exact type/size/link observations and verify all directory handles close while unrelated sentinel bytes stay unchanged.

*Optional practice:* Inspect a file and an opened descriptor after a symlink-path replacement, then explain why their identities need not match.

### Module 4 — Pipe Inheritance, EOF and Two-Child IPC

#### Outcomes

- SEF7-O1
- SEF7-O2
- SEF7-O3
- SEF7-O7
- SEF7-O11
- SEF7-O12

#### Lessons

1. **Anonymous pipes as byte streams** — Define the producer/consumer byte contract and track both pipe ends separately from any application-level record boundary.
2. **Parent and child descriptor graph** — Draw every inherited read/write copy after fork and dup2 and decide precisely which process must close each unused end.
3. **Why EOF waits for all writers** — Prove that a consumer sees EOF only after every writer copy is closed, including forgotten parent or child handles.
4. **Two child statuses and exec errors** — Launch a known producer and consumer, reap both and propagate missing executables, nonzero exits and signal termination instead of trusting the last visible output.
5. **Partial progress and finite backpressure** — Respect short transfers and a bounded pipe-buffer capacity using small fixtures and a finite test harness, not an unbounded wait.
6. **SIGPIPE, EPIPE and early consumer exit** — Use an explicit broken-pipe signal policy, report actual failures and avoid accidentally terminating the coordinator.
7. **Injected writer-leak failure** — Retain one extra pipe write descriptor in a fault fixture, observe a bounded missing-EOF failure and correct the exact closure invariant.
8. **Independent IPC acceptance matrix** — Verify normal bytes, empty production, early consumer close, unavailable child and cleanup against separately predicted output, error and status results.

*Optional practice:* Annotate every writer copy remaining after a two-child fork and predict which one prevents a reader from seeing EOF.

### Module 5 — Blocking Loopback TCP and Explicit Framing

#### Outcomes

- SEF7-O1
- SEF7-O8
- SEF7-O10
- SEF7-O11
- SEF7-O12

#### Lessons

1. **One peer, ordered bytes, no message boundary** — Distinguish TCP stream order from send/recv call boundaries using small local client and server fixtures.
2. **Loopback-only listener and selected port** — Bind to 127.0.0.1 at an unprivileged available port, discover it with getsockname and account for each listening, accepted and client socket.
3. **Four network-order length octets** — Define a four-octet header and at-most-4096-octet payload with explicit empty-frame policy and eight-bit-octet compatibility assumptions for the Linux fixture.
4. **Complete frame read and write loops** — Track partial header/body progress and reject the advertised length before allocation rather than reading truncated data as a complete message.
5. **Fragmentation and coalescing experiments** — Split header and payload writes and send multiple frames; independently verify exact recovered bytes instead of assuming network packet or write boundaries.
6. **EOF, EINTR and broken send failures** — Distinguish clean EOF after a frame from premature header/body EOF, connection failure and EPIPE, documenting a safe SIGPIPE policy.
7. **Bounded blocking waits** — Use supported socket or enclosing-harness deadlines for accept/connect/read/write rather than presuming an idle peer will unblock itself.
8. **Invalid and hostile-shaped local inputs** — Test over-4096 length, malformed/incomplete header, truncated body, empty payload by policy and refused loopback connection without any external host.
9. **Protocol oracle and SYS4 boundary** — Record expected network-order bytes, observed listener, statuses and cleanup; explain why multi-client services, overload and backpressure are separate SYS4 work.

*Optional practice:* Hand-encode a small four-octet header and show how one-byte receiver progress reassembles it without relying on TCP packetization.

### Module 6 — Nonblocking Poll, Frame State and Monotonic Deadlines

#### Outcomes

- SEF7-O1
- SEF7-O8
- SEF7-O9
- SEF7-O10
- SEF7-O11
- SEF7-O12

#### Lessons

1. **What nonblocking mode actually changes** — Set O_NONBLOCK where needed and distinguish EAGAIN/EWOULDBLOCK from EOF without reintroducing the blocking TCP protocol.
2. **poll readiness is not completed I/O** — Read revents together with the actual return of recv/send; readiness alone cannot establish receipt of a complete frame.
3. **Pending nonblocking connect when applicable** — When using nonblocking connect, treat EINPROGRESS as pending and check SO_ERROR after writable readiness instead of assuming POLLOUT means connection success.
4. **Separate header, body and send offsets** — Track partial progress with a bounded state machine and enforce the 4096-payload limit independently of packet segmentation.
5. **A single CLOCK_MONOTONIC deadline** — Compute remaining time after each fragment and interrupted poll without restarting the original end-to-end deadline.
6. **POLLHUP/POLLERR and interrupted operations** — Diagnose disconnection, EINTR, short I/O and error events by consulting real interface statuses rather than interpreting a ready bit as a completed frame.
7. **No spin on EAGAIN** — Wait for later readiness and prove idle/malformed-peer cases terminate under finite bounds without busy-looping.
8. **Independent timeout and fragmentation tests** — Exercise a four-part header, multi-part body, valid repeat, oversized frame, early close, idle peer and injected EINTR/would-block against predicted results.
9. **Repair a state or deadline bug** — Capture a seeded offset/timer regression, correct it and verify both payload bytes and cleanup with a new unfamiliar case.
10. **Explicit level-of-depth decision** — Document tested platform limits and distinguish a single-peer poll loop from SYS4 multi-client fairness/backpressure and SYS7 production observability.

*Optional practice:* Trace an EINTR during poll halfway through an incomplete header and explain why its deadline stays fixed as the received-byte counter grows.

### Module 7 — Integrated Unix Utility, Resource Faults and Independent Defense

#### Outcomes

- SEF7-O1
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
- SEF7-O13
- SEF7-O14

#### Lessons

1. **One reusable mini Unix utility** — Reuse already assessed descriptor, owned-child, filesystem, pipe and framed-TCP helpers in an inspect/run/net-demo CLI rather than creating independent projects.
2. **Real command and environment contracts** — Specify accepted inputs, statuses, file/process/network boundaries, compiler/Make setup and what evidence a fresh nonprivileged checkout can reproduce.
3. **Complete ownership and partial-failure ledger** — Map each descriptor, DIR handle, child, socket and buffer to its creator, release, and correct state on full or partial success.
4. **Independent cross-interface fault fixtures** — Exercise missing/dangling files, failed exec, signal exit, writer-leak EOF, truncated/oversized frame and finite deadline against known byte/status/identity oracles.
5. **Controlled cleanup and unaffected state** — Verify valid owned-resource cleanup after normal and error paths, reaping test children and preserving an unrelated fixture sentinel, with honest PID/path race limits.
6. **Trace provenance and portability** — Label in-process return/errno logs, wrapper-injected failures and actual optional syscall traces separately, recording standards edition, compiler and libc versions.
7. **Source-located unfamiliar defect repair** — Reproduce one new error, identify which owner/state/return contract it violates, repair it and retain a failing-before/green-after regression.
8. **Accessible independent reproduction** — Provide semantic text/Markdown docs, precise build/test commands and an outcome-evidence map; record actual independent reviewer results for a normal and failing case.
9. **Foundational-to-SYS technical defense** — Defend the design choice, untested limitations and why Rust comparison, kernel internals and production multi-client services belong in SYS, not hidden SEF7 gates.

*Optional practice:* Map the seven published assessment decisions onto the existing utility's source, independent oracle and reviewer evidence without adding a new assessment.

## Completion requirements

### Existing assessment evidence by instructional stage

This table is a **teaching/evidence crosswalk**, not a new grading contract. The original Work, Criteria, Evidence and review conditions below remain unchanged, and the same tested helper may satisfy more than one existing assessed requirement.

| Assessment | Instructional stages | Already required evidence |
| --- | --- | --- |
| `SEF7-AS1` | Module 1 | Descriptor offsets and flags, partial I/O, EINTR, accurate return/error and ownership contracts |
| `SEF7-AS2` | Module 2 | Controlled fork/exec/error pipe, signals, waitpid and bounded child cleanup |
| `SEF7-AS3` | Module 3 | stat/lstat/fstat, link/permission claims and race-aware bounded directory inspection |
| `SEF7-AS4` | Modules 2 and 4 | Two-child pipe/dup2, EOF from actual writer closure, SIGPIPE/EPIPE and byte/status evidence |
| `SEF7-AS5` | Module 5 | Blocking loopback TCP, four-octet frames, truncation and independent payload oracles |
| `SEF7-AS6` | Modules 5–6 | Nonblocking poll state, EAGAIN/EINTR, finite monotonic deadline and cleanup |
| `SEF7-AS7` | Module 7, reusing previous evidence | One C Unix utility, actual failure and resource ownership, independent review and technical defense |

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

### Current disciplinary boundary

SEF7's fourteen outcomes and seven summative evaluations remain mandatory. Their Work, Criteria and Evidence specify the assessed C/POSIX foundation. Advanced Rust, kernel and network work cannot supply missing SEF7 evidence. Assessment records identify the source revision, outcomes, expected and observed results, and reviewer decision. The course remains `draft` pending learner and independent review evidence.
