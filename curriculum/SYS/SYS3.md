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

### Module 1 — Concurrent Contracts, Histories and Causal Reasoning

#### Outcomes

- SYS3-O1
- SYS3-O2
- SYS3-O4

#### Lessons

1. **Concurrency and observable contracts** — Extend SYS10 scheduler reasoning to user-space overlapping operations versus physical parallelism. Trace legal interleavings and predict which outputs a stated sequential API must preserve; do not infer ordering from wall-clock timestamps.
2. **Safety, liveness and progress assumptions** — Write an invariant and a progress claim under explicit fairness, resource and failure assumptions. Contrast a safe but stuck system with a live but incorrect one; one bounded stress test proves neither universal property.
3. **Concurrent histories and sequential reference** — Identify invocation, response, pending operations and state transitions in a small queue or counter. Derive expected outcomes independently and reject a concrete history inconsistent with the public sequential contract.
4. **Data races versus higher-level logical races** — Distinguish undefined conflicting non-atomic access from a legal Rust check-then-act, lost update or duplicate job whose individual locks are correct. Use models or safe code rather than requiring executed undefined behavior.
5. **Happens-before and linearization intuition** — Draw program-order, locking and message-transfer edges; identify a candidate effect point between call and response. Give a counterexample disproving the point instead of equating a diagnostic log order with a guarantee.
6. **Minimal counterexamples and explicit oracles** — For one bounded two-thread state machine, publish initial state, admissible transitions and an independently solved failing schedule before running a fixture; state which premises are model assumptions and not observed host events.

*Optional formative feedback:* Derive two legal and one impossible operation history, with the safety property and the fairness assumption identified.

### Module 2 — Rust Threads, Ownership and Failure Boundaries

#### Outcomes

- SYS3-O1
- SYS3-O2
- SYS3-O4
- SYS3-O5

#### Lessons

1. **Scoped, spawned and joined threads** — Contrast scoped borrowed workers with moved spawned captures requiring Send and relevant lifetime bounds. Trace join, panic and handle drop: dropping JoinHandle detaches, not automatically cancels or joins.
2. **Send, Sync, Arc and safe shared ownership** — Explain why Arc, Rc, RefCell and Mutex have different thread-sharing conditions. Trace captured owners and synchronized mutation; show why Arc alone does not turn an unsynchronized inner value into a valid shared-state protocol.
3. **Interior mutability and correct protocols** — Compare single-thread RefCell runtime checks with Mutex-protected cross-thread state. Diagnose a compiler or runtime rejection and a separate legal Rust implementation that nonetheless loses a logical update.
4. **Panic, poisoning and invariant recovery** — Trace a worker panic while owning an in-flight job or mutex guard. Treat poison as advisory; state when to reestablish invariants, mark work failed or refuse further work, and report join errors rather than blindly unwrapping.
5. **Bounded lifecycle and shutdown ownership** — Set finite thread/task limits and trace normal, canceled and panicked workers to an observable completion or failure and join. Identify an unjoined detached worker and explain why arbitrary scheduler overload prevents real-time completion promises.

*Optional formative feedback:* Contrast a Send/Sync compilation failure with a valid Rust deadlock, and show an explicit shutdown/poison response.

### Module 3 — Locks, Condition Variables and Synchronization Invariants

#### Outcomes

- SYS3-O1
- SYS3-O3
- SYS3-O4
- SYS3-O5

#### Lessons

1. **Mutex state and transaction invariants** — Specify all state fields protected by a guard and a whole-operation invariant. Counterexample: two individually locked steps still allow a duplicate claim if the transaction is split across critical sections.
2. **Lock order and hidden blocking** — Draw an AB/BA wait-for graph, impose a safe lock order or eliminate nested locks, and inspect callbacks, I/O and bounded-channel sends under guards as potential hidden waits.
3. **RwLock and semaphore-style permit accounting** — Choose a read/write or finite-permit protocol where useful. Prove permits-in-use plus available equals the configured maximum and handle panic/cancel cleanup; never assume implementation-independent writer fairness.
4. **Condvar predicates and wakeup correctness** — Use a mutex-guarded predicate loop with spurious wakeups; compare atomic unlock/wait and synchronized state change with a broken check-then-sleep history. Trace the missing wakeup and correction.
5. **Timeout waits and close notification** — Use an elapsed-time/monotonic deadline and recheck the guarded condition after every wake. Distinguish scheduler delays, legitimate timeout and closure; ensure waiting senders and receivers are notified on shutdown.
6. **Primitive choice and independent rejection cases** — Defend a Mutex, RwLock, Condvar, bounded channel or atomic state transition for one stated invariant. Construct a failing history for a wrong primitive or lock scope and identify what progress remains unproved.

