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

This revises the legacy APP3 course while retaining its identity
and important content. Direct prerequisites are deliberately
**APP19, APP21 and APP4**, not APP1. [APP19](APP19.md) already
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

### Module 1 — Service Requirements, Boundaries and Reference Environment

#### Outcomes

- APP3-O1
- APP3-O2
- APP3-O5
- APP3-O16

#### Lessons

1. **Backend Framework Scope and Verifiable API Contracts** — Situate API services between browser clients, domain decisions, persistent records and external dependencies; identify what APP19, APP21 and APP4 already teach; derive actors, user actions, resources, invariants, observable successes, failures, privacy assumptions and consumption requirements from a synthetic stakeholder brief.

2. **HTTP and Domain Terminology** — Review rather than reteach APP21 request/response handling; distinguish transport semantics, application policy, authorization and database state.

3. **Reference Stack and Version Baseline** — Record maintained Node, TypeScript, Fastify and PostgreSQL versions plus free locally available dependencies, scripts, lockfile and unprivileged test setup.

4. **Independent Consumer and Controlled Fixture** — Provide a local API test client and synthetic users/tenants; separate initial free dependency provisioning from repeatable offline assessment execution.

5. **Threat and Trust Inventory** — List untrusted URL/path/body/header/cookie inputs, validated principals, server-side secrets, database roles and which component owns each check.

6. **Requirements Traceability Matrix** — Map example requirements to API operations, errors, security policies and tests, marking unsupported or unknown claims honestly.

*Optional practice — Bounded API Design Review:* Inspect a tempting overfeatured service brief, choose a coherent vertical slice and document deferred needs without omitting required negative cases.

### Module 2 — Fastify Architecture, Plugins and Request Lifecycle

#### Outcomes

- APP3-O2
- APP3-O4
- APP3-O5
- APP3-O12

#### Lessons

1. **Framework Value beyond Node HTTP** — Compare APP21 raw node:http responsibilities with framework routing, validation, serialization, plugin composition and lifecycle hooks.

2. **Create the Typed Reference Service** — Configure a modular Fastify instance separately from process listen/start, use a supported TypeScript setup and verify a local inject/integration request.

3. **Route Registration and Method Boundaries** — Implement typed route handlers for explicit methods and paths, handling unsupported operations with deliberate status/Allow policy where applicable.

4. **Fastify Lifecycle Sequence** — Trace route matching, parsing, validation, preHandler authentication/authorization, handler, serialization and onResponse behavior using the installed release docs.

5. **Plugins, Encapsulation and Scope** — Demonstrate local plugin context, decorator scope and registration order; diagnose a capability unintentionally exposed or unavailable to a child plugin.

6. **Hooks and Middleware Responsibilities** — Select hooks for cross-cutting work without mistaking a framework's lifecycle for all Express-style middleware or bypassing route security.

7. **Errors and Reply Ownership** — Handle thrown/rejected errors, response-sent state, duplicate replies and early failures without assuming every error hook sees the same normalized payload.

8. **Boot, Close and Test Isolation** — Make factory/create, ready and close operations explicit so integration tests do not open unmanaged sockets or leave active database handles.

*Optional practice — Plugin Boundary Fault:* Repair an encapsulation or hook-order defect and explain it with a request trace rather than a vocabulary-only answer.

### Module 3 — HTTP Resource and Consumer Contract Design

#### Outcomes

- APP3-O1
- APP3-O3
- APP3-O4
- APP3-O11

#### Lessons

1. **Resource Identity and HTTP Methods** — Design clear paths and stable identifiers; compare GET, HEAD, POST, PUT, PATCH and DELETE by documented behavior, safe/idempotent semantics and method-specific preconditions.

2. **Statuses and Response Semantics** — Use correct success, accepted, no-content, validation, missing, forbidden, unauthorized, conflict and dependency-failure responses without returning generic success for every result.

3. **Content Negotiation and Encoding** — Validate expected Content-Type and Accept choices, structured JSON bodies and correct no-body responses, avoiding undocumented serialization assumptions.

4. **Filters, Pagination and Order** — Publish bounds, stable cursors or offset/limit rules, consistent ordering, filter allowlists and total-count limitations where applicable.

5. **Conditional Reads and Write Preconditions** — Introduce ETag/If-Match or revision-token alternatives for a concrete stale-write or cache-use scenario; do not falsely promise automatic concurrency safety.

6. **Error and Retry Contracts** — Design stable error codes and expose safe details using a documented problem-details shape or justified project alternative; distinguish machine action from internal diagnostics.

7. **API Examples and Negative Paths** — Define valid, missing, malformed, conflicting and unauthorized example requests for an independently runnable consumer.

8. **API Contract Change Review** — Change a field/operation while marking affected clients, compatibility expectations, status semantics and required migration evidence.

