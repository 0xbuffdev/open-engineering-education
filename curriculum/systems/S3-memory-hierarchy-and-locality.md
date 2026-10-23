# S3 — Memory Hierarchy & Locality

**Track:** Systems · **Prerequisite:** S2 · **Core** · **Time:** 4 weeks, 60 hours · **Project:** P3 memory mountain

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Modern CPUs are much faster than DRAM. Performance is dominated by whether data is in a register, L1, L2, L3, or main memory. This course builds the mental model and the measurement skills to predict and improve locality.

## Outcomes

You can:

- explain the memory hierarchy and the latency/bandwidth gap;
- calculate the cost of a cache miss and an access pattern;
- explain spatial/temporal locality and how data layout affects it;
- measure a memory mountain varying stride and working-set size;
- distinguish latency-bound from bandwidth-bound workloads;
- use the roofline model qualitatively;
- predict why two O(n) loops differ in runtime and validate the prediction.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B3 *Digital Design and Computer Architecture* | §**5.5**, §§**8.1–8.3** | Memory arrays, memory-system performance, caches |
| B6 *What Every Programmer Should Know About Memory* | Ch. **2**, §§**3.1–3.5** | RAM technology, cache operation, associativity, write behaviour, miss factors |
| CS:APP | §§**6.1–6.4** | Storage technologies, locality, memory hierarchy, cache organization |
| [Ulrich Drepper, “Memory part 1–3”](https://lwn.net/Articles/250967/) | Optional | Readable companion to B6 |

## Modules

### 1. The hierarchy

- registers, L1/L2/L3, DRAM, SSD, network;
- latency and bandwidth orders of magnitude;
- SRAM vs DRAM, row buffer, CAS/RAS;
- cache lines, sets, ways, tags, offsets;
- inclusive vs exclusive caches;
- write-through vs write-back, write-allocate;
- replacement policies (LRU, pseudo-LRU, random).

### 2. Locality

- temporal and spatial locality;
- row-major vs column-major traversal;
- array of structs vs struct of arrays;
- linked lists vs arrays;
- blocking/tiling;
- prefetching (hardware and software);
- cache-oblivious algorithms (intro).

### 3. Measurement

- working-set size vs stride;
- memory mountain;
- `perf stat` counters (cache-misses, cache-references, cycles, instructions);
- `gettimeofday`/`clock_gettime` and benchmark noise;
- CPU frequency scaling and pinning;
- latency vs bandwidth microbenchmarks;
- roofline model.

## Labs

### Lab 1 — Memory mountain

Write a benchmark that traverses an array with varying stride and working-set size. Plot cycles per element. Identify L1/L2/L3/DRAM plateaus and estimate cache sizes. Record CPU model, cache sizes, and compiler flags.

### Lab 2 — Access patterns

Compare contiguous, strided, linked-list, and random access on the same number of elements. Predict the order before measuring. Explain the gap with cache-line and prefetch reasoning.

### Lab 3 — Data layout

Implement a particle or record simulation with array-of-structs and struct-of-arrays. Measure both. Explain when each layout wins and why.

### Lab 4 — Matrix traversal

Compare row-major and column-major traversal of a large matrix. Then add blocking/tiling and measure. Explain the improvement using cache capacity and reuse.

### Lab 5 — Roofline sketch

For one kernel (dot product, matrix multiply, or stencil), estimate arithmetic intensity and place it on a roofline sketch. State whether it is latency-, bandwidth-, or compute-bound.

## Exercises

1. Calculate the number of cache lines touched by five access patterns.
2. Convert latency numbers to cycles at 3 GHz.
3. Explain why a linked list can be slower than an array even with the same O(n).
4. Predict the effect of doubling the working set.
5. Explain write-back vs write-through with a timeline.
6. Identify three locality bugs in supplied code.
7. Explain why benchmarking without pinning can mislead.
8. Estimate arithmetic intensity for a matrix multiply.
9. Explain hardware prefetching and one case where it hurts.
10. Explain why a smaller data structure can be slower.

## Project increment — P3 memory mountain

Create a reusable benchmark harness in C or Rust:

- configurable stride, working-set size, iterations, and thread count;
- CSV/JSON output with environment metadata;
- a plotting script;
- a report with prediction, measurement, and interpretation.

This harness is reused in S4, S7, S8, and S9.

**Brief:** [P3 — cachebench](../projects/project-ladder.md#p3--cachebench)

## Exit check

- [ ] predict why two O(n) loops differ in runtime, then validate with data;
- [ ] measure a memory mountain and identify cache levels;
- [ ] explain spatial/temporal locality in your own code;
- [ ] distinguish latency-bound from bandwidth-bound;
- [ ] explain one layout change that improved performance and its cost;
- [ ] state the limits of your benchmark.

## Common failure modes

- Benchmarking a working set that fits in cache and generalizing.
- Ignoring compiler vectorization and optimization flags.
- Using wall-clock time without enough iterations.
- Measuring on a noisy laptop without recording frequency/thermal state.
- Treating the memory mountain as universal across CPUs.
- Confusing cache line size with word size.

## Evidence to commit

- `labs/systems/S3/` with benchmark harness, plots, and report
- P3 memory mountain
- `notes/systems/S3/summary.md`

## Optional depth

- B6 §3.5 in full (cache/memory bandwidth, critical word load, FSB).
- *Systems Performance* (Gregg) Ch. 7.
- `likwid`, `cachegrind`, and `perf c2c`.
- Cache-oblivious matrix multiplication.
