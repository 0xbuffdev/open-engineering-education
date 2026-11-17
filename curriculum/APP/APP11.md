# APP11 — Advanced Backend Architecture

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `elective`
**Prerequisites:** [APP3](APP3.md) — Backend Framework Engineering, [APP4](APP4.md) — Databases & Data Modeling, [APP6](APP6.md) — Software Quality & Engineering Operations
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; calibrate against learner/reviewer experience)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

**Design backend boundaries that preserve business correctness through change, concurrent access, interrupted delivery and partial failure.** Start with a functioning TypeScript/Fastify/PostgreSQL service rather than an empty microservice fleet. Evolve its domain boundaries, transactions, event handoff, multi-step business coordination, derived views and contracts using real local processes and SQL evidence. Explain when a modular monolith is the best architecture and when independent processes or differently owned state justify their extra latency, security and operating cost.

This is an **optional advanced APP specialization**. It does not form part of APP9's core graduation prerequisite closure. Its approved direct prerequisites are **APP3, APP4 and APP6**; APP4 is intentionally explicit even though APP3 also requires it. APP3 already teaches typed API behavior, runtime validation, security/authentication, service code organization, elementary transactions, idempotency and HTTP integration. APP4 supplies query planning, relational modeling, actual isolation, locks, constraints and persistence. APP6 supplies mature tests, CI, telemetry, review and incident evidence. APP11 advances **ownership of evolving domain boundaries, coordination of independently committed work, service integration contracts, safe migration and measured cost**; it does not teach beginner SQL, Fastify, general logging or foundational test design again.

**Course boundary against APP8 and SYS:** APP8 owns whole-application capacity, overload, scale and architecture evolution at core depth. APP11 goes deeper into **backend module ownership, domain/event contracts, transactional outbox plus inbox, independently observed compensation workflows, temporal coupling, service-specific data authority, projection rebuild and incremental extraction**. SYS owns distributed protocols, consensus, replication internals, scheduling and systems-language or operating-system mechanisms. APP12 owns client-facing realtime connections and synchronization. These may be discussed when choosing architecture but are not covert APP11 requirements. No learner is required to implement a consensus algorithm, distributed lock service, Kafka cluster, Kubernetes deployment or public cloud.

**Reference environment:** Begin with a bounded, already functioning APP3/APP6-style authenticated Fastify/TypeScript backend using actual local PostgreSQL, synthetic tenants, contract and independent HTTP/DB tests. Evolve a workflow involving two separately observable ownership contexts, such as allocation/reservation followed by local simulated fulfillment or another reversible operation. Start inside a well-factored modular monolith. For cross-boundary experiments, run a small **separately startable local worker or HTTP participant**, with its own recorded state and failure triggers. Use open-source locally provisionable tools; a PostgreSQL outbox/jobs table and an isolated consumer process are enough for reliable delivery experiments. A second independent PostgreSQL database or separate transaction contexts can demonstrate separate commit authority; disclose that a same-host local experiment is **not** evidence of actual distributed network partitions, multi-region availability or independent cloud failure domains.

**Atomicity is scoped.** One PostgreSQL transaction can commit a domain change and its outbox intent together, but ordinary application code cannot atomically commit a different process, database and external side effect in the same local transaction. After a send-before-acknowledge crash, re-delivery is possible. Consumers need durable inbox/dedup and idempotent business effects. Promise neither globally ordered events nor **exactly-once remote business effects** from a queue setting alone. Ordering guarantees must be explicit per key/aggregate and supported by demonstrable storage and dispatch behavior.

**Compensation is a new transaction, not time travel.** Model durable workflow progress, retry ownership, compensable steps, irreversible pivots, user-visible uncertainty and operator reconciliation. A compensation can fail or itself have side effects. If a reservation, payment-like fixture or notification is already committed, reusing previous code or deploying an earlier image does not necessarily restore the original state. Train learners to choose safe forward completion, explicit compensation or human escalation rather than falsely claiming a global rollback.

**Trust and privacy cross every boundary.** Do not trust tenant IDs from forwarded headers, events, jobs or read projections without suitable verified context. Test access by user, tenant, resource and action independently at API and worker/consumer ownership points. Record event/schema identity, minimize private payloads and protected correlation/log data, bound queue storage and retries and prevent noisy-neighbor starvation. A locally reproducible threat simulation uses only learner-controlled credentials, endpoints and synthetic data.

**Measured alternatives, not novelty:** Compare a working module-based design against a service/worker boundary in the same product with matched workloads, actual failure recovery, old/new contract tests, database invariants and operating costs. Count added process supervision, schema compatibility, dispatch/inbox storage, tracing, monitoring and human incident burden. A justified **no-extraction** decision can be superior; however, a concrete independently owned-process communication exercise is still required to demonstrate the boundary and failure competence.

**Duration and evidence:** The 14–18-week estimate and weekly workload are provisional, not learner-verified. Fourteen progressively deeper modules feed **seven outcome-mapped required summative assessments**; module investigations are formative. One evolving service and controlled local participant can provide evidence for all seven, with authentic independent verification of failures, repairs and unfamiliar bounded changes. No commercial platform, cloud subscription, paid queue, public domain or production data is a required assessment dependency.

## Learning outcomes

