# SYS6 — Distributed Systems

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS4](SYS4.md), [SYS5](SYS5.md)
**Duration:** 18–24 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

Build on SYS4's reliable per-connection behavior and SYS5's crash-durable local storage to explain and implement **failure-aware replicated state**. A distributed call can fail after taking effect; no isolated client timeout proves whether it completed. Learn histories, consistency, replication, majority quorums, terms, leader election, replicated logs, deterministic fault injection and recovery. Use a scoped **Raft-like fixed-membership** leader-based service with published model and omissions; implementing full production Raft, Byzantine consensus, reconfiguration or multi-region deployment is not required. Local processes with controllable message delivery and separate fixture directories provide free, reproducible experiments, but do not simulate independent physical machines or power domains.

## Learning outcomes

- **SYS6-O1:** Model asynchronous message delays, omission, duplication, process crash and network partitions and explain indistinguishable observations.
- **SYS6-O2:** Specify RPC identity, deadline, retry, deduplication and uncertain outcomes without promising exactly-once execution.
- **SYS6-O3:** Distinguish consistency, availability, durability and safety/liveness claims under explicit failure assumptions.
- **SYS6-O4:** Analyze linearizability, sequential consistency and eventual consistency through client histories and counterexamples.
- **SYS6-O5:** Explain quorum intersection, replication factor and acknowledgment policies with concrete failure budgets.
- **SYS6-O6:** Design leader epochs/terms, fencing and durable replicated-log constraints that prevent stale-leader acceptance.
- **SYS6-O7:** Derive the essential election, log-matching, commitment and state-machine safety properties of a leader-based consensus protocol.
- **SYS6-O8:** Implement a bounded replicated log or state-machine service with crash-recoverable term/log state and controlled deterministic scheduling.
- **SYS6-O9:** Specify read semantics, membership and configuration limitations, and distinguish stale, leader and quorum-based reads.
- **SYS6-O10:** Reason about snapshot, compaction and state transfer while preserving applied/committed boundaries.
- **SYS6-O11:** Design fault-injection tests for partition, delay, duplication, crash/restart, leader change and quorum loss.
- **SYS6-O12:** Use independent history checking or a reference state machine to evaluate claimed safety under generated schedules.
- **SYS6-O13:** Measure the latency/availability cost of replication under controlled local workloads and disclose extrapolation limits.
- **SYS6-O14:** Build and operate a small replicated key-value service or equivalent coordination component with honest guarantee documentation.
- **SYS6-O15:** Defend an unfamiliar distributed failure by identifying an invalid history, deriving root cause and testing a correction.

## Modules

### Module 1 — Distributed Failure and the Network

#### Outcomes

- SYS6-O1
- SYS6-O2
- SYS6-O3

#### Lessons

1. **From one machine to many** — Separate shared-memory and local filesystem guarantees from remote messages and independent clocks.
2. **Failure observations** — Explain why a timeout cannot distinguish a failed server, delayed packet or lost response.
3. **Latency and clock limits** — Discuss monotonic local timers, clock skew and why wall-clock timestamps cannot substitute for consensus.
4. **Failure models** — Define crash-stop, crash-recovery, network omission, duplication and Byzantine exclusion.
5. **Partition scenarios** — Map reachable and unreachable components and which requests can honestly finish.
6. **Safety and liveness vocabulary** — Give counterexample histories where progress stops but safety persists, and vice versa.

### Module 2 — RPC, Retries and Operation Identity

#### Outcomes

- SYS6-O2
- SYS6-O3
- SYS6-O14

#### Lessons

1. **RPC envelopes** — Define version, request ID, client identity, bounded payload and response state.
2. **Duplicate work** — Trace retries where the server commits but the reply disappears.
3. **Idempotent application** — Contrast mathematically idempotent operations with deduplicated non-idempotent commands.
4. **At-most and at-least once** — Explain trade-offs and why exact-once effect requires additional state and assumptions.
5. **Deadline budgets** — Separate client timeout, server work budget and retry backoff under overload.
6. **Deterministic network harness** — Implement a local fault proxy/scheduler with controlled delay, drop, reorder and duplicate events.
7. **Failure reporting** — Make unknown completion explicit instead of fabricating success or rollback.

### Module 3 — Consistency Models and Histories

#### Outcomes

- SYS6-O3
- SYS6-O4
- SYS6-O5
- SYS6-O9
- SYS6-O12

#### Lessons

1. **Histories and operations** — Write invocation/response histories that record real-time precedence.
2. **Linearizability** — Judge whether a read/write history admits legal atomic points respecting order.
3. **Sequential consistency** — Compare with linearizability and produce a concrete separating example.
4. **Eventual consistency** — Define convergence assumptions and why it does not imply immediate read-after-write.
5. **Quorum arithmetic** — Calculate majority overlap under odd/even replica counts and named failure cases.
6. **Read semantics** — Distinguish stale, leader-local, lease and read-index/quorum approaches with their proof obligations.
7. **Availability under partition** — State exactly which responses can continue without compromising selected guarantees.

