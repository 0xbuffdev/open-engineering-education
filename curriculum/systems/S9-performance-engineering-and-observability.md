# S9 — Performance Engineering & Observability

**Track:** Systems · **Prerequisite:** S4, S6 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P3/P4 performance investigations

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Performance work is applied evidence, not intuition. You will learn a repeatable method: define the question, establish a baseline, form a hypothesis, collect the cheapest useful evidence, change one variable, and report the result with limits.

## Outcomes

You can:

- use the USE method (utilization, saturation, errors) for a system;
- read `perf stat`, `perf record`, flame graphs, and traces;
- measure latency distributions (p50/p95/p99), throughput, and resource usage;
- distinguish CPU-, memory-, I/O-, lock-, and queueing-bound behaviour;
- build a reproducible benchmark with warm-up and noise control;
- write an investigation report with baseline, hypothesis, evidence, change, and result;
- add metrics, logs, and traces to a service;
- avoid the common traps of micro-benchmarks and vanity metrics.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B6 | Ch. **7**, §**8.3**, §§**7.4–7.5** | Memory performance tools, latency trends, branch prediction, page-fault optimization |
| B5 | §**10.7**, Ch. **12, 35–36** | Process time, `/proc`, scheduling, resource usage |
| *Systems Performance* (Brendan Gregg) | Ch. **1–5** | Method, observability tools, CPUs, memory, file systems |
| [perf wiki](https://perf.wiki.kernel.org/) | Tutorial and examples | Practical profiling |
| [BPF Performance Tools](https://www.brendangregg.com/bpf-performance-tools-book.html) | Selected chapters | Deep observability (optional) |

## Modules

### 1. Method

- question → metric → method → tool;
- baseline and control;
- one variable at a time;
- latency vs throughput;
- averages vs distributions;
- USE method;
- workload characterization;
- Amdahl's law and scalability;
- queueing theory basics (Little's law);
- measurement overhead and observer effect.

### 2. CPU

- cycles, instructions, IPC, frequency;
- user vs system vs idle;
- run queue, scheduling, context switches;
- `perf stat`, `perf top`, `perf record/report`;
- flame graphs;
- off-CPU analysis;
- CPU affinity and isolation.

### 3. Memory

- cache misses, TLB misses, page faults;
- bandwidth and latency;
- RSS/PSS/VSZ;
- `perf mem`, `perf c2c`;
- allocation profiling;
- NUMA effects (S8).

### 4. I/O and storage

- file system caches;
- block I/O, IOPS, throughput, queue depth;
- `iostat`, `iotop`, `blktrace`, `bpftrace`;
- fsync and durability costs;
- direct I/O;
- network I/O basics.

### 5. Observability

- metrics, logs, traces;
- structured logging;
- counters vs gauges vs histograms;
- p50/p95/p99 and tail latency;
- RED/USE dashboards;
- OpenTelemetry concepts;
- sampling and cardinality;
- alerting on symptoms, not causes.

### 6. Benchmarking

- micro vs macro benchmarks;
- warm-up, steady state, cooldown;
- input size and distribution;
- noise sources: frequency, thermal, other tenants, GC, JIT;
- statistical significance;
- reproducible scripts and environment capture.

## Labs

### Lab 1 — Ten investigations

Produce ten small investigations, each with:

- question and prediction;
- baseline;
- evidence (command output, graph, trace);
- one change;
- result and interpretation;
- limitation.

Suggested topics: CPU-bound loop, branch misprediction, cache miss, page fault, lock contention, syscall overhead, disk fsync, network round trip, thread oversubscription, memory allocation.

### Lab 2 — Flame graph

Profile a CPU-bound program with `perf record` and generate a flame graph. Identify the top stack and one actionable change. Repeat with an I/O-bound program using off-CPU analysis if available.

### Lab 3 — Service observability

Add to P4:

- request count, error count, duration histogram;
- queue depth and worker utilization;
- structured logs with request IDs;
- one trace or span;
- a dashboard or text summary;
- an alert condition.

### Lab 4 — Load test and tail latency

Run a load test at increasing concurrency. Plot throughput and p50/p95/p99. Identify the knee and explain it with queueing or a resource limit.

### Lab 5 — Fix a measured bottleneck

Take one bottleneck from an earlier lab, make one change, and measure again. If it did not improve, explain why and revert.

## Exercises

1. Apply USE to a Linux host and list three hypotheses.
2. Explain why average latency hides a problem.
3. Calculate Little's law for a queue.
4. Interpret a `perf stat` output with IPC and cache misses.
5. Read a flame graph and identify one leaf and one ancestor.
6. Explain the observer effect in tracing.
7. Design a benchmark for a CLI and a server.
8. Explain why p99 can be dominated by GC or scheduling.
9. Write an alert that detects a symptom, not a cause.
10. Explain one case where optimizing a component did not improve the system.

## Project increment — P3/P4 investigations

Add to P3/P4:

- a benchmark harness with environment capture;
- ten investigation reports;
- a dashboard/metrics endpoint;
- one fixed bottleneck with before/after evidence;
- a limitations section.

**Brief:** [P3 — cachebench](../projects/project-ladder.md#p3--cachebench) · [P4 — workbenchd](../projects/project-ladder.md#p4--workbenchd)

## Exit check

- [ ] produce a reproducible report that attributes a bottleneck to evidence, not intuition;
- [ ] read a flame graph and a latency distribution;
- [ ] distinguish CPU-, memory-, I/O-, lock-, and queue-bound behaviour;
- [ ] add metrics/logs/traces to a service;
- [ ] explain one failed optimization and why it failed;
- [ ] state the limits of your benchmark.

## Common failure modes

- Optimizing without a baseline.
- Changing several variables at once.
- Reporting averages only.
- Benchmarking on a noisy laptop and overclaiming.
- Confusing CPU utilization with saturation.
- Adding high-cardinality metrics that explode storage.
- Fixing a component that is not the bottleneck.

## Evidence to commit

- `labs/systems/S9/` with ten investigations, flame graphs, load test, report
- P3/P4 observability increment
- `notes/systems/S9/summary.md`

## Optional depth

- *Systems Performance* Ch. 6–12.
- *BPF Performance Tools* selected chapters.
- *The Art of Capacity Planning* (Allspaw).
- OpenTelemetry and Prometheus documentation.
