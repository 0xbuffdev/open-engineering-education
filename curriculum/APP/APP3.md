# APP3 — Backend Engineering & API Design

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP1](APP1.md)
**Duration:** 5 weeks
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

## Modules

### Module 1 — API Structure

#### Outcomes

- Explain **Routes, handlers, middleware, and service boundaries** in the context of the course.
- Apply **Designing resource-oriented APIs** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Course introduction: Backend Engineering & API Design** — `lesson`

   Learn to turn application requirements into maintainable backend services. You will work through API boundaries, business logic, security controls, background work, idempotency, logging, and operational error handling.
2. **Routes, handlers, middleware, and service boundaries** — `lesson`
3. **Designing resource-oriented APIs** — `lesson`
4. **API boundaries** — `test`
5. **Turn a domain description into an API contract** — `lab`

### Module 2 — Validation & Failure Behavior

#### Outcomes

- Explain **Input validation and structured errors** in the context of the course.
- Apply **Configuration and predictable failure handling** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Input validation and structured errors** — `lesson`
2. **Configuration and predictable failure handling** — `lesson`
3. **failure behavior** — `test`
4. **Add invalid-input cases and assert the API error contract** — `lab`

### Module 3 — Identity & Access

#### Outcomes

- Explain **Authentication** in the context of the course.
- Apply **Authorization and permission boundaries** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Authentication** — `lesson`
2. **Authorization and permission boundaries** — `lesson`
3. **authentication versus authorization** — `test`
4. **Model users, roles, and one protected resource** — `lab`

### Module 4 — Operational Backend Concerns

#### Outcomes

- Explain **Logging and health checks** in the context of the course.
- Apply **Background work, idempotency, and API versioning** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Logging and health checks** — `lesson`
2. **Background work, idempotency, and API versioning** — `lesson`
3. **production API behavior** — `test`
4. **Simulate a duplicate request and make the operation safe** — `lab`

### Module 5 — Production API

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

**Exit demonstration:**

The learner can design an API from requirements, explain its boundaries and failure behavior, and test both success and failure paths.

---
