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
evidence. **Instructional sufficiency governs this structure**:
queueing models need numerical worked examples and assumption checks;
overload, worker, cache, database and fault mechanisms need distinct
bounded implementations, observable counterexamples and feedback;
architecture alternatives need matched experiments and independent
defense. Related terms may share context, but a mathematically or
operationally new idea must not be hidden inside an overloaded lesson.
All lesson investigations are formative unless required by the seven
published summative assessments. One evolving product can provide
separately judged evidence without repeated submissions.

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

1. **From Deploying Software to Evidence-Led Architecture** — Place APP8 after APP7 operations and APP6 quality, briefly trace how scaling strategies arose in response to measured problems, and distinguish an architecture decision from another tool or service purchase; diagnose a proposal that cannot name its constraint.

2. **A Protected User Task and an Observable Success Definition** — Use one existing APP5 authorized user journey; define committed result, permission denial, deadline and acceptable degraded response, then show why HTTP 200 or an accepted queue item alone cannot be counted as completed work.

3. **Historical Alternatives, Not a Scale Ladder** — Contrast scale-up, extra API replicas, cache and partitioned services as context-dependent remedies; examine a historical/synthetic bottleneck where adding instances worsens the shared database.

4. **Workload Provenance and Bounded Service Objectives** — Distinguish forecasts, real local measurements and actual user research; set explicit eligible tasks, data scale, latency/error/consistency/privacy limits and confidence before selecting architecture.

5. **Verified Monolith Baseline, Trust Ownership and Options** — Capture actual proxy/app/DB/worker ownership, consumer contracts and release identity before comparison; map the first cheaper corrective option and explain its security/state boundary.

6. **Falsifiable Change Hypothesis and Review Feedback** — Predict a measurable effect, a competing cause and a failure counterexample for two plausible designs; specify what observation would make a recommendation change.

*Optional practice — architecture review:* Reject a proposed microservice split unsupported by workload data and identify a measurable alternative with lower cost and risk.

### Module 2 — Workload Characterization, Measurement Quality and Test Harnesses

#### Outcomes

- APP8-O1
- APP8-O2
- APP8-O3
- APP8-O12

#### Lessons

1. **Open versus Closed Arrivals and Real User Pressure** — Contrast scheduled independent arrivals with client-throttled closed-loop completion using a worked trace; select one model and explain when it understates a saturated service.

2. **Task, Tenant, Payload and Denied-Request Mix** — Build a reproducible authorized/forbidden/read/write mix with hot/cold payloads and uneven tenants, then test whether a single fast endpoint is a misleading proxy for the real user journey.

3. **Data Growth, Distribution Skew and Seeded Fixtures** — Control row count, join/fan-out, tenant sizes and key popularity in a disposable Postgres dataset; check which distribution assumptions are synthetic rather than measured.

4. **Warm/Cold Cache, JIT and Instrumentation Effects** — Separate browser/DB/service cache warm-up, runtime JIT and measurement overhead; use matched fixed runs to reveal a false performance gain.

5. **Percentiles, Error Mix and Observation Bias** — Read a concrete request trace, computing sample-aware latency summaries with completed, rejected, failed and timed-out operations; note why a mean or success-only p99 cannot describe all users.

6. **Coordinated Omission and Exhausted Load Generator** — Deliberately underdrive a loopback service or delay a generator and compare scheduled arrival times with issued/completed requests, then repair the reporting to avoid missing severe user waits.

7. **Controlled Baseline Protocol and Independent Recheck** — Fix version, hardware, dataset, release, warm-up, duration, generator utilization and samples; rerun a changed load and explain which observed differences may be noise or missing events.

*Optional practice — invalid experiment:* Detect a suspicious throughput gain caused by an accidentally warmed cache, changed response shape or underdriving client.

### Module 3 — Queueing Theory, Concurrency and Capacity Boundaries

#### Outcomes

- APP8-O2
- APP8-O3
- APP8-O4
- APP8-O5

#### Lessons

