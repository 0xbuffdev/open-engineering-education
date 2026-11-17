# APP5 — Full-Stack Application Architecture

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP20](APP20.md) — React Application Engineering, [APP3](APP3.md) — Backend Framework Engineering
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; calibrate against reviewed learner evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Design, build and defend a **single coherent full-stack user
workflow** across React/browser, authenticated TypeScript/Fastify
API, domain logic, PostgreSQL, cache, safe private file resources
and asynchronous work. Start from testable stakeholder
requirements and trace an operation from user intent through
service authorization, database commit, external side-effect
intent and back into an understandable, accessible interface.
Verify cross-layer state ownership, data integrity, contract
compatibility, identity isolation, partial failure and recovery.

APP5 **integrates** existing competencies rather than teaching
another beginner framework, database or JavaScript language.
Its direct prerequisites are [APP20](APP20.md) React Application
Engineering and [APP3](APP3.md) Backend Framework Engineering.
Through APP3, the learner already has [APP19](APP19.md)
TypeScript, [APP21](APP21.md) Node backend-runtime and
[APP4](APP4.md) relational data capability. APP20 likewise
covers browser/HTML/CSS, JavaScript and interface-specific
engineering. APP4 must **not** be added as an unnecessary
direct prerequisite solely because it is used here; it is
satisfied transitively.

**This is a systems-integration course at application scope.**
APP3 owns standalone API authentication/authorization,
framework lifecycle, transactions and job policy. APP20
owns React state, components and accessible interactions.
APP5 tests whether those pieces agree about one business
operation, across boundaries and failure cases, and who
owns the resulting state and recovery. Cross-layer
requirements, privacy/identity constraints, dependency
failure semantics and safe product change belong here.
Do not turn APP5 into a production Kubernetes course:
APP6 owns broader test/CI/reliability practice, APP7
deployment and operations, APP8 production-scale
architecture and APP9 independent capstone synthesis.
Elective APP12 specializes in advanced realtime systems.

**Free reproducible reference:** a compatible documented
React/TypeScript browser project, Node/Fastify API,
disposable PostgreSQL database and lightweight local
worker plus fixtures for a cache, private object-style
file storage and a simulated external dependency.
A modular monolith is the default: a separate worker
may run as a controlled process, but a distributed
microservices system, hosted Redis, commercial object
store, malware scanner, identity provider, push service,
public domain, paid SaaS or production user data is not
required. Provision free dependencies and pinned
artifacts beforehand; after setup, required outcomes
must be reviewable offline on an unprivileged local
environment with synthetic tenants and accounts.

**Protect the full journey.** The browser may optimistically
display a change, but the database owns committed facts.
The user/session must be verified on the server for every
protected operation; UI hiding, CORS and a client-supplied
tenant identifier do not grant authority. Authenticated
records, cache keys, files, job status and user-visible
error messages must not cross identity boundaries. Use
actual invalid/forbidden/concurrent/revoked/expired
negative cases and inspect committed state independently.

**Do not promise cross-system atomicity.** One PostgreSQL
transaction cannot roll back a successful external
notification, object write or already-delivered message.
Keep durable intent separate from the external operation;
acknowledge queued versus completed results honestly.
An outbox can support at-least-once processing but does
not prove exactly-once remote side effects. Local
private file handling can demonstrate byte, content
policy, staged publication and tenant access controls;
it cannot prove actual malware safety or the
authorization properties of a cloud provider.
A polling or simple event-stream progress UI must
refetch authoritative job state after missed events.

**Access, usability and evidence are as important as
working code.** Model loading/empty/success/pending/
conflict/forbidden/failed/recovery states. Preserve
keyboard, focus and status announcements across
client navigation, retries and logout. Trace one
failed user journey using real sanitized browser/API/
database/worker evidence; report unknowns rather
than invent metrics, participant feedback or
deployment-grade reliability. All real-person
feedback requires consent and minimal data capture.

The proposed 14–18-week duration and focused weekly
hours are planning estimates only. Formative module
investigations support progressively independent
practice; **the seven explicitly required assessments**
below, which may share one evolving vertical slice,
are the only summative completion requirements.

## Learning outcomes

- **APP5-O1:** Translate a bounded stakeholder problem into verifiable full-stack user journeys, acceptance criteria, data/privacy requirements, trust assumptions and recovery behavior, distinguishing synthetic requirements from actual user observations.
- **APP5-O2:** Design and defend a cohesive browser/API/domain/database topology with clear ownership, synchronous/asynchronous boundaries, dependency and context diagrams, and a traceable request-to-commit-to-UI sequence.
- **APP5-O3:** Integrate typed React client and Fastify service contracts with actual runtime input/output validation, interoperable error semantics, authentication context and independently verified client/server compatibility.
- **APP5-O4:** Implement end-to-end identity/session and tenant/resource authorization through client navigation, API, repository, cache and asynchronous side effects, demonstrating genuine server-side denials and safe identity-transition cleanup.
- **APP5-O5:** Reconcile browser draft/optimistic/remote state with committed relational state under conflicting writes, stale responses and network uncertainty, using explicit state transitions, server authority and rollback/refetch policies.
- **APP5-O6:** Integrate transactional PostgreSQL data and API mutations with coherent schema/contract evolution, preserving cross-layer invariants and declaring where external effects cannot participate in database atomicity.
- **APP5-O7:** Choose and implement a bounded cross-layer cache with ownership, keys, tenant scope, freshness, invalidation and eviction policy; reproduce stale and unauthorized cache failures and verify correction.
- **APP5-O8:** Design and implement a safe local file/object-style resource workflow with validated metadata/content boundaries, ownership, staged publication, nonpublic access and cleanup, explaining what an external object store or signed URL would change.
- **APP5-O9:** Integrate a durable or explicitly bounded asynchronous workflow with request acknowledgement, retry/idempotency, job progress and recovery from duplicate or delayed delivery; distinguish notification from authoritative state.
- **APP5-O10:** Provide a proportionate user-facing progress/notification mechanism using bounded polling or a simple event stream, reconciling reconnect/missed messages with authoritative state rather than assuming exactly-once ordering.
- **APP5-O11:** Handle partial dependency failure across UI, API, data store and simulated external service with deadlines, isolation, truthful degraded states, safe retry and user-directed recovery without hiding committed side effects.
- **APP5-O12:** Trace and mitigate full-stack security/privacy threats including session/CSRF/CORS boundaries, cross-tenant exposure, untrusted uploads, unsafe external requests, secrets and client or server cache leakage, with negative evidence.
- **APP5-O13:** Plan and verify a bounded contract/schema/UI change across current and previous consumers, including expand/migrate/contract sequencing, compatible deployment assumptions and a truthful rollback/forward-repair decision.
- **APP5-O14:** Design independent component, API, real-database, security, contract and browser end-to-end tests that establish a representative user journey, negative cases, reproducible environment and failure diagnostics without demanding a production cloud.
- **APP5-O15:** Correlate a browser-observed failure with service, database, job and dependency evidence, classify causality and unknowns, measure bounded workflow latency/recovery and verify a repair without claiming general production reliability.
- **APP5-O16:** Deliver, reproduce, extend and independently defend a secure, accessible, cohesive full-stack vertical slice under an unfamiliar bounded requirement or partial failure, explaining integration trade-offs and incomplete production guarantees.