- **APP11-O1:** Diagnose a bounded backend evolution problem from business invariants, change frequency, coupling, concurrency, privacy, failure, team ownership and credible workload evidence; distinguish a real architectural need from enthusiasm for microservices.
- **APP11-O2:** Define and enforce stable domain/aggregate/application module boundaries with explicit dependency direction, public contracts and fitness tests, preserving behavior in a refactoring of an existing typed backend.
- **APP11-O3:** Specify and verify transactional invariants, ownership and consistency boundaries with actual PostgreSQL concurrency, isolation/locking or revision evidence and explicit limits on atomicity outside a database transaction.
- **APP11-O4:** Implement a trustworthy transaction-to-event handoff using an actual committed write plus transactional outbox, controlled dispatch and state correlation, verifying no orphan publication on rollback and durable pending events on failure.
- **APP11-O5:** Build independently verifiable message/command contracts and idempotent consumers/inboxes that handle duplicate delivery, racing consumers, replay, versioned envelopes, ordering scope and poison events without misrepresenting end-to-end exactly-once effects.
- **APP11-O6:** Design and execute a multi-step business workflow spanning independently owned state/effects with explicitly modeled progress, timeout, retriable steps, compensation and irreversible pivots, showing that compensation is not rollback.
- **APP11-O7:** Build and reconcile an eventually consistent read model/projection with documented lag, ordering, rebuild/replay and correctness limits, ensuring authoritative writes and authorization do not rely on stale projections.
- **APP11-O8:** Evaluate and demonstrate an appropriate service/process boundary against a modular-monolith alternative, including independent lifecycle, contract, latency, failure ownership and coupling; avoid requiring a distributed platform without demonstrable benefit.
- **APP11-O9:** Apply bounded asynchronous worker/queue execution with retry budgets, backpressure, concurrency and capacity limits, dead-letter/reconciliation policy, interruption/recovery and truthful user-visible completion states.
- **APP11-O10:** Preserve authentication, server-side action/object/property/tenant authorization, trusted identity propagation, secret isolation and fair resource use across modules, events, queues, projections and controlled service calls, including negative tests.
- **APP11-O11:** Contain slow, unavailable and malicious dependencies with realistic end-to-end deadlines, bounded retry ownership, cancellation ambiguity, bulkheads/circuit breakers only when justified, and independently measured blast radius.
- **APP11-O12:** Migrate a backend responsibility incrementally using versioned consumer/event schemas, contract compatibility, strangler or branch-by-abstraction boundaries, data ownership/backfill, observed shadow operation and a verified rollback or forward-repair decision.
- **APP11-O13:** Use meaningful cross-boundary logs, traces, immutable correlation IDs, workflow-state/audit records, privacy-safe telemetry and reconciliation tools to diagnose split ownership, stuck work and divergent state in an actually running controlled system.
- **APP11-O14:** Compare architecture alternatives with matched throughput/latency/error and resource measurements, consistency and security guarantees, release/incident cost, staffing/maintenance complexity and declared financial assumptions; defend the least complex adequate design.
- **APP11-O15:** Reproduce real negative scenarios—parallel business mutations, process restart, publication interruption, duplicate/out-of-order events, stale projections, compensation failure and tenant attacks—and preserve evidence tied to requirements, source revision and runtime environment.
- **APP11-O16:** Deliver, independently reproduce, evolve and defend a cohesive advanced backend architecture under an unfamiliar bounded concurrency, integration, identity, contract, incident or migration constraint, explaining the supported behavior and limitations of a local test environment.

## Modules

### Module 1 — Architecture Decisions Begin with Invariants and Change

#### Outcomes

- APP11-O1
- APP11-O2
- APP11-O8
- APP11-O14

#### Lessons

1. **From correct API to resilient evolving backend** — Explain how APP3's typed service and APP6 quality evidence become the input to new domain ownership and coordination decisions, not an occasion to repeat HTTP fundamentals.

2. **Historical drivers of architectural change** — Contrast tightly coupled applications, modular monoliths, service-oriented systems and event-driven integration as contingent responses to scale, organization and change.

3. **Business workflow and failure contract** — Select a bounded multi-step workflow with actual tenant/resource access, committed state and one delayed or externally simulated effect.

4. **Invariants, authority and reversibility** — Write what must never occur, what may converge later, which actions commit irreversibly and how users learn an outcome.

5. **Coupling map and change hotspots** — Inspect imports, shared tables, cross-module calls, runtime ownership and actual prior changes to identify costly seams.

6. **Operations and data ownership inventory** — Identify principal data owners, worker/process lifetimes, production responsibility and boundaries where a local prototype cannot claim cloud proof.

7. **Problem-specific options and explicit non-goals** — Compare simple in-process calls, PostgreSQL jobs, local process APIs and more elaborate brokers or clusters against real needs.

8. **Measurable risk and architecture hypothesis** — Record security, data, latency, incident, maintenance and cost criteria with evidence that could disconfirm a proposed split.

*Optional practice — false-complexity decision:* Reject a fashionable service extraction without a justified data, failure or team ownership benefit.

### Module 2 — Domain Modeling, Aggregates, Modules and Fitness Tests

#### Outcomes

- APP11-O1
- APP11-O2
- APP11-O3
- APP11-O8

#### Lessons

1. **Bounded contexts and domain language** — Recognize meaningful domain terms, state transitions, responsible actors and noninterchangeable policy concepts.

2. **Aggregates and invariant ownership** — Choose units where consistency should be strongly enforced; compare an oversized aggregate with an under-protected transaction.

3. **Application/use-case versus transport responsibilities** — Keep domain decisions out of Fastify route boilerplate and prevent route parsing from becoming business truth.

4. **Dependency direction and interfaces** — Define narrow type/runtime ports for repositories, time, outbound work and policy rather than repository-dependent domain code.

5. **Modules with explicit public surfaces** — Prevent accidental imports of internal files and direct cross-module table access; make allowed dependency direction executable.

6. **TypeScript types and runtime contracts** — Separate compile-time architectural checks from runtime validation and message/API schema guarantees.

7. **Ownership and transactional seams** — Identify where two operations legitimately share one PostgreSQL transaction and where independent ownership makes coupling dangerous.

8. **Module refactoring without a behavior change** — Extract a tangled use case behind ports while preserving old external HTTP behavior, authorization and DB effects.

9. **Architecture fitness and reviewer tests** — Write import/dependency rules, consumer contract tests and a behavioral regression matrix that fails on a seeded boundary breach.

### Module 3 — Transactional Consistency, Races and Authority

#### Outcomes

- APP11-O3
- APP11-O5
- APP11-O6
- APP11-O15

#### Lessons

1. **PostgreSQL as source of transaction truth** — Reuse APP4's constraints, isolation and locking in an applied domain flow; distinguish single-DB atomicity from external calls.

2. **Transaction scope and connection ownership** — Ensure repository calls and persisted intent use the same actual transaction context where atomicity is required.

