# SYS3 — Concurrency, Atomics & Memory Models

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** SYS2 *(legacy mapping; reconcile before activation)*
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SYS.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Study threads, locks, atomics, channels, races, deadlocks, memory ordering, cache coherence, false sharing, and introductory NUMA behavior through controlled experiments.

## Learning outcomes

- Identify races, deadlocks, starvation, and unsafe shared-state assumptions.
- Choose appropriate synchronization primitives for a concurrent design.
- Explain atomic operations and the core idea of happens-before and memory ordering.
- Measure lock contention, false sharing, and other concurrency costs.
- Build and verify a concurrent component with explicit correctness reasoning.

## Modules

### Module 1 — Threads & Shared State

#### Outcomes

By the end of this module, the learner can:

- Explain **Threads, shared memory, and races** in the context of the course.
- Apply **Locks, deadlocks, and starvation** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Threads, shared memory, and races** — `lesson`
2. **Locks, deadlocks, and starvation** — `lesson`
3. **Checkpoint: concurrency hazards** — `test`
4. **Micro-lab: Create a small race condition and make the failure reproducible.** — `lab`

### Module 2 — Atomics & Memory Ordering

#### Outcomes

By the end of this module, the learner can:

- Explain **Atomic operations and synchronization** in the context of the course.
- Apply **Memory ordering and happens-before** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Atomic operations and synchronization** — `lesson`
2. **Memory ordering and happens-before** — `lesson`
3. **Checkpoint: atomic correctness** — `test`
4. **Micro-lab: Justify the ordering needed for a small concurrent handoff.** — `lab`

### Module 3 — Channels & Concurrent Structures

#### Outcomes

By the end of this module, the learner can:

- Explain **Channels and message passing** in the context of the course.
- Apply **Concurrent data structures** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Channels and message passing** — `lesson`
2. **Concurrent data structures** — `lesson`
3. **Checkpoint: design choices in concurrency** — `test`
4. **Micro-lab: Implement a bounded queue and define its correctness properties.** — `lab`

### Module 4 — Contention & Hardware Effects

#### Outcomes

By the end of this module, the learner can:

- Explain **Cache coherence and false sharing** in the context of the course.
- Apply **Basic NUMA and locality considerations** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Cache coherence and false sharing** — `lesson`
2. **Basic NUMA and locality considerations** — `lesson`
3. **Checkpoint: contention versus hardware effects** — `test`
4. **Micro-lab: Compare adjacent and padded counters across thread counts.** — `lab`

### Module 5 — Concurrent Runtime Component

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Build, benchmark, and defend the Concurrent Runtime Component** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- threads
- locks
- atomics
- race conditions
- deadlocks
- starvation
- memory ordering
- happens-before
- channels
- concurrent data structures
- cache coherence
- false sharing
- basic NUMA concepts

### Labs

- bounded queue
- thread pool
- atomic counter benchmark
- deliberately racy program
- lock-contention experiment
- false-sharing benchmark

### Substantial course lab

**Concurrent Runtime Component**

Build a concurrent subsystem with benchmarks and a written correctness argument.
