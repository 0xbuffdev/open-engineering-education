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


### Modules

#### Module 1 — Profiling & Measurement



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