3. **Transactional Concurrency and Idempotency Races** — Verify lost-update protection under two independent connections and mismatched revision responses; use actual DB uniqueness/locking under parallel duplicate requests, not a process-local Set as the only guard.

4. **Isolation anomalies and explicit tests** — Reproduce a relevant read/write skew or conflict using actual SQL while acknowledging selected isolation-mode behavior.

5. **Commit order versus event order** — Distinguish business aggregate version, database commit order, created timestamps and globally ordered events.

6. **Long transactions and lock contention** — Inspect lock waits, deadlocks and pool starvation and choose a bounded transaction duration before adding distributed machinery.

7. **Failure between commit and external effect** — Reproduce why an external HTTP message cannot be committed atomically with a PostgreSQL transaction by ordinary application code.

*Optional practice — concurrent reservation bug:* Repair a double-claim or stale-state flow and verify one durable allowed outcome using independent SQL.

### Module 4 — Transactional Outbox, Dispatch and Lifecycle Guarantees

#### Outcomes

- APP11-O3
- APP11-O4
- APP11-O5
- APP11-O9
- APP11-O13

#### Lessons

1. **The dual-write failure matrix** — Enumerate successful DB/failing publish, failing DB/successful publish, process death and ambiguous acknowledgement outcomes.

2. **Commit domain state with outbox intent** — Write domain change and event intent in one PostgreSQL transaction and verify rollback removes both.

3. **Event envelope and aggregate identity** — Include stable event ID, aggregate ID/version, tenant, occurrence time, schema revision and safe correlation metadata.

4. **Outbox polling and row claims** — Use safe DB row-claim techniques with bounded batch and lease/recovery policy appropriate to the reference runner.

5. **Dispatch acknowledgement window** — Reproduce crash after send/before marking acknowledged and explain why retransmission may occur.

6. **Ordering boundaries and writer concurrency** — Preserve per-aggregate order where required, and disclose where timestamps or multiple dispatchers cannot promise total order.

7. **Retention, cleanup and dead letters** — Specify archive/prune conditions, unresolved delivery records and recovery procedures without silently dropping pending business work.

8. **Observing stuck outbox state** — Expose privacy-safe backlog age, attempts, last failure and a testable alert/reconciliation action.

*Optional practice — outbox crash drill:* Kill the dispatcher at a controlled point, restart and confirm committed intent is eventually handled without duplicate business effects.

### Module 5 — Inbox Contracts, Duplicate Consumers and Event Evolution

#### Outcomes

- APP11-O4
- APP11-O5
- APP11-O7
- APP11-O9
- APP11-O10

#### Lessons

1. **Command versus event semantics** — Differentiate request to act, committed domain fact and integration notification with versioned ownership.

2. **Schema validation on message entry** — Treat message body, tenant claims, provenance and event schema version as untrusted runtime data.

3. **Idempotent inbox and dedup scope** — Atomically reserve a processed event/command identity with permitted effect, avoiding per-process memory-only flags.

4. **Concurrent consumer claims** — Reproduce two workers racing the same ID and verify a single durable intended effect.

5. **Retry and acknowledgement uncertainty** — Model success followed by lost ACK, poison body, transient downstream error and backoff ceilings.

6. **Event ordering and stale revisions** — Reject, buffer or reconcile out-of-order aggregate versions according to an explicit local invariant.

7. **Backward/forward compatible event evolution** — Make additive fields and old/new reader interpretation testable; identify breaking schema and deprecation conditions.

8. **Replay and audit privacy** — Replay permitted synthetic data while preventing stale personal claims, tenant impersonation and unbounded historical retention.

*Optional practice — duplicate delivery repair:* Break a consumer with an acknowledgement race, repair it and show real DB invariants after repeated deliveries.

### Module 6 — Cross-Boundary Business Workflows and Compensation

#### Outcomes

- APP11-O3
- APP11-O4
- APP11-O5
- APP11-O6
- APP11-O9

#### Lessons

1. **When one transaction is insufficient** — Select a workflow with independently owned state or simulated external commit and explain why a single local transaction is not a truthful model.

2. **Business workflow state machine** — Define pending, reserved, confirmed, compensating, compensated, failed, uncertain and manual-review states with legal transitions.

3. **Choreography versus orchestration** — Compare event-driven peer progression and a durable coordinator, including ownership, observability and coupling.

4. **Local commits and durable progress** — Write each participant's local state and progress before issuing the next independently owned step.

5. **Compensable, pivot and retryable steps** — Identify exactly what can be undone by a new operation, what is irreversible and when forward completion is required.

6. **Timeout and outcome ambiguity** — Distinguish no response, known rejection, committed-but-lost-ack and user-visible pending states without fabricated global atomicity.

7. **Concurrent workflows and semantic locks** — Protect the same resource from incompatible parallel reservations and stale compensation of newer work.

8. **Compensation failure and reconciliation** — Inject failure of the compensation itself and record unresolved state, retry/runbook and escalation instead of claiming rollback.

*Optional practice — saga fault matrix:* Exercise good flow, failed step, duplicated event, timeout and failed compensation with traceable participant state.

### Module 7 — Materialized Projections, Lag and Reconciliation

#### Outcomes

- APP11-O3
- APP11-O5
- APP11-O7
- APP11-O10
- APP11-O13

#### Lessons

1. **Read models and owned write state** — Define authoritative domain records versus derived denormalized views and identify queries that may tolerate staleness.

2. **Projection schema and version ownership** — Design a rebuildable PostgreSQL read table with event ID/aggregate versions and appropriate tenant filtering.

3. **Projection lag and observed limits** — Introduce controlled delivery delay and measure currentness while labeling local simulated lag honestly.

4. **Duplicate and out-of-order projection updates** — Test exactly what happens under replay and delayed updates, avoiding stale overwrite of a newer projection.

5. **Rebuild from authoritative history** — Reconstruct a projection from a bounded event log or snapshot with valid provenance and no duplicate side effects.

6. **Gap detection and repair** — Compare authoritative aggregate counts/versions and projection records and create an inspectable reconciliation path.