*Optional formative feedback:* Hand-check a capacity-one producer/consumer predicate and a lost-wakeup or leaked-permit counterexample.

### Module 4 — Progress, Deadlock and Controlled Shutdown

#### Outcomes

- SYS3-O1
- SYS3-O3
- SYS3-O4
- SYS3-O8

#### Lessons

1. **Deadlock, livelock and stalled service** — Distinguish cyclic waiting, active retry without progress, starvation and slow load through a concrete schedule and wait-for graph; a timeout alone is not a proof that deadlock is the cause.
2. **Fairness, priority inversion and progress levels** — Trace starvation or priority inversion under stated scheduler assumptions, then contrast blocking, lock-free system progress and wait-free per-operation bounds. Priority inheritance is conditional OS policy, not a Rust Mutex promise.
3. **Cancellation and accepted-job identity** — Track admission, queue, running, completion and explicit cancellation/failure across a worker panic after dequeue. State the precise in-memory delivery assumptions; never imply durable exactly-once processing.
4. **Close, wakeup and cooperative termination** — Order admission closure, wake-all, draining or cancellation, final work accounting and joining. Derive a failing schedule where a blocked sender/receiver never notices close or an accepted job vanishes.
5. **Bounded failure tests and reasoning limits** — Use finite thread/time limits and controlled fault hooks to separate observed hang from verified cyclic dependency. Explain what a bounded model, timeout and stress run can and cannot establish.

*Optional formative feedback:* Trace a blocked producer and panicking worker through closure, ensuring every accepted job has one declared state.

### Module 5 — Atomic Memory Ordering and Protocol Reasoning

#### Outcomes

- SYS3-O1
- SYS3-O5
- SYS3-O6
- SYS3-O7

#### Lessons

1. **Atomic state, modification order and Relaxed** — Trace AtomicBool/AtomicUsize loads, stores and RMW under declared legal orderings. Explain when Relaxed safely counts an isolated quantity and why it does not publish unrelated state or make a multi-field transaction atomic.
2. **Release/acquire and happens-before** — Build a correctly owned publication example with sequenced-before and synchronizes-with edges; derive exactly when an Acquire observation of a Release write makes earlier payload changes visible.
3. **SeqCst and weak-memory litmus histories** — Independently solve a two-location store-buffering case for Relaxed versus SeqCst under a specified memory model; explain the SeqCst total order without treating it as total ordering of every non-atomic event.
4. **Compare-exchange and failure ordering** — Trace successful and failed CAS/RMW including compare_exchange_weak spurious failure and retry. Reject Release/AcqRel as failure orderings and justify valid success/failure pairs rather than defaulting blindly to SeqCst.
5. **All-atomic operations can still violate logic** — Demonstrate a safe SeqCst check-then-act that duplicates work despite atomic variables. Repair it with a justified RMW or guarded state transition and hand-check an adversarial interleaving.
6. **Linearization, ABA and reclamation boundaries** — Identify a claim-once CAS/RMW linearization point and a legal retry failure. Analyze A→B→A reuse and distinguish logical identity, memory reclamation and progress assumptions; do not require unsafe lock-free structures.
7. **Data-race UB versus legal weak outcomes** — Classify a conflicting non-atomic access as undefined behavior, not a predictable stale read. Use safe atomics, source reasoning or bounded modeled tables rather than executing undefined behavior to prove a point.
8. **Independent models and observation limits** — Prepare permitted/forbidden outcomes and synchronization graphs before observing optional model-checker or repeated hardware tests. State limited explored states and why an unobserved weak outcome is not language-level impossibility.

*Optional formative feedback:* Solve release/acquire publication and a CAS failure pair, providing one invalid ordering and the relevant visibility graph.

### Module 6 — Bounded Multi-Producer/Consumer Components

#### Outcomes

- SYS3-O1
- SYS3-O3
- SYS3-O8
- SYS3-O9