## Modules

### Module 1 — Requirements, User Journeys and Cross-Layer Acceptance

#### Outcomes

- APP5-O1
- APP5-O2
- APP5-O14

#### Lessons

1. **Course orientation and product scope** — Define full-stack architecture as a coherent user journey across an independently built React frontend and Fastify/PostgreSQL backend; distinguish it from a course teaching their syntax.

2. **Stakeholder problem and provenance** — Work from a synthetic brief or consented stakeholder observations, marking assumptions and actual user evidence honestly.

3. **Actors, boundaries and business invariants** — Identify users, tenants, roles, resources, forbidden actions, cross-layer side effects and where correctness must be enforced.

4. **End-to-end success and failure scenarios** — Write observable acceptance cases for signed-in, invalid, denied, empty, conflicting, stale, pending, failed and recovered workflows.

5. **Nonfunctional requirements with measures** — Define scoped response/latency, accessibility, privacy, data-retention and local reliability objectives without claiming production service levels.

6. **Requirements-to-evidence traceability** — Map each user action to UI state, HTTP contract, durable record, trust check and test, including the negative paths.

7. **Choose an achievable vertical slice** — Bound the problem to a small multi-tenant workspace, catalog/reservation or document-processing product rather than a distributed microservice estate.

*Optional practice — requirements review:* Expose a misleading 'works on my machine' success claim and add the missing acceptance and recovery evidence.

### Module 2 — Architecture Views, Responsibilities and Local Composition

#### Outcomes

- APP5-O2
- APP5-O3
- APP5-O6
- APP5-O11

#### Lessons

1. **System Boundaries and Architecture Views** — Draw browser, API, PostgreSQL, job runner, file resource and outbound fixture, distinguishing actors from processes and durable state; use level-appropriate context, component, deployment and interaction views without implying every diagram describes separate services.

2. **Synchronous request path** — Trace browser event through React, Fetch, authenticated Fastify handler, domain operation and SQL transaction to returned response and UI result.

3. **Asynchronous side-effect path** — Trace an accepted mutation through durable work record, dispatcher, simulated external dependency, notification/progress and UI refetch.

4. **Authority and data ownership** — Separate client drafts, cache replicas, authoritative resource rows, identity/session ownership and immutable audit facts.

5. **Monolith versus distributed alternatives** — Choose a small modular monolith for the reference project and explain when a separate worker or object store becomes justified.

6. **Composition and configuration** — Wire independent frontend/backend/data components using documented local origins, environment values and ports; eliminate hidden absolute URLs.

*Optional practice — boundary trace:* Find a domain check leaking into React or a transaction falsely spanning an external HTTP call and repair the architecture view.

### Module 3 — Client–Service Contract Integration and Failure Mapping

#### Outcomes

- APP5-O1
- APP5-O3
- APP5-O5
- APP5-O11
- APP5-O14

#### Lessons

1. **Reusing APP20 and APP3 contracts** — Connect an existing typed React feature to an independently tested Fastify API without copying a fake client contract by hand.

2. **End-to-end request/response shape** — Compare OpenAPI and actual JSON/headers/status, including runtime validation after TypeScript compilation.

3. **Credentialed Fetch and origin policy** — Configure same-origin or cross-origin local fixture behavior deliberately and explain cookies, fetch credentials and CORS visibility rather than treating CORS as identity verification.

4. **Error categories through presentation** — Map 400, 401, 403, 404, 409, 429, 500 and transport errors into accurate, accessible UI recovery states.

5. **Request IDs and correlation fields** — Carry safe bounded trace/request identifiers across boundaries without logging tokens or assuming browsers can trust a caller-supplied ID.

6. **Client retries and safe semantics** — Distinguish read retry, non-idempotent mutation and uncertain server commit after a lost response.

7. **Consumer-driven contract fixtures** — Run an independently written HTTP consumer alongside React integration tests and compare results with the published contract.

*Optional practice — mismatched-contract repair:* Repair a runtime response missing a required field or returning inconsistent errors, with both client and server regression cases.

### Module 4 — Session Continuity, Authorization and Tenant Isolation

#### Outcomes

- APP5-O3
- APP5-O4
- APP5-O12
- APP5-O14

