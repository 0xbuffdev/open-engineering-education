# APP3 — Backend Engineering & API Design

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP1](APP1.md)
**Duration:** 9 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Learn to turn application requirements into maintainable backend services. You will work through API boundaries, business logic, security controls, background work, idempotency, logging, and operational error handling.

## Learning outcomes

By the end of this course, the learner will be able to:

- Design clear HTTP APIs from application requirements.
- Structure backend code around domain, application, and infrastructure responsibilities.
- Validate inputs and return consistent, useful error responses.
- Implement authentication and authorization appropriate to application requirements.
- Handle retries, duplicate requests, background work, and operational failures safely.
- Build, test, document, and observe a production-oriented backend service.
- Enforce domain invariants and transaction boundaries under concurrent requests and partial failures.
- Publish a versioned API contract, verify consumer compatibility and test error behavior independently of framework internals.
- Protect authenticated and multi-tenant resources through server-side authorization and negative-path tests.
- Diagnose a production-style backend failure through correlated telemetry, tests and a repeatable repair.

## Modules

### Module 1 — API Structure

#### Outcomes

- Explain **Routes, handlers, middleware, and service boundaries** in the context of the course.
- Apply **Designing resource-oriented APIs** in a problem, implementation, experiment, or design decision.

- Separate transport, application, domain, and persistence responsibilities in a testable API.

#### Lessons

1. **Course introduction: Backend Engineering & API Design** — `lesson`

   Learn to turn application requirements into maintainable backend services. You will work through API boundaries, business logic, security controls, background work, idempotency, logging, and operational error handling.
2. **Routes, handlers, middleware, and service boundaries** — `lesson`
3. **Designing resource-oriented APIs** — `lesson`
4. **HTTP contract design and API schema evolution** — `lesson`
5. **Routing boundaries, service dependencies, and layering** — `lesson`
6. **Request and response serialization and content validation** — `lesson`
7. **API boundaries** — `test`
8. **Turn a domain description into an API contract** — `lab`

### Module 2 — Validation & Failure Behavior

#### Outcomes

- Explain **Input validation and structured errors** in the context of the course.
- Apply **Configuration and predictable failure handling** in a problem, implementation, experiment, or design decision.

- Classify errors and handle untrusted input without leaking sensitive operational details.

#### Lessons

1. **Input validation and structured errors** — `lesson`
2. **Configuration and predictable failure handling** — `lesson`
3. **Trust boundaries and canonical input validation** — `lesson`
4. **Failure classes, exception mapping, and safe diagnostics** — `lesson`
5. **Timeouts, cancellation, and resource cleanup** — `lesson`
6. **failure behavior** — `test`
7. **Add invalid-input cases and assert the API error contract** — `lab`

### Module 3 — Identity & Access

#### Outcomes

- Explain **Authentication** in the context of the course.
- Apply **Authorization and permission boundaries** in a problem, implementation, experiment, or design decision.

- Implement authentication and per-resource authorization without substituting frontend checks for backend enforcement.

#### Lessons

1. **Authentication** — `lesson`
2. **Authorization and permission boundaries** — `lesson`
3. **Password storage and credential security fundamentals** — `lesson`
4. **Sessions, tokens, revocation, and expiry** — `lesson`
5. **Permission checks, resource ownership, and multi-tenant scoping** — `lesson`
6. **authentication versus authorization** — `test`
7. **Model users, roles, and one protected resource** — `lab`

### Module 4 — Operational Backend Concerns

#### Outcomes

- Explain **Logging and health checks** in the context of the course.
- Apply **Background work, idempotency, and API versioning** in a problem, implementation, experiment, or design decision.

- Operate background and synchronous backend workflows with correct replay and diagnostic behavior.

#### Lessons

1. **Logging and health checks** — `lesson`
2. **Background work, idempotency, and API versioning** — `lesson`
3. **Structured logging, correlation IDs, and audit trails** — `lesson`
4. **Background jobs, bounded retries, and dead-letter queues** — `lesson`
5. **Request idempotency, replay safety, and API compatibility** — `lesson`
6. **production API behavior** — `test`
7. **Simulate a duplicate request and make the operation safe** — `lab`

### Module 5 — Domain Models & Dependency Boundaries

#### Outcomes

- Encode business invariants in domain operations independently of HTTP and storage.
- Design replaceable infrastructure boundaries and verify behavior through meaningful tests.

#### Lessons

1. **Domain invariants and aggregate boundaries** — `lesson`
2. **Dependency inversion and adapters** — `lesson`
3. **Application services and transaction orchestration** — `lesson`
4. **Test doubles versus contract tests** — `lesson`
5. **Domain invariant and boundary verification** — `test`
6. **Refactor a coupled API into layers** — `lab`

### Module 6 — Persistence, Transactions & Consistency

#### Outcomes

- Explain when a domain invariant must be enforced in a database transaction.
- Handle concurrent writes without silently overwriting protected state.

#### Lessons

