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

The 14–18-week duration and weekly workload remain
provisional planning estimates; fewer editorial lesson
entries do not prove lower study effort or learner-tested
readiness. Each of the **seven explicitly required
summative assessments** evaluates a distinct cross-layer
decision using **one evolving full-stack vertical slice**.
Module exercises remain formative. Accepted evidence may be referenced when it supports a later required assessment.

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

### Module 1 — User Journeys, Requirements and Cross-Layer Acceptance

#### Outcomes

- APP5-O1
- APP5-O2
- APP5-O14

#### Lessons

1. **A Full-Stack User Task and Its Historical Context** — Situate integrated browser/server/data development through one synthetic multi-tenant user problem, distinguishing APP20 React and APP3 API competencies from the new requirement that they agree on a single observable journey.

2. **Stakeholder Provenance, Actors and Data Invariants** — Use a supplied or consent-based brief, label actual observations versus assumptions, identify user/tenant roles, resource lifecycle and necessary forbidden actions without inventing participant research.

3. **Acceptance States and Independent Expected Results** — Specify success, empty, denied, validation, conflict, stale, pending, uncertain and recovery outcomes; define the server/database truth and what a user should observe in each, rather than add template statuses mechanically.

4. **Proportionate Privacy, Accessibility and Recovery Goals** — Set scoped privacy, task usability, time/size and recovery conditions with locally measurable expectations and honest production/real-user limitations.

5. **One Vertical Slice and Requirements-to-Evidence Map** — Choose one achievable document/reservation/workspace workflow; trace an action through interface, HTTP, application policy, transaction, optional file/job and checkable evidence, keeping extra features out of scope.

*Optional practice — requirements review:* Expose a misleading 'works on my machine' success claim and add the missing acceptance and recovery evidence.

### Module 2 — Application Topology, State Authority and Local Composition

#### Outcomes

- APP5-O2
- APP5-O3
- APP5-O6
- APP5-O11

#### Lessons

1. **Context, Component and Sequence Views of One Application** — Diagram React/browser, Fastify, PostgreSQL, local object/cache fixtures, worker and simulated dependency at the detail each decision needs; do not portray every module as a separate deployable service.

2. **Synchronous Write and Read Ownership** — Trace form action to credentialed HTTP, verified principal, domain rule, SQL commit, documented response and reconciled UI, identifying exactly where state becomes authoritative.

3. **Durable Intent and External Effect Boundaries** — Trace database-recorded work through local dispatcher, failure/duplicate event, durable status and browser refetch; distinguish database commit from externally completed work.

4. **One Cohesive Modular Monolith and Tested Wiring** — Choose a bounded local topology with versioned origins/ports, synthetic credentials, config, single source of truth and free pre-provisioned toolchain; explain when distribution is justified without requiring it.

5. **One Ownership/Atomicity Counterexample** — Find a browser-owned permission rule, wrong cache owner or transaction imagined to include an external notification; correct the architecture and demonstrate changed expected evidence.

*Optional practice — boundary trace:* Find a domain check leaking into React or a transaction falsely spanning an external HTTP call and repair the architecture view.

### Module 3 — React–Fastify Contract and Cross-Layer Failure Translation

#### Outcomes

- APP5-O1
- APP5-O3
- APP5-O5
- APP5-O11
- APP5-O14

#### Lessons

1. **Reuse Typed Contracts without Assuming Runtime Truth** — Connect the APP20 React interface to real APP3 Fastify/SQL behavior using independently verified OpenAPI/schema or generated types with runtime checks; avoid duplicating predecessor syntax lessons.

2. **HTTP Status, Content and User-Facing Meaning** — Inspect actual response status, media, empty/204, conflict 409, precondition 412, authentication 401, authorization 403, 429 and network failure; give truthful accessible recovery rather than blanket error toasts.

3. **Credentials, Cookies and Browser Origin Boundaries** — Configure documented same-origin or credentialed cross-origin local requests with appropriate CSRF policy; show CORS visibility is not API authorization.