### Module 4 — Leader Coordination and Replicated Logs

#### Outcomes

- SYS6-O5
- SYS6-O6
- SYS6-O7
- SYS6-O8

#### Lessons

1. **Terms and leader identity** — Track election rounds and reject stale leadership state.
2. **Election safety** — State conditions for granting a vote with an up-to-date durable log.
3. **Append and log matching** — Explain preceding-index/term checks and how conflicting suffixes are resolved.
4. **Commit conditions** — Distinguish replicated entry from committed entry and apply current-term constraints.
5. **Fencing and stale writers** — Protect downstream effects using term/epoch or an equivalent authority guard.
6. **Deterministic state machine** — Apply only committed commands in order with deduplication for retried client operations.
7. **Counterexample exercise** — Trace a naive replication algorithm that loses an acknowledged write on leader change.

### Module 5 — Persistent Consensus State and Recovery

#### Outcomes

- SYS6-O6
- SYS6-O7
- SYS6-O8
- SYS6-O10

#### Lessons

1. **Term/vote persistence** — Write and recover durable election state before behavior that depends on it.
2. **Log record durability** — Reuse SYS5 WAL guarantees and explain a crash between append, sync and acknowledgement.
3. **Restart transitions** — Recover last committed/applied state without assuming a restarted replica knows the current leader.
4. **Snapshot boundaries** — Specify included index and term and verify replay and install semantics.
5. **Compaction safety** — Prevent removal of entries needed by lagging followers or recovery invariants.
6. **Storage-full and corruption** — Define safe refusal behavior rather than violating durable consensus promises.
7. **Recovery trace** — Demonstrate interruption during write, replay or snapshot transfer with controlled synthetic faults.

### Module 6 — Replication Service Integration

#### Outcomes

- SYS6-O2
- SYS6-O8
- SYS6-O9
- SYS6-O14

#### Lessons

1. **Replicated API** — Design put/get/delete and request IDs with explicit consistency choice.
2. **Local replica processes** — Run three bounded instances using loopback ports and fixture directories.
3. **Leader transitions** — Add election, log append, commit, apply and client redirects or clear unavailable results.
4. **Membership scope** — Keep a fixed configured replica set; explain joint-consensus membership change as out of scope.
5. **Read pathway** — Implement a documented safe chosen read policy or explicitly refuse unsupported strong reads.
6. **Client uncertainty** — Surface unknown outcomes and allow safe retry through deduplication.

### Module 7 — Fault Injection and Safety Review

#### Outcomes

- SYS6-O1
- SYS6-O3
- SYS6-O7
- SYS6-O11
- SYS6-O12
- SYS6-O15

#### Lessons

1. **Deterministic schedule control** — Seed message ordering, delays, loss and process restarts for reproducible histories.
2. **Partition and rejoin** — Check committed-prefix and no-divergent-acknowledgment invariants across leaders.
3. **Leader election storms** — Inject repeated timeouts and demonstrate bounded but possibly unavailable progress.
4. **Reply duplication and reorder** — Ensure client-result state remains correct under repeated requests.
5. **History checker** — Validate operation histories against a simple independent sequential specification.
6. **Invariant logging** — Record terms, indices, applied state and admission without leaking arbitrary private data.
7. **Unfamiliar failure** — Find and repair a seeded safety or liveness defect without claiming exhaustive model checking.

### Module 8 — Performance, Limits and Operational Guarantees

#### Outcomes

- SYS6-O3
- SYS6-O9
- SYS6-O10
- SYS6-O13
- SYS6-O14

#### Lessons

1. **Latency decomposition** — Measure network, queue, disk sync, quorum and apply steps separately under local load.
2. **Replication throughput** — Compare replica count, batching and acknowledged durability modes without changing consistency silently.
3. **Degraded capacity** — Evaluate quorum loss, slow follower and disk-full scenarios.
4. **Read/write asymmetry** — Explain stale read performance versus stronger read proof obligations.
5. **Local-host limitation** — Disclose that three local processes do not reproduce independent datacenter failures.
6. **Recovery plan** — Document safe restart and resynchronization without destructive manual edits.

### Module 9 — Replicated System Defense

#### Outcomes

- SYS6-O4
- SYS6-O8
- SYS6-O11
- SYS6-O12
- SYS6-O14
- SYS6-O15

#### Lessons

1. **Guarantee table** — Publish what the implementation does and does not prove, including fixed membership and fault model.
2. **Independent rebuild** — Recreate three local replicas and fixture histories from a clean checkout.
3. **Correctness demonstration** — Show leader change, retry and crash recovery without acknowledged-state loss.
4. **Operational incident** — Inject an unfamiliar fault, repair code or bound the claim and defend evidence.
5. **Review of limitations** — Explain missing production concerns and avoid claiming a toy implementation is production-safe.

