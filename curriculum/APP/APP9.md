# APP9 — Application Engineering Capstone

**Program:** APP — Application Engineering
**Type:** `project`
**Prerequisites:** [APP1](APP1.md), [APP2](APP2.md), [APP3](APP3.md), [APP4](APP4.md), [APP5](APP5.md), [APP6](APP6.md), [APP7](APP7.md), [APP8](APP8.md)
**Duration:** 12–16 weeks
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
- Validate a scoped product need using ethically collected feedback, explicit acceptance criteria and a documented change decision.
- Classify project data and demonstrate protective controls for privacy, access and retention.
- Define operational indicators and demonstrate deployment recovery and data integrity under injected failure.
- Support an independent clean-checkout reproduction, a scoped change request and an evidence-based technical defense.

## Modules

### Module 1 — Product Definition & Architecture

#### Outcomes

- Explain **Requirements, user workflows, domain model, architecture, and scope** in the context of the course.
- Apply **Architecture review** in a problem, implementation, experiment, or design decision.

- Define a feasible, testable product scope and explicit success thresholds before implementation.

#### Lessons

1. **Course introduction: Application Engineering Capstone** — `lesson`

   The capstone is the final project course in Application Engineering. You will combine frontend, backend, data, testing, deployment, observability, and production architecture into one coherent product. The project should be substantial enough to demonstrate professional engineering without relying on unnecessary architectural complexity.
2. **Requirements, user workflows, domain model, architecture, and scope** — `lesson`
3. **Problem framing and user research ethics** — `lesson`
4. **User stories, acceptance criteria and priority** — `lesson`
5. **Domain boundaries, architecture options and ADRs** — `lesson`
6. **Threat modeling and measurable nonfunctional goals** — `lesson`
7. **Architecture review** — `test`
8. **Convert a product idea into requirements and an architecture diagram** — `lab`

### Module 2 — Full-Stack Implementation

#### Outcomes

- Explain **Frontend, backend, database, authentication, and application workflows** in the context of the course.

- Deliver independently testable features spanning UI, API, state and persistent data.

#### Lessons

1. **Frontend, backend, database, authentication, and application workflows** — `lesson`
2. **Vertical-slice delivery and staging increments** — `lesson`
3. **Transactional state and data migration planning** — `lesson`
4. **Session, identity and application access policy** — `lesson`
5. **Background work and integration contract verification** — `lesson`
6. **Implementation checkpoint** — `test`
7. **Implement one complete vertical slice from UI interaction through persistence** — `lab`

### Module 3 — Quality, Reliability & Security

#### Outcomes

- Explain **Testing, validation, observability, secure configuration, resilience, and failure handling** in the context of the course.

- Show that security, accessibility, correctness and fault recovery are actively verified.

#### Lessons

1. **Testing, validation, observability, secure configuration, resilience, and failure handling** — `lesson`
2. **Security verification, threat response and accessibility** — `lesson`
3. **Test architecture, CI quality gates and code review** — `lesson`
4. **Structured telemetry and failure reproduction** — `lesson`
5. **Dependency outages, rollback and operational readiness** — `lesson`
6. **Production readiness checkpoint** — `test`
7. **Introduce a controlled failure and use logs/metrics to diagnose it** — `lab`

### Module 4 — Deployment & Performance

#### Outcomes

- Explain **CI/CD, deployment, monitoring, load testing, rollback, and operational documentation** in the context of the course.
- Apply **Release review** in a problem, implementation, experiment, or design decision.

- Operate a deployed product using observable service objectives and recovery evidence.

#### Lessons

1. **CI/CD, deployment, monitoring, load testing, rollback, and operational documentation** — `lesson`
2. **Repeatable deployment and release approvals** — `lesson`
3. **Performance workload design and measurable targets** — `lesson`
4. **Backup/restore and failed-release recovery** — `lesson`
5. **Observability dashboards and incident runbooks** — `lesson`
6. **Release review** — `test`
7. **Perform a load measurement, identify a bottleneck, and record the improvement** — `lab`

### Module 5 — Product Validation & Ethical Data Collection

#### Outcomes

- Validate a project requirement with reproducible and ethically collected user evidence.
- Adapt scope from feedback without hiding changes to acceptance criteria.

#### Lessons

1. **Research questions and representative users** — `lesson`
2. **Consent, privacy and low-risk research methods** — `lesson`
3. **Prototype feedback and evidence-driven scope changes** — `lesson`
4. **Accessible usability evaluation and product metrics** — `lesson`
5. **Assessing product assumptions and feedback quality** — `test`
6. **Run a scoped product validation exercise** — `lab`

### Module 6 — Privacy, Data Stewardship & Security Review

#### Outcomes