1. **Arrival, Throughput, Concurrency and Wait-Time Units** — Work through one real request timeline, distinguishing offered/accepted/completed operations, service time, queue wait and in-flight occupancy, with consistent units and boundaries.

2. **Little's Law in an Actually Stable Boundary** — Derive and apply L=λW from a fixed-window stable queue trace with consistent arrivals/departures; contrast with a growing backlog that makes naïve steady-state capacity estimates invalid.

3. **Queueing Tails, Utilization and Bottleneck Service** — Use a bounded controlled example to trace rising wait and tail latency near bottleneck saturation, separating CPU, event loop, DB pool and external service; reject a universal deterministic tail curve.

4. **Burst Capacity, Headroom and Uncertain Demand** — Estimate how much bounded demand a measured resource can serve, contrasting sustained arrival rate and burst occupancy with evidence-based safety margin rather than extrapolating one benchmark indefinitely.

5. **Node Work, Database Pools and Explicit Semaphores** — Coordinate actual pool/worker limits with application request admission; demonstrate a setting where more concurrent API calls increase wait without increasing committed throughput.

6. **Bounded versus Unbounded Backlog and Latency Debt** — Measure real queue depth, age, memory and deadline misses during a burst, and show how pending work can remain unserviceable long after arrivals fall.

7. **Admit, Defer or Reject Based on Actual Work Ownership** — Choose admission for synchronous reads versus durable mutations, show honest rejection and no dropped committed intent, then verify the invariant using an unfamiliar request schedule.

*Optional practice — saturation worksheet:* Calculate response/wait/queue quantities on a supplied local trace and identify invalid inference under overload.

### Module 4 — Profiling the Actual System and Removing Work

#### Outcomes

- APP8-O3
- APP8-O4
- APP8-O12
- APP8-O14

#### Lessons

1. **User-Task Critical Path with Correlated Timings** — Trace one React→Fastify→Postgres→worker/proxy request through actual timestamps and status, identify untrusted/missing timing segments, and construct two testable bottleneck hypotheses.

2. **Event Loop, CPU, Allocation and Queue Pressure** — Use sampled Node event-loop delay, CPU, GC/memory and application backlog under a matched workload to distinguish a blocking calculation from DB wait; avoid conflating async syntax with parallel CPU execution.

3. **PostgreSQL EXPLAIN and Measured Query Repair** — Apply EXPLAIN (ANALYZE, BUFFERS) with synthetic safe data, compare actual rows/costs/IO, then trial an appropriate query/index adjustment without declaring all plan cost estimates to be measured latency.

4. **Pool Wait, Locks and Long-Held Transactions** — Use actual local PostgreSQL sessions to tell connection checkout delay apart from query execution and lock contention, checking pool size against DB budget and isolation behavior.

5. **N+1 Amplification and Bounded Batching** — Identify duplicated application–database calls from an actual request trace, implement a scoped query/batch alternative, and verify that output ordering, permission and result shape remain correct.

6. **Serialization, Payload and Browser Work** — Measure HTTP transfer size, JSON serialization, compression/proxy and browser render cost for a real task; demonstrate a case where backend scaling does not cure total interaction latency.

7. **Remove Work before Adding Capacity** — Compare a measured work-reduction repair against the same system with an extra worker/process or increased resource bound, recording bottleneck migration, new costs, errors and remaining uncertainty.

*Optional practice — bottleneck triage:* Reject a CPU-scaling proposal when pool contention or query fan-out is the actual limiting factor.

### Module 5 — Vertical, Horizontal and Partitioned Scaling Choices

#### Outcomes

- APP8-O1
- APP8-O4
- APP8-O8
- APP8-O12
- APP8-O14

#### Lessons

1. **Scale-Up and Resource-Specific Constraints** — Calculate whether extra CPU/RAM/IO on one process addresses an actually measured limit; include downtime, headroom and its single-failure domain without assuming a faster host is always cheaper.

2. **Additional API Replicas and Stateful Assumptions** — Identify hidden local sessions/files/schedulers, request affinity and worker responsibility in APP7's deployed product; reproduce a shared DB pool that gets worse as replicas are added.

