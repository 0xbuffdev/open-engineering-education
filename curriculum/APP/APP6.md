# APP6 — Software Quality & Engineering Operations

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP3](APP3.md), [APP5](APP5.md)
**Duration:** 4 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Develop a practical quality strategy for production applications. You will work across unit, integration, and end-to-end testing, CI, static analysis, dependency management, observability, configuration, and production debugging.

## Learning outcomes

By the end of this course, the learner will be able to:

- Choose appropriate test levels for different application behaviors.
- Build CI workflows that continuously verify software quality.
- Use logging, metrics, and traces to investigate application failures.
- Manage configuration, secrets, dependencies, and reproducible builds safely.
- Turn discovered production failures into durable tests and engineering improvements.

## Modules

### Module 1 — Testing Strategy

#### Outcomes

- Explain **Unit, integration, and end-to-end tests** in the context of the course.
- Apply **Choosing the right test boundary** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Course introduction: Software Quality & Engineering Operations** — `lesson`

   Develop a practical quality strategy for production applications. You will work across unit, integration, and end-to-end testing, CI, static analysis, dependency management, observability, configuration, and production debugging.
2. **Unit, integration, and end-to-end tests** — `lesson`
3. **Choosing the right test boundary** — `lesson`
4. **test strategy** — `test`
5. **Move one over-mocked test to the most useful level** — `lab`

### Module 2 — Automation & Delivery Quality

#### Outcomes

- Explain **CI, static analysis, and dependency management** in the context of the course.
- Apply **Reproducible checks before merge** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **CI, static analysis, and dependency management** — `lesson`
2. **Reproducible checks before merge** — `lesson`
3. **engineering automation** — `test`
4. **Build a CI workflow that fails on tests or quality violations** — `lab`

### Module 3 — Observability

#### Outcomes

- Explain **Structured logging and metrics** in the context of the course.
- Apply **Tracing concepts and cross-component diagnosis** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Structured logging and metrics** — `lesson`
2. **Tracing concepts and cross-component diagnosis** — `lesson`
3. **observability** — `test`
4. **Trace one failed request through multiple components** — `lab`

### Module 4 — Incident Debugging

#### Outcomes

- Explain **Incident symptoms, evidence, and hypotheses** in the context of the course.
- Apply **Configuration, secrets, and recovery practices** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Incident symptoms, evidence, and hypotheses** — `lesson`
2. **Configuration, secrets, and recovery practices** — `lesson`
3. **incident reasoning** — `test`
4. **Diagnose a controlled production-style failure from logs and configuration** — `lab`

### Module 5 — Reliability Upgrade

#### Outcomes

- Complete and explain the Reliability Upgrade lab, demonstrating the applicable course outcomes and retaining required evidence.

#### Lessons

1. **Apply the Reliability Upgrade to the APP5 product** — `lab`

## Completion requirements

- Complete the required practical exercises, knowledge checkpoints, and evaluated labs described in the modules.
- Complete the final integrated `lab` in the last module and satisfy its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, failures investigated, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required practical exercises:**

- turn a bug into a regression test
- build a CI pipeline
- trace one failed request across components
- remove a flaky test
**Final integration lab — required work:**

Required artifact: **Reliability Upgrade**.

Take the APP5 product and add a meaningful test strategy, CI pipeline, observability, deployment-safe configuration and a documented incident/debugging workflow.

**Exit demonstration:**

The learner can choose appropriate test levels, diagnose a failing production workflow from evidence, and explain why a test belongs where it does.

---
