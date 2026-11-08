# SEC1 — Security Foundations & Threat Modeling

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** Program 1 — SEF *(legacy mapping; reconcile before activation)*
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SEC.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Establish the methods and rules used throughout the Security Engineering program. You will learn threat modeling, abuse cases, security requirements, and authorized-testing boundaries using real software systems as the subject of analysis.

## Learning outcomes

- Identify assets, actors, trust boundaries, attack surfaces, and security assumptions.
- Create useful threat models and abuse cases for software systems.
- Translate threats into concrete security requirements and verification tests.
- Define clear rules of engagement for authorized security work.
- Communicate security risks in terms developers and system owners can act on.

## Modules

### Module 1 — Security Fundamentals

#### Outcomes

By the end of this module, the learner can:

- Explain **Security principles and assets** in the context of the course.
- Apply **Trust boundaries and attack surface** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Security principles and assets** — `lesson`
2. **Trust boundaries and attack surface** — `lesson`
3. **Checkpoint: security foundations** — `test`
4. **Micro-lab: Draw trust boundaries for a small application.** — `lab`

### Module 2 — Identity & Access

#### Outcomes

By the end of this module, the learner can:

- Explain **Authentication and authorization** in the context of the course.
- Apply **Least privilege and security requirements** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Authentication and authorization** — `lesson`
2. **Least privilege and security requirements** — `lesson`
3. **Checkpoint: access control** — `test`
4. **Micro-lab: Identify one authorization requirement that must be enforced server-side.** — `lab`

### Module 3 — Threat Modeling

#### Outcomes

By the end of this module, the learner can:

- Explain **STRIDE and threat identification** in the context of the course.
- Apply **Abuse cases and attack paths** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **STRIDE and threat identification** — `lesson`
2. **Abuse cases and attack paths** — `lesson`
3. **Checkpoint: threat modeling** — `test`
4. **Micro-lab: Turn an abuse case into a concrete security requirement.** — `lab`

### Module 4 — Verification & Risk Prioritization

#### Outcomes

By the end of this module, the learner can:

- Explain **Threat treatment and validation** in the context of the course.
- Apply **Prioritizing risks and security tests** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Threat treatment and validation** — `lesson`
2. **Prioritizing risks and security tests** — `lesson`
3. **Checkpoint: security requirements** — `test`
4. **Micro-lab: Convert the highest-risk threats into verification tests.** — `lab`

### Module 5 — Threat Model & Security Test Plan

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Produce and validate the Threat Model & Security Test Plan** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- security principles
- assets
- trust boundaries
- authentication
- authorization
- attack surface
- STRIDE
- abuse cases
- threat modeling
- security requirements
- OWASP concepts

### Labs

- model an existing application
- identify trust boundaries
- write abuse cases
- translate threats into tests

### Substantial course lab

**Threat Model & Security Test Plan**

Take a real project and create a security model whose highest-risk threats become testable requirements.