3. **Pool Budget across Replicas and Reserved DB Capacity** — Compute per-instance connection allocation with explicit total DB budget, spare administrator/migration capacity and bounded bursts; test the consequences of excess connections.

4. **Traffic Selection, Locality and Tenant Skew** — Compare proxy routing and affinity effects on hot tenants/cache state, measure imbalance and show why uniform replica counts do not imply uniform useful capacity.

5. **Partitions as Ownership and Cross-Partition Trade-Offs** — Reason through a tenant/domain partition key, hot partition, permissions, joins, transactions and change cost using a drawn example, not an undeclared mandatory sharded database.

6. **Skewed Partitions, Rebalance and Failure Modes** — Use synthetic skew to compare practical load distribution and tenant fairness before/after a partition strategy; record rebalancing, retry and stale-state risks.

7. **Decide Whether to Distribute at All** — Defend one scale-up, database query, routing or small partition improvement against a service split with actual measurement, consistency, incident/debugging and operational-cost evidence.

*Optional practice — scaling decision:* Use measured bottleneck plus DB capacity limits to defend vertical upgrade, query repair, horizontal scale or no change.

### Module 6 — Overload Admission, Rate Limits and Tenant Fairness

#### Outcomes

- APP8-O3
- APP8-O5
- APP8-O10
- APP8-O11
- APP8-O15

#### Lessons

1. **Overload, Latency Debt and User Harm** — Differentiate a real saturated/queued user task from ordinary traffic variation with observed request age and error behavior; preserve auth and completed-work semantics under pressure.

2. **Admission Boundaries and Explicit Queue Limits** — Set a finite in-flight/queued item and memory/age budget for two work classes, test a burst and count accepted, refused, expired and *actually committed* operations.

3. **Rate-Limiter Mathematics and Distributed Limits** — Calculate a token bucket's burst/refill and a fixed-window boundary on a worked arrival sequence; identify clock and per-instance limits without implying one in-memory counter is a global quota.

4. **Per-Tenant Fairness and Guaranteed-Service Limits** — Reproduce one tenant monopolizing a shared pool, apply quotas or weighted fair scheduling with real admission traces and test that privileged work does not silently override authorization.

5. **End-to-End Deadline and Timeout Ownership** — Budget queue, database and upstream time across browser/API/worker boundaries; use an already committed operation to demonstrate why a timed-out client cannot assume it was rolled back.

6. **HTTP 429/503, Retry-After and Accessible Refusal** — Distinguish a rate quota from service overload, emit documented refusal/retry guidance and verify clients do not amplify requests or report refused work as success.

7. **Shedding Safe Work without Dropping Durable Intent** — Classify optional suggestions, protected mutations and committed job intents; verify which may be refused, paused, retried or must survive a restart, with actual persisted-state evidence.

8. **Before/After Burst, Fairness and Invariant Defense** — Measure distribution of waits, rejects, throughput, queue growth and one denied tenant/duplicate replay under a fixed burst; demonstrate that an apparent p95 gain did not merely discard valid work.

*Optional practice — abusive burst:* Repair a single-tenant load pattern that saturates shared capacity or causes a misleading fallback authorization bypass.

### Module 7 — Background Work, Queues, Backpressure and Replay

#### Outcomes

- APP8-O5
- APP8-O6
- APP8-O9
- APP8-O10

#### Lessons

1. **User Deadline versus Durable Accepted Work** — Choose when a user operation may be completed inline or accepted for processing, distinguishing HTTP 202, server commit, job progress and actual business completion.

2. **Queue Ownership, Capacity and Age Limits** — Derive finite backlog, worker concurrency and per-tenant age/priority rules from task arrivals and DB/upstream budgets, with an independently inspectable rejected/postponed state.

3. **Backpressure between Producers and Consumers** — Trace a consumer slower than incoming work, demonstrate safe producer throttling and failure reporting, and avoid buffering indefinitely in API memory or user-interface state.

