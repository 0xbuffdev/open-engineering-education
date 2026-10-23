# S6 — Concurrency, Atomics & Memory Models

**Track:** Systems · **Prerequisite:** S1, F5 · **Core** · **Time:** 6 weeks, 90 hours · **Project:** P4 bounded queue/thread pool

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Concurrency is where systems bugs become intermittent, expensive, and dangerous. You will learn the primitives, the memory model, and the discipline required to say "this code is correct" rather than "it usually works."

## Outcomes

You can:

- explain threads vs processes, shared memory, and scheduling;
- use mutexes, condition variables, semaphores, and channels correctly;
- identify data races, deadlocks, livelocks, and priority inversion;
- use atomics and explain acquire/release/relaxed ordering;
- write a bounded queue and a thread pool with clean shutdown;
- write tests and stress harnesses that expose races;
- explain happens-before and why a race may disappear under a debugger;
- choose between locks, atomics, channels, and async I/O.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B4 *OSTEP* | Ch. **26–33** | Concurrency, threads, locks, condition variables, semaphores, bugs, events |
| B5 *TLPI* | Ch. **29–33, 53** | POSIX threads, synchronization, thread safety, cancellation, POSIX semaphores |
| B6 | §**6.4**, §**8.1** | Multi-thread optimizations, atomic-operation costs |
| *Rust Atomics and Locks* | Ch. **1–4, 8–9** | Rust threads, atomics, memory ordering, spin locks, OS primitives, locks |
| CS:APP | Ch. **12** | Concurrent programming |
| [C++ memory model / Rust `Ordering` docs](https://doc.rust-lang.org/std/sync/atomic/enum.Ordering.html) | Reference | Memory-ordering semantics |

## Modules

### 1. Foundations

- concurrency vs parallelism;
- threads, processes, address spaces;
- context switching and scheduling;
- shared mutable state;
- critical sections;
- races and atomicity;
- happens-before.

### 2. Synchronization primitives

- mutex: lock/unlock, contention, fairness;
- condition variables: wait/signal, predicate loop, lost wakeups;
- semaphores: counting, binary;
- barriers;
- readers–writer locks;
- spin locks and when they are appropriate;
- channels/message passing;
- thread-local storage;
- once/init.

### 3. Atomics and memory ordering

- load/store, read-modify-write;
- compare-and-swap, fetch-add;
- relaxed, acquire, release, acq-rel, seq-cst;
- fences;
- data races and undefined behaviour;
- lock-free vs wait-free (awareness);
- ABA problem;
- false sharing preview (S7).

### 4. Concurrent data structures

- bounded queue;
- thread pool;
- producer–consumer;
- work stealing (concept);
- concurrent hash map (concept);
- reference counting;
- graceful shutdown and cancellation;
- backpressure.

### 5. Testing and debugging concurrency

- stress tests;
- deterministic schedulers (`loom` for Rust, `rr`, model checking);
- ThreadSanitizer;
- deadlock detection;
- logging without changing timing too much;
- reproducing a race;
- proving a happens-before argument.

### 6. Async and event-driven

- futures, tasks, executors;
- async/await vs threads;
- cancellation and timeouts;
- blocking in async code;
- event loops (preview of S10).

## Labs

### Lab 1 — Racy counter

Write a counter incremented by N threads without synchronization. Show a lost update. Fix it with a mutex, then with an atomic. Compare correctness and performance. Explain why the race may not appear every run.

### Lab 2 — Bounded queue

Implement a bounded queue with a mutex and two condition variables. Requirements:

- block when full/empty;
- support close/shutdown;
- no lost wakeups;
- no busy-waiting;
- tests for multiple producers/consumers;
- a stress test with a timeout.

### Lab 3 — Thread pool

Build a thread pool with a job queue, worker threads, graceful shutdown, and error propagation. Add a benchmark comparing fixed vs dynamic scheduling.

### Lab 4 — Memory ordering

Implement a published-value example with relaxed vs acquire/release ordering. Show a case that fails with relaxed and passes with acquire/release. Explain the happens-before edges.

### Lab 5 — Deadlock and repair

Create a program that deadlocks due to lock ordering. Diagnose it with a debugger/ThreadSanitizer, fix it with a documented lock order, and add a regression test or stress harness.

## Exercises

1. Define data race, race condition, and deadlock with examples.
2. Draw the happens-before graph for a producer–consumer trace.
3. Explain why `if` is wrong around `wait` and `while` is right.
4. Implement a semaphore from a mutex and condition variable.
5. Explain the four memory orderings with one use case each.
6. Find the bug in five supplied concurrent programs.
7. Explain why a race may disappear under `printf`.
8. Calculate the maximum useful thread count for a CPU-bound and I/O-bound workload.
9. Explain false sharing and how to detect it (preview of S7).
10. Explain when async is better than threads and when it is not.

## Project increment — P4 workbenchd concurrency core

Implement the reusable concurrency core for `workbenchd`:

- bounded work queue;
- worker pool;
- graceful shutdown with in-flight work;
- metrics: queue depth, jobs completed, errors;
- stress tests and a benchmark;
- a short correctness argument.

**Brief:** [P4 — workbenchd](../projects/project-ladder.md#p4--workbenchd)

## Exit check

- [ ] explain why concurrent code is correct, not merely usually successful;
- [ ] choose and defend a memory ordering;
- [ ] implement a bounded queue without lost wakeups;
- [ ] diagnose a deadlock and a data race;
- [ ] show a happens-before argument for a published value;
- [ ] demonstrate clean shutdown under load.

## Common failure modes

- Using a mutex but reading shared state outside it.
- `if` instead of `while` around a condition variable.
- Holding a lock while doing I/O or calling user code.
- Assuming atomics make a whole operation atomic.
- Using `relaxed` everywhere because it is faster.
- Testing concurrency only with a single run.
- Ignoring cancellation and shutdown until production.

## Evidence to commit

- `labs/systems/S6/` with racy counter, bounded queue, thread pool, ordering lab, deadlock report
- P4 concurrency core
- `notes/systems/S6/summary.md`

## Optional depth

- *Rust Atomics and Locks* Ch. 5–7 (spin locks, channels, concurrent data structures).
- *The Art of Multiprocessor Programming* (Herlihy & Shavit).
- *Java Concurrency in Practice* for concepts that transfer.
- `loom`, `shuttle`, and `rr` for systematic testing.
