# APP11 — Advanced Backend Architecture

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP3](APP3.md), [APP4](APP4.md), [APP6](APP6.md)
**Duration:** 9 weeks
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
- Implement and reason about partial distributed transactions, compensations and replay-safe event handling.
- Enforce tenant isolation and constrained resource use across service and message boundaries.
- Plan and verify an incremental backend architecture migration with compatibility and rollback criteria.
- Compare modular and distributed implementations using measured operational and economic costs.

## Modules

### Module 1 — Domain & Module Boundaries

#### Outcomes

- Identify invariants, use cases and ownership boundaries in an application domain.
- Use dependency direction and contract tests to protect modules.

- Draw boundaries around stable business rules rather than technology packages.

#### Lessons

1. **Course introduction: Advanced Backend Architecture** — `lesson`

   Design backend systems whose boundaries withstand changing requirements, concurrent traffic and partial failure. Compare modular monoliths and service boundaries through real experiments, emphasizing data consistency, operability and the cost of distributed complexity.
2. **Domain boundaries and aggregate invariants** — `lesson`
3. **Ports, adapters and modular contracts** — `lesson`
4. **Domain events and invariant ownership** — `lesson`
5. **Aggregate boundaries and transactional consistency** — `lesson`
6. **Coupling metrics and dependency direction** — `lesson`
7. **Choosing module boundaries** — `test`
8. **Separate a tangled service** — `lab`

### Module 2 — Data & Transaction Architecture

#### Outcomes

- Choose transaction boundaries with explicit consistency guarantees.
- Explain read models, outbox patterns and competing-write behavior.

- Choose consistency mechanisms based on observed failure and recovery needs.

#### Lessons

1. **Consistency and transaction ownership** — `lesson`
2. **Events, outboxes and read models** — `lesson`
3. **Isolation levels and concurrency anomalies** — `lesson`
4. **Outbox polling and exactly-once misconceptions** — `lesson`
5. **Materialized projections and repair workflows** — `lesson`
6. **Reasoning about consistency** — `test`
7. **Implement a reliable event handoff** — `lab`

### Module 3 — Services & Async Coordination

#### Outcomes

- Assess when a service split helps or harms deployment and ownership.
- Handle retries, ordering, deadlines and duplicate messages safely.

- Control asynchronous processing and service evolution under partial failures.

#### Lessons

1. **Service extraction and contract evolution** — `lesson`
2. **Workers, queues and idempotent consumers** — `lesson`
3. **Backpressure, deadlines and fairness** — `lesson`
4. **Idempotent consumer design and poison-message handling** — `lesson`
5. **Cross-service contract versioning** — `lesson`
6. **Service boundary decisions** — `test`
7. **Exercise a queue-based workflow** — `lab`

### Module 4 — Operability & Evolution

#### Outcomes

- Analyze bottlenecks and failure containment at subsystem boundaries.
- Plan an incremental migration with rollback and observability.

- Keep backend functionality explainable and recoverable through reversible architecture evolution.

#### Lessons

1. **Bulkheads, timeouts and backpressure** — `lesson`
2. **Evolutionary migration and decision records** — `lesson`
3. **Fault domains and observability propagation** — `lesson`
4. **Load shedding, circuit breakers and retry budgets** — `lesson`
5. **Architecture decision records and migration rollbacks** — `lesson`
6. **Reviewing architecture trade-offs** — `test`
7. **Run a failure injection** — `lab`

### Module 5 — Distributed Data Coordination

#### Outcomes

- Define explicit commit and compensation semantics across service boundaries.
- Reconcile partial progress and duplicates without relying on global atomicity.

#### Lessons

1. **Sagas and compensating actions** — `lesson`
2. **Transactional outbox and inbox pairing** — `lesson`
3. **Distributed transaction limitations** — `lesson`
4. **Event schemas, ordering and replay** — `lesson`
5. **Multi-step workflow consistency** — `test`
6. **Build a compensating distributed workflow** — `lab`

### Module 6 — Multi-Tenant Security & Boundaries

#### Outcomes

- Demonstrate tenant isolation at every data and action boundary.
- Enforce bounded resource access and trustworthy identity across services.

#### Lessons

