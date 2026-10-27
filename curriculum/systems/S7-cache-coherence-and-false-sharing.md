# S7 — Cache Coherence & False Sharing

**Track:** Systems · **Prerequisite:** S4, S6 · **Core** · **Time:** 2 weeks, 30 hours · **Project:** P3 false-sharing study
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Multi-core performance is shaped by cache coherence. Two threads writing unrelated variables can destroy throughput if those variables share a cache line. This short course makes coherence protocols and false sharing measurable.

## Outcomes

You can:

- explain MESI/MOESI states and transitions at a high level;
- explain read-for-ownership, invalidation, and store buffers;
- distinguish true sharing from false sharing;
- detect false sharing with `perf c2c` or a controlled benchmark;
- fix it with padding, alignment, or per-thread data;
- quantify the cost across thread counts and data layouts.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B3 | §**7.8.8** | Multiprocessors and coherence |
| B6 | §**6.4**, Appendix **A.3** | Multi-thread optimizations, cache-line sharing overhead |
| [Linux `perf c2c` docs](https://perf.wiki.kernel.org/index.php/Tutorial#Cache_to_Cache) | Selected sections | Detection tool |
| [Ulrich Drepper, “Memory part 6”](https://lwn.net/Articles/256433/) | Full | Concurrency, atomicity, bandwidth |

## Modules

### 1. Coherence

- why private caches need coherence;
- invalidation vs update;
- MESI states: Modified, Exclusive, Shared, Invalid;
- read-for-ownership;
- store buffers and memory barriers;
- coherence vs consistency (preview of S6);
- NUMA preview (S8).

### 2. False sharing

- cache line granularity;
- adjacent counters/fields;
- true vs false sharing;
- padding and alignment;
- per-thread accumulators;
- data layout changes;
- compiler and allocator effects;
- detection with `perf c2c`, `perf stat`, and timing.

## Labs

### Lab 1 — Adjacent vs padded counters

Write a benchmark with N threads incrementing adjacent counters in one struct and padded counters on separate cache lines. Measure across 1, 2, 4, 8, … threads. Predict the curves before measuring.

### Lab 2 — Separate contention sources

Design a benchmark that separates:

- lock contention;
- true sharing of one counter;
- false sharing of adjacent counters;
- independent per-thread work.

Show which one dominates in each configuration.

### Lab 3 — Detect with `perf c2c`

If available, run `perf c2c record`/`report` on the false-sharing benchmark. Identify the cache line and the conflicting accesses. If unavailable, document the limitation and use timing plus layout evidence.

## Exercises

1. Draw MESI transitions for a read then write by two cores.
2. Explain read-for-ownership in one paragraph.
3. Predict the effect of padding on a 4-thread counter benchmark.
4. Explain why a `struct` of two `u64` counters can be pathological.
5. Explain why false sharing is a performance bug, not a correctness bug.
6. Explain how per-thread accumulation avoids the problem.
7. Explain one case where padding hurts (memory footprint/cache capacity).
8. Explain the difference between coherence and consistency.
9. Design a benchmark that would expose false sharing in a queue.
10. State one limitation of `perf c2c`.

## Project increment — P3 false-sharing study

Add a false-sharing benchmark and report to P3:

- adjacent vs padded vs per-thread counters;
- thread-count sweep;
- timings and, if available, `perf c2c` evidence;
- a recommendation with a cost/benefit statement.

**Brief:** [P3 — cachebench](../projects/project-ladder.md#p3--cachebench)

## Exit check

- [ ] identify false sharing from a data layout;
- [ ] prove an improvement with a measurement;
- [ ] distinguish true sharing, false sharing, and lock contention;
- [ ] explain MESI at a level that predicts the benchmark;
- [ ] state the memory-cost trade-off of padding.

## Common failure modes

- Adding padding everywhere and wasting cache capacity.
- Measuring only one thread count.
- Confusing false sharing with a data race.
- Assuming `volatile` fixes coherence.
- Ignoring allocator placement of separately allocated objects.
- Trusting one run on a noisy machine.

## Evidence to commit

- `labs/systems/S7/` with benchmark, plots, `perf c2c` output or limitation note, report
- P3 false-sharing study
- `notes/systems/S7/summary.md`

## Optional depth

- B6 Ch. 6 in full.
- *A Primer on Memory Consistency and Cache Coherence* (Sorin, Hill, Wood).
- `perf c2c` documentation and examples.
- Study your CPU's cache-line size and prefetcher behaviour.
