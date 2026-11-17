# SYS7 — Performance Engineering & Observability

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS3](SYS3.md), [SYS4](SYS4.md)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

Advance SYS1's introductory machine-performance experiments into an end-to-end **systems performance investigation**. SYS3 supplies contention models and SYS4 supplies realistic concurrent service behavior. Learn workload design, CPU/off-CPU profiling, queueing analysis, tail latency, observability, controlled interventions and defensible reporting. The outcome is not a mandatory speedup: valid evidence may show that the hypothesis was wrong or optimization is harmful. Use local synthetic data, open-source profilers or portable instrumentation; privileged perf events, commercial tracing platforms and production customer traffic are not required. All performance and capacity statements remain bounded to the measured conditions.

## Learning outcomes

- **SYS7-O1:** Define a falsifiable performance question and distinguish symptoms, candidate causes and independent measurements.
- **SYS7-O2:** Design correct, reproducible throughput and latency benchmarks with warmup, controls, repetitions, variability and workload realism.
- **SYS7-O3:** Interpret CPU profiles, call stacks and flame graphs with sampling and inlining limitations.
- **SYS7-O4:** Investigate blocked/off-CPU time, I/O, lock contention, memory pressure and event-loop scheduling using suitable evidence.
- **SYS7-O5:** Design service metrics, structured logs and distributed or local traces with cardinality, correlation and privacy constraints.
- **SYS7-O6:** Explain queues, utilization, Little's Law and capacity bottlenecks while identifying assumptions of the chosen model.
- **SYS7-O7:** Analyze percentile/tail latency, coordinated omission and queue-induced collapse without confusing percentiles with averages.
- **SYS7-O8:** Correlate load, resource saturation, errors and traces to discriminate CPU, memory, storage, network and synchronization constraints.
- **SYS7-O9:** Perform safe workload and fault experiments on bounded local services, including a controlled negative or invalid hypothesis.
- **SYS7-O10:** Evaluate a proposed optimization against correctness, repeatability, implementation cost and regression risk.
- **SYS7-O11:** Write an independent performance report with inspectable data, uncertainty, alternative explanations and no unsupported generalization.
- **SYS7-O12:** Defend an unfamiliar bottleneck investigation and revise the experiment or implementation when new evidence contradicts the first diagnosis.

## Modules

### Module 1 — Scientific Performance Engineering

#### Outcomes

- SYS7-O1
- SYS7-O2
- SYS7-O10
- SYS7-O11

#### Lessons

1. **Evidence versus intuition** — Separate observed slowdown, hypothesis, test intervention and causal claim.
2. **Historical measurement traps** — Discuss optimized-away work, clock precision, noisy neighbors and benchmark-driven overfitting.
3. **Correctness invariants** — Specify output oracle and admissible resource budget before timing variants.
4. **Warm and cold regimes** — Distinguish startup, cache-warm, steady-state and recovery behavior.
5. **Repeatability** — Record toolchain, kernels, seeds, sample count, distribution and plausible confounders.
6. **Intervention design** — Change one meaningful factor or disclose interactions and uncertainty.
7. **Unfamiliar input** — Test whether the claimed gain transfers outside the calibration workload.

### Module 2 — Profiling and Execution Attribution

#### Outcomes

- SYS7-O3
- SYS7-O4
- SYS7-O8

#### Lessons

1. **Sampling and instrumentation** — Contrast timer-based samples with event tracing and their costs.
2. **Call stacks and inlining** — Interpret stacks, optimized code and missing symbols without inventing a precise total.
3. **CPU flame graphs** — Identify inclusive cost and compare workloads, not color or width as absolute speed proof.
4. **Off-CPU wait states** — Investigate blocking syscalls, mutex waits and run-queue delay with accessible tools.
5. **Cache and allocator pressure** — Relate allocation counts, page faults and hardware counters to bounded symptoms.
6. **perf access limits** — Use perf when permissions permit, otherwise language-level timing or trace probes with documented limitations.

### Module 3 — Production Signals and Trace Correlation

#### Outcomes

- SYS7-O5
- SYS7-O8
- SYS7-O11

#### Lessons

1. **Metrics taxonomy** — Choose requests, errors, duration, saturation and queue-depth measures for explicit decisions.
2. **Instrumentation cost** — Bound cardinality, sampling rates, collection memory and correlation ID lifetimes.
3. **Structured logs** — Create privacy-safe context without logging payload secrets or unverifiable causes.
4. **Span and request timelines** — Correlate wait, run, I/O and downstream operations for one representative request.
5. **Tracing limits** — Explain sampling loss, missing causal links and timestamp skew in multi-process settings.
6. **Operational visibility** — Design a small dashboard/table that can distinguish overload from correctness errors.

### Module 4 — Queues, Tail Latency and Capacity

#### Outcomes

- SYS7-O6
- SYS7-O7
- SYS7-O8

#### Lessons

1. **Workload arrival and service** — Model arrival rate, service time, queue length and saturation assumptions.
2. **Little's Law** — Calculate L = lambda W and identify nonstationary cases where the simple model misleads.
3. **Utilization and waiting** — Demonstrate queue growth approaching a bottleneck using local workload.
4. **Mean versus percentiles** — Show p50, p95 and p99 from actual distributions without meaningless interpolation claims.
5. **Coordinated omission** — Design load generators that do not hide stalled response-time exposure.
6. **Bounded admission** — Compare queueing, rejection and backpressure policies using service-level effects.
7. **Capacity uncertainty** — State why one local machine's ceiling does not establish a production throughput guarantee.

### Module 5 — Cross-Layer Diagnostic Experiments

#### Outcomes

