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

Learn to **specify, implement, verify, measure and defend correct concurrent components** under uncertain scheduling and memory visibility. Completed SEF already supplies foundational program reasoning; [SYS2](SYS2.md) formally teaches Rust ownership and basic safe helper-thread I/O coordination; [SYS10](SYS10.md) supplies OS threads, scheduling, preemption, kernel blocking and memory contexts. SYS3 therefore owns **new, user-space concurrency competencies**: operation histories and invariants, shared-state locks and wakeup protocols, starvation/deadlock/cancellation, safe Rust thread contracts, atomic memory order and happens-before, bounded producer/consumer coordination, linearizability-style reasoning, independent schedule tests and measured contention.

The central assessed implementation is **one bounded Rust concurrent queue, worker pool or dispatcher**, with explicit admission, ownership, completion, shutdown, panic and resource semantics. One shared component may be reused across separate functional, performance and unfamiliar-diagnostic assessments; learners are not asked to build several equivalent queues. A separate compact *atomic-protocol reasoning artifact* establishes ordering knowledge even if the main component correctly uses mutexes rather than attempting an unsafe lock-free queue.

**Required environment:** Stable Rust and Cargo on an ordinary nonprivileged Linux machine with a modest CPU/thread budget, synthetic jobs and local test harness. Tests must run without root access, hardware counters, NUMA equipment, public services, unsafe code, proprietary race detection or paid resources. Bounded `std::thread`, `Arc`, `Mutex`, `Condvar`, documented atomics and a `VecDeque` can establish baseline competence; optional channels and freely available model-checking tools may deepen the evidence if their exact versions and assumptions are disclosed. Explain how `std::sync::mpsc`'s **single receiving endpoint** differs from a genuinely multi-consumer design; an unbounded channel is not a bounded worker queue just because consumers eventually drain it.

**Precision of claims:** Rust's `Send`/`Sync` and safe APIs exclude important categories of invalid shared-memory access but do not prove deadlock freedom, starvation freedom, bounded memory use or logical exactly-once processing. `Mutex` poisoning is advisory, condition-variable wakeups may be spurious, and a test not observing a weak-memory outcome is not a language-level proof that it is forbidden. A `SeqCst` flag is not automatically a transaction over unrelated state. No practical scheduler can promise a fixed completion deadline under arbitrary preemption, host overload or process termination; state progress and resource assumptions explicitly. Some lock-free analysis addresses `unsafe` invariants and ABA, **without requiring students to execute or implement unsafe lock-free reclamation**.

**Workload and progression:** Provisional **14–18 weeks** at **10–15 focused hours/week** (140–270 focused hours) covers hand traces, safe Rust synchronization, atomic reasoning, independent oracles, controlled tests, measurement, revision and technical defense. This remains an **unverified planning estimate**, not a course-completion threshold. The prior OS mechanisms of SYS10 are invoked as preparation rather than reassessed; [SYS4](SYS4.md) later applies this work to multi-client networking, [SYS5](SYS5.md) to storage concurrency and [SYS7](SYS7.md) to deeper operational profiling.

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

### Module 1 — Concurrency Semantics, Invariants and Execution Histories

#### Outcomes

- SYS3-O1
- SYS3-O2
- SYS3-O4

#### Lessons

1. **Concurrency as a semantic problem** — Take SYS10's scheduling and context-switch account as prior knowledge and distinguish overlapping operations from actual multicore execution. Give two legal interleavings for the same instruction-independent workload and predict which user-visible outcomes must agree.
2. **Histories and operation boundaries** — Define invocation, response, in-flight operation and completion in a bounded concurrent history; distinguish a concurrent implementation's permitted orderings from one sequential reference specification.
3. **Safety versus liveness** — State an invariant that must never be violated and a progress property that must eventually hold under explicit scheduling, resource and failure assumptions; give a counterexample showing why one does not imply the other.
4. **Data races and logical races** — Distinguish unsynchronized conflicting non-atomic memory access from an incorrect check-then-act transaction protected by individually sound mutex operations; identify what safe Rust forbids and what it does not prove.
5. **Atomicity and linearization intuition** — Describe an operation that should appear to take effect at one instant between call and return; locate a possible linearization point for a simple locked counter and exhibit a history that cannot be explained by the claimed contract.
6. **Schedules, events and causal order** — Produce a small event graph with program-order, lock and message handoff edges; distinguish observed wall-clock interleaving, a legal schedule and evidence of an ordering guarantee.
7. **Adversarial transfer examples** — Review lost updates, duplicate job IDs, incorrectly published state and a missing wakeup as different errors; predict the shortest schedule that violates each contract rather than relying on a flaky stress run.
8. **Assumptions and counterexample oracles** — Write the initial state, permitted transitions, work budget, scheduler assumptions and independent expected outputs for one two-thread state machine. Specify which counterexample can be hand-checked without an actual concurrent runtime.