1. **Tenant ownership and trust-boundary design** — `lesson`
2. **Per-tenant authorization and data isolation** — `lesson`
3. **Rate control and noisy-neighbor protection** — `lesson`
4. **Secrets, token propagation and audit integrity** — `lesson`
5. **Tenant isolation and identity propagation** — `test`
6. **Attack and repair a multi-tenant test service** — `lab`

### Module 7 — Production Evolution & Compatibility

#### Outcomes

- Evolve a live backend boundary without breaking established client contracts.
- Explain the migration and recovery costs of data and interface changes.

#### Lessons

1. **Strangler-pattern migration stages** — `lesson`
2. **Dual-write hazards and data backfill** — `lesson`
3. **Versioned APIs, schema changes and feature flags** — `lesson`
4. **Deployment choreography and rollback windows** — `lesson`
5. **Migration compatibility and reversibility** — `test`
6. **Migrate a service boundary incrementally** — `lab`

### Module 8 — Architecture Measurement & Economic Trade-offs

#### Outcomes

- Make architecture decisions from reproducible measurements and ownership constraints.
- Assess complexity and maintainability alongside capacity and reliability.

#### Lessons

1. **Capacity models and workload baselines** — `lesson`
2. **Tail latency, queueing and saturation** — `lesson`
3. **Service ownership and on-call costs** — `lesson`
4. **Decision records and architecture fitness tests** — `lesson`
5. **Evidence-based service decomposition** — `test`
6. **Compare modular and distributed alternatives** — `lab`

### Module 9 — Resilient Backend Architecture Review

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

**Expanded module assessment and lab requirements:**

- **Module 1 checkpoint and micro-lab:** Show tests that enforce domain invariants independently of delivery and persistence components.
- **Module 2 checkpoint and micro-lab:** Simulate duplicate delivery, concurrent write conflict, and projection rebuilding without breaking protected invariants.
- **Module 3 checkpoint and micro-lab:** Measure bounded queue behavior and demonstrate safe replay and compatibility changes.
- **Module 4 checkpoint and micro-lab:** Prove one failure does not cascade beyond documented limits and record a rollback rehearsal.

- **Module 5 — Distributed Data Coordination (Build a compensating distributed workflow):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Implement a two-service reservation-style flow with an intentionally failing step, compensating action and retry-safe message handling.
  - Verification: Show recorded outcomes for success, crash, retry, duplicate message and compensation paths.
  - Evidence: State diagrams, event log and invariant tests.
  - Failure analysis: Explain why compensation is not true rollback and why retry semantics remain visible to users.
- **Module 6 — Multi-Tenant Security & Boundaries (Attack and repair a multi-tenant test service):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Create two tenant scenarios, attempt unauthorized cross-tenant work, simulate overload, and repair server-side isolation.
  - Verification: Security tests fail on the seeded defect and pass after repair while normal authorized workflows remain functional.
  - Evidence: Access matrix, failed requests, tenancy model and rate-control tests.
  - Failure analysis: Detect tenant IDs trusted from request headers and shared cache state leakage.
- **Module 7 — Production Evolution & Compatibility (Migrate a service boundary incrementally):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Route a small operation through an old and new implementation across staged deployment; compare outputs, perform a backfill and roll back safely.
  - Verification: Demonstrate client compatibility, complete data integrity checks and an explicit no-return point if any.
  - Evidence: Version matrix, migration scripts, shadow results and rollback record.
  - Failure analysis: Analyze partial dual writes, data divergence and backward-incompatible schema deployment.
- **Module 8 — Architecture Measurement & Economic Trade-offs (Compare modular and distributed alternatives):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Implement or simulate two designs for one bounded workflow, measure their latency and operational failure behavior, and document the trade-off.
  - Verification: Present matched benchmark conditions and a decision that identifies when each option is preferable.
  - Evidence: Benchmark scripts, failure traces, architecture decisions and cost assumptions.
  - Failure analysis: Identify benchmarking shortcuts, hidden network cost and decomposition for its own sake.

**Exit assessment expectation:**

Demonstrate the subject outcomes on an unfamiliar example, show at least one negative path and retain evidence allowing another reviewer to reproduce the result. Checkpoint answers must explain mechanisms, while the final integration lab must integrate and verify the expanded topics.

**Exit demonstration:**

Demonstrate the working implementation, explain the relevant mechanisms, reproduce at least one failure and repair, and defend the chosen trade-offs using retained evidence.
