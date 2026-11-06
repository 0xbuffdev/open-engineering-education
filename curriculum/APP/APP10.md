# APP10 — Advanced Frontend Performance

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP2](APP2.md), [APP6](APP6.md)
**Duration:** 7 weeks
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
- Distinguish network delivery, rendering, scheduling and memory bottlenecks using repeatable traces.
- Tune complex interactions and asset loading with accessibility-safe performance measurements.
- Establish a performance regression gate with documented test variance and user-centered budgets.

## Modules

### Module 1 — Browser Rendering & Runtime

#### Outcomes

- Explain DOM, CSSOM, style, layout, paint, composition and main-thread work.
- Identify forced layout and long tasks in a browser trace.

- Map a slow interaction to concrete browser main-thread, rendering and compositing work.

#### Lessons

1. **Course introduction: Advanced Frontend Performance** — `lesson`

   Investigate the performance of real browser applications from network delivery to rendering, interactivity, and long-running sessions. Use repeatable measurements, not benchmark anecdotes, to prioritize improvements while preserving accessibility and correct behavior.
2. **Rendering pipeline and scheduling** — `lesson`
3. **JavaScript tasks, layout and painting** — `lesson`
4. **Task scheduling, microtasks, and animation frames** — `lesson`
5. **Style recalculation, layout invalidation, and containment** — `lesson`
6. **Compositing layers and GPU cost** — `lesson`
7. **Browser trace interpretation** — `test`
8. **Trace a costly render** — `lab`

### Module 2 — Measurement & Budgets

#### Outcomes

- Distinguish laboratory from field measurements and control test conditions.
- Design a meaningful performance budget tied to a user workflow.

- Select performance indicators that reflect user workflows and describe uncertainty.

#### Lessons

1. **User-centered loading and responsiveness metrics** — `lesson`
2. **Profiling methodology and measurement variance** — `lesson`
3. **Field measurements, attribution and sampling bias** — `lesson`
4. **Tail responsiveness and interaction latency** — `lesson`
5. **Benchmark reproducibility and workload representativeness** — `lesson`
6. **Interpreting performance data** — `test`
7. **Benchmark an interaction** — `lab`

### Module 3 — Assets, Delivery & Caching

#### Outcomes

- Explain how bundles, media, HTTP caching and critical resources affect delivery.
- Choose loading and caching strategies that avoid stale or broken content.

- Measure delivery strategies with correct network and cache behavior.

#### Lessons

1. **Resource prioritization and bundling** — `lesson`
2. **Image, font and cache strategy** — `lesson`
3. **Critical resource prioritization and preloading** — `lesson`
4. **Font, image and media loading choices** — `lesson`
5. **HTTP/2, caching boundaries and content compression** — `lesson`
6. **Asset delivery trade-offs** — `test`
7. **Optimize the critical path** — `lab`

### Module 4 — Interactive Performance & Regression

#### Outcomes

- Identify wasted rendering, expensive computations and memory retention.
- Protect accessible behavior and establish automated regression gates.

- Detect rendering waste and memory retention through repeatable profiling and regression checks.

#### Lessons

1. **State-driven rendering and scheduling** — `lesson`
2. **Memory analysis, accessibility and regression gates** — `lesson`
3. **Framework rendering ownership and render budgets** — `lesson`
4. **Memory heap snapshots and leak hypotheses** — `lesson`
5. **Frontend monitoring, privacy and alert selection** — `lesson`
6. **Diagnosing slow interactions** — `test`
7. **Repair an interaction bottleneck** — `lab`

### Module 5 — Network, Edge & Client Delivery

#### Outcomes

- Explain how network and edge delivery decisions influence browser performance and correctness.
- Design a safe update strategy that avoids stale assets and private-data caching.

#### Lessons

1. **CDN placement and cache key correctness** — `lesson`
2. **Resource hints, prioritization and streaming** — `lesson`
3. **HTTP caching invalidation under deployment** — `lesson`
4. **Service workers, offline behavior and update lifecycle** — `lesson`
5. **Delivery optimizations and cache correctness** — `test`
6. **Repair a stale or slow delivery path** — `lab`

