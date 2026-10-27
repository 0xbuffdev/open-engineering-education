# S4 — CPU Caches

**Track:** Systems · **Prerequisite:** S3 · **Core** · **Time:** 4 weeks, 60 hours · **Project:** P3 cache simulator
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Go from "caches exist" to "I can calculate a cache's behaviour and optimize for it." You will build a configurable cache simulator, hand-trace addresses, and measure real matrix-multiplication variants.

## Outcomes

You can:

- calculate tag/set/offset fields for a given address and cache geometry;
- simulate direct-mapped, set-associative, and fully associative caches;
- distinguish compulsory, capacity, and conflict misses;
- explain replacement and write policies;
- optimize a kernel with blocking/tiling and explain the result;
- use `perf stat` cache counters and state their limitations;
- distinguish a cache miss from a TLB miss and a page fault.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B3 | §§**8.2–8.3** | Memory-system performance and cache design |
| B6 | §§**3.2–3.5** | Cache operation, implementation, associativity, write behavior, miss factors |
| B6 | §§**6.2–6.3**, Appendix **A.1** | Cache access optimization, prefetching, matrix multiplication |
| CS:APP | §§**6.4–6.7** | Cache organization, performance, and lab-style cache simulation |
| [Intel/AMD optimization manuals](https://www.agner.org/optimize/) | Cache chapters | Real hardware details |

## Modules

### 1. Cache geometry

- address decomposition: tag, set index, block offset;
- direct-mapped, N-way set-associative, fully associative;
- capacity = line size × associativity × sets;
- valid/dirty bits;
- address aliasing and virtual vs physical indexing;
- VIPT/PIPT (concept);
- cache line size and sectoring.

### 2. Misses and policies

- compulsory, capacity, conflict;
- LRU, pseudo-LRU, random, FIFO;
- write-through, write-back, write-allocate, no-write-allocate;
- replacement effects;
- prefetching;
- inclusive/exclusive/non-inclusive;
- shared vs private caches.

### 3. Cache-aware optimization

- loop interchange;
- blocking/tiling for matrix multiply;
- loop fusion/fission;
- padding to avoid conflict misses;
- data alignment;
- streaming stores (concept);
- software prefetch;
- cache-oblivious recursion.

### 4. Measurement

- `perf stat -e cache-references,cache-misses,cycles,instructions`;
- `perf record`/`perf report`;
- `cachegrind`;
- TLB counters;
- benchmark controls and repeatability.

## Labs

### Lab 1 — Cache simulator

Implement a configurable simulator with:

- cache size, line size, associativity, replacement policy, write policy;
- address trace input;
- hit/miss/eviction counters;
- compulsory/capacity/conflict classification;
- tests with hand-computed traces.

Run it on traces from your own programs.

### Lab 2 — Hand traces

For five address sequences, compute hits/misses/evictions for direct-mapped and 2-way caches. Compare with the simulator.

### Lab 3 — Matrix multiplication

Benchmark naïve, transposed, and blocked matrix multiplication. Measure runtime and cache misses. Explain the improvement and the point where blocking stops helping.

### Lab 4 — Conflict misses

Construct an access pattern that suffers conflict misses in a direct-mapped cache but improves in a 2-way cache or with padding. Measure and explain.

### Lab 5 — Cache vs TLB vs page fault

Write a program that triggers a cache miss, a TLB miss, and a page fault (or observe them with `perf`). Explain the different costs and mechanisms.

## Exercises

1. Compute tag/set/offset for ten addresses.
2. Calculate cache capacity and number of sets.
3. Simulate five traces by hand.
4. Classify misses for three loops.
5. Explain why increasing associativity can hurt.
6. Explain why a write-back cache needs a dirty bit.
7. Compare LRU and random replacement on a small trace.
8. Explain the difference between a cache miss and a page fault.
9. Predict the effect of loop order on a matrix kernel.
10. Explain one reason `perf` cache counters may be misleading.

## Project increment — P3 cache simulator

Add the simulator to the P3 harness with:

- a documented trace format;
- a CLI and config file;
- tests and example traces;
- a report comparing simulation with measured `perf` counters;
- a limitation section (e.g., no prefetcher model).

**Brief:** [P3 — cachebench](../projects/project-ladder.md#p3--cachebench)

## Exit check

- [ ] calculate tag/set/offset fields;
- [ ] distinguish a cache miss, TLB miss, and page fault;
- [ ] simulate a trace and match a hand calculation;
- [ ] optimize a matrix kernel and prove the improvement with measurements;
- [ ] explain one optimization that did not work and why;
- [ ] state the limits of your simulator.

## Common failure modes

- Forgetting that cache line size affects the offset bits.
- Confusing cache size with number of sets.
- Assuming all misses are capacity misses.
- Benchmarking with compiler auto-vectorization and attributing everything to caches.
- Ignoring the TLB.
- Optimizing a kernel that is not cache-bound.

## Evidence to commit

- `labs/systems/S4/` with simulator, traces, matrix benchmark, report
- P3 cache simulator
- `notes/systems/S4/summary.md`

## Optional depth

- B6 §3.5 and Ch. 7.
- CS:APP Cache Lab.
- *What Every Programmer Should Know About Memory* Appendix A.
- Read your CPU's optimization guide for cache-line size and prefetchers.
