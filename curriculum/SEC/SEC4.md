## SEC4 — Network & Infrastructure Security

**Duration:** 5 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SEC2 and SEF5

**Recommended:** SYS4.

### Overview

Study service exposure, network segmentation, secure configuration, TLS, host hardening, secrets, and least privilege through controlled environments and authorized assessment.

### Prerequisites

**SEC2 — Web & Application Security**
**SEF5 — Low-Level Programming with C & Linux**
**Recommended:** SYS4.

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Identify the attack surface of a networked service environment.
- Analyze service exposure, segmentation, and secure configuration.
- Harden hosts and services using least privilege and appropriate network controls.
- Use controlled evidence to validate whether a security control is effective.
- Produce a remediation-focused infrastructure security review.


### Resource map

**Required**

- **B5** Ch. 37–39 and 56–63 — carried from ZtP D4.
- **R85** TryHackMe / Hack The Box — carried from ZtP D4 (authorized labs only).
- **B41** Ch. 10 and 21 · **B19** §8.6 and §8.9 · **R66** Nmap book · **R67** CIS Benchmarks · **R68** NIST SP 800-123 · **R70** NIST SP 800-52 Rev. 2 · **R69** NIST SP 800-92 — added.

### Modules

#### Module 1 — Network Attack Surface

**Reading:** **B5** Ch. 56 (Sockets: Introduction), Ch. 58 (Fundamentals of TCP/IP Networks), Ch. 59 (Internet Domains), Ch. 61 (Advanced Topics). **R66** Ch. 1 (Getting Started), Ch. 3 (Host Discovery), Ch. 4–5 (Port Scanning), Ch. 7 (Service and Application Version Detection) — authorized targets only. **B41** Ch. 21 (Network Attack and Defence).


### Module outcomes

By the end of this module, the learner can:

- Explain **Services, ports, and exposed interfaces** in the context of the course.
- Apply **Service enumeration in authorized environments** in a problem, implementation, experiment, or design decision.

1. **Services, ports, and exposed interfaces**
   - kind: `lesson`
2. **Service enumeration in authorized environments**
   - kind: `lesson`
3. **Checkpoint: network attack surface**
   - kind: `test`

4. **Micro-lab: Inventory the attack surface of the provided training environment.**
   - kind: `lab`
#### Module 2 — Transport & Segmentation

**Reading:** **B19** §8.6 (Securing TCP Connections: TLS), §8.9 (Operational Security: Firewalls and Intrusion Detection Systems). **B20** Ch. 4. **R70** NIST SP 800-52 Rev. 2. **B41** Ch. 10 (Boundaries). **R22** Mozilla Server-Side TLS.


### Module outcomes

By the end of this module, the learner can:

- Explain **TLS concepts and encrypted transport** in the context of the course.
- Apply **Network segmentation and firewalling** in a problem, implementation, experiment, or design decision.

1. **TLS concepts and encrypted transport**
   - kind: `lesson`
2. **Network segmentation and firewalling**
   - kind: `lesson`
3. **Checkpoint: network controls**
   - kind: `test`

4. **Micro-lab: Model which traffic should be allowed between two isolated services.**
   - kind: `lab`
#### Module 3 — Service Hardening

**Reading:** **B5** Ch. 37 (Daemons), Ch. 38 (Writing Secure Privileged Programs), Ch. 39 (Capabilities). **R67** CIS Benchmarks for the host OS. **R68** NIST SP 800-123. **R14** Secrets Management cheat sheet.


### Module outcomes

By the end of this module, the learner can:

- Explain **Secure service configuration** in the context of the course.
- Apply **Least privilege and secrets** in a problem, implementation, experiment, or design decision.

1. **Secure service configuration**
   - kind: `lesson`
2. **Least privilege and secrets**
   - kind: `lesson`
3. **Checkpoint: hardening**
   - kind: `test`

4. **Micro-lab: Remove unnecessary permissions from a controlled service deployment.**
   - kind: `lab`
#### Module 4 — Logging & Verification

**Reading:** **R69** NIST SP 800-92. **R14** Logging cheat sheet. **R31** A09 Security Logging and Alerting Failures. **R66** Ch. 9 (Nmap Scripting Engine) for repeatable verification.


### Module outcomes

By the end of this module, the learner can:

- Explain **Security logging and verification** in the context of the course.
- Apply **Retesting hardened infrastructure** in a problem, implementation, experiment, or design decision.

1. **Security logging and verification**
   - kind: `lesson`
2. **Retesting hardened infrastructure**
   - kind: `lesson`
3. **Checkpoint: evidence of hardening**
   - kind: `test`

4. **Micro-lab: Verify that one intended attack path is no longer available.**
   - kind: `lab`
#### Module 5 — Hardened Service Environment

**Reading:** **R85** the matching lab environments. Apply Modules 1–4.


1. **Deploy, assess, harden, and verify the Hardened Service Environment**
   - kind: `lab`

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

---

