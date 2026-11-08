# SYS7 — Performance Engineering & Observability

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** SYS3 and SYS4 *(legacy mapping; reconcile before activation)*
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SYS.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Develop a repeatable performance-engineering workflow using profiling, benchmarking, tracing, metrics, and controlled experiments. The goal is to replace intuition with evidence.

## Learning outcomes

- Design reproducible benchmarks and control common measurement errors.
- Use profiling and tracing tools to locate expensive operations.
- Distinguish CPU, memory, I/O, synchronization, and network bottlenecks using evidence.
- Instrument a service with useful metrics and traces.
- Produce a technical performance report that connects a change to a measured result.

## Modules

### Module 1 — Profiling & Measurement

#### Outcomes

By the end of this module, the learner can:

- Explain **Profiling and benchmark design** in the context of the course.
- Apply **Flame graphs and hotspot identification** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Profiling and benchmark design** — `lesson`
2. **Flame graphs and hotspot identification** — `lesson`
3. **Checkpoint: profiling interpretation** — `test`
4. **Micro-lab: Profile a real workload and identify its dominant cost.** — `lab`

### Module 2 — Observability Signals

#### Outcomes

By the end of this module, the learner can:

- Explain **Tracing and metrics** in the context of the course.
- Apply **Correlating logs, traces, and measurements** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Tracing and metrics** — `lesson`
2. **Correlating logs, traces, and measurements** — `lesson`
3. **Checkpoint: observability reasoning** — `test`
4. **Micro-lab: Connect one user-visible slowdown to a trace segment and metric change.** — `lab`

### Module 3 — Latency, Throughput & Queues

#### Outcomes

By the end of this module, the learner can:

- Explain **Tail latency and throughput** in the context of the course.
- Apply **Queueing effects and capacity reasoning** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Tail latency and throughput** — `lesson`
2. **Queueing effects and capacity reasoning** — `lesson`
3. **Checkpoint: performance trade-offs** — `test`
4. **Micro-lab: Measure how queue depth changes latency under load.** — `lab`

### Module 4 — Performance Investigation Method

#### Outcomes

By the end of this module, the learner can:

- Explain **Hypothesis-driven performance work** in the context of the course.
- Apply **Quantifying an improvement and checking regressions** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Hypothesis-driven performance work** — `lesson`
2. **Quantifying an improvement and checking regressions** — `lesson`
3. **Checkpoint: evidence quality** — `test`
4. **Micro-lab: Run a before/after experiment with controlled conditions.** — `lab`

### Module 5 — Performance Investigation

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Investigate, improve, and quantify a real systems bottleneck** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

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