*Optional formative feedback:* Hand-enumerate three event schedules for a two-thread reservation ledger. Check a safety invariant and identify which progress claim needs a fairness assumption.

### Module 2 — Rust Thread Ownership, Shared State and Failure

#### Outcomes

- SYS3-O2
- SYS3-O5
- SYS3-O1
- SYS3-O4

#### Lessons

1. **From SYS2 helper threads to concurrent APIs** — Revisit SYS2's one-purpose helper threads used to drain child pipes, then extend to genuinely concurrent shared-state operations. Do not repeat Rust ownership syntax or require an async runtime as hidden preparation.
2. **Thread spawn, scope and join** — Contrast scoped threads borrowing stack data with owned spawned threads that need Send+'static captures as appropriate; track join results and distinguish thread panic from an ordinary successful return.
3. **Send and Sync contracts** — Classify example types such as owned Vec, Rc, Arc, RefCell and Mutex under Send/Sync bounds without claiming that Arc<T> alone makes an unsynchronized T shareable. State what a safe type boundary prevents and what protocol correctness still requires.
4. **Arc ownership and closure capture** — Move or clone Arc handles deliberately into worker closures and explain reference-count ownership, cleanup and cycles; use a diagram to distinguish handle aliases from mutable access to the referent.
5. **Interior mutability across threads** — Compare RefCell's runtime borrow checks with Mutex-protected state; explain why unsafe sharing or unbounded global mutable state is not needed to implement the assessed component.
6. **Panic and poisoning policy** — Handle JoinHandle panics and Mutex poisoning with an explicit application decision; poisoning is advisory and recovery demands invariant review, not unconditional unwrap or treating poisoning as a soundness guarantee.
7. **Thread lifecycle and bounded resources** — Track owned thread handles through start, normal completion, cancellation and panic. Define thread count and memory budget and explain why Rust dropping a JoinHandle detaches instead of automatically canceling or joining its task.
8. **Structured termination without async dependencies** — Design a lexical or owner-managed shutdown contract in which every accepted task reaches a declared completed/canceled state and all owned workers have a terminating and joined path; distinguish this protocol from guarantees of an arbitrary scheduler.

*Optional formative feedback:* Diagnose one Send/Sync compile rejection and one legal-but-deadlocking safe Rust example; give a corrected design without hiding failure behind unchecked thread detachment.

### Module 3 — Mutex, RwLock, Condvar and Synchronization Protocols

#### Outcomes

- SYS3-O3
- SYS3-O4
- SYS3-O5
- SYS3-O1

#### Lessons

1. **Critical sections and invariant ownership** — Specify exactly which fields one Mutex protects, when the invariant must hold, and what data may be inspected only under the guard. Compare atomic update of a field with an atomic transaction involving multiple fields.
2. **Lock scope and dependency ordering** — Calculate a wait-for graph for nested locks and establish a consistent global order; identify when callbacks, formatting, blocking I/O or channel sends while holding a guard introduce hidden dependencies.
3. **Panic-safe state transitions** — Trace a worker panic inside a critical section and decide whether to recover, reject further operations or rebuild state. Separate poisoned-lock detection from actual verification of state validity.
4. **Reader-writer tradeoffs** — Contrast read-heavy snapshots and update-heavy workloads; define what a protected RwLock state exposes and avoid assuming writer fairness, recursive locking or a particular OS scheduling policy.
5. **Condition-variable predicate discipline** — Use a guarded predicate and re-check it in a loop after wait/wait_while. Explain spurious wakeups and why inspecting a predicate outside the shared Mutex can lose notifications.
6. **No lost wakeup by construction** — Hand-trace consumer checks, mutex release-and-sleep, producer state update and notify; derive how a condition variable's atomic unlock/wait behavior avoids a check-then-sleep race under the correct guarded-predicate protocol.
7. **Timeout waiting is not a contract by itself** — Use a monotonic deadline and repeated predicate checks with remaining-duration accounting. Describe how timeout return, spurious wakeups and scheduling delays can coexist without promising a hard real-time bound.
8. **Semaphores and permit accounting** — Model an explicit counting-semaphore/permit protocol or review a documented implementation, showing total permits plus in-use equals the configured limit and why cancellation/panic must return permits. A separate third-party semaphore crate is not mandatory.
9. **Choosing the primitive and negative evidence** — Defend a Mutex, RwLock, Condvar, bounded channel or atomic approach for a concrete invariant; supply a wrong-version schedule that violates safety, liveness or resource bounds.

