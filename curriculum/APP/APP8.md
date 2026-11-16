# APP8 — Production Application Architecture

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP5](APP5.md) — Full-Stack Application Architecture, [APP6](APP6.md) — Software Quality & Engineering Operations, [APP7](APP7.md) — Deployment, Cloud & DevOps
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; calibrate with learner and reviewer evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

**Evolve an existing deployed application architecture only when a
measured growth, data, correctness, latency, availability or cost
constraint justifies change.** Profile realistic workload and queueing,
localize the dominant bottleneck, select admission control or work
partitioning, evaluate caching and database-consistency policies,
contain dependency cascades and execute a deliberately reversible
architecture improvement. Preserve tenant/security boundaries and
user-visible correctness while comparing performance, complexity
and total operating cost.

The **direct prerequisites are APP5, APP6 and APP7**, as specified by
the reviewed APP program architecture. APP5 provides the credible
authenticated React/TypeScript/Fastify/PostgreSQL product, transactional
and asynchronous workflows, tenant-scoped data and observable failures.
APP6 establishes risk-based verification, meaningful telemetry,
representative load testing, SLI/SLO reasoning, reproducible
quality gates and incident investigation. APP7 establishes deployable
artifacts, secure ingress, isolated environments, stateful-compatible
releases and independent backup/restore. APP8 **does not re-teach**
these foundations: it builds and defends *architecture-level* decisions
driven by changed workload and failure constraints.

**A more distributed design is not inherently a better design.**
Begin with the known-good modular-monolith baseline. Compare removing
unnecessary work, query/index improvements, pool sizing, rate and
concurrency limits, local batching, bounded workers, caching,
vertical capacity and horizontal service replicas **before** proposing
a service split, message broker or database partitioning. Increased
service count brings failure domains, consistency coordination, API
compatibility, tracing, operational cost and security work.
APP11 (elective) and SYS may deepen distributed protocols and
multi-service internals, but **no APP8 graduate must build Kafka,
Kubernetes, a distributed sharded database or a paid service**
to satisfy the core.

**Evidence requires an appropriate workload and honest model.**
Use a repeatable bounded local scenario with tenant/user mix,
known data scale, explicit client arrival schedule, run duration,
warm/cold states, sample counts and generator capacity. Interpret
throughput, in-flight concurrency, response distribution and
resource/queue timings together. Tail latency often increases
under saturation; a hidden generator bottleneck or coordinated
omission can make a system look faster than users experience.
Little's law describes a stable system under consistent steady-state
definitions; do **not** mechanically apply it to an ever-growing
overload backlog. SLO and error-budget calculations from APP6
inform design priorities but do not establish real-world uptime
from a synthetic laboratory trace.

**Overload, caching and asynchronous work must remain correct.**
Measure queue admission, deadlines, bounded retries, per-tenant
quotas/fairness, backpressure, job recovery and circuit-breaker or
bulkhead choices *where justified*. Rejected and degraded outcomes
must be honest to the user; a fast 200 response that never commits
the requested effect is not reliability. A database transaction
cannot atomically commit an external effect, a timeout does not
undo a server-side mutation, and a queued event is not inherently
exactly-once. Cache keys and replicas may not override the
authoritative server-side access policy or leak a prior tenant's
data; a lagged read model is inappropriate as a source of truth
for a protected transactional decision.

**Strong invariants require real evidence.** Use actual local
PostgreSQL sessions for concurrent writes, constraints, isolation
and durable state verification. A controllable delayed-read
adapter may teach replica-lag/client reconciliation *if clearly
identified as a simulation*; it is not proof of actual PostgreSQL
streaming replication. Live multi-replica deployment, distributed
consensus, managed Redis, external brokers and public load tests
are optional exploration, not mandatory study infrastructure.

**The locally reproducible reference** is the APP7 deployed
application with its APP6 metrics/tests, synthetic tenant fixtures,
PostgreSQL, locally controlled worker and dependency failure
simulator and an open-source bounded load generator. Tools may
be freely pre-provisioned; core exercises must run thereafter
using documented local resources without a credit card, public
endpoint or production secret. Use synthetic data and named
disposable databases and never apply load, exploits or fault
injection to an unauthorized third-party service.

**Compare architecture alternatives on their full effects.**
A candidate change must be observed under matched client and
server conditions and keep real authorized/forbidden workflows,
transactional data, idempotency, cache authorization, accessible
degraded status, API compatibility and recovery correct.
Estimate CPU, memory, DB pool, replica/cache/storage, egress,
queued work and operational/maintenance burden under declared
units and assumptions. A lower-complexity design that meets
the targets is often preferable to a novel mechanism without
measured benefit. Demonstrate safe staged switching and
rollback or forward repair when committed state cannot be
reversed by simply replacing application code.

The provisional 14–18-week duration and 10–14-hour weekly
workload are planning assumptions, **not** educational readiness
evidence. All lesson investigations are formative unless included
in one of the seven publicly required summative assessments.
One evolving product with separately inspectable evidence
can satisfy them all.

## Learning outcomes

