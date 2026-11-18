# APP3 — Backend Framework Engineering

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `core`
**Prerequisites:** [APP19](APP19.md) — TypeScript Programming, [APP21](APP21.md) — Node.js & Backend Foundations, [APP4](APP4.md) — Databases & Data Modeling
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; calibrate with actual learner evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Build secure, independently testable, maintainable **framework-based
backend services** from a credible requirements and API contract.
Apply TypeScript, Node's runtime and relational data engineering
as established by prerequisite courses: define route/framework
lifecycles, validate and serialize untrusted data, preserve domain
invariants across adapters and PostgreSQL transactions, establish
real local authentication and **server-side per-object, per-action,
per-property and per-tenant authorization**, handle concurrency
and duplicate requests, integrate bounded asynchronous/dependency
work, publish versioned consumer contracts, diagnose failures,
and defend an integrated typed service.

This core course retains its established direct prerequisites
**APP19, APP21 and APP4**, and assesses the distinctive
framework/application responsibilities beyond those foundations. [APP19](APP19.md) already
teaches TypeScript contracts and runtime type limits.
[APP21](APP21.md) teaches the raw Node HTTP/stream/process
runtime and general fault boundaries; it is not repeated as
a JavaScript introduction. [APP4](APP4.md) already teaches
relational design, SQL, integrity, isolation, tenant RLS and
backup/recovery. APP3 focuses on **using** those competencies
together in a framework-driven service with contracts,
security, transaction orchestration and consumer evidence.

