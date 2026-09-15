# Systems Engineering Practice Guide

Run these labs on Linux unless the course documents a safe fallback. Use C when the goal is to expose an OS or machine interface; use Rust for maintainable multi-file systems. Record the full environment and a prediction before every measurement.

## S1 — Computer Systems Foundations

### Labs

1. **Process and descriptor probes.** Write small C probes for addresses, allocation/free, descriptors, `fork`, and `exec`. State ownership and expected output before running each.
2. **C-to-Rust comparison.** Rebuild two probes in safe Rust and document which failure modes move from runtime to compile time and which remain.

### Exercises

1. Trace stack, heap, static, and code addresses for a small C program.
2. Draw parent/child process states around `fork`, `exec`, and `wait`.
3. Identify descriptor ownership through a pipeline and repair intentional allocation/descriptor leaks.
4. Add checks for failure paths, not just success paths.

**Ready when:** the report explains the journey from `main` to OS services and compares one real C failure with the Rust version.

## S2 — Machine Code, CPU, and Computer Architecture

### Labs

1. **Source-to-assembly trace.** Compile a small C/Rust function at two optimization levels; inspect symbols, sections, disassembly, and registers through a load, call, branch, and return.
2. **Branch/arithmetic benchmark.** Compare predictable branch, unpredictable branch, and branch-reduced versions using repeatable inputs. Report compiler flags, dispersion, and why instruction count alone misleads.

### Exercises

1. Hand-trace a simplified datapath for load, add, branch, call, and return.
2. Label instruction/data dependencies and possible pipeline hazards.
3. Decode a small disassembly into variables and control flow.
4. Compare signed/unsigned overflow and explain one correct/incorrect branch-prediction example.

**Ready when:** you can follow one function across source, assembly, registers, and return value without guessing.

## S3 — Memory Hierarchy and Locality

### Labs

1. **Memory mountain.** Vary working-set size and stride in a compiled benchmark. Produce a table or heatmap with warm-up and repeated measurements.
2. **Layout comparison.** Compare contiguous, strided, linked-list, and random access over equivalent work. Explain the prediction and any surprising result.

### Exercises

1. Classify temporal and spatial locality in short loops.
2. Predict cache-friendly versus cache-hostile traversals.
3. Calculate bytes touched for row-major and column-major loops.
4. Design controls that separate allocation, initialization, and access costs.

**Ready when:** the memory-mountain result includes raw data and a defensible locality explanation.

## S4 — CPU Caches

### Labs

1. **Configurable cache simulator.** Implement direct-mapped, set-associative, and fully associative modes with explicit block size, set count, replacement policy, and trace input.
2. **Matrix-access study.** Benchmark naïve, transposed, and tiled matrix multiplication at several dimensions. Pair with `perf stat` where available; otherwise document the limitation.

### Exercises

1. Hand-trace a short address stream through a chosen configuration.
2. Calculate tag, set, and offset fields.
3. Distinguish compulsory, capacity, and conflict misses.
4. Choose tile sizes as hypotheses and distinguish cache miss, TLB miss, and page fault.

**Ready when:** tests cover hit, miss, eviction, and associativity changes, and the matrix study explains results rather than only selecting a winner.

## S5 — Virtual Memory

### Labs

1. **Address translation simulator.** Given virtual address, page size, and page-table entries, simulate translation, TLB state, permissions, and page-fault outcomes.
2. **Mapping behaviour study.** Compare `malloc`, anonymous `mmap`, file-backed private/shared mappings, and copy-on-write in a local test program. Observe mappings/fault counters with OS-provided tools.

### Exercises

1. Split virtual addresses into VPN/offset for several page sizes.
2. Hand-walk a page-table and TLB lookup.
3. Identify protection/isolation outcomes for read/write/execute cases.
4. Reason about copy-on-write after `fork` and design cleanup for mapped resources.

**Ready when:** the report independently explains a TLB miss, a page-table walk, and a page fault.

## S6 — Concurrency, Atomics, and Memory Models

### Labs

1. **Bounded queue and thread pool.** Implement a bounded queue and worker pool with clear shutdown semantics. Stress it and prove blocked producers/consumers can finish safely.
2. **Race diagnosis.** Create a deliberately racy local counter, demonstrate nondeterministic failure, repair it, and write the happens-before argument.

### Exercises

1. Enumerate interleavings for two tiny threads.
2. Classify data race, deadlock, livelock, and starvation scenarios.
3. Compare mutex, channel, atomic, and immutable-message designs.
4. Justify an ordering for one atomic protocol and test cancellation/cleanup.

**Ready when:** correctness is established with invariants and tests, not a single successful run.

## S7 — Cache Coherence and False Sharing

### Labs