4. **Data Contract Drift and an Independent Consumer** — Run a separately written HTTP consumer and real browser with conflicting/malformed/omitted fields, distinguishing TypeScript compilation, schema validation and actual UI behavior.

5. **Safe Correlation and Uncertain Client Retry** — Carry bounded request correlation without secrets or trusting caller-controlled IDs, and distinguish safely retriable reads from an uncertain post-commit write needing idempotency/reconciliation.

6. **Contract-Driven Failure Repair across Both Sides** — Inject a changed field, unexpected error shape or no-body result, demonstrate the failing client and repair both API response and user state without hiding an unsupported case.

*Optional practice — mismatched-contract repair:* Repair a runtime response missing a required field or returning inconsistent errors, with both client and server regression cases.

### Module 4 — Session, Tenant and Resource Identity across the Whole Journey

#### Outcomes

- APP5-O3
- APP5-O4
- APP5-O12
- APP5-O14

#### Lessons

1. **Verified Session through Reload, Route and Logout** — Use APP3's real local synthetic session to verify browser refresh, navigation, expired/revoked credentials and explicit sign-out; never equate client-held user IDs with verified principals.

2. **Direct Resource and Property Denials** — Execute independently issued HTTP list/detail/create/update/delete requests against two tenants, guessed IDs and extra writable/readable properties, inspecting actual unchanged DB rows and serialized output.

3. **Browser Visibility, Drafts and Server Authority** — Make UI navigation and form state reflect authorized data while proving hidden buttons and route guards do not grant/revoke permissions; preserve recoverable nonsecret drafts when appropriate.

4. **Authentication/CSRF Model for Mutations and Background Views** — Check the actual selected cookie/bearer mode and server CSRF controls where applicable; enforce server-held role/tenant identity for progress and file resources, not client-asserted claims.

5. **Revocation during Pending Work and Old-User Results** — Revoke/expire a session while upload, mutation, fetch or worker/progress poll is pending; ensure late results are discarded and privileged work is reauthorized or fails under an explicit policy.

6. **Two-Identity UI–API–DB Regression** — Switch two synthetic users/tenants, checking no previous-user cache, rendered result, file handle, status request or unauthorized row appears after logout or re-login.

*Optional practice — multi-tenant audit:* Inject a direct-resource access or stale-cache disclosure and verify the repaired server and UI behavior independently.

### Module 5 — Committed Mutations, Optimistic State and Cross-Layer Invariants

#### Outcomes

- APP5-O1
- APP5-O2
- APP5-O5
- APP5-O6
- APP5-O11
- APP5-O14

#### Lessons

1. **One Domain Invariant and its Actual Owning State** — Define a reservation, entitlement or document publication rule, contrasting local draft, optimistic prediction, API response and PostgreSQL committed fact, reusing APP4 and APP3 invariants.

2. **User-Visible Mutation State and Recovery Policy** — Model editing, submitting, confirmed, rejected, conflict, uncertain and reconciled transitions, retaining meaningful drafts, focus and accessible status rather than re-teaching React state syntax.

3. **Scoped Transaction and API Result** — Use one real service transaction for related writes and return correct success/conflict/validation semantics; inspect independently expected DB changes under a failed second write.

4. **Two-Client Race and Stale Revision** — Coordinate two real clients changing the same record with revision/If-Match or justified DB control; verify no unnoticed overwrite and choose an accurate 409/412 or project-specific conflict response.

5. **Lost Response after a Real Commit** — Drop an HTTP response after a committed change, show UI uncertainty and idempotent lookup/replay, and refuse blind retries that could duplicate side effects.

6. **Optimistic Rollback and Refetch of Server Truth** — Render provisional success only under an explicit contract; on conflict/rejection/lost response, preserve the user's intent while reverting or reconciling against real committed data.

7. **Cross-Layer Consistency after Cache or Job Delay** — Explain a committed database write with stale cached read or pending external job; state the actual consistency window rather than promise immediate availability across systems.

