# B6 — *What Every Programmer Should Know About Memory*

**Author:** Ulrich Drepper · **Published:** 2007 (Red Hat white paper) · **Level:** intermediate to advanced · **Access:** [free PDF](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf)

A deep, practical explanation of the memory hierarchy: DRAM, caches, TLBs, NUMA, prefetching, and optimization. The hardware examples are old, but the mechanisms and measurement methodology remain valuable. Always pair the reading with measurements on your own machine.

## Structure

| Part | Sections | Theme |
| --- | --- | --- |
| Introduction | 1 | Why memory matters |
| Commodity hardware | 2 | RAM, northbridge/southbridge, buses |
| CPU caches | 3.1–3.5 | Cache types, operation, associativity, write policy, misses |
| Virtual memory | 4 | Pages, page tables, TLB, translation, virtualization |
| NUMA | 5 | Nodes, local/remote memory, policy |
| Multi-threaded optimizations | 6 | Affinity, cache sharing, false sharing, memory ordering |
| Performance tools | 7 | `perf`, `oprofile`, measurement |
| Future | 8 | Trends and implications |
| Appendices | A, D | Cache/TLB details, glossary or measurement notes |

**Section warning:** the paper is not a modern textbook. Use its section titles and figures, and verify current cache/TLB numbers with `lscpu`, `getconf`, and sysfs.

## Course map

| Course | Read | Why | Check |
| --- | --- | --- | --- |
| [S3](../systems/S3-memory-hierarchy-and-locality.md) | Ch. **2**, §§**3.1–3.5** | DRAM, caches, locality | Measure a memory mountain |
| [S4](../systems/S4-cpu-caches.md) | §§**3.2–3.5**, §§**6.2–6.3**, App. **A.1** | Cache organization and measurement | Build a cache simulator and validate it |
| [S5](../systems/S5-virtual-memory.md) | Ch. **4** | Paging, TLB, translation | Measure TLB/page-fault effects |
| [S6](../systems/S6-concurrency-atomics-and-memory-models.md) | §**6.4**, §**8.1** | Cache sharing, memory ordering | Explain a false-sharing/ordering result |
| [S7](../systems/S7-cache-coherence-and-false-sharing.md) | §**6.4**, App. **A.3** | Coherence and false sharing | Measure a false-sharing penalty |
| [S8](../systems/S8-numa-and-memory-topology.md) | Ch. **5**, §**6.5**, App. **D** | NUMA topology and policy | Measure local vs remote access |
| [S9](../systems/S9-performance-engineering-and-observability.md) | Ch. **7**, §**8.3** | Performance tools and counters | Diagnose a memory bottleneck |
| [S13](../systems/S13-ai-infrastructure-systems-lens.md) | Ch. **2–3, 5–7** | Bandwidth, caches, NUMA, tools | Connect CPU memory behavior to GB200/HBM |
| [AI16](../ai/AI16-gpu-programming-and-kernels.md) | Ch. **2–3, 5–6** | Memory hierarchy and coalescing analogy | Explain GPU memory coalescing using CPU cache concepts |

## Reading route

1. **S3:** Ch. 2 and §3.1–3.5. Write down the latency/bandwidth numbers for your machine before reading, then compare.
2. **S4:** §3.2–3.5 and §6.2–6.3. Build the cache simulator; use the paper's associativity/tag/index explanation.
3. **S7/S8:** §6.4, Ch. 5, and the appendices. Measure false sharing and NUMA before reading the optimization advice.
4. **S9:** Ch. 7. Use `perf stat`, `perf c2c`, and `numastat`; record unavailable counters.
5. **S13/AI16:** read for the hierarchy and bandwidth model, then translate to HBM/shared memory with the GPU docs.

## Labs that pair well

- Memory mountain: pointer-chase latency across working-set sizes.
- Cache associativity/conflict experiment with a strided access pattern.
- False sharing: two threads writing adjacent cache lines.
- NUMA: `numactl --cpunodebind` vs `--membind`, measure bandwidth/latency.
- TLB: huge pages vs 4 KiB pages for a large random-access workload.
- Prefetcher: sequential vs random access at several strides.

## Measurement rules

- Record CPU model, core/thread count, cache sizes (`lscpu`), RAM, NUMA nodes, kernel, compiler, optimization flags, and governor.
- Warm up, run multiple repetitions, and report variance—not one number.
- Separate latency from bandwidth; do not compare them as if they were the same metric.
- If a performance counter is unavailable in a VM/container, say so. Do not fabricate a number.
- The paper's hardware numbers are historical; your measurements are the evidence.

## Limits

- 2007 hardware: no modern DDR5, chiplets, HBM, or hybrid cores.
- The paper's NUMA and prefetch advice is directional, not a substitute for profiling.
- It does not cover GPU memory hierarchies; pair with AI16 and vendor docs.
- It is not a substitute for the Intel/AMD optimization manuals when you need exact ISA behaviour.

## Acquisition

Free PDF from the official mirrors. Do not commit the PDF; link to it and keep local notes.