*Optional practice — HTTP Ambiguity Audit:* Find an underspecified DELETE, pagination tie or invalid method response, then revise the contract and independent tests.

### Module 4 — Runtime Schemas, Validation and Safe Error Handling

#### Outcomes

- APP3-O3
- APP3-O4
- APP3-O13

#### Lessons

1. **Untrusted Input Is Not a TypeScript Type** — Accept external input as unknown, distinguish runtime schema validation from static inference and verify that a cast cannot enforce a trust boundary.

2. **Fastify Request Schema Surfaces** — Declare supported schema rules for params, query, body and headers, with explicit additional-field and coercion policies on the pinned framework release.

3. **Response Serialization Contracts** — Define public response schemas to prevent accidental internal-property disclosure and test actual serialized output, not just declared TypeScript interfaces.

4. **Schema Compilation and Security** — Treat JSON Schemas as reviewed application code; never compile arbitrary attacker-supplied schemas or confuse generated validators with a safely sandboxed interpreter.

5. **Synchronous Shape versus Async Domain Checks** — Perform shape validation before authorization/domain/database checks; keep database/network lookups outside inappropriate synchronous validator execution.

6. **Canonical Inputs and Limits** — Check media type, body bytes, accepted properties, Unicode and numeric ranges, identifiers and pagination bounds before applying domain rules.

7. **Structured Problem Details** — Use stable error taxonomy, status alignment and safe RFC 9457-like problem responses when suitable; never leak stack traces, SQL text or personal data.

8. **Unexpected and Duplicate Failure Paths** — Inject malformed JSON, validation failure, thrown domain error and serialization failure; confirm exactly one deliberate client response and preserved internal cause.

*Optional practice — Schema/Type Drift:* Produce a counterexample where a declared inferred type and actual validator behavior differ, then fix both evidence and code.

### Module 5 — Domain Rules, Application Services and Dependency Boundaries

#### Outcomes

- APP3-O1
- APP3-O5
- APP3-O8
- APP3-O14

#### Lessons

1. **Domain versus HTTP Responsibilities** — Keep business invariants independent of route handlers and status codes; define a narrow application operation for a transaction-like use case.

2. **Domain Entities, Value Objects and Invariants** — Choose explicit identity/quantity/state representations and test invariants without importing Fastify or a database adapter.

3. **Application Orchestration** — Coordinate authorization, domain decisions and repositories through an application use-case boundary without scattering rule checks among hooks.

4. **Adapter Interfaces and Composition Roots** — Provide testable persistence/clock/identity/external-service ports, wire production-like local implementations and state ownership clearly.

5. **Error Translation across Layers** — Distinguish domain conflicts, invalid commands, unauthorized intent and infrastructure failures before mapping to HTTP responses.

6. **Test Doubles and False Confidence** — Use simple fakes for domain logic and real database or HTTP integration tests for assumptions that mocks cannot prove.

7. **Refactor a Coupled Route** — Move a rule-heavy handler into domain/application/adapters without changing supported status/error/transaction behavior.

*Optional practice — Refactor Review:* Add a new business constraint and demonstrate one place where the rule belongs plus a regression that catches bypass.

### Module 6 — Authentication, Sessions and Credential Safety

#### Outcomes

- APP3-O6
- APP3-O7
- APP3-O12
- APP3-O13

#### Lessons

1. **Authentication versus Authorization** — Distinguish identity proof from permission to access a specific resource and from data-layer role enforcement.

2. **Identity and Session Trust Model** — Choose a bounded local credential/session design, explain principal provenance, login/logout lifecycle, expiry and token/session compromise assumptions.

3. **Password Handling with Established Primitives** — Explain salt, slow password KDF, parameter choice, secure entropy and safe verification; use a supported reviewed implementation, not a homemade password algorithm.

4. **Cookie and Token Trade-offs** — Distinguish opaque session identifiers and signed/verified bearer tokens, secure cookie attributes, revocation limitations and storage risks.

5. **Local HTTPS and Deployment Caveat** — Test on controlled loopback with synthetic credentials and explain Secure/HttpOnly/SameSite and TLS requirements for actual public deployment.

6. **Credential and Session Leakage** — Keep secret values out of URLs/logs/errors; inspect session fixation, rotation and deliberate logout/expiry failure behavior.

7. **Brute-Force and Enumeration Mitigation** — Use proportionate login error behavior and local attempt limits while disclosing limitations of a single-process demo.

8. **Auth Hook and Principal Injection** — Verify session once at a carefully placed boundary, construct a trusted principal context and ensure route-level authorization still executes.

*Optional practice — Authentication Failure:* Inject expired/revoked or forged session data and show denial plus appropriately sanitized diagnostic evidence.

