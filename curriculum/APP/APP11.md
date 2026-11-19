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

**Instructional sufficiency, duration and evidence:** Keep the 14–18-week estimate and weekly workload **provisional**, not learner-verified. The fourteen distinct mechanisms remain teachable: domain ownership needs a worked invariant, PostgreSQL transaction/outbox needs an actual dual-write counterexample, inbox needs separate transactionally protected duplicate evidence, saga needs legal transitions and **failed compensation**, projections need an actually sufficient rebuild source, and extraction needs a running process plus matched alternatives. A new backend mechanism requires an explanation, a worked trace, independent operation/failure and useful feedback **before** summative judgment; neither a heading nor a passing assessment mapping establishes depth. Fourteen organically distinct modules feed **seven independently decidable summative assessments** on one evolving service plus a controlled separate local participant; formative experiments are not hidden gates. No commercial platform, cloud subscription, paid queue, public domain or production data is required.

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

1. **From foundational API to an evolving domain contract** — Use actual APP3 and APP6 assessed service/source and tests to compare a once-correct HTTP endpoint with a change that crosses transactional, tenant and event boundaries. Explain the historical attraction and added complexity of independent services without a new protocol survey.

2. **One bounded business process and observable failure contract** — Choose an authenticated multi-step synthetic reservation/fulfilment-like workflow, distinct authoritative owners and one genuinely committed local participant or external fixture; specify which user action counts as complete.

3. **Strong invariants, durable facts and irreversible decisions** — Write an invariant, permitted eventual lag, irreversible pivot, privacy boundary and reachable failure state, then apply them to an example where HTTP timeout follows a committed database mutation.

4. **Measure real coupling and ownership before adding services** — Inspect actual imports, direct cross-module SQL, API consumers, change hotspots and shared resource pools, and demonstrate one defensible module seam plus an unwanted dependency.

5. **Compare module, durable worker and separate participant** — Use the same task to reason through in-process calls, database outbox/worker and independently committed local HTTP participant; identify genuine state/process ownership and when a broker or cluster solves no demonstrated problem.

6. **Falsifiable quality-attribute and cost hypothesis** — Predict one failure/consistency improvement and one new latency/operational cost of extracting a boundary, with competing explanations, data/tenant scale, real trace requirements and a no-extraction exit option.

*Optional practice — false-complexity decision:* Reject a fashionable service extraction without a justified data, failure or team ownership benefit.

### Module 2 — Domain Modeling, Aggregates, Modules and Fitness Tests

#### Outcomes

- APP11-O1
- APP11-O2
- APP11-O3
- APP11-O8

#### Lessons

1. **Domain language, ownership and inconsistent terminology** — Extract real commands/events/entities from the chosen task, test whether two use cases give an overloaded term different meanings, and allocate actual policy/transaction ownership without asserting every noun is an aggregate.

2. **Aggregate invariant and worked concurrency counterexample** — Model a scarce resource, reserved quantity or entitlement under two concurrent transactions and compare oversize aggregate locks versus a leaky undersized invariant; justify one atomic scope.

3. **Application policy versus HTTP framing** — Separate untrusted Fastify decoding and route errors from application decisions and domain state transitions, then run the same use case through a non-HTTP fixture to verify transport independence.

4. **Ports, dependency direction and integration failure seams** — Define narrow TypeScript interfaces for storage/time/outbound requests and test an alternate adapter, preserving runtime schema and explicit failure semantics rather than pretending interfaces enforce external trust.

5. **Public module surface and prohibited cross-owner writes** — Enforce a dependency/import rule and actual PostgreSQL role/adapter ownership where possible; demonstrate a seeded direct private-table write caught before the final integrated test.

6. **Compile-time shape, runtime schema and schema evolution** — Show a TypeScript-compatible unsafe message or JSON payload, validate it at the real API/event boundary and record version semantics for old/new consumers.

7. **Characterization-first modular refactor** — Start with externally observed authorized/denied Fastify, SQL and async outcomes, move a tangled use case behind a module boundary, and prove the refactor did not change committed facts or error/role semantics.

8. **Fitness gate with a real failing dependency violation** — Combine static import checks, actual adapter/contract tests and a seeded broken boundary, report what architecture tests cannot prove about runtime process failure and explain reviewer feedback.

### Module 3 — Transactional Consistency, Races and Authority

#### Outcomes

- APP11-O3
- APP11-O5
- APP11-O6
- APP11-O15

#### Lessons

1. **One PostgreSQL transaction and its authority limits** — Reuse APP4 transaction/isolation evidence on the selected business effect; draw which SQL rows and outbox intents can commit together versus independently committed or externally visible actions.

2. **Transaction-bound repository and intent write** — Use one real driver/connection transaction for domain + event intent, intentionally separate a repository's connection and observe the partial-commit bug before correcting ownership.

3. **Two-session business race and atomic deduplication** — Coordinate real independent PostgreSQL connections with barriers to prove constraint/version protection and atomically scoped idempotency; a process-local map cannot arbitrate two workers or a service restart.

