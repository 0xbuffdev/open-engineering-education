# SEC4 — Network & Infrastructure Security

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** SEC2 and SEF5 *(legacy mapping; reconcile before activation)*
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SEC.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Study service exposure, network segmentation, secure configuration, TLS, host hardening, secrets, and least privilege through controlled environments and authorized assessment.

## Learning outcomes

- Identify the attack surface of a networked service environment.
- Analyze service exposure, segmentation, and secure configuration.
- Harden hosts and services using least privilege and appropriate network controls.
- Use controlled evidence to validate whether a security control is effective.
- Produce a remediation-focused infrastructure security review.

## Modules

### Module 1 — Network Attack Surface

#### Outcomes

By the end of this module, the learner can:

- Explain **Services, ports, and exposed interfaces** in the context of the course.
- Apply **Service enumeration in authorized environments** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Services, ports, and exposed interfaces** — `lesson`
2. **Service enumeration in authorized environments** — `lesson`
3. **Checkpoint: network attack surface** — `test`
4. **Micro-lab: Inventory the attack surface of the provided training environment.** — `lab`

### Module 2 — Transport & Segmentation

#### Outcomes

By the end of this module, the learner can:

- Explain **TLS concepts and encrypted transport** in the context of the course.
- Apply **Network segmentation and firewalling** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **TLS concepts and encrypted transport** — `lesson`
2. **Network segmentation and firewalling** — `lesson`
3. **Checkpoint: network controls** — `test`
4. **Micro-lab: Model which traffic should be allowed between two isolated services.** — `lab`

### Module 3 — Service Hardening

#### Outcomes

By the end of this module, the learner can:

- Explain **Secure service configuration** in the context of the course.
- Apply **Least privilege and secrets** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Secure service configuration** — `lesson`
2. **Least privilege and secrets** — `lesson`
3. **Checkpoint: hardening** — `test`
4. **Micro-lab: Remove unnecessary permissions from a controlled service deployment.** — `lab`

### Module 4 — Logging & Verification

#### Outcomes

By the end of this module, the learner can:

- Explain **Security logging and verification** in the context of the course.
- Apply **Retesting hardened infrastructure** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Security logging and verification** — `lesson`
2. **Retesting hardened infrastructure** — `lesson`
3. **Checkpoint: evidence of hardening** — `test`
4. **Micro-lab: Verify that one intended attack path is no longer available.** — `lab`

### Module 5 — Hardened Service Environment

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Deploy, assess, harden, and verify the Hardened Service Environment** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- network attack surface
- service enumeration
- TLS concepts
- network segmentation
- firewalling
- secure service configuration
- infrastructure hardening
- secrets
- logging
- least privilege

### Labs

- inspect a local service
- harden a Linux host
- analyze network traffic
- test segmentation
- review service exposure

### Substantial course lab

**Hardened Service Environment**

Deploy a small service stack, document its attack surface, harden it, and verify the controls.
