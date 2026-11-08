# SYS6 — Distributed Systems

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** SYS4 and SYS5 *(legacy mapping; reconcile before activation)*
**Duration:** 7 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SYS.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Study RPC, replication, fault models, consistency, leader-based coordination, durable logs, recovery, and consensus through staged implementation and fault-injection exercises.

## Learning outcomes

- Explain why distributed systems fail in ways single-process systems do not.
- Design RPC protocols with explicit timeout, retry, and failure behavior.
- Implement and reason about replication and durable coordination mechanisms.
- Use fault injection to investigate partitions, dropped replies, duplication, and restarts.
- State the guarantees a distributed service provides and the assumptions behind them.

## Modules

### Module 1 — RPC & Failure Models

#### Outcomes

By the end of this module, the learner can:

- Explain **Remote procedure calls** in the context of the course.
- Apply **Failure models and timeouts** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Remote procedure calls** — `lesson`
2. **Failure models and timeouts** — `lesson`
3. **Checkpoint: distributed failure reasoning** — `test`
4. **Micro-lab: Inject dropped requests and distinguish timeout from successful completion.** — `lab`

### Module 2 — Replication & Consistency

#### Outcomes

By the end of this module, the learner can:

- Explain **Replication models and consistency** in the context of the course.
- Apply **Leader/follower behavior and replicated logs** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Replication models and consistency** — `lesson`
2. **Leader/follower behavior and replicated logs** — `lesson`
3. **Checkpoint: consistency concepts** — `test`
4. **Micro-lab: Trace a write through replicas and identify possible divergence.** — `lab`

### Module 3 — Retries & Idempotency

#### Outcomes

By the end of this module, the learner can:

- Explain **Retries and duplicate requests** in the context of the course.
- Apply **Idempotent service operations** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Retries and duplicate requests** — `lesson`
2. **Idempotent service operations** — `lesson`
3. **Checkpoint: retry semantics** — `test`
4. **Micro-lab: Make a retried client request safe against duplicate application.** — `lab`

### Module 4 — Partitions & Consensus

#### Outcomes

By the end of this module, the learner can:

- Explain **Partitions and leader election** in the context of the course.
- Apply **Consensus fundamentals and fault injection** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Partitions and leader election** — `lesson`
2. **Consensus fundamentals and fault injection** — `lesson`
3. **Checkpoint: consensus reasoning** — `test`
4. **Micro-lab: Run a controlled failure scenario and explain the resulting client guarantee.** — `lab`

### Module 5 — Replicated Key-Value Service

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Build and fault-inject the Replicated Key-Value Service** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

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
