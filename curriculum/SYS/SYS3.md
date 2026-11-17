# SYS3 — Concurrency, Atomics & Memory Models

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS10](SYS10.md) (including its SYS1/SYS2 foundations)
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

Engineer correct shared-state and message-passing programs under nondeterministic schedules. SYS2 establishes Rust ownership and safe OS resource handling, and SYS10 establishes scheduling, memory and kernel execution context; this course develops synchronization invariants, memory-order reasoning, progress and performance. The primary reference environment is stable Rust on nonprivileged Linux, but scheduling and hardware performance vary. Dynamic race checkers and NUMA tools are optional; deterministic history traces and portable fixtures must suffice where specialized tooling is unavailable. Rust safe code prevents certain memory violations, but does not automatically prevent deadlock, starvation, duplicated effects or incorrect atomic publication.

## Learning outcomes

- **SYS3-O1:** Specify safety, liveness and progress properties for a concurrent component and distinguish data races from higher-level logical races.
- **SYS3-O2:** Explain OS threads, scheduling, preemption, blocking and CPU parallelism without assuming deterministic interleavings.
- **SYS3-O3:** Design mutex, reader-writer, condition-variable and semaphore protocols with documented invariants and cleanup.
- **SYS3-O4:** Diagnose deadlock, starvation, livelock, priority inversion and cancellation hazards using wait-for and interleaving traces.
- **SYS3-O5:** Explain Rust Send/Sync, shared ownership and synchronization without mistaking safe compilation for deadlock freedom.
- **SYS3-O6:** Use atomic operations and happens-before reasoning to justify selected ordering, visibility and linearization points.
- **SYS3-O7:** Distinguish sequential consistency, release/acquire, relaxed order and invalid concurrent access through small litmus tests.
- **SYS3-O8:** Design and verify bounded message passing, wakeup and cancellation without lost notifications or unbounded queues.
- **SYS3-O9:** Implement a concurrent queue, worker pool or related component with documented correctness, backpressure and shutdown semantics.
- **SYS3-O10:** Measure contention, false sharing, locality and scheduling effects with representative workload controls.
- **SYS3-O11:** Construct deterministic and adversarial interleaving tests, including timeouts and failure cases, without claiming exhaustive proof.
- **SYS3-O12:** Defend an unfamiliar concurrency failure with a causal explanation, constrained fix and regression evidence.

## Modules

### Module 1 — Concurrency Contracts and Thread Execution

#### Outcomes

- SYS3-O1
- SYS3-O2
- SYS3-O5

#### Lessons

1. **Concurrency versus parallelism** — Distinguish interleaving from simultaneous work on multiple CPU cores.
2. **Thread states and OS scheduling** — Trace runnable, sleeping, blocked and preempted states against resource use.
3. **Atomicity and invariants** — Define a shared-state invariant and distinguish data-race freedom from application correctness.
4. **Rust thread interfaces** — Use scoped or owned threads and reason about captured values and safe join behavior.
5. **Thread failure and panic** — Describe propagation, poisoned locks, ownership cleanup and limits of restart promises.
6. **State-space reasoning** — Enumerate counterexample schedules for a tiny account or handoff protocol.

### Module 2 — Locks, Waiting and Progress

#### Outcomes

- SYS3-O3
- SYS3-O4
- SYS3-O5

#### Lessons

1. **Mutex protocols** — Bind lock scope to the exact invariant and avoid accidental hold across blocking work.
2. **Condition variables** — Implement predicate loops and explain spurious wakeups and lost notifications.
3. **Reader-writer locks** — Choose fair or unfair access knowingly and test starvation under a defined policy.
4. **Semaphores and limits** — Bound concurrency and prove permit ownership on panic, timeout and cancellation paths.
5. **Deadlock graphs** — Construct a wait-for graph and demonstrate lock-order repair.
6. **Priority inversion** — Discuss scheduling interference and mitigation without claiming universal scheduler support.
7. **Structured concurrency limits** — Ensure all spawned work has explicit ownership, termination and join obligations.

### Module 3 — Atomics and Memory Ordering

#### Outcomes

- SYS3-O5
- SYS3-O6
- SYS3-O7

#### Lessons