*Optional formative feedback:* Write predicate-based pseudocode for a bounded queue's not-empty/not-full conditions and challenge a version that sends a notification without synchronized state change.

### Module 4 — Progress, Deadlock, Starvation and Cancellation

#### Outcomes

- SYS3-O1
- SYS3-O3
- SYS3-O4
- SYS3-O8

#### Lessons

1. **The four Coffman conditions** — Identify mutual exclusion, hold-and-wait, no preemption and circular wait in a supplied lock graph; distinguish sufficient diagnosis of a deadlock pattern from a claim that every stalled program has a deadlock.
2. **Deadlock, livelock and slow progress** — Use a bounded timeline to distinguish cyclic waiting, active retry without useful work, priority-induced delay and ordinary high load; define the additional observation needed when symptoms alone are ambiguous.
3. **Starvation and fairness assumptions** — Construct a reader/writer or job-admission history where one participant never progresses despite work elsewhere. Explain why a successful finite test cannot establish starvation freedom or fairness for every schedule.
4. **Priority inversion and scheduling effects** — Trace a low-priority guard holder preempted by medium-priority CPU work while high-priority work waits; discuss priority inheritance/ceiling as conditional OS mechanisms rather than universal Rust standard-library guarantees.
5. **Blocking versus lock-free versus wait-free** — Compare mutex blocking, non-blocking retry and bounded-step per-operation progress definitions; distinguish an atomic operation being lock-free on some target from a whole algorithm making lock-free progress.
6. **Cancellation points and ownership** — Define which work may be abandoned, completed or returned to the caller on shutdown; preserve owned task IDs and avoid silently discarding accepted work when a cancellation flag changes.
7. **Panic and partial completion** — Trace a worker failure after dequeue but before acknowledgement; specify an explicit at-most-once, at-least-once or exactly-once-within-scope policy, and reject promises not supported by task outcome evidence.
8. **Shutdown ordering and wake-all** — Sequence admission closure, wakeup of sleepers, in-flight resolution, final accounting and thread joining so blocked producers/consumers can terminate; include a counterexample where an otherwise correct worker waits forever after closure.
9. **Finite fault-injection boundaries** — Bound wall-clock test time and worker/thread counts; explain why a timeout is evidence of nontermination in a chosen run, not automatically a proof of deadlock in all schedules.

*Optional formative feedback:* Analyze a three-lock wait-for graph and a canceled worker-pool trace. Give a repair and predict how its safety and liveness properties differ.

### Module 5 — Atomic Operations, Happens-Before and Memory Models

#### Outcomes

- SYS3-O5
- SYS3-O6
- SYS3-O7
- SYS3-O1

#### Lessons