1. **Query planning and repository responsibility** — `lesson`
2. **Database constraints and transaction boundaries** — `lesson`
3. **Concurrency, isolation, and lost-update avoidance** — `lesson`
4. **Optimistic concurrency and consistency trade-offs** — `lesson`
5. **Transaction and race-condition reasoning** — `test`
6. **Reproduce and repair a concurrent write defect** — `lab`

### Module 7 — API Contracts, Compatibility & Documentation

#### Outcomes

- Specify behavior sufficiently for an independent client to integrate.
- Evolve an endpoint without silently breaking existing callers.

#### Lessons

1. **OpenAPI and machine-readable request schemas** — `lesson`
2. **Backwards-compatible API evolution** — `lesson`
3. **Pagination, filtering, sorting, and resource identity** — `lesson`
4. **Error documents and consumer-driven integration** — `lesson`
5. **API compatibility and consumer impact** — `test`
6. **Publish and validate a versioned API contract** — `lab`

### Module 8 — Backend Testing & Production Observability

#### Outcomes

- Design a backend quality strategy covering security, concurrency, and failure behavior.
- Diagnose a production-style failure from observable evidence and turn it into a regression test.

#### Lessons

1. **Unit, integration, contract, and end-to-end test boundaries** — `lesson`
2. **Logs, metrics, traces, and correlation** — `lesson`
3. **Health, readiness, and dependency diagnosis** — `lesson`
4. **Incident reproduction and resource leak investigation** — `lesson`
5. **Choosing backend observability and test coverage** — `test`
6. **Investigate and prevent a backend outage** — `lab`

### Module 9 — Production API

#### Outcomes

- Complete and explain the Production API lab, demonstrating the applicable course outcomes and retaining required evidence.

#### Lessons

1. **Build and validate the Production API** — `lab`

## Completion requirements

- Complete the required practical exercises, knowledge checkpoints, and evaluated labs described in the modules.
- Complete the final integrated `lab` in the last module and satisfy its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, failures investigated, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required practical exercises:**

- design an API from requirements
- implement validation and error contracts
- add authentication/authorization
- simulate duplicate requests
- add structured logging
**Final integration lab — required work:**

Required artifact: **Production API**.

Build a backend service with a documented API, authentication, authorization, validation, structured errors, tests, logging and health checks.

**Expanded module assessments and practical work:**

- **Module 1 checkpoint and micro-lab:** Verify a route-to-service trace, stable error shape, and contract tests against invalid requests.
- **Module 2 checkpoint and micro-lab:** Use negative-path tests for malformed input, partial failures, timeout, and deterministic error responses.
- **Module 3 checkpoint and micro-lab:** Reject unauthenticated and cross-tenant access, demonstrate session expiry, and document credential handling.
- **Module 4 checkpoint and micro-lab:** Demonstrate a repeatable duplicate-request test and trace one failed async job across log events.

- **Module 5 — Domain Models & Dependency Boundaries (Refactor a coupled API into layers):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Extract a rule-heavy feature into domain/application/adapter layers while preserving its public API and error contract.
  - Verification: Pass invariant tests and contract tests with both a real persistence adapter and a controlled test substitute.
  - Evidence: Dependency diagram, regression suite, and documented boundary decisions.
  - Failure analysis: Detect leaky transport types, duplicated rules, and over-mocked tests that conceal broken integration.
- **Module 6 — Persistence, Transactions & Consistency (Reproduce and repair a concurrent write defect):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Create a two-client race, observe an incorrect result, and repair it through constraints, concurrency tokens, or a suitable transaction policy.
  - Verification: Prove the invariant holds under repeated concurrent attempts, including conflict responses.
  - Evidence: Race reproduction, database state, concurrency tests, and transaction explanation.
  - Failure analysis: Explain isolation anomalies, deadlocks, retry safety, and expected conflict semantics.
- **Module 7 — API Contracts, Compatibility & Documentation (Publish and validate a versioned API contract):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Document an API, validate examples, change a contract with a compatibility plan, and test an old client against the new implementation.
  - Verification: Run documented contract tests for success, invalid input, access denial, pagination, and backwards compatibility.
  - Evidence: API document, representative exchanges, contract test results, and change note.
  - Failure analysis: Identify underspecified nullability, inconsistent error codes, and undocumented version-breaking behavior.
- **Module 8 — Backend Testing & Production Observability (Investigate and prevent a backend outage):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Inject a dependency timeout or malformed message, correlate logs/traces to the failure, and add an automated regression test.
  - Verification: Demonstrate the failure before, passing diagnostics after, and clean recovery without exposing secrets.
  - Evidence: Telemetry, test report, failure timeline, and recovery plan.
  - Failure analysis: Distinguish health checks from readiness, avoid logging credentials, and account for missing traces.

**Exit assessment expectation:**

Demonstrate the course outcomes through a new scenario, including at least one negative path and independently reproducible evidence. Checkpoint answers must explain the mechanism and not merely name a tool. The final integration lab must incorporate and verify the expanded material.

**Exit demonstration:**

The learner can design an API from requirements, explain its boundaries and failure behavior, and test both success and failure paths.

---
