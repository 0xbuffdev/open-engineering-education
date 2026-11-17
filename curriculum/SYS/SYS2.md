# SYS2 — Systems Programming with C & Rust

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS1](SYS1.md) (completed SEF includes SEF6 and SEF7)
**Duration:** 16–20 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; validate with learners)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Curriculum design guide](../DESIGN-GUIDE.md)

## Overview

This is **SYS's first required, fully taught Rust course**. It builds on SEF6 C11 memory safety and SEF7's assessed C/POSIX descriptors, process handling, pipes and single-peer networking without repeating foundational graduation work. Rust ownership, borrowing, lifetimes, error types, modules, Cargo and safe resource handling are taught before SYS3 concurrency, SYS4 services or SYS5 storage. Comparative C/Rust work evaluates equivalent behavior and real limitations of each language, rather than celebrating safety by assertion.

Use a stable Rust toolchain, C compiler and nonprivileged Linux environment with disposable synthetic fixtures. Unsafe Rust/FFI is treated as a precisely bounded safety and interoperability topic, not a default implementation technique; no privileged daemon, public host or paid service is required. The substantial exit performance is a robust supervised multi-process Rust systems utility with independent failure tests and a technical defense.

## Learning outcomes

- **SYS2-O1:** Build and test reproducible multi-module Rust programs using Cargo, explicit toolchains and robust error contracts.
- **SYS2-O2:** Explain and apply ownership, moves, borrowing, lifetimes, slices and Drop to systems-facing APIs.
- **SYS2-O3:** Model invalid, pending and completed operations with enums, Option, Result and checked conversions.
- **SYS2-O4:** Manage bounded buffers, files and other OS resources with explicit owned/borrowed lifetimes and cleanup policies.
- **SYS2-O5:** Compare equivalent C11/POSIX and Rust implementations using independently verified behavior and precise memory-safety claims.
- **SYS2-O6:** Analyze process/resource inheritance, address-space boundaries and multichild lifecycle beyond SEF7's foundational exercises.
- **SYS2-O7:** Implement failure-aware child supervision, bounded pipes, timeouts, signal policy, cancellation and reaping.
- **SYS2-O8:** Use Rust Unix abstractions for file, descriptor and IPC operations while identifying Linux-specific behavior.
- **SYS2-O9:** Identify unsafe, FFI, ABI and panic boundaries and specify the invariants required to prevent undefined behavior.
- **SYS2-O10:** Reproduce and diagnose a C memory/resource defect and its Rust counterpart using diagnostics, independent tests and limitations.
- **SYS2-O11:** Implement bounded byte-oriented parsing, path validation and output contracts without conflating UTF-8 strings with OS paths.
- **SYS2-O12:** Deliver a reproducible multi-module Rust utility with controlled normal, invalid, partial-failure and cleanup paths.
- **SYS2-O13:** Explain a previously unseen ownership/resource failure and defend an evidenced correction.
- **SYS2-O14:** Distinguish language, library, POSIX, Linux and hardware guarantees in systems-facing decisions.

## Modules

### Module 1 — SEF-to-Rust Systems Handoff

#### Outcomes

- SYS2-O1
- SYS2-O5
- SYS2-O14

#### Lessons

1. **Prior C/POSIX capability** — Review SEF6 object lifetimes and SEF7 descriptor/process evidence as prerequisites, not new summative exercises.
2. **Why Rust exists** — Compare manual ownership, tracing collectors and affine ownership with realistic resource costs and historical motivations.
3. **Toolchain identity** — Pin rustc, rustup target, Cargo dependency graph, lockfile and reproducible build commands.
4. **Crates and visibility** — Separate library, binary, modules and tests with meaningful public interfaces.
5. **Rust expressions and patterns** — Use structs, enums and match to model explicit state and ownership.
6. **Correctness baseline** — Specify input/output fixtures before translating a C example into Rust.

### Module 2 — Ownership, Borrowing and API Lifetimes

#### Outcomes

- SYS2-O2
- SYS2-O4
- SYS2-O9

#### Lessons

1. **Move and Copy** — Predict when data moves, is cloned or remains borrowed and who owns cleanup.
2. **Shared and exclusive loans** — Analyze valid and invalid aliasing using compiler diagnostics and memory diagrams.
3. **Owned and borrowed bytes** — Use String, Vec, slices and &str without invalid indexing or dangling views.
4. **Lifetime relationships** — Annotate returned borrowed data when required; distinguish lexical scope from actual runtime resource duration.
5. **Drop and fallible cleanup** — Account for file sync, close failures and why destructors cannot promise that a write is durable.
6. **Resource graph design** — Choose ownership boundaries for nested files, children and buffers rather than sprinkling clones.
7. **Interior mutability boundary** — Explain RefCell's runtime checks without introducing unnecessary cross-thread synchronization.

### Module 3 — Fallibility, Types and Verification

#### Outcomes