8. **Schema-to-UI Evolution at the Transaction Boundary** — Trace a changed field or constraint through migration, Fastify response, old/new React consumer, cache and durable status; defer detailed rollout evaluation to M11.

9. **Transaction–File/Notification Separation and Repair** — Reproduce a DB commit followed by failure to publish a file or send external notification; demonstrate retained truth and a compensating/forward-repair plan without claiming distributed atomic rollback.

*Optional practice — conflict scenario:* Run two synthetic clients editing the same resource and repair a misleading final-state message with database evidence.

### Module 6 — Identity-Safe Cache Ownership and Invalidation

#### Outcomes

- APP5-O4
- APP5-O5
- APP5-O7
- APP5-O11

#### Lessons

1. **Which Layer Owns a Cache and Why** — Compare browser memory, HTTP, API-side transient data and authoritative PostgreSQL; select one necessary bounded cache with a meaningful stale-read/privacy problem.

2. **Tenant, Principal, Resource, Filter and Version Keys** — Construct collision-resistant semantic keys using server-verified scope and relevant query/revision dimensions, and test a cross-user cache-collision counterexample.

3. **Freshness, Eviction and Invalidation after Commit** — Define TTL/eviction and write-after-read invalidation; demonstrate how a database mutation can leave cached list/detail state wrong until an explicit refresh.

4. **HTTP Validators and Privacy Semantics** — Use ETag/If-None-Match when beneficial and correctly scope Cache-Control, protected responses and conditional reads without mistaking caching headers for authorization.

5. **Revocation and Identity Switch while a Cache Exists** — Test a private response after logout/role change/tenant switch, preventing stale render or server-side unauthorized retrieval even if a local browser cache survives.

6. **Unavailable Cache and Bounded Recovery** — Inject a cache miss/stale response or local cache outage, prove the fallback respects policy and resource budget, and reject unnecessary hosted Redis/distributed stampede machinery.

*Optional practice — cache leak and stale row:* Reproduce a previous user's cached result or a stale post-edit list and verify the fixed key/invalidation policy.

### Module 7 — Private File Resources, Safe Publication and Cleanup

#### Outcomes

- APP5-O4
- APP5-O8
- APP5-O11
- APP5-O12

#### Lessons

1. **Files, Metadata and Nonpublic Ownership** — Separate arbitrary bytes, database metadata, published visibility and tenant/resource membership in one local object-style resource workflow; avoid pretending a file path is a credential.

2. **Staged Upload and Server Byte/Type Policy** — Model temporary, validated, published, rejected and expired states; generate storage IDs, enforce actual size limits and check appropriate content signatures without trusting filenames or client-supplied MIME.

3. **Safe Content Policy and Isolation Limits** — Use harmless synthetic adversarial content, reject unsupported formats and isolate unpublished bytes; demonstrate local validation cannot certify content malware-free or replicate provider scanning.

4. **Server-Authorized Download and Capability Risks** — Authorize every download against current principal and resource, set safe content/attachment response headers, and discuss signed URL bearer capabilities without requiring cloud storage.

5. **DB Commit versus Filesystem Publication** — Inject failures before and after metadata commit/file move, document observable temporary state and reconcile via a durable intent or bounded compensating cleanup rather than claim transactionally atomic file operations.

6. **Orphans, Revocation and Recovery Verification** — Expire abandoned uploads, detect orphaned objects and test tenant-switch/revoked download attempts while independently checking physical files, durable records and cleanup.

*Optional practice — file boundary investigation:* Test forged metadata, oversize data, wrong tenant download, stale signed-like token and failed publication; show safe rejection.

### Module 8 — Durable Job Results and User-Visible Progress Reconciliation

#### Outcomes

- APP5-O5
- APP5-O6
- APP5-O9
- APP5-O10
- APP5-O11
- APP5-O14

#### Lessons

1. **Synchronous Completion versus Accepted Background Work** — Decide when a real user operation completes inline and when HTTP 202 means only accepted or queued, never a guaranteed completed action; publish an authorized durable status endpoint.