### Module 6 — Complex Interaction & Memory Performance

#### Outcomes

- Improve interaction responsiveness in complex views with repeatable causal measurements.
- Prevent leaks and prove accessibility and functionality survive the optimization.

#### Lessons

1. **Large lists and virtualization trade-offs** — `lesson`
2. **Input latency, task yielding and worker boundaries** — `lesson`
3. **Expensive calculations, memoization and invalidation** — `lesson`
4. **Memory lifecycle, listeners and detached DOM nodes** — `lesson`
5. **Rendering under accessibility and reduced-motion constraints** — `lesson`
6. **Interaction and memory profiling** — `test`
7. **Recover responsiveness in a large-data interface** — `lab`

### Module 7 — Performance Governance & Continuous Verification

#### Outcomes

- Set defensible budgets and identify when changes degrade real interactions.
- Operate a performance review process that includes uncertainty, privacy and business trade-offs.

#### Lessons

1. **Choosing user-centered performance budgets** — `lesson`
2. **Automated smoke and regression measurement** — `lesson`
3. **Experiment design and variance reporting** — `lesson`
4. **Field telemetry privacy and sampling** — `lesson`
5. **Incident analysis for browser regressions** — `lesson`
6. **Benchmark validity and regression decisions** — `test`
7. **Add a performance release gate** — `lab`

### Module 8 — Measured Frontend Performance Upgrade

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

**Expanded module assessment and lab requirements:**

- **Module 1 checkpoint and micro-lab:** Use a browser trace to distinguish scripting, layout, paint, and compositing costs; validate the hypothesis with a targeted change.
- **Module 2 checkpoint and micro-lab:** Collect multiple comparable runs and explain warmup, cache state and device conditions.
- **Module 3 checkpoint and micro-lab:** Prove an optimization reduces a specified bottleneck without invalidating cache behavior or causing visual instability.
- **Module 4 checkpoint and micro-lab:** Demonstrate the optimized workflow with both functional and accessibility regressions excluded.

- **Module 5 — Network, Edge & Client Delivery (Repair a stale or slow delivery path):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Measure cold/warm loads through a controlled cache, introduce an asset version change and ensure the deployed page remains consistent.
  - Verification: Show waterfall improvements and correct invalidation without serving protected content from a shared cache.
  - Evidence: Versioned assets, cache headers, load traces and update tests.
  - Failure analysis: Identify cache poisoning, opaque stale service-worker assets and misleading CDN benchmarks.
- **Module 6 — Complex Interaction & Memory Performance (Recover responsiveness in a large-data interface):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Exercise a large list, background operation and form submission while recording task latency and heap behavior; choose a bounded fix.
  - Verification: The fixed flow meets a documented responsiveness budget, avoids unbounded memory growth and retains correct keyboard/screen-reader behavior.
  - Evidence: Profiler output, heap samples, tests and constraints.
  - Failure analysis: Discuss virtualization focus traps, premature memoization and measurement under different device loads.
- **Module 7 — Performance Governance & Continuous Verification (Add a performance release gate):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Establish a performance budget in CI or a reproducible local harness; inject a slow change to verify its detection.
  - Verification: A failing regression is detected and a corrected build passes with recorded thresholds and test conditions.
  - Evidence: Harness configuration, run history, policy rationale and false-positive notes.
  - Failure analysis: Explain flaky metrics, sampling bias, inconsistent test machines and overfitting benchmarks.

**Exit assessment expectation:**

Demonstrate the subject outcomes on an unfamiliar example, show at least one negative path and retain evidence allowing another reviewer to reproduce the result. Checkpoint answers must explain mechanisms, while the final integration lab must integrate and verify the expanded topics.

**Exit demonstration:**

Demonstrate the working implementation, explain the relevant mechanisms, reproduce at least one failure and repair, and defend the chosen trade-offs using retained evidence.