### Module 7 — Authorization, Tenant Isolation and Property-Level Safety

#### Outcomes

- APP3-O5
- APP3-O7
- APP3-O8
- APP3-O13
- APP3-O14

#### Lessons

1. **Authority to Act, Object and Field** — Separate permission for a route/action, a particular object ID and each returned/writable property; refer to relevant OWASP object/property/function risk classes.

2. **Policy Matrix by Role, Tenant and Operation** — Publish owner/admin/member/guest access across two synthetic tenants, methods and resources, including denied updates and hidden fields.

3. **Trusted Tenant Resolution** — Bind tenant scope to authenticated claims plus authoritative database membership, never trust arbitrary client-supplied tenant IDs as proof of permission.

4. **Repository and SQL Scope** — Apply ownership checks at a trustworthy data-access boundary and use database permissions/RLS as defense in depth where configured.

5. **Prevent IDOR and BOLA** — Test guessed identifiers, cross-tenant list/detail reads, nested resource writes and enumeration-resistant error policies.

6. **Prevent Mass Assignment and Data Exposure** — Allowlist writable fields and project response data; show why accepting `role: admin` or returning password/session columns violates property-level policy.

7. **Privilege Escalation via Background Work** — Preserve principal/tenant authority in queued operations, re-evaluate permissions or fail safely when context expires.

8. **Global Admin and Service Accounts** — Separate deliberately elevated maintenance operations from ordinary tenant actors and verify audit boundaries and exemptions.

*Optional practice — Cross-Tenant Attack Fixture:* Reproduce a local unauthorized request that initially succeeds, then fix the policy and verify all negative matrix entries.

### Module 8 — PostgreSQL Integration, Transactions and Concurrency

#### Outcomes

- APP3-O5
- APP3-O8
- APP3-O9
- APP3-O14

#### Lessons

1. **From APP4 SQL to Service Persistence** — Reuse APP4's SQL/constraints/isolation/migrations knowledge to implement application-specific repositories, without re-teaching relational normalization.

2. **Database Adapter and Parameter Binding** — Use a compatible pre-provisioned PostgreSQL driver with bound values, proper connection lifecycle and validated dynamic identifier allowlists.

3. **Service Transaction Ownership** — Define one application operation's transaction begin/commit/rollback and ensure all participating writes use the correct scoped connection.

4. **Atomic Domain Change** — Demonstrate two related writes and an invariant protected by constraints or transactionally checked state under malformed and failed cases.

5. **Revision-Controlled Concurrent Writes** — Use a version column or conditional update to reject stale writes and map conflicts to an independently specified HTTP response; run two controlled API requests against real local PostgreSQL sessions, inspect the interleaving and verify no silent lost update or double-spend.

6. **Isolation and Full Transaction Retry** — Choose PostgreSQL isolation/locking appropriately, handle recognized serialization/deadlock failures with bounded retry of the complete unit, and avoid retrying non-idempotent side effects.

7. **Schema Migrations with Two Client Versions** — Apply a staged schema change with existing API consumers, preserve compatibility claims and keep migration ownership distinct from handler code.

8. **Resource and Cleanup Boundaries** — Release clients/connections on errors, aborts and shutdown without promising all interrupted DB work is automatically canceled.

*Optional practice — Transaction Leak:* Repair a repository method that uses a different connection mid-transaction and prove rollback/commit integrity with real database evidence.

### Module 9 — Idempotency, Asynchronous Work and Partial Failure

#### Outcomes

- APP3-O8
- APP3-O9
- APP3-O10
- APP3-O13

#### Lessons

1. **HTTP Method Idempotence versus Business Deduplication** — Explain why PUT/DELETE semantics do not automatically deduplicate all effects, and why POST requests need explicit replay policy when a use case demands it.

2. **Idempotency-Key Storage Contract** — Define key scope by principal/tenant/operation, request fingerprint, expiration, duplicate-in-flight behavior and durable result interpretation.

3. **Atomic Dedup and Business Change** — Record an idempotency reservation and associated domain mutation transactionally where the chosen design permits; test repeated and conflicting payloads.

4. **Background Task Lifetime** — Contrast Node in-process queues with durable database-backed work, crashes and restart behavior; never label an ephemeral promise queue a durable job system.

5. **Outbox and Reliable Dispatch Boundary** — Introduce a small transactionally recorded outbox entry and idempotent worker consumer or an equivalent justified durable design; explain at-least-once rather than exactly-once guarantees.

6. **Retry, Backoff and Dead Letters** — Classify transient and permanent failures, bounded retry/attempt limits, poison work and manual replay constraints.

7. **Partial Failures across Database and External Calls** — Trace a committed DB change followed by a failed notification and defend the chosen recovery or compensation path; avoid holding a transaction open during arbitrary network I/O.

