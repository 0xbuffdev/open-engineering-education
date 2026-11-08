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


### Resource map

**Required**

- **B4** Ch. 26–33 · **B5** Ch. 29–33 and 53 · **B6** §6.4 and §8.1 — carried from ZtP S6.
- **B30** Ch. 1–4 and 8–9 (carried) plus Ch. 5 and 7 (added: channels; the processor).
- **B3** §7.8.8 · **B6** §6.4, App. A.3, Ch. 5, §6.5, App. D · **B5** §35.4 · **R44** — carried from ZtP S7–S8.

**Optional**

- **B30** Ch. 10 (Ideas and Inspiration).

### Modules

#### Module 1 — Threads & Shared State

**Reading:** **B4** Ch. 26 (Concurrency: An Introduction), Ch. 27 (Interlude: Thread API), Ch. 28 (Locks), Ch. 32 (Common Concurrency Problems). **B5** Ch. 29 (Threads: Introduction), Ch. 30 (Threads: Thread Synchronization), Ch. 31 (Threads: Thread Safety and Per-Thread Storage). **B30** Ch. 1 (Basics of Rust Concurrency).


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

**Reading:** **B30** Ch. 2 (Atomics), Ch. 3 (Memory Ordering). **B6** §6.4 (Multi-Thread Optimizations — atomicity optimizations), §8.1 (The Problem with Atomic Operations).


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

**Reading:** **B4** Ch. 29 (Lock-based Concurrent Data Structures), Ch. 30 (Condition Variables), Ch. 31 (Semaphores). **B30** Ch. 4 (Building Our Own Spin Lock), Ch. 5 (Building Our Own Channels). **B5** Ch. 53 (POSIX Semaphores).


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

**Reading:** **B3** §7.8.8 (Multiprocessors). **B6** §6.4 (Multi-Thread Optimizations — false sharing), App. A.3 (Measure Cache Line Sharing Overhead), Ch. 5 (NUMA Support), §6.5 (NUMA Programming), App. D (libNUMA Introduction). **B30** Ch. 7 (Understanding the Processor). **B5** §35.4 (CPU Affinity). **R44** Linux NUMA documentation.


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

**Reading:** **B4** Ch. 33 (Event-based Concurrency). **B30** Ch. 8 (Operating System Primitives), Ch. 9 (Building Our Own Locks). **B5** Ch. 33 (Threads: Further Details). *Optional:* **B30** Ch. 10 (Ideas and Inspiration).


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