#### Lessons

1. **Authentication continuity across page loads** — Use APP3's verified synthetic session mechanism through login, refresh, navigation, expiry and deliberate logout.

2. **Principal and resource ownership** — Resolve the server-side current principal and authoritative tenant membership before every protected list/detail/mutation.

3. **Client visibility versus server authority** — Display navigation only when appropriate but test direct forbidden HTTP requests despite hidden buttons or routes.

4. **Session expiry and interrupted workflows** — Handle an expired/revoked session during an upload, optimistic mutation or progress check without leaking previous user state.

5. **CSRF and cookie boundaries** — Explain SameSite/Secure/HttpOnly trade-offs and verify a proportionate local anti-CSRF policy appropriate to the chosen credential mode.

6. **Resource and field-level authorization** — Reject guessed resource IDs, cross-tenant list/detail writes, unsafe role edits and data fields not visible to the principal.

7. **Caches and async worker identity** — Scope cache keys/job access by authoritative tenant and ensure workers cannot inherit unchecked client-asserted claims.

8. **Logout and identity switching** — Clear or invalidate scoped local state and stop stale updates; prove no prior tenant data flashes after sign-out or user switch.

*Optional practice — multi-tenant audit:* Inject a direct-resource access or stale-cache disclosure and verify the repaired server and UI behavior independently.

### Module 5 — State Ownership, Optimistic Mutations and Conflict Recovery

#### Outcomes

- APP5-O1
- APP5-O5
- APP5-O6
- APP5-O14

#### Lessons

1. **Local draft versus confirmed server state** — Model unsubmitted form fields, optimistic UI, pending server state, committed facts and cached views as distinct concepts.

2. **Write lifecycle and transition diagrams** — Define pending, conflict, uncertain, retrying, committed and reverted states for one user-facing change.

3. **Lost response versus failed write** — Simulate a transaction that commits before its HTTP response disappears and show why retry must not blindly duplicate effects.

4. **Conflicting updates and revision tokens** — Use a server-side version/ETag or justified conflict strategy, with meaningful 409/412-type feedback and no silent overwrite.

5. **Optimistic update with explicit rollback** — Show provisional UI success and restore/resolve it on failed validation or conflict, retaining the user's draft safely.

6. **Out-of-order fetches and user intent** — Reproduce a late stale response after a newer edit or tenant switch; prevent it from overwriting authoritative current view.

7. **Read-after-write and consistency windows** — Explain what the user can expect after commit versus delayed cache/job projections, without promising instantly synchronized replicas.

*Optional practice — conflict scenario:* Run two synthetic clients editing the same resource and repair a misleading final-state message with database evidence.

### Module 6 — Persistence, Transactions and Cross-Layer Invariants

#### Outcomes

- APP5-O2
- APP5-O5
- APP5-O6
- APP5-O9
- APP5-O13

#### Lessons

1. **From APP4 schema to full-stack workflow** — Trace state transitions through a service repository and SQL transaction without re-teaching normalization.

2. **Choosing a durable business invariant** — Define one meaningful inventory, entitlement or document ownership rule and map checks to domain and database constraints.

3. **Transaction boundary and application result** — Keep all related database writes in one explicit scoped transaction and map failed preconditions to stable API results.

4. **Cross-request concurrency and conflict** — Demonstrate a two-client race and inspect committed rows, constraint rejections and intended user-facing recovery.

5. **Database and external side-effect separation** — Show why a committed DB transaction does not atomically publish a file or send an external notification.

6. **Idempotency and durable workflow intent** — Use a transactionally recorded key/job/outbox state for replay safety when appropriate, and document its limitations.

7. **Schema changes and old client behavior** — Keep a staged migration compatible with defined older consumers until usage and backfill evidence make a contract change safe.

*Optional practice — invariant failure:* Repair a handler that returns success before checking a failed transaction or leaves inconsistent file metadata after rollback.

### Module 7 — Cache Keys, Freshness, Invalidations and Authorization

#### Outcomes

- APP5-O4
- APP5-O5
- APP5-O7
- APP5-O11

#### Lessons

1. **What and where to cache** — Distinguish browser memory, HTTP cache semantics, API-side caches and database queries by ownership, sensitivity and change frequency.

2. **Cache key construction** — Include authoritative tenant/resource identity, query filters and version dimensions; avoid collisions and untrusted key components.

3. **Freshness and invalidation model** — Define TTL, explicit invalidation, revision changes, stale-while-revalidate where justified and bounded storage policy.

4. **Mutation and cache coherence** — Update or invalidate derived list/detail state after a committed write, and explain failure if cache publication races the DB.

5. **HTTP validators and conditional responses** — Use ETag/If-None-Match where appropriate without confusing a conditional read with an authorization check.

6. **Security and stale permissions** — Prevent caching protected data across users or treating cached permissions as authority after revocation.

7. **Cache stampedes and unavailable cache** — Consider a small controlled request burst and choose a simple fallback strategy; avoid manufacturing distributed-cache requirements.

*Optional practice — cache leak and stale row:* Reproduce a previous user's cached result or a stale post-edit list and verify the fixed key/invalidation policy.

### Module 8 — Files, Object-Style Resources and Publication Safety

#### Outcomes

- APP5-O4
- APP5-O8
- APP5-O11
- APP5-O12

#### Lessons

1. **Why files are a separate trust boundary** — Distinguish file bytes, metadata, record ownership and serving authorization; keep synthetic content local.

2. **Staged upload lifecycle** — Design requested/pending/uploaded/validated/available/rejected states and a bounded temporary storage policy.

3. **Client and server size/type checks** — Use server-enforced byte limits, generated storage IDs and content-based inspection as appropriate, not just filename or client MIME trust.