- SYS2-O1
- SYS2-O3
- SYS2-O11
- SYS2-O13

#### Lessons

1. **Option and Result** — Separate missing data, invalid input and recoverable operating-system failure.
2. **Typed state machines** — Replace magic error codes and invalid multi-boolean states with explicit variants.
3. **Checked sizes and integers** — Avoid overflow, truncation and attacker-controlled large allocations.
4. **UTF-8 and Unix paths** — Distinguish bytes, text, OsString and filesystem names that need not be valid UTF-8.
5. **Trait-bound adapters** — Use limited traits and dependency injection to test a filesystem or child-process interface.
6. **Failure context** — Preserve safe error causes without leaking arbitrary paths or child environment secrets.
7. **Property and regression tests** — Construct independent invalid/boundary fixtures and verify emitted errors.

### Module 4 — C/Rust Representation and Unsafe Boundaries

#### Outcomes

- SYS2-O2
- SYS2-O5
- SYS2-O9
- SYS2-O10
- SYS2-O14

#### Lessons

1. **Layout and alignment** — Compare C structs with repr(C) and unspecified default Rust representation.
2. **Aliasing and UB** — Explain when C object lifetime/provenance bugs become undefined behavior and why Rust compiler checks differ.
3. **Safe Rust is not authorization** — Expose algorithmic, race, protocol and resource failures outside the type system.
4. **Unsafe contracts** — Write a narrow safety invariant for raw pointers and checked FFI; no arbitrary unsafe implementation requirement.
5. **FFI and panic policy** — Consider ABI, allocation ownership, unwinding and error translation at a controlled example boundary.
6. **Diagnostics in context** — Use C sanitizers, Rust compiler errors and targeted assertions to isolate a demonstrated defect.

### Module 5 — Linux Files, Descriptors and Durability

#### Outcomes

- SYS2-O4
- SYS2-O6
- SYS2-O8
- SYS2-O11
- SYS2-O14

#### Lessons

1. **Owned FDs** — Explain ownership transfer, descriptor duplication, close-on-exec and borrowed raw handles.
2. **Path identity** — Handle relative fixtures, directory handles, permissions and symlink limitations without asserting a naïve prefix check is safe.
3. **Buffered and unbuffered I/O** — Relate std::io operations to partial writes, interruptions and OS return behavior.
4. **File completion versus persistence** — Distinguish successful write, flush, file sync and parent-directory sync.
5. **IPC envelopes** — Define bounded pipe/socketpair messages and failure responses for owned processes.
6. **Linux observation limits** — Read /proc or optional syscall traces without assuming availability in every sandbox.

### Module 6 — Process Supervision and Lifecycle

#### Outcomes

- SYS2-O3
- SYS2-O6
- SYS2-O7
- SYS2-O8
- SYS2-O12

#### Lessons

1. **Spawn and exec failures** — Discriminate spawn failure from a successfully launched child that exits with a nonzero status.
2. **Owned child identity** — Track and reap only children launched by the utility, avoiding stale PID assumptions.
3. **Signal and cancellation policy** — Use application-level notification and monotonic deadlines rather than work in unsafe signal handlers.
4. **Pipe deadlocks** — Bound stdin/stdout/stderr handling, especially when a child writes more than pipe capacity.
5. **Partial failure matrix** — Inject broken pipes, early termination, slow children and invalid executables.
6. **Escalation and cleanup** — Design TERM/wait/KILL or controlled equivalent with explicit uncertainty and idempotent cleanup.
7. **Independent supervision review** — Check that no child remains, no descriptor leaks and all result states are classifiable.

### Module 7 — Comparative Engineering and Trust

#### Outcomes

- SYS2-O5
- SYS2-O9
- SYS2-O10
- SYS2-O11
- SYS2-O13
- SYS2-O14

#### Lessons

1. **Shared behavior contract** — Use the same fixture oracle for equivalent C and Rust operations before comparing quality or speed.
2. **Controlled C defect** — Isolate a realistic bounds, lifetime or cleanup flaw with safe synthetic test inputs.
3. **Rust counterpart** — Explain compile-time protection where it applies and test remaining unchecked errors.
4. **Command and path authority** — Avoid shell interpolation, untrusted executable selection, unsafe environment forwarding and uncontrolled writes.
5. **Portability declaration** — State OS, libc, Rust target and compiler-dependent assumptions.
6. **Unfamiliar failure challenge** — Reproduce an unseen ownership or lifecycle defect and prove a targeted repair.

### Module 8 — Integrated Rust Unix Utility

#### Outcomes

- SYS2-O1
- SYS2-O3
- SYS2-O4
- SYS2-O7
- SYS2-O8
- SYS2-O11
- SYS2-O12
- SYS2-O13

#### Lessons

