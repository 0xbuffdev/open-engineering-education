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


### Modules

#### Module 1 — Network Attack Surface



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

