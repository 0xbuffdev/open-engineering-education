# AI16 — GPU Programming & Kernels

**Track:** AI & ML · **Prerequisite:** S13 or AI9 · **Elective** · **Time:** 5 weeks, 75 hours · **Project:** elective
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Learn to program accelerators and reason about kernel performance. You will write and profile small CUDA/Triton kernels, analyze memory coalescing and occupancy, and connect kernel behavior to model-serving cost.

## Outcomes

You can:

- explain the GPU execution model: grids, blocks, warps, lanes, and scheduling;
- write correct vector-add, reduction, and tiled matrix-multiply kernels;
- coalesce global-memory access and use shared memory effectively;
- explain occupancy, register pressure, and latency hiding;
- use the roofline model for a kernel;
- profile with Nsight Compute or an equivalent tool;
- compare CUDA and Triton implementations;
- validate numerical correctness against a CPU/PyTorch baseline;
- state when a custom kernel is not justified.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [CUDA C Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) | Programming model, memory, performance, warps | CUDA fundamentals |
| [CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/) | Full | Optimization patterns |
| [Programming Massively Parallel Processors](https://www.elsevier.com/books/programming-massively-parallel-processors/hwu/9780323912310) (4th ed.) | Ch. **1–7, 10–12** | Structured treatment |
| [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/) | Vector add, matmul, softmax | Higher-level kernels |
| [Nsight Compute docs](https://docs.nvidia.com/nsight-compute/) | Metrics, roofline, memory analysis | Measurement |
| [Roofline paper](https://dl.acm.org/doi/10.1145/1498765.1498785) | Full | Performance model |

## Modules

1. **Execution model** — host/device, grids, blocks, warps, threads, SIMT, divergence, synchronization.
2. **Memory hierarchy** — registers, shared memory, L1/L2, global/HBM, coalescing, bank conflicts, caching.
3. **Kernel patterns** — map, reduce, scan, transpose, stencil, tiled GEMM, softmax.
4. **Performance** — occupancy, register pressure, instruction mix, latency hiding, roofline, arithmetic intensity.
5. **Profiling** — correctness first, warm-up, timing, counters, memory throughput, achieved occupancy, bottleneck classification.
6. **Modern tooling** — Triton, CUDA graphs, streams, Tensor Cores, mixed precision; when to use libraries instead.

## Labs

### Lab 1 — Vector add and bandwidth

Write vector add in CUDA/Triton. Validate against CPU. Measure achieved bandwidth for several block sizes and compare with the device peak. Explain the gap.

### Lab 2 — Reduction

Implement a parallel sum reduction with shared memory. Handle non-power-of-two sizes and numerical error. Compare naive, tree, and warp-shuffle variants.

### Lab 3 — Tiled matrix multiply

Implement tiled GEMM. Compare naive and tiled versions. Profile memory throughput, occupancy, and compute utilization. Validate against PyTorch.

### Lab 4 — Softmax or layernorm kernel

Implement a row-wise softmax with numerical stability. Handle long rows. Profile and compare with PyTorch. Explain one correctness or performance issue.

### Lab 5 — Roofline report

For one kernel, compute arithmetic intensity, measured FLOP/s, and memory bandwidth. Place it on a roofline plot. State the bottleneck and what change would move it.

## Exercises

1. Calculate warps per block for a given block size.
2. Explain coalesced versus strided access.
3. Compute shared-memory bank conflicts for an access pattern.
4. Explain occupancy and one reason to limit it.
5. Calculate arithmetic intensity for GEMM.
6. Explain why a reduction needs synchronization.
7. Compare CUDA and Triton trade-offs.
8. Diagnose a kernel that is memory-bound.
9. Explain Tensor Core requirements.
10. State when a custom kernel is slower than a library.

## Project increment (optional)

Write and benchmark one GPU kernel against a PyTorch or Triton baseline. Report occupancy, memory traffic, the roofline, and correctness across shapes. Integrate it into P8/P9 only if it improves a measured end-to-end metric. This is an elective extension, not a new ladder project.

## Exit check

- [ ] write a correct vector add and reduction;
- [ ] implement tiled GEMM and validate it;
- [ ] profile a kernel and identify the bottleneck;
- [ ] explain coalescing, occupancy, and roofline for your kernel;
- [ ] compare against a library baseline;
- [ ] state when not to write a custom kernel.

## Common failure modes

- Benchmarking without warm-up or synchronization.
- Ignoring numerical error in reductions.
- Assuming high occupancy always means fast.
- Uncoalesced access and shared-memory bank conflicts.
- Comparing against a poorly configured baseline.
- Optimizing a kernel that is not the bottleneck.
- Reporting device peak as achieved performance.

## Evidence to commit

- `labs/ai/AI16/` with vector add, reduction, GEMM, softmax, profiles, roofline
- `notes/ai/AI16/summary.md`
- GPU model, driver, CUDA/Triton versions, and clocks

## Optional depth

- *CUDA by Example* (Sanders & Kandrot).
- *Professional CUDA C Programming* (Cheng et al.).
- Triton language and compiler internals.
- CUTLASS and FlashAttention kernel design.
- `nsys` and Nsight Systems for end-to-end traces.
