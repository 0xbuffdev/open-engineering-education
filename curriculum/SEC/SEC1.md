## SEC1 — Security Foundations & Threat Modeling

**Duration:** 5 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** Program 1 — SEF

### Overview

Establish the methods and rules used throughout the Security Engineering program. You will learn threat modeling, abuse cases, security requirements, and authorized-testing boundaries using real software systems as the subject of analysis.

### Prerequisites

**SEF — Software Engineering Foundations**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Identify assets, actors, trust boundaries, attack surfaces, and security assumptions.
- Create useful threat models and abuse cases for software systems.
- Translate threats into concrete security requirements and verification tests.
- Define clear rules of engagement for authorized security work.
- Communicate security risks in terms developers and system owners can act on.


### Resource map

**Required**

- **B40** Ch. 1–5 and 7–10 (first edition) — carried from ZtP D1.
- **B5** Ch. 8–9, 15, 17, 38 and 39 — carried from ZtP D1.
- **R31** OWASP Top 10:2025 — carried from ZtP D1 (“use the current OWASP Top 10”).
- **B41** Ch. 1–2 and 6 (What Is Security Engineering?; Who Is the Opponent?; Access Control) — added.

**Optional**

- **B40** Ch. 12 (Requirements Cookbook) · **R14** Threat Modeling cheat sheet.

### Modules

#### Module 1 — Security Fundamentals

**Reading:** **B40** Ch. 1 (Dive In and Threat Model!), Ch. 2 (Strategies for Threat Modeling). **B41** Ch. 1 (What Is Security Engineering?), Ch. 2 (Who Is the Opponent?). **R31** the introduction (what the risk categories are and how they were chosen).


### Module outcomes

By the end of this module, the learner can:

- Explain **Security principles and assets** in the context of the course.
- Apply **Trust boundaries and attack surface** in a problem, implementation, experiment, or design decision.

1. **Security principles and assets**
   - kind: `lesson`
2. **Trust boundaries and attack surface**
   - kind: `lesson`
3. **Checkpoint: security foundations**
   - kind: `test`

4. **Micro-lab: Draw trust boundaries for a small application.**
   - kind: `lab`
#### Module 2 — Identity & Access

**Reading:** **B5** Ch. 8 (Users and Groups), Ch. 9 (Process Credentials), Ch. 15 (File Attributes), Ch. 17 (Access Control Lists), Ch. 38 (Writing Secure Privileged Programs), Ch. 39 (Capabilities). **B41** Ch. 6 (Access Control). **R31** A01 Broken Access Control, A07 Authentication Failures.


### Module outcomes

By the end of this module, the learner can:

- Explain **Authentication and authorization** in the context of the course.
- Apply **Least privilege and security requirements** in a problem, implementation, experiment, or design decision.

1. **Authentication and authorization**
   - kind: `lesson`
2. **Least privilege and security requirements**
   - kind: `lesson`
3. **Checkpoint: access control**
   - kind: `test`

4. **Micro-lab: Identify one authorization requirement that must be enforced server-side.**
   - kind: `lab`
#### Module 3 — Threat Modeling

**Reading:** **B40** Ch. 3 (STRIDE), Ch. 4 (Attack Trees), Ch. 5 (Attack Libraries). *Optional:* **R14** Threat Modeling cheat sheet.


### Module outcomes

By the end of this module, the learner can:

- Explain **STRIDE and threat identification** in the context of the course.
- Apply **Abuse cases and attack paths** in a problem, implementation, experiment, or design decision.

1. **STRIDE and threat identification**
   - kind: `lesson`
2. **Abuse cases and attack paths**
   - kind: `lesson`
3. **Checkpoint: threat modeling**
   - kind: `test`

4. **Micro-lab: Turn an abuse case into a concrete security requirement.**
   - kind: `lab`
#### Module 4 — Verification & Risk Prioritization

**Reading:** **B40** Ch. 7 (Processing and Managing Threats), Ch. 8 (Defensive Tactics and Technologies), Ch. 9 (Trade-Offs When Addressing Threats), Ch. 10 (Validating That Threats Are Addressed).


### Module outcomes

By the end of this module, the learner can:

- Explain **Threat treatment and validation** in the context of the course.
- Apply **Prioritizing risks and security tests** in a problem, implementation, experiment, or design decision.

1. **Threat treatment and validation**
   - kind: `lesson`
2. **Prioritizing risks and security tests**
   - kind: `lesson`
3. **Checkpoint: security requirements**
   - kind: `test`

4. **Micro-lab: Convert the highest-risk threats into verification tests.**
   - kind: `lab`
#### Module 5 — Threat Model & Security Test Plan

**Reading:** **B40** Ch. 1–10 as the workflow; Ch. 12 (Requirements Cookbook). **R31** A06 Insecure Design. **R28** ASVS as a source of verifiable requirements.


1. **Produce and validate the Threat Model & Security Test Plan**
   - kind: `lab`

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

---

