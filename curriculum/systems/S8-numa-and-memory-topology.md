# S8 — NUMA & Memory Topology

**Track:** Systems · **Prerequisite:** S7 · **Core** · **Time:** 2 weeks, 30 hours · **Project:** P3 topology report
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

On multi-socket and large multi-core machines, memory access cost depends on which node owns the data and which core touches it. NUMA is the difference between a benchmark that scales and one that collapses.

## Outcomes

You can:

- inventory CPU/memory topology with `numactl`, `lscpu`, `/sys`, and `hwloc`;
- explain first-touch allocation and local vs remote access;
- use memory policies (`--localalloc`, `--interleave`, `--membind`);
- bind threads and memory to nodes;
- measure local/remote latency and bandwidth;
- explain NUMA balancing and when it helps/hurts;
- state when a single-node result cannot generalize.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B6 | Ch. **5**, §**6.5**, Appendix **D** | NUMA hardware, OS support, remote access costs, programming, libNUMA |
| B5 | §**35.4** | CPU affinity |
| [Linux NUMA memory policy docs](https://docs.kernel.org/admin-guide/mm/numa_memory_policy.html) | Full | Current Linux policy semantics |
| [numactl man page](https://man7.org/linux/man-pages/man8/numactl.8.html) | Full | Practical commands |

## Modules

### 1. Topology

- sockets, cores, SMT/hyperthreads;
- NUMA nodes, local/remote memory;
- cache hierarchy per node;
- interconnects (UPI/Infinity Fabric);
- `lscpu`, `numactl -H`, `hwloc-ls`, `/sys/devices/system/node`;
- memory holes and node distances.

### 2. Allocation and policy

- first-touch;
- `mbind`, `set_mempolicy`, `get_mempolicy`;
- `numactl --localalloc`, `--interleave`, `--membind`, `--preferred`;
- `numa_alloc_onnode`, `numa_run_on_node` (libnuma);
- `MADV_HUGEPAGE` interaction;
- page migration and NUMA balancing;
- cgroup memory placement (preview of S14).

### 3. Measurement

- local vs remote latency;
- local vs remote bandwidth;
- thread pinning;
- memory pinning;
- scaling curves;
- noise and frequency effects;
- documenting unavailable hardware.

### 4. Performance patterns

- first-touch initialization;
- per-node data partitioning;
- replication vs remote access;
- interleaving for bandwidth;
- binding for latency;
- avoiding cross-node false sharing.

## Labs

### Lab 1 — Topology inventory

Record `lscpu`, `numactl -H`, `hwloc-ls`, and node distances. Draw the topology. If the machine has one node, document that and use a public benchmark or simulator for the rest.

### Lab 2 — First touch

Allocate a large array, initialize it from one thread on node 0, then read it from a thread on node 1 (if available). Measure bandwidth/latency. Compare with interleaved allocation.

### Lab 3 — Pinning

Run a memory-bound benchmark with:

- no pinning;
- CPU pinning only;
- CPU + memory pinning;
- interleaved memory.

Measure and explain.

### Lab 4 — NUMA-aware data layout

Partition a workload by node (per-node accumulators or shards) and compare with a shared global structure. Explain the trade-off.

## Exercises

1. Draw a two-socket topology with local/remote paths.
2. Explain first-touch with a timeline.
3. Compare `--localalloc`, `--interleave`, and `--membind`.
4. Explain why a single-node benchmark can mislead.
5. Explain NUMA balancing and one failure mode.
6. Calculate the theoretical bandwidth of local vs remote access.
7. Explain how thread pinning interacts with memory policy.
8. Explain why per-node replication can beat shared memory.
9. State what you cannot conclude without multi-node hardware.
10. Design a NUMA-aware queue or counter.

## Project increment — P3 topology report

Add a topology and NUMA section to P3:

- machine inventory;
- allocation policy experiments;
- local/remote measurements where possible;
- an explicit "hardware limitation" section if single-node;
- a recommendation for the benchmark harness.

**Brief:** [P3 — cachebench](../projects/project-ladder.md#p3--cachebench)

## Exit check

- [ ] explain first-touch placement;
- [ ] show evidence separating local from remote access, or document why the hardware cannot;
- [ ] use `numactl`/`hwloc` to inventory topology;
- [ ] explain one NUMA-aware data layout;
- [ ] state the limits of your measurements.

## Common failure modes

- Assuming all cores have equal memory access cost.
- Allocating on one node and reading on another without noticing.
- Pinning CPUs but not memory.
- Interleaving everything and hurting latency-sensitive work.
- Reporting a single-node result as a general NUMA result.
- Ignoring huge pages and NUMA balancing interactions.

## Evidence to commit

- `labs/systems/S8/` with topology, benchmark, plots, limitation note
- P3 topology report
- `notes/systems/S8/summary.md`

## Optional depth

- `hwloc` documentation and `lstopo`.
- *What Every Programmer Should Know About Memory* Ch. 5 in full.
- Vendor NUMA optimization guides (Intel/AMD/ARM).
- Study a public multi-node benchmark if you lack hardware.