8. **Cancellation, Deadlines and Service Shutdown** — Own timers/workers/abort signals and state what work remains pending or can be replayed after a service stop.

*Optional practice — Duplicate Request Drill:* Replay concurrent identical and conflicting requests and a simulated dispatcher restart, verifying each business invariant and documented status/result.

### Module 10 — Outbound Services, Resilience and Dependency Trust

#### Outcomes

- APP3-O4
- APP3-O9
- APP3-O10
- APP3-O12
- APP3-O13

#### Lessons

1. **Outbound API as Untrusted Dependency** — Define a typed adapter for a local synthetic external service with clear data and error shapes, version expectations and failure scope.

2. **Target URL and SSRF Controls** — Reject client-controlled internal URLs/hosts/protocols; use fixed or allowlisted outbound destinations and explain DNS/redirect and metadata-service risks.

3. **Response Size, Timeouts and Abort** — Bound local test traffic, enforce actual bytes and declared deadlines, and distinguish an aborted client request from proven cancellation of a remote operation.

4. **Dependency Errors and Information Leakage** — Classify 4xx/5xx, network failure, invalid JSON, latency and contradictory data; ensure client responses do not expose upstream credentials or internals.

5. **Retry Eligibility and Budgets** — Choose safe idempotent retries and bounded attempt limits; avoid amplifying overloaded services or repeating uncertain mutations blindly.

6. **Overload and Circuit-Breaker Reasoning** — Explain what a circuit breaker/bulkhead can and cannot guarantee, with optional local fault injection rather than mandatory infrastructure complexity.

7. **Consumer of Third-Party Data** — Validate external response contracts, restrict unexpected properties and apply least authority rather than trusting a well-known partner API.

*Optional practice — External Failure:* Simulate malformed responses, slow dependency, redirect to an unapproved target or repeated 503s and verify controlled behavior and clean logs.

### Module 11 — API Documentation, Contract Evolution and Compatibility

#### Outcomes

- APP3-O1
- APP3-O3
- APP3-O4
- APP3-O11
- APP3-O14

#### Lessons

1. **OpenAPI as a Consumer Interface** — Publish machine-readable operations, statuses, media types, security schemes and representative examples with a free local validation tool.

2. **Schema-to-Implementation Alignment** — Choose one verified source-of-truth strategy for request/response schemas, documenting limitations of code-first and schema-first generation.

3. **Compatibility of Requests and Responses** — Analyze adding an optional field, changing required fields or response types, enum evolution and field removal for actual existing consumers.

4. **Semantic Error Compatibility** — Retain stable machine-readable problem codes and status contracts or explicitly describe a breaking change and migration path.

5. **Authentication and Tenant Contract Documentation** — Document protected operations and authorization outcomes without exposing session internals or claiming docs alone enforce policy.

6. **Pagination and Conditional Consumer Tests** — Provide an old and new client for a changed listing/query, including cursor/ordering and conflict response handling.

7. **Deprecation and Versioning Strategy** — Choose endpoint/representation versioning or a compatible evolution approach and publish intended support/rejection windows without assuming perpetual compatibility.

8. **Local Contract Verification** — Compare documented examples against actual independently issued HTTP requests and a schema/contract checker, including malformed/forbidden cases.

*Optional practice — API Revision Review:* Apply a bounded requirements change and identify one breaking consumer consequence caught by a failing test.

### Module 12 — Configuration, Health, Lifecycle and Observability

#### Outcomes

- APP3-O2
- APP3-O8
- APP3-O12
- APP3-O15

#### Lessons

1. **Configuration before Listening** — Check known server settings, database connection targets, secrets and safe local defaults before exposing a socket.

2. **Readiness, Liveness and Dependency States** — Define what a local /health and /ready check actually observes and what a green response cannot guarantee.

3. **Structured Request Correlation** — Generate or validate bounded request IDs, record a trace through route, application, database and job paths without logging raw tokens/bodies.

4. **Logs, Metrics and Traces** — Select a small request/error/latency/dependency metric set and show how structured logs and traces can point to—but not prove—a root cause.

5. **Privacy and Sampling Boundaries** — Redact or avoid personally identifying data and credentials, bound log volume and disclose missing trace spans and synthetic observations.

6. **Framework Shutdown and Resource Cleanup** — Stop new requests, drain bounded in-flight work and release database pools, timers and local dispatchers under the recorded Node/Fastify baseline.

7. **Configuration and Dependency Failure Injection** — Test a missing secret/test DB, pool exhaustion or unavailable local dependency and prove startup/readiness/failure policy.

8. **Local Operational Troubleshooting** — Read an incident timeline and identify request IDs, retries, database conflicts and affected endpoints without inventing unavailable telemetry.

