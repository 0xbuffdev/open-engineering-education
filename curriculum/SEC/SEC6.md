# SEC6 — Cloud, Containers & Identity Security

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** SEC2, SEC4 and APP7 *(legacy mapping; reconcile before activation)*
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SEC.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Apply security engineering to modern deployment environments: containers, CI/CD, identities, permissions, cloud resources, secrets, and software supply chains.

## Learning outcomes

- Analyze identity, permission, and secret-management risks in cloud environments.
- Harden containers and deployment configurations.
- Apply least-privilege principles to service and CI/CD identities.
- Identify common software-supply-chain and secret-exposure risks.
- Review a deployed environment and produce actionable security improvements.

## Modules

### Module 1 — Isolation & Container Security

#### Outcomes

By the end of this module, the learner can:

- Explain **Linux and container isolation concepts** in the context of the course.
- Apply **Container images and runtime boundaries** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Linux and container isolation concepts** — `lesson`
2. **Container images and runtime boundaries** — `lesson`
3. **Checkpoint: container security** — `test`
4. **Micro-lab: Inspect an image and identify unnecessary privileges or components.** — `lab`

### Module 2 — Identity & Least Privilege

#### Outcomes

By the end of this module, the learner can:

- Explain **IAM and service identities** in the context of the course.
- Apply **Least privilege in cloud environments** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **IAM and service identities** — `lesson`
2. **Least privilege in cloud environments** — `lesson`
3. **Checkpoint: identity security** — `test`
4. **Micro-lab: Reduce a service identity to the permissions it actually needs.** — `lab`

### Module 3 — Secrets & Supply Chain

#### Outcomes

By the end of this module, the learner can:

- Explain **Secrets management** in the context of the course.
- Apply **Dependency and CI/CD supply-chain risks** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Secrets management** — `lesson`
2. **Dependency and CI/CD supply-chain risks** — `lesson`
3. **Checkpoint: supply-chain security** — `test`
4. **Micro-lab: Identify one credential or dependency risk in a sample pipeline.** — `lab`

### Module 4 — Cloud Attack Surfaces

#### Outcomes

By the end of this module, the learner can:

- Explain **Cloud network and configuration attack surfaces** in the context of the course.
- Apply **Secure deployment verification** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Cloud network and configuration attack surfaces** — `lesson`
2. **Secure deployment verification** — `lesson`
3. **Checkpoint: cloud security review** — `test`
4. **Micro-lab: Review an exposed deployment and verify each remediation.** — `lab`

### Module 5 — Secure Deployment Review

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Review identities, secrets, images, network exposure, permissions, and CI/CD security** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- Linux/container isolation
- container images
- secrets
- IAM
- least privilege
- service identities
- CI/CD security
- supply-chain risks
- cloud attack surfaces
- configuration management

### Labs

- inspect container permissions
- harden a container
- build an IAM policy
- detect leaked secrets
- secure a CI pipeline

### Substantial course lab

**Secure Deployment Review**

Deploy a small application and produce a security review covering identities, secrets, images, network exposure, permissions, and CI/CD.
