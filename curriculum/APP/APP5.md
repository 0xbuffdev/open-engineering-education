# APP5 — Full-Stack Architecture

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP2](APP2.md), [APP3](APP3.md), [APP4](APP4.md)
**Duration:** 8 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Move from individual application layers to a complete product architecture. You will integrate persistent data, authentication, asynchronous work, caching, realtime behavior, and external services while preserving understandable system boundaries.

## Learning outcomes

By the end of this course, the learner will be able to:

- Trace a user workflow across frontend, API, application logic, data, and external services.
- Define boundaries between frontend, backend, domain logic, and infrastructure components.
- Integrate asynchronous jobs, queues, caching, file/object storage, or realtime communication appropriately.
- Design for partial dependency failure and graceful degradation.
- Build an integrated full-stack product with end-to-end tests and documented architecture.
- Enforce identity and resource authorization throughout frontend, API and data boundaries.
- Integrate asynchronous work, object storage and cache invalidation without exposing private data or losing committed operations.
- Build contract, integration and end-to-end verification for a compatible full-stack change.
- Recover an end-to-end workflow from a dependency failure using correlated evidence and documented degradation behavior.

## Modules

### Module 1 — System Boundaries

#### Outcomes

- Explain **Frontend/backend responsibilities** in the context of the course.
- Apply **Domain modeling and API contracts** in a problem, implementation, experiment, or design decision.

- Trace an operation across architecture boundaries and justify what each layer owns.

#### Lessons

1. **Course introduction: Full-Stack Architecture** — `lesson`

   Move from individual application layers to a complete product architecture. You will integrate persistent data, authentication, asynchronous work, caching, realtime behavior, and external services while preserving understandable system boundaries.
2. **Frontend/backend responsibilities** — `lesson`
3. **Domain modeling and API contracts** — `lesson`
4. **Domain boundaries and bounded contexts** — `lesson`
5. **Contract-first frontend/backend interfaces** — `lesson`
6. **Error propagation across application layers** — `lesson`
7. **system boundaries** — `test`
8. **Trace one business operation across the application boundary** — `lab`

### Module 2 — State & Data Flow

#### Outcomes

- Explain **Application state versus server state** in the context of the course.
- Apply **Data flow across UI, API, and persistence** in a problem, implementation, experiment, or design decision.

- Design state transitions that distinguish speculative local state from committed server state.

#### Lessons

1. **Application state versus server state** — `lesson`
2. **Data flow across UI, API, and persistence** — `lesson`
3. **Data ownership and authoritative server state** — `lesson`
4. **Caching and mutation invalidation on the client** — `lesson`
5. **Consistent updates across UI, API and persistence** — `lesson`
6. **state management** — `test`
7. **Map the state transitions of one end-to-end workflow** — `lab`

### Module 3 — Caching, Files & External Resources

#### Outcomes

- Explain **Caching fundamentals and invalidation** in the context of the course.
- Apply **File uploads and object storage concepts** in a problem, implementation, experiment, or design decision.

- Handle externally stored data and cache lifecycles without leaking resources or trusting client metadata.

#### Lessons

1. **Caching fundamentals and invalidation** — `lesson`
2. **File uploads and object storage concepts** — `lesson`
3. **Object-store access policies and signed URLs** — `lesson`
4. **Cache invalidation and content freshness** — `lesson`
5. **Asynchronous file validation and malware-safe upload boundaries** — `lesson`
6. **external resource design** — `test`
7. **Design a safe file-upload flow and identify failure cases** — `lab`

### Module 4 — Asynchronous & Realtime Systems

#### Outcomes

- Explain **Background jobs and queues** in the context of the course.
- Apply **Realtime communication, resilience, and graceful degradation** in a problem, implementation, experiment, or design decision.

- Design asynchronous features that remain correct under retries, partial outages and reconnects.

#### Lessons

1. **Background jobs and queues** — `lesson`
2. **Realtime communication, resilience, and graceful degradation** — `lesson`
3. **Delivery guarantees and event ownership** — `lesson`
4. **Background job retries, deadlines and poison messages** — `lesson`
5. **Realtime connection lifecycle and client synchronization** — `lesson`
6. **asynchronous architecture** — `test`
7. **Move a slow operation behind a background boundary and define its failure behavior** — `lab`

### Module 5 — Identity & End-to-End Authorization

#### Outcomes

- Enforce authorization at every server-side data and action boundary.
- Model session expiry and permission changes consistently across client and service.

#### Lessons