- **APP8-O1:** Turn a credible application growth or failure scenario into measurable user-task, throughput, latency, security, consistency, availability and cost objectives, prioritizing risks and retaining evidence provenance.
- **APP8-O2:** Construct a representative, reproducible workload with stated arrival model, tenant/task mix, data volume, warm-up, sampling and controlled generator limits; identify coordinated omission, cache effects and misleading aggregate metrics.
- **APP8-O3:** Explain and quantify service utilization, concurrency, queues, service time, waiting time, tail latency and saturation using valid measurement and capacity models; apply Little's law only under its stated stable-system assumptions.
- **APP8-O4:** Locate a demonstrable bottleneck using correlated application, Node/runtime, database and dependency metrics and choose a justified vertical, horizontal, partitioning or work-reduction response without assuming replication automatically improves every workload.
- **APP8-O5:** Implement and verify bounded overload admission, quotas, fair tenant scheduling, backpressure, deadline and load-shedding policies with observable latency, rejection, saturation and starvation behavior.
- **APP8-O6:** Evaluate synchronous work against bounded queues/workers and durable intent, choose safe concurrency and backlog limits, and test delayed, duplicate, failed or restarted work without claiming exactly-once effects.
- **APP8-O7:** Select, implement and compare cache placement, keys, freshness, eviction, invalidation and request-coalescing strategies against a measured workload, preserving sensitive tenant/permission boundaries and observable consistency.
- **APP8-O8:** Compare relational database connection limits, query/index work, read replicas, partitioning and caching under realistic contention, read/write amplification, stale reads and operational trade-offs; distinguish simulated lag from actual replicated storage.
- **APP8-O9:** Enforce a specified business invariant across simultaneous updates, retries, idempotency records, request ordering and stale/lagged views with independent PostgreSQL checks and explicit client reconciliation.
- **APP8-O10:** Design and measure dependency-failure containment using bounded timeout budgets, retry ownership, circuit breaking, resource isolation, bulkheads and correct fallback policy while preventing amplified traffic and forbidden fail-open behavior.
- **APP8-O11:** Define and verify a user-centered degraded-service contract and availability decision, balancing successful tasks, tail latency, error budgets, noncritical feature shedding and service recovery without weakening authorization or transactional correctness.
- **APP8-O12:** Conduct controlled comparative architecture experiments with fixed workload and environment, repeated trials, numerical uncertainty and negative-path verification, stating which effects are causal, correlated or untested.
- **APP8-O13:** Introduce a production-architecture boundary incrementally with versioned contracts, an old/new compatibility matrix, reversible traffic/feature selection and a justified rollback or forward-repair rule for persistent data changes.
- **APP8-O14:** Quantify performance, resilience, implementation/maintenance complexity, operational ownership and marginal compute/storage/egress costs across at least two plausible designs, documenting a decision and a less-complex baseline.
- **APP8-O15:** Maintain system-level privacy and security through scaling and evolution, including tenant-fair capacity, authorization in caches/queues/read models, retry/replica replay safety, data minimization and bounded abuse controls.
- **APP8-O16:** Reproduce, implement, evaluate and independently defend a measured production-application architectural improvement under an unfamiliar bounded growth, saturation, consistency, failure or cost constraint.

## Modules

### Module 1 — Production Architecture as Measurable Engineering

#### Outcomes

- APP8-O1
- APP8-O4
- APP8-O12
- APP8-O14

#### Lessons

1. **From deployment to architectural evolution** — Locate APP8 after APP7's secure deployment, backup/release and APP6's quality/telemetry foundations; identify the *new* architectural decisions demanded by changing workload and failure patterns.

2. **User task and product constraint** — Choose one high-value authenticated workflow and define real success, forbidden behavior and important state transitions rather than treating HTTP 200 as universal user success.

3. **History of application scaling approaches** — Contrast single-process, scale-up, scale-out, caching and partitioned service approaches as historical responses to constraints, not inevitable maturity levels.

4. **Stakeholders, assumptions and provenance** — Separate synthetic workload forecasts, measured local traces and independently observed user behavior; never pass estimates off as production measurements.

5. **Service-level and data-risk objectives** — Derive bounded latency/throughput, tail, availability, correctness, privacy and maintainability objectives with explicit sample/window and failure definitions.

6. **Operating responsibility and architectural ownership** — Map browser, API, database, queue, cache, proxy and external dependencies to owners and authority boundaries; inherit APP7's release mechanisms.

7. **Baseline before architecture changes** — Preserve the simplest verified modular-monolith baseline, its deployment identity and supported consumer contracts before experimenting.

8. **Change hypothesis and falsifiability** — Describe how a proposed architecture improvement should affect measured user behavior and which counterexample could disprove the hypothesis.

9. **Formative architecture review** — Reject a proposed microservice split unsupported by workload data and identify a measurable alternative with lower cost and risk.

### Module 2 — Workload Characterization, Measurement Quality and Test Harnesses

#### Outcomes

- APP8-O1
- APP8-O2
- APP8-O3
- APP8-O12

#### Lessons

1. **Arrival patterns and client behavior** — Distinguish open versus closed-loop load generators and choose a workload consistent with the expected user/task arrivals.

2. **Tenant and endpoint mix** — Represent authorized/denied, read/write, small/large payload and hot/cold resource distributions rather than one artificial endpoint.

3. **Data scale and skew** — Control row count, fan-out, hot keys and tenant size with synthetic reproducible seeds and declare how they differ from unknown production patterns.

4. **Warm-up, caches and JIT** — Record relevant runtime warm-up, DB page cache, browser cache and fixture initialization effects with separate cold/warm observations.

5. **Tail latency, percentiles and sample sizes** — Capture p50/p95/p99 or relevant distribution with request counts, confidence/variance limits and the distinction between percentiles and averages.

6. **Coordinated omission and load-generator saturation** — Show how a blocked/underpowered generator can under-sample slow requests and report both scheduled and completed work.

7. **Observation and sampling bias** — Correlate user completion, failed responses, timeouts, dropped requests and traces without treating unobserved traffic as success.

8. **Fixed baseline protocol** — Record CPU/RAM/OS, versions, concurrency, data seed, duration and instrument overhead to make comparisons meaningful.

9. **Formative invalid experiment** — Detect a suspicious throughput gain caused by an accidentally warmed cache, changed response shape or underdriving client.

### Module 3 — Queueing Theory, Concurrency and Capacity Boundaries

#### Outcomes

- APP8-O2
- APP8-O3
- APP8-O4
- APP8-O5

#### Lessons

1. **Throughput, concurrency, latency and occupancy** — Define completed operations/time, in-flight requests and service duration using actual measurement units.

2. **Little's law and assumptions** — Apply L = λW to a stable system with consistent boundaries/averages; explain why overload and growing backlogs violate casual steady-state calculations.

3. **Service time versus wait time** — Decompose time into arrival, admission, queue, CPU/IO, database pool, external dependency and return path.

4. **Utilization and nonlinear tails** — Observe increased tail delay near resource saturation without assuming a universal fixed curve or deterministic behavior.

5. **Capacity planning with safety margins** — Estimate bounded demand from arrival rate and measured resource requirement, including headroom and burst assumptions.

6. **Concurrency pools and semaphore limits** — Test thread/event-loop-adjacent work, DB pool and worker concurrency budgets with a reproducible local setup.

