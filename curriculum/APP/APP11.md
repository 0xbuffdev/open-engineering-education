# APP11 — Advanced Backend Architecture

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP3](APP3.md), [APP4](APP4.md), [APP6](APP6.md)
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Design backend systems whose boundaries withstand changing requirements, concurrent traffic and partial failure. Compare modular monoliths and service boundaries through real experiments, emphasizing data consistency, operability and the cost of distributed complexity.

This is an optional specialization. It is not required to complete APP9 or graduate from Application Engineering.

## Learning outcomes

By the end of this course, the learner will be able to:

- Define service and domain boundaries using business invariants and change patterns.
- Compare modular monolith and distributed-service designs against measured constraints.
- Implement resilient asynchronous workflows with explicit consistency and retry semantics.
- Diagnose contention, overload and partial dependency failures.
- Document architectural decisions, migrations and operational consequences.

## Modules

### Module 1 — Domain & Module Boundaries

#### Outcomes

- Identify invariants, use cases and ownership boundaries in an application domain.
- Use dependency direction and contract tests to protect modules.

#### Lessons

1. **Course introduction: Advanced Backend Architecture** — `lesson`

   Design backend systems whose boundaries withstand changing requirements, concurrent traffic and partial failure. Compare modular monoliths and service boundaries through real experiments, emphasizing data consistency, operability and the cost of distributed complexity.
2. **Domain boundaries and aggregate invariants** — `lesson`
3. **Ports, adapters and modular contracts** — `lesson`
4. **Choosing module boundaries** — `test`
5. **Separate a tangled service** — `lab`

### Module 2 — Data & Transaction Architecture

#### Outcomes

- Choose transaction boundaries with explicit consistency guarantees.
- Explain read models, outbox patterns and competing-write behavior.

#### Lessons

1. **Consistency and transaction ownership** — `lesson`
2. **Events, outboxes and read models** — `lesson`
3. **Reasoning about consistency** — `test`
4. **Implement a reliable event handoff** — `lab`

### Module 3 — Services & Async Coordination

#### Outcomes

- Assess when a service split helps or harms deployment and ownership.
- Handle retries, ordering, deadlines and duplicate messages safely.

#### Lessons

1. **Service extraction and contract evolution** — `lesson`
2. **Workers, queues and idempotent consumers** — `lesson`
3. **Service boundary decisions** — `test`
4. **Exercise a queue-based workflow** — `lab`

### Module 4 — Operability & Evolution

#### Outcomes

- Analyze bottlenecks and failure containment at subsystem boundaries.
- Plan an incremental migration with rollback and observability.

#### Lessons

1. **Bulkheads, timeouts and backpressure** — `lesson`
2. **Evolutionary migration and decision records** — `lesson`
3. **Reviewing architecture trade-offs** — `test`
4. **Run a failure injection** — `lab`

### Module 5 — Resilient Backend Architecture Review

#### Outcomes

- Integrate the elective's techniques in a demonstrable application change or complete system.
- Evaluate correctness, operational limitations, and engineering trade-offs from repeatable evidence.

#### Lessons

1. **Resilient Backend Architecture Review** — `lab`

## Completion requirements

- Complete the module checkpoints and all listed practical exercises, then complete the final integration lab.
- State tools, versions, runtime assumptions and test data so another learner can reproduce the work.
- Retain artifacts, test results, design decisions, evidence of at least one investigated failure and a technical retrospective according to [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required module checkpoints and exercises:**

- **Module 1 — Domain & Module Boundaries:** Pass `Choosing module boundaries` by explaining and applying the module outcomes; perform the `Separate a tangled service` lab: Refactor a coupled endpoint into tested application and infrastructure boundaries without changing its external API. Retain Architecture diagram, contract tests and unchanged API responses.
- **Module 2 — Data & Transaction Architecture:** Pass `Reasoning about consistency` by explaining and applying the module outcomes; perform the `Implement a reliable event handoff` lab: Use a transactional outbox or equivalent recoverable handoff and demonstrate a crash/retry scenario. Retain Database state, event log, test for duplicate delivery.
- **Module 3 — Services & Async Coordination:** Pass `Service boundary decisions` by explaining and applying the module outcomes; perform the `Exercise a queue-based workflow` lab: Build a bounded worker and demonstrate duplicate messages, poison events and recovery. Retain Worker traces and replayable failure tests.
- **Module 4 — Operability & Evolution:** Pass `Reviewing architecture trade-offs` by explaining and applying the module outcomes; perform the `Run a failure injection` lab: Inject slow or unavailable dependencies, record user-visible impact and revise timeouts or boundaries. Retain Load traces, incident note and rollback plan.

**Final integration lab — Resilient Backend Architecture Review:**

Extend a functioning backend with a changed scale or reliability requirement. Compare two credible architectural options, implement the lower-risk improvement and demonstrate transaction correctness, retry safety, operability and a migration/rollback path.

**Success criteria:**

- Explain the domain invariants and justify boundaries using observable constraints.
- Show tests for concurrent requests, duplicate delivery and at least one dependency failure.
- Demonstrate the desired behavior under a repeatable workload or failure injection.
- Present a decision record describing rejected alternatives, cost and rollback.

**Evidence to retain:**

- A version-controlled implementation, configuration and exact steps for reproduction.
- Input/workload data and automated tests or repeatable manual verification records.
- Observed results, rejected alternatives, important design decisions and a technical retrospective.

**Failure analysis:**

Analyze split-brain ownership, lost events, idempotency-key misuse, unbounded retries and network partition assumptions without claiming distributed transactions where none exist.

**Exit demonstration:**

Demonstrate the working implementation, explain the relevant mechanisms, reproduce at least one failure and repair, and defend the chosen trade-offs using retained evidence.
