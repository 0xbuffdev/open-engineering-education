## SYS6 — Distributed Systems

**Duration:** 7 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SYS4 and SYS5

### Overview

Study RPC, replication, fault models, consistency, leader-based coordination, durable logs, recovery, and consensus through staged implementation and fault-injection exercises.

### Prerequisites

**SYS4 — Linux Networking & Services**
**SYS5 — Storage Engines & Data Systems**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Explain why distributed systems fail in ways single-process systems do not.
- Design RPC protocols with explicit timeout, retry, and failure behavior.
- Implement and reason about replication and durable coordination mechanisms.
- Use fault injection to investigate partitions, dropped replies, duplication, and restarts.
- State the guarantees a distributed service provides and the assumptions behind them.


### Resource map

**Required**

- **B25** Ch. 1–2 and 5–10 · **B4** Ch. 47–49 · **B5** Ch. 43–44 and 56, 59–61 (selective) — carried from ZtP S11.
- **R38** MIT 6.5840 lectures and labs · **R39** the Raft paper.

### Modules

#### Module 1 — RPC & Failure Models

**Reading:** **B4** Ch. 47 (Distributed Systems: communication layers, RPC). **B25** Ch. 9 (The Trouble with Distributed Systems). **R38** the introductory RPC and threads lectures.


### Module outcomes

By the end of this module, the learner can:

- Explain **Remote procedure calls** in the context of the course.
- Apply **Failure models and timeouts** in a problem, implementation, experiment, or design decision.

1. **Remote procedure calls**
   - kind: `lesson`
2. **Failure models and timeouts**
   - kind: `lesson`
3. **Checkpoint: distributed failure reasoning**
   - kind: `test`

4. **Micro-lab: Inject dropped requests and distinguish timeout from successful completion.**
   - kind: `lab`
#### Module 2 — Replication & Consistency

**Reading:** **B25** Ch. 6 (Replication), Ch. 10 (Consistency and Consensus). **B4** Ch. 48 (Sun's Network File System), Ch. 49 (The Andrew File System).


### Module outcomes

By the end of this module, the learner can:

- Explain **Replication models and consistency** in the context of the course.
- Apply **Leader/follower behavior and replicated logs** in a problem, implementation, experiment, or design decision.

1. **Replication models and consistency**
   - kind: `lesson`
2. **Leader/follower behavior and replicated logs**
   - kind: `lesson`
3. **Checkpoint: consistency concepts**
   - kind: `test`

4. **Micro-lab: Trace a write through replicas and identify possible divergence.**
   - kind: `lab`
#### Module 3 — Retries & Idempotency

**Reading:** **B4** Ch. 47 (RPC semantics — at-least-once and at-most-once). **B25** Ch. 9. **R17** Idempotent requests and **R10** AIP-155 as practical idempotency patterns.


### Module outcomes

By the end of this module, the learner can:

- Explain **Retries and duplicate requests** in the context of the course.
- Apply **Idempotent service operations** in a problem, implementation, experiment, or design decision.

1. **Retries and duplicate requests**
   - kind: `lesson`
2. **Idempotent service operations**
   - kind: `lesson`
3. **Checkpoint: retry semantics**
   - kind: `test`

4. **Micro-lab: Make a retried client request safe against duplicate application.**
   - kind: `lab`
#### Module 4 — Partitions & Consensus

**Reading:** **B25** Ch. 9–10. **R39** the Raft paper. **R38** the Raft lectures and lab.


### Module outcomes

By the end of this module, the learner can:

- Explain **Partitions and leader election** in the context of the course.
- Apply **Consensus fundamentals and fault injection** in a problem, implementation, experiment, or design decision.

1. **Partitions and leader election**
   - kind: `lesson`
2. **Consensus fundamentals and fault injection**
   - kind: `lesson`
3. **Checkpoint: consensus reasoning**
   - kind: `test`

4. **Micro-lab: Run a controlled failure scenario and explain the resulting client guarantee.**
   - kind: `lab`
#### Module 5 — Replicated Key-Value Service

**Reading:** **R38** the Raft and fault-tolerant key/value service labs. **B25** Ch. 7 (Sharding) and Ch. 8 (Transactions) for context.


1. **Build and fault-inject the Replicated Key-Value Service**
   - kind: `lab`

### Topics

- RPC
- replication
- consistency
- failure models
- leader election
- logs
- retries
- idempotency
- partitions
- consensus fundamentals
- fault injection

### Labs

- RPC service
- duplicate-request experiment
- leader/replica simulation
- dropped-message experiment
- restart/recovery experiment

### Substantial course lab

**Replicated Key-Value Service**

Build a small replicated service and test it under controlled failures.

---