2. **Transactionally Recorded Job Intent and State** — Use APP3's durable outbox/worker foundation and define tenant, idempotency identity, queued/running/retryable/completed/failed state, recorded attempts and no claimed cross-system atomicity.

3. **Duplicate Delivery, Lost Acknowledgement and Worker Restart** — Reproduce a durable restart, duplicate signal and committed-but-unacknowledged worker action; make the protected business outcome idempotent or explain unsupported external exactly-once claims.

4. **Safe Retries, Poison Jobs and Shutdown** — Bound attempts, backoff, final failure and work ownership when the worker stops, without silently discarding an already accepted job.

5. **Bounded Polling with Accessible Progress** — Implement bounded interval/backoff/visibility-aware polling with authenticated status reads, appropriate pending/terminal announcements and reliable cleanup on route/logout.

6. **Optional EventSource and Missed Event Semantics** — For a justified simple SSE alternative, demonstrate supported EventSource connection and Last-Event-ID behavior, but do not require SSE in addition to polling, and do not treat an event ID as an authoritative durable event log.

7. **Stale, Duplicate or Cross-Tenant Progress Counterexample** — Deliver delayed/duplicated/forged or old-identity progress updates and show a newer authoritative job/status query overrides stale presentation; never let unauthorized IDs reveal job metadata.

8. **Reconnect, Reload and User Recovery** — Interrupt the UI or drop events during a true job transition, then reauthenticate/revalidate and refetch actual durable state after reconnect to give accurate completion or failure feedback.

9. **User-Task Completion versus a Notification** — Test that final UI status and accessible controls reflect a committed business result rather than merely a delivered signal, including failure and retry instructions.

*Optional practice — duplicate-delivery scenario:* Restart a disposable local worker after a simulated crash and prove accepted work is neither silently forgotten nor duplicated as a business operation.

### Module 9 — Partial Dependency Failure, Degraded States and Retry Budgets

#### Outcomes

- APP5-O2
- APP5-O9
- APP5-O11
- APP5-O15

#### Lessons

1. **Real Failure Owners and Cross-Service Uncertainty** — Map browser network, API, DB, cache, files, worker and synthetic upstream failures to the specific state each owns without repeating APP3 outbound connector design.

2. **Timeout and Total Retry Budget across Layers** — Trace UI, API and worker backoff/retries, reproduce amplification under one slow dependency and assign a bounded retry owner instead of stacking automatic retries.

3. **Committed State and Uncertain External Effects** — Observe database committed data alongside timed-out remote notification or unpublished file; explain why AbortSignal and SQL rollback cannot undo completed external operations.

4. **Truthful Degraded, Queued and Failed UX** — Choose accurate loading/partial/accepted/failed messaging and focus/keyboard recovery so the user never sees success when the business result is still uncertain.

5. **Fallback and Safe Feature Limitations** — Decide when cache-served reads, queued intents or unavailable writes are acceptable under a real stated policy, and refuse a fallback that bypasses server authorization.

6. **Dependency Restoration, Reconciliation and Evidence** — Restore a synthetic upstream, inspect actual DB/job/file state and the UI's final result, and prove a causal fault repair with bounded measurements and honest missing evidence.

*Optional practice — cascading outage:* Simulate slow outbound dependency and retry storm; document bounded mitigation and what remains unsupported.

### Module 10 — Full-Stack Privacy, Security and Resource Lifecycle

#### Outcomes

- APP5-O4
- APP5-O7
- APP5-O8
- APP5-O11
- APP5-O12

#### Lessons

1. **Cross-Layer Attack Surface and Actual Risk Ownership** — Map current OWASP object/property/function authorization, session, unsafe input/upload, cache, job status and outbound URL risks onto the same user's journey, without reteaching APP3's isolated controls.