1. **Atomicity at the variable boundary** — Use AtomicBool or AtomicUsize load/store/swap/fetch_add with declared legal orderings; calculate a counter trace and explain why a single atomic field cannot automatically protect an unrelated multi-field invariant.
2. **Program order and synchronization edges** — Draw a two-thread event graph separating per-thread sequenced-before, synchronizes-with and derived happens-before relationships. Identify which cross-thread observation is required to establish visibility.
3. **Relaxed order and atomic counters** — Justify relaxed fetch_add for a count whose value does not publish unrelated non-atomic payload; distinguish coherent modification order of one atomic object from inter-object ordering or fairness.
4. **Release/acquire publication** — Reason about a producer writing payload under a valid ownership/access discipline, publishing a flag with Release and consumer observing the corresponding flag with Acquire. Derive the visibility edge and explain why Relaxed alone cannot justify the payload observation.
5. **Sequential consistency and total order** — Analyze a two-location store-buffering litmus test and distinguish the additional total order on SeqCst operations from stronger claims about all non-SeqCst or non-atomic operations.
6. **Read-modify-write and compare exchange** — Model compare_exchange and compare_exchange_weak loops with explicit success/failure outcomes. Identify valid success/failure order choices, why Release/AcqRel are not failure orderings, and why failed CAS does not publish new state.
7. **Acquire-release transitions and failure paths** — Check what changes when a successful RMW uses Acquire, Release or AcqRel, and how a CAS retry reads state when it fails. Justify the weakest ordering adequate for a supplied invariant rather than using SeqCst as an unexplained incantation.
8. **Atomic versus non-atomic conflicts** — Classify conflicting accesses under the Rust/C++-style memory model and explain why undefined data-race behavior is not a license to assert a predictable stale read. Use safe Rust or supplied litmus tables for required experiments.
9. **Ordering does not imply uniqueness** — Show a check-then-act case using only SeqCst loads/stores that still creates duplicate work; identify the RMW or lock-guarded transaction needed to make the business operation atomic.
10. **Linearization points for atomic protocols** — For a bounded once-flag or claim-once counter, identify the successful CAS/RMW that defines one conceptual effect and test failures/retries. Treat complex lock-free queues and memory reclamation as analysis topics, not mandatory unsafe implementations.
11. **ABA and reclamation hazards** — Trace A→B→A reuse and show why matching a pointer or version does not prove identity; distinguish the logical ABA problem from memory-reclamation safety. Do not require students to construct a raw-pointer queue without a proven reclamation design.
12. **Litmus tests, models and observation** — Derive allowed/forbidden outcomes from specified atomic orderings using documentation or a trustworthy model; run small optional repetitions, but explain why seeing no forbidden outcome on a machine cannot prove language-level correctness.

*Optional formative feedback:* Solve a release/acquire message-passing graph and an invalid CAS-failure-order example; give an allowed history, a forbidden inference and a corrected implementation using only safe atomics.

### Module 6 — Bounded Queues, Channels and Worker Ownership

#### Outcomes

- SYS3-O3
- SYS3-O8
- SYS3-O9
- SYS3-O1

#### Lessons

1. **Message passing versus shared mutation** — Specify who owns a job before enqueue, while queued, during processing and after completion; contrast explicit move-based handoff with sharing a mutable job list under a Mutex.
2. **Channel contracts and API choices** — Contrast unbounded std::sync::mpsc::channel with bounded sync_channel and its zero-capacity rendezvous. Explain that the classic mpsc Receiver is a single-consumer abstraction; cloning senders does not make the receiver a multi-consumer queue.
3. **Explicit capacity and accounting** — Define a finite queue capacity, worker count and total accepted/in-flight/completed/canceled accounting invariant; distinguish a bounded queue's occupancy cap from the whole service's resource budget.
4. **Multi-producer, multi-consumer implementation** — Implement or specify a safe Mutex<VecDeque<Job>>+Condvar worker queue, or a documented equivalent bounded MPMC abstraction with the same semantics. A single shared std mpsc receiver behind a lock is not silently represented as parallel receiving.
5. **Admission and backpressure** — Distinguish blocking, try-send rejection and timeout under full capacity. Define observable caller results and ensure queued work cannot grow through auxiliary unbounded staging buffers.
6. **Wakeup and close semantics** — Use guarded not-empty/not-full predicates and explicit admission-close state; wake blocked waiters on shutdown and define whether draining or cancellation occurs for already accepted jobs.
7. **Exactly-once within stated scope** — Assign operation IDs, derive how each accepted job is processed once *or* explicitly canceled under no-process-crash assumptions, and specify what a worker panic does to unfinished tasks. Do not imply durable/distributed exactly-once delivery.
8. **Worker pool lifecycle** — Track worker startup, panic status, bounded task execution, cancellation and join obligations, including when a blocked producer must become able to return; record failures rather than masking detached threads.
9. **Async tasks versus OS threads** — Compare cooperative async task scheduling with OS threads without requiring an executor, reactor, Tokio or APP concurrency course; explain why a blocking call inside a cooperative task could stop unrelated progress.
10. **API contracts and independent oracles** — Publish send/receive/close/error contract and a state-machine transition table before implementation. Use a reference sequential queue and independently computed accepted/completed/canceled sets as correctness oracles.

*Optional formative feedback:* Hand-run a queue-capacity-two scenario with three producers and two workers, including close during a blocked send; check all task IDs and wakeup paths.