4. **Real Durable Intent and Restart Ownership** — Reuse APP5's transactionally recorded Postgres intent, inspect an actual stop/restart and independently verify no acknowledged committed job silently disappeared.

5. **Worker Fairness and Downstream Pool Contention** — Measure worker count, task age and DB/outbound contention under mixed tenants; fix a starvation case rather than assuming more workers always improve completed work.

6. **Redelivery, Visibility and Idempotent External Effects** — Inject lost worker acknowledgement and duplicate delivery with bounded redelivery semantics, inspecting real committed domain/idempotency rows and admitting any unverified external exactly-once limitations.

7. **Poison Work and Honest Terminal States** — Test retry exhaustion and a permanently invalid job with finite attempts, dead-letter/manual-review state and meaningful user-visible failure, plus correct cleanup on shutdown.

*Optional practice — worker crash under burst:* Restart a disposable worker with pending and duplicate work, then inspect actual durable state and no double business effect.

### Module 8 — Cache Hierarchies, Coherence, Stampedes and Data Privacy

#### Outcomes

- APP8-O7
- APP8-O8
- APP8-O9
- APP8-O15

#### Lessons

1. **A Cache Layer Chosen for a Measured Read Problem** — Contrast browser, API process and shared cache paths for one real DB/latency bottleneck; require an explicit memory/consistency benefit rather than a default Redis dependency.

2. **Tenant, Permission, Filter and Revision Keying** — Derive cache keys and entry-sharing policy from server-held principal/tenant and authoritative permission scope; reproduce a cross-user cache collision or shared-key leak and repair it.

3. **Freshness, Write Invalidation and Stale-While-Revalidate** — Choose TTL, revision/ETag or explicit invalidation based on data criticality; show one stale legitimate read and a revoked-permission read and distinguish their acceptable recovery policies.

4. **Matched Warm/Cold Cache and Hit/Miss Evidence** — Measure actual DB calls, hit ratio, memory and user-task tail latency under the same workload across cold/warm and identity variants, reporting cache invalidation cost.

5. **Hot-Key Stampede and Scoped Single-Flight** — Reproduce concurrent misses with a barrier, implement safe key-scoped coalescing or bounded admission, and test shared caller cancellation, failure and unrelated-key progress.

6. **Negative Cache, Existence Disclosure and Error Semantics** — Decide whether absent/error results can be cached, then test whether authorization changes expose private existence or leak stale forbidden results.

7. **After-Commit Consistency and Replayed Requests** — Race a committed write, invalidation, old response and request replay and demonstrate newer authoritative data is not silently overwritten by stale cache state.

8. **Unavailable Cache, Fail-Closed Identity and Fallback** — Inject cache outage and identity change; verify a safe DB fallback or honest failure, no cross-tenant result exposure and bounded fallback load under pressure.

*Optional practice — stale identity leak:* Fix a synthetic previous-user cache leak that only appears under concurrent session changes.

### Module 9 — Data-Intensive Boundaries, Replicas and Consistency

#### Outcomes

- APP8-O4
- APP8-O8
- APP8-O9
- APP8-O13
- APP8-O15

#### Lessons

1. **Read/Write Demand and Storage Bottleneck Ownership** — Quantify actual query/read, mutation/write, row-growth and pool/lock pressure before proposing replica or partition topology; maintain an ordinary primary-only comparison.

2. **Primary, Async Replica and Visibility Semantics** — Explain WAL shipping/apply lag, read-your-writes and recovery conflicts with current PostgreSQL mechanisms; map which authenticated queries may tolerate a delayed view and which must hit the authority.

3. **Labeled Delayed-Read Simulation and Reconciliation** — Use an explicit delayed-read adapter or a separately configured actual PostgreSQL standby, compare a stale successful response with a primary result and show identity-safe client reconciliation. **Never label the injected adapter as measured streaming replication.**

4. **Authoritative Writes, Permissions and Quotas** — Route security-critical membership, entitlement, inventory and other protected mutation decisions through real PostgreSQL transactions on the authority, rejecting stale replica-only checks.