2. **Cookie, CSRF and Public Exposure Limits** — Challenge chosen credentialed Fetch/SameSite/CSRF behavior with synthetic local requests; distinguish browser CORS, deployed TLS requirements and server authority.

3. **Direct API, File and Progress Access Matrix** — Bypass the React UI and attempt unauthorized list/detail/write, download, status and optional event-stream access; inspect actual HTTP, durable rows and hidden fields across tenants.

4. **Revoked Identity, Cache and Job Leakage** — Expire a session or change role while a protected cache, file and async operation exists; test that no prior-user content or privileged action escapes across the boundary.

5. **Untrusted Bytes, Unsafe URLs and Retention** — Validate bounded file bytes/metadata, allowlist external request targets, safely dispose orphaned temporary resources and explain what local scanning and deletion do not guarantee.

6. **Package Provenance and Secret-Free Diagnostic Evidence** — Record pinned local dependencies and test-fixture provenance, sanitize correlation/logs and document concrete untested threats without claiming a production penetration test.

*Optional practice — trust audit:* Identify one client-only permission check and one leaked output in a local test, repair both at actual enforcement boundaries.

### Module 11 — Compatible Full-Stack Evolution and Independent Tests

#### Outcomes

- APP5-O1
- APP5-O3
- APP5-O6
- APP5-O13
- APP5-O14

#### Lessons

1. **One Bounded Business Change and Impact Map** — Trace changed field, role, status or invariant through browser validation, API/OpenAPI, SQL, caches, files, jobs and currently deployed clients, recording which boundaries actually change.

2. **Expand, Backfill, Verify and Contract** — Apply a staged schema/API/UI change with real existing rows, allow both old/new consumers during the supported period and verify when removal is safe.

3. **Independent Old/New Consumer and Browser Compatibility** — Run prior/current HTTP clients and a real browser under a deliberately incompatible field/status/permission change, showing one failing-before and repaired path.

4. **Data/External-Effect Rollback versus Forward Repair** — Demonstrate why a source rollback may not undo migrations, deleted files or dispatched notifications, and choose a tested restore/reconciliation or forward-repair policy.

5. **Independent Test Layers and Failure Oracles** — Combine React interaction, real browser, Fastify HTTP, actual Postgres row/invariant, role/security, worker and contract tests with a separately calculated expected result, not only shared mock assumptions.

6. **Deterministic Race and Migration Regression** — Coordinate controlled concurrent requests, deferred promises and isolated fixtures without arbitrary sleeps, and check compatibility/authorization after the staged change.

*Optional practice — compatibility break:* Inject a new required field or breaking enum and show which previous consumer fails, then amend staged evolution correctly.

### Module 12 — Cross-Layer Incident Diagnosis and Accessible Recovery

#### Outcomes

- APP5-O2
- APP5-O11
- APP5-O14
- APP5-O15

#### Lessons

1. **Request, Identity, Transaction and Job Correlation** — Connect sanitized browser events, independent HTTP observations, database state and worker/dependency events using bounded request/job IDs without recording session tokens or personal payloads.

2. **What Each Evidence Layer Can and Cannot Prove** — Compare screenshots, HTTP status, Postgres rows, worker logs and tests, distinguishing measured facts from inferred cause and explicitly recording absent spans.

3. **Critical Path and Comparable Local Latency** — Measure a real task's UI/API/DB/job path under a declared browser/runtime/data fixture; distinguish durations from different clocks, reporting variance and uncertainty.

4. **Inject Failure, Diagnose and Repair the Cause** — Seed one unavailable local dependency or bad state transition, reconstruct a defensible timeline and repair the mechanism, not merely a misleading error label.

5. **Recover Authoritative State and Accessible User Intent** — Check committed result, duplicate-job/failed-file effects, focus/keyboard and status announcements after recovery; preserve legitimate drafts and prevent previous-user exposure.

6. **Reproduce, Recheck and Defend Residual Risk** — Demonstrate failing-before/passing-after user, HTTP, DB and job observations, state limitations and avoid claims of production availability or WCAG certification.