4. **Content safety and quarantine** — Explain that a local fixture can validate known byte/file policies but cannot certify malware-free content; quarantine or reject unsupported types.

5. **Private access and signed URL semantics** — Implement an authorized local download path; model short-lived scoped capabilities conceptually and explain bearer-style signed URL risks without needing a cloud bucket.

6. **Ownership and metadata consistency** — Bind file records to authenticated tenant/resource and define transaction-plus-file-operation recovery when one side succeeds.

7. **Cleanup of abandoned and rejected uploads** — Enforce expiration/garbage collection on local temporary objects and prove no cross-user access to orphaned artifacts.

*Optional practice — file boundary investigation:* Test forged metadata, oversize data, wrong tenant download, stale signed-like token and failed publication; show safe rejection.

### Module 9 — Async Work, Durable Intent and Retry Semantics

#### Outcomes

- APP5-O5
- APP5-O6
- APP5-O9
- APP5-O11

#### Lessons

1. **Synchronous versus asynchronous user outcomes** — Choose when a request may finish inline and when to acknowledge durable pending work with an honest progress status.

2. **Job state machine and ownership** — Represent queued/running/retryable/completed/permanent-failure states with tenant ownership, attempt counters and timestamps.

3. **Database outbox and worker boundary** — Write domain mutation and intent record together, then process separately with bounded local worker using the APP3 foundation.

4. **At-least-once and idempotent consumers** — Inject duplicate deliveries, lost acknowledgements and process restart, verifying no unintended duplicate business side effects.

5. **Transient retry and poison jobs** — Define bounded backoff, dead-letter/failed state and manual retry conditions with clear user communication.

6. **Eventual result and client reconciliation** — Offer an authoritative status endpoint and clear rules for when a UI pending state may be considered complete.

7. **Shutdown and work ownership** — Stop accepting new work, record in-progress ownership and recover durable uncompleted jobs without asserting all work ran exactly once.

*Optional practice — duplicate-delivery scenario:* Restart a disposable local worker after a simulated crash and prove accepted work is neither silently forgotten nor duplicated as a business operation.

### Module 10 — Progress Delivery, Polling and Reconnect Reconciliation

#### Outcomes

- APP5-O5
- APP5-O9
- APP5-O10
- APP5-O11

#### Lessons

1. **Notification versus source of truth** — Explain that UI progress events are hints; authoritative durable job status must determine the recovered state.

2. **Bounded polling design** — Implement interval/backoff/jitter policy, terminal-state stop and visibility/route cleanup without indefinite high-frequency requests.

3. **Simple event stream as an option** — Inspect a small Server-Sent Events stream if useful, distinguishing SSE from a durable queue, authentication channel or general bidirectional realtime platform.

4. **Connection interruption and stale events** — Model reconnect, delayed/duplicated updates and old-job notifications; use monotonic version/status reconciliation where appropriate.

5. **Authentication on progress endpoints** — Require real server-side authorization for polling/subscriptions and avoid leaking tenant job identifiers in unauthenticated streams.

6. **Accessible pending and completed updates** — Present progress, retry and completion with proportionate live-region announcements and task-oriented messaging.

7. **Slow client, tab hidden and teardown** — Bound active timers/connections, clean up on route change or sign-out and resume by refetching actual job state.

*Optional practice — missed-notification test:* Drop a notification or pause polling and prove the client reaches the correct end state after reconnect.

### Module 11 — External Dependencies, Degradation and Recovery

#### Outcomes

- APP5-O2
- APP5-O9
- APP5-O11
- APP5-O15

#### Lessons

1. **Map dependency failure domains** — Identify failures from browser network, API, database, worker, cache, file and synthetic outbound service independently.

2. **Deadlines and timeout budgets** — Bound operations and understand why cancellation cannot undo a committed DB change or external side effect.

3. **Downstream response validation** — Validate local simulated external API status/body/content type, restrict outbound targets and avoid unbounded response buffering.

4. **Retry amplification and overload** — Demonstrate how UI, API and worker retries can multiply requests; select one defensible retry owner and budget.

5. **Truthful degraded states** — Show pending, temporarily unavailable, partial success and failed outcomes without giving users a false completed/safe message.

6. **Fallback and service boundary decisions** — Choose whether cached reads or queued writes remain acceptable under dependency outage and state lost guarantees clearly.

7. **Recovery and reconciliation after restoration** — Reconcile durable job/resource state, refresh UI and verify no unauthorized or duplicate side effects appeared.

*Optional practice — cascading outage:* Simulate slow outbound dependency and retry storm; document bounded mitigation and what remains unsupported.

### Module 12 — Full-Stack Security, Privacy and Data Lifecycle

#### Outcomes

- APP5-O4
- APP5-O7
- APP5-O8
- APP5-O11
- APP5-O12

#### Lessons

1. **System-level threat model** — Trace client-input, session, tenant, API, DB, cache, file and job boundaries and list representative attacker actions on synthetic resources.

2. **Session and cross-origin policy** — Test credentialed fetch, cookie expiry/rotation and anti-CSRF policy where relevant, distinguishing cross-origin visibility from server authority.

3. **Direct-object access and field exposure** — Issue API calls without using the UI to verify role, tenant and property-level denials across all relevant methods.

4. **Cache and stale authorization** — Simulate revocation and logout while a protected result exists in memory/cache, confirming no cross-identity disclosure.

5. **File content, URLs and retention** — Restrict upload/download paths, reject unsafe external URL handling and document user-visible file deletion versus actual local cleanup.

6. **Privacy-aware observability** — Log request IDs and safe error classifications without raw credentials, unnecessary PII or file contents.

7. **Dependency and artifact provenance** — Pin packages and local fixture versions, document update risks and distinguish a reproducible stack from a production security audit.

