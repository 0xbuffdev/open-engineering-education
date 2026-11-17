# SEF7 → SYS Competency Boundary and Evidence Retention

> [SEF7](SEF7.md) · [SEF program](README.md) · [SYS program](../SYS/README.md) · [Accepted RFC 0003](../../rfcs/0003-sef-academic-progression.md)

**Status: non-normative, proposed downstream mapping — not an enacted transfer or assessment migration.**

## Purpose and controlling rules

SEF7, [Unix System Interfaces](SEF7.md), is the assessed **common foundational Unix programming course** following C11 memory and resource models in SEF6 and shell behavior in SEF3. It uses a single controlled Linux environment and learner-owned fixtures to teach descriptor/resource ownership, two-child process behavior, files and directories, signals, pipes and bounded *single-peer* loopback TCP including a `poll` state machine.

The migrated advanced SYS program deepens these models through **C/Rust comparative systems programming, concurrency, multi-client services, backpressure, observability, storage durability and production failure behavior**. These are not silently folded into SEF7 and are not considered passed merely because a learner produced a small Unix utility.

**Current evidence authority:**

- The 14 published `SEF7-O1`–`SEF7-O14` and seven published `SEF7-AS1`–`SEF7-AS7` remain required *in SEF7*. The SEF7 [course definition](SEF7.md) and current SEF [catalog](README.md) govern completion. Historical review evidence remains tied to its assessed course revision.
- All ten SYS courses, including [SYS10](../SYS/SYS10.md), now publish outcome-driven OEE `v0.2.0` **draft** requirements and summative evidence in the [SYS catalog](../SYS/README.md). The destinations in this historical mapping remain **non-binding candidates for a hypothetical future SEF7 transfer**, not evidence of equivalent credit, learner-tested readiness or a governance approval.
- No SYS outcome/assessment has been added by this map. No SEF7 requirement may be removed based solely on a common topic title. Transfer would require an accepted subsequent architecture revision, a real matching assessed SYS capability with public Work/Criteria/Evidence and prerequisite access, explicit version-pinned evidence mapping, steward review and separate migration/approval.
- Rust study and C/Rust comparison belong in SYS, especially **[SYS2](../SYS/SYS2.md)**, not in SEF7. The new SYS source does not alter any original SEF7 completion expectation or historical learner result.

## Shared foundation versus advanced systems depth

| Boundary | Required SEF7 foundation | Candidate advanced SYS extension |
| --- | --- | --- |
| Language and platform | C11 with documented POSIX interfaces and Linux implementation assumptions; identify system call vs library wrappers | [SYS2](../SYS/SYS2.md): Rust ownership/borrowing and **side-by-side C/Rust resource/FFI/system-interface analysis**, additional platform details and robust systems-component design |
| Operating-system implementation | SEF7 uses C/POSIX resource APIs without a kernel-internals completion obligation | [SYS10](../SYS/SYS10.md): educational kernel traps, scheduling, virtual-memory management, VFS/device pathways and protection, beyond SEF7's public interface work |
| Processes and signals | Bounded, directly launched **owned local children**; correct exit/exec distinction, safe handler and reaping | [SYS2](../SYS/SYS2.md): robust cross-language process supervision, system-resource architecture and deep OS behavior; [SYS3](../SYS/SYS3.md) for concurrent-process/thread scheduling and synchronization |
| Files and directories | Fixture `stat`/`lstat`/`fstat`, directory-relative reasoning, nonadversarial safe paths and honest TOCTOU limitations | [SYS2](../SYS/SYS2.md): more sophisticated resource abstraction and OS-specific primitives; [SYS5](../SYS/SYS5.md): durable files, WAL, crash-recovery and data integrity |
| Pipes and local IPC | One two-child pipe, descriptor closure/EOF and finite failure handling | [SYS2](../SYS/SYS2.md): more robust IPC facilities and lifecycle integration; [SYS3](../SYS/SYS3.md): concurrent queues, atomics and memory-ordering guarantees |
| Networking | Framed **single-peer**, loopback-only TCP; one `poll`-driven connection with finite deadlines | [SYS4](../SYS/SYS4.md): multi-client/concurrent Rust service, connection limits, backpressure, partial writes, overload, graceful shutdown, service-oriented protocol reliability |
| Correctness, tracing and performance | Independent byte/file/status oracles, short-I/O fault wrappers, bounded timeouts and truthful source/trace provenance | [SYS7](../SYS/SYS7.md): profiling, attribution, observability and controlled latency/throughput investigations; [SYS8](../SYS/SYS8.md): production reliability and operational review |
| Integration | One locally reproducible mini Unix utility using prior SEF7 evidence | [SYS9](../SYS/SYS9.md): systems-focused capstone with greater concurrency/persistence/service load and resilience, not a replacement for earlier SEF7 completion |

## Explicit mapping of every existing SEF7 learning outcome

The **target is a curricular destination to review**, not proof it currently has sufficient assessed depth. All current statuses are **retain in SEF7**.