*Optional practice — Health and Shutdown Audit:* Find a green-but-broken readiness check or connection leak and verify a corrected bounded test.

### Module 13 — API Security Engineering and Abuse Cases

#### Outcomes

- APP3-O4
- APP3-O6
- APP3-O7
- APP3-O10
- APP3-O13
- APP3-O14

#### Lessons

1. **Risk-Led API Threat Modeling** — Map actors, entry points, assets, resource ownership and misuse paths to representative current OWASP API Security categories.

2. **Broken Object, Property and Function Authorization** — Drive negative tests of role elevation, tenant/object ID guessing, extra writable fields and leaking responses, distinguishing authentication from each access decision.

3. **SQL and Structured Input Injection** — Use bound query values, allowlisted identifiers and reviewed schema construction; demonstrate local injection failures without attacking external systems.

4. **CORS, Cookies and CSRF** — Explain that CORS constrains browsers rather than authorizes API callers, and design local CSRF and cookie-policy tests appropriate to the chosen authentication mode.

5. **Resource Consumption and Abuse Boundaries** — Enforce body, pagination, concurrency, login and background job limits with meaningful errors; avoid claiming a single-process rate limiter protects a distributed service.

6. **Response Data and API Inventory** — Check unexpected verbose errors, overbroad serialization, undocumented endpoints, deprecated versions and secret-bearing logs.

7. **Third-Party Package and Supply-Chain Review** — Inspect lockfile provenance, framework/plugin compatibility and unsafe install scripts; record accepted risk and update/rollback policy.

8. **Security Regression and Limits** — Maintain a published attack/defense matrix for the local service and clearly distinguish verified cases from production pentest or external certification.

*Optional practice — Authorization Bypass Repair:* Inject two synthetic security defects and prove remediation with independent HTTP and persistence evidence.

### Module 14 — Testing, Contract Verification and Incident Investigation

#### Outcomes

- APP3-O3
- APP3-O4
- APP3-O5
- APP3-O7
- APP3-O8
- APP3-O9
- APP3-O11
- APP3-O14
- APP3-O15

#### Lessons

1. **Pure Domain Unit Tests** — Verify rule invariants with representative normal, invalid and boundary inputs without a running network service.

2. **Fastify Injection and HTTP Integration** — Exercise real request lifecycle, validation/hooks/auth/error serialization and response status through an isolated Fastify app factory.

3. **PostgreSQL Integration Fixtures** — Use disposable local DB/schema, reset data safely and test constraints, rollback and transaction connection scope against the real driver.

4. **Auth and Tenant Security Matrix** — Cover invalid/expired sessions, cross-tenant list/detail/write, forbidden properties, role changes and server-side principal derivation.

5. **Concurrency and Replay Tests** — Trigger two-client data races, duplicate idempotency keys, DB serialization conflicts and queued-job redelivery with deterministic coordination.

6. **Contract and Consumer Tests** — Use independent HTTP clients and schema checking to distinguish framework-handler success from actual published API compatibility.

7. **Fault Injection and Cleanup Tests** — Inject dependency timeouts, malformed remote data, crashes in a local dispatcher, invalid configuration and interrupted requests.

8. **Service Incident Timeline** — Build an evidence-based request/dependency log timeline, distinguish symptom/root cause and propose a testable fix and a bounded recovery procedure.

9. **Reproducibility and Review Integrity** — Start from pinned local artifacts, run tests on unprivileged loopback with synthetic data, disclose flaky timings and avoid private or invented measurements.

*Optional practice — Security/Incident Review:* Fix a selected failure and show failing-before/passing-after evidence in multiple relevant test layers.

### Module 15 — Integrated Typed API Service and Independent Defense

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

1. **Choose a Small Multi-Tenant Domain** — Select fictional reservations, inventory, document access or similar product with genuine ownership and transaction invariants, not excessive microservices.

2. **Publish Requirements, Roles and API Contract** — Define synthetic users/tenants, role-action-property matrix, domain transitions, API schemas, error taxonomy and independent consumer cases.

3. **Build the Framework and Domain Boundaries** — Wire versioned Fastify/TypeScript routes, validated schema and serialization, service/domain interfaces and PostgreSQL adapters.

4. **Implement Real Local Identity and Authorization** — Demonstrate a credible local authentication/session boundary, ownership checks on every relevant access, and denial of unsafe properties or actions.

5. **Enforce Transactions and Replay Behavior** — Implement one conflicting concurrent operation plus idempotency/async work that remains truthful under duplicate or partial failure.

6. **Verify External Failures and Safe Responses** — Simulate outbound delay/bad response, missing DB or job failure and confirm bounded retry, redacted problem responses and correct recovery.

