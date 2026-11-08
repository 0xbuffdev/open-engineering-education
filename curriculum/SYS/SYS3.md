## SYS3 — Concurrency, Atomics & Memory Models

**Duration:** 6 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SYS2

### Overview

Study threads, locks, atomics, channels, races, deadlocks, memory ordering, cache coherence, false sharing, and introductory NUMA behavior through controlled experiments.

### Prerequisites

**SYS2 — Systems Programming with C & Rust**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Identify races, deadlocks, starvation, and unsafe shared-state assumptions.
- Choose appropriate synchronization primitives for a concurrent design.
- Explain atomic operations and the core idea of happens-before and memory ordering.
- Measure lock contention, false sharing, and other concurrency costs.
- Build and verify a concurrent component with explicit correctness reasoning.


### Modules

#### Module 1 — Threads & Shared State



### Module outcomes

By the end of this module, the learner can:

- Explain **Threads, shared memory, and races** in the context of the course.
- Apply **Locks, deadlocks, and starvation** in a problem, implementation, experiment, or design decision.

1. **Threads, shared memory, and races**
   - kind: `lesson`
2. **Locks, deadlocks, and starvation**
   - kind: `lesson`
3. **Checkpoint: concurrency hazards**
   - kind: `test`

4. **Micro-lab: Create a small race condition and make the failure reproducible.**
   - kind: `lab`
#### Module 2 — Atomics & Memory Ordering



### Module outcomes

By the end of this module, the learner can:

- Explain **Atomic operations and synchronization** in the context of the course.
- Apply **Memory ordering and happens-before** in a problem, implementation, experiment, or design decision.

1. **Atomic operations and synchronization**
   - kind: `lesson`
2. **Memory ordering and happens-before**
   - kind: `lesson`
3. **Checkpoint: atomic correctness**
   - kind: `test`

4. **Micro-lab: Justify the ordering needed for a small concurrent handoff.**
   - kind: `lab`
#### Module 3 — Channels & Concurrent Structures



### Module outcomes

By the end of this module, the learner can:

- Explain **Channels and message passing** in the context of the course.
- Apply **Concurrent data structures** in a problem, implementation, experiment, or design decision.

1. **Channels and message passing**
   - kind: `lesson`
2. **Concurrent data structures**
   - kind: `lesson`
3. **Checkpoint: design choices in concurrency**
   - kind: `test`

4. **Micro-lab: Implement a bounded queue and define its correctness properties.**
   - kind: `lab`
#### Module 4 — Contention & Hardware Effects



### Module outcomes

By the end of this module, the learner can:

- Explain **Cache coherence and false sharing** in the context of the course.
- Apply **Basic NUMA and locality considerations** in a problem, implementation, experiment, or design decision.

1. **Cache coherence and false sharing**
   - kind: `lesson`
2. **Basic NUMA and locality considerations**
   - kind: `lesson`
3. **Checkpoint: contention versus hardware effects**
   - kind: `test`

4. **Micro-lab: Compare adjacent and padded counters across thread counts.**
   - kind: `lab`
#### Module 5 — Concurrent Runtime Component



1. **Build, benchmark, and defend the Concurrent Runtime Component**
   - kind: `lab`

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

---