1. **Atomic operations** — Use load/store/swap/fetch/CAS with clearly documented state transitions.
2. **Happens-before** — Derive synchronization edges and distinguish compiler reordering from hardware observation.
3. **Relaxed operations** — Justify counters that do not publish associated data and identify misuse cases.
4. **Release/acquire handoff** — Explain visibility after publication and consumption using a trace of two threads.
5. **Sequential consistency** — Contrast stronger ordering with weaker valid protocols and their costs.
6. **CAS retry and ABA** — Recognize spurious failure, ABA and linearization hazards in naive lock-free structures.
7. **Rust/C memory boundaries** — State why non-atomic conflicting access can be undefined behavior, not merely stale output.
8. **Litmus-test limitations** — Use repeatable tests and reasoning; absence of a forbidden outcome does not prove correctness.

### Module 4 — Messages, Queues and Work Ownership

#### Outcomes

- SYS3-O1
- SYS3-O3
- SYS3-O8
- SYS3-O9

#### Lessons

1. **Message passing versus shared state** — Choose a channel when explicit work ownership simplifies safety.
2. **Bounded channel semantics** — Define send/receive, close, block, timeout and cancellation behavior.
3. **Queue invariants** — Specify FIFO/order expectations, capacity and concurrent producers/consumers.
4. **Worker pool lifecycle** — Handle startup, admission, work completion, panic and clean termination.
5. **Backpressure and fairness** — Test producers under slow workers and ensure bounded resource use.
6. **Async and OS threads** — Compare tasks, threads and blocking without requiring an async framework or reenacting APP runtime lessons.
7. **Negative handoff cases** — Inject queue closure, cancellation during wait and partial completion.

### Module 5 — Hardware and Scheduling Costs

#### Outcomes

- SYS3-O2
- SYS3-O6
- SYS3-O10

#### Lessons

1. **Cache coherence** — Explain coherence invalidation and the distinction from a language memory model.
2. **False sharing** — Construct adjacent/padded counter cases with identical work and verify outputs.
3. **NUMA awareness** — Explain placement and remote access effects; use optional emulation when hardware is unavailable.
4. **Contention curves** — Vary thread count, critical-section work and workload size with controlled measurement.
5. **Queueing and oversubscription** — Distinguish service time, wait time and CPU saturation.
6. **Measurement caution** — Record thermal, scheduler and allocator confounders and avoid overclaiming microbenchmarks.

### Module 6 — Concurrent Verification and Fault Reproduction

#### Outcomes

- SYS3-O1
- SYS3-O4
- SYS3-O7
- SYS3-O11
- SYS3-O12

#### Lessons

1. **Independent test oracles** — Define exact-once work accounting, invariants and allowed final states before building tests.
2. **Interleaving harness** — Use barriers and seeded schedules to reproduce specific race histories.
3. **Race detection limits** — Interpret compiler-assisted checks and dynamic race tools without treating passing runs as proofs.
4. **Progress checks** — Bound all waits and distinguish deadlock from slow execution.
5. **Fault injection** — Test worker crash/panic, queue closure, duplicate work and cancellation.
6. **Linearization review** — Explain whether the operation has a valid single conceptual effect point.
7. **Unfamiliar defect challenge** — Produce a minimal trace and justified fix rather than replacing synchronization at random.

### Module 7 — Integrated Concurrent Runtime Component

#### Outcomes

- SYS3-O3
- SYS3-O6
- SYS3-O8
- SYS3-O9
- SYS3-O10
- SYS3-O11
- SYS3-O12

#### Lessons

1. **Choose a realistic component** — Implement a bounded job scheduler, queue or dispatcher with explicit API invariants.
2. **Design trade-off** — Select locks or atomics for stated reason and identify unsafe assumptions.
3. **Implementation and tests** — Exercise producer/consumer counts, cancellation, overload and shutdown.
4. **Contention profiling** — Benchmark multiple workloads and distinguish latency from throughput.
5. **Review and defense** — Resolve an unfamiliar schedule or invariant failure and discuss unproved cases.

## Completion requirements

The following assessments, not routine lesson practice, establish completion. Reuse one correct component across performance and failure evaluations where the different outcomes remain independently decidable.