7. **Publish and Compare API Versions** — Generate/check a portable OpenAPI contract and validate an independent old/new consumer under one changed field or status condition.

8. **Demonstrate Operability and Threat Mitigation** — Run startup/readiness/shutdown checks, correlate an injected incident and execute cross-tenant/resource-exhaustion negative tests.

9. **Reproduce from a Clean Local Checkout** — Use documented free local artifacts, fake credentials, a disposable database and clients to replay success, errors, concurrency, job and cleanup evidence.

10. **Unfamiliar Change and Technical Defense** — Respond to a new permission, route rule or data invariant; assess impact across layers, implement, retest and defend portable API versus framework-specific decisions.

## Completion requirements

**All sixteen required APP3 outcomes** must be demonstrated
through the **seven required summative assessments** below.
One evolving application can satisfy several assessments
when each required outcome is independently reviewable.
Seven unrelated backend projects are **not** required.
Lesson-level tests, investigations and formative exercises
are preparation, not hidden independent graduation gates.

| Required assessment | Required outcome coverage | Principal evidence |
| --- | --- | --- |
| `APP3-AS1` — Requirements-to-HTTP Contract and Framework Lifecycle | APP3-O1, APP3-O2, APP3-O3, APP3-O4, APP3-O5, APP3-O11 | Requirements/role/use-case table, typed service and schema source, Fastify/version/lockfile details, route/lifecycle diagram, OpenAPI/examples, consumer test results, before/after defect and architectural explanation |
| `APP3-AS2` — Credential, Object and Tenant Authorization Security Audit | APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O12, APP3-O13, APP3-O14 | Synthetic account/session fixture, role-tenant-method-field access matrix, HTTP negative and positive tests with effective principal and safe status/error outputs, credential-lifecycle observations, data state checks and threat/remaining-risk rationale |
| `APP3-AS3` — Transactional Service Invariant and Idempotent Replay | APP3-O5, APP3-O7, APP3-O8, APP3-O9, APP3-O13, APP3-O14 | Real local PostgreSQL migration/schema fixtures, versioned service/repository source, concurrent request interleaving table, transaction and idempotency policies, before/after state checks, redelivery/outbox or equivalent design evidence and regression tests |
| `APP3-AS4` — Versioned API Contract, Independent Consumer and Dependency Boundary | APP3-O1, APP3-O3, APP3-O4, APP3-O10, APP3-O11, APP3-O13, APP3-O14 | OpenAPI and validation output, old/new consumer source with normal/negative tests, compatibility matrix and migration note, mocked/local upstream failure and SSRF tests, documented problem/error codes and transport-boundary rationale |
| `APP3-AS5` — Background Work, Fault Handling and Operability Drill | APP3-O2, APP3-O8, APP3-O9, APP3-O10, APP3-O12, APP3-O14, APP3-O15 | Job/outbox fixtures, failure timeline and redacted logs, configuration and state machine, tests for retry/duplicate/shutdown/dependency outage, bounded timing/health observations, repair diff and limitations report |
| `APP3-AS6` — Security, Concurrency and Service Incident Regression Review | APP3-O3, APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O8, APP3-O9, APP3-O12, APP3-O13, APP3-O14, APP3-O15 | Threat-and-test matrix, synthetic fixtures, observed exploit/failure steps, layered tests and database-state comparisons, sanitized causal incident notes, corrected code, compatibility checks and remaining-risk statement |
| `APP3-AS7` — Integrated Typed API Service and Independent Engineering Defense | APP3-O1, APP3-O2, APP3-O3, APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O8, APP3-O9, APP3-O10, APP3-O11, APP3-O12, APP3-O13, APP3-O14, APP3-O15, APP3-O16 | Versioned service source, manifest/lockfile and local prerequisite recipe, SQL migrations/seeds and disposable DB setup, API/OpenAPI requirements and role matrix, independent clients, negative/normal/concurrency/replay/incident test logs, sanitized request correlation, clean-checkout and repair/change records, and accessible written/recorded/live technical defense |

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
  - Work: From a bounded synthetic domain brief, derive user/consumer requirements and build a small Fastify/TypeScript service slice with route/handler/plugin layering, versioned JSON request/response schemas and stable error categories. Publish an independently runnable HTTP client and an initial OpenAPI description with success, invalid, missing and conflict cases. Demonstrate one lifecycle/hook or encapsulation defect and repair it while preserving a portable contract.
  - Criteria: Route behavior matches documented HTTP method/status/media/serialization semantics, client-facing data is validated at runtime (not only TypeScript) and no unsafe internal field is serialized. The domain rule can be unit tested without a Fastify import. An independent consumer can reproduce normal and malformed requests; the framework lifecycle and plugin scoping are explained against actual traces. Requirements map to verifiable behavior, not invented stakeholder observations.
  - Evidence: Requirements/role/use-case table, typed service and schema source, Fastify/version/lockfile details, route/lifecycle diagram, OpenAPI/examples, consumer test results, before/after defect and architectural explanation.