### Module 7 — Linearizability, Interleaving Tests and Failure Reproduction

#### Outcomes

- SYS3-O1
- SYS3-O4
- SYS3-O7
- SYS3-O9
- SYS3-O11
- SYS3-O12

#### Lessons

1. **Sequential reference histories** — Define accepted/rejected admissions and queue completion under a small sequential specification; enumerate allowed output histories so a tester never uses the component's own log as its sole oracle.
2. **Linearizability of operations** — Identify an operation's invocation/response interval and choose a legal point within it; examine a history where nonoverlapping calls impose real-time order and a claimed implementation violates the reference.
3. **Histories versus timestamps** — Distinguish logical order, synchronization edges and clock observations; show why log-line ordering, OS thread ID or wall time alone is insufficient proof of a race or linearization point.
4. **Deterministic schedule construction** — Use barriers or explicit test hooks to force a known counterexample while preserving a valid locking protocol in production; explain why a barrier placed under the wrong lock may manufacture an artificial deadlock.
5. **State-space exploration** — Enumerate all interleavings of a tiny two-thread, few-step model under declared atomicity and state limits; count explored states and disclose what unsimulated transitions or scheduler behavior remain.
6. **Randomized stress with seeds** — Design repeated stress runs over differing worker counts, capacities and seeds and retain actual failing histories; describe the limits of stress coverage rather than presenting long runtimes as exhaustive proof.
7. **Fault injection and panic paths** — Trigger producer closure, consumer panic, duplicate admission, blocked waiter and timer expiry with synthetic bounded fixtures; classify expected failure states without introducing uncontrolled host processes.
8. **Race and model checker limitations** — Describe what a dynamic race detector or an optional model-checking crate can establish for the observed configuration and why memory-safe Rust can still deadlock or violate application ordering.
9. **Unseen causal diagnosis** — Reduce a previously unseen failing history to a minimal schedule, identify violated safety/liveness/order property, propose one localized fix and run independent regression plus neighboring unchanged cases.

*Optional formative feedback:* Assess a five-event history against a sequential queue specification and provide a shorter schedule exposing a lost notification or double completion.

### Module 8 — Contention, Locality and Controlled Concurrency Performance

#### Outcomes

- SYS3-O2
- SYS3-O4
- SYS3-O6
- SYS3-O10
- SYS3-O11

#### Lessons

1. **A correctness-first benchmark** — Use the same accepted task set and independent expected final state for all compared variants; never interpret a faster run that skipped work, changed output or hid panics as an optimization.
2. **Throughput, latency and scaling** — Define completed useful operations per unit time, per-task latency, queue wait, wall time and speedup with meaningful denominators; calculate sequential and parallel efficiency without assuming linear scaling.
3. **Critical section and contention cost** — Vary worker count, work duration and lock-scope size while holding data and outputs fixed. Predict lock contention, queue wait and context-switch effects, then compare with observed results.
4. **Coherence and false sharing** — Use a specified cache-line teaching model to explain coherence invalidation and how independent adjacent counters can interfere; separate C++/Rust memory-order correctness from hardware cache-coherence traffic.
5. **Padded versus adjacent state** — Compare independently mutable per-worker counters with and without documented spacing/padding, checking alignment and equal useful work. Explain why allocator, architecture and compiler decisions may hide any expected timing difference.
6. **Oversubscription and scheduler noise** — Compare one, hardware-thread-count and deliberately oversubscribed configurations using modest local thread limits; identify scheduling, thermal, frequency and background workload confounders.
7. **Optional NUMA and hardware counters** — Explain why remote memory access can change performance, but do not require NUMA equipment, root, perf permissions or exotic cores. Use safe local repeated timing and documented model reasoning when such tools are unavailable.
8. **Repetitions and warranted inference** — Record at least five individual timings per variant, a center and spread and one plausible alternative explanation; declare when effects are inconclusive rather than forcing a speedup narrative.

*Optional formative feedback:* Predict the direction of a lock-hold-time comparison, then formulate two distinct hypotheses that would explain an unexpected result without altering correctness criteria.

### Module 9 — Integrated Concurrency Component and Independent Defense

#### Outcomes

- SYS3-O1
- SYS3-O3
- SYS3-O4
- SYS3-O5
- SYS3-O6
- SYS3-O8
- SYS3-O9
- SYS3-O10
- SYS3-O11
- SYS3-O12