- Classify the project's sensitive data and justify how it is retained and protected.
- Demonstrate server-side authorization and a testable remediation for a high-priority threat.

#### Lessons

1. **Data classification and retention** — `lesson`
2. **Threat modeling across application boundaries** — `lesson`
3. **Least privilege and secret lifecycle** — `lesson`
4. **Dependency risk and supply-chain provenance** — `lesson`
5. **Security and privacy architecture review** — `test`
6. **Execute a security and retention test plan** — `lab`

### Module 7 — Production Operations & Disaster Recovery

#### Outcomes

- Define operational targets from user workflows and measure service health.
- Restore a failed deployment or data component from tested, documented procedures.

#### Lessons

1. **User-centered SLOs and health checks** — `lesson`
2. **Capacity and resource consumption budgets** — `lesson`
3. **Reliable backups, restores and migration recovery** — `lesson`
4. **Incident triage, on-call handoff and service runbooks** — `lesson`
5. **Operational risk and recovery planning** — `test`
6. **Rehearse an application outage and recovery** — `lab`

### Module 8 — Engineering Defense & Transfer

#### Outcomes

- Defend implementation choices against realistic alternatives using evidence.
- Make and explain an unfamiliar scoped change without abandoning project invariants.

#### Lessons

1. **Trade-off arguments and architectural alternatives** — `lesson`
2. **Reproducible demos and environment control** — `lesson`
3. **Independent change request and code explanation** — `lesson`
4. **Evidence indexing and technical retrospective** — `lesson`
5. **Project defense readiness and trade-off reasoning** — `test`
6. **Complete a transfer and reproducibility rehearsal** — `lab`

### Module 9 — Final Project Lab

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
**Expanded module assessments and practical work:**

- **Module 1 checkpoint and micro-lab:** Review signed-off acceptance criteria, scope exclusions, data model and architecture risks; demonstrate a trace from requirements to planned tests.
- **Module 2 checkpoint and micro-lab:** Prove a working vertical slice with realistic data and error-path tests, not only mock screens.
- **Module 3 checkpoint and micro-lab:** Demonstrate negative authorization, injected dependency outage and a regression test added after diagnosis.
- **Module 4 checkpoint and micro-lab:** Run a controlled incident drill showing deployment revision, detection, rollback/recovery and measured impact.

- **Module 5 — Product Validation & Ethical Data Collection (Run a scoped product validation exercise):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Conduct or simulate a documented moderated usability study on a prototype with a defined scenario and consent assumptions; synthesize observations and revise one requirement.
  - Verification: Show a trace from observations to a changed acceptance criterion and explicit limitations.
  - Evidence: Anonymized notes, usability tasks, change log and updated backlog.
  - Failure analysis: Identify selection bias, exposed personal data, misleading success metrics and scope creep.
- **Module 6 — Privacy, Data Stewardship & Security Review (Execute a security and retention test plan):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Create a project-specific threat model and attempt cross-user access, unsafe inputs and expired credentials in a controlled environment.
  - Verification: Record prevented attacks and verified retention/deletion behavior where applicable; repair at least one detected defect.
  - Evidence: Threat model, privacy inventory, authorization test suite and sanitised findings.
  - Failure analysis: Discuss leaked logs, broken tenant scoping, excessive data retention and secret exposure.
- **Module 7 — Production Operations & Disaster Recovery (Rehearse an application outage and recovery):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Induce a failed release and isolated data-service outage, measure impact and recover without undocumented steps.
  - Verification: Document detection, recovery time, data integrity and residual limitations against stated targets.
  - Evidence: Incident timeline, telemetry, runbook, backup/restore transcript.
  - Failure analysis: Identify false health checks, incompatible rollback and unrecoverable data scenarios.
- **Module 8 — Engineering Defense & Transfer (Complete a transfer and reproducibility rehearsal):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Have a reviewer or independent checklist reproduce the build and request a small change; make the change while maintaining critical tests and documentation.
  - Verification: Clean-checkout setup succeeds, a change is demonstrated, tests remain green, and limitations are explained.
  - Evidence: Reviewer checklist, release revision, change diff and defense notes.
  - Failure analysis: Address hidden dependencies, undocumented manual fixes, and unsupported performance claims.

**Exit assessment expectation:**

Demonstrate the relevant course outcomes on an unfamiliar scenario, including failure behavior and independently reproducible evidence. Checkpoint responses must explain mechanisms; every final lab or project must integrate and verify the expanded material.

**Project defense:**

The learner must:

1. demo the product using a realistic workflow;
2. explain its architecture and major trade-offs;
3. demonstrate the automated tests and deployment pipeline;
4. show one failure or performance problem and the evidence used to fix it;
5. explain what they would change at the next scale of usage.

This is the **Program 2 — APP graduation requirement**.