| Required SEF7 outcome | Currently assessed foundation | Candidate SYS destination and advanced distinction |
| --- | --- | --- |
| `SEF7-O1` | Correct POSIX descriptor read/write, partial results, EINTR, EOF and errno | [SYS2](../SYS/SYS2.md) deeper C/Rust I/O abstraction; [SYS4](../SYS/SYS4.md) concurrent network I/O |
| `SEF7-O2` | Shared open-file descriptions, per-descriptor FD_CLOEXEC, dup/redirect | [SYS2](../SYS/SYS2.md) cross-language handle lifecycle, inheritance and OS facilities |
| `SEF7-O3` | Bounded fork/exec/waitpid and distinct exec-failure evidence | [SYS2](../SYS/SYS2.md) robust process supervision and C/Rust comparison |
| `SEF7-O4` | Minimal async-signal-safe handling and owned-child cleanup | [SYS2](../SYS/SYS2.md) robust shutdown; [SYS3](../SYS/SYS3.md) concurrency/signal interaction |
| `SEF7-O5` | File identity, stat/lstat/fstat, symlink and permission constraints | [SYS2](../SYS/SYS2.md) advanced OS object policies; [SYS5](../SYS/SYS5.md) durable storage identity |
| `SEF7-O6` | Owned-directory traversal, ordering and link/TOCTOU caveats | [SYS2](../SYS/SYS2.md) stronger directory-resource design; [SYS5](../SYS/SYS5.md) storage invariants |
| `SEF7-O7` | Two-child pipes, EOF via descriptor closure and error propagation | [SYS2](../SYS/SYS2.md) advanced IPC; [SYS3](../SYS/SYS3.md) concurrent coordination |
| `SEF7-O8` | Local single-peer TCP, four-octet framing and bounded messages | [SYS4](../SYS/SYS4.md) multi-client protocols and backpressure |
| `SEF7-O9` | Single nonblocking `poll` state machine, deadlines, EAGAIN | [SYS4](../SYS/SYS4.md) concurrent event loop, fairness, resource caps and overload |
| `SEF7-O10` | Linux, libc and POSIX provenance; library call vs syscall trace distinction | [SYS2](../SYS/SYS2.md) C/Rust portability/toolchain detail; [SYS7](../SYS/SYS7.md) evidence-based kernel/service tracing |
| `SEF7-O11` | Resource owner and error-state contracts for descriptors, children and sockets | [SYS2](../SYS/SYS2.md) explicit Rust/C resource models; [SYS4](../SYS/SYS4.md) multi-client lifecycle |
| `SEF7-O12` | Independent synthetic byte/state fixtures and seeded failure recovery | [SYS2](../SYS/SYS2.md) stronger fault modeling; [SYS7](../SYS/SYS7.md) measured diagnosis |
| `SEF7-O13` | One bounded metadata/process/loopback Unix utility | [SYS2](../SYS/SYS2.md) Rust service utility and comparative boundary; [SYS4](../SYS/SYS4.md) multi-client service |
| `SEF7-O14` | Accessible review and defensible Linux/POSIX resource limits | [SYS7](../SYS/SYS7.md) performance claims; [SYS8](../SYS/SYS8.md) operational design; [SYS9](../SYS/SYS9.md) advanced capstone |

## Explicit mapping of every existing SEF7 assessment

| Required assessment | Still compulsory in SEF7 | Candidate advanced extension — **not equivalent credit** |
| --- | --- | --- |
| `SEF7-AS1` | Descriptor sharing, partial I/O, FD_CLOEXEC and EINTR evidence | [SYS2](../SYS/SYS2.md): C/Rust handle ownership and deeper OS I/O design |
| `SEF7-AS2` | Fork/exec error-pipe, safe signals, child cleanup and reaping | [SYS2](../SYS/SYS2.md): robust cross-language process supervision |
| `SEF7-AS3` | Directory identity, link policy, metadata and safe owned fixtures | [SYS2](../SYS/SYS2.md) advanced filesystem policies; [SYS5](../SYS/SYS5.md) durability |
| `SEF7-AS4` | Two-child pipeline with correct descriptor closure and statuses | [SYS2](../SYS/SYS2.md) advanced IPC; [SYS3](../SYS/SYS3.md) concurrency |
| `SEF7-AS5` | Single-peer blocking loopback TCP and bounded framing | [SYS4](../SYS/SYS4.md) concurrent service protocol under backpressure |
| `SEF7-AS6` | One nonblocking `poll` connection and monotonic deadline | [SYS4](../SYS/SYS4.md) event-loop scale, fairness, overload and clean shutdown |
| `SEF7-AS7` | One mini Unix utility with independent review and prior evidence reuse | [SYS2](../SYS/SYS2.md), [SYS4](../SYS/SYS4.md) and [SYS9](../SYS/SYS9.md) for genuinely advanced systems outcomes |

## Preconditions for any future transfer

A subsequent separately approved SYS architecture and outcome-driven migration must, **before editing SEF7 requirements**:

1. Recheck the current SYS architecture, prerequisite graph, Rust handoff, Linux/Unix scope and realistic workload for the specific competency proposed for transfer; a migrated draft format alone does not prove educational equivalence.
2. Specify the advanced SYS outcome and required assessment in public OEE `v0.2.0` Work, Criteria and Evidence terms; validate against a real downstream prerequisite path, including learners who complete SEF without enrolling in SYS.
3. Compare actual competencies rather than matching topic names. Prove that **every** removed SEF7 requirement has a valid new teaching and assessed-evidence destination available to affected learners; if it has no such destination, **do not remove it**.
4. Publish source-revision-pinned mapping from the old outcome/assessment IDs and learner evidence to new IDs; distinguish reusing genuine evidence from automatically awarding untested credit. Do not revoke or silently regrade past completions.
5. Require a separately reviewed and approved, revision-pinned SEF7 change on a focused branch after substantive equivalence and downstream learner access are established. The SYS migration and this historical map do not approve any SEF7 transfer.

**Standing decision: keep every SEF7 outcome and assessment obligation intact.** Advanced SYS work builds on them; source migration of SYS neither cancels any requirement nor automatically awards equivalent completion. A future SEF7 transfer would require its own evidence-backed governance decision.
