# APP16 — Platform Engineering

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP6](APP6.md), [APP7](APP7.md)
**Duration:** 8 weeks
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
- Build a discoverable internal service catalogue with verifiable ownership and self-service documentation.
- Promote immutable artifacts through controlled environments with least-privilege policy enforcement.
- Measure platform reliability, developer adoption, operational cost and service lifecycle obligations.
- Demonstrate recovery from failed provisioning or deployment without undocumented privileged manual steps.

## Modules

### Module 1 — Platform Boundaries & Developer Experience

#### Outcomes

- Define platform consumers, supported workflows and ownership.
- Measure developer friction with representative tasks and feedback.

- Select platform capabilities from observed developer needs, not tool fashion.

#### Lessons

1. **Course introduction: Platform Engineering** — `lesson`

   Design self-service development infrastructure that reduces delivery friction without hiding operational risk. Build a small, documented internal platform with reproducible environments, paved-road templates, deployment automation, policy controls and feedback from developer experience.
2. **Internal platforms, products and paved roads** — `lesson`
3. **Service catalogs and developer workflow mapping** — `lesson`
4. **Developer personas and support boundaries** — `lesson`
5. **Value stream mapping and platform success metrics** — `lesson`
6. **Platform APIs and golden-path responsibilities** — `lesson`
7. **Evaluating platform value** — `test`
8. **Benchmark developer onboarding** — `lab`

### Module 2 — Templates & Reproducible Environments

#### Outcomes

- Specify golden-path templates without locking out justified deviations.
- Provision development environments idempotently and document dependencies.

- Provision developer environments without hidden manual steps or unmanaged drift.

#### Lessons

1. **Project scaffolds and versioned templates** — `lesson`
2. **Infrastructure-as-code concepts and environment parity** — `lesson`
3. **Declarative infrastructure and reproducible builds** — `lesson`
4. **Template upgrades and backward compatibility** — `lesson`
5. **Ephemeral preview environments and cleanup** — `lesson`
6. **Choosing reusable platform contracts** — `test`
7. **Provision a repeatable environment** — `lab`

### Module 3 — Self-Service Delivery & Security

#### Outcomes

- Apply least privilege to platform credentials and service actions.
- Expose a testable pipeline with approval and rollback controls.

- Design developer self-service that preserves privileged-operation boundaries.

#### Lessons

1. **CI/CD service interfaces and deployment automation** — `lesson`
2. **Secrets, policy checks and audit trails** — `lesson`
3. **Self-service authorization and audit trails** — `lesson`
4. **Credential rotation and workload identity** — `lesson`
5. **Deployment approvals, policy checks and rollback** — `lesson`
6. **Assessing self-service permissions** — `test`
7. **Gate a deployment workflow** — `lab`

### Module 4 — Reliability, Governance & Economics

#### Outcomes

- Define operational ownership and SLOs for a platform service.
- Track availability, cost and support burden alongside usage.

- Operate a platform component as a product with measurable reliability and user feedback.

#### Lessons

1. **Platform SLOs and incident operations** — `lesson`
2. **Cost visibility, lifecycle and deprecation** — `lesson`
3. **Operational ownership and incident response** — `lesson`
4. **Reliability targets, platform telemetry and usability** — `lesson`
5. **Platform deprecation and cost allocation** — `lesson`
6. **Platform versus team trade-offs** — `test`
7. **Investigate a broken platform path** — `lab`

### Module 5 — Developer Portals & Service Catalogues

#### Outcomes

- Provide discoverable service ownership and self-service documentation.
- Validate whether a developer portal improves a real task rather than adding an extra interface.

#### Lessons

1. **Service ownership metadata and lifecycle** — `lesson`
2. **Backstage-style portal patterns without vendor lock-in** — `lesson`
3. **Platform API design and templates** — `lesson`
4. **Searchability, documentation and support loops** — `lesson`
5. **Service catalog usability and ownership** — `test`
6. **Build a minimal internal service catalogue** — `lab`

### Module 6 — Multi-Environment Delivery & Policy

#### Outcomes

- Promote the same tested artifact across environments with explicit policy controls.
- Detect configuration drift and preserve audit evidence during deployment.

#### Lessons

1. **Promotion chains and artifact immutability** — `lesson`
2. **Environment policies and drift detection** — `lesson`
3. **Secrets delivery with least privilege** — `lesson`
4. **Approvals, change windows and rollback constraints** — `lesson`
5. **Artifact provenance and environment promotion** — `test`
6. **Enforce a guarded release path** — `lab`

### Module 7 — Platform Reliability & Adoption Economics

#### Outcomes

- Evaluate platform reliability and value using credible operational and developer metrics.
- Justify expansion or deprecation of an abstraction with cost and ownership evidence.

#### Lessons

1. **Service-level objectives for developer workflows** — `lesson`
2. **Cost attribution and capacity planning** — `lesson`
3. **Adoption, satisfaction and support toil metrics** — `lesson`
4. **Platform lifecycle and deprecation planning** — `lesson`
5. **Platform SLO and adoption decisions** — `test`
6. **Conduct a platform service review** — `lab`

### Module 8 — Self-Service Application Platform Slice

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

**Expanded module assessment and lab requirements:**

- **Module 1 checkpoint and micro-lab:** Measure existing onboarding work and specify a testable reduction in effort and failure rate.
- **Module 2 checkpoint and micro-lab:** Rebuild a template from clean state and show controlled upgrade/recovery.
- **Module 3 checkpoint and micro-lab:** Demonstrate an unauthorized deployment denied by policy and a valid release with complete audit data.
- **Module 4 checkpoint and micro-lab:** Record failure detection, recovery, cost assumptions and developer experience in a reviewable report.

- **Module 5 — Developer Portals & Service Catalogues (Build a minimal internal service catalogue):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Represent a few services with ownership, runtime, dependencies and runbooks, then execute a common onboarding workflow through the catalogue.
  - Verification: Users can locate the owner, environment and reproducible setup steps without privileged access.
  - Evidence: Catalog schema, user-task record and ownership validation.
  - Failure analysis: Explain stale metadata, unknown ownership and over-coupled portal abstractions.
- **Module 6 — Multi-Environment Delivery & Policy (Enforce a guarded release path):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Build once, promote through two simulated environments, reject an unauthorized change and recover after a bad configuration.
  - Verification: Show identical artifact hashes, policy-denied attempts and tested rollback behavior.
  - Evidence: Release manifests, policy logs, approval records and config diff.
  - Failure analysis: Explain credential sprawl, mutable release tags and unreviewed production drift.
- **Module 7 — Platform Reliability & Adoption Economics (Conduct a platform service review):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Measure a template/provisioning workflow under a failure scenario, estimate operating cost, and propose a bounded improvement plan.
  - Verification: Present SLO data, cost model, incident notes and a prioritized decision tied to developer outcomes.
  - Evidence: Metrics, baseline/after comparison, cost assumptions and proposal.
  - Failure analysis: Explain vanity adoption metrics, unbudgeted support toil and hidden vendor dependencies.

**Exit assessment expectation:**

Demonstrate the subject outcomes on an unfamiliar example, show at least one negative path and retain evidence allowing another reviewer to reproduce the result. Checkpoint answers must explain mechanisms, while the final integration lab must integrate and verify the expanded topics.

**Exit demonstration:**

Demonstrate the resulting implementation, explain its key mechanisms, reproduce at least one failure and recovery and defend the chosen trade-offs with inspectable evidence.