5. **Indexes, Projection and Partition Alternatives** — Compare real query plan improvement, materialized view refresh and partitioned table complexity for the measured workload, including write amplification and maintenance/recovery costs.

6. **Two-Session Write Race, Locks and Isolation** — Schedule two real independent PostgreSQL updates under explicit barriers, inspect final rows, lock/conflict status and safe retry/optimistic version behavior.

7. **Shared Pool, Replica Lag and Query Cancel Trade-Offs** — Budget primary and read-replica connections, explain how hot-standby query conflicts and lag affect availability and interpret actual standby monitoring only if real replication was deployed.

8. **Mixed-Version Schema Change and Stale Readers** — Test an expand/backfill/contract change against prior/new clients with deliberate delayed projections; identify permission, schema and consistency exceptions requiring forward repair.

*Optional practice — replica misuse:* Repair a workflow that uses lagged data for an authorization or strongly consistent write decision.

### Module 10 — Idempotency, Ordering and Event-Driven Correctness

#### Outcomes

- APP8-O6
- APP8-O8
- APP8-O9
- APP8-O10
- APP8-O15

#### Lessons

1. **Idempotency under Saturation, Not a Repeat of APP3** — Start from an already working principal/tenant/operation-scoped APP3 idempotency key, then load-test fingerprint expiry, replay and starvation decisions; distinguish request de-duplication from server admission.

2. **Atomic Deduplication with Backlog Contention** — Coordinate real PostgreSQL idempotency/domain records under concurrent admission, proving no race between a duplicate key and the committed business effect.

3. **Different Keys, Same Invariant and Real Conflicts** — Use actual revision/constraint checks for simultaneous legitimate operations and explain why distinct keys do not protect against a shared-stock/entitlement invariant.

4. **Stale Client Completion and Current Identity** — Force late old-identity and out-of-order results after route/tenant change; verify the React view never overwrites newer authorized server state.

5. **Delayed/Repeated Worker Effect and Unknown Remote Outcome** — Lose an acknowledgement after a committed local intent, show safe redelivery/reconciliation and explicitly bound what cannot be guaranteed about external side effects.

6. **Ordering within a Key, Not Global Total Order** — Use a synthetic event stream with same-key sequence and independent tenants to choose an ordering/partition rule; show which global-order costs are unjustified.

7. **Retry Storm, Dedup Storage and Expiry under Recovery** — Reproduce a bounded post-outage burst of old and new key requests; measure dedup table size, rejected load and committed state, and avoid retry amplification with finite budgets.

*Optional practice — replay and stale read:* Reproduce two concurrent same-key submissions plus delayed projection and verify one intended durable effect.

### Module 11 — Cascading Dependency Failure and Resource Isolation

#### Outcomes

- APP8-O5
- APP8-O10
- APP8-O11
- APP8-O12
- APP8-O15

#### Lessons

1. **Dependency Graph, Fan-Out and Shared Failure Domains** — Map critical and optional backend/API/worker dependencies with shared pools, fan-out and resource budgets for a protected task, identifying the single failure most likely to cascade.

2. **Total Deadline versus a Per-Hop Timeout** — Allocate end-to-end queue/DB/external time on a concrete request trace, then show a deadline race where the caller cannot undo committed downstream work.

3. **One Retry Owner, Finite Budget and Backoff** — Inject a local upstream failure and count actual browser/API/worker attempts; remove layered retries, justify eligibility and set a capped backoff without infinite synchronous waiting.

4. **Circuit States and When Not to Add a Breaker** — Model open/closed/half-open with a sample error and probe timeline, implement only if observed failure conditions warrant; compare to a simpler timeout/admission limit.

5. **Bulkhead Resource Partitioning** — Give critical authenticated work its own bounded resource budget when an optional dependency hangs; verify a tenant with valid entitlement still completes without bypassing permissions.

6. **Fail-Closed Core and Truthful Optional Fallback** — Select only truly optional cached/reduced features for degraded responses and reject a scenario where stale forbidden data or false transaction success is served to improve an SLI.