4. **Isolation anomalies and conflicting writes in the actual backend** — Reproduce one actual read/write anomaly or serialization conflict with declared isolation mode, inspect SQL effects and distinguish safe retry conditions from repeating an irreversible external call.

5. **Commit sequence, aggregate version and event timestamp** — Trace two concurrent commits and queued events, demonstrate why created_at and dispatch order do not establish global or even aggregate business order, and specify the intended version rule.

6. **Lock waits, short transactions and load feedback** — Measure lock wait and pool occupation while a transaction performs slow work, then keep external calls outside protected SQL commit scope without losing durable intent.

7. **Dual write and uncertain external side effect** — Inject database rollback/HTTP send ambiguity and a crash between local commit and publish, identify the inconsistent outcomes and the narrow problem a transactional outbox solves.

*Optional practice — concurrent reservation bug:* Repair a double-claim or stale-state flow and verify one durable allowed outcome using independent SQL.

### Module 4 — Transactional Outbox, Dispatch and Lifecycle Guarantees

#### Outcomes

- APP11-O3
- APP11-O4
- APP11-O5
- APP11-O9
- APP11-O13

#### Lessons

1. **Dual-write failure states with genuinely observed outcomes** — Create a domain-commit/send failure matrix including rollback, crash before publish, send with lost ACK and replay, and show which SQL and consumer facts exist at each stage.

2. **Same-transaction domain fact and outbox event** — Insert a versioned domain mutation and event intent on the same PostgreSQL connection transaction; verify both commit or roll back under a real injected constraint/throw.

3. **Stable event IDs, owners, versions and minimal payloads** — Design event ID, aggregate key/version, event type/schema, tenant/safe actor scope and trace correlation without copying credentials or treating a caller-provided tenant as trusted authority.

4. **Claimed batches, SKIP LOCKED and lease failure semantics** — Implement a bounded PostgreSQL dispatcher with actual row claims or an explicit single-worker alternative; explain that SKIP LOCKED provides an **inconsistent queue-like view**, not global FIFO or a guarantee that a claimed row is delivered, and test competing worker claims.

5. **Send, uncertain acknowledgement and duplicate publishing** — Crash a worker after local consumer receipt but before marking the event sent, then inspect durable pending intent and possible duplicate delivery; distinguish a relay attempt from observed externally durable completion.

6. **Concurrent writers and per-aggregate ordering proof** — Use two writers and dispatchers to test an aggregate-version gap, with explicit claim/scheduling rule and consumer buffering/reconciliation; never assert created timestamps or SKIP LOCKED alone preserve key order.

7. **Outbox retention without destroying recovery history** — Design max age, bounded attempts, poison quarantine and archive/replay source ownership; distinguish a prunable dispatch outbox from an authoritative event log needed for a future full projection rebuild.

8. **Age, retries, orphaned claims and safe operator replay** — Measure pending age and attempt state with sanitized operation IDs, introduce a stuck claimed event and demonstrate recovery without double committed effects or silent deletion.

*Optional practice — outbox crash drill:* Kill the dispatcher at a controlled point, restart and confirm committed intent is eventually handled without duplicate business effects.

### Module 5 — Inbox Contracts, Duplicate Consumers and Event Evolution

#### Outcomes

- APP11-O4
- APP11-O5
- APP11-O7
- APP11-O9
- APP11-O10

#### Lessons

1. **Command request versus committed event fact** — Compare a command asking another owner to act with a versioned domain event recording what **already** committed, then test an invalid command that must not appear as a completed fact.

2. **Validate envelope and verify message authority** — Treat id, tenant, claimed actor, schema and payload as untrusted at receipt; require a trusted producer/boundary contract and re-evaluate owner policy rather than believe an event header.

3. **Atomic inbox key, fingerprint and business effect** — Use a durable inbox key scoped to consumer, tenant, event and optionally payload fingerprint **in the same local DB transaction as the protected effect**; reject same-key-different-payload ambiguity.

4. **Two consumer races, rollback and recovery** — Schedule parallel worker reads of the same event, force a transaction rollback after the inbox check, and inspect one completed effect and safe redelivery with actual unique constraints.

5. **ACK loss, transient retry and poison handling** — Reproduce effect committed/ack lost, transient failure and permanently invalid envelope as different states; use finite retries and meaningful quarantine rather than count successful handler calls.

6. **Aggregate version gaps and scoped ordering** — Deliver duplicate and out-of-order events, choose buffer/rebuild/refetch or rejection under an explicit per-key version invariant, and explain why global order and memory-only cursors are inadequate.

7. **Old/new reader, schema compatibility and contract break** — Test an additive/defaulted field and a breaking rename or changed semantics with independent old/new consumers; note schema compatibility tooling does not prove behavioral authorization or all historical replay.