*Optional practice — trust audit:* Identify one client-only permission check and one leaked output in a local test, repair both at actual enforcement boundaries.

### Module 13 — Compatible Change, Tests and Staged Evolution

#### Outcomes

- APP5-O1
- APP5-O3
- APP5-O6
- APP5-O13
- APP5-O14

#### Lessons

1. **Change impact across components** — Map a new field/status/permission through React, API schemas, domain logic, SQL, caches, jobs and tests before implementation.

2. **Expand/migrate/contract sequence** — Add backward-compatible schema/API support first, migrate data and clients, then remove obsolete behavior only with declared evidence.

3. **Versioned Consumer Checks and Rollout Controls** — Verify the previous client still works within the supported period and a new client exercises the updated contract; use a small local configuration toggle or simulated staged release, stating that production multi-instance deployment is APP7's scope.

4. **Rollback versus forward repair** — Distinguish application code revert from irreversible data/side-effect reversal; rehearse a repair path where rollback is unsafe.

5. **Contract, integration and browser test layers** — Choose independent tests for typed payloads, real HTTP/database, protected data, job delivery, navigation and visible user outcomes.

6. **Deterministic race and failure controls** — Use explicitly controlled promises, test clocks, barriers, fixture events and isolated DB resets rather than brittle timing sleeps.

*Optional practice — compatibility break:* Inject a new required field or breaking enum and show which previous consumer fails, then amend staged evolution correctly.

### Module 14 — Evidence-Based End-to-End Investigation and Operability

#### Outcomes

- APP5-O2
- APP5-O11
- APP5-O14
- APP5-O15

#### Lessons

1. **Cross-layer correlation and context** — Attach safe request/job correlation identifiers to browser logs, service traces and durable job records without exposing private identities.

2. **Evidence mapping to outcomes** — Distinguish screenshots, API logs, DB rows, worker events and automated assertions and explain what each can and cannot prove.

3. **Workflow latency and critical path** — Measure a bounded journey across render, API, DB and asynchronous waiting while avoiding invalid comparisons between incomparable clocks.

4. **Dependency health and readiness** — Explain a local service's health versus true readiness to complete a specific workflow, without claiming platform operations certification.

5. **Failure injection and causal timeline** — Simulate one unavailable dependency and reconstruct from observed requests, committed state, retry attempts and UI presentation.

6. **Recovery time and user experience** — Measure the observed local recovery and describe how long the user sees pending/error states, qualifying variance and missing observations.

7. **Testing accessibility during failure** — Retest keyboard/focus and status announcements during slow, forbidden, uncertain and recovered flows.

*Optional practice — incident defense:* Repair a discovered misleading pending status or duplicate notification and provide before/after evidence across layers.

### Module 15 — Integrated Vertical Slice and Independent Architecture Defense

#### Outcomes

- APP5-O1
- APP5-O2
- APP5-O3
- APP5-O4
- APP5-O5
- APP5-O6
- APP5-O7
- APP5-O8
- APP5-O9
- APP5-O10
- APP5-O11
- APP5-O12
- APP5-O13
- APP5-O14
- APP5-O15
- APP5-O16

#### Lessons

1. **Select the coherent product journey** — Use an accessible multi-tenant React application and authenticated Fastify/PostgreSQL service with a meaningful committed operation and recovery scenario.

2. **Publish cross-layer acceptance and threat models** — Document user tasks, action/role matrix, resource lifecycle, contracts, data ownership, privacy and fault paths before choosing libraries.

3. **Compose free local reference components** — Use compatible pinned React, Fastify, TypeScript, PostgreSQL and local job/file/cache fixtures without a paid external service or microservices requirement.

4. **Implement authoritative UI/API/database integration** — Build an actual protected request and durable mutation with correct client feedback, denied access and independent DB consistency evidence.

5. **Implement one safe cache or resource workflow** — Include a tenant-aware cache and a locally simulated file/object-style workflow with explicit bounded lifecycle and enforcement.

6. **Complete async work and progress reconciliation** — Integrate a durable intent/job path and bounded polling or simple event notification, recovering missed/duplicate signals from authoritative state.

7. **Inject two independent partial failures** — Simulate a post-commit lost response and a delayed/failed external or worker step; demonstrate truthful UI state and safe final reconciliation.

8. **Execute complete cross-layer test evidence** — Run direct API, DB, negative security, browser E2E, concurrency, compatibility and accessibility checks with clean fixture setup/teardown.

9. **Make and validate a staged compatible change** — Extend one real workflow with a new field, permission or lifecycle variant; verify old/new client and DB compatibility as appropriate.

10. **Clean reproduction and unfamiliar defense** — From a fresh local checkout, run documented commands, respond to an unfamiliar bounded bug/requirement and defend trade-offs, uncertainty and limits.

## Completion requirements