7. **Load Plus Dependency Fault and Retry Amplification Trace** — Under bounded repeatable traffic, delay a synthetic local upstream and inspect in-flight demand, queue/pool use, user-task success/reject, error mix and secret-safe correlation before/after repair.

8. **Recovery Ramp, Circuit Probes and Work Replay** — Re-enable the dependency and prove limited probe/retry/admission rates, durable work reconciliation and a stable safe user path without a second load spike.

*Optional practice — cascading outage:* Identify a misleading cache fallback or unbounded retry loop and verify repaired unaffected user operations.

### Module 12 — Availability, Degraded Experience and Reliability Budget Trade-offs

#### Outcomes

- APP8-O1
- APP8-O10
- APP8-O11
- APP8-O14

#### Lessons

1. **A User-Centered Availability and Completion Contract** — Use APP6's defined SLI eligible signed-in tasks and durable completion states, not raw HTTP 200/202, to distinguish actual business success, honest refusal and optional degraded results.

2. **Blast Radius, Tenant Harm and Partial State** — Analyze two component failures by affected tenants, privacy, time and durable data state; quantify actual local evidence separately from conjectural outage probabilities.

3. **SLO Error Budget as an Architecture Decision Input** — Use one previously established APP6 SLI window and actual/synthetic eligible counts to decide which reliability/capacity fix matters, without repeating the full SLO teaching sequence.

4. **Which Work May Degrade and Why** — Rank critical authorization, protected writes and optional personalization/analytics, demonstrating one useful degraded feature and one forbidden fallback.

5. **Honest Rejection versus Unbounded Wait** — Compare a fast and explicit 429/503 with an indefinitely blocked accepted job, inspecting client retry guidance, deadline, resource consumption and completed user task.

6. **Security/Invariants under Partial Dependency Loss** — Test protected read/write and tenant scope through cache outage, late replica-like results and optional dependency failure using real authoritative rows.

7. **Accessible Pending, Refused, Recovering and Final State** — Reproduce user-facing keyboard/focus/status after a slowed, denied or late-completed request and verify no earlier-user data flash or misleading success announcement.

*Optional practice — degraded-mode review:* Reject a proposal to serve stale confidential data merely to improve aggregate latency.

### Module 13 — Incremental Architecture Migration, Governance and Compatibility

#### Outcomes

- APP8-O1
- APP8-O12
- APP8-O13
- APP8-O14
- APP8-O15

#### Lessons

1. **Measured Architecture Fitness and Alternative Decision** — Take one observed bottleneck, failed SLI or growth constraint, compare simplest viable repair with at least one added boundary, and declare the test that would change the recommendation.

2. **Monolith Module, Extracted Worker and Service Split** — Compare ownership, deployment, transaction, auth, trace and failure cost for a focused boundary and show why a network hop may worsen a formerly atomic operation.

3. **Safe Flags, Routing and Shadow Read Paths** — Select old/new code or route with observed tenant behavior and safely shadow only permitted side-effect-free requests; demonstrate a duplicate external effect caused by naïve shadow writes.

4. **Dual Write, Backfill and State Reconciliation Risk** — Map old/new schemas/stores and recovery after partial migration; distinguish a measured read-model rebuild from an unsafe two-source-of-truth write policy.

5. **Versioned Contracts and Independently Old/New Consumers** — Test historical/current API, DB/schema and job payload versions with actual clients and identify an incompatible change that a successful type checker would miss.

6. **Traffic/Feature Switch with Verified Reversal Conditions** — Apply a bounded APP7-derived release switch to a measured architecture candidate and verify stop/forward-repair behavior after committed DB/files/remote side effects.

7. **Decision Record, Cost and Revisit Trigger** — Defend actual measured benefit, rejected simpler alternative, privacy/authorization, operating burden and compatibility plan with an explicit load/cost threshold for reconsideration.

*Optional practice — reversible migration:* Stage a bounded cache/worker/service boundary change and prove failing candidate can be disabled safely.

### Module 14 — Performance, Complexity and Operational Cost Economics