- **SYS3-AS1** — Concurrency Model and Failure Analysis
  - **Outcomes:** SYS3-O1, SYS3-O2, SYS3-O3, SYS3-O4, SYS3-O5.
  - **Work:** Model at least two plausible schedules for shared-state access and repair a deliberately flawed synchronization protocol.
  - **Criteria:** Safety/liveness claims are explicit; lock-order/wakeup arguments are correct; a failure can be reproduced or logically demonstrated.
  - **Evidence:** State diagrams, traces, corrected pseudocode/code, adversarial test fixtures.

- **SYS3-AS2** — Memory-Ordering Reasoning
  - **Outcomes:** SYS3-O5, SYS3-O6, SYS3-O7.
  - **Work:** Implement or analyze bounded atomic handoffs and distinguish relaxed, release/acquire and seq-cst behavior under specified invariants.
  - **Criteria:** Happens-before and linearization claims supported with explicit ordering; non-atomic data races rejected; no claim based only on a test run.
  - **Evidence:** Annotated Rust atomic code, litmus histories, ordering justification and counterexamples.

- **SYS3-AS3** — Bounded Concurrent Component
  - **Outcomes:** SYS3-O3, SYS3-O8, SYS3-O9, SYS3-O11.
  - **Work:** Build a worker pool, queue or dispatcher with cancellation, backpressure and safe shutdown under stress.
  - **Criteria:** Capacity remains bounded; no work silently lost/duplicated beyond declared policy; termination completes within tested deadline; invariants survive invalid inputs.
  - **Evidence:** Source, state machine, independent oracle, stress/failure tests, clean-run commands.

- **SYS3-AS4** — Contention and Locality Experiment
  - **Outcomes:** SYS3-O2, SYS3-O4, SYS3-O10.
  - **Work:** Compare sync approaches and false-sharing or scheduling effects over variable thread counts.
  - **Criteria:** Correctness precedes timing; repeat samples; provide slowdown/speedup causes and uncertainty; do not require dedicated NUMA hardware.
  - **Evidence:** Workload scripts, measurements, environment, plots/table and cautions.

- **SYS3-AS5** — Unknown Interleaving Defense
  - **Outcomes:** SYS3-O1, SYS3-O4, SYS3-O6, SYS3-O9, SYS3-O11, SYS3-O12.
  - **Work:** Diagnose a newly supplied race, starvation, deadlock or failed-shutdown scenario and repair it.
  - **Criteria:** Root cause and violated invariant are defensible; corrected program has regression test; residual limitations identified.
  - **Evidence:** Minimal failing schedule, patch, tests and oral/written defense.

### Academic and verification boundaries

SEF covers basic program state, SYS2 introduces ownership and SYS10 explains OS scheduling and kernel mechanisms; this course owns concurrent progress, memory ordering, synchronization and measurable contention. SYS4 adds network-service backpressure rather than re-teaching lock invariants; SYS5 applies already learned concurrency to durable storage. Unsafe lock-free implementations are not mandatory; reasoning about unsafe/weak-memory design failures is. Correctness claims require explicit invariants, model/trace analysis and adversarial tests, not only stress-run success. Use local synthetic work and bounded thread counts, avoiding accidental machine overload.

### Evidence and reproducibility

Document toolchain, build flags, CPU/OS and input seeds or schedule control where relevant. Required executable evidence must rebuild cleanly, contain independently justified behavioral oracles, include boundary and failure tests, and disclose nondeterministic limitations. Each summative decision references course revision, outcomes, assessment IDs and inspectable evidence. No paid hardware or profiler is mandatory. Historical legacy completion records retain their original contract. The course remains `draft` pending learner and independent-review evidence.

## Optional disciplinary references

- [Rust atomic memory ordering reference](https://doc.rust-lang.org/std/sync/atomic/enum.Ordering.html): language-level Acquire, Release, Relaxed and SeqCst contracts and limitations.
- [CS2023 Parallel and Distributed Computing knowledge area](https://csed.acm.org/knowledge-areas/): disciplinary coverage context, not a mandated course packaging or proof of OEE conformance.

These references support independent investigation; the published outcomes and assessment criteria remain authoritative.