#### Lessons

1. **Select one authentic bounded component** — Choose a safe Rust queue, worker pool or small dispatcher with finite task admission, explicit completion/cancellation semantics and stated numbers of producer/consumer threads. It must actually involve coordinated concurrent ownership, not independent sequential tasks.
2. **Public behavior and safety invariants** — Specify the API, capacity, close/cancel outcomes, state-transition table, ownership of accepted job IDs, linearization candidates and the circumstances in which each invariant is expected to hold.
3. **Synchronization design review** — Select a documented Mutex/Condvar, bounded channel and optional atomic flag/counter arrangement justified by the necessary ordering. Explain why the code does not require unsafe lock-free memory reclamation to meet the target.
4. **Implement and integrate without duplicate submissions** — Reuse the same implementation across the formal correctness evaluation, benchmark and unfamiliar defense, preserving separate checks for different outcomes rather than requiring three independent queue projects.
5. **Normal, invalid and capacity tests** — Verify multiple producers/consumers, zero/one capacity where supported, malformed input, duplicate job IDs, full queue and close-before/drain-after cases against precomputed expected accepted/completed/canceled sets.
6. **Cancellation, panic and finite teardown** — Test blocked producers/consumers, worker panic, repeated cancel and shutdown time budget with join obligations; report a bounded fault that cannot guarantee liveness under an unfair scheduler without pretending to have proved otherwise.
7. **Performance with constrained claims** — Measure the same implementation under varying thread counts and contention patterns, documenting actual work and repeated samples; connect any tuning to a specified mechanism, not an unsupported global claim.
8. **Unfamiliar schedule and technical defense** — Respond to an unseen adversarial history or modified requirement, reproduce or logically demonstrate the failure, give a minimal invariant-preserving correction and independently check the regression in a reviewable explanation.

*Optional formative feedback:* Have a reviewer reorder two events in a published test history; predict the required outcome before running the program and distinguish the tested property from unproved progress or fairness claims.

## Completion requirements

**The following five summative evaluations are required.** Lesson exercises, optional model-checking experiments and module feedback are formative; no additional completion gates are implied. Evaluators must decide whether the published evidence actually demonstrates **each of SYS3-O1–SYS3-O12**, not merely whether a learner has passed a stress-test command. Reuse one bounded concurrent implementation and its fixtures across AS3, AS4 and AS5 where different work/criteria genuinely require distinct demonstrations.

- **SYS3-AS1** — Concurrent Safety, Synchronization and Progress Analysis
  - **Outcomes:** SYS3-O1, SYS3-O2, SYS3-O3, SYS3-O4, SYS3-O5.
  - **Work:** Define a compact shared-state API with its sequential reference behavior; analyze **at least three distinct supplied or self-derived histories** including (a) an incorrect check-then-act or lost update, (b) deadlock from cyclic lock ownership or a lost-notification wait, and (c) starvation, cancellation or panic-induced lack of progress. Provide a corrected Mutex/RwLock/Condvar/permit protocol in bounded pseudocode or safe Rust, track Send/Sync/thread ownership and state explicit scheduler/resource assumptions.
  - **Criteria:** Every history specifies initial state, named participants, operation invocation/response or lock events, violated safety/liveness property and a minimally reproducible counterexample. Mutex or condition-variable predicates and lock-release ordering preserve the stated invariant; waiting is in a guarded predicate loop, lock ordering avoids proven cycles, and poison/panic/cancel paths have an explicit invariant-recovery or refusal policy. Differentiate deadlock, starvation, livelock, mere slow scheduling and logical race from a true undefined data race; do not infer unfair-scheduler progress guarantees from finite tests.
  - **Evidence:** Sequential reference contract; event diagrams and at least three hand-verified histories; thread ownership and lock/wait-for graph; corrected code/pseudocode; relevant deterministic negative/regression cases with stated limits.