7. **Privacy and authorization in read models** — Verify old tenant permission, deleted/private fields and cache/access changes cannot expose unauthorized derived data.

8. **Read-your-writes and user contract** — Choose when to await, poll, show pending, read authoritative source or reject a stale view instead of promising immediate consistency.

*Optional practice — lagged-order workflow:* Repair a user screen reporting completion while only an out-of-date projection exists.

### Module 8 — Process Boundaries, Contracts and Service Extraction Choices

#### Outcomes

- APP11-O1
- APP11-O2
- APP11-O8
- APP11-O11
- APP11-O14

#### Lessons

1. **Module versus process ownership** — Compare same-process imports, separate workers and locally running HTTP services by latency, deployment and failure costs.

2. **Synchronous contract and deadline semantics** — Declare request/response schema, timeout, idempotency and error handling across a process boundary.

3. **Consumer-driven compatibility testing** — Exercise old/new producers and consumers independently, including unknown fields, renamed statuses and absent data.

4. **Service identity and boundary authentication** — Distinguish verified end-user identity from trusted service identity and reject forwarded user headers from untrusted clients.

5. **Process restart and network failures** — Demonstrate controlled connection refusal, partial response and DNS/port timeout under two local processes.

6. **Cross-process tracing and correlation** — Propagate safe correlation and causal event IDs while avoiding raw tokens and unrestricted baggage.

7. **Data ownership without shared writes** — Prohibit independent services writing each other's authoritative tables and test a seeded ownership violation.

8. **When extraction fails the cost test** — Benchmark and explain a modular monolith with clear modules against a local process split, considering complexity and constraints.

*Optional practice — contract-break investigation:* Repair an independently restarted service that silently changed a required contract or trust assumption.

### Module 9 — Queue Capacity, Backpressure and Worker Recovery

#### Outcomes

- APP11-O5
- APP11-O6
- APP11-O9
- APP11-O11
- APP11-O13

#### Lessons

1. **Choose durable local queue semantics** — Apply a PostgreSQL outbox/jobs implementation or a justified local open-source queue, not a paid broker requirement.

2. **Claim, visibility timeout and heartbeats** — Explain leases/claims/worker process ownership and repeatable recovery when a worker dies mid-task.

3. **Bounded concurrency and downstream capacity** — Set worker and DB pool limits; measure throughput, job age and external provider pressure without assuming more workers always help.

4. **Backpressure and rejection policy** — Define what can be deferred or refused, with truthful API/user outcome and finite memory/database growth.

5. **Retry backoff, jitter and budget** — Set attempt caps, timeouts and actor ownership, avoiding multiplicative retries across HTTP, worker and dependency.

6. **Poison messages and terminal action** — Quarantine malformed/permanently denied messages and provide auditable retry, remediation or cancellation choices.

7. **Per-tenant fairness and quotas** — Prevent one synthetic tenant's jobs from starving others while preserving correct tenant ownership.

8. **Eventual completion and user status** — Report accepted, pending, failed, reconciled and completed outcomes from authoritative records rather than optimistic promises.

*Optional practice — stalled-work failure:* Kill a worker during processing, restart/reclaim a safe lease and show no unintended duplicate business action.

### Module 10 — Tenant, Service Identity and Security Across Boundaries

#### Outcomes

- APP11-O5
- APP11-O7
- APP11-O8
- APP11-O10
- APP11-O15

#### Lessons

1. **Identity and trust graph** — Map human principal, tenant, service actor, process identity and the authority needed for each business step.

2. **Authorization at every execution boundary** — Enforce object/action/property rules in HTTP, worker, event consumer and projection read, not once on the entry API only.

3. **Forwarded claim integrity** — Test forged tenant IDs, request headers, message envelopes and expired tokens across process/message transitions.

4. **Tenant-scoped deduplication and cache keys** — Prevent same event/request ID collisions, shared read models and retry state from bridging tenants.

5. **Narrow DB roles and private state** — Use local scoped SQL roles, secrets and least-privilege access where feasible, and verify denied cross-owner writes.

6. **Noisy neighbor and abuse resource controls** — Apply tenant-aware queue quotas, bounded payload sizes and backpressure with explicit fairness trade-offs.

7. **PII minimization in events and logs** — Prefer opaque identifiers and explicit retention, avoiding copying account details through every event or trace.

8. **Security negative test matrix** — Run cross-tenant direct API, event spoof, projection read and job-status authorization attacks against synthetic services.

*Optional practice — forged event drill:* Repair a consumer that trusts tenant identity from a producer message without independent authorization context.

### Module 11 — Partial Failure Containment, Deadline Budgets and Recovery

#### Outcomes

- APP11-O6
- APP11-O9
- APP11-O11
- APP11-O13
- APP11-O15

#### Lessons

1. **Dependency graph and shared resource pools** — Locate fan-out, DB/pool, worker queues and critical versus optional paths that could propagate failure.

2. **End-to-end deadline and cancellation** — Allocate time across service and DB hops; explain why canceling a request cannot undo a committed external effect.

3. **Retry storm and ambiguous success** — Observe increased traffic after injected dependency failure and choose one bounded retry owner and dedup rules.

4. **Bulkhead and circuit-breaker decisions** — Measure when separate resource pools or circuit state solve an actual blast-radius problem, avoiding ritual complexity.

5. **Graceful degraded product contract** — Protect business/security invariants while shedding optional work with truthful response and accessible pending status.

6. **Recovery ramp and backlog drain** — Limit replay bursts against a recovering dependency and measure pending/failed/reconciled workflows.

7. **Reconciliation after incomplete compensation** — Compare coordinator/participant records and execute a documented safe operator action.

8. **Negative-path operational evidence** — Correlate real local HTTP failures, worker state, database facts and user-visible outcomes under a fixed fault scenario.

*Optional practice — cascading outage:* Show a slow optional service exhausting a shared pool, then measure verified containment and legitimate denied requests.

### Module 12 — Incremental Migration, Schema Compatibility and Reversibility

#### Outcomes