- SYS7-O4
- SYS7-O8
- SYS7-O9
- SYS7-O12

#### Lessons

1. **CPU saturation** — Contrast busy-work and runnable starvation with queue traces.
2. **Memory capacity** — Measure allocation bursts, paging and working-set change without unsafe OOM tests.
3. **Storage and network wait** — Separate disk flush, socket backpressure and other I/O delay.
4. **Synchronization contention** — Reuse SYS3 lock models and measure time in waiting paths.
5. **Failure and overload** — Inject slow handlers, timeout and bounded queue exhaustion in a local service.
6. **Discriminating evidence** — Design a second observation that could invalidate the leading hypothesis.

### Module 6 — Optimization and Regression Decisions

#### Outcomes

- SYS7-O2
- SYS7-O9
- SYS7-O10
- SYS7-O11

#### Lessons

1. **Optimization contract** — State what correctness and resource invariants may not change.
2. **Comparable before/after** — Use equivalent work, build flags, measurement conditions and test coverage.
3. **Effect and variability** — Report individual samples, confidence caveats and effect sizes rather than cherry-picked minima.
4. **Cost of optimization** — Account for complexity, memory, portability, energy and failure-mode consequences.
5. **Regression guard** — Add a practical benchmark or traced threshold check with stated statistical limits.
6. **Negative result** — Explain why a plausible intervention failed or improved the wrong metric.

### Module 7 — Performance Investigation Defense

#### Outcomes

- SYS7-O1
- SYS7-O3
- SYS7-O5
- SYS7-O7
- SYS7-O10
- SYS7-O11
- SYS7-O12

#### Lessons

1. **Select a SYS artifact** — Use a concurrent or network service from earlier work or a public synthetic fixture.
2. **Baseline and profiling** — Reproduce a user-visible issue and gather cost and latency signals.
3. **Cause and repair** — Propose two hypotheses, reject at least one, implement or decline an optimization.
4. **Decision report** — Present data, uncertainty, SLO/capacity effect and remaining risk.
5. **Independent challenge** — React to new workload evidence and defend revised conclusions.

## Completion requirements

The following work is summative. Measurements made during lessons are formative unless supplied as part of the identified required evidence; no automatic credit is awarded for an arbitrary percentage improvement.

- **SYS7-AS1** — Experimental Design and Baselines
  - **Outcomes:** SYS7-O1, SYS7-O2, SYS7-O6, SYS7-O7.
  - **Work:** Specify workloads, independently correct outputs and benchmark controls; calculate queue/capacity scenarios.
  - **Criteria:** Reproducible timing method; assumptions and math defensible; latency quantiles interpreted correctly with non-stationary cases disclosed.
  - **Evidence:** Harness, fixture, calculations, repeated samples and environment details.

- **SYS7-AS2** — CPU/Off-CPU Profiling Analysis
  - **Outcomes:** SYS7-O3, SYS7-O4, SYS7-O8.
  - **Work:** Identify competing bottlenecks in at least two profiling/wait traces or instrumented local fixtures.
  - **Criteria:** Correct attribution from evidence; distinguish sampling from complete trace; no unsupported exactness or privileged-tool dependency.
  - **Evidence:** Annotated profiles/traces, raw events, alternative explanations and tool constraints.

- **SYS7-AS3** — Service Signal and Capacity Instrumentation
  - **Outcomes:** SYS7-O5, SYS7-O6, SYS7-O7, SYS7-O8, SYS7-O9.
  - **Work:** Instrument one bounded service with privacy-safe metrics, logs and request traces under controlled load.
  - **Criteria:** Correlation reveals queue, latency, errors and saturation; no unbounded labels or secret leakage; overload response measured.
  - **Evidence:** Source, metrics schema, trace samples, load setup, negative privacy tests and observations.

- **SYS7-AS4** — Controlled Optimization Study
  - **Outcomes:** SYS7-O2, SYS7-O9, SYS7-O10, SYS7-O11.
  - **Work:** Reproduce a bottleneck and test one correction with a correctness oracle before and after.
  - **Criteria:** Statistically honest samples and workload controls; report negative/neutral results; operational cost and regression risk evaluated.
  - **Evidence:** Code revisions, test transcripts, samples, plots/table and reasoned decision.

- **SYS7-AS5** — Independent Performance Defense
  - **Outcomes:** SYS7-O1, SYS7-O3, SYS7-O4, SYS7-O8, SYS7-O11, SYS7-O12.
  - **Work:** Analyze a new performance anomaly inconsistent with the first hypothesis and revise measurement or design.
  - **Criteria:** Use a falsifiable discriminator, locate actual limiting operation and state remaining uncertainty and applicability.
  - **Evidence:** Challenge dataset, before/after diagnosis, profile/counter evidence, independent tests and defense.

### Measurement and privacy boundaries

Do not equate sampling count with complete execution, CPU time with wall-clock latency, average with tail, or microbenchmarks with whole-service behavior. On restricted Linux environments, equivalent user-space instrumentation may establish the outcomes if its limitations are stated. Avoid privileged probes, unbounded stress and private production telemetry. The goal is reasoned diagnosis, not universal tooling proficiency or unverifiable performance claims. SYS8 owns production design decisions after the investigation, and SYS9 integrates them.

### Evidence and course completion

Store baseline outputs, instrumented changes, reproducible workload generators, raw measurements, repeat counts, environment details and an analysis of confounders. Keep sensitive identifiers and payloads out of evidence. Assessment records identify version, outcome/assessment IDs, decision and appropriate result; a missing required diagnosis cannot be replaced by passing CI or report formatting. Legacy evidence is revision-scoped, and the course's educational status is `draft` until genuine learner/reviewer evidence exists.