- **SYS3-AS2** — Atomic Memory-Ordering and Litmus Reasoning
  - **Outcomes:** SYS3-O5, SYS3-O6, SYS3-O7.
  - **Work:** Analyze a set of **at least four independently reasoned compact atomic scenarios**: (1) a relaxed standalone counter, (2) a release/acquire message or publication pattern with explicit ownership, (3) a SeqCst versus weaker store-buffering or equivalent litmus test, and (4) a compare_exchange or compare_exchange_weak state transition with distinct success/failure orderings and a retry path. Also show one logically incorrect all-atomic check-then-act case and an appropriate RMW or lock correction. Use documented safe Rust atomics, supplied event histories or a bounded model; implementing a raw-pointer lock-free structure is **not required**.
  - **Criteria:** Each case states operations, initial values, ordering parameters, permitted/forbidden outcomes under declared assumptions and why synchronization edges do or do not exist. Justify what Relaxed provides for one atomic, when release/acquire publication becomes visible, what SeqCst actually orders and why even SeqCst loads/stores may fail to implement a multi-field transaction. Use valid compare-exchange success/failure ordering combinations; recognize that Release/AcqRel are not legal failure orderings and that failed CAS only loads. Treat a conflicting non-atomic data race as undefined behavior rather than a predictable stale-read result; never assert that an unobserved weak outcome is impossible merely because a stress run did not show it.
  - **Evidence:** Four annotated atomic/Rust or pseudocode cases, per-event happens-before/order graphs, expected model outcomes and independent reasoning, incorrect/corrected check-then-act comparison, optional tool outputs with provenance and limits.

- **SYS3-AS3** — Bounded Multi-Producer/Consumer Runtime Component
  - **Outcomes:** SYS3-O3, SYS3-O8, SYS3-O9, SYS3-O11.
  - **Work:** Implement a **safe Rust bounded concurrent job queue, worker pool or dispatcher** with **at least two producers and two consumers/workers** under a documented finite thread/queue/task budget. Specify admission, full capacity, exact task identity, processing, close/cancel, timeout, panic and join behavior. Accept a Mutex/Condvar-based bounded MPMC queue, or an equivalent **documented** abstraction; a standard-library `std::sync::mpsc` single-consumer channel must not be mislabeled as cloned-receiver MPMC. Publish a simple sequential specification and independent normal/invalid/adversarial fixtures.
  - **Criteria:** A reviewer can identify the protected invariant, waiting predicates and wakeup paths; enforced queue capacity and any auxiliary staging remain within declared limits *during operation*. Every accepted task has a unique accounted state (queued, running, successfully completed or explicitly canceled/failed) under the published failure assumptions; no silently lost/duplicated completion is accepted. Blocked senders/receivers wake or return when admission closes; normal completion/cancellation and injected worker-panic paths are finite in bounded tests and owned workers are joined or an explicitly limited failure is reported. Verify capacity 1, full queue, concurrent producer/consumer interleavings, close while waiting, duplicate IDs, panic and work accounting against independent hand-derived expected states. No application-wide starvation/fairness or durable exactly-once claim is made without evidence.
  - **Evidence:** Complete source, stable toolchain/lockfile where applicable, public API and capacity/ownership/state-transition contract, reference oracle, deterministic barrier/schedule or fault harness, bounded stress samples and negative cases, clean reproduction commands and limitations.

- **SYS3-AS4** — Contention, Scheduling and Locality Investigation
  - **Outcomes:** SYS3-O2, SYS3-O4, SYS3-O10.
  - **Work:** Using the correct AS3 implementation or a controlled equivalent, compare at least **two distinct performance mechanisms** under fixed useful-work and input contracts: (a) varying producer/worker count or lock scope/critical-section contention; and (b) adjacent versus padded per-thread state for false-sharing/locality or a clearly justified controlled scheduling alternative. Name competing hypotheses *before* collecting observations and calculate throughput, speedup or latency metrics under declared assumptions.
  - **Criteria:** Both comparisons verify identical intended results and account for accepted/completed/canceled task work before measurement. Record relevant target/OS/CPU, Rust toolchain and flags, input/workload, thread counts, warmup and setup, and **at least five individual timed trials per variant** with units, center/spread and environmental variability. Distinguish cache-coherence and false-sharing model expectations from observations; timing alone does not prove false sharing. Explain at least one confounder or alternative mechanism per comparison and report an inconclusive result when evidence does not discriminate. Perf counters, root, NUMA, special CPUs and public services remain optional.
  - **Evidence:** Reproducible benchmark harness/commands, identical-work oracle, independent preregistered predictions, raw per-trial timing data, summary tables or plots, relevant calculations, competing-explanation analysis and a constrained performance claim.

