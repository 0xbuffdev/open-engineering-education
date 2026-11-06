# APP9 — Application Engineering Capstone

**Program:** APP — Application Engineering
**Type:** `project`
**Prerequisites:** [APP1](APP1.md), [APP2](APP2.md), [APP3](APP3.md), [APP4](APP4.md), [APP5](APP5.md), [APP6](APP6.md), [APP7](APP7.md), [APP8](APP8.md)
**Duration:** 8–10 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

The capstone is the final project course in Application Engineering. You will combine frontend, backend, data, testing, deployment, observability, and production architecture into one coherent product. The project should be substantial enough to demonstrate professional engineering without relying on unnecessary architectural complexity.

## Learning outcomes

By the end of this course, the learner will be able to:

- Translate a user problem into scoped product and technical requirements.
- Design and implement a complete full-stack application.
- Integrate frontend, backend, persistent data, authentication, and asynchronous work appropriately.
- Build automated tests and operate a reliable CI/CD workflow.
- Deploy and observe a real application and recover from a failed release.
- Measure application behavior and make architecture decisions from evidence.
- Defend production trade-offs involving reliability, performance, security, maintainability, and cost.

## Modules

### Module 1 — Product Definition & Architecture

#### Outcomes

- Explain **Requirements, user workflows, domain model, architecture, and scope** in the context of the course.
- Apply **Architecture review** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Course introduction: Application Engineering Capstone** — `lesson`

   The capstone is the final project course in Application Engineering. You will combine frontend, backend, data, testing, deployment, observability, and production architecture into one coherent product. The project should be substantial enough to demonstrate professional engineering without relying on unnecessary architectural complexity.
2. **Requirements, user workflows, domain model, architecture, and scope** — `lesson`
3. **Architecture review** — `test`
4. **Convert a product idea into requirements and an architecture diagram** — `lab`

### Module 2 — Full-Stack Implementation

#### Outcomes

- Explain **Frontend, backend, database, authentication, and application workflows** in the context of the course.

#### Lessons

1. **Frontend, backend, database, authentication, and application workflows** — `lesson`
2. **Implementation checkpoint** — `test`
3. **Implement one complete vertical slice from UI interaction through persistence** — `lab`

### Module 3 — Quality, Reliability & Security

#### Outcomes

- Explain **Testing, validation, observability, secure configuration, resilience, and failure handling** in the context of the course.

#### Lessons

1. **Testing, validation, observability, secure configuration, resilience, and failure handling** — `lesson`
2. **Production readiness checkpoint** — `test`
3. **Introduce a controlled failure and use logs/metrics to diagnose it** — `lab`

### Module 4 — Deployment & Performance

#### Outcomes

- Explain **CI/CD, deployment, monitoring, load testing, rollback, and operational documentation** in the context of the course.
- Apply **Release review** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **CI/CD, deployment, monitoring, load testing, rollback, and operational documentation** — `lesson`
2. **Release review** — `test`
3. **Perform a load measurement, identify a bottleneck, and record the improvement** — `lab`

### Module 5 — Final Project Lab

#### Outcomes

- Complete and explain the Final Project Lab lab, demonstrating the applicable course outcomes and retaining required evidence.

#### Lessons

1. **Build, deploy, operate, evaluate, and harden the production application** — `lab`

## Completion requirements

- Complete the required practical exercises, knowledge checkpoints, and evaluated labs described in the modules.
- Complete the final integrated `lab` in the last module and satisfy its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, failures investigated, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Suitable capstone shapes:**

- multi-user SaaS application
- developer platform/tool
- workflow system
- collaborative application
- data/product management system
- education product
**Required project qualities:**

- written requirements and scope
- architecture/design document
- frontend and backend
- relational data model
- authentication and authorization
- automated tests
- CI/CD
- production deployment
- observability
- secure configuration and secrets handling
- meaningful load/performance measurement
- failure/rollback procedure
- API and user documentation
- architecture diagram
- technical retrospective
**Final integration lab — required work:**

Build, deploy, operate, evaluate, and harden the production application described by the required qualities below.
**Project defense:**

The learner must:

1. demo the product using a realistic workflow;
2. explain its architecture and major trade-offs;
3. demonstrate the automated tests and deployment pipeline;
4. show one failure or performance problem and the evidence used to fix it;
5. explain what they would change at the next scale of usage.

This is the **Program 2 — APP graduation requirement**.