#### Outcomes

- APP8-O1
- APP8-O3
- APP8-O12
- APP8-O14
- APP8-O15

#### Lessons

1. **Cost per Authorized Completed Business Operation** — Define total useful completed user work as denominator and account for rejected/failed retries, queued work and degraded results rather than count raw HTTP requests.

2. **Capacity/Headroom and Marginal Compute** — Use measured CPU/memory/IO and plausible instance-hours to calculate a bounded cost curve for one process and replica alternative, with single-failure/overprovisioning costs.

3. **Storage, Cache, Replica and Write Amplification** — Estimate memory, persistent GB/month, backups, replication traffic, extra writes and coherence/maintenance effort for two meaningful designs.

4. **External Fan-Out, Worker Retries and Data Transfer** — Account for scheduled/failed attempts, egress, vendor quota and queue storage using explicit units and illustrative rates, not invented live quotes.

5. **Engineering, Availability and Support Burden** — Compare fault-domain isolation, idle/redundant capacity, deploy/recovery complexity, on-call/operating effort and additional code/tests—not just instance bills.

6. **Sensitivity Table, Pareto Trade-Off and Decision** — Vary arrival skew, data growth, burst, failure and pricing assumptions; compare both designs' task success/p95/errors/privacy/maintenance and identify where a simpler solution dominates.

*Optional practice — complexity rejection:* Argue against an unjustified shared message broker or microservice based on measured scale, privacy and operational overhead.

### Module 15 — One Measured Architecture Improvement and Independent Defense

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

1. **One Existing Product, Constraint and Prior Judgments** — Use the same APP7-deployed APP5 system assessed through APP8-AS1–AS6; identify independently accepted workload, capacity, security, consistency and cost decisions by reference instead of collecting a fifteenth checklist of full implementations.

2. **Competing Options, Evidence and One Coherent Change** — Connect verified bottleneck, measured alternatives, local admission, cache/read-path, durable-worker and failure choices into a defensible minimal improvement; do not implement an unrelated scaling feature solely to demonstrate breadth.

3. **Adverse User/Data/Privacy and Recovery Recheck** — Reproduce the real selected change under a bounded mixed-tenant load and one failure, verify true committed PostgreSQL results, stale state and unauthorized access denial, and reuse accepted AS1–AS6 tests where unaffected.

4. **Unfamiliar Growth, Lag, Starvation or Failure Challenge** — Receive a new bounded workload/tenant distribution, stale read, permission change, retry storm or cost constraint, predict failure, independently reproduce it and correct the responsible design with targeted regression.

5. **Clean Local Comparison and Independent Technical Defense** — Build/reproduce before and after with recorded free toolchain, traceable decision/evidence index, matched measurements and cost/complexity trade-offs, disclosing what remains a simulation and what would need real deployment or learning validation.

## Completion requirements

All **sixteen APP8 outcomes** require **seven independently
decidable summative assessments** on **one evolving APP7-deployed
product**. AS1 observes valid workload/capacity; AS2 verifies actual
bounded admission, fair queue/worker recovery; AS3 verifies scoped
cache/DB consistency; AS4 limits genuine dependency cascades; AS5
tests a justified architecture change and compatibility; AS6
independently judges privacy, SLO/cost and alternatives; AS7
integrates **previously accepted evidence by reference** and an
unfamiliar bounded engineering challenge. Distinct mechanisms remain
teachable and examinable; seven unrelated systems, paid services,
mandatory distributed clusters or hidden formative gates do not.

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

APP8 remains an OEE `v0.2.0` **draft** with its
established APP5, APP6 and APP7 direct prerequisites.
The previous nine-week checkpoint format is historical;
the core architecture and outcome-based APP9 project
already exist in the published catalog. This source-only
academic reassessment does not declare APP8 `tested`,
independently `verified` or accredited; does not
rewrite APP9 or elective requirements; and does not
reinterpret prior learner completions. OEE Workspace,
content and 0xNAND source/evidence pins must be updated
only through deliberate revision review.

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