#### Lessons

1. **Task ownership and sequential specification** — Define task IDs and admitted, queued, running, finished or canceled/failed states; create a reference sequential queue and independently derived identity-accounting oracle before implementing concurrent behavior.
2. **Channel shape and finite capacity** — Compare unbounded std::sync::mpsc channel, bounded sync_channel and a true MPMC queue, including receiver topology and optional rendezvous behavior. Cloning senders does not make the mpsc receiver multi-consumer.
3. **Safe bounded MPMC implementation** — Build a safe Mutex<VecDeque<Job>> plus Condvar or documented equivalent with at least two producers and two consumers, finite queue/thread/task budgets and no unbounded auxiliary backlog.
4. **Full admission, guarded waits and close** — Define full/reject/block/timeout and close/drain/cancel public outcomes. Recheck not-empty/not-full predicates in guarded loops and wake all blocked participants on closure, preserving accepted task identity.
5. **Panic, completion and delivery limits** — Account explicitly for a worker panicking between dequeue and recorded completion, and for owned worker join. State at-most-once or scoped completion claims only under declared no-process-crash and scheduling assumptions.
6. **Independent fixtures and negative transitions** — Hand-derive expected capacity-one, simultaneous producer/consumer, duplicate ID, blocked close and panic outcomes, then compare with actual accepted/completed/canceled sets rather than testing against the program's own logs.

*Optional formative feedback:* Hand-run capacity-two with three producers and two workers, close while one is blocked and reconcile every job ID.

### Module 7 — Linearizability, Schedule Testing and Failure Reproduction

#### Outcomes

- SYS3-O1
- SYS3-O4
- SYS3-O7
- SYS3-O9
- SYS3-O11

#### Lessons

1. **Linearizability and real-time precedence** — Check invocation/response intervals against a separate sequential specification: preserve order of non-overlapping calls while choosing a legal order for overlapping ones. Identify an impossible history even when no data race occurs.
2. **Deterministic schedule hooks** — Use barriers, controlled state steps or safe hooks to produce one known bad event schedule; avoid placing a barrier beneath a guard in a way that manufactures a test-only deadlock.
3. **Bounded state-space exploration** — Enumerate interleavings of a tiny two-thread model with named atomic steps, permitted states and limits; compare a proof over those states with unexamined OS schedules and larger workloads.
4. **Seeded stress and injected failures** — Vary capacities, thread counts and seeds under a finite budget; inject producer closure, worker panic, duplicate task or lost notification and preserve minimal failure histories. Duration alone cannot demonstrate exhaustive coverage.
5. **Distinguish models, clocks and tools** — Separate logical happens-before, wall-clock logs, optional race-detector/model-checker output and independently solved oracles. Report the exact property and environment checked, not a universal deadlock-freedom result.
6. **Independent correction and regression** — Correct a known bad transition and recheck a previously failing and a previously good history against expected state derived independently, naming the remaining untested schedules.

*Optional formative feedback:* Classify a five-event queue history for linearizability and design a safe fixture that exposes its first incorrect transition.

### Module 8 — Contention, Locality and Scientific Concurrency Measurement

#### Outcomes

- SYS3-O2
- SYS3-O4
- SYS3-O6
- SYS3-O10
- SYS3-O11

#### Lessons

1. **Correct useful work and measured quantities** — Verify identical task results and counts across variants before comparing throughput, latency, queue waits, total wall time, speedup or efficiency. Reject a seemingly faster run that drops work or hides panics.
2. **Lock contention and worker scaling** — Vary worker count and lock scope while holding useful work fixed, within modest thread/CPU limits. Predict waiting and scheduler effects, identify oversubscription and compare actual measured behavior.
3. **Cache coherence and false-sharing hypotheses** — Compare independent adjacent versus padded counters under a declared cache-line model, checking actual layout and equal work. Explain why timing variation alone does not prove hardware false-sharing interference.
4. **Repetitions, environment and alternatives** — Record individual trials, center/spread, warmup and toolchain/flags/OS/CPU plus plausible background, frequency, thermal or allocator confounders. NUMA and hardware counters must remain optional.
5. **Warranted optimization conclusions** — Contrast contention, locality and scheduling explanations with a discriminating intervention; limit conclusions to observed cases and check that an optimization preserves correctness, resource bounds and shutdown.