**Reference stack:** a mutually compatible supported release
of [Fastify](https://fastify.dev/), TypeScript, Node.js,
PostgreSQL and an appropriate open-source local driver/session
implementation, including their documented plugin and schema
validation mechanisms. Fastify's plugin encapsulation,
request lifecycle, schema compilation, request validation and
response serialization make framework-specific reasoning
observable. Teach portable HTTP and domain principles alongside
those facilities; a learner should be able to explain what
would change under another framework.

A reference implementation should favor a **small cohesive
single service**: 2–3 synthetic tenants/roles, clear resource
ownership, one transactional invariant and one honest async
workflow. A microservices estate, managed queue, distributed
deployment, paid auth provider, commercial observability
tool, browser frontend, production endpoint or real credential
is **not** required. Tools may be pre-provisioned or installed
for free before the assessed work; provide pinned, reviewable
dependency and fixture artifacts so required execution can be
repeated offline from a clean local checkout after provisioning.
A disposable local PostgreSQL cluster, loopback Fastify server,
free local HTTP clients and synthetic account/session fixtures
are enough. Avoid touching shared databases or testing any
third-party account without permission.

**Actual security properties matter.** Authentication must
verify a supported credential/session mechanism; a header
called `user-id` or client-provided `tenant-id` is not an
authenticated principal. Authorization must be enforced on
the server for every relevant action, object and property.
A database RLS policy may add defense in depth but does not
excuse missing application checks. TypeScript signatures,
response schemas, CORS, UI hiding and locally passing tests
do not automatically prove security. Test expired/revoked
sessions, cross-tenant reads/writes, mass assignment,
ownership changes, oversized requests and failure paths.
Local loopback/HTTP testing cannot stand in for production
HTTPS, CSRF, session storage, secret management and
multi-instance infrastructure review.

**Correctness across failure boundaries matters.**
A database transaction is not atomic with a remote API
call. Network retries cannot indiscriminately repeat a
side-effecting request. In-process background promises are
not durable jobs. An outbox or another documented durable
record may bridge database commits to at-least-once dispatch,
but it cannot promise exactly-once execution in a separate
system. Model uncertain results, retries, duplicate requests,
shutdown, health and recovery honestly. Use independent
HTTP clients, actual disposable PostgreSQL connections,
fault injection and appropriately redacted correlation
evidence, not only mocked handler return values.

API contracts should describe real HTTP method/status
semantics, versioned request/response schemas, strict
response fields, security expectations, pagination and
compatible evolution. Machine-readable OpenAPI and a
stable public problem/error format are useful reference
patterns; an RFC 9457-inspired response must not be
falsely labeled conformant unless its actual shape
satisfies that standard and the correct media type.
Framework schema compilation is **trusted application
code**; never compile untrusted user-supplied schemas.

**Cross-course boundary:** APP5 owns frontend/backend
integration, cross-layer identity and whole-application
behavior; APP6 owns broader engineering quality/CI and
reliability strategy; APP7 owns actual production
deployment and service releases; APP8/APP9 own
system/product-wide architecture and defense.
APP11 is an optional advanced backend architecture
specialization. APP3 must leave learners ready to build
a verified backend service without pretending to have
already operated it on a production platform.

The 14–18 week timeline is a provisional workload
estimate reflecting authentication, authorization,
real transaction races, API contract compatibility and
fault-injection evidence. It is **not** proof of
educational readiness. Module investigations are
formative unless specifically covered by a required
summative assessment below; one evolving service
can provide evidence throughout the course.

## Learning outcomes

- **APP3-O1:** Translate a bounded product/service problem into testable API requirements, threat/trust assumptions, consumer scenarios and explicit operational and failure criteria, distinguishing supplied stakeholder hypotheses from verified user evidence.
- **APP3-O2:** Implement and explain a TypeScript backend service using a documented supported Fastify release, its route/plugin/encapsulation model and request lifecycle; distinguish framework concerns from Node host and portable HTTP behavior.
- **APP3-O3:** Design stable resource-oriented HTTP interfaces with correct methods, status codes, media types, pagination, filtering, conditional requests where appropriate, versioned request/response contracts and independent consumer examples.
- **APP3-O4:** Validate and serialize untrusted request/response data using explicit runtime schemas, shape/size limits, well-defined normalization and safe structured errors; distinguish TypeScript inference, schema compilation and domain authorization.
- **APP3-O5:** Organize transport, application, domain and persistence responsibilities behind testable boundaries with dependency injection or another defensible composition strategy, preserving domain invariants independent of Fastify.
- **APP3-O6:** Implement a locally reproducible and credible authentication boundary using appropriately maintained credential/session mechanisms, deliberate cookie/token handling, expiry/revocation and negative tests; explain which additional public-deployment protections remain outside the exercise.
- **APP3-O7:** Enforce server-side action, object, property and tenant authorization on reads and writes using a verified principal and authoritative resource ownership, including cross-tenant/role escalation and forbidden-field negative evidence.
- **APP3-O8:** Integrate PostgreSQL persistence, database constraints and transaction orchestration for domain operations, demonstrating correct commit, conflict and rollback behavior when multiple application requests race.
- **APP3-O9:** Design bounded retry/idempotency and asynchronous work with explicit duplicate, partial-failure and shutdown policies, distinguishing an in-process task from a durable job/outbox and preventing unjustified replay of external effects.
- **APP3-O10:** Implement trustworthy outbound dependency boundaries with timeouts, abort ownership, response validation, circuit/overload policy where justified and controls against untrusted target URLs, secret exposure and unsafe dependency data.
- **APP3-O11:** Publish a portable machine-readable API description and meaningful examples; verify contract alignment, consumer compatibility and a bounded API revision, including breaking changes and error semantics.
- **APP3-O12:** Establish safe runtime configuration, request/resource limits, dependency readiness, graceful cleanup and low-overhead structured correlation/health signals; distinguish service-level operation from APP7 production deployment.
- **APP3-O13:** Apply a coherent API threat model covering authentication flaws, broken object/property/function authorization, mass assignment, injection, CSRF/CORS misconceptions, resource exhaustion and vulnerable dependencies, with verified proportionate mitigations.
- **APP3-O14:** Design and run independent domain, HTTP integration, database, contract, security, concurrency and fault-injection tests with realistic negative cases and reproducible fixture isolation.
- **APP3-O15:** Investigate a production-style service incident using sanitized logs/metrics/request correlation, reproduce a root-cause defect, document recovery and defend a tested repair without inventing telemetry or unsupported performance assurances.
- **APP3-O16:** Deliver, reproduce, maintain and independently defend a cohesive typed backend API/service under an unfamiliar bounded requirement or fault, explaining the security, data, framework and operational trade-offs using inspectable evidence.

## Modules

### Module 1 — Service Problem, Trust and Local Reference Environment

#### Outcomes

- APP3-O1
- APP3-O2
- APP3-O5
- APP3-O16

#### Lessons

1. **A Bounded Framework-Service Problem** — From a fictional two-tenant reservation/inventory brief, identify actors, domain invariants, acceptance/denial, operational failures and client-visible HTTP behavior. Situate modern HTTP frameworks briefly at the point of use; reuse APP19, APP21 and APP4 competence instead of reteaching it.

2. **Compatible Fastify/PostgreSQL/TypeScript Toolchain** — Pin and record compatible maintained framework/runtime/driver/schema/session dependencies and a free local reproducible lockfile; distinguish pre-provisioning from offline assessed execution.

3. **Independent Client and Synthetic Tenants** — Establish disposable database, two tenant fixtures, safe fake identities and a separate real HTTP consumer. Distinguish client assertions from server-held principal and tenant facts.

4. **Actual Trust and Threat Boundary** — Map input/body/header/cookie, verified identity, domain state and upstream dependency to the check that owns each; name concrete unsafe assumptions to challenge later.

5. **Requirements-to-Test Trace** — Map accepted, invalid, forbidden, conflict, replay and partial-failure cases to an endpoint, independent expected state and concrete evidence; explicitly mark synthetic stakeholder assumptions.

*Optional practice — Bounded API Design Review:* Inspect a tempting overfeatured service brief, choose a coherent vertical slice and document deferred needs without omitting required negative cases.

### Module 2 — Fastify Plugin Encapsulation, Hooks and Service Lifecycle

#### Outcomes

- APP3-O2
- APP3-O4
- APP3-O5
- APP3-O12

#### Lessons

1. **Why Fastify beyond Raw Node HTTP** — Reuse APP21's HTTP runtime knowledge, demonstrate a real framework advantage in route/schema/plugin/lifecycle scope and explain what remains portable.

2. **Typed Factory, Injector and Resource Ownership** — Create a Fastify app factory separate from listen, wire bounded dependencies, run inject and a real loopback client, and own ready/close/DB pool cleanup.

3. **Actual Hook Order and Authorization Placement** — Trace installed-version route matching/parsing/schema/preValidation/preHandler/onSend/onResponse behavior and locate principal verification plus per-object authorization without claiming schema shape validation is a security policy.

4. **Plugin Encapsulation and Registration Fault** — Demonstrate scoped plugin/decorator dependencies, reproduce a missing or unexpectedly shared capability and verify a corrected hook/plugin trace.

5. **Replies, Errors and Double-Send Limits** — Test early reply, thrown/rejected failures and schema serialization errors; prevent second sends after response commitment and preserve safe diagnostic causes.

6. **Startup, Ready and Test Teardown** — Show invalid configuration before listen, independent repeated test instances and a clean bounded close path with no leaked sockets or database clients.

*Optional practice — Plugin Boundary Fault:* Repair an encapsulation or hook-order defect and explain it with a request trace rather than a vocabulary-only answer.

### Module 3 — HTTP Operations, Pagination and Consumer Contracts

#### Outcomes

- APP3-O1
- APP3-O3
- APP3-O4
- APP3-O11

#### Lessons

1. **Resource and HTTP Method Contracts** — Use concrete resource actions and stable IDs to distinguish safe/idempotent HTTP method semantics from business deduplication; inspect actual side effects through a separate client.

2. **Status, No-Body and Error Meaning** — Verify created/accepted/no-content, bad-input, unauthorized, forbidden, missing, conflict and upstream failures with actual HTTP headers and correct no-body/HEAD behavior.

3. **Media Types, Public Response and Safe Problem Shapes** — Define JSON Content-Type/Accept, response field and status commitments; if claiming RFC 9457 check required fields and application/problem+json rather than mislabeling any error JSON.

4. **Deterministic Filtering and Pagination** — Validate filter allowlists and bounded pages, stable sort tie-breakers and cursor semantics under changing data; do not repeat APP4 SQL grammar.

5. **Optimistic Preconditions and Client Conflicts** — Test one ETag/If-Match or explicit revision-token stale write and distinguish observable precondition policy from actual Postgres transaction protection.

6. **Consumer Compatibility from One Changed Contract** — Exercise independent old/new consumers with valid and malformed requests; identify what changed and carry the decision into later OpenAPI evolution rather than assuming compatibility.

*Optional practice — HTTP Ambiguity Audit:* Find an underspecified DELETE, pagination tie or invalid method response, then revise the contract and independent tests.

### Module 4 — Runtime Schemas, Serialization and Safe Failure

#### Outcomes

- APP3-O3
- APP3-O4
- APP3-O13

#### Lessons

1. **Static Types versus Actual Runtime Trust** — Demonstrate one cast accepted by TypeScript but invalid for a real JSON request; separate shape checking, domain invariants, identity and property authorization.

2. **Request Schema, Coercion and Unknown Fields** — Check actual Fastify params/query/body/headers schema behavior under the installed Ajv configuration, including coerced values and additional-property handling.

3. **Response Serialization and Confidential Property Tests** — Define a deliberately narrow public schema and inspect real serialized fields, comparing route internals with actual client output on normal and error paths.

4. **Reviewed Schema Compilation and Unsafe Inputs** — Explain that Fastify validation/serialization code generation treats schemas as trusted code; reject attacker-provided schemas and defer DB/async authorization checks to appropriate hooks or service logic.

5. **Shape Validation versus Async Authorization** — Place database-backed membership and domain lookups after safe parsing/shape checks; reproduce a counterexample where valid shape passes but forbidden ownership must still fail.

6. **Real Validation, Serialization and Error Failure Matrix** — Inject malformed, ambiguous/coerced and unknown fields, oversized content, serialization failure and domain errors; show correct status, privacy and once-only reply behavior.

*Optional practice — Schema/Type Drift:* Produce a counterexample where a declared inferred type and actual validator behavior differ, then fix both evidence and code.

### Module 5 — Domain Rules and Application Service Boundaries

#### Outcomes

- APP3-O1
- APP3-O5
- APP3-O8
- APP3-O14

#### Lessons

1. **A Framework-Free Domain Invariant** — Define a real reservation/inventory invariant and test it with synthetic data without importing Fastify or PostgreSQL.

2. **Domain Identity, State and Valid Change** — Represent identity and quantities with meaningful constraints and failure cases rather than repeat APP4 normalization; check actual domain state transitions.

3. **Application Authorization and Transaction Orchestration** — Place authoritative permission and domain decisions in a coherent use case and explicitly own the transactional unit, rather than scattering rules among hooks and repositories.

4. **Adapter Ports, Composition and Trust** — Bind real PostgreSQL/clock/dispatcher interfaces to one app factory; compare a helpful fake with real DB/HTTP tests it cannot replace.

5. **Change a Coupled Route without Changing its Contract** — Repair a route with business logic in the wrong layer and prove unchanged role permissions, result status, rollback and public fields with independent tests.

*Optional practice — Refactor Review:* Add a new business constraint and demonstrate one place where the rule belongs plus a regression that catches bypass.

### Module 6 — Real Authentication and Session Lifecycle

#### Outcomes

- APP3-O6
- APP3-O7
- APP3-O12
- APP3-O13

#### Lessons

1. **Verified Identity Is Not Authorization** — Distinguish a cryptographically or store-verified principal from client-supplied identity or tenant labels and from permission to access particular resources.

2. **Credible Local Credential and Session Policy** — Choose a maintained opaque session or verified token method with expiry, revocation and local test isolation; no made-up user-id header or homemade authentication protocol.

3. **Safe Secret Storage and Verification** — Use a reviewed password KDF and entropy when password sign-in is in scope; verify credentials without plaintext reusable secrets, and document appropriate parameters.

4. **Cookie/Token, CSRF and Rotation Boundaries** — Inspect bearer versus cookie transport, Secure/HttpOnly/SameSite, fixation/rotation and TLS/CSRF assumptions, without asserting loopback HTTP is deployment-grade.

5. **Expired, Revoked and Forged Credential Evidence** — Attempt forged, expired and revoked logins plus session fixation/replay; keep tokens out of URL/logs and explain whether result demonstrates authentication or merely handler success.

6. **Trusted Principal, Hook Placement and Login Abuse** — Build principal context only after verification, bound login attempts and enumeration, invoke authorization on actual objects and test logout/stale-session denial under a declared local threat model.

*Optional practice — Authentication Failure:* Inject expired/revoked or forged session data and show denial plus appropriately sanitized diagnostic evidence.

### Module 7 — Action, Object, Property and Tenant Authorization

#### Outcomes

- APP3-O5
- APP3-O7
- APP3-O8
- APP3-O13
- APP3-O14

#### Lessons

1. **Actions, Objects, Properties and Principals** — Separate function permission, object ownership and allowed read/write properties, using current OWASP API risk classes only to select concrete attacks.

2. **Two-Tenant Role/Action/Field Matrix** — Publish actual permissions and exceptions for owners, members, guests and elevated roles across methods and resource fields, with denied-write state expectations.

3. **Membership from Authoritative Data** — Derive tenant scope from a verified principal and persisted membership, not a request header/context variable, and identify scoped trusted admin exceptions.

4. **Repository Scope and Defense-in-Depth RLS** — Test scoped queries and application policy with real PostgreSQL rows, while acknowledging APP4 RLS protects an additional boundary but is not sufficient alone.

5. **BOLA/IDOR and Function-Level Access Negatives** — Probe guessed and nested IDs, list/detail/bulk enumeration and unauthorized operations using independent requests and inspect unchanged authoritative data.

6. **Mass Assignment, Response Projection and Delayed Authority** — Attempt forbidden input updates and leaked output columns, then challenge a queued task with stale authority; keep privileged service accounts out of ordinary tenant paths.

*Optional practice — Cross-Tenant Attack Fixture:* Reproduce a local unauthorized request that initially succeeds, then fix the policy and verify all negative matrix entries.

### Module 8 — Database Integration, Invariants and Concurrent Requests

#### Outcomes

- APP3-O5
- APP3-O8
- APP3-O9
- APP3-O14

#### Lessons

1. **Real PostgreSQL Integration, Not Another SQL Introduction** — Reuse APP4's tested schema, constraints and transaction model inside Fastify repositories with documented driver versions and pool ownership.

2. **Bound Values, Connections and Trusted Identifiers** — Exercise a bound query, connection lifecycle and strict dynamic identifier allowlist; distinguish client-generated strings from server-controlled SQL.

3. **One Transaction Connection across Service Layers** — Deliberately run part of a multi-row operation on the wrong connection, observe an incomplete rollback and repair use-case/transaction scope.

4. **Independent Database Invariant Checks** — Verify real two-row domain changes before/after an intentional failure, including constraint enforcement and no unauthorized tenant row changes.

5. **Two HTTP Requests and Revision Conflict** — Coordinate an actual pair of PostgreSQL-backed requests to reproduce a stale revision/contention result, apply conditional update/constraint/isolation control, inspect final state and HTTP conflict responses.

6. **Retry the Whole Safe Transaction** — Handle real retryable serialization/deadlock failure with bounded full-unit retry and fresh state without replaying unrelated external effects; relate migration/cleanup to established APP4 competence.

*Optional practice — Transaction Leak:* Repair a repository method that uses a different connection mid-transaction and prove rollback/commit integrity with real database evidence.

### Module 9 — Idempotency, Durable Work and Partial Failure

#### Outcomes

- APP3-O8
- APP3-O9
- APP3-O10
- APP3-O13

#### Lessons

1. **Business Replay versus HTTP Method Idempotence** — Define why safe/idempotent methods and idempotency keys solve different problems for a real charge/reservation-like local side effect.

2. **Key Scope, Fingerprints and Conflicting Replays** — Specify tenant/principal/operation scope, request fingerprint, expiry and duplicate-in-flight semantics with synthetic fixture outcomes.

3. **Atomic Idempotency State with the Domain Write** — Use actual database records to show key reservation, business mutation and replay state commit or roll back together across two concurrent requests.

4. **Ephemeral Work versus Restart-Persistent Jobs** — Crash a local in-process queue and contrast it with a durable database record; explain state that can or cannot be recovered on restart.

5. **Outbox/Worker at Least Once and Failure Boundaries** — Demonstrate transactionally recorded dispatch intent, bounded retries/poison handling and idempotent consumer processing, explicitly rejecting exactly-once external execution.

6. **Commit then Failure, Uncertain Results and Shutdown** — Inject a failed external call after DB commit, lost response or service stop; inspect persisted work and define safe replay/compensation rather than assuming rollback spans the network.

*Optional practice — Duplicate Request Drill:* Replay concurrent identical and conflicting requests and a simulated dispatcher restart, verifying each business invariant and documented status/result.

### Module 10 — Outbound Dependencies, SSRF and Failure Budgets

#### Outcomes

- APP3-O4
- APP3-O9
- APP3-O10
- APP3-O12
- APP3-O13

#### Lessons

1. **Untrusted Synthetic Upstream behind an Adapter** — Use a locally controlled external fixture with checked data shape and error classification; avoid real third-party accounts or remote test targets.

2. **SSRF and Redirect/DNS Trust Boundaries** — Use an allowlisted scheme/host/target, reject redirects to unapproved destinations, and explain why simple string-prefix checking fails against DNS rebinding, IP changes and internal endpoints.

3. **Real Body, Time and Concurrency Limits** — Bound actual response bytes, deadline and in-flight resources, distinguishing AbortSignal from the guaranteed cancellation of an already executed remote mutation.

4. **Invalid Dependency Data and Safe Public Errors** — Compare 4xx/5xx, malformed shape, network rejection and secret-bearing upstream error, disclosing only stable safe client codes.

5. **Bounded Retry and Overload Choice** — Choose retry/backoff only for justified eligible work with total budget and a small circuit/bulkhead alternative where evidence warrants; reject uncertain write replay.

*Optional practice — External Failure:* Simulate malformed responses, slow dependency, redirect to an unapproved target or repeated 503s and verify controlled behavior and clean logs.

### Module 11 — OpenAPI, Compatibility and Independent Consumers

#### Outcomes

- APP3-O1
- APP3-O3
- APP3-O4
- APP3-O11
- APP3-O14

#### Lessons

1. **A Portable Executable OpenAPI Contract** — Generate/maintain a machine-readable operation/response/security/error contract that matches actual Fastify schema and status behavior.

2. **A Verified Single Contract Authority** — Choose schema-first or generated code-first, expose a discrepancy where TypeScript/schema/OpenAPI disagree and correct it against real consumer evidence.

3. **Old/New Consumers and Compatibility Decision** — Run old/revised clients for changed required/optional response fields, pagination/enum expansion and identify a real incompatibility rather than assuming all additions are safe.

4. **Security, Errors and Precondition Compatibility** — Test changed authentication/field exposure, RFC 9457 media/status and an optimistic precondition or deprecation policy under an explicitly bounded support decision.

5. **Independent HTTP Contract Regression** — Compare documented examples and security schemas against actually sent success/denied/invalid/conflict requests, with a failing-before/passing-after correction.

*Optional practice — API Revision Review:* Apply a bounded requirements change and identify one breaking consumer consequence caught by a failing test.

### Module 12 — Configuration, Readiness, Shutdown and Diagnostics

#### Outcomes

- APP3-O2
- APP3-O8
- APP3-O12
- APP3-O15

#### Lessons

1. **Validated Startup and Trustworthy Readiness** — Reject missing/untrusted configuration before listen and make health/readiness report actual local dependency conditions without secrets.

2. **Bounded In-Flight Shutdown and Pool Ownership** — Close Fastify and DB/dispatcher resources with measured in-flight request behavior and a forced-stop limit; compare planned and observed lifecycle.

3. **Safe Request/DB/Job Correlation** — Generate scoped bounded request IDs and trace a real HTTP/transaction/dispatch failure without storing tokens, personal payloads or raw SQL secrets.

4. **Actual Local Cancellation and Cleanup** — Trigger shutdown/abort during an in-flight DB job and verify a safe policy for remaining work, sockets and connections under the documented Fastify/Node release.

5. **Dependency Failure and Evidence-Based Incident** — Inject unavailable DB/upstream or invalid config, observe actual readiness and correlation, identify known missing telemetry and repair a supported cause, not a fabricated production incident.

*Optional practice — Health and Shutdown Audit:* Find a green-but-broken readiness check or connection leak and verify a corrected bounded test.

### Module 13 — Adversarial API Verification, Tests and Incident Analysis

#### Outcomes

- APP3-O3
- APP3-O4
- APP3-O5
- APP3-O6
- APP3-O7
- APP3-O8
- APP3-O9
- APP3-O10
- APP3-O12
- APP3-O13
- APP3-O14
- APP3-O15

#### Lessons

1. **Threat-to-Test Matrix instead of Repeating Security Theory** — Choose concrete broken object/property/function authorization, authentication, SQL/schema injection, SSRF, unsafe upstream and resource-exhaustion risks based on the actual app; use prior modules' mitigations rather than reteach their introductory examples.

2. **Pure Domain, Fastify Inject and Real HTTP Layers** — Test domain invariants and request hook/schema responses separately from an independently issued local HTTP client and explain what mocks cannot verify.

3. **Real DB Tenant, Concurrency and Idempotency Cases** — Inspect disposable PostgreSQL states under two-client conflict, forbidden property update and duplicate replay, with independent expected rows and no fake repository-only conclusion.

4. **Cookie/CSRF, Input and Response Exposure Regression** — Attempt forged/expired sessions, mass assignment, parser coercion, unsafe response properties and cookie-mode CSRF where the chosen scheme applies; CORS is not server authorization.

5. **SSRF, Dependency and Resource-Budget Probes** — Challenge outbound URL/redirect policy, actual body/page/worker bounds, dependency timeout and package/plugin compatibility using local bounded synthetic traffic.

6. **Independent Old/New API and Background-Work Tests** — Check actual contract versions and error media along with committed-before-notified, duplicate delivery and worker restart paths; do not claim passing injection tests prove the public client.

7. **Request-to-Database Incident Timeline** — Correlate safe synthetic request, principal, DB transaction and job identifiers, reason from observed failure events and state which causal links are uncertain or absent.

8. **Two New Cross-Layer Defects and Causal Repair** — Seed and repair two distinct failures not identical to prior AS2–AS5 exercises, for example schema evolution leaking a private field and a retry/durable-work race; require failing-before/passing-after HTTP and persisted-state evidence.

9. **Risk, Regression and Independent Technical Judgment** — Verify affected auth, consumer, transaction and cleanup cases after repair, disclose untested threats, production limits and actual reviewer-observable results rather than submit a checklist.

*Optional practice — Security/Incident Review:* Fix a selected failure and show failing-before/passing-after evidence in multiple relevant test layers.

### Module 14 — One Integrated Typed Service and Independent Defense

#### Outcomes

- APP3-O1
- APP3-O2
- APP3-O3
- APP3-O4
- APP3-O5
- APP3-O6
- APP3-O7
- APP3-O8
- APP3-O9
- APP3-O10
- APP3-O11
- APP3-O12
- APP3-O13
- APP3-O14
- APP3-O15
- APP3-O16

#### Lessons

1. **One Cumulative Domain and Evidence Contract** — Use the same bounded two-tenant Fastify/TypeScript/Postgres service from APP3-AS1–AS6, name authentic requirements, role policy and public contracts, and link previously accepted judgments instead of creating seven services.

2. **Integrate Identity, Transactions and Durable Recovery** — Verify trusted sessions, exact object/property/tenant authorization, scoped domain invariants, replay/outbox and safe outbound dependencies together without weakening layer contracts.

3. **Independent Clients, Failure and Operating Readiness** — Exercise old/new clients, actual database state, negative security cases, redacted correlation and in-flight shutdown against known local fixtures.

4. **New Bounded Incident, Permission or Data Change** — Reproduce and repair an assessor-supplied unfamiliar route, field, tenant-rule, transaction or worker failure with explicitly tested impacted consumers and prior acceptance cases.

5. **Fresh Local Reproduction and Engineering Defense** — Build/test/start/stop using pinned free local artifacts and disposable data, cite accepted evidence, show targeted new changes and defend framework/domain/Node/PostgreSQL/production boundaries.

## Completion requirements

All **sixteen APP3 outcomes** must be established through
**seven independently decidable summative assessments**.
Use **one evolving local Fastify/TypeScript/PostgreSQL service**:
AS1 proves framework/consumer contracts; AS2 authenticates
and authorizes; AS3 proves real transaction/replay behavior;
AS4 checks independent clients and untrusted dependencies;
AS5 verifies durable work and service failures; AS6 audits
**new cross-layer security/incident defects**; and AS7
integrates the accepted work with an unfamiliar bounded
requirement and independent defense. Previously accepted
evidence may be **referenced** rather than resubmitted.
Seven separate applications and compulsory formative
module checklists are not required.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP3-AS1` — Requirements-to-HTTP Contract and Framework Lifecycle | APP3-O1, APP3-O2, APP3-O3, APP3-O4, APP3-O5, APP3-O11 | Requirements/role/use-case table, typed service and schema source, Fastify/version/lockfile details, route/lifecycle diagram, OpenAPI/examples, consumer test results, before/after defect and architectural explanation |
| `APP3-AS2` — Credential, Object and Tenant Authorization Security Audit | APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O12, APP3-O13, APP3-O14 | Synthetic account/session fixture, role-tenant-method-field access matrix, HTTP negative and positive tests with effective principal and safe status/error outputs, credential-lifecycle observations, data state checks and threat/remaining-risk rationale |
| `APP3-AS3` — Transactional Service Invariant and Idempotent Replay | APP3-O5, APP3-O7, APP3-O8, APP3-O9, APP3-O13, APP3-O14 | Real local PostgreSQL migration/schema fixtures, versioned service/repository source, concurrent request interleaving table, transaction and idempotency policies, before/after state checks, redelivery/outbox or equivalent design evidence and regression tests |
| `APP3-AS4` — Versioned API Contract, Independent Consumer and Dependency Boundary | APP3-O1, APP3-O3, APP3-O4, APP3-O10, APP3-O11, APP3-O13, APP3-O14 | OpenAPI and validation output, old/new consumer source with normal/negative tests, compatibility matrix and migration note, mocked/local upstream failure and SSRF tests, documented problem/error codes and transport-boundary rationale |
| `APP3-AS5` — Background Work, Fault Handling and Operability Drill | APP3-O2, APP3-O8, APP3-O9, APP3-O10, APP3-O12, APP3-O14, APP3-O15 | Job/outbox fixtures, failure timeline and redacted logs, configuration and state machine, tests for retry/duplicate/shutdown/dependency outage, bounded timing/health observations, repair diff and limitations report |
| `APP3-AS6` — Security, Concurrency and Service Incident Regression Review | APP3-O3, APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O8, APP3-O9, APP3-O12, APP3-O13, APP3-O14, APP3-O15 | Independent new cross-layer attack/incident matrix, real failing-before/passing-after HTTP and DB state, targeted layered regression, sanitized causal observations and residual-risk disclosure |
| `APP3-AS7` — Integrated Typed API Service and Independent Engineering Defense | APP3-O1, APP3-O2, APP3-O3, APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O8, APP3-O9, APP3-O10, APP3-O11, APP3-O12, APP3-O13, APP3-O14, APP3-O15, APP3-O16 | One versioned service with pinned local tools and synthetic DB, a references-first AS1–AS6 evidence index, independently reproducible unfamiliar change and regressions, clean checkout and technical defense |

### Shared local execution, integrity and safety boundaries

- Use a documented compatible Node/TypeScript/Fastify/
  PostgreSQL toolchain, driver, schema validator and
  reviewed authentication/session dependencies. Record
  versions, package lockfile and local artifact provenance.
  A maintained framework release must actually be
  compatible with the supported Node baseline.
- Build/test with freely accessible tools and synthetic
  users, tenants and resources. Initial dependency
  provisioning may use a public download; after
  provisioning the project and assessments must be
  reproducible offline with documented local artifacts.
  No production credentials, proprietary vendor,
  public deployment, paid SaaS, microservice mesh,
  managed queue or APP20 React client is required.
- Use a disposable local PostgreSQL database and loopback
  HTTP endpoints, not a shared or production server.
  Reviewable local role/session and test credentials
  must be synthetic and never confused with real secrets.
- Check required HTTP methods, statuses, media types,
  input bounds, response schemas, consistent problem
  errors and documented compatibility, using **actual
  independent request execution**. A TypeScript type
  or compiled request schema is not permission to
  skip application-domain authorization.
- Authenticate a verified principal before using
  their identity and derive permitted tenant/action/
  property access from authoritative server-held
  information. Test guessed IDs, cross-tenant lists
  and writes, role escalation and forbidden field
  reads/writes. A client-chosen tenant context,
  HTTP CORS policy or RLS bypass-role result cannot
  substitute for correct authorization.
- A local session may use controlled loopback HTTP,
  but do not claim deployment-grade cookie or
  credential protections without an actual TLS,
  CSRF, persistence, rotation and privilege model.
  Use established cryptographic and session
  mechanisms, never a hand-written token/signature
  primitive or plaintext reusable password storage.
- Transaction and idempotency evidence must inspect
  real concurrent PostgreSQL state and the observed
  HTTP outcomes. A simulation of an outbox/worker
  must state its durability, duplicate and retry
  guarantees; exactly-once external execution is
  not presumed. Recover safely from uncertain results.
- Do not run injection, SSRF or exhaustion tests
  against real external systems. Use synthetic
  requests, local allowlisted addresses, bounded
  test workloads and deliberately rejected redirect
  targets. Never log or publish raw secrets, sessions,
  SQL internals or sensitive request data.
- Measure only what the declared local environment
  supports: response timings, logs, tests, retry
  attempts, health and shutdown observations.
  A single local test cannot establish general
  capacity, production uptime or security compliance.
- An independent reviewer may supply an unfamiliar
  bounded requirement, denied access scenario or
  controlled service incident aligned with published
  outcomes. A written, recorded, live or equivalent
  accessible defense must use the same public
  evaluation criteria, not a hidden proprietary
  toolchain or additional frontend course.

### Required summative assessments

- **APP3-AS1** (required requirements-to-http contract and framework lifecycle)
  - Outcomes: APP3-O1, APP3-O2, APP3-O3, APP3-O4, APP3-O5, APP3-O11
  - Work: Begin **one cumulative Fastify/TypeScript service** from a synthetic user/tenant/consumer brief, with accepted and denied business states, free pinned toolchain and an independent local HTTP consumer. Implement a typed route/plugin/schema boundary and public response contract. Reproduce and repair a real plugin encapsulation or hook-order defect; verify actual OpenAPI examples, no-body/errors and independently testable domain logic without depending on Fastify.
  - Criteria: An independent issued request matches declared methods, media/status, public response shape and negative cases; neither TypeScript types nor request schema shape checks are misrepresented as domain authorization. The plugin/hook fault is reproduced and corrected under the recorded Fastify release, with no double reply or internal-property leakage. Requirements trace to evidence rather than invented stakeholder research.
  - Evidence: Requirements/role/use-case table, typed service and schema source, Fastify/version/lockfile details, route/lifecycle diagram, OpenAPI/examples, consumer test results, before/after defect and architectural explanation.

- **APP3-AS2** (required credential, object and tenant authorization security audit)
  - Outcomes: APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O12, APP3-O13, APP3-O14
  - Work: Extend **the same service** with reviewed credential/session verification using fabricated users, expiry and revocation. Establish trusted principals and authoritative tenant membership; enforce action, object, **read/write property**, and tenant authorization over two synthetic tenants with contrasting roles. Test forged/expired/revoked sessions, guessed nested IDs, cross-tenant list/detail/create/update/delete, unauthorized role/owner field assignment and unsafe response projection using independent HTTP clients and real persistent state.
  - Criteria: Authentication is independently verified before using a principal, and authorization is checked for every required object/action/property, including denial paths and privileged exemptions. Each rejected mutation leaves authoritative database state unchanged and private fields never appear in public serialized results. A caller-chosen header or tenant label, client guard, CORS setting or RLS bypass-role test does not qualify as proof; local credential, cookie/CSRF and public TLS limitations are explicit.
  - Evidence: Synthetic account/session fixture, role-tenant-method-field access matrix, HTTP negative and positive tests with effective principal and safe status/error outputs, credential-lifecycle observations, data state checks and threat/remaining-risk rationale.

- **APP3-AS3** (required transactional service invariant and idempotent replay)
  - Outcomes: APP3-O5, APP3-O7, APP3-O8, APP3-O9, APP3-O13, APP3-O14
  - Work: Extend **the same source** with a real local PostgreSQL multi-write transaction and correct connection scope. Coordinate **two actual API requests** through independent DB sessions, reproducing stale write/invariant contention and verifying a corrected database/HTTP result. Implement tenant/principal/operation-scoped idempotency with a request fingerprint and duplicate-in-flight policy. Inject two same-key requests, conflicting payloads, a **post-commit lost response**, a bounded retry and a real transactionally durable outbox/worker intent or rigorously justified equivalent. Inspect replay, redelivery and restart behavior without promising exactly-once remote effects.
  - Criteria: Real DB rows and the two-client trace show that conflict and rollback preserve the invariant. All related work uses an owned scoped transaction connection; safe full-unit serialization retries cannot repeat non-idempotent external effects. Concurrent replay under the same key is handled deterministically, mismatched payloads are rejected, post-commit uncertainty is reconciled, and durable work is demonstrably restart-observable under its declared assumptions. At-least-once dispatch is not mislabeled exactly-once.
  - Evidence: Real local PostgreSQL migration/schema fixtures, versioned service/repository source, concurrent request interleaving table, transaction and idempotency policies, before/after state checks, redelivery/outbox or equivalent design evidence and regression tests.

- **APP3-AS4** (required versioned api contract, independent consumer and dependency boundary)
  - Outcomes: APP3-O1, APP3-O3, APP3-O4, APP3-O10, APP3-O11, APP3-O13, APP3-O14
  - Work: Publish executable OpenAPI and real examples for the **evolving service**, then apply one versioned field/status/operation change and run **independent old and revised clients** with normal, forbidden, invalid, conditional and pagination cases. Add a synthetic local outbound dependency with fixed/allowlisted destination, checked responses and actual byte/time budgets. Inject timeout, 429/5xx, malformed upstream shape, rejected transport and disallowed redirect or target pivot; verify bounded retries. If declaring RFC 9457 problems, inspect required shape and `application/problem+json` rather than label arbitrary JSON conformant.
  - Criteria: Machine-readable docs and actual serialized HTTP agree on methods, statuses, auth, public fields, preconditions and error media. The old/new test exposes a real compatibility issue that is repaired or deliberately declared breaking. Untrusted upstream payload, location, redirect and headers are controlled; response size/deadline and side-effect retry eligibility are bounded, secrets never leak and an allowlist based only on URL prefix is not accepted as SSRF protection.
  - Evidence: OpenAPI and validation output, old/new consumer source with normal/negative tests, compatibility matrix and migration note, mocked/local upstream failure and SSRF tests, documented problem/error codes and transport-boundary rationale.

- **APP3-AS5** (required background work, fault handling and operability drill)
  - Outcomes: APP3-O2, APP3-O8, APP3-O9, APP3-O10, APP3-O12, APP3-O14, APP3-O15
  - Work: Extend **the same service** with a real durable/outbox or appropriately qualified background workflow, safe request/job correlation, honest health/readiness, bounded outgoing timeouts and in-flight shutdown. Inject a database-committed but dependency-failed operation, duplicate/redelivered job, lost acknowledgement, exhausted retry, missing startup dependency and shutdown with an active HTTP request and queued work. Reproduce a specific lifecycle/failure defect and use sanitized HTTP/DB/job observations to test a causal repair and restart.
  - Criteria: Post-commit failures preserve committed DB truth and pending/recoverable work according to an explicit policy; in-process tasks are not misrepresented as durable, nor at-least-once work as exactly-once. Invalid settings fail before unsafe listen, readiness reflects observed dependencies, bounded drain/stop owns HTTP, DB and worker resources, and correlation avoids personal/secret payloads. A local timeline supports the proposed cause and corrected regression without fictitious production-availability claims.
  - Evidence: Job/outbox fixtures, failure timeline and redacted logs, configuration and state machine, tests for retry/duplicate/shutdown/dependency outage, bounded timing/health observations, repair diff and limitations report.

- **APP3-AS6** (required security, concurrency and service incident regression review)
  - Outcomes: APP3-O3, APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O8, APP3-O9, APP3-O12, APP3-O13, APP3-O14, APP3-O15
  - Work: Perform an **independent adversarial cross-layer audit** of the already assessed service rather than copying AS2/AS3/AS4 results. Select **two newly seeded distinct defects** that arise from interaction between mechanisms—for example a response-property exposure after an API schema evolution and an inconsistent transaction/idempotency/outbox retry after dependency failure. Use current OWASP API object/property/function authorization and relevant injection, CSRF/cookie, SSRF, unsafe upstream and resource-exhaustion risks to build a targeted matrix. Reproduce failure through independent HTTP requests and **real PostgreSQL state** where applicable, repair both root causes and run relevant domain, Fastify, contract, DB and fault regressions.
  - Criteria: At least two **new cross-layer failure cases**, not simply earlier successful AS2–AS5 traces, have failing-before/passing-after evidence and checked authoritative state. Repaired security boundaries prevent forbidden object/property exposure, invalid work and unsafe retries without breaking legitimate consumers; reproducible diagnostics distinguish facts from hypotheses and missing telemetry. A single green count, generic OWASP checklist or local scripted test is not claimed to certify production security.
  - Evidence: Threat-and-test matrix, synthetic fixtures, observed exploit/failure steps, layered tests and database-state comparisons, sanitized causal incident notes, corrected code, compatibility checks and remaining-risk statement.

- **APP3-AS7** (required integrated typed api service and independent engineering defense)
  - Outcomes: APP3-O1, APP3-O2, APP3-O3, APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O8, APP3-O9, APP3-O10, APP3-O11, APP3-O12, APP3-O13, APP3-O14, APP3-O15, APP3-O16
  - Work: Deliver **one coherent cumulative Fastify/TypeScript/PostgreSQL service** integrating prior approved AS1–AS6 contracts and evidence. Show authentic sessions, server-side tenant/object/property policy, actual concurrent transaction/replay behavior, bounded outbound dependencies, versioned clients, correlated fault observations and ready/drain/stop conditions. **Reference earlier accepted** tests and artifacts instead of rebuilding seven apps or duplicating reports. Respond to an unfamiliar but bounded permission, data invariant, API change or incident, reproduce and correct it, retest impacted layers and defend the framework/domain/Node/PostgreSQL distinctions from a clean synthetic local checkout.
  - Criteria: A reviewer can reproduce the free local service, actual old/new clients, disposable Postgres state, denied access, concurrency/replay, real failure/shutdown, safe response and unfamiliar change. Each material fault has observed before/after correction, and **AS7 cannot excuse missing or failed AS1–AS6 evidence**. Unsafe session data, tenant/property exposure, duplicate business effects, unresolved resource leaks or irreproducible required source block passing. No untested exactly-once, global security or production uptime guarantee is asserted.
  - Evidence: One versioned local source/fixture bundle with pinned dependency/DB prerequisites and clean run/test/stop steps; an **outcome-to-accepted-AS1–AS6 evidence index** instead of copied logs; independent changed API/security/transaction/incident observations, unfamiliar change diff and targeted regressions, material caveats and a reviewable written, recorded or equivalent technical defense.

### Completion decision and revision safety

Completion requires an inspectable passing decision for
`APP3-AS1` through `APP3-AS7` with evidence covering
`APP3-O1` through `APP3-O16`. Where one evolving
service is reused, assessors must verify **new evidence**
for security, concurrency, compatibility and incident
claims rather than merely reuse an old green test log.
Missing access denial, unsafe credentials, corrupted
business state, irreversible unacknowledged side effects,
misleading response contracts and unreproducible
source must be corrected before a passing decision.

Review records must preserve the actual course and OEE
revision, outcome/assessment IDs, source commit or
artifact references, environment, negative-path results,
technical defense, observations, limitations and
decision provenance in accordance with
[OEE Evidence Rules](../../spec/evidence-rules.md).

APP3 remains an OEE `v0.2.0` **draft** with
the established APP19/APP21/APP4 direct prerequisites
and seven independent summative decisions. The earlier
APP1 prerequisite change is already reflected in the
published catalog, which also includes APP5–APP9 and
the electives. This editorial reassessment does not
promote the course to `tested` or `verified`, change
downstream course acceptance, or retroactively certify
earlier learner work. Historical source/spec decisions
and OEE Workspace/content/0xNAND revision pins require
explicit review rather than automatic substitution.

### Public non-mandatory study references

These publicly accessible technical references may
be consulted for mechanism and version checks, but
all required tasks and criteria appear above.

- [Fastify TypeScript reference](https://fastify.dev/docs/latest/Reference/TypeScript/)
  and [Fastify Validation and Serialization](https://fastify.dev/docs/latest/Reference/Validation-and-Serialization/)
  for type-safe route context, reviewed schemas, request
  validation and response serialization boundaries.
- [Fastify lifecycle](https://fastify.dev/docs/latest/Reference/Lifecycle/)
  and [plugins](https://fastify.dev/docs/latest/Reference/Plugins/)
  for specific hook sequencing and encapsulation semantics.
- [OWASP API Security Top 10](https://owasp.org/API-Security/)
  and [API Security Project](https://owasp.org/projects/api-security-project)
  for object, property/function authorization, authentication,
  unsafe consumption and resource exhaustion risks.
- [RFC 9457 problem details](https://www.rfc-editor.org/rfc/rfc9457.html)
  for stable structured HTTP error document semantics.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
  for portable API definition and consumer examples.
- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
  and [row-level security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
  for the actual persistence and tenant defense model.
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
  and [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
  for safe credential/session and verification trade-offs.