1. **Utility requirements** — Select a bounded process-supervisor, fixture indexer or local streaming converter and define acceptance behavior.
2. **Module contracts** — Separate CLI validation, core transformations, OS adapter, diagnostics and lifecycle.
3. **Resource ownership map** — Document cleanup responsibilities on success, partial progress and cancellation.
4. **Failure harness** — Exercise large input, malformed framing, inaccessible fixture, child exit and interrupted transfer.
5. **Rebuild from scratch** — Reproduce on a declared nonprivileged Linux environment without paid services or hidden files.
6. **Technical defense** — Make an independent change, re-run representative tests and explain residual risk.

## Completion requirements

Only the assessments below are summative; module examples and feedback exercises are not extra completion gates. A cumulative source artifact may serve several nonduplicative evaluations when their criteria are separately assessed.

- **SYS2-AS1** — Rust API and Ownership Demonstration
  - **Outcomes:** SYS2-O1, SYS2-O2, SYS2-O3, SYS2-O4.
  - **Work:** Build a library with ownership-aware container and fallible I/O interfaces; justify compile-rejected borrowing scenarios.
  - **Criteria:** Defined valid results and negative cases pass; types/Drop ownership and cleanup are explained; no unjustified unsafe.
  - **Evidence:** Source, Cargo lockfile, tests, compile diagnostics, ownership trace and reproducible commands.

- **SYS2-AS2** — C/Rust Safety Comparison
  - **Outcomes:** SYS2-O2, SYS2-O5, SYS2-O9, SYS2-O10, SYS2-O14.
  - **Work:** Implement one equivalent bounded operation in C and Rust, reproduce a controlled C defect and explain safety boundaries.
  - **Criteria:** Oracle behavior is matched before comparison; compiler/sanitizer evidence is interpreted accurately; logic and OS bugs are not claimed impossible.
  - **Evidence:** C and Rust source, fixtures, sanitizer output, safety invariant and comparative reasoning.

- **SYS2-AS3** — Failure-Aware Unix Supervision
  - **Outcomes:** SYS2-O3, SYS2-O6, SYS2-O7, SYS2-O8, SYS2-O11.
  - **Work:** Implement supervision of multiple owned synthetic child processes and a bounded IPC protocol.
  - **Criteria:** No descriptor/child leaks after normal and injected failure paths; timeout and shutdown semantics are explicit; non-UTF-8/error cases treated correctly.
  - **Evidence:** State graph, test runner, child/failure traces, clean build and OS assumptions.

- **SYS2-AS4** — Complete Rust Systems Utility
  - **Outcomes:** SYS2-O1, SYS2-O3, SYS2-O4, SYS2-O6, SYS2-O7, SYS2-O8, SYS2-O11, SYS2-O12.
  - **Work:** Release a multi-module utility consuming safe fixture resources with documented operational behavior.
  - **Criteria:** Reproduces from clean state and validates normal, malformed, resource-limit, interrupted and recovery paths; no privilege or proprietary service.
  - **Evidence:** Source, CLI spec, fixtures, expected results, tests, runbook and limitations.

- **SYS2-AS5** — Independent Resource Failure Defense
  - **Outcomes:** SYS2-O2, SYS2-O5, SYS2-O9, SYS2-O10, SYS2-O12, SYS2-O13, SYS2-O14.
  - **Work:** Investigate an unfamiliar Rust or mixed-language ownership/ABI/resource problem and implement a bounded repair.
  - **Criteria:** Explain root cause, show reproducer and regression, distinguish guarantee levels and defend affected resource ownership.
  - **Evidence:** Before/after evidence, patch, explanation, tests and review record.

### Curriculum and safety boundaries

SEF7-O1–O14 and SEF7-AS1–AS7 remain authoritative in SEF7, with no assessment transfer or retroactive equivalence. SYS2 advances to multi-child supervision, Rust ownership and C/Rust analysis; SYS3 owns atomics/concurrent correctness, SYS4 scalable networking, and SYS5 storage internals. APP15's independent Rust-readiness exercise is not a prerequisite or substitute for this course. Demonstrations must use synthetic owned processes and safe temporary directories. Explain limitations of the kernel, libraries, compiler and language separately.

### Evidence and reproducibility

Required source and executable tests must reproduce from a clean checkout with documented toolchain, dependency locks, commands, environment requirements, known-correct synthetic oracles, boundary/fault tests and relevant limitations. Capture actual failures and corrections rather than claiming safety from a green compiler alone. Assessment decisions identify course revision, outcome and assessment IDs, evidence, reviewer decision and material assumptions. Legacy work is not silently treated as passing the new requirements. Educational readiness remains `draft` until actual learner evidence supports promotion.

## Optional disciplinary references

- [The Rust Programming Language — Understanding Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html) and [Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html): public language references for ownership, borrowing and fallible APIs.
- [Linux man-pages project](https://man7.org/linux/man-pages/): verify the exact interface contracts and portability limits of the Linux/POSIX operations actually used.

These are public research references, not paid readings, mandatory provider accounts or substitutes for published course assessments.