8. **Replay scope, privacy expiry and dedup retention** — Reprocess synthetic historical events through a controlled consumer, guard deleted/private data and retention, and prevent expired dedup records from resurrecting an already committed effect.

*Optional practice — duplicate delivery repair:* Break a consumer with an acknowledgement race, repair it and show real DB invariants after repeated deliveries.

### Module 6 — Cross-Boundary Business Workflows and Compensation

#### Outcomes

- APP11-O3
- APP11-O4
- APP11-O5
- APP11-O6
- APP11-O9

#### Lessons

1. **Separately committed owners and why compensation is required** — Run a bounded two-owner workflow with a genuinely independent transaction or locally recorded irreversible fixture; distinguish it from a sequence of mocks within one rolled-back DB transaction.

2. **Durable saga states and allowed transitions** — Define reserve, pending, confirmed, compensating, compensated, failed, uncertain and manual-attention states with a clear legal transition table and user-visible truth.

3. **Choreography or orchestration chosen by evidence** — Trace the same two-step workflow under a message-choreographed versus durable coordinator design, compare misplaced ownership/coupling and pick one implementable local model.

4. **Local commit before cross-owner message and recovery** — Record each participant's local transaction/workflow progress and outbox intent before the next action; stop a process midstep and recover from durable state, not memory.

5. **Reversibility, pivot and compensation as a new action** — Work through a reservation/fulfillment step that is reversible versus irreversible; issue a compensating operation, preserve audit trail and avoid calling it rollback of earlier commits.

6. **Timeout, ambiguous remote outcome and no blind compensation** — Lose the result of a committed participant, then choose authoritative status reconciliation before retry or compensating; verify a late success cannot be overwritten by an outdated action.

7. **Concurrent sagas, semantic locks and stale compensation** — Schedule two reservation workflows and delayed compensation of the first; use actual version/ownership checks to protect the second's legitimate result.

8. **Compensation failure, retries and manual reconciliation** — Fail the compensating action itself, demonstrate bounded retry and terminal manual-review record with operator evidence, and distinguish an unresolved partial effect from a successful transaction.

*Optional practice — saga fault matrix:* Exercise good flow, failed step, duplicated event, timeout and failed compensation with traceable participant state.

### Module 7 — Materialized Projections, Lag and Reconciliation

#### Outcomes

- APP11-O3
- APP11-O5
- APP11-O7
- APP11-O10
- APP11-O13

#### Lessons

1. **One authoritative write source versus derived read state** — Model a business write and the denormalized projection it informs; show which queries can tolerate delay and which authorization/business mutations must consult authoritative state.

2. **Projection schema, event cursor and tenant safety** — Design materialized read rows with aggregate versions, source offsets, schema and tenant filter, then independently test a previous-tenant read after a permission change.

3. **Actual measured delivery lag versus invented replication** — Pause a controlled local projector, measure event-to-view delay and explicitly label it **application projection delay**, not PostgreSQL streaming replication or guaranteed convergence.

4. **Duplicate/older update and gap detection** — Deliver version 3 before 2 and replay 2 twice, show a prevented stale overwrite and what a detectable gap means for a currently displayed summary.

5. **Full rebuild requires retained authoritative history** — Compare a safe snapshot+subsequent retained event log with a pruned delivery outbox; implement a truly replayable rebuild or reconstruct from the current authoritative database, disclosing when missing history prevents exact recovery.

6. **Projection drift, reconciliation and missing events** — Create an omitted/double event, compare version/row counts and actual underlying authority, rebuild safely and report a user-relevant stale interval rather than only log a warning.

7. **Read-model secret/property and current-permission denial** — Exercise a removed role, sensitive field, deleted record and cross-tenant key after projection/permission changes, ensuring derived data never substitutes for current authorization.

8. **Read-your-writes and truthful pending/reconciled UI** — Use a controlled delayed view and actual primary result to choose wait, authoritative read or eventual UI status with an independent before/after user state check.

*Optional practice — lagged-order workflow:* Repair a user screen reporting completion while only an out-of-date projection exists.

### Module 8 — Process Boundaries, Contracts and Service Extraction Choices

#### Outcomes

- APP11-O1
- APP11-O2
- APP11-O8
- APP11-O11
- APP11-O14

#### Lessons

1. **In-process module versus real lifecycle isolation** — Compare one domain operation through same-process calls, a separately restartable worker and local HTTP service, recording actual commit, error and operational overhead.

2. **Process contract, deadline and lost-response semantics** — Define runtime-validated HTTP or durable command contract, finite request deadline, ambiguity after timeout and idempotent status/reconciliation, then test a partial response.

3. **Old/new independent consumer compatibility** — Run two differently versioned consumers against the same published schema with missing/defaulted fields and changed statuses, capturing an actual break and a repaired compatibility rule.

4. **Real service identity versus delegated end-user rights** — Show a trusted local service credential and a user-scoped authorization decision as distinct things; send forged forwarded identity via direct HTTP and verify denied DB effect.