7. **Queue length and wait-time growth** — Measure backlog under load and discuss stable versus unbounded queue behavior and error/timeout consequences.

8. **Admission, rejection and work conservation** — Choose explicit enqueue/reject/defer policy for tasks with different deadlines and protect invariants under overload.

9. **Formative saturation worksheet** — Calculate response/wait/queue quantities on a supplied local trace and identify invalid inference under overload.

### Module 4 — Profiling the Actual System and Removing Work

#### Outcomes

- APP8-O3
- APP8-O4
- APP8-O12
- APP8-O14

#### Lessons

1. **Trace the critical path** — Map a specific user action through React, Fastify, SQL, worker and outbound mock to real timing and status evidence.

2. **Event loop and CPU contention** — Observe blocking CPU work, garbage collection, memory pressure and Node event-loop lag without confusing async syntax with parallel CPU execution.

3. **SQL execution plans and indexes** — Reuse APP4/APP3 to inspect a slow query, its plan and row counts, testing a measurable index/query change.

4. **Database connection-pool waiting** — Distinguish slow SQL from saturated pool, long-held transactions and connection setup or lock contention.

5. **N+1 and read amplification** — Identify repeated database/service requests and reduce work through appropriate query shaping or bounded batching.

6. **Serialization and transfer cost** — Measure payload size, JSON serialization, compression/proxy cost and browser work; avoid attributing all latency to backend execution.

7. **Memory and queue capacity** — Measure resident memory, queued objects and per-request allocation under a declared workload, preventing misleading low-load conclusions.

8. **Compare removing work versus adding machines** — Test optimization before scale-out and explain when extra capacity remains justified.

9. **Formative bottleneck triage** — Reject a CPU-scaling proposal when pool contention or query fan-out is the actual limiting factor.

### Module 5 — Vertical, Horizontal and Partitioned Scaling Choices

#### Outcomes

- APP8-O1
- APP8-O4
- APP8-O8
- APP8-O12
- APP8-O14

#### Lessons

1. **Scale-up economics and failure limits** — Compare more CPU/RAM/IO on one instance with actual bottleneck resources, upgrade downtime and single-failure-domain risk.

2. **Horizontal scaling and stateless handlers** — Identify sticky in-memory state, session, worker, scheduler and file assumptions before adding service replicas.

3. **Shared resources as bottlenecks** — Explain why additional API instances can worsen database connections, locks, cache misses or remote service limits.

4. **Connection and resource budgeting across replicas** — Calculate safe per-instance pool size from a declared shared DB budget and reserved capacity.

5. **Request routing and traffic locality** — Compare simple proxy balancing/affinity and their impact on cache behavior, hot tenants and failure.

6. **Partitioning by domain or tenant** — Reason about key selection, skew, cross-partition operations, ownership and operational burden without a mandatory sharded cluster.

7. **Hot partitions and uneven load** — Measure or simulate skewed tenant/key demand and compare a rebalanced scheme against the baseline.

8. **When not to distribute** — Quantify extra consistency, deployment, tracing and ownership costs of a proposed split.

9. **Formative scaling decision** — Use measured bottleneck plus DB capacity limits to defend vertical upgrade, query repair, horizontal scale or no change.

### Module 6 — Overload Admission, Rate Limits and Tenant Fairness

#### Outcomes

- APP8-O3
- APP8-O5
- APP8-O10
- APP8-O11
- APP8-O15

#### Lessons

1. **Overload versus ordinary traffic growth** — Define resource exhaustion, burst absorption, failure latency and user impact instead of declaring any slow response an overload incident.

2. **Admission control and bounded queues** — Set capacity and backlog limits with deliberate rejection or deferral semantics, never unbounded memory accumulation.

3. **Token bucket and fixed-window boundaries** — Compare plausible limiter semantics, burst behavior, implementation scope and known distributed-instance limitations.

4. **Per-identity and per-tenant fairness** — Distinguish anonymous, authenticated and privileged task priority while preventing one synthetic tenant from starving others.

5. **Deadline propagation and budget allocation** — Apply end-to-end time budgets to queueing, DB and upstream calls, with reasonable cancellation and uncertainty about already-committed effects.

6. **HTTP overload responses and client behavior** — Use honest 429/503 or equivalent documented errors, Retry-After where appropriate and meaningful accessible retry guidance.

7. **Queue shedding versus work loss** — Specify which tasks may be dropped, postponed or rejected and which durable mutation intents cannot simply disappear.

8. **Compare pre/post admission under burst** — Measure p95, success rate, rejection fraction, queue growth, throughput and tenant fairness with a controlled workload.

9. **Formative abusive burst** — Repair a single-tenant load pattern that saturates shared capacity or causes a misleading fallback authorization bypass.

### Module 7 — Background Work, Queues, Backpressure and Replay

#### Outcomes

- APP8-O5
- APP8-O6
- APP8-O9
- APP8-O10

#### Lessons

1. **Synchronous versus asynchronous product contract** — Choose inline execution or durable accepted work based on user deadlines, business result and failure honesty.

2. **Queue boundedness and ownership** — Select maximum age, depth, concurrency, retry attempts and worker ownership while preventing silently dropped committed work.

3. **Backpressure and upstream signals** — Compare blocking/deferral, rejecting new work and queue partitioning as workload protection mechanisms.

4. **Durable intent from APP5** — Reuse PostgreSQL outbox/job state to explain at-least-once dispatch and why ephemeral in-process queues are not durable.

5. **Worker concurrency and downstream capacity** — Tune consumer count against actual pool/remote API limits rather than assuming more workers always improve throughput.

6. **Priority and fair scheduling** — Assess starvation, slow tasks, per-tenant quotas and consequences of adding priority lanes.

7. **Duplicate delivery and visibility timeout** — Simulate lost acknowledgements, redelivery and expiration with safe idempotent consumer handling.

8. **Poison messages and terminal failures** — Bound retries/backoff, identify permanently invalid jobs and preserve recoverable human-facing states.

9. **Formative worker crash under burst** — Restart a disposable worker with pending and duplicate work, then inspect actual durable state and no double business effect.

### Module 8 — Cache Hierarchies, Coherence, Stampedes and Data Privacy