**All sixteen APP5 outcomes** must be established through
the **seven required summative assessments** below.
A single evolving application may supply evidence for
each, where independent observations remain possible;
seven separate products or hosted cloud services are
**not required**. Lesson-level practice, exploratory
models and formative activities are preparation rather
than hidden additional completion gates.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP5-AS1` — Requirements, Architecture Trace and Integrated Contract | APP5-O1, APP5-O2, APP5-O3, APP5-O6, APP5-O14 | Requirements-to-evidence and failure matrices, architecture context/component/sequence views, API/OpenAPI fixtures, code and versioned local setup, UI/HTTP/DB traces, independent consumer tests and rationale |
| `APP5-AS2` — Authenticated Workflow, State and Cross-Tenant Integrity | APP5-O3, APP5-O4, APP5-O5, APP5-O6, APP5-O12, APP5-O14 | Role/action/field matrix, session and two-tenant synthetic fixtures, server/direct HTTP negative tests, DB before/after and controlled concurrency log, React state transition and focus observations, lost-response and identity-switch tests and security trade-off notes |
| `APP5-AS3` — Cache and Object-Style Resource Consistency | APP5-O4, APP5-O5, APP5-O7, APP5-O8, APP5-O11, APP5-O12 | Cache/data ownership diagram, policy and invalidation fixtures, private object lifecycle state table, tested access/byte/metadata failures, local files and DB manifests, orphan/cleanup verification and documented security/consistency limitations |
| `APP5-AS4` — Asynchronous Commit, Idempotent Progress and Reconnect | APP5-O5, APP5-O6, APP5-O9, APP5-O10, APP5-O11, APP5-O14 | Transaction/outbox/work-state model, dispatcher and progress code, HTTP/DB/job logs for duplicates/restart/lost reply, identity authorization matrix, stop/reconnect tests, UI status observations and limitations analysis |
| `APP5-AS5` — Partial Failure, Correlation and Recovery Investigation | APP5-O2, APP5-O5, APP5-O9, APP5-O10, APP5-O11, APP5-O12, APP5-O14, APP5-O15 | Fault-injection configuration, redacted cross-component trace and timing timeline, observed durable rows and retry counts, degraded UI/focus records, root-cause hypothesis and verified repair diff, bounded measurements and uncertainties |
| `APP5-AS6` — Compatible Full-Stack Evolution and Verification Strategy | APP5-O1, APP5-O3, APP5-O4, APP5-O6, APP5-O7, APP5-O13, APP5-O14, APP5-O15 | Cross-layer change-impact/compatibility matrix, versioned migration/app code, old/new consumer and browser fixtures, schema/DB checks, failing-before/passing-after results, staged-release simulation and rollback/forward-repair rationale |
| `APP5-AS7` — Integrated Full-Stack Product and Independent Engineering Defense | APP5-O1, APP5-O2, APP5-O3, APP5-O4, APP5-O5, APP5-O6, APP5-O7, APP5-O8, APP5-O9, APP5-O10, APP5-O11, APP5-O12, APP5-O13, APP5-O14, APP5-O15, APP5-O16 | Versioned repository/configuration/lockfile plus local seed and setup steps; published requirements, diagrams, API/role and state matrices; React/HTTP/PostgreSQL/job/file/cache source and tests; independent browser/API/DB security/failure evidence; correlation and performance traces; compatibility/change log; clean-start reproduction; and accessible written, recorded or live engineering defense |

### Shared execution, access, evidence and safety boundaries

- Record compatible maintained React/React DOM,
  TypeScript, Node/Fastify, PostgreSQL, driver and
  testing-tool versions, package locks/locally supplied
  dependencies, local origins/ports and synthetic
  fixture data. Initial free downloads are allowed;
  tests and independent demonstrations must be
  reproducible after documented local provisioning,
  without network registry access during assessment.
- The core project uses a local browser, loopback API,
  disposable PostgreSQL, a bounded worker and local
  cache/file/remote-response fixtures. It must not
  require managed Redis, S3, public DNS, paid identity,
  queues, hosted telemetry, a cloud account, real
  personal data or a microservices cluster.
- Implement a complete normal user journey and
  representative invalid, forbidden, empty,
  stale, conflicting, revoked, duplicate,
  lost-response and partial-failure cases. Evidence
  must identify actual client observations,
  HTTP responses, database state and job/file state.
- Authentication and action/object/property/tenant
  authorization occur at real server-held boundaries.
  Test direct HTTP calls independently of React,
  plus identity switches and cache invalidation.
  Client controls, storage or CORS are not permission
  enforcement. Cross-origin credential requests
  and CSRF protections must match the local
  authentication policy actually selected.
- Client values and HTTP/JSON/file metadata are
  untrusted until validated. Use bounded uploads,
  generated private storage IDs, server-controlled
  access, quarantined or rejected unsupported
  content, safe download responses and verifiable
  temporary-file cleanup. Do not treat extension,
  client MIME or a mocked malware scan as proof
  that bytes are harmless; no actual malware or
  real unsafe files are needed for negative tests.
- Do not pretend a SQL transaction is atomic
  with cache publication, a file operation,
  notification or external service. Model the
  lasting record, user-visible uncertainty,
  idempotency, retry and cleanup or reconciliation
  process explicitly. No exactly-once cross-system
  delivery claim follows from an outbox.
- Progress polling or an optional simple event
  stream must be bounded and authenticated;
  duplicated, delayed or missed notifications
  may not supersede more authoritative server
  resource/job state. Stop timers/connections
  on route changes, logout and terminal states.
- Use synthetic users/roles, localhost-only
  requests and allowlisted external-response
  fixtures for security and outage exercises.
  Never conduct scans/exploits against third-party
  services, use real credentials, upload private
  records or include sensitive cookies/headers/
  file contents in public logs or assessment data.
- Investigations into performance and recovery
  record runtime/browser, data volumes, topology,
  workload, conditions and uncertainty. A local
  timing or passing browser screenshot is not
  a production availability, penetration-test,
  privacy or WCAG certification.
- Validate screen-reader behavior when practical,
  but document actual keyboard, focus, announcement,
  zoom and reduced-motion evidence. A synthetic
  usability task is not an observed human study.
  Technical defense may be accessible written,
  recorded, synchronous or equivalent form.
- A reviewer may introduce an unfamiliar bounded
  failure, permission or contract change aligned
  with published outcomes. They must not impose
  additional unpublished services, paid software,
  advanced distributed systems or electives.

### Required summative assessments

- **APP5-AS1** (required requirements, architecture trace and integrated contract)
  - Outcomes: APP5-O1, APP5-O2, APP5-O3, APP5-O6, APP5-O14
  - Work: Given a bounded multi-tenant user-task brief and prior APP20/APP3 competence, publish verifiable flow/failure acceptance criteria, security/privacy assumptions and a system context, component and sequence trace. Connect a typed React UI to a real local Fastify/PostgreSQL contract for one protected operation; use a separate HTTP client to verify expected normal, invalid, denied, empty and conflicting outcomes and explain which data is authoritative at each boundary.
  - Criteria: Requirements map to real UI, HTTP, domain, SQL and test observations; the diagrams represent deployed local components honestly and show transaction and external effect limits. The browser and independent client consume the same published contract, validate runtime responses, and display actual method/status/problem distinctions. No API response is treated as successful merely because TypeScript compiles. The learner defends responsibilities and an unimplemented/unknown stakeholder claim without inventing real user testing.
  - Evidence: Requirements-to-evidence and failure matrices, architecture context/component/sequence views, API/OpenAPI fixtures, code and versioned local setup, UI/HTTP/DB traces, independent consumer tests and rationale.

- **APP5-AS2** (required authenticated workflow, state and cross-tenant integrity)
  - Outcomes: APP5-O3, APP5-O4, APP5-O5, APP5-O6, APP5-O12, APP5-O14
  - Work: Implement a session-backed multi-tenant React/API workflow with one genuinely durable PostgreSQL mutation and visible pending/committed/conflict/error states. Simulate two users/tenants, revoked/expired sessions, wrong-object IDs, mass-assignment fields, concurrent writes, a response lost after commit and stale requests after identity change. Inspect actual DB records and verify server-side access controls on reads, writes and returned fields, while React clears scoped state and recovers drafts truthfully.
  - Criteria: Authenticated identity and effective permissions are derived and enforced server-side, not from client tenant hints, hidden buttons or CORS; direct HTTP denial tests and database checks confirm no cross-tenant mutation/disclosure. Browser pending/optimistic results reconcile with committed facts under conflict and lost response; no naive retry duplicates a side effect or reveals a prior user's cache. Expiry, logout and accessibility of error/recovery paths are tested with meaningful messages and preserved input as specified.
  - Evidence: Role/action/field matrix, session and two-tenant synthetic fixtures, server/direct HTTP negative tests, DB before/after and controlled concurrency log, React state transition and focus observations, lost-response and identity-switch tests and security trade-off notes.

- **APP5-AS3** (required cache and object-style resource consistency)
  - Outcomes: APP5-O4, APP5-O5, APP5-O7, APP5-O8, APP5-O11, APP5-O12
  - Work: Implement a bounded tenant-aware client/API caching policy and one local private file/object-style resource lifecycle within the same evolving application. Verify cache keys, freshness/eviction/invalidation after a write, wrong-user isolation and permission revocation; process a synthetic uploaded object through staged metadata/content validation, publication, authorized retrieval and cleanup. Inject an oversize/wrong-type upload, attempted cross-tenant fetch, failed metadata/file step and orphaned resource condition, documenting what a real object store and time-limited signed URL would change.
  - Criteria: Cached private content cannot be retrieved after identity/permission changes or by another tenant, and committed mutations invalidate relevant stale views according to the published policy. Untrusted filenames, MIME claims and upload bytes are not sufficient security authority; server-side limits, nonpublic ownership, staged publication and cleanup are demonstrated. A simulated file scanner is not falsely claimed to prove malware-free content or production object-store security. Failed metadata/file actions produce inspectably consistent or explicitly recoverable state, not silent data loss.
  - Evidence: Cache/data ownership diagram, policy and invalidation fixtures, private object lifecycle state table, tested access/byte/metadata failures, local files and DB manifests, orphan/cleanup verification and documented security/consistency limitations.

- **APP5-AS4** (required asynchronous commit, idempotent progress and reconnect)
  - Outcomes: APP5-O5, APP5-O6, APP5-O9, APP5-O10, APP5-O11, APP5-O14
  - Work: Extend the integrated workflow with a transactionally recorded work intent/outbox or an equivalent convincingly durable local queue. Implement an independent bounded dispatcher, per-tenant status endpoint and a user-facing progress mechanism using bounded polling or a simple compatible event stream. Inject duplicate job delivery, missed notification, process restart, an invalid attempt and a response lost after the database commit. Reconnect or refresh the UI and derive truth from authoritative records, not the last notification.
  - Criteria: Committed intent is replayable after a worker restart, attempts are bounded and duplicated work does not repeat protected business effects. The learner distinguishes at-least-once delivery/notification from exactly-once external execution and can demonstrate an uncertain failure without falsely reporting success. Progress endpoint authorization and UI cleanup prevent cross-tenant leakage and orphaned pollers; terminal states, retries and reconnects are visible and accessible, and status reconciliation is demonstrated after a missed signal.
  - Evidence: Transaction/outbox/work-state model, dispatcher and progress code, HTTP/DB/job logs for duplicates/restart/lost reply, identity authorization matrix, stop/reconnect tests, UI status observations and limitations analysis.

- **APP5-AS5** (required partial failure, correlation and recovery investigation)
  - Outcomes: APP5-O2, APP5-O5, APP5-O9, APP5-O10, APP5-O11, APP5-O12, APP5-O14, APP5-O15
  - Work: Inject a slow or failed locally simulated outbound dependency and one separate database/cache/worker availability failure during a real user task. Capture sanitized browser correlation, server requests, database state and job/dependency events. Construct a causal timeline, expose an honest degraded/pending/error UI with retry/deadline policy, implement a bounded repair and verify completion or safe failure after dependency restoration. Repeat keyboard/focus checks and compare bounded end-to-end latency/recovery observations.
  - Criteria: Each observed failure is grounded in reproducible input/state/trace evidence and its owner and recovery obligations are identified; no invented logs or production SLA claims appear. Retried work does not corrupt committed business state or amplify load indefinitely; a fallback never claims completed delivery when only a durable intent exists. Logs protect secrets and scoped identities, the browser preserves user context and accessible error explanation, and an identified fault has a failing-before/passing-after regression.
  - Evidence: Fault-injection configuration, redacted cross-component trace and timing timeline, observed durable rows and retry counts, degraded UI/focus records, root-cause hypothesis and verified repair diff, bounded measurements and uncertainties.

- **APP5-AS6** (required compatible full-stack evolution and verification strategy)
  - Outcomes: APP5-O1, APP5-O3, APP5-O4, APP5-O6, APP5-O7, APP5-O13, APP5-O14, APP5-O15
  - Work: Apply one bounded change to a live local workflow—such as a new role-limited field, renamed response state or altered persistence invariant—across React components, Fastify schema/contract, domain/persistence, cache keys, work status and relevant tests. Stage an expand/backfill/validate/contract approach, run old and revised independent clients with a disposable migrated database, and demonstrate one deliberately introduced incompatibility caught before a repaired rollout. State whether source/database/file/work changes can be rolled back safely or require forward repair.
  - Criteria: The change-impact matrix accounts for every touched contract and authorized data boundary; both consumer versions exhibit the declared supported behavior and an incompatible change is observed and corrected or explicitly classified. Real DB schema/content and cache/work status are verified after migration and failure injection. The test plan includes unit, API, DB, security, contract and browser E2E levels without treating a coverage percentage as readiness. Unreversible data or dispatched external effects are not incorrectly labeled safe for automatic rollback.
  - Evidence: Cross-layer change-impact/compatibility matrix, versioned migration/app code, old/new consumer and browser fixtures, schema/DB checks, failing-before/passing-after results, staged-release simulation and rollback/forward-repair rationale.

- **APP5-AS7** (required integrated full-stack product and independent engineering defense)
  - Outcomes: APP5-O1, APP5-O2, APP5-O3, APP5-O4, APP5-O5, APP5-O6, APP5-O7, APP5-O8, APP5-O9, APP5-O10, APP5-O11, APP5-O12, APP5-O13, APP5-O14, APP5-O15, APP5-O16
  - Work: Deliver a complete cohesive local React/TypeScript plus authenticated Fastify/PostgreSQL vertical slice for a real user task and synthetic multi-tenant data. Reuse qualifying AS1–AS6 work rather than produce unrelated apps. Include documented UI/API/data contracts, server-enforced authorization, correct state reconciliation, tenant-scoped cache, a safe local private file resource, transactionally recorded async work and progress reconciliation, independent partial-failure recovery, a compatible change, multiple-layer tests, basic performance/observability evidence and accessible completion/error paths. Execute a fresh-checkout reproduction and respond to an unfamiliar bounded user or incident requirement with evidence-backed design defense.
  - Criteria: A reviewer can provision the stated free local tools, run the synthetic environment on unprivileged loopback and reproduce normal/invalid/forbidden/concurrent/stale/duplicate/failure/recovery cases without a paid cloud, production secret, public deployment or microservice fabric. Cross-layer authority and database invariants remain correct under tested races and retries; private cache/files/jobs do not cross tenants. The learner accurately distinguishes local demonstrated behavior from unverified production safety/availability, integrates the unfamiliar change while preserving existing contracts and accessibility, and gives a coherent technical defense of each boundary and its alternatives.
  - Evidence: Versioned repository/configuration/lockfile plus local seed and setup steps; published requirements, diagrams, API/role and state matrices; React/HTTP/PostgreSQL/job/file/cache source and tests; independent browser/API/DB security/failure evidence; correlation and performance traces; compatibility/change log; clean-start reproduction; and accessible written, recorded or live engineering defense.

### Completion decision, revision and downstream protection

Completion requires an inspectable satisfactory decision
on `APP5-AS1` through `APP5-AS7`, jointly demonstrating
`APP5-O1` through `APP5-O16`. A passing UI demo
alone is inadequate where the outcome claims server
authorization, database invariants, replay safety,
cache privacy, compatible changes or recoverable
partial failure. Material violations require
correction with actual negative-path evidence.

Reviewers should record the course/OEE source revision,
assessment/outcome IDs, controlled environments,
independent client/API/DB and browser test locations,
observed failure and recovery, change analysis,
accessibility investigations and unsupported claims
according to [OEE Evidence Rules](../../spec/evidence-rules.md).

APP5 retains its course ID while replacing the legacy
8-week lab/checkpoint contract and APP2+APP3+APP4 direct
prerequisites with a new OEE `v0.2.0` **draft**.
Earlier APP5 learner evidence remains tied to its
historical revision and is not silently upgraded
to the new criteria. A green repository parser
or successful software test does **not** establish
learner `tested` or `verified` status. APP6–APP9 and all APP electives now have separately
migrated `v0.2.0` drafts. Pinned OEE Workspace,
content/resource and 0xNAND consumer updates still
require explicit revision and evidence review.

### Public non-mandatory study references

These public sources support mechanism and standard
investigation but do not add hidden completion
requirements beyond the course above.

- [MDN Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
  and [MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS)
  for credential modes, origins and client/network failure behavior.
- [OWASP API Security](https://owasp.org/projects/api-security-project)
  and [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
  for object authorization, untrusted files, type/content and access controls.
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
  for durable data boundaries, concurrency and transaction semantics.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110.html)
  for cache/conditional and method contract interpretation.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
  for consumer-facing contract alignment.
- [React Learn](https://react.dev/learn)
  for existing client architecture and asynchronous view integration.
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
  and [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
  for dynamic state/error/accessibility review.
- [OpenTelemetry Trace Context](https://opentelemetry.io/docs/concepts/context-propagation/)
  for optional portable terminology in correlation/trace discussions.