5. **Restart, refusal, partial response and bounded wait** — Actually stop the separate participant during a protected request and compare connection refusal, failure-after-send and retry behavior, avoiding false claims of network partitions on one host.

6. **Causal correlation and safe trace propagation** — Propagate operation IDs and whitelisted context across two independently running processes, test clock/order limitations and exclude raw tokens and user-provided trust baggage.

7. **Separate write ownership and controlled violations** — Prohibit one participant modifying the other's authoritative table directly, demonstrate an import/SQL role violation caught by independent permission/invariant tests.

8. **Measured extraction premium and justified no split** — Compare the same task in a modular monolith versus the local split under matched accepted/failed traffic, source/ops burden, privacy and restart; explicitly allow retaining the monolith as the final design.

*Optional practice — contract-break investigation:* Repair an independently restarted service that silently changed a required contract or trust assumption.

### Module 9 — Queue Capacity, Backpressure and Worker Recovery

#### Outcomes

- APP11-O5
- APP11-O6
- APP11-O9
- APP11-O11
- APP11-O13

#### Lessons

1. **Durable job transport choice from measured needs** — Use the existing Postgres outbox/jobs or a free local worker rather than import a broker tutorial; name durable acceptance, ordering scope and priority policy for the chosen domain step.

2. **Claim ownership, lease expiry and lost worker ACK** — Demonstrate real claim/lease or a well-scoped single-worker alternative, kill the worker during an effect and recover without claiming lease expiration prevents duplicate processing.

3. **Worker limits against DB/remote pool budgets** — Vary bounded local concurrency and tenant load to measure committed work, queue age and pool wait; choose an observed safe limit rather than maximizing workers.

4. **Admission, backlog age and truthful refusal** — Set finite queue count/age/resources, distinguish refused uncommitted requests from accepted durable intent, and show status remains correct after an overload burst.

5. **Retry ownership, jitter and no amplification** — Trace attempted HTTP/API/worker/outbound requests on failure, remove duplicate retry owners and cap budget/jitter and interaction deadlines.

6. **Poison records, expiry and operator repair** — Quarantine a permanently invalid event or revoked tenant scope, show finite attempts and independently reviewable dead-letter/manual replay decision.

7. **Fairness under tenant skew and security boundaries** — Demonstrate a noisy tenant starving another's protected jobs, then enforce fair bounded capacity without letting a different tenant inspect another's jobs.

8. **Completed versus accepted with authoritative status** — Show actual domain/workflow state for accepted, processing, failed, reconciled and completed operations; a 202 or queue receipt is not evidence that business work finished.

*Optional practice — stalled-work failure:* Kill a worker during processing, restart/reclaim a safe lease and show no unintended duplicate business action.

### Module 10 — Tenant, Service Identity and Security Across Boundaries

#### Outcomes

- APP11-O5
- APP11-O7
- APP11-O8
- APP11-O10
- APP11-O15

#### Lessons

1. **Verified identity/authority graph across all owners** — Map real human principal, service actor, tenant/resource and domain action at HTTP, event, projection and worker handoff; distinguish identity propagation from policy authority.

2. **Independent authorization at actual execution point** — Prove an authorized API request cannot grant a consumer future privilege after role revocation; check action/object/read-write-property policy at each meaningful owner.

3. **Forged tenant envelope and stale principal** — Inject client-crafted headers and a future/old event claiming a different tenant; verify consumers validate trusted origin and current ownership rather than read an untrusted string.

4. **Inbox, projection and retry keys with tenant scope** — Collide two tenants' identical event IDs and expired dedup keys, showing independent state and no cross-tenant de-duplication or cached/private query leak.

5. **DB roles, event stores and least-privilege negative proof** — Configure scoped local database roles/paths for independently writing owners, attempt a forbidden table mutation and check real denied SQL effects.

6. **Noisy-neighbor quotas and payload-based resource abuse** — Send oversized/rapid synthetic tenant jobs, enforce meaningful body, memory, queue, concurrency and attempt budgets while preserving permitted work.

7. **Minimal event metadata, private attributes and retention** — Compare a dangerous payload copied into all events/logs with opaque identifiers and retention limits, verify private properties remain inaccessible under replay and operator inspection.

8. **Independent attack matrix with unchanged business facts** — Run direct API, forged envelope, wrong tenant event/projection, expired actor and job-status attacks, examining SQL/workflow state and safe redacted traces before/after correction.

*Optional practice — forged event drill:* Repair a consumer that trusts tenant identity from a producer message without independent authorization context.

### Module 11 — Partial Failure Containment, Deadline Budgets and Recovery

#### Outcomes

- APP11-O6
- APP11-O9
- APP11-O11
- APP11-O13
- APP11-O15

#### Lessons

1. **Critical/optional dependency fan-out and shared pools** — Build actual call/queue/DB resource graph and reproduce optional dependency latency exhausting critical capacity, unlike the APP8 general case by observing outbox/saga progress.