## Completion requirements

These summative contracts, not independent lesson attendance or the number of injected faults, determine demonstrated competence. A cumulative service may satisfy several distinct evaluations with reusable source and fixture evidence.

- **SYS6-AS1** — Distributed Failure and Consistency Histories
  - **Outcomes:** SYS6-O1, SYS6-O2, SYS6-O3, SYS6-O4, SYS6-O5.
  - **Work:** Analyze supplied RPC, partition and client histories; classify safety, liveness and consistency properties.
  - **Criteria:** Correctly identify unknown outcomes, majority constraints and a linearizability counterexample without unjustified guarantees.
  - **Evidence:** Time diagrams, operation histories, calculations, consistency argument.

- **SYS6-AS2** — Leader and Log Safety Reasoning
  - **Outcomes:** SYS6-O5, SYS6-O6, SYS6-O7, SYS6-O9.
  - **Work:** Derive election and log-matching invariants for fixed membership and expose a naive stale-leader failure.
  - **Criteria:** Correct durable term/vote/log constraints; no committed-prefix violation in analyzed trace; stated read and membership limitations.
  - **Evidence:** State transition diagrams, adversarial leader histories, invariant justification.

- **SYS6-AS3** — Durable Replicated State Machine
  - **Outcomes:** SYS6-O2, SYS6-O7, SYS6-O8, SYS6-O10, SYS6-O14.
  - **Work:** Implement a bounded multi-process log-backed replicated key-value state machine with recoverable state.
  - **Criteria:** Commands only applied in committed order; restart replay and snapshots, if implemented, respect durable boundaries; retries surface safe states.
  - **Evidence:** Source, log/term fixtures, clean startup, failure traces, API and guarantee table.

- **SYS6-AS4** — Partition and Crash Safety Suite
  - **Outcomes:** SYS6-O1, SYS6-O3, SYS6-O8, SYS6-O11, SYS6-O12.
  - **Work:** Use seeded deterministic fault injection and an independent sequential model to test node crash, restart, message loss, duplication and split/rejoin.
  - **Criteria:** No acknowledged divergence in tested histories; safety checks are meaningful independent oracles; progress assumptions and missing schedule coverage disclosed.
  - **Evidence:** Harness, seeds, histories, invariant failures/successes and checker code.

- **SYS6-AS5** — Replication Cost and Operations Analysis
  - **Outcomes:** SYS6-O3, SYS6-O9, SYS6-O10, SYS6-O13.
  - **Work:** Measure bounded service performance under steady and degraded local scenarios and document safe operational response.
  - **Criteria:** Correctness held constant; samples and variability shown; quorum loss and recovery policy honest; no extrapolation to multi-region SLA.
  - **Evidence:** Configuration, workload data, measurement method, failure runbook and assumptions.

- **SYS6-AS6** — Unknown Distributed Failure Defense
  - **Outcomes:** SYS6-O4, SYS6-O6, SYS6-O7, SYS6-O11, SYS6-O12, SYS6-O14, SYS6-O15.
  - **Work:** Investigate a new log divergence, stale leader, read anomaly or retry/commit uncertainty and implement an evidenced fix.
  - **Criteria:** Reproduce invalid history, identify violated invariant, repair without weakening safety and show regression checks.
  - **Evidence:** Challenge log, history, patch, independent oracle and technical defense.

### Safety and model boundaries

A replicated log is not a proof that a service is linearizable. Learners must explicitly state elected-leader validity, durability prerequisites, which operations can be acknowledged, read consistency and what happens on quorum loss. Fixed membership is mandatory for this course's reference design; membership changes, cross-region clocks, Byzantine attacks and production-grade observability are discussed as limitations rather than silently promised. No learner is asked to deploy public infrastructure or use actual destructive partitions. Named algorithms are educational reference models, not accreditation.

### Reproducibility and decisions

Keep source, dependency lock, local network simulator, explicit seeds, synthetic command histories, independently derived reference results, persistent fixture state and tested crash points. Record timing methodology and hardware/OS constraints for quantitative claims. Summative records identify course and specification revision, assessment and outcome IDs, decision and inspectable evidence. Past legacy work is not automatically equivalent. Status remains `draft` until required independent learner/reviewer evidence exists.

## Optional disciplinary references

- [MIT Distributed Systems](https://pdos.csail.mit.edu/6.824/): network failures, RPC, replicated state and fault-tolerant service laboratory context.
- [In Search of an Understandable Consensus Algorithm (Raft)](https://raft.github.io/raft.pdf): a primary algorithm specification for leader-based log reasoning; this course's stated reduced fixed-membership scope is not a claim of full Raft implementation.

These are openly available study references, not mandatory paid materials or claims of university equivalence.
