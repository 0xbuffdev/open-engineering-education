# APP16 — Platform Engineering

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP6](APP6.md), [APP7](APP7.md)
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Design self-service development infrastructure that reduces delivery friction without hiding operational risk. Build a small, documented internal platform with reproducible environments, paved-road templates, deployment automation, policy controls and feedback from developer experience.

This specialization is optional and not required for APP9 or APP graduation.

## Learning outcomes

By the end of this course, the learner will be able to:

- Identify developer workflow bottlenecks and define measurable platform-service goals.
- Provide reproducible application scaffolding and safe environment provisioning.
- Design self-service deployment workflows with access controls, secrets management and auditability.
- Implement platform observability, reliability boundaries and incident recovery.
- Evaluate developer adoption, cost and operational burden before expanding abstraction layers.

## Modules

### Module 1 — Platform Boundaries & Developer Experience

#### Outcomes

- Define platform consumers, supported workflows and ownership.
- Measure developer friction with representative tasks and feedback.

#### Lessons

1. **Course introduction: Platform Engineering** — `lesson`

   Design self-service development infrastructure that reduces delivery friction without hiding operational risk. Build a small, documented internal platform with reproducible environments, paved-road templates, deployment automation, policy controls and feedback from developer experience.
2. **Internal platforms, products and paved roads** — `lesson`
3. **Service catalogs and developer workflow mapping** — `lesson`
4. **Evaluating platform value** — `test`
5. **Benchmark developer onboarding** — `lab`

### Module 2 — Templates & Reproducible Environments

#### Outcomes

- Specify golden-path templates without locking out justified deviations.
- Provision development environments idempotently and document dependencies.

#### Lessons

1. **Project scaffolds and versioned templates** — `lesson`
2. **Infrastructure-as-code concepts and environment parity** — `lesson`
3. **Choosing reusable platform contracts** — `test`
4. **Provision a repeatable environment** — `lab`

### Module 3 — Self-Service Delivery & Security

#### Outcomes

- Apply least privilege to platform credentials and service actions.
- Expose a testable pipeline with approval and rollback controls.

#### Lessons

1. **CI/CD service interfaces and deployment automation** — `lesson`
2. **Secrets, policy checks and audit trails** — `lesson`
3. **Assessing self-service permissions** — `test`
4. **Gate a deployment workflow** — `lab`

### Module 4 — Reliability, Governance & Economics

#### Outcomes

- Define operational ownership and SLOs for a platform service.
- Track availability, cost and support burden alongside usage.

#### Lessons

1. **Platform SLOs and incident operations** — `lesson`
2. **Cost visibility, lifecycle and deprecation** — `lesson`
3. **Platform versus team trade-offs** — `test`
4. **Investigate a broken platform path** — `lab`

### Module 5 — Self-Service Application Platform Slice

#### Outcomes

- Integrate the elective's techniques in a working and verifiable application change or system.
- Evaluate correctness, operational limitations and trade-offs through reproducible evidence.

#### Lessons

1. **Self-Service Application Platform Slice** — `lab`

## Completion requirements

- Complete the required module checkpoints and practical exercises, then complete the final integration lab.
- State tools, versions, system assumptions and test data for reproducibility.
- Retain artifacts, test results, design decisions, an investigated failure and a technical retrospective in accordance with [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required module checkpoints and practical work:**

- **Module 1 — Platform Boundaries & Developer Experience:** Pass `Evaluating platform value` by explaining and applying the module outcomes; perform the `Benchmark developer onboarding` lab: Time a manual service setup, document failure points and define a measurable improvement target. Retain Baseline task recording, friction log and platform service goal.
- **Module 2 — Templates & Reproducible Environments:** Pass `Choosing reusable platform contracts` by explaining and applying the module outcomes; perform the `Provision a repeatable environment` lab: Create a minimal service template and automated local/test environment bootstrap, then rebuild from a clean state. Retain Template version, bootstrap logs and clean-rebuild tests.
- **Module 3 — Self-Service Delivery & Security:** Pass `Assessing self-service permissions` by explaining and applying the module outcomes; perform the `Gate a deployment workflow` lab: Implement a self-service deployment with a policy check, denied-action test and documented manual recovery. Retain Workflow run, authorization matrix and audit record.
- **Module 4 — Reliability, Governance & Economics:** Pass `Platform versus team trade-offs` by explaining and applying the module outcomes; perform the `Investigate a broken platform path` lab: Inject a failed provisioning or deployment action, triage from telemetry and publish a recovery playbook. Retain Failure traces, recovery time and change record.

**Final integration lab — Self-Service Application Platform Slice:**

Deliver one self-service workflow for a small application team: a versioned service template, repeatable development environment, gated deployment, basic observability and a documented failure-recovery path. Validate value through at least one representative user workflow, without requiring a commercial cloud.

**Success criteria:**

- Demonstrate complete setup and deployment from a clean checkout without hidden credentials or steps.
- Enforce role-appropriate access controls and show an unauthorized operation being rejected.
- Recover from a failed workflow, retaining logs and audit evidence.
- Compare the workflow with its baseline, including operational cost and adoption limitations.

**Evidence to retain:**

- Version-controlled implementation and configuration, including clean-rebuild instructions.
- Inputs and repeatable tests, output or measurements, and failure/recovery records.
- Trade-off analysis, limitations and technical retrospective.

**Failure analysis:**

Analyze snowflake environments, overprivileged automation, secret exposure, opaque self-service errors and platforms whose maintenance cost exceeds demonstrated benefit.

**Exit demonstration:**

Demonstrate the resulting implementation, explain its key mechanisms, reproduce at least one failure and recovery and defend the chosen trade-offs with inspectable evidence.