- **SYS3-AS5** — Unfamiliar Concurrent Failure Defense
  - **Outcomes:** SYS3-O1, SYS3-O4, SYS3-O6, SYS3-O9, SYS3-O11, SYS3-O12.
  - **Work:** Investigate one **previously unseen** bounded concurrency scenario supplied by a reviewer or transparent public-generation rule: for example a lost notification, ABA-flavored logical retry error, ordering mistake, livelock, worker cancellation or incorrect full/close transition. Before changing code, state the intended invariant, two plausible causes and a discriminating event schedule; use hand reasoning and safe test hooks or a compact model to demonstrate the violation. Apply the smallest justified correction or document a bounded refusal when assumptions are insufficient, then independently test affected and unaffected histories.
  - **Criteria:** The diagnosis identifies a legal counterexample schedule or proved protocol violation, distinguishes actual observations from modeled transitions and rejects unsupported progress claims. The corrected implementation/handoff preserves previously established safety, ownership, boundedness and shutdown criteria for the tested cases; it includes a regression whose expected result is not derived from its own output. The defense recognizes residual untested schedules, unfair execution and any architecture-specific assumptions; no compulsory unsafe code or inaccessible hardware is required.
  - **Evidence:** Original unfamiliar trace/seed or task, ordered pre-observation predictions, hand-checked state/history, minimal patch or alternative, reproducible negative/positive regression evidence, causal explanation, limits and a written, recorded or live reviewable technical defense.

### Academic boundaries, safety and independence

Completed SEF and SYS2 provide prior language/object and C/Rust ownership preparation. SYS10 already teaches **kernel-side** scheduler, context switch, interrupt, lock and wakeup mechanisms; SYS3 adds **user-space concurrent algorithm contracts, atomic memory ordering, progress properties, reusable Rust synchronization and counterexample verification** without recreating SYS10's teaching-kernel assessment. [SYS4](SYS4.md) applies the ownership/progress work to multi-client service backpressure; [SYS5](SYS5.md) applies it to storage and durability; [SYS7](SYS7.md) further develops performance attribution. Calling a teaching scheduler state trace a Linux timing guarantee or an atomic instruction a complete concurrency protocol is incorrect.

Baseline assessed artifacts use safe Rust, local synthetic jobs, bounded worker counts and wall-clock safeguards against accidental overload; an ordinary laptop can perform the required reasoning and finite reproducible experiments. Optional model checking, `loom`, platform counters or alternative channel crates are tools—not compulsory hidden prerequisites. If timing or host fairness prevents a strong performance/progress conclusion, report that limitation rather than claim successful universal proof. Diagrams may be expressed as equivalent accessible event tables. Numeric limits and test seeds must be published with each executable task.

### Revision, outcome decisions and course readiness

**SYS3-O1–SYS3-O12** and **SYS3-AS1–SYS3-AS5** preserve their existing identity and substantive competencies. More explicit memory-model litmus, invariant and resource-budget requirements are **material assessment-expectation clarifications** for *this course revision*, not grounds to silently regrade historical learner completions. A decision names source revision, assessment ID, evaluated outcomes, reviewer, evidence and material limitations; independent oracles and clean-checkout reproduction are required wherever code is assessed. Neither repository CI nor an untested outline supports promotion from `draft` to `tested` or `verified`.

## Optional disciplinary references

These public sources inform engineering accuracy and individual study; they are not mandatory paid readings, hidden assessment rules or proof of accreditation.

- [Rust standard library — atomics and Ordering](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html) and [AtomicUsize](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicUsize.html) — Relaxed, release/acquire, SeqCst, RMW and compare-exchange contracts.
- [Rust standard library — Mutex](https://doc.rust-lang.org/stable/std/sync/struct.Mutex.html), [Condvar](https://doc.rust-lang.org/stable/std/sync/struct.Condvar.html) and [thread](https://doc.rust-lang.org/stable/std/thread/) — poisoning, predicate waits, join and thread ownership.
- [Rust standard library — mpsc channels](https://doc.rust-lang.org/stable/std/sync/mpsc/) — unbounded and bounded producer/single-consumer handoff, rendezvous and disconnected channels.
- [Rustonomicon — Atomics](https://doc.rust-lang.org/nomicon/atomics.html) and [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — memory-model caveats, ownership and safe Rust.
- [ACM/IEEE-CS/AAAI CS2023](https://csed.acm.org/) — broad parallel/distributed knowledge-area comparison, not a mandate to copy another program's course structure.