*Optional formative feedback:* Predict lock-scope and padded-counter effects, then propose a falsifier when observations disagree.

### Module 9 — Cumulative Concurrent Component and Independent Defense

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

1. **One coherent, bounded public artifact** — Retain the same AS3 safe Rust queue/worker-pool artifact with explicit admission, task IDs, capacity, worker limits, close/cancel and failure policy. Defend its synchronization and progress assumptions rather than implementing another queue.
2. **Reuse separate correctness and measurement evidence** — Connect AS1 protocol analyses, AS2 atomic reasoning, AS3 executable behavior, AS4 measured comparisons and independent schedule tests to distinct review decisions about the one component; do not duplicate submissions.
3. **Unseen fault, rival causes and bounded correction** — Predict at least two plausible explanations and a discriminating event sequence for a reviewer-supplied new concurrency defect. Explain a minimal invariant-preserving change or justified refusal before changing the code.
4. **Independent regression and technical defense** — Re-run the unfamiliar and a previously correct case against independent expected state; disclose untested schedules and crash/fairness limits. Reproduce a clean build and defend authorship and the scope of supported conclusions.

*Optional formative feedback:* Derive an unfamiliar close/dequeue failure and defend a minimal correction without changing the previously verified public contract.

## Completion requirements

**The following five summative evaluations are required.** Lesson exercises, optional model-checking experiments and module feedback are formative; no additional completion gates are implied. Evaluators must decide whether the published evidence actually demonstrates **each of SYS3-O1–SYS3-O12**, not merely whether a learner has passed a stress-test command. Reuse one bounded concurrent implementation and its fixtures across AS3, AS4 and AS5 where different criteria require distinct demonstrations. The unfamiliar defense specifically measures SYS3-O12; prior competencies require their own successful assessments.

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
  - **Criteria:** A reviewer can identify the protected invariant, waiting predicates and wakeup paths; enforced queue capacity and any auxiliary staging remain within declared limits *during operation*. Every accepted task has a unique accounted state (queued, running, successfully completed or explicitly canceled/failed) under the published failure assumptions; no silently lost/duplicated completion is accepted. An injected **panic after dequeue and before completion** must have an explicit owned-task/failure-accounting policy and a reproducible test of that policy, rather than depending on type checking or a happy-path job count. Blocked senders/receivers wake or return when admission closes; normal completion/cancellation and injected worker-panic paths are finite in bounded tests and owned workers are joined or an explicitly limited failure is reported. Verify capacity 1, full queue, concurrent producer/consumer interleavings, close while waiting, duplicate IDs, panic and work accounting against independent hand-derived expected states. No application-wide starvation/fairness or durable exactly-once claim is made without evidence.
  - **Evidence:** Complete source, stable toolchain/lockfile where applicable, public API and capacity/ownership/state-transition contract, reference oracle, deterministic barrier/schedule or fault harness, bounded stress samples and negative cases, clean reproduction commands and limitations.

- **SYS3-AS4** — Contention, Scheduling and Locality Investigation
  - **Outcomes:** SYS3-O2, SYS3-O4, SYS3-O10.
  - **Work:** Using the correct AS3 implementation or a controlled equivalent, compare at least **two distinct performance mechanisms** under fixed useful-work and input contracts: (a) varying producer/worker count or lock scope/critical-section contention; and (b) adjacent versus padded per-thread state for false-sharing/locality or a clearly justified controlled scheduling alternative. Name competing hypotheses *before* collecting observations and calculate throughput, speedup or latency metrics under declared assumptions.
  - **Criteria:** Both comparisons verify identical intended results and account for accepted/completed/canceled task work before measurement. Record relevant target/OS/CPU, Rust toolchain and flags, input/workload, thread counts, warmup and setup, and **at least five individual timed trials per variant** with units, center/spread and environmental variability. Distinguish cache-coherence and false-sharing model expectations from observations; timing alone does not prove false sharing. Explain at least one confounder or alternative mechanism per comparison and report an inconclusive result when evidence does not discriminate. Perf counters, root, NUMA, special CPUs and public services remain optional.
  - **Evidence:** Reproducible benchmark harness/commands, identical-work oracle, independent preregistered predictions, raw per-trial timing data, summary tables or plots, relevant calculations, competing-explanation analysis and a constrained performance claim.