- **APP3-AS2** (required credential, object and tenant authorization security audit)
  - Outcomes: APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O12, APP3-O13, APP3-O14
  - Work: Implement synthetic local authentication using maintained credential/session facilities with expiry/revocation policy and no production credentials. Add a server-side authorization layer for two tenants and multiple roles, verifying read, list, create, update, delete and property-level restrictions. Inject forged/expired credentials, guessed resource IDs, cross-tenant requests, unauthorized role changes and sensitive response fields. Show that the application's principal and tenant are not trusted merely because a request supplied an ID, cookie or a hidden UI claim.
  - Criteria: Authentication and authorization are distinct and independently tested. Real signed/opaque session verification and expiry/revocation match the documented local threat model; cross-tenant and role/field escalation attempts fail at server-side boundaries for all relevant methods, including negative writes and overbroad response serialization. Database RLS is recognized as defense in depth rather than the sole application policy, and CORS/client hiding is not accepted as authorization. Secrets and private material are absent from logs/evidence. Public-production security omissions are explicitly acknowledged.
  - Evidence: Synthetic account/session fixture, role-tenant-method-field access matrix, HTTP negative and positive tests with effective principal and safe status/error outputs, credential-lifecycle observations, data state checks and threat/remaining-risk rationale.

- **APP3-AS3** (required transactional service invariant and idempotent replay)
  - Outcomes: APP3-O5, APP3-O7, APP3-O8, APP3-O9, APP3-O13, APP3-O14
  - Work: Implement a domain operation requiring at least two related PostgreSQL changes, enforce a database-backed business invariant and reproduce two concurrent requests with a controlled conflict. Design a scoped idempotency-key or equivalent replay policy for one side-effecting endpoint; inject duplicate same-key submissions, key reuse with different payloads, serialization/transaction failure and a post-commit lost-response scenario. Propose or demonstrate a bounded durable outbox/worker approach for dependent background work with explicit at-least-once delivery and retry behavior.
  - Criteria: No partial commit or unprotected cross-tenant mutation violates the domain invariant, including concurrent requests. The application uses a correctly scoped transaction connection and rollback/commit decisions; recognized serialization failures trigger bounded full-unit retry where safe. Same-key duplicates follow a documented deterministic/accepted-outcome policy, mismatched payloads are rejected, and network uncertainty does not lead to indiscriminate repeat effects. A durable outbox is not misdescribed as exactly-once external delivery. Failure cases inspect real database state, not only mocked repository returns.
  - Evidence: Real local PostgreSQL migration/schema fixtures, versioned service/repository source, concurrent request interleaving table, transaction and idempotency policies, before/after state checks, redelivery/outbox or equivalent design evidence and regression tests.

- **APP3-AS4** (required versioned api contract, independent consumer and dependency boundary)
  - Outcomes: APP3-O1, APP3-O3, APP3-O4, APP3-O10, APP3-O11, APP3-O13, APP3-O14
  - Work: Publish a machine-readable OpenAPI contract and executable examples for a route family, then apply a bounded version change or field/status evolution. Run at least two independent local consumers (old and revised behavior) and classify compatible and breaking cases. Add one local synthetic outbound dependency whose URL is fixed/allowlisted, response validated and failure bounded; test timeout, invalid upstream shape, 429/5xx or rejected transport and an unsafe redirect/target scenario. Explain how structured problem details and retry policy support consumers without exposing internal secrets.
  - Criteria: OpenAPI/request/response examples match observed framework behavior including authentication, errors, pagination and changed fields. Tests identify a real incompatibility before correction, preserve supported consumers or clearly document an unavoidable break, and do not assume TypeScript interfaces enforce external JSON. Outbound calls have controlled destinations, response/body/time limits and justified retry eligibility; SSRF/redirect or secret leakage paths are rejected in the local fixture. No unsafe replay of a non-idempotent remote mutation is claimed safe.
  - Evidence: OpenAPI and validation output, old/new consumer source with normal/negative tests, compatibility matrix and migration note, mocked/local upstream failure and SSRF tests, documented problem/error codes and transport-boundary rationale.