*Optional practice — incident defense:* Repair a discovered misleading pending status or duplicate notification and provide before/after evidence across layers.

### Module 13 — One Defended Full-Stack Product and Unfamiliar Change

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

1. **One Bounded Vertical Slice and Accepted Evidence** — Use the same cumulative React–Fastify–PostgreSQL product assessed in APP5-AS1–AS6, with role/contract/ownership maps and links to accepted evidence rather than seven new apps.

2. **Real Identity, State, Cache and Private Resource Integration** — Integrate user task, protected durable mutation, reliable reconciliation, a justified scoped cache and one safe object-style resource with negative-case authority checks.

3. **Async Status, Failures and Contract/Accessibility Recheck** — Integrate durable job/reconnect behavior, two meaningful partial failures, old/new clients and real browser keyboard/focus/status observations using previously qualified evidence.

4. **Assessor-Supplied Change, Diagnosis and Regression** — Handle a new bounded permission, cache invalidation, file lifecycle, stale request, API evolution or incident counterexample, fix the right layer and rerun impacted client/server/data/job tests.

5. **Clean Offline-Capable Local Setup and Technical Defense** — Build/start/stop a free loopback reference with synthetic credentials and disposable DB/files, cite accepted evidence, describe true limits and defend trade-offs without requiring APP7 production deployment.

## Completion requirements

All **sixteen APP5 outcomes** require **seven independently
decidable summative assessments** on **one evolving local
full-stack product**. AS1 verifies the real journey/contract,
AS2 session and authoritative mutation state, AS3 private
cache/file access, AS4 durable progress reconciliation,
AS5 partial-failure diagnosis, AS6 compatible evolution
and AS7 an unfamiliar change and independent defense.
The same codebase, synthetic fixtures and previously
accepted observations may be **referenced**, but a
passing AS7 cannot excuse an unproven earlier required
assessment. Seven separate products, a public cloud or
compulsory module practice are **not** required.

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
  - Work: Begin **the one cumulative product** from a synthetic/consenting user-task brief, with acceptance, forbidden, conflict and recovery conditions and an honest browser/API/domain/PostgreSQL/job context/sequence model. Connect React to real Fastify/PostgreSQL on unprivileged loopback for one protected mutation. Verify OpenAPI/request/response/media semantics, runtime decoding, actual committed state and error UI through a separately authored HTTP consumer, not just matching TypeScript types.
  - Criteria: Observed browser, independent HTTP and real SQL results agree about the same operation and authority boundary; unsupported stakeholder assumptions are labeled. The contract covers no-body, malformed, forbidden and conflict paths correctly, and architecture views distinguish DB commit, cache publication and external effect. The actual user flow preserves semantic keyboard/status behavior rather than passing on a screenshot or simulated handler return.
  - Evidence: Requirements-to-evidence and failure matrices, architecture context/component/sequence views, API/OpenAPI fixtures, code and versioned local setup, UI/HTTP/DB traces, independent consumer tests and rationale.

- **APP5-AS2** (required authenticated workflow, state and cross-tenant integrity)
  - Outcomes: APP5-O3, APP5-O4, APP5-O5, APP5-O6, APP5-O12, APP5-O14
  - Work: Extend **the same product** with APP3's verified synthetic session/tenant authority and a durable multi-row change. Test login, refresh, expiry/revocation and role/tenant switches, guessed resource IDs, forbidden writable/readable properties, two concurrent writes, optimistic conflict and a **response deliberately lost after commit**. Independently inspect actual SQL rows and direct HTTP denials; in React demonstrate current-user state, draft preservation and safe late-response/cache cleanup.
  - Criteria: Actual verified sessions and server-held membership gate every protected action, resource and property, and denied requests do not modify or reveal another tenant's data. Two-client conflict and lost-response tests prove UI follows authoritative commit and does not blindly replay a non-idempotent operation. After identity switch or revocation, no previous-user result or progress content flashes, and focus/error/recovery remains understandable and keyboard operable.
  - Evidence: Role/action/field matrix, session and two-tenant synthetic fixtures, server/direct HTTP negative tests, DB before/after and controlled concurrency log, React state transition and focus observations, lost-response and identity-switch tests and security trade-off notes.