2. **End-to-end time budget with independent commits** — Allocate request, queue, participant and SQL deadlines in a sample trace; show canceling the caller cannot undo a committed later workflow step.

3. **Count actual retries and lost-ACK uncertain state** — Inject failed dependency after remote commit and count nested attempts; select one retry owner with idempotent reconciliation and finite backoff.

4. **Bulkhead/circuit decision from measured isolation** — Run a shared-pool failure and a measured alternate containment (capacity split/stop/circuit), justify complexity and avoid implying a breaker fixes database truth.

5. **Fail closed for security, degrade only optional work** — Show a user task that can lose optional analytics but not entitlement or durable mutation, with truthful HTTP/worker statuses and accessible pending state.

6. **Controlled ramp-up with pending saga/outbox records** — Recover a slow dependency under bounded replay/admission, measure queue age/attempts and ensure old unresolved compensations do not corrupt newer work.

7. **Reconcile conflicting local owners and failed compensation** — Compare actual owner/participant records and execute a safe operator action, recording which effects cannot be reversed and which unknown outcomes remain.

8. **Causal incident exercise with independent SQL truth** — Inject one new partial failure and construct sanitized request/worker/event/SQL timeline with competing explanations, then verify repair and unchanged tenant permissions.

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

1. **Business pressure and evolving responsibility boundary** — Identify one change hotspot with real old consumers, owned records and a measured cost/consistency risk; explain why remaining internal is also an acceptable architecture outcome.

2. **Branch by abstraction, controlled strangler and switches** — Introduce a small versioned adapter before a second implementation, test routing and health without deploying two production microservices.

3. **Old/new API, event, inbox and DB contract matrix** — Run actual old/current consumers of HTTP and event envelopes with changed status/field semantics, including replay of retained events and a documented incompatible case.

4. **Expandable schema and resumable source data migration** — Apply additive tables/fields, bounded backfill with interrupted resume and actual SQL row checks, then delay contraction until real old readers/writers leave.

5. **Read-only shadow without duplicate business writes** — Route a permitted side-effect-free alternate read through the candidate and compare results, proving the shadow does not repeat payments/jobs or leak private data.

6. **Owner transition, divergent writes and repair rule** — Model two state owners, replay/backfill lag and divergent writes, refusing unsafe unchecked dual writes and naming an authoritative repair source.

7. **Controlled route cutover and observed old-user behavior** — Switch limited local traffic/workers under a recorded operator decision, measure permitted/denied task, late events and state reconciliation rather than only /health.

8. **Compatible rollback or forward fix after pivot** — Inject a contract/data cutover defect, check real committed state and old/new consumers, execute safe reversal only where valid and demonstrate forward repair when irreversible work occurred.

*Optional practice — contract migration drill:* Seed an old-consumer break or stale projection during cutover, detect it and repair without losing legitimate state.

### Module 13 — Architecture Measurements, Operations and Economics

#### Outcomes

- APP11-O1
- APP11-O11
- APP11-O13
- APP11-O14

#### Lessons

1. **Quality-attribute fitness as measured contract** — Define change-cost, failure blast radius, security/privacy, operation success and version-compatibility measures for an actual backend workflow, not a generic architecture score.

2. **Matched workload, owner count and failure profiles** — Reuse APP6 test discipline for same payload/tenants/CPU/version, local process/network effects, error/timeout counting and limited samples; avoid pretending local loopback equals WAN.

3. **Business completion versus extra process latency** — Compare true completed authorized task and failure states between internal module and local split, measure serialisation, pool/queue cost and useful throughput with uncertainty.

4. **Durable age, stuck compensation and trace visibility** — Link sanitized causal operation/event IDs, outbox/inbox backlog, workflow owner state and stuck compensation with actual operator action; avoid raw tenant IDs and high-cardinality telemetry labels.

5. **Process, data, delivery and incident cost units** — Estimate explicit CPU/instance-hours, DB/pool, disk/retention, event delivery, monitoring and operator burden for both architectures; disclose source of any price assumptions.

6. **Traffic and failure sensitivity with no-split case** — Vary tenant skew, load, payload retention, failure rates and review/upgrade cost, naming the threshold where the monolith wins or separation becomes justified.

7. **Reviewable decision record and revisit trigger** — Record measured trade-off, failed hypotheses, model limits, personally defensible source, chosen extraction/no-extraction and a concrete future evidence threshold.

*Optional practice — no-benefit extraction:* Identify a service split that slows users and increases incidents despite satisfying a fashionable architecture diagram.

### Module 14 — One Evolving Backend and Independent Architecture Defense

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

1. **One existing backend and accepted evidence map** — Use one functioning APP3/APP6-based service and **reference** independently accepted APP11-AS1–AS6 judgments, capturing authoritative SQL ownership, module policy, event/replay and fault evidence rather than building seven standalone systems.

2. **Reproduce durable cross-owner behavior with real state** — From a clean locally provisioned setup, exercise a protected domain mutation through same-transaction outbox, independent consumer/inbox, delayed projection and separately committed saga action, including an actual interrupted worker.