#### Outcomes

- APP8-O7
- APP8-O8
- APP8-O9
- APP8-O15

#### Lessons

1. **Cache layers and workload goals** — Compare browser HTTP cache, React memory, API-process memoization, shared cache and database query reuse for a defined bottleneck.

2. **Cache key scope and tenant authorization** — Include validated resource/tenant/permissions/version attributes where necessary and avoid cross-user cache collisions.

3. **Freshness, TTL and invalidation** — Define expiration, explicit mutation invalidation, revision checking and stale-while-revalidate behavior with appropriate security guarantees.

4. **Cold-cache and warm-cache experiments** — Measure hit ratio, tail latency, extra DB load and memory cost under matched request distributions.

5. **Cache stampedes and request coalescing** — Reproduce a hot-key miss burst, then use controlled single-flight, jitter or bounded concurrency without globally blocking unrelated keys.

6. **Negative caching and error risk** — Evaluate whether 404/error responses may be cached safely and how authorization changes affect that decision.

7. **Consistency with writes and replay** — Prevent a stale cache from reviving an invalid record or overriding a newer committed state after retries.

8. **Cache failure and bypass policy** — Define whether protected reads may bypass cache, fail closed or report degraded service without leaking tenant data.

9. **Formative stale identity leak** — Fix a synthetic previous-user cache leak that only appears under concurrent session changes.

### Module 9 — Data-Intensive Boundaries, Replicas and Consistency

#### Outcomes

- APP8-O4
- APP8-O8
- APP8-O9
- APP8-O13
- APP8-O15

#### Lessons

1. **Workload-dependent database topology** — Estimate read/write mix, query shape, storage growth and transaction contention before choosing replicas or partitions.

2. **Read replicas versus authoritative primary** — Explain asynchronous replication and read-your-writes assumptions; do not represent a locally delayed fake as real PostgreSQL streaming replication.

3. **Controlled lag experiment** — Use a documented injected delayed-read adapter or actual supported local replication to show stale results and client reconciliation.

4. **Strong consistency for protected mutations** — Keep authorization, quota and money/inventory-like invariants on authoritative transactional paths with real PostgreSQL tests.

5. **Index, partition and materialized-view tradeoffs** — Compare improved query plans, write/index amplification, maintenance and stale projections under observed workload.

6. **Lock/contention and isolation** — Demonstrate an actual two-connection concurrent update and correct serializable/revision conflict handling.

7. **Connection pool and follower consistency** — Identify pool exhaustion, read routing and race effects in mixed-version or replica-lag environments.

8. **Schema migration with active traffic** — Plan expand/backfill/contract compatible with existing reads/writes, quantifying lock and backfill uncertainty.

9. **Formative replica misuse** — Repair a workflow that uses lagged data for an authorization or strongly consistent write decision.

### Module 10 — Idempotency, Ordering and Event-Driven Correctness

#### Outcomes

- APP8-O6
- APP8-O8
- APP8-O9
- APP8-O10
- APP8-O15

#### Lessons

1. **Idempotency scope and business meaning** — Distinguish HTTP method properties from tenant/user/operation-specific deduplication of effects.

2. **Request fingerprints and TTL** — Bind keys to authenticated scope and validated payload; test same-key mismatched input and expiry policies.

3. **Atomic state and deduplication** — Store idempotency result/intention transactionally with affected domain rows when required to avoid race windows.

4. **Concurrency and optimistic versions** — Use actual PostgreSQL conflict/revision checks to avoid lost updates and duplicated committed changes.

5. **Out-of-order response completion** — Prove a late response does not replace more recent UI or account state under client navigation and retries.

6. **Worker redelivery and external calls** — Describe at-least-once delivery, limited external guarantees and mechanisms to reconcile uncertain remote effects.

7. **Event ordering and partition keys** — Evaluate same-key ordering and when globally ordered messages are neither necessary nor free.

8. **Replay under a recovering service** — Simulate retry storms during partial outage and ensure bounded dedup/retry does not exhaust shared capacity.

9. **Formative replay and stale read** — Reproduce two concurrent same-key submissions plus delayed projection and verify one intended durable effect.

### Module 11 — Cascading Dependency Failure and Resource Isolation

#### Outcomes

- APP8-O5
- APP8-O10
- APP8-O11
- APP8-O12
- APP8-O15

#### Lessons

1. **Failure domains and critical paths** — Draw dependency graph, fan-out and which user tasks share scarce CPU, pools or upstream limits.

2. **Timeout versus end-to-end deadline** — Allocate per-hop and total budgets; distinguish an aborted client request from cancellation of external committed work.

3. **Retry ownership and budgets** — Coordinate retries across browser/API/worker to avoid multiplying calls when an upstream is impaired.

4. **Circuit breaker state reasoning** — Model closed/open/half-open behavior and recovery probes where appropriate, documenting when it adds more complexity than value.

5. **Bulkheads and dedicated limits** — Give high-priority operations a bounded independent pool so a slow optional dependency cannot consume all connections.

6. **Graceful fallback correctness** — Keep security, authorization, payment-like invariants and private data fail-closed, while shedding genuinely optional work.

7. **Failure injection under realistic load** — Delay and reject a controlled local external service to observe retry amplification, queue growth, p95 and error rates.

8. **Recovery with controlled ramp-up** — Avoid overwhelming a restarted dependency with pending retries and limit half-open probes/work replay.

9. **Formative cascading outage** — Identify a misleading cache fallback or unbounded retry loop and verify repaired unaffected user operations.

### Module 12 — Availability, Degraded Experience and Reliability Budget Trade-offs

#### Outcomes

- APP8-O1
- APP8-O10
- APP8-O11
- APP8-O14

#### Lessons

1. **Availability from user tasks** — Define a successful signed-in operation, queue completion, protected data and degraded-but-valid behavior using actual APP6 SLI semantics.

2. **Failure modes, impact and blast radius** — Rank component/dependency loss by affected tenants, duration, private data risk and recoverability.

3. **SLO targets and error-budget tradeoffs** — Interpret existing APP6 objective/burn-rate signals for architecture choices without reteaching the entire monitoring course.

4. **What can safely degrade** — Identify optional personalization, analytics or recommendations that may be disabled while core access remains correct.