1. **Counter-layout benchmark.** Compare adjacent counters, padded counters, and a shared locked counter across increasing thread counts. Keep work equal.
2. **Contention control.** Separate synchronization contention from false sharing and explain which control supports each conclusion.

### Exercises

1. Sketch cache-line ownership transitions for a shared write.
2. Identify likely false-sharing fields in several structs.
3. Calculate padding/alignment consequences.
4. Predict scaling curves and list alternative designs such as sharding/reduction.

**Ready when:** you show evidence for an improvement and avoid claiming every multicore regression is false sharing.

## S8 — NUMA and Memory Topology

### Labs

1. **Topology inventory.** Capture CPU, cache, node, and memory topology using Linux tooling; distinguish tool facts from assumptions.
2. **Local/remote study or fallback.** On a NUMA host compare pinned-thread first-touch/local allocation with remote placement. Without suitable hardware, document a reproducible methodology and the missing capability.

### Exercises

1. Explain first-touch with a multi-thread initialization example.
2. Map cores to NUMA nodes from supplied topology output.
3. Predict effects of migrating a thread or data.
4. Propose a memory-placement strategy for a sharded service.

**Ready when:** hardware constraints are explicit and local-versus-remote claims have evidence.

## S9 — Performance Engineering and Observability

### Labs

1. **Investigation log.** Complete ten compact investigations from earlier artifacts: baseline, hypothesis, one measurement source, change, result, and confidence. At least three should end with a rejected hypothesis.
2. **Measured repair.** Fix one confirmed bottleneck, prove its effect with before/after data, and confirm correctness remains intact.

### Exercises

1. Write a benchmark plan controlling warm-up, input, repetitions, and noise.
2. Interpret example CPU, memory, I/O, and scheduler counters.
3. Distinguish p50/p95/p99 and throughput.
4. Identify a misleading benchmark claim and write a performance regression threshold.

**Ready when:** a reader can reproduce the baseline and agrees the conclusion follows from the evidence.

## S10 — Linux Systems Programming and Networking

### Labs

1. **Protocol-correct echo service.** Start with a C CLI and TCP echo server, then implement a safe-Rust multi-client service. Test fragmented requests, partial writes, invalid frames, disconnects, timeouts, and shutdown.
2. **Backpressure/load study.** Apply bounded queues, connection limits, and timeouts under a local load generator. Record latency, errors, resources, and failure without bounds.

### Exercises

1. Parse/validate a length-delimited local protocol.
2. Write robust partial-read/partial-write handling.
3. Map every descriptor/socket/task to its owner and close point.
4. Test timeout, cancellation, malformed-input paths, and write an overload runbook.

**Ready when:** clean shutdown, ownership, and error paths are demonstrated from a clean start.

## S11 — Distributed Systems

### Labs

1. **Staged private KV store.** Build checkpoints for request IDs/RPC, durable append log, restart recovery, leader/replica protocol, and metrics. Preserve an integration test at each checkpoint.
2. **Fault matrix.** Inject local delayed/dropped/duplicate replies, partition simulation, replica restart, and client retry. State the client-visible guarantee and observed result for each.

### Exercises

1. Define request idempotency and deduplication behaviour.
2. Trace a replicated write under normal and retry paths.
3. Write invariants for acknowledged data and log recovery.
4. Compare at-most-once, at-least-once, and effectively-once claims; choose a consistency/durability trade-off.

**Ready when:** fault tests demonstrate limits as well as happy-path replication.

## S12 — Data Systems and Storage Engines

### Labs

1. **Crash-safe LSM store.** Stage WAL append/sync, memtable, sorted-table flush, manifest/checksum, compaction, and recovery. Use a failure-injection hook in your own process.
2. **Workload benchmark.** Generate reproducible read/write/mixed workloads and compare two compaction/table-size configurations, including write amplification and tail latency where measurable.

### Exercises

1. Implement/test record encoding with corruption detection.
2. Reason about WAL ordering and commit points.
3. Hand-trace lookup across memtable and sorted tables.
4. Write compaction invariants and a recovery table for interruption at each write stage.

**Ready when:** controlled failures prove exactly which acknowledged writes survive.

## S13 — AI Infrastructure (Systems Lens)

### Labs

1. **Inference-gateway simulator.** Build a local simulator with bounded batching/queues that emits queue time, batch size, throughput, memory estimate, errors, and tail latency.
2. **Trade-off experiment.** Vary one control—batch window, maximum batch, concurrency, cache, or model size—and explain throughput/latency/cost effects. Label simulator results honestly.

### Exercises

1. Calculate service/arrival-rate scenarios and identify overload.
2. Design a metrics schema for queueing and inference.
3. Write an admission-control policy and rejection response.
4. Diagnose supplied p50/p95/p99 traces and propose a capacity/rollback threshold.

**Ready when:** you can connect a queueing/hardware cause to a measured service-level outcome.