1. **Session lifecycle across frontend and backend** — `lesson`
2. **Resource ownership and tenant-scoped access** — `lesson`
3. **Anti-forgery, token boundaries, and logout** — `lesson`
4. **Auditing authorization and revoked access** — `lesson`
5. **Full-stack identity and access invariants** — `test`
6. **Audit a protected end-to-end workflow** — `lab`

### Module 6 — Full-Stack Testing & Change Safety

#### Outcomes

- Build a test pyramid focused on real workflow risks rather than arbitrary coverage targets.
- Demonstrate a compatible, reversible change across frontend, API, and persistence.

#### Lessons

1. **Contract tests between client and service** — `lesson`
2. **Database integration fixtures and isolation** — `lesson`
3. **End-to-end test data and environment reproducibility** — `lesson`
4. **Feature flags, staged changes, and rollback design** — `lesson`
5. **Test boundary and contract reasoning** — `test`
6. **Test an evolving full-stack feature** — `lab`

### Module 7 — Operational Workflows & Failure Recovery

#### Outcomes

- Diagnose end-to-end workflow failures using correlated client and server evidence.
- Define bounded failure behavior when a data store, job queue or external API is unavailable.

#### Lessons

1. **Correlation identifiers across components** — `lesson`
2. **Rate limiting and backpressure for user flows** — `lesson`
3. **Readiness probes and dependency timeouts** — `lesson`
4. **Graceful degradation and user-facing recovery** — `lesson`
5. **Recovery and boundary isolation** — `test`
6. **Recover a failed multi-service user workflow** — `lab`

### Module 8 — Integrated Full-Stack Product

#### Outcomes

- Complete and explain the Integrated Full-Stack Product lab, demonstrating the applicable course outcomes and retaining required evidence.

#### Lessons

1. **Extend APP2–APP4 into the Integrated Full-Stack Product** — `lab`

## Completion requirements

- Complete the required practical exercises, knowledge checkpoints, and evaluated labs described in the modules.
- Complete the final integrated `lab` in the last module and satisfy its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, failures investigated, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required practical exercises:**

- add caching to an existing endpoint
- implement a background job
- design a realtime update flow
- handle partial dependency failure
**Final integration lab — required work:**

Required artifact: **Integrated Full-Stack Product**.

Extend APP2–APP4 into a coherent application with a real user workflow, persistent data, authentication, background work, one realtime or asynchronous feature, and end-to-end tests.

**Expanded module assessments and practical work:**

- **Module 1 checkpoint and micro-lab:** Produce a context diagram, request/response and dependency trace with at least one explicit failure boundary.
- **Module 2 checkpoint and micro-lab:** Demonstrate rollback of an optimistic update, stale-response handling and transactional persistence evidence.
- **Module 3 checkpoint and micro-lab:** Exercise invalid file metadata, expired upload access and a stale cache; show controlled authorization and recovery.
- **Module 4 checkpoint and micro-lab:** Show a replay-safe job, bounded retry behavior and client resynchronization after a missed notification.

- **Module 5 — Identity & End-to-End Authorization (Audit a protected end-to-end workflow):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Create role-based and owner-based access cases, revoke one session during an operation, and verify the UI and API both respond safely.
  - Verification: Cross-user and expired sessions are rejected server-side; no private cached data remains after logout.
  - Evidence: Access matrix, denied requests, tests, and audit trail.
  - Failure analysis: Explain stale client permissions, confused deputies, cache isolation, and trust in client-supplied identifiers.
- **Module 6 — Full-Stack Testing & Change Safety (Test an evolving full-stack feature):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Add a user workflow across UI, API and schema while an older client still operates; include failure tests and a migration/rollback plan.
  - Verification: All test layers agree about contract, persistence, authorization, and upgrade compatibility.
  - Evidence: CI run, fixtures, contracts and staged deployment record.
  - Failure analysis: Explain contract drift, brittle browser tests, data migration incompatibility and flaky test diagnostics.
- **Module 7 — Operational Workflows & Failure Recovery (Recover a failed multi-service user workflow):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Inject a slow external dependency during a user action and measure the effect through client, service and worker logs; implement a bounded fallback.
  - Verification: The user receives a predictable result, no duplicate persistent action occurs, and retries recover after dependency restoration.
  - Evidence: Tracing evidence, failure timeline, tests and a recovery procedure.
  - Failure analysis: Discuss retry amplification, partial commits, hidden errors and fallback behavior that misleads users.

**Exit assessment expectation:**

Demonstrate the relevant course outcomes on an unfamiliar scenario, including failure behavior and independently reproducible evidence. Checkpoint responses must explain mechanisms; every final lab or project must integrate and verify the expanded material.

**Exit demonstration:**

The learner can explain the major boundaries of the product and trace a user action through browser, API, application logic, database and external services.

---
