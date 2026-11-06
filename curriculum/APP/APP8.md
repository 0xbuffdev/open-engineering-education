# APP8 — Production Application Architecture

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP5](APP5.md), [APP6](APP6.md), [APP7](APP7.md)
**Duration:** 9 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Learn how production applications evolve when traffic, data, dependencies, and failure modes increase. The course emphasizes architectural trade-offs driven by measurements rather than technology fashion.

## Learning outcomes

By the end of this course, the learner will be able to:

- Identify application bottlenecks using measurements and load tests.
- Select appropriate caching, queues, workers, and rate-limiting strategies.
- Design for idempotency, resilience, graceful degradation, and controlled failure.
- Estimate capacity and define useful performance or availability targets.
- Evaluate cost, complexity, and technical-debt trade-offs when evolving an application.
- Implement and defend an evidence-based production architecture change.
- Design representative load tests and explain tail latency, saturation and measurement uncertainty.
- Choose data scaling and consistency strategies under concurrency, migration and replica lag constraints.
- Contain cascading dependency failures using bounded timeouts, retries, isolation and correct fallback behavior.
- Stage a reversible application architecture change and justify its complexity and cost with measured evidence.

## Modules

### Module 1 — Scaling Models & Bottlenecks

#### Outcomes

- Explain **Scaling up, out, and by partitioning work** in the context of the course.
- Apply **Capacity planning and performance budgets** in a problem, implementation, experiment, or design decision.

- Identify limiting resources through measurable throughput, concurrency and latency behavior.

#### Lessons

1. **Course introduction: Production Application Architecture** — `lesson`

   Learn how production applications evolve when traffic, data, dependencies, and failure modes increase. The course emphasizes architectural trade-offs driven by measurements rather than technology fashion.
2. **Scaling up, out, and by partitioning work** — `lesson`
3. **Capacity planning and performance budgets** — `lesson`
4. **Queueing effects, tail latency and saturation** — `lesson`
5. **Capacity estimates and realistic workload models** — `lesson`
6. **Horizontal versus vertical scaling bottlenecks** — `lesson`
7. **scaling choices** — `test`
8. **Estimate capacity from a stated workload and verify one assumption** — `lab`

### Module 2 — Queues, Workers & Rate Limits

#### Outcomes

- Explain **Queues, workers, and burst absorption** in the context of the course.
- Apply **Rate limiting and overload control** in a problem, implementation, experiment, or design decision.

- Protect users and dependencies from overload using bounded queue and admission policies.

#### Lessons

1. **Queues, workers, and burst absorption** — `lesson`
2. **Rate limiting and overload control** — `lesson`
3. **Worker concurrency and bounded queues** — `lesson`
4. **Fair scheduling, quotas and throttling** — `lesson`
5. **Deadlines, backpressure and overload behavior** — `lesson`
6. **protecting a system under load** — `test`
7. **Introduce a bounded queue or rate limiter and measure its effect** — `lab`

### Module 3 — Caching & Idempotency

#### Outcomes

- Explain **Caching strategies and invalidation trade-offs** in the context of the course.
- Apply **Idempotency and application-level concurrency** in a problem, implementation, experiment, or design decision.

- Keep application data correct under caching, retries and concurrent operations.

#### Lessons

1. **Caching strategies and invalidation trade-offs** — `lesson`
2. **Idempotency and application-level concurrency** — `lesson`
3. **Cache stampedes and key design** — `lesson`
4. **Idempotency scopes, TTLs and retries** — `lesson`
5. **Concurrent state updates and ordering** — `lesson`
6. **consistency under retries** — `test`
7. **Make a retried operation safe to repeat** — `lab`

### Module 4 — Resilience & Evolution

#### Outcomes

- Explain **Resilience patterns and graceful failure** in the context of the course.
- Apply **Technical debt, architecture evolution, and cost/performance trade-offs** in a problem, implementation, experiment, or design decision.

- Evolve application boundaries under measured constraints while retaining operational recovery options.

#### Lessons

1. **Resilience patterns and graceful failure** — `lesson`
2. **Technical debt, architecture evolution, and cost/performance trade-offs** — `lesson`
3. **Circuit breakers, timeouts and partial degradation** — `lesson`
4. **Release flags and reversible architectural migrations** — `lesson`
5. **Quantified costs and architecture decision records** — `lesson`
6. **architecture trade-offs** — `test`
7. **Redesign one boundary under a stated growth constraint** — `lab`

### Module 5 — Performance Modeling & Load Test Design

#### Outcomes

- Design a representative load test and identify measurement bias.
- Explain observed service saturation through resource and queueing data.

#### Lessons

1. **Workload characterization and arrival patterns** — `lesson`
2. **Tail latency and coordinated omission** — `lesson`
3. **Resource instrumentation and bottleneck localization** — `lesson`
4. **Capacity projections with uncertainty** — `lesson`
5. **Evaluating load-test validity** — `test`
6. **Investigate a throughput collapse** — `lab`

### Module 6 — Data-Intensive Application Boundaries

#### Outcomes

- Choose data scaling strategies without sacrificing required consistency guarantees.
- Define how client workflows behave under lag, contention or data migration.

