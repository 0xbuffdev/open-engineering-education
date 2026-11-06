# APP10 — Advanced Frontend Performance

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP2](APP2.md), [APP6](APP6.md)
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Investigate the performance of real browser applications from network delivery to rendering, interactivity, and long-running sessions. Use repeatable measurements, not benchmark anecdotes, to prioritize improvements while preserving accessibility and correct behavior.

This is an optional specialization. It is not required to complete APP9 or graduate from Application Engineering.

## Learning outcomes

By the end of this course, the learner will be able to:

- Profile loading, rendering, responsiveness and memory behavior with reproducible browser measurements.
- Explain the browser rendering pipeline and diagnose layout, script and main-thread bottlenecks.
- Optimize bundles, assets, cache behavior and delivery without compromising correctness.
- Design responsive interactions that remain usable under constrained CPU and network conditions.
- Compare before-and-after results, detect regressions and justify performance trade-offs.

## Modules

### Module 1 — Browser Rendering & Runtime

#### Outcomes

- Explain DOM, CSSOM, style, layout, paint, composition and main-thread work.
- Identify forced layout and long tasks in a browser trace.

#### Lessons

1. **Course introduction: Advanced Frontend Performance** — `lesson`

   Investigate the performance of real browser applications from network delivery to rendering, interactivity, and long-running sessions. Use repeatable measurements, not benchmark anecdotes, to prioritize improvements while preserving accessibility and correct behavior.
2. **Rendering pipeline and scheduling** — `lesson`
3. **JavaScript tasks, layout and painting** — `lesson`
4. **Browser trace interpretation** — `test`
5. **Trace a costly render** — `lab`

### Module 2 — Measurement & Budgets

#### Outcomes

- Distinguish laboratory from field measurements and control test conditions.
- Design a meaningful performance budget tied to a user workflow.

#### Lessons

1. **User-centered loading and responsiveness metrics** — `lesson`
2. **Profiling methodology and measurement variance** — `lesson`
3. **Interpreting performance data** — `test`
4. **Benchmark an interaction** — `lab`

### Module 3 — Assets, Delivery & Caching

#### Outcomes

- Explain how bundles, media, HTTP caching and critical resources affect delivery.
- Choose loading and caching strategies that avoid stale or broken content.

#### Lessons

1. **Resource prioritization and bundling** — `lesson`
2. **Image, font and cache strategy** — `lesson`
3. **Asset delivery trade-offs** — `test`
4. **Optimize the critical path** — `lab`

### Module 4 — Interactive Performance & Regression

#### Outcomes

- Identify wasted rendering, expensive computations and memory retention.
- Protect accessible behavior and establish automated regression gates.

#### Lessons

1. **State-driven rendering and scheduling** — `lesson`
2. **Memory analysis, accessibility and regression gates** — `lesson`
3. **Diagnosing slow interactions** — `test`
4. **Repair an interaction bottleneck** — `lab`

### Module 5 — Measured Frontend Performance Upgrade

#### Outcomes

- Integrate the elective's techniques in a demonstrable application change or complete system.
- Evaluate correctness, operational limitations, and engineering trade-offs from repeatable evidence.

#### Lessons

1. **Measured Frontend Performance Upgrade** — `lab`

## Completion requirements

- Complete the module checkpoints and all listed practical exercises, then complete the final integration lab.
- State tools, versions, runtime assumptions and test data so another learner can reproduce the work.
- Retain artifacts, test results, design decisions, evidence of at least one investigated failure and a technical retrospective according to [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required module checkpoints and exercises:**

- **Module 1 — Browser Rendering & Runtime:** Pass `Browser trace interpretation` by explaining and applying the module outcomes; perform the `Trace a costly render` lab: Capture a performance trace of a deliberately slow interface, identify a long task and explain its cause. Retain A trace, annotated timeline and reproduction steps.
- **Module 2 — Measurement & Budgets:** Pass `Interpreting performance data` by explaining and applying the module outcomes; perform the `Benchmark an interaction` lab: Run repeated tests under a documented device/network profile, summarize variation and set a justified budget. Retain A baseline table, test profile and budget rationale.
- **Module 3 — Assets, Delivery & Caching:** Pass `Asset delivery trade-offs` by explaining and applying the module outcomes; perform the `Optimize the critical path` lab: Compare a baseline and optimized build using a waterfall, document bytes and requests changed and check cache invalidation. Retain Waterfall captures and a verified asset update.
- **Module 4 — Interactive Performance & Regression:** Pass `Diagnosing slow interactions` by explaining and applying the module outcomes; perform the `Repair an interaction bottleneck` lab: Reproduce a slow interaction, fix it, run functional/accessibility checks, and record remaining limitations. Retain Reproduction, trace comparison, tests and trade-off note.

**Final integration lab — Measured Frontend Performance Upgrade:**

Improve a representative frontend from APP2 or a comparable accessible application. Establish a reproducible baseline, diagnose the dominant bottleneck, implement a justified change and evaluate loading and interaction performance under the same constraints.

**Success criteria:**

- Provide repeatable baseline and post-change measurements with the test environment disclosed.
- Demonstrate a causal connection between the diagnosed bottleneck and the implemented optimization.
- Preserve functional correctness, keyboard access and understandable loading/error states.
- Document at least one trade-off, residual bottleneck and a regression-detection plan.

**Evidence to retain:**

- A version-controlled implementation, configuration and exact steps for reproduction.
- Input/workload data and automated tests or repeatable manual verification records.
- Observed results, rejected alternatives, important design decisions and a technical retrospective.

**Failure analysis:**

Investigate noisy benchmarks, warm-cache effects, layout shifts introduced by optimization, or a change that improves a metric while damaging usability.

**Exit demonstration:**

Demonstrate the working implementation, explain the relevant mechanisms, reproduce at least one failure and repair, and defend the chosen trade-offs using retained evidence.