- **APP3-AS5** (required background work, fault handling and operability drill)
  - Outcomes: APP3-O2, APP3-O8, APP3-O9, APP3-O10, APP3-O12, APP3-O14, APP3-O15
  - Work: Extend the local service with a bounded background/dispatch workflow, structured request/job correlation, valid configuration and clear liveness/readiness signals. Inject a failed external call after the database commit, an exhausted retry/dead-letter condition, a lost or duplicated job acknowledgement, a missing dependency on startup, an in-flight request during shutdown and an unrelated request that must still complete safely. Capture a causal incident timeline and repair at least one root cause, with an explicit account of nonrecoverable observations.
  - Criteria: The policy distinguishes durable queued work from in-process tasks, documents retry and poison-message handling, and prevents silent successful responses when required work is not accepted. The service fails fast on bad configuration, reports readiness and health based on actual local checks, drains or rejects bounded work on shutdown, and releases DB and other resources. Logging is correlated and sanitized; failure and recovery are demonstrated with reproducible fixture evidence rather than claims of production high availability. Corrective code has meaningful regression coverage.
  - Evidence: Job/outbox fixtures, failure timeline and redacted logs, configuration and state machine, tests for retry/duplicate/shutdown/dependency outage, bounded timing/health observations, repair diff and limitations report.

- **APP3-AS6** (required security, concurrency and service incident regression review)
  - Outcomes: APP3-O3, APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O8, APP3-O9, APP3-O12, APP3-O13, APP3-O14, APP3-O15
  - Work: Audit a supplied or evolving API with deliberate flaws in object/property authorization, request schema/canonicalization, rate/resource bounds, transaction connection scope, dependency handling and diagnostic output. Select applicable OWASP API risks; construct independent normal/denied/concurrent/oversized fixture requests and a controlled production-style incident trace; repair at least two meaningful defects without weakening documented contracts. Verify via domain unit tests, framework HTTP injection, real PostgreSQL integration, consumer contract checks and negative-path/security regression tests.
  - Criteria: The audit identifies verifiable trust boundaries, not merely an OWASP checklist label. Each fixed defect has failing-before/passing-after tests, captures database/object/role evidence as applicable and avoids dangerous handling of synthetic credentials or raw stack/error leakage. Body/page/work limits, CSRF/cookie/CORS policy and multi-tenant property exposure are evaluated against the actual chosen design. The incident diagnosis states what logs/tests support and where evidence is missing; a green test count alone is insufficient.
  - Evidence: Threat-and-test matrix, synthetic fixtures, observed exploit/failure steps, layered tests and database-state comparisons, sanitized causal incident notes, corrected code, compatibility checks and remaining-risk statement.

- **APP3-AS7** (required integrated typed api service and independent engineering defense)
  - Outcomes: APP3-O1, APP3-O2, APP3-O3, APP3-O4, APP3-O5, APP3-O6, APP3-O7, APP3-O8, APP3-O9, APP3-O10, APP3-O11, APP3-O12, APP3-O13, APP3-O14, APP3-O15, APP3-O16
  - Work: Deliver one cohesive independently reproducible Fastify/TypeScript and PostgreSQL service for a bounded synthetic multi-tenant domain, integrating requirements traceability, typed request/response schema and portable HTTP contract, actual authentication and server-side object/property/tenant authorization, domain-adapter boundaries, transactional concurrency safety, idempotency and justified background work, safe dependency handling, versioned OpenAPI, observability, fault and shutdown policy. Reuse qualifying components from APP3-AS1–AS6 rather than build unrelated servers. Handle an unfamiliar bounded permission or business-rule change or incident, retest the relevant layers and defend why each mechanism belongs to the framework, the domain, Node or database.
  - Criteria: A reviewer can provision the documented free local dependencies, start disposable PostgreSQL and the loopback API using synthetic users, execute reproducible positive and negative clients, observe a real transaction race and denial of cross-tenant/property access, and verify cleanup without paid hosting, a React app or live identity provider. The old/new contract and error behavior are accurate; duplicate and partial-failure cases preserve stated invariants and do not overclaim exactly-once external delivery. The unfamiliar change produces inspectable working code and regression tests. The learner independently defends boundary, privacy, transaction, retry and operations trade-offs and states verified versus unsupported production guarantees.
  - Evidence: Versioned service source, manifest/lockfile and local prerequisite recipe, SQL migrations/seeds and disposable DB setup, API/OpenAPI requirements and role matrix, independent clients, negative/normal/concurrency/replay/incident test logs, sanitized request correlation, clean-checkout and repair/change records, and accessible written/recorded/live technical defense.

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

This course replaces APP3's legacy course-format
assessment contract and direct APP1 prerequisite with
a new OEE `v0.2.0` **draft**. Earlier APP3 completions
remain attached to their prior course revision and
cannot silently satisfy these new outcomes. APP3 is
not automatically `tested` or `verified` simply
because repository validators and CI pass.
APP5–APP9 and all APP electives now publish their own separately
migrated `v0.2.0` drafts. Downstream OEE Workspace,
content/resource and 0xNAND source/evidence pins still require
deliberate revision review; they are not automatically upgraded.

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