- APP11-O2
- APP11-O5
- APP11-O7
- APP11-O8
- APP11-O12
- APP11-O15

#### Lessons

1. **Choose the evolving responsibility** — Select one real module or data ownership boundary and specify measured reason, present consumers and rollback risk.

2. **Branch by abstraction and strangler approach** — Introduce a versioned switch/adapter so old and candidate implementations can coexist without immediate global cutover.

3. **Consumer compatibility matrix** — Test old/new HTTP clients, event schemas, database migrations and worker versions with a running synthetic workflow.

4. **Expand, backfill, validate, contract** — Stage additive schema changes and bounded backfill; verify how older consumers continue to function.

5. **Shadow execution and side-effect safety** — Compare old/new read-only or otherwise safe candidate behavior without duplicating writes, emails or payments.

6. **Data ownership and dual-write trap** — Explain why copying writes into two independent stores can diverge; design safe migration/backfill/monitoring.

7. **Traffic/feature cutover and observation** — Shift a bounded local request or worker route under health/permission/data correctness checks and recorded approval.

8. **Rollback versus forward repair after pivot** — Demonstrate previous version compatibility, irreversible writes and when rollback must be refused for safe forward repair.

*Optional practice — contract migration drill:* Seed an old-consumer break or stale projection during cutover, detect it and repair without losing legitimate state.

### Module 13 — Architecture Measurements, Operations and Economics

#### Outcomes

- APP11-O1
- APP11-O11
- APP11-O13
- APP11-O14

#### Lessons

1. **Architecture fitness as evidence** — Define coupling change, runtime latency, resource usage, failure isolation and consumer compatibility indicators linked to requirements.

2. **Representative workload and fault conditions** — Use APP6 measurement discipline for matching traffic/data, version, CPU/network and error counting without APP8 scale re-teaching.

3. **Compare monolith and separated boundary** — Measure local successful/failed user task, p95 where sample permits, serialization/pool work and new failure modes.

4. **Observability and workflow correlation** — Inspect consistent operation/workflow/event IDs and state transitions without high-cardinality metrics or leaked identity.

5. **Backlog age, compensation and health** — Monitor outbox age, worker attempts, unprocessed inbox and unresolved compensation rather than treating process up as business success.

6. **Total operating and migration cost** — Include process/service overhead, trace/log storage, DB connections, deployment coordination, incident/runbook and development time.

7. **Economic and privacy sensitivity** — Vary traffic, tenant skew, broker/provider expense and data retention to explain which architectural option could win.

8. **Decision record, rejected options and exit triggers** — Write an ADR explaining why to preserve the modular monolith or extract a boundary, and what future evidence changes the choice.

*Optional practice — no-benefit extraction:* Identify a service split that slows users and increases incidents despite satisfying a fashionable architecture diagram.

### Module 14 — Integrated Advanced Backend and Independent Technical Defense

#### Outcomes

- APP11-O1
- APP11-O2
- APP11-O3
- APP11-O4
- APP11-O5
- APP11-O6
- APP11-O7
- APP11-O8
- APP11-O9
- APP11-O10
- APP11-O11
- APP11-O12
- APP11-O13
- APP11-O14
- APP11-O15
- APP11-O16

#### Lessons

1. **Select an authentic multi-step backend workflow** — Start from a credible APP3/APP6 service with real PostgreSQL, two synthetic tenants and a defensible changed requirement.

2. **Publish domain and security model** — Document aggregate boundaries, authoritative owner, allowed transitions, identity and event/data privacy constraints.

3. **Refactor modules behind testable contracts** — Preserve public API and database invariants while enforcing import boundaries and describing an alternate service split.

4. **Implement transaction-to-event safety** — Commit business state and outbox record atomically, dispatch to a controlled independent consumer and inject an acknowledgement crash.

5. **Handle duplicated and ordered work** — Use inbox/idempotency, replay and version checks, actual parallel PostgreSQL operations and a poison-event policy.

6. **Coordinate failure and compensation** — Execute a bounded two-owner multi-step workflow including a failed pivot/retry/compensation and an unresolved branch.

7. **Rebuild and protect read projections** — Reconcile a lagged projection and verify protected reads/tenant boundaries without relying on derived state for authoritative action.

8. **Control resources and process failure** — Enforce retry/backpressure/deadlines, stop/restart worker/process and prove optional dependency failure does not corrupt business state.

9. **Stage a compatible architecture evolution** — Use a safe adapter/feature switch, old/new client/event/database tests, a read-only shadow or safe equivalent and a rollback/repair rule.

10. **Measure alternatives and operational consequences** — Compare at least two credible boundaries with matched evidence, costs, unresolved risks and a reason to reject extra complexity.

11. **Unfamiliar bounded incident and independent defense** — Respond to a new cross-tenant message, duplicate/out-of-order event, transaction race, compensation failure, migration fault or overload condition with reproducible evidence.

## Completion requirements