3. **Preserve tenants, compatible contracts and recovery** — Recheck previously accepted action/object/property/tenant permission, backlog/compensation limits, old/new consumer and read-rebuild tests, choosing the smallest legitimate regression after the cumulative integration.

4. **Assessor supplies unfamiliar cross-owner fault** — Accept a new bounded outbox-ACK loss, event gap, stale permission, compensating race, contract change or worker saturation, predict the user/SQL failure and construct an independent before-fix oracle.

5. **Correct mechanism and independently verify committed truth** — Repair the selected causal issue or perform justified safe reconciliation, rerun affected HTTP/SQL/worker tests and compare matched observations; reject a false exactly-once or production-distribution claim.

6. **Accessible technical defense and justified architecture choice** — Explain the personally owned source, accepted AS1–AS6 artifacts, alternative monolith/process design, actual limits, cost and rejected extra infrastructure through an equivalent written/recorded/live review.

## Completion requirements

All **APP11-O1–APP11-O16** require **seven independently decidable summative assessments** on one evolving backend and controlled separately committed local participant. AS1 tests authoritative modules/real concurrency; AS2 actual outbox/inbox/derived state and crash recovery; AS3 compensable *and noncompensable* multi-owner workflows; AS4 tenant/resource trust under worker overload; AS5 observed old/new compatibility and safe extraction; AS6 causal incident economics; AS7 an independently reproduced **previously unseen bounded failure**. Accepted AS1–AS6 artifacts can be cited by reference, not duplicated across seven projects. Formative lessons, optional tools and this elective never add an APP9 graduation gate.

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
  - Work: Using the existing APP3/APP6 authenticated Fastify/PostgreSQL service, choose a real domain change with two plausible context boundaries and a specific consistency/coupling problem. Characterize the normal/forbidden API and actual SQL before refactor, implement an owner-respecting aggregate/module public interface, and enforce a failing-before/passing-after import/**direct cross-owner DB write** architecture rule. Schedule **two independent PostgreSQL connections** racing a business invariant and compare an in-process-only guard with actual constraint/version/transaction protection. Defend a no-extraction alternative and independent fault review.
  - Criteria: Before/after behavior is checked with real signed-in/denied HTTP and independently inspected SQL rows; new modules enforce actual dependency/ownership rather than rename files. A genuine concurrent schedule preserves the authoritative invariant with declared isolation/lock/retry semantics; no inferred SQL atomicity across separate remote commits. An actual injected cross-module import/write fails the appropriate enforcement, and two viable alternatives are judged against measured change, privacy and operating costs. Prior APP3/APP4 basics need not be reimplemented as extra assessments.
  - Evidence: Domain and change hypothesis, architecture dependency diagram and module contracts, source diff, complete signed-in/forbidden API regression suite, independent concurrent DB logs and constraints, fitness-rule failure/pass, ADR and limitations.

- **APP11-AS2** (required atomic outbox, inbox idempotency and replayable handoff)
  - Outcomes: APP11-O3, APP11-O4, APP11-O5, APP11-O7, APP11-O9, APP11-O13, APP11-O15
  - Work: Write one protected domain mutation and **versioned outbox intent in the same real PostgreSQL transaction**; verify rollback cannot leave a publishable event. Run an actual separately controlled dispatcher and consumer with **consumer/tenant/event-scoped durable inbox + business effect in one local consumer transaction**, and a derived projection. Inject committed-pending-before-dispatch, **sent/received-before-relay-ACK crash**, racing same-event/different-fingerprint consumers, duplicate/out-of-order aggregate versions, a permanently invalid/poison payload, restart and a genuine projection rebuild from **retained authoritative history or current owned-state resnapshot**. Test row claiming and explicitly justify ordering; PostgreSQL SKIP LOCKED is a queue convenience, **not FIFO or complete business-history proof**.
  - Criteria: Independent SQL and actual process/consumer observations prove same-transaction domain+intent or neither, durable pending recovery and **possible repeated dispatch** after lost acknowledgement. The inbox and protected consumer effect atomically enforce the tested dedup scope, including different-tenant/same-ID and same-key-different-payload cases, without claiming exactly-once remote delivery. Out-of-order versions cannot silently overwrite newer projections, and a genuine rebuild is possible from a declared complete source; a pruned outbox is not silently treated as an append-only event log. Backlog/claim/poison retry and privacy limits are bounded and observable.
  - Evidence: Outbox/inbox schemas and SQL transaction, event envelope/contracts and dispatcher/worker code, failure injection scripts, version/order/idempotency/poison tests and DB before/after records, projection rebuild and privacy-safe state/correlation logs.

- **APP11-AS3** (required multi-step coordination, compensation and failure recovery)
  - Outcomes: APP11-O3, APP11-O5, APP11-O6, APP11-O9, APP11-O11, APP11-O13, APP11-O15
  - Work: Implement a **durably recorded two-owner** local business workflow using a second actual PostgreSQL transaction authority or real stateful HTTP participant with independently verifiable effects. Demonstrate success, duplicate command, timeout **after remote commit with lost response**, legitimate concurrent workflow and stale compensation attempt, a failed following step, compensating transaction, *failed compensation* and explicit operator reconciliation. Record legal state transitions, owner/tenant permissions, reversible actions, **irreversible pivot**, bounded retry decisions and truthful user accepted/pending/uncertain/completed state, checking authoritative records after process restart.
  - Criteria: The two participants truly commit independently—sequencing mocked functions inside one SQL transaction cannot pass. Unknown remote outcome is checked before blind repeat/compensation, local durable state supports restart and cross-workflow semantic locking/version guard blocks stale compensation. Compensating work is an auditable **new** action that can fail; irreversible effects are not reported undone, and failed compensation remains an honest bounded manual/retry state. Independent HTTP/SQL records establish end-user authorization and final durable facts.
  - Evidence: Workflow state diagram and transition policy, separately observed local participants and DBs/fixtures, complete fault/compensation matrix, real traces and SQL effects, user-facing status examples, operator reconciliation runbook and unsupported-guarantee notes.

- **APP11-AS4** (required cross-boundary tenant trust and bounded resource safety)
  - Outcomes: APP11-O5, APP11-O7, APP11-O8, APP11-O9, APP11-O10, APP11-O11, APP11-O15
  - Work: On the running two-owner backend, trace verified human and **separate service** identity through HTTP, outbox/inbox, worker, derived projection and job-status queries. Inject actual forged tenant/role headers and envelopes, expired or revoked user permissions, same message ID in two tenants, forbidden read/write properties and a tenant-skew burst against a slow local dependency. Verify real protected DB and message state, introduce bounded payload/queue/claim/worker/pool and retry budgets, and recheck legitimate other-tenant progress under overload and after recovery.
  - Criteria: Each authoritative execution owner independently checks permitted action/object/read-write property and current tenant scope; a locally trusted service credential does not grant unverified end-user permission. Forged headers/events, replayed dedup IDs and stale projections do not leak or alter another tenant's source/inbox/projection, as demonstrated by actual denied HTTP/message and unchanged PostgreSQL facts. Overload limits produce measured finite pending/denied/committed results without silent loss or unbounded retries; telemetry carries no sensitive attributes.
  - Evidence: Trust-boundary and access matrix, tenant/worker identities and limits, adversarial synthetic HTTP/envelope scripts, DB row/queue/error/timing evidence, before/after authorization and contention tests and remaining risks.

- **APP11-AS5** (required incremental backend extraction and versioned contract compatibility)
  - Outcomes: APP11-O1, APP11-O2, APP11-O5, APP11-O7, APP11-O8, APP11-O12, APP11-O14
  - Work: Starting from one proven modular backend and measured ownership/change pressure, implement a versioned adapter and a **real separate locally restartable participant/worker** for one bounded contract, compare its task cost to an internal-module alternative and run independent old/current HTTP/event/worker clients. Stage an actually applied compatible PostgreSQL schema/projection change with **interrupted and resumed backfill** where needed, safely **shadow only side-effect-free reads** (or justify and evidence an equivalent safe comparison), then switch limited local requests. Inject an old-consumer break or projected stale result and demonstrate a compatible rollback or **forward repair** when committed effects cannot safely be reversed.
  - Criteria: The alternate process contract actually runs and fails under controlled isolation; the chosen final architecture may remain a modular monolith, but no purely theoretical drawing satisfies cross-process competence. Tests independently exercise old/new consumer and replay/tenant/SQL behavior, with actual previous and current database rows, an observed compatibility fault and safe staged backfill. No shadow duplicate writes, unchecked dual write or tenant-scope bypass; a code rollback is never claimed to reverse already committed owner transactions or irreversible compensating/pivot actions. The extraction decision includes attributable costs and future reconsideration threshold.
  - Evidence: ADR and business trigger, old/new sequence and contract matrix, adapter/feature-switch code, migration/backfill and safe shadow evidence, controlled failure/release choice, SQL/user security invariants, operational cost/limits and reproducible test recipe.

- **APP11-AS6** (required architecture failure, observability and economic decision)
  - Outcomes: APP11-O1, APP11-O8, APP11-O9, APP11-O11, APP11-O13, APP11-O14
  - Work: Using **the same evolving system**, run matched low-resource and bounded burst scenarios for monolith/module versus local process boundary with real synthetic tenant mix, SQL and queue/worker work, measuring **eligible completed authorized business tasks**, timeouts/rejections, latency distribution/sample count and resource/pool limits. Inject a *new* dependency or stuck outbox/compensation problem distinct from the earlier AS2/AS3 fault replay, collect sanitized cross-process causal HTTP/SQL/event/inbox/workflow evidence, compare competing root causes, apply one justified mitigation or operator reconciliation and remeasure. Price alternatives with explicit illustrative compute/DB/worker/telemetry/incident/maintenance units and sensitivity.
  - Criteria: A newly introduced fault is actually observed and repaired before/after, not just a reused screenshot/trace from other assessments. Useful completed business effects, failed/queued work, sample variance and process overhead are visible, and external/multi-region reliability is not inferred from loopback. The repair preserves cross-tenant authorization, committed facts and bounded retry; safe no-split decisions may be preferable. Quantitative operating costs and uncertainty are explicit without fabricated live hosted rates or unsupported uptime claims.
  - Evidence: Reproducible workload/fault scripts and profiles, real HTTP/SQL/worker traces with safe correlation, before/after outcomes, incident/reconciliation timeline, component/owner cost comparison, architecture fitness rubric, ADR and limitations.

- **APP11-AS7** (required integrated architecture and independent boundary defense)
  - Outcomes: APP11-O1, APP11-O2, APP11-O3, APP11-O4, APP11-O5, APP11-O6, APP11-O7, APP11-O8, APP11-O9, APP11-O10, APP11-O11, APP11-O12, APP11-O13, APP11-O14, APP11-O15, APP11-O16
  - Work: Present **one** actual APP3/APP6-based backend evolving through APP11, and **reference independently accepted APP11-AS1–AS6 evidence** instead of building separate projects or resubmitting each entire log/diagram. From a clean documented free local environment demonstrate representative authorized and forbidden HTTP, real independent PostgreSQL transaction/claim, independently running consumer, duplicate/lost-ACK outbox/inbox, durable two-owner saga with failed compensation handling, reconstructible projection, compatible old/new client route, and bounded process failure. An assessor supplies a **previously unseen but public-scope** aggregate race, duplicate/out-of-order event, forged tenant permission, state gap, compensation failure, consumer migration or overload scenario. Predict failure, obtain an independent before-fix authoritative oracle, apply a narrowly causal fix or safe reconciliation, rerun targeted prior regressions and defend whether extracting another service would improve the product.
  - Criteria: All APP11-AS1–AS6 judgments remain **separately passing**; APP11-AS7 cannot substitute for missing evidence or make this elective an APP9 prerequisite. Clean local setup and genuine process/SQL failures permit independent review; a rehearsal of a known previous fault cannot pass as unfamiliar transfer. Corrected behavior is shown with actual before/after SQL/HTTP/worker and tenant-denied facts, not curated traces alone; local process isolation never implies distributed partition tolerance, globally ordered events or exactly-once remote effects. One optional small participant is sufficient and a monolith-first final choice may prevail under measured costs.
  - Evidence: One versioned APP3/APP6 source and pinned free local fixture, **outcome-to-previously-accepted-APP11-AS1–AS6 evidence index**, selected independently inspected SQL/HTTP/consumer/replay/compensation and security tests, actual incident/contract/architecture decision, new unseen assessor scenario and before/after targeted regressions, real-versus-simulated guarantees/cost limits and accessible written/recorded/live technical defense.

### Completion, academic status and historical revision

APP11 completion requires acceptable independently inspectable decisions for `APP11-AS1` through `APP11-AS7`, collectively establishing `APP11-O1` through `APP11-O16`. A successful demo of two HTTP endpoints or more Kubernetes resources does not compensate for broken domain ownership, transaction consistency, lost message handling, compensation safety, tenant isolation, incompatible consumers, unobservable incidents or unsupported economic claims.

Retain OEE/course revision, relevant outcome and assessment IDs, source/artifact identities, local environment, contracts and synthetic fixture identities, actual failure and independent SQL evidence, race/duplicate/compensation and security negatives, matched measurements, ADR/rollback decision, accessible technical defense, limitations and reviewer decision under [OEE Evidence Rules](../../spec/evidence-rules.md).

APP11 remains an optional OEE `v0.2.0` `draft` course requiring APP3, APP4 and APP6. APP9 graduation does not depend on this specialization. Preserve independently evaluated source/specification revisions, assessment decisions and evidence references when a learner or implementation advances to a newer course revision. Structural CI cannot establish learner-tested readiness, formal educational conformance or production fault-tolerance guarantees.

### Public non-mandatory technical references

These resources inform independent investigation; they introduce no hidden assessment, required commercial system or extra completion gate.

- [AWS Prescriptive Guidance — Transactional outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html) for atomic event intent versus duplicate-delivery risks.
- [Azure Architecture Center — Saga pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) for compensations, pivots, coordination, irreversibility and fault boundaries.
- [Martin Fowler — Bounded Context](https://martinfowler.com/bliki/BoundedContext.html) and [Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html) for domain language and incremental system evolution.
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) and [explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) for independent concurrency evidence.
- [Microsoft Architecture Center — Compensating Transaction](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction) and [Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) for qualified recovery and containment.
- [OWASP API Security Project](https://owasp.org/www-project-api-security/) for broken object/property authorization and data exposure review.
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/) for observed incident and operator evidence.