- **APP5-AS3** (required cache and object-style resource consistency)
  - Outcomes: APP5-O4, APP5-O5, APP5-O7, APP5-O8, APP5-O11, APP5-O12
  - Work: In **the existing product**, justify one bounded cross-layer cache and one private local object-style file lifecycle. Publish identity/resource/query-aware key and invalidation rules, test a stale committed update plus role/user switch, then stage an actual synthetic upload through server-enforced byte/type policy, generated storage identity, metadata authorization, private download and safe cleanup. Inject fake MIME, unexpected file signature, oversized body, denied tenant download, DB–file publication failure and an orphaned temporary object. Record SQL metadata **and actual local file** state.
  - Criteria: Cached private data is not disclosed across principals or stale privileges, and committed writes reconcile to the defined freshness policy. File identifiers, content type/byte limits, response/content disposition, server-held ownership and staged publication are independently checked. Temporary/orphan states are disposed or safely recoverable after failure; filename, client MIME, local signature or simulated scanner is never claimed to prove malware safety or provider-level signed URL guarantees.
  - Evidence: Cache/data ownership diagram, policy and invalidation fixtures, private object lifecycle state table, tested access/byte/metadata failures, local files and DB manifests, orphan/cleanup verification and documented security/consistency limitations.

- **APP5-AS4** (required asynchronous commit, idempotent progress and reconnect)
  - Outcomes: APP5-O5, APP5-O6, APP5-O9, APP5-O10, APP5-O11, APP5-O14
  - Work: Extend **the same operation** with a PostgreSQL-committed intent/outbox or genuinely equivalent restart-durable local job, an authorized job-status endpoint, and **one** proportionate client progress mechanism (bounded polling **or** justified SSE). Test the distinction between HTTP **202 accepted** and completed business work, a post-commit lost response, identical/changed-payload replay, duplicate delivery, a worker restart, dropped/delayed/duplicate progress and a logout/tenant switch. Reconnect and **refetch durable authoritative status** rather than trusting the last signal.
  - Criteria: The status/identity model does not report success until authoritative completion, and accepted/pending work is not silently lost on restart. A bounded idempotent processing policy prevents unintended business duplication while disclosing at-least-once notification/dispatch limitations. Only the currently authorized principal reads job status, orphaned polling/event listeners stop, and a missed signal or stale event cannot overwrite newer committed state. SSE, when used, is not called an exactly-once or durable queue; polling alone remains sufficient.
  - Evidence: Transaction/outbox/work-state model, dispatcher and progress code, HTTP/DB/job logs for duplicates/restart/lost reply, identity authorization matrix, stop/reconnect tests, UI status observations and limitations analysis.

- **APP5-AS5** (required partial failure, correlation and recovery investigation)
  - Outcomes: APP5-O2, APP5-O5, APP5-O9, APP5-O10, APP5-O11, APP5-O12, APP5-O14, APP5-O15
  - Work: Inject **two distinct** synthetic cross-layer failures in the previously assessed product: a slow/failed outbound dependency and a separate DB/cache/file/worker-availability or response-loss fault. Trace the browser action, real HTTP, database rows, worker attempts and external fixture with sanitized correlation, observing an accurate pending/failed/degraded interface rather than a false success. Reproduce a bounded retry-amplification or wrong-layer fallback counterexample, repair its cause and verify final state after restoration. Assess real keyboard/focus/status recovery and compare local timing measurements with recorded environment/uncertainty.
  - Criteria: Two independent fault mechanisms have observed failing-before/passing-after evidence; database and job/file outcomes, user-visible state and retry budgets agree without losing committed work or duplicating external effects. Correlation distinguishes a measured event from inferred causation or absent telemetry. Safe fallback never bypasses tenant policy; secrets are redacted and measured local recovery is not mislabeled production uptime. User input and accessible status/keyboard behavior survive honest recovery.
  - Evidence: Fault-injection configuration, redacted cross-component trace and timing timeline, observed durable rows and retry counts, degraded UI/focus records, root-cause hypothesis and verified repair diff, bounded measurements and uncertainties.

