# APP8 — Production Application Architecture

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP5](APP5.md), [APP6](APP6.md), [APP7](APP7.md)
**Duration:** 5 weeks
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

## Modules

### Module 1 — Scaling Models & Bottlenecks

#### Outcomes

- Explain **Scaling up, out, and by partitioning work** in the context of the course.
- Apply **Capacity planning and performance budgets** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Course introduction: Production Application Architecture** — `lesson`

   Learn how production applications evolve when traffic, data, dependencies, and failure modes increase. The course emphasizes architectural trade-offs driven by measurements rather than technology fashion.
2. **Scaling up, out, and by partitioning work** — `lesson`
3. **Capacity planning and performance budgets** — `lesson`
4. **scaling choices** — `test`
5. **Estimate capacity from a stated workload and verify one assumption** — `lab`

### Module 2 — Queues, Workers & Rate Limits

#### Outcomes

- Explain **Queues, workers, and burst absorption** in the context of the course.
- Apply **Rate limiting and overload control** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Queues, workers, and burst absorption** — `lesson`
2. **Rate limiting and overload control** — `lesson`
3. **protecting a system under load** — `test`
4. **Introduce a bounded queue or rate limiter and measure its effect** — `lab`

### Module 3 — Caching & Idempotency

#### Outcomes

- Explain **Caching strategies and invalidation trade-offs** in the context of the course.
- Apply **Idempotency and application-level concurrency** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Caching strategies and invalidation trade-offs** — `lesson`
2. **Idempotency and application-level concurrency** — `lesson`
3. **consistency under retries** — `test`
4. **Make a retried operation safe to repeat** — `lab`

### Module 4 — Resilience & Evolution

#### Outcomes

- Explain **Resilience patterns and graceful failure** in the context of the course.
- Apply **Technical debt, architecture evolution, and cost/performance trade-offs** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Resilience patterns and graceful failure** — `lesson`
2. **Technical debt, architecture evolution, and cost/performance trade-offs** — `lesson`
3. **architecture trade-offs** — `test`
4. **Redesign one boundary under a stated growth constraint** — `lab`

### Module 5 — Production Architecture Review

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

**Exit demonstration:**

The learner can choose a scaling strategy from measured constraints rather than defaulting to more services or more hardware.

---