- **SYS3-AS5** — Unfamiliar Concurrent Failure Defense
  - **Outcomes:** SYS3-O12.
  - **Work:** Investigate **one previously unseen** bounded concurrency scenario supplied by a reviewer or transparent public-generation rule, such as lost notification, ABA-flavored retry, incorrect ordering, livelock, worker cancellation or full/close transition. Before editing, state the public invariant, two plausible causes and discriminating event history; reproduce or derive the violation with safe hooks, a hand-solved schedule or a bounded model. Apply a minimal justified correction or bounded refusal, then independently check the affected and one previously correct history. This evaluates **O12 unfamiliar causal diagnosis and defense**, not automatic re-award of every distinct outcome covered by AS1–AS4.
  - **Criteria:** A genuine unfamiliar schedule or protocol violation is reconstructed with explicit state and synchronization edges, and the learner selects evidence distinguishing the competing causes. The correction or justified refusal follows from a checkable invariant, with an independently derived failing-case oracle and a previously correct regression. The learner explains authorship, residual untested schedules, fairness and target-model limitations without universal progress claims. A single optional-kind case does **not** by itself establish O1/O4/O6/O9/O11 anew; those requirements retain separate mandatory AS1–AS4 evidence. No unsafe code or special hardware is required.
  - **Evidence:** Original unfamiliar trace/seed or task, ordered pre-observation predictions, hand-checked state/history, minimal patch or alternative, reproducible negative/positive regression evidence, causal explanation, limits and a written, recorded or live reviewable technical defense.

### Academic boundaries, safety and independence

Completed SEF and SYS2 provide prior language/object and C/Rust ownership preparation. SYS10 already teaches **kernel-side** scheduler, context switch, interrupt, lock and wakeup mechanisms; SYS3 adds **user-space concurrent algorithm contracts, atomic memory ordering, progress properties, reusable Rust synchronization and counterexample verification** without recreating SYS10's teaching-kernel assessment. [SYS4](SYS4.md) applies the ownership/progress work to multi-client service backpressure; [SYS5](SYS5.md) applies it to storage and durability; [SYS7](SYS7.md) further develops performance attribution. Calling a teaching scheduler state trace a Linux timing guarantee or an atomic instruction a complete concurrency protocol is incorrect.

Baseline assessed artifacts use safe Rust, local synthetic jobs, bounded worker counts and wall-clock safeguards against accidental overload; an ordinary laptop can perform the required reasoning and finite reproducible experiments. Optional model checking, `loom`, platform counters or alternative channel crates are tools—not compulsory hidden prerequisites. If timing or host fairness prevents a strong performance/progress conclusion, report that limitation rather than claim successful universal proof. Diagrams may be expressed as equivalent accessible event tables. Numeric limits and test seeds must be published with each executable task.

### Assessment records and readiness

A decision records the source revision, target/thread model, assessed outcomes, expected histories, observed behavior, reviewer and remaining schedule limitations. Executable work must reproduce from a clean checkout. The course remains `draft` until learner testing and qualified review support a status change.

## Optional disciplinary references

These public sources inform engineering accuracy and individual study; they are not mandatory paid readings, hidden assessment rules or proof of accreditation.

- [Rust standard library — atomics and Ordering](https://doc.rust-lang.org/stable/std/sync/atomic/enum.Ordering.html) and [AtomicUsize](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicUsize.html) — Relaxed, release/acquire, SeqCst, RMW and compare-exchange contracts.
- [Rust standard library — Mutex](https://doc.rust-lang.org/stable/std/sync/struct.Mutex.html), [Condvar](https://doc.rust-lang.org/stable/std/sync/struct.Condvar.html) and [thread](https://doc.rust-lang.org/stable/std/thread/) — poisoning, predicate waits, join and thread ownership.
- [Rust standard library — mpsc channels](https://doc.rust-lang.org/stable/std/sync/mpsc/) — unbounded and bounded producer/single-consumer handoff, rendezvous and disconnected channels.
- [Rustonomicon — Atomics](https://doc.rust-lang.org/nomicon/atomics.html) and [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — memory-model caveats, ownership and safe Rust.
- [ACM/IEEE-CS/AAAI CS2023](https://csed.acm.org/) — broad parallel/distributed knowledge-area comparison, not a mandate to copy another program's course structure.