- **APP5-AS6** (required compatible full-stack evolution and verification strategy)
  - Outcomes: APP5-O1, APP5-O3, APP5-O4, APP5-O6, APP5-O7, APP5-O13, APP5-O14, APP5-O15
  - Work: Apply **one bounded cross-layer change** to the same real user journey—e.g. an owned response field, permission, lifecycle state or SQL invariant—using an explicit impact map through React, Fastify/OpenAPI, PostgreSQL migration, cache keys, private file/job status and tests where affected. Deliberately introduce one old-client/schema incompatibility, run **independent old and revised HTTP consumers and an actual browser**, then stage expand/backfill/validate/contract with real existing data and corrective evidence. Inject a rollback/forward-repair decision where an external effect or schema transformation is not reversible.
  - Criteria: Old/new supported clients and real Postgres state demonstrate the declared compatibility window, not just a generated-types diff. A failing-before/passing-after regression identifies and corrects or explicitly rejects the breaking case; the migration preserves tenant authorization and correct cache/job presentation. Tests cover real browser, API, SQL, contract, security and targeted asynchronous failures. A source-code revert is not falsely claimed to reverse already dispatched external effects or lost data.
  - Evidence: Cross-layer change-impact/compatibility matrix, versioned migration/app code, old/new consumer and browser fixtures, schema/DB checks, failing-before/passing-after results, staged-release simulation and rollback/forward-repair rationale.

- **APP5-AS7** (required integrated full-stack product and independent engineering defense)
  - Outcomes: APP5-O1, APP5-O2, APP5-O3, APP5-O4, APP5-O5, APP5-O6, APP5-O7, APP5-O8, APP5-O9, APP5-O10, APP5-O11, APP5-O12, APP5-O13, APP5-O14, APP5-O15, APP5-O16
  - Work: Finish **the same cumulative React/TypeScript–Fastify–PostgreSQL vertical slice** evaluated across APP5-AS1–AS6, with one scoped cache, a protected local file lifecycle, durable asynchronous work, user-facing status and independently observed security/recovery/compatibility behavior. **Reference previously accepted source/tests/evidence** rather than submit seven separate products or recreate complete logs. Implement an unfamiliar bounded requirement or newly seeded client/API/cache/file/job/permission failure, repair the correct layer and verify impacted previous decisions from a clean free local checkout. Defend state authority, coordination, security and uncertainty.
  - Criteria: A reviewer can independently start, exercise and stop the entire synthetic local workflow without a paid service, real credentials, hosting or a production infrastructure. Genuine HTTP, database and browser evidence proves authorization, optimistic/concurrent and lost-response correctness, cache/file privacy, durable work/reconnect and accessible error/recovery; new changes do not invalidate earlier accepted cases. **AS7 cannot substitute for a missing AS1–AS6 decision**, and material cross-tenant leaks, duplicate side effects, data loss or irreproducible required behavior block passing. Real production guarantees remain explicitly unverified.
  - Evidence: **One** versioned code/fixture and compatible free pinned local setup, a concise **outcome-to-accepted-AS1–AS6 evidence index** rather than duplicate reports, independent browser/HTTP/SQL/job/file and security observations, unfamiliar-change diff with targeted before/after regression, accessibility/measurement limits and an accessible technical defense.

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

APP5 remains an OEE `v0.2.0` `draft` course requiring APP20 and APP3. APP4 preparation is supplied through APP3. Learner completion requires the published summative evidence; source validation does not establish `tested` or `verified` readiness. Records must retain the course/specification revision actually evaluated. Updates to OEE Workspace, content mappings or 0xNAND source pins require separate review.

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
