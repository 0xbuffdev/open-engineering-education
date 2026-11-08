## SYS7 — Performance Engineering & Observability

**Duration:** 5 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SYS3 and SYS4

### Overview

Develop a repeatable performance-engineering workflow using profiling, benchmarking, tracing, metrics, and controlled experiments. The goal is to replace intuition with evidence.

### Prerequisites

**SYS3 — Concurrency, Atomics & Memory Models**
**SYS4 — Linux Networking & Services**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Design reproducible benchmarks and control common measurement errors.
- Use profiling and tracing tools to locate expensive operations.
- Distinguish CPU, memory, I/O, synchronization, and network bottlenecks using evidence.
- Instrument a service with useful metrics and traces.
- Produce a technical performance report that connects a change to a measured result.


### Resource map

**Required**

- **B32** Ch. 2 (Methodologies), 4 (Observability Tools), 5 (Applications), 6 (CPUs), 12 (Benchmarking) and 13 (perf) — added: ZtP S9 recommends “a systems-performance book”.
- **B6** Ch. 7 and §8.3 · **B5** §10.7 and Ch. 12, 35, 36 · **R43** perf and tracing documentation — carried from ZtP S9.
- **B27** Ch. 5–8 · **R25** The Tail at Scale · **R41** The USE Method and CPU Flame Graphs.

### Modules

#### Module 1 — Profiling & Measurement

**Reading:** **B32** Ch. 5 (Applications), Ch. 6 (CPUs — profiling), Ch. 13 (perf). **R41** CPU Flame Graphs. **B6** Ch. 7 (Memory Performance Tools). **B5** §10.7 (Process Time), Ch. 36 (Process Resources). **R43** perf documentation.


### Module outcomes

By the end of this module, the learner can:

- Explain **Profiling and benchmark design** in the context of the course.
- Apply **Flame graphs and hotspot identification** in a problem, implementation, experiment, or design decision.

1. **Profiling and benchmark design**
   - kind: `lesson`
2. **Flame graphs and hotspot identification**
   - kind: `lesson`
3. **Checkpoint: profiling interpretation**
   - kind: `test`

4. **Micro-lab: Profile a real workload and identify its dominant cost.**
   - kind: `lab`
#### Module 2 — Observability Signals

**Reading:** **B27** Ch. 5 (Structured Events Are the Building Blocks of Observability), Ch. 6 (Stitching Events into Traces), Ch. 7 (Instrumentation with OpenTelemetry), Ch. 8 (Analyzing Events to Achieve Observability). **B32** Ch. 4 (Observability Tools). **B5** Ch. 12 (System and Process Information).


### Module outcomes

By the end of this module, the learner can:

- Explain **Tracing and metrics** in the context of the course.
- Apply **Correlating logs, traces, and measurements** in a problem, implementation, experiment, or design decision.

1. **Tracing and metrics**
   - kind: `lesson`
2. **Correlating logs, traces, and measurements**
   - kind: `lesson`
3. **Checkpoint: observability reasoning**
   - kind: `test`

4. **Micro-lab: Connect one user-visible slowdown to a trace segment and metric change.**
   - kind: `lab`
#### Module 3 — Latency, Throughput & Queues

**Reading:** **B32** Ch. 2 (Methodologies — latency, queueing, capacity planning). **R25** The Tail at Scale. **B26** Ch. 6 (Monitoring Distributed Systems — the four golden signals).


### Module outcomes

By the end of this module, the learner can:

- Explain **Tail latency and throughput** in the context of the course.
- Apply **Queueing effects and capacity reasoning** in a problem, implementation, experiment, or design decision.

1. **Tail latency and throughput**
   - kind: `lesson`
2. **Queueing effects and capacity reasoning**
   - kind: `lesson`
3. **Checkpoint: performance trade-offs**
   - kind: `test`

4. **Micro-lab: Measure how queue depth changes latency under load.**
   - kind: `lab`
#### Module 4 — Performance Investigation Method

**Reading:** **B32** Ch. 2 (Methodologies — USE method, workload characterization, drill-down analysis), Ch. 12 (Benchmarking). **R41** The USE Method. **B6** §8.3. **B5** Ch. 35 (Process Priorities and Scheduling).


### Module outcomes

By the end of this module, the learner can:

- Explain **Hypothesis-driven performance work** in the context of the course.
- Apply **Quantifying an improvement and checking regressions** in a problem, implementation, experiment, or design decision.

1. **Hypothesis-driven performance work**
   - kind: `lesson`
2. **Quantifying an improvement and checking regressions**
   - kind: `lesson`
3. **Checkpoint: evidence quality**
   - kind: `test`

4. **Micro-lab: Run a before/after experiment with controlled conditions.**
   - kind: `lab`
#### Module 5 — Performance Investigation

**Reading:** **B32** Ch. 16 (Case Study) and the chapter for the resource under investigation (Ch. 6 CPUs, 7 Memory, 8 File Systems, 9 Disks, 10 Network). **B6** Ch. 7.


1. **Investigate, improve, and quantify a real systems bottleneck**
   - kind: `lab`

### Topics

- profiling
- benchmarking
- flame graphs
- `perf`
- tracing
- metrics
- tail latency
- throughput
- queueing effects
- performance hypotheses
- capacity reasoning

### Labs

Every lab follows:

```text
baseline
→ hypothesis
→ measurement
→ change
→ measurement
→ explanation
```

### Substantial course lab

**Performance Investigation**

Take an earlier systems project, find a real bottleneck, prove it with measurements, improve it, and quantify the result.

---