5. **Admission and latency versus success** — Choose when a quick honest 503 is better than requests hanging indefinitely or falsely reporting success.

6. **Fail-closed invariants under stress** — Prove resource authorization, tenant isolation and transaction state survive cache/dependency outages.

7. **Recovery objectives and state guarantees** — Distinguish service recovery, data restoration and write correctness from APP7 backup/rollback execution.

8. **User-facing explanations and accessibility** — Make pending/retry/error/degraded states understandable, keyboard accessible and nondeceptive.

9. **Formative degraded-mode review** — Reject a proposal to serve stale confidential data merely to improve aggregate latency.

### Module 13 — Incremental Architecture Migration, Governance and Compatibility

#### Outcomes

- APP8-O1
- APP8-O12
- APP8-O13
- APP8-O14
- APP8-O15

#### Lessons

1. **Architecture fitness versus novelty** — Document architecture problem, measured constraint, options, rejected alternatives and the minimal experiment needed.

2. **Modular monolith, extracted service and strangler** — Compare boundaries, transaction semantics, network call overhead, team ownership and failure domains.

3. **Feature flags and traffic shadowing** — Test an alternate code path or shadow request safely while preventing duplicate external mutations.

4. **Dual-read/write and data migration risks** — Map consistency between old/new storage, reconciliation cost and which mirrored writes are prohibited by side-effect semantics.

5. **Compatibility matrix and public API changes** — Test older and candidate clients/services, schema revisions, statuses and event shapes under a staged contract.

6. **Gradual traffic migration** — Apply reversible local routing or feature selection with explicit safety checks inherited from APP7.

7. **Rollback versus forward repair** — Explain how schema/data or remote side effects can make an architectural rollback unsafe despite a good previous image.

8. **Architecture decision record with evidence** — Publish decision, alternatives, measurements, security implications, economic impact, risks and trigger for revisiting it.

9. **Formative reversible migration** — Stage a bounded cache/worker/service boundary change and prove failing candidate can be disabled safely.

### Module 14 — Performance, Complexity and Operational Cost Economics

#### Outcomes

- APP8-O1
- APP8-O3
- APP8-O12
- APP8-O14
- APP8-O15

#### Lessons

1. **Cost per useful completed operation** — Define the unit of business work including failures, queue delays, cache/storage, operational staffing and reliability targets.

2. **Compute and memory marginal costs** — Estimate resource hours, peak headroom, scaling delay and throughput-per-instance from declared local measurements.

3. **Data, replica and cache total cost** — Include additional writes, storage, replication bandwidth, memory, backup and cache invalidation labor.

4. **Network and worker economics** — Account for request fan-out, ingress/egress, job attempts, external API quotas and failed/retried operations.

5. **Availability and redundancy expense** — Compare cost of standby capacity, isolation and recovery with justified user-impact requirements.

6. **Engineering and maintenance burden** — Record additional deployment complexity, configuration, incident paths, change coordination and support costs.

7. **Sensitivity and confidence intervals** — Vary arrivals, payload, data growth, burst profile and price assumptions rather than reporting one exact future spend.

8. **Baseline versus two alternatives** — Make a reproducible table of bottleneck, p95, error, user outcome, complexity and cost for at least two plausible designs.

9. **Formative complexity rejection** — Argue against an unjustified shared message broker or microservice based on measured scale, privacy and operational overhead.

### Module 15 — Integrated Production Architecture Review and Independent Defense

#### Outcomes

- APP8-O1
- APP8-O2
- APP8-O3
- APP8-O4
- APP8-O5
- APP8-O6
- APP8-O7
- APP8-O8
- APP8-O9
- APP8-O10
- APP8-O11
- APP8-O12
- APP8-O13
- APP8-O14
- APP8-O15
- APP8-O16

#### Lessons

1. **Choose one APP7 product with a real constraint** — Start from the independently deployed, recoverable APP5 application and APP6 verification/observability baseline.

2. **Publish user-facing growth and failure assumptions** — Set throughput, latency, consistency, reliability, security and cost acceptance criteria and their evidence sources.

3. **Capture representative workload and baseline** — Record synthetic traffic mix, data size, generator capability, cold/warm periods, failure/denial counts and matched local environment.

4. **Explain baseline capacity and bottleneck** — Correlate response tail, CPU/event loop, SQL pool/locks, queue depth and dependency timeouts and provide counterexamples.

5. **Choose and implement justified overload protection** — Add rate/fairness/backpressure or worker-concurrency controls and verify bounded failure under an explicit burst.

6. **Investigate cache and state correctness** — Compare scoped cache/invalidation and a delayed-read or replica-like adapter without weakening PostgreSQL authority.

7. **Reproduce duplicate and partial-failure outcomes** — Exercise idempotency and external dependency overload, including retry amplification and safe degraded behavior.

8. **Stage a reversible architectural boundary** — Deploy a selected change behind a safe switch with old/new contract evidence and rollback/repair policy.

9. **Rerun measurements and calculate costs** — Compare repeated p95, throughput, rejections, correctness, resource use and illustrative operational cost with uncertainty.

10. **Audit privacy and tenant protections** — Verify no cross-tenant cache, rate-limit, worker or stale-view exposure during load and failure.

11. **Unfamiliar bounded scenario and independent defense** — Respond to a new workload distribution or failed dependency without replacing evidence with speculation; defend chosen simplicity or added complexity.

## Completion requirements

