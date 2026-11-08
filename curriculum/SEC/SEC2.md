## SEC2 — Web & Application Security

**Duration:** 6 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SEC1, APP1 and APP3

### Overview

Examine the security properties of HTTP applications, sessions, authentication, authorization, validation, and APIs. Learners use deliberately vulnerable environments to understand failures, implement fixes, and add regression tests.

### Prerequisites

**SEC1 — Security Foundations & Threat Modeling**
**APP1 — Web & Internet Foundations**
**APP3 — Backend Engineering & API Design**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Recognize common web and API security weaknesses and their underlying causes.
- Safely reproduce representative vulnerabilities in authorized training environments.
- Design and implement effective application-level mitigations.
- Verify security fixes with regression tests.
- Explain why client-side validation cannot enforce authorization or trust boundaries.


### Resource map

**Required**

- **R32** Web Security Academy — SQL injection; Authentication; Access control; Cross-site scripting; CSRF; SSRF; File upload vulnerabilities; API testing; Path traversal; OS command injection — carried from ZtP D3.
- **R31** OWASP Top 10:2025 — carried from ZtP D3 · **R29** WSTG · **R28** ASVS · **R30** API Security Top 10 (2023).
- **B5** Ch. 38 — carried from ZtP D3 (its Ch. 56–61 are used in SEC4).
- **R14** the cheat sheet for each remediation · **R84** OWASP Juice Shop for the local lab.

### Modules

#### Module 1 — Web Trust & Identity

**Reading:** **R32** Authentication; Access control. **R31** A01 Broken Access Control, A07 Authentication Failures. **R14** Session Management; Authorization cheat sheets. **R29** Authentication and Authorization testing.


### Module outcomes

By the end of this module, the learner can:

- Explain **HTTP, sessions, and cookies** in the context of the course.
- Apply **Authentication and authorization failures** in a problem, implementation, experiment, or design decision.

1. **HTTP, sessions, and cookies**
   - kind: `lesson`
2. **Authentication and authorization failures**
   - kind: `lesson`
3. **Checkpoint: web identity**
   - kind: `test`

4. **Micro-lab: Trace an authorization decision and identify where enforcement belongs.**
   - kind: `lab`
#### Module 2 — Input & Injection Attacks

**Reading:** **R32** SQL injection; Cross-site scripting; CSRF; OS command injection. **R31** A05 Injection. **R14** SQL Injection Prevention; Cross Site Scripting Prevention; CSRF Prevention; Input Validation.


### Module outcomes

By the end of this module, the learner can:

- Explain **Input validation and injection** in the context of the course.
- Apply **XSS and CSRF** in a problem, implementation, experiment, or design decision.

1. **Input validation and injection**
   - kind: `lesson`
2. **XSS and CSRF**
   - kind: `lesson`
3. **Checkpoint: injection and browser attacks**
   - kind: `test`

4. **Micro-lab: Use a controlled lab input to demonstrate why output encoding matters.**
   - kind: `lab`
#### Module 3 — Server-Side Application Risks

**Reading:** **R32** SSRF; File upload vulnerabilities; Path traversal; API testing. **R30** API Security Top 10 (2023). **R14** SSRF Prevention; File Upload.


### Module outcomes

By the end of this module, the learner can:

- Explain **SSRF and insecure file handling** in the context of the course.
- Apply **API security and access-control failures** in a problem, implementation, experiment, or design decision.

1. **SSRF and insecure file handling**
   - kind: `lesson`
2. **API security and access-control failures**
   - kind: `lesson`
3. **Checkpoint: application attack paths**
   - kind: `test`

4. **Micro-lab: Write a regression test for an authorization boundary.**
   - kind: `lab`
#### Module 4 — Secure Repair & Regression

**Reading:** **R28** ASVS — verification requirements as the regression checklist. **R29** WSTG testing methodology. **B5** Ch. 38 (Writing Secure Privileged Programs). **R31** A10 Mishandling of Exceptional Conditions.


### Module outcomes

By the end of this module, the learner can:

- Explain **Secure coding and remediation** in the context of the course.
- Apply **Security regression testing** in a problem, implementation, experiment, or design decision.

1. **Secure coding and remediation**
   - kind: `lesson`
2. **Security regression testing**
   - kind: `lesson`
3. **Checkpoint: secure remediation**
   - kind: `test`

4. **Micro-lab: Verify that a repaired vulnerability remains fixed after refactoring.**
   - kind: `lab`
#### Module 5 — Secure Web Application

**Reading:** **R84** Juice Shop (or another deliberately vulnerable app you run locally). **R32** labs for the chosen flaws. **R29** WSTG for evidence and reporting.


1. **Demonstrate selected flaws in a local application, repair them, and add regression tests**
   - kind: `lab`

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

---

