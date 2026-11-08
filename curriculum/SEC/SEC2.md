# SEC2 — Web & Application Security

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** SEC1, APP1 and APP3 *(legacy mapping; reconcile before activation)*
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SEC.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Examine the security properties of HTTP applications, sessions, authentication, authorization, validation, and APIs. Learners use deliberately vulnerable environments to understand failures, implement fixes, and add regression tests.

## Learning outcomes

- Recognize common web and API security weaknesses and their underlying causes.
- Safely reproduce representative vulnerabilities in authorized training environments.
- Design and implement effective application-level mitigations.
- Verify security fixes with regression tests.
- Explain why client-side validation cannot enforce authorization or trust boundaries.

## Modules

### Module 1 — Web Trust & Identity

#### Outcomes

By the end of this module, the learner can:

- Explain **HTTP, sessions, and cookies** in the context of the course.
- Apply **Authentication and authorization failures** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **HTTP, sessions, and cookies** — `lesson`
2. **Authentication and authorization failures** — `lesson`
3. **Checkpoint: web identity** — `test`
4. **Micro-lab: Trace an authorization decision and identify where enforcement belongs.** — `lab`

### Module 2 — Input & Injection Attacks

#### Outcomes

By the end of this module, the learner can:

- Explain **Input validation and injection** in the context of the course.
- Apply **XSS and CSRF** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Input validation and injection** — `lesson`
2. **XSS and CSRF** — `lesson`
3. **Checkpoint: injection and browser attacks** — `test`
4. **Micro-lab: Use a controlled lab input to demonstrate why output encoding matters.** — `lab`

### Module 3 — Server-Side Application Risks

#### Outcomes

By the end of this module, the learner can:

- Explain **SSRF and insecure file handling** in the context of the course.
- Apply **API security and access-control failures** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **SSRF and insecure file handling** — `lesson`
2. **API security and access-control failures** — `lesson`
3. **Checkpoint: application attack paths** — `test`
4. **Micro-lab: Write a regression test for an authorization boundary.** — `lab`

### Module 4 — Secure Repair & Regression

#### Outcomes

By the end of this module, the learner can:

- Explain **Secure coding and remediation** in the context of the course.
- Apply **Security regression testing** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Secure coding and remediation** — `lesson`
2. **Security regression testing** — `lesson`
3. **Checkpoint: secure remediation** — `test`
4. **Micro-lab: Verify that a repaired vulnerability remains fixed after refactoring.** — `lab`

### Module 5 — Secure Web Application

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Demonstrate selected flaws in a local application, repair them, and add regression tests** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- HTTP
- sessions
- cookies
- authentication
- authorization
- input validation
- injection
- XSS
- CSRF
- SSRF
- insecure file handling
- access-control failures
- secure API design

### Labs

Use PortSwigger/OWASP-style labs and a local vulnerable application.

### Substantial course lab

**Secure Web Application**

Start with a deliberately vulnerable local application, demonstrate selected vulnerabilities, fix them, and add regression tests.