**All sixteen APP8 outcomes** must be demonstrated through
the **seven required summative assessments** below.
Assessments may extend a single evolving deployed APP7
product and APP6 quality baseline; seven unrelated systems,
paid services, distributed microservices or hidden exercises
are not required. Module-level investigations and comparisons
are formative except where the summative work explicitly
calls for their results.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP8-AS1` — Representative Workload, Capacity and Bottleneck Investigation | APP8-O1, APP8-O2, APP8-O3, APP8-O4, APP8-O12, APP8-O14 | Scenario, workload-generator source and seed, platform/traffic/data configuration, repeated latency/error/throughput/resource traces, generator-bias inspection, capacity worksheet, alternative hypotheses and defensible preliminary decision |
| `APP8-AS2` — Bounded Admission, Queues and Fairness under Burst | APP8-O3, APP8-O5, APP8-O6, APP8-O9, APP8-O11, APP8-O15 | Admission/queue/job source and limits, policy state and tenancy matrix, deterministic burst test and comparison table, database before/after and replay logs, shutdown/poison-work observations, accessible user-facing errors and trade-off analysis |
| `APP8-AS3` — Cache, Data Lag and Concurrent Correctness | APP8-O4, APP8-O7, APP8-O8, APP8-O9, APP8-O15 | Source, workload and cache/adapter contracts, hit/miss and request-trace evidence, cache stampede comparison, PostgreSQL race/transaction observations, delayed-read/identity-switch tests, error/result matrices and residual consistency/cost claims |
| `APP8-AS4` — Cascading Failure Containment and Truthful Degradation | APP8-O5, APP8-O6, APP8-O10, APP8-O11, APP8-O12, APP8-O15 | Dependency graph, fault-switch and load script, redacted traces and resource metrics, timeout/retry/bulkhead policy, matched normal/failure/recovery runs, denied/committed-state tests, recovery timeline and limitations |
| `APP8-AS5` — Reversible Architectural Evolution and Consumer Compatibility | APP8-O1, APP8-O4, APP8-O8, APP8-O9, APP8-O12, APP8-O13, APP8-O14 | ADR/options with measured hypotheses, old/new component/sequence diagram, feature-selection or routing implementation, contract and DB compatibility tests, failure injection, staged rollout/rollback or forward-fix transcript, repeated measurements and limits |
| `APP8-AS6` — Architecture Security, SLO and Cost Decision Review | APP8-O1, APP8-O3, APP8-O5, APP8-O8, APP8-O10, APP8-O11, APP8-O14, APP8-O15 | Risk/SLO and tenant-abuse matrix, before/after negative HTTP/DB/cache tests, resource and business-task observations, multi-option numerical costs and sensitivity, recorded architecture decision and unverified assumptions |
| `APP8-AS7` — Integrated Measured Production Architecture and Independent Defense | APP8-O1, APP8-O2, APP8-O3, APP8-O4, APP8-O5, APP8-O6, APP8-O7, APP8-O8, APP8-O9, APP8-O10, APP8-O11, APP8-O12, APP8-O13, APP8-O14, APP8-O15, APP8-O16 | Versioned application/environment/workload/source, traceable problem and evidence mapping, baseline and modified tail-latency/throughput/queue/error results, DB/cache/retry/authorization and restore-safe tests, ADR and old/new compatibility records, illustrative cost/sensitivity model, fresh reproduction and accessible written/recorded/live technical defense |

### Shared independence, measurement and safety boundaries

- Record a mutually compatible React/TypeScript,
  Node/Fastify and PostgreSQL runtime, open-source local
  load/fault tools, fixture versions, machine/resources,
  data volumes, traffic mix and setup/cleanup.
  Initial free downloads are permitted; actual assessment
  runs must be reproducible using locally available
  provisioned artifacts, disposable test resources
  and synthetic accounts.
- Use a **real running local product and PostgreSQL**
  to verify important HTTP, data and authorization
  claims. Controllable local queues, caches, delayed
  replica-like reads and synthetic upstream failures
  are appropriate when their behavior and limitations
  are stated. Never portray a simulated follower,
  clock, worker cluster or cloud failover as an
  actual distributed system guarantee.
- Separate **arrival rate from observed completion
  throughput** and report failures, scheduled-but-
  unissued, canceled, dropped/rejected and timed-out
  tasks rather than timing successful requests alone.
  Qualify p50/p95/p99 with sample counts, variability,
  environment, warm-up, cache skew, load-generator
  capacity and coordinated omission risks.
- State assumptions and units for queue/capacity
  calculations and Little's law. An unstable system,
  unbounded queue or partial data cannot justify
  steady-state arithmetic as a reliable future
  capacity prediction.
- Compare alternatives with repeatable matched
  workload, dataset, environment and release version.
  Include both user-task and system metrics,
  material regressions, credible confidence/variance
  and negative security/data tests. Avoid a claim
  of improved architecture based solely on a
  faster synthetic endpoint or test score.
- Bound admission, backlog, concurrency, deadlines,
  retry attempts, worker lifetimes, cache memory
  and resource consumption. Ensure a failed
  request honestly reports refusal or uncertain
  durable work and does not silently duplicate
  a business operation. Optional features may
  degrade; authentication, confidentiality,
  data invariants and authorization must not.
- Prove strong state/invariant claims through
  actual concurrent PostgreSQL transactions
  with independent data inspection. Repeated
  idempotency keys, stolen/wrong tenant access,
  stale client results and permission changes
  must not bypass policy or corrupt authoritative
  state. A delayed-read adapter is explicitly
  a lag *simulation*, not true replicated SQL.
- Distinguish cache performance benefits from
  freshness and privacy guarantees, and verify
  tenant/version/permission scopes, invalidation
  and behavior during cache unavailability,
  identity switching and service overload.
- Perform fault/load exercises only against
  approved learner-owned localhost or isolated
  disposable environments with bounded
  concurrency/duration; never overload,
  scan, exploit or induce failure on external
  production services or real user data.
- Architecture migration plans must include
  relevant old/new consumers, schema/contracts,
  job/file side effects, authorization and
  rollback compatibility. If an effect is
  irreversible, define a staged pause or
  forward repair rather than falsely claiming
  that traffic rollback repairs committed data.
- Cost conclusions must show assumptions,
  numerical units, sensitivity and relevant
  compute, connection/DB, cache, queue,
  storage/egress and operational work.
  Illustrative rates are not live cloud
  quotations, and no provider account,
  purchase or public deployment is required.
- An independent reviewer may introduce a
  bounded unfamiliar growth, cache/tenant
  leak, replica-lag, retry-storm or architecture
  cost/failure case aligned to published
  outcomes. Any written, recorded, synchronous
  or equivalent accessible technical defense
  can satisfy the same public review criteria.
  Do not impose electives or privately
  selected technology as additional gates.

### Required summative assessments

- **APP8-AS1** (required representative workload, capacity and bottleneck investigation)
  - Outcomes: APP8-O1, APP8-O2, APP8-O3, APP8-O4, APP8-O12, APP8-O14
  - Work: Given a running APP7 application and a bounded synthetic user-growth scenario, design an open/closed-loop workload with explicit arrival pattern, read/write/tenant mix, hot keys, known dataset, generator capacity, cold/warm periods and legitimate/denied outcomes. Reproduce a measurable baseline under at least two loads; collect p50/p95/p99 (or justified sample-appropriate distribution), completed/failed/timeout rates, DB/pool/resource and queue evidence. Calculate an appropriate steady-state concurrency or capacity relationship, and identify the actual limiting boundary with at least two plausible alternative hypotheses.
  - Criteria: Measurements are repeatable under declared environment and sample conditions, and invalid generator/latency summaries—including coordinated omission or cache-only gains—are corrected or explicitly bounded. A demonstrated resource/queuing observation supports a bottleneck hypothesis; any Little's law use states assumptions and units. The reviewer can distinguish user success, protected denials, overload rejects and failed operations from raw status 200. No guessed production throughput, phantom cloud measurements or unjustified scaling recommendation is credited.
  - Evidence: Scenario, workload-generator source and seed, platform/traffic/data configuration, repeated latency/error/throughput/resource traces, generator-bias inspection, capacity worksheet, alternative hypotheses and defensible preliminary decision.

- **APP8-AS2** (required bounded admission, queues and fairness under burst)
  - Outcomes: APP8-O3, APP8-O5, APP8-O6, APP8-O9, APP8-O11, APP8-O15
  - Work: Extend the APP5 job or request path with a bounded admission and worker/backpressure policy, per-tenant quotas or fair scheduling, meaningful 429/503/error semantics and a durable/explicitly limited backlog. Generate a controlled burst above demonstrated capacity with mixed tenants and work types. Compare before/after queue length, p95, accepted/processed/rejected counts, worker-pool pressure, completion/timeout and tenant fairness. Inject a worker restart, redelivery, poison task and non-idempotent request replay.
  - Criteria: No queue or memory grows without stated bounds; overload leads to predictable accepted, rejected, postponed or failed user outcomes and an unaffected tenant is not starved without documented justification. Durable business intent remains recoverable after restart and duplicate requests produce no unintended double committed effect. Full and partial failures are reported honestly and client retry semantics avoid amplification. Claims about guaranteed per-tenant fairness or exactly-once remote effects are supported only if explicitly demonstrated within their limited domain.
  - Evidence: Admission/queue/job source and limits, policy state and tenancy matrix, deterministic burst test and comparison table, database before/after and replay logs, shutdown/poison-work observations, accessible user-facing errors and trade-off analysis.

- **APP8-AS3** (required cache, data lag and concurrent correctness)
  - Outcomes: APP8-O4, APP8-O7, APP8-O8, APP8-O9, APP8-O15
  - Work: Compare a baseline primary-database query path against one justified caching/coalescing and one data-routing or delayed-read scenario using synthetic multi-tenant records. Evaluate cache key/tenant scope, freshness/eviction/invalidation and hot-key stampede under controlled traffic. Use actual local PostgreSQL sessions for conflict/constraint/idempotency proofs and a clearly labeled simulated lag adapter or an actual supported local replica for stale-read behavior. Inject cross-tenant access, permission revocation, delayed updates, concurrent writes and a committed mutation followed by a lost response.
  - Criteria: A measured change demonstrably alters request/DB load without sacrificing server-side authorization, transaction integrity or user reconciliation. Cache/public responses cannot leak another user's or tenant's records after identity/permission changes; a stale replica/adapter is not relied upon for authoritative access or protected mutation decisions. Actual PostgreSQL evidence establishes strong invariants; simulated replica lag is labeled simulation rather than an achieved replication guarantee. Duplicate and out-of-order operations do not silently corrupt committed state.
  - Evidence: Source, workload and cache/adapter contracts, hit/miss and request-trace evidence, cache stampede comparison, PostgreSQL race/transaction observations, delayed-read/identity-switch tests, error/result matrices and residual consistency/cost claims.

- **APP8-AS4** (required cascading failure containment and truthful degradation)
  - Outcomes: APP8-O5, APP8-O6, APP8-O10, APP8-O11, APP8-O12, APP8-O15
  - Work: Inject a slow or failing synthetic outbound service under concurrent APP7 traffic, with an optional noncritical user feature sharing resources with a protected core operation. Observe baseline retries, queue/pool growth, latency, errors and affected tenants; define and implement a bounded end-to-end deadline, one controlled retry owner, targeted bulkhead or circuit-breaker/admission defense and a safe degraded UI/API policy. Repeat matched conditions and verify restoration/ramp-up while a dependency recovers.
  - Criteria: The mitigation limits retry amplification, blocked resources and failure propagation for the declared workload, with actual before/after user outcomes and reasonable local capacity. No circuit breaker or bulkhead is required if a simpler proven fix meets the risk. Core authorization, private data and transaction guarantees fail closed; optional feature degradation is clearly communicated and accessible. A canceled/timeout request is not incorrectly treated as reversing a completed external or database action. Recovery probes and retry attempts are bounded; synthetic signals are not misrepresented as production uptime.
  - Evidence: Dependency graph, fault-switch and load script, redacted traces and resource metrics, timeout/retry/bulkhead policy, matched normal/failure/recovery runs, denied/committed-state tests, recovery timeline and limitations.

- **APP8-AS5** (required reversible architectural evolution and consumer compatibility)
  - Outcomes: APP8-O1, APP8-O4, APP8-O8, APP8-O9, APP8-O12, APP8-O13, APP8-O14
  - Work: From a demonstrated bottleneck or business-growth requirement, compare at least two coherent architecture interventions (for example batching within the monolith, an isolated worker, a read-model/cache strategy or a narrowly extracted service). Implement only the justified boundary using a feature flag, proxy route or controlled alternate adapter, and run old/new API, database, cache and job consumers through a staged state-contract compatibility matrix. Seed a candidate incompatibility or partial migration, rehearse a safe rollback or tested forward repair, and measure unchanged user/tenant security guarantees.
  - Criteria: The chosen design reduces an observed constraint or produces a defensible rejection of extra complexity; a prototype without compatible behavior and independent tests does not pass. The migration records effective state/traffic boundaries, old/new client and data compatibility, staged acceptance, cost/change risk and how rollback interacts with committed writes or external side effects. The learner tests real protected work and denies cross-tenant access before and after a switched change. Changed latency/resource conclusions use comparable workloads and acknowledge measurement uncertainty.
  - Evidence: ADR/options with measured hypotheses, old/new component/sequence diagram, feature-selection or routing implementation, contract and DB compatibility tests, failure injection, staged rollout/rollback or forward-fix transcript, repeated measurements and limits.

- **APP8-AS6** (required architecture security, slo and cost decision review)
  - Outcomes: APP8-O1, APP8-O3, APP8-O5, APP8-O8, APP8-O10, APP8-O11, APP8-O14, APP8-O15
  - Work: Audit the evolving APP8 architecture under a user-centered SLO/error-budget scenario, a synthetic tenant traffic spike and a confidential-data read. Compare two possible capacity/resilience solutions using resource-hour, storage, data transfer, retry/background work and operational ownership assumptions. Inject an unfair tenant quota, unsafe cache fallback, stale permission or overly permissive replica read and show the server/database corrections. Explain how the chosen overload or redundancy policy affects actual user-task success, tail latency, security, monthly cost and maintenance burden without inventing cloud quotes.
  - Criteria: Performance/reliability goals are defined with eligible events and a defensible window; a numerical budget or synthetic scenario is not presented as live uptime. Security/privacy tests cover tenant authorization and private data under stale/read/degraded paths. Calculations show units, sensitivity and uncertainty, plus at least one cheaper/simpler alternative; the decision acknowledges engineering upkeep, capacity headroom and provider responsibility. Added complexity is proportional to a measured need, not an unquestioned design preference.
  - Evidence: Risk/SLO and tenant-abuse matrix, before/after negative HTTP/DB/cache tests, resource and business-task observations, multi-option numerical costs and sensitivity, recorded architecture decision and unverified assumptions.

- **APP8-AS7** (required integrated measured production architecture and independent defense)
  - Outcomes: APP8-O1, APP8-O2, APP8-O3, APP8-O4, APP8-O5, APP8-O6, APP8-O7, APP8-O8, APP8-O9, APP8-O10, APP8-O11, APP8-O12, APP8-O13, APP8-O14, APP8-O15, APP8-O16
  - Work: Deliver an independently reproducible architectural evolution of one APP7-deployed APP5 full-stack product, using APP6 observability and local synthetic tenants. Provide representative workload design and measured saturation model; implement a bounded overload/queue or fairness improvement, coherent cache/data consistency controls and a demonstrated cascading-failure mitigation; stage one architecture boundary with old/new contract and recovery evidence; assess private access and cross-tenant correctness under stress, marginal financial/operating complexity and accessible degraded user states. Reuse qualifying AS1–AS6 artifacts, and respond to an unfamiliar bounded load, stale-data, dependency, security or cost constraint with independently defendable evidence.
  - Criteria: A reviewer can reproduce tests with documented free local tools, pinned versions, synthetic data and authorized localhost traffic, inspect all measured normal/adverse outcomes and verify actual PostgreSQL invariants without required Redis, Kafka, sharded DB, Kubernetes or paid cloud. A claimed improvement is supported by repeatable comparable measurements, actual user-task and security evidence, bounded overload and retry, a compatibility-safe migration and acknowledged limitations. The learner demonstrates an unfamiliar corrective change and explains why the simplest design meeting the requirements was selected or why extra architectural complexity was justified.
  - Evidence: Versioned application/environment/workload/source, traceable problem and evidence mapping, baseline and modified tail-latency/throughput/queue/error results, DB/cache/retry/authorization and restore-safe tests, ADR and old/new compatibility records, illustrative cost/sensitivity model, fresh reproduction and accessible written/recorded/live technical defense.

### Completion decision, status and revision safety

Completion requires an inspectable accepted decision
for `APP8-AS1` through `APP8-AS7`, jointly
covering `APP8-O1` through `APP8-O16`.
A fast benchmark, image diagram, self-reported
cloud experience, high cache hit ratio or green
unit test cannot alone establish measured
performance, concurrency safety, truthful
degradation or an independently defensible
architecture choice.

Material violations of security/tenant isolation,
durable state correctness, reproducibility,
bounded overload, evidence integrity or
consumer compatibility require correction
before passing. The review should record the
course/OEE revision, actual source and test
artifact identities, assessment/outcome IDs,
load and environment conditions, negative
cases, competing hypotheses, incident/
migration evidence, assumptions, decision
and limitations according to
[OEE Evidence Rules](../../spec/evidence-rules.md).

APP8 retains its code and core identity,
replacing the legacy nine-week checkpoints/
final-lab contract with an OEE `v0.2.0`
**draft**. Its direct prerequisites remain
APP5, APP6 and APP7, per approved program
architecture. Historical completion evidence
continues to refer to its original course
revision and must not be retroactively
reinterpreted as meeting the new outcome
or assessment IDs. APP9's capstone remains
a separately reviewed project with its
own graduation evidence; APP10–APP16
electives and OEE Workspace/content/0xNAND
consumer pins need distinct review.

Passing structural checks, tests or this
local architecture exercise does not
promote APP8 to `tested` or `verified`.

### Public non-mandatory study references

These open materials clarify mechanisms
but do not add hidden assessment requirements.

- [Google SRE — Handling Overload](https://sre.google/sre-book/handling-overload/)
  and [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)
  for admission, shedding, retries and service-degradation trade-offs.
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/)
  for measured user-focused SLO and capacity decisions.
- [PostgreSQL high availability and replication](https://www.postgresql.org/docs/current/high-availability.html)
  for genuine asynchronous read replica and lag limitations.
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
  and [EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
  for real query and concurrency verification.
- [Azure Architecture — Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker)
  and [Bulkhead](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead)
  for bounded dependencies and isolation decisions.
- [Microsoft Retry Storm antipattern](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/retry-storm/)
  for retry amplification and its mitigation.
- [RFC 9110 HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
  for correct overload/error contracts.