#### Lessons

1. **Read/write amplification and database connection pools** — `lesson`
2. **Partitioning, read replicas and consistency trade-offs** — `lesson`
3. **Eventual consistency at application boundaries** — `lesson`
4. **Schema and data migration under active traffic** — `lesson`
5. **Data consistency and capacity decisions** — `test`
6. **Test replica lag and conflict handling** — `lab`

### Module 7 — Failure Containment & Availability

#### Outcomes

- Bound cross-service failure propagation with explicit timeouts and resource limits.
- Define usable degraded behavior consistent with application correctness.

#### Lessons

1. **Failure domains and dependency mapping** — `lesson`
2. **Timeout budgeting and retry amplification** — `lesson`
3. **Bulkheads, fallbacks and graceful service degradation** — `lesson`
4. **Operational experiments and rollback** — `lesson`
5. **Failure containment and retry behavior** — `test`
6. **Inject a cascading dependency failure** — `lab`

### Module 8 — Architecture Evolution, Governance & Economics

#### Outcomes

- Plan an incremental architecture change supported by measurable objectives.
- Defend a design against its complexity, maintenance and financial cost.

#### Lessons

1. **Strangler migrations and reversible feature boundaries** — `lesson`
2. **Architecture decision records and deprecation** — `lesson`
3. **Operational cost and ownership trade-offs** — `lesson`
4. **Build-versus-buy and service consolidation** — `lesson`
5. **Architecture alternatives under constraints** — `test`
6. **Stage a reversible architecture migration** — `lab`

### Module 9 — Production Architecture Review

#### Outcomes

- Complete and explain the Production Architecture Review lab, demonstrating the applicable course outcomes and retaining required evidence.

#### Lessons

1. **Measure, redesign, implement, and document the Production Architecture Review** — `lab`

## Completion requirements

- Complete the required practical exercises, knowledge checkpoints, and evaluated labs described in the modules.
- Complete the final integrated `lab` in the last module and satisfy its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, failures investigated, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required practical exercises:**

- load-test an endpoint
- introduce a queue to absorb burst traffic
- add rate limiting
- compare cache strategies
- design for a stated availability/performance target
**Final integration lab — required work:**

Required artifact: **Production Architecture Review**.

Take the deployed APP7 product through a realistic growth or failure scenario. Measure its bottleneck, redesign one architectural boundary, implement the change and document the trade-offs.

**Expanded module assessments and practical work:**

- **Module 1 checkpoint and micro-lab:** Explain p50/p95/p99 latency and saturation measurements under a repeatable load pattern.
- **Module 2 checkpoint and micro-lab:** Demonstrate that queues do not grow without bound and shed or delay excess work predictably.
- **Module 3 checkpoint and micro-lab:** Reproduce a duplicate-request or stale-cache failure and prove the selected mitigation.
- **Module 4 checkpoint and micro-lab:** Compare alternatives using latency, failure tolerance, change cost and rollback feasibility.

- **Module 5 — Performance Modeling & Load Test Design (Investigate a throughput collapse):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Build a workload profile, capture latency percentiles and resource saturation, and correct one demonstrable bottleneck.
  - Verification: Compare repeatable pre/post traces and identify both the client and server bottlenecks.
  - Evidence: Load script, test environment and utilization/latency tables.
  - Failure analysis: Explain cache warming, coordinated omission and synthetic load not matching real arrivals.
- **Module 6 — Data-Intensive Application Boundaries (Test replica lag and conflict handling):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Use a controllable data-store simulation or two-phase pipeline to create delayed reads; demonstrate how the application communicates and recovers.
  - Verification: Prove no unauthorized stale state is exposed and that operations with strong consistency requirements remain protected.
  - Evidence: Consistency model, trace and correctness tests.
  - Failure analysis: Explain stale reads, migration locks and unsafe reliance on replicas for critical writes.
- **Module 7 — Failure Containment & Availability (Inject a cascading dependency failure):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Introduce a slow or failing upstream service under load, observe cascading symptoms, and contain the failure with bounded retries or isolation.
  - Verification: Show recovered request latency and throughput limits with an explicit fallback correctness condition.
  - Evidence: Fault-injection setup, traces, metrics and resilience decision.
  - Failure analysis: Distinguish failed closed versus failed open and account for shared resource contention.
- **Module 8 — Architecture Evolution, Governance & Economics (Stage a reversible architecture migration):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Prototype two approaches to a measurable bottleneck, roll out the selected boundary behind a safe switch and rehearse its rollback.
  - Verification: Show compatible interfaces, observed performance and documented migration/rollback steps.
  - Evidence: ADRs, diagrams, measurements and rollback record.
  - Failure analysis: Explain over-engineering, stale dependencies and production costs hidden by prototypes.

**Exit assessment expectation:**

Demonstrate the relevant course outcomes on an unfamiliar scenario, including failure behavior and independently reproducible evidence. Checkpoint responses must explain mechanisms; every final lab or project must integrate and verify the expanded material.

**Exit demonstration:**

The learner can choose a scaling strategy from measured constraints rather than defaulting to more services or more hardware.

---
