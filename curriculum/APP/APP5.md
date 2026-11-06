# APP5 — Full-Stack Architecture

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP2](APP2.md), [APP3](APP3.md), [APP4](APP4.md)
**Duration:** 6 weeks
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

## Modules

### Module 1 — System Boundaries

#### Outcomes

- Explain **Frontend/backend responsibilities** in the context of the course.
- Apply **Domain modeling and API contracts** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Course introduction: Full-Stack Architecture** — `lesson`

   Move from individual application layers to a complete product architecture. You will integrate persistent data, authentication, asynchronous work, caching, realtime behavior, and external services while preserving understandable system boundaries.
2. **Frontend/backend responsibilities** — `lesson`
3. **Domain modeling and API contracts** — `lesson`
4. **system boundaries** — `test`
5. **Trace one business operation across the application boundary** — `lab`

### Module 2 — State & Data Flow

#### Outcomes

- Explain **Application state versus server state** in the context of the course.
- Apply **Data flow across UI, API, and persistence** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Application state versus server state** — `lesson`
2. **Data flow across UI, API, and persistence** — `lesson`
3. **state management** — `test`
4. **Map the state transitions of one end-to-end workflow** — `lab`

### Module 3 — Caching, Files & External Resources

#### Outcomes

- Explain **Caching fundamentals and invalidation** in the context of the course.
- Apply **File uploads and object storage concepts** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Caching fundamentals and invalidation** — `lesson`
2. **File uploads and object storage concepts** — `lesson`
3. **external resource design** — `test`
4. **Design a safe file-upload flow and identify failure cases** — `lab`

### Module 4 — Asynchronous & Realtime Systems

#### Outcomes

- Explain **Background jobs and queues** in the context of the course.
- Apply **Realtime communication, resilience, and graceful degradation** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Background jobs and queues** — `lesson`
2. **Realtime communication, resilience, and graceful degradation** — `lesson`
3. **asynchronous architecture** — `test`
4. **Move a slow operation behind a background boundary and define its failure behavior** — `lab`

### Module 5 — Integrated Full-Stack Product

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

**Exit demonstration:**

The learner can explain the major boundaries of the product and trace a user action through browser, API, application logic, database and external services.

---