All **APP11-O1–APP11-O16** must be demonstrated through the **seven required summative assessments** listed below. The learner may submit one evolving backend and controlled local participant, reusing inspectable earlier evidence when it addresses distinct requirements. Formative lesson investigations, reading choices and elective-adjacent optional infrastructure do not create hidden graduation gates.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP11-AS1` — Domain Boundary Refactoring and Transactional Invariants | APP11-O1, APP11-O2, APP11-O3, APP11-O8, APP11-O15 | Domain and change hypothesis, architecture dependency diagram and module contracts, source diff, complete signed-in/forbidden API regression suite, independent concurrent DB logs and constraints, fitness-rule failure/pass, ADR and limitations |
| `APP11-AS2` — Atomic Outbox, Inbox Idempotency and Replayable Handoff | APP11-O3, APP11-O4, APP11-O5, APP11-O7, APP11-O9, APP11-O13, APP11-O15 | Outbox/inbox schemas and SQL transaction, event envelope/contracts and dispatcher/worker code, failure injection scripts, version/order/idempotency/poison tests and DB before/after records, projection rebuild and privacy-safe state/correlation logs |
| `APP11-AS3` — Multi-Step Coordination, Compensation and Failure Recovery | APP11-O3, APP11-O5, APP11-O6, APP11-O9, APP11-O11, APP11-O13, APP11-O15 | Workflow state diagram and transition policy, separately observed local participants and DBs/fixtures, complete fault/compensation matrix, real traces and SQL effects, user-facing status examples, operator reconciliation runbook and unsupported-guarantee notes |
| `APP11-AS4` — Cross-Boundary Tenant Trust and Bounded Resource Safety | APP11-O5, APP11-O7, APP11-O8, APP11-O9, APP11-O10, APP11-O11, APP11-O15 | Trust-boundary and access matrix, tenant/worker identities and limits, adversarial synthetic HTTP/envelope scripts, DB row/queue/error/timing evidence, before/after authorization and contention tests and remaining risks |
| `APP11-AS5` — Incremental Backend Extraction and Versioned Contract Compatibility | APP11-O1, APP11-O2, APP11-O5, APP11-O7, APP11-O8, APP11-O12, APP11-O14 | ADR and business trigger, old/new sequence and contract matrix, adapter/feature-switch code, migration/backfill and safe shadow evidence, controlled failure/release choice, SQL/user security invariants, operational cost/limits and reproducible test recipe |
| `APP11-AS6` — Architecture Failure, Observability and Economic Decision | APP11-O1, APP11-O8, APP11-O9, APP11-O11, APP11-O13, APP11-O14 | Reproducible workload/fault scripts and profiles, real HTTP/SQL/worker traces with safe correlation, before/after outcomes, incident/reconciliation timeline, component/owner cost comparison, architecture fitness rubric, ADR and limitations |
| `APP11-AS7` — Integrated Architecture and Independent Boundary Defense | APP11-O1, APP11-O2, APP11-O3, APP11-O4, APP11-O5, APP11-O6, APP11-O7, APP11-O8, APP11-O9, APP11-O10, APP11-O11, APP11-O12, APP11-O13, APP11-O14, APP11-O15, APP11-O16 | Source and environment revisions, bounded synthetic two-tenant database/queue/HTTP fixture, architecture/ADR/security and contract map, replay/compensation/repair fault transcripts, SQL and API normal/negative results, deployment and resource metrics, cost/maintenance analysis and independent written/recorded/live defense |

### Shared execution, integrity and ethical boundaries

- Use versioned TypeScript/Node/Fastify and compatible actual PostgreSQL, controlled free local process/worker or HTTP fixture, deterministic synthetic roles/tenants and bounded tasks. Document OS/toolchain, database versions, package lockfiles, startup, failure toggles, safe teardown, signed-in test requests and resource requirements. Initial free dependencies may be provisioned; assessed demonstrations must be reproducible thereafter using disclosed local resources.
- Demonstrate **real business state** and transaction/concurrency through PostgreSQL queries, constraints, commit/rollback and independent connections. Static diagrams, mocked repository methods and a sequential success-only script cannot prove transactional correctness or races. Declare transaction boundaries at every state authority, including when logical owners share a development host.
- A transactional outbox commits event intent alongside the domain fact; it does **not** grant guaranteed delivery to an independently owned consumer or exactly-once external effects. Induce a publisher crash after dispatch and before acknowledgement, prove recoverability, and verify durable idempotency/inbox scope. Per-aggregate versioning, ordering and retention are explicit, not assumed from timestamp order.
- Model *at least one* actual separate local process/independently committed participant for cross-boundary failure behavior in the required assessments. This is not a demand for microservices production architecture: a modular-monolith final decision remains valid when it meets the measured constraints, and the separated participant can remain a controlled disposable learning fixture.
- For saga/compensation exercises, publish legal state transitions, commitment/irreversible pivot, retry and abandonment conditions. A compensation is a new action that may fail; prove a failed compensation or uncertain outcome can be reconciled or placed in explicitly reviewable/manual attention, not silently returned as completed.
- Derived read projections and caches cannot authorize protected writes from stale tenant/resource facts. Use authoritative access checks, replay and version checks and protect data deletion/retention as applicable. A delayed locally simulated read model does not prove real PostgreSQL streaming replication or geographic consistency behavior.
- Identity and authorization must be enforced at meaningful service, worker, event, projection and job-status boundaries. Test forged/expired/foreign tenant inputs, cross-tenant event IDs and resource identifiers, unapproved properties and worker exhaustion using synthetic identities and direct independent HTTP/message/DB inspection.
- Bound HTTP and worker payload sizes, queue length, in-flight operations, concurrency, deadlines, retry attempts, poison handling and data retention according to the declared scenario. A client timeout or process cancellation does not undo a previously committed business/external effect; use truthful pending/failure outcomes and explicit reconciliation.
- Compare old/new API/event/schema consumers with real replay and compatible migration evidence. Shadow traffic must not duplicate irreversible writes or external notifications; staged cutover needs recorded owner, route/feature state, result comparison, data migration safety and a rollback or forward-repair decision that respects committed effects.
- Use privacy-safe correlation, workflow-state records and operator runbooks to make failed and stuck work diagnosable without leaking raw credentials, PII, cross-tenant payloads or long-lived unbounded logs.
- Measure architectural choices with matched bounded workload/tenant mix, configured machine and resource budgets, sufficient samples and failure/error accounting; do not substitute a traffic-free microbenchmark for true user-task evidence. Cost analyses specify compute/DB/queue/logging/operational labor units and sensitivity, not invented live hosted prices or universal production availability guarantees.
- Conduct testing only on learner-owned local HTTP processes, authorized databases and synthetic messages. No tests against arbitrary external users, services, protected cloud environments or real payment systems are necessary or permissible without authorization.
- Reviewers may introduce an unfamiliar bounded dependency failure, lost ACK, contract version, forged event, competing transaction, stale projection, compensation fault or architecture migration dilemma. The change must remain inside published outcomes and accessible free local tools, and allow an equivalent written, recorded, live or otherwise inspectable technical defense.

### Required summative assessments

- **APP11-AS1** (required domain boundary refactoring and transactional invariants)
  - Outcomes: APP11-O1, APP11-O2, APP11-O3, APP11-O8, APP11-O15
  - Work: From a real APP3/APP6-style authenticated TypeScript/Fastify/PostgreSQL service, document a tangled domain workflow with at least two plausible ownership seams. Refactor one vertical use case into stable domain/application/persistence modules, preserve existing HTTP contracts and independently verify a meaningful aggregate invariant under actual concurrent PostgreSQL connections. Seed a forbidden internal import, cross-module write or lost-update case and demonstrate a failing architecture/contract/SQL test before repair.
  - Criteria: The refactor preserves normal/denied browser-independent API results while reducing a defined coupling or ownership problem; new interfaces do not merely rename files. One authoritative transaction protects the declared invariant, independent concurrent SQL sessions reveal conflict semantics and seeded boundary tests fail before repair. Two alternatives and an explicit no-split argument are reviewed against actual change costs. No claim is made that TypeScript types validate untrusted runtime inputs or that an aggregate automatically spans unrelated remote commits.
  - Evidence: Domain and change hypothesis, architecture dependency diagram and module contracts, source diff, complete signed-in/forbidden API regression suite, independent concurrent DB logs and constraints, fitness-rule failure/pass, ADR and limitations.

- **APP11-AS2** (required atomic outbox, inbox idempotency and replayable handoff)
  - Outcomes: APP11-O3, APP11-O4, APP11-O5, APP11-O7, APP11-O9, APP11-O13, APP11-O15
  - Work: Implement a real PostgreSQL transaction that commits a business mutation and bounded outbox event intent together, then dispatch to a separately inspectable local consumer/worker with durable inbox/dedup and protected read projection or equivalent derived state. Cause DB rollback, publisher crash after delivery/before ACK, racing duplicate deliveries, delayed and out-of-order aggregate versions, malformed/poison envelopes, process restart and projection rebuild. Prove the correct durable state under each condition using independent DB queries.
  - Criteria: A rolled-back domain transaction cannot publish a valid associated event, while a committed but undelivered event remains recoverable. Duplicate messages or concurrent consumers cause at most the one intended durable business effect within the tested scope, with no false end-to-end exactly-once claim. Replays and out-of-order events cannot silently overwrite a newer derived view; eventually consistent results are labeled with lag and checked against authoritative records. Delivery bounds, error status, retention and recovery are testable with free local tooling.
  - Evidence: Outbox/inbox schemas and SQL transaction, event envelope/contracts and dispatcher/worker code, failure injection scripts, version/order/idempotency/poison tests and DB before/after records, projection rebuild and privacy-safe state/correlation logs.

- **APP11-AS3** (required multi-step coordination, compensation and failure recovery)
  - Outcomes: APP11-O3, APP11-O5, APP11-O6, APP11-O9, APP11-O11, APP11-O13, APP11-O15
  - Work: Build a bounded two-owner local workflow with separately committed state or an actual controlled HTTP external fixture, using a durable state machine and either explicit coordinator or well-justified event choreography. Exercise success, timeout with uncertain outcome, duplicate steps, failed dependent action, compensation attempt, compensation failure and safe operator reconciliation. Mark irreversible pivot and user-visible pending/terminal states; preserve independent transaction boundaries and verify owner/tenant access.
  - Criteria: At least two independently observable state or side-effect owners and their actual local interactions are exercised; a single mocked function returning a sequence is insufficient. The workflow never claims atomic rollback across already committed participants; compensation creates a new auditable operation and its failure remains recoverable/visible. Idempotent retries and business locks/versions prevent double-claims and stale compensations. Results reconcile to authoritative records after restart or explicit manual intervention without disclosing confidential state.
  - Evidence: Workflow state diagram and transition policy, separately observed local participants and DBs/fixtures, complete fault/compensation matrix, real traces and SQL effects, user-facing status examples, operator reconciliation runbook and unsupported-guarantee notes.

- **APP11-AS4** (required cross-boundary tenant trust and bounded resource safety)
  - Outcomes: APP11-O5, APP11-O7, APP11-O8, APP11-O9, APP11-O10, APP11-O11, APP11-O15
  - Work: On a locally composed modular backend plus worker or bounded HTTP service boundary, trace verified principal/tenant permissions through normal API, message, projection and background job paths. Seed attacks using forged tenant headers/envelopes, same dedup ID across tenants, unauthorized projection reads, stale permission and a noisy-neighbor message burst; control worker concurrency, tenant quotas, payload limits and a slow local dependency. Demonstrate how the corrected design keeps protected operations available and blocks prohibited data effects.
  - Criteria: Identity and authority are rechecked at each ownership boundary rather than trusted because a caller previously authenticated; privileged service identity is not confused with end-user permissions. Cross-tenant reads/writes/status projections and dedup collisions are denied by independently observed HTTP/message/DB outcomes. Queue, retry and worker limits remain bounded under the declared burst and failure; protected user/business state remains correct and failures are reported honestly. Traces/secrets/PII are appropriately redacted.
  - Evidence: Trust-boundary and access matrix, tenant/worker identities and limits, adversarial synthetic HTTP/envelope scripts, DB row/queue/error/timing evidence, before/after authorization and contention tests and remaining risks.

- **APP11-AS5** (required incremental backend extraction and versioned contract compatibility)
  - Outcomes: APP11-O1, APP11-O2, APP11-O5, APP11-O7, APP11-O8, APP11-O12, APP11-O14
  - Work: Choose one measurable change/ownership pressure in a modular backend; compare an internal module/adapter evolution with a separate bounded service/process alternative. Implement a versioned abstraction, old/new HTTP/event consumers, a compatible staged schema/backfill or projection change, safe read-only shadow/differential checks and an actual local feature/route cutover. Seed an old-consumer break or out-of-date event/read-model defect, then demonstrate a safe rollback or defensible forward repair preserving committed data and private access.
  - Criteria: A real alternate implementation or process boundary runs; an architecture drawing alone cannot satisfy the evolution exercise. Both old/new consumer behaviors and domain invariants are verified using independent contract, DB and tenant-negative tests. Shadow operation does not duplicate irreversible side effects, the migration uses explicit data ownership and avoids unchecked dual writes, and rollback is refused when a committed data change makes old code unsafe. Reversibility, added operational burden and exit triggers are recorded honestly.
  - Evidence: ADR and business trigger, old/new sequence and contract matrix, adapter/feature-switch code, migration/backfill and safe shadow evidence, controlled failure/release choice, SQL/user security invariants, operational cost/limits and reproducible test recipe.

- **APP11-AS6** (required architecture failure, observability and economic decision)
  - Outcomes: APP11-O1, APP11-O8, APP11-O9, APP11-O11, APP11-O13, APP11-O14
  - Work: Run a matched bounded workload and fault experiment against one complex protected use case using a modular-monolith baseline and a plausible separated/local-process or async variant. Inject a slow/unavailable dependency, retry amplification or stuck outbox/compensation, correlate user errors/latency with actual request, DB, worker and workflow state, and implement a justified containment or operational reconciliation. Compare end-to-end task success, p95 or justified distribution, queue/inbox backlog, failure blast radius, complexity and illustrative monthly resource/maintenance cost across options.
  - Criteria: Measurements record environment, data/tenant mix, errors/timeouts, versions, samples and test bias; process split is not presumed superior. Fault scenarios are actually run against learner-owned local systems and observable end-to-end business state, and no unavailable cloud/multi-region property is asserted. A bounded mitigation preserves authorization and transactional correctness and its effect is inspectable. Resource and operating cost estimates have explicit units and sensitivity; a rational no-extraction/less-complex choice may pass.
  - Evidence: Reproducible workload/fault scripts and profiles, real HTTP/SQL/worker traces with safe correlation, before/after outcomes, incident/reconciliation timeline, component/owner cost comparison, architecture fitness rubric, ADR and limitations.

- **APP11-AS7** (required integrated architecture and independent boundary defense)
  - Outcomes: APP11-O1, APP11-O2, APP11-O3, APP11-O4, APP11-O5, APP11-O6, APP11-O7, APP11-O8, APP11-O9, APP11-O10, APP11-O11, APP11-O12, APP11-O13, APP11-O14, APP11-O15, APP11-O16
  - Work: Deliver one coherent local advanced backend evolution from a correctly tested APP3/APP6 Fastify/PostgreSQL service. Demonstrate published domain and transaction ownership, contract-protected modules, actual outbox/inbox handoff, durable step coordination with genuine partial failure/compensation and read-model reconciliation, negative tenant/work-queue tests, fault isolation, compatibility-safe incremental evolution and a measured reason to retain or add process boundaries. Reuse qualifying AS1–AS6 evidence. A reviewer introduces an unfamiliar but bounded race, duplicate/order, stale projection, forged tenant event, compensation failure, contract migration or dependency incident and observes a specific correction or safe diagnosis with maintained security/business invariants.
  - Criteria: From a clean documented free local environment, the reviewer can execute and inspect real HTTP, independent SQL transactions, safe synthetic events, actual worker/process interruptions, owner state, negative tenant tests, contract evolution and matched user-task observations without mandatory paid broker/cloud/Kubernetes/SYS elective. Every claimed effect and recovery is verifiable at authoritative data boundaries rather than by curated log messages alone; compensation, event ordering and exactly-once guarantees are qualified. The unfamiliar challenge is aligned to disclosed public outcomes and the learner demonstrates technically reasoned repair or safe remediation, rejected alternatives and unresolved operating cost/limits through an accessible defense.
  - Evidence: Source and environment revisions, bounded synthetic two-tenant database/queue/HTTP fixture, architecture/ADR/security and contract map, replay/compensation/repair fault transcripts, SQL and API normal/negative results, deployment and resource metrics, cost/maintenance analysis and independent written/recorded/live defense.

### Completion, academic status and historical revision

APP11 completion requires acceptable independently inspectable decisions for `APP11-AS1` through `APP11-AS7`, collectively establishing `APP11-O1` through `APP11-O16`. A successful demo of two HTTP endpoints or more Kubernetes resources does not compensate for broken domain ownership, transaction consistency, lost message handling, compensation safety, tenant isolation, incompatible consumers, unobservable incidents or unsupported economic claims.

Retain OEE/course revision, relevant outcome and assessment IDs, source/artifact identities, local environment, contracts and synthetic fixture identities, actual failure and independent SQL evidence, race/duplicate/compensation and security negatives, matched measurements, ADR/rollback decision, accessible technical defense, limitations and reviewer decision under [OEE Evidence Rules](../../spec/evidence-rules.md).

APP11 retains its code, title, `course` type, **optional `elective`** status and the approved direct prerequisites **APP3 + APP4 + APP6**. It replaces the legacy nine-week checkpoint and final-lab contract with outcome-driven OEE `v0.2.0` **draft** outcomes and assessments. Historical APP11 completions and learner evidence remain tied to their original revision, not silently reinterpreted as meeting new requirements. APP9 and all required core courses remain unchanged; APP12–APP16 now publish their own separately migrated outcome-driven elective drafts, subject to independent academic and learner review. Any OEE Workspace, content/resource or 0xNAND version/evidence pin changes require separate downstream review, not automatic conversion.

This draft's software structural CI does not certify independent learner testing, public educational conformance, genuine public-cloud fault tolerance or production readiness.

### Public non-mandatory technical references

These resources inform independent investigation; they introduce no hidden assessment, required commercial system or extra completion gate.

- [AWS Prescriptive Guidance — Transactional outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html) for atomic event intent versus duplicate-delivery risks.
- [Azure Architecture Center — Saga pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) for compensations, pivots, coordination, irreversibility and fault boundaries.
- [Martin Fowler — Bounded Context](https://martinfowler.com/bliki/BoundedContext.html) and [Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html) for domain language and incremental system evolution.
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) and [explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) for independent concurrency evidence.
- [Microsoft Architecture Center — Compensating Transaction](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction) and [Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) for qualified recovery and containment.
- [OWASP API Security Project](https://owasp.org/www-project-api-security/) for broken object/property authorization and data exposure review.
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/) for observed incident and operator evidence.
