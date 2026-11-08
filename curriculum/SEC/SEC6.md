## SEC6 — Cloud, Containers & Identity Security

**Duration:** 5 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SEC2, SEC4 and APP7

### Overview

Apply security engineering to modern deployment environments: containers, CI/CD, identities, permissions, cloud resources, secrets, and software supply chains.

### Prerequisites

**SEC2 — Web & Application Security**
**SEC4 — Network & Infrastructure Security**
**APP7 — Deployment, Cloud & DevOps**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Analyze identity, permission, and secret-management risks in cloud environments.
- Harden containers and deployment configurations.
- Apply least-privilege principles to service and CI/CD identities.
- Identify common software-supply-chain and secret-exposure risks.
- Review a deployed environment and produce actionable security improvements.


### Modules

#### Module 1 — Isolation & Container Security



### Module outcomes

By the end of this module, the learner can:

- Explain **Linux and container isolation concepts** in the context of the course.
- Apply **Container images and runtime boundaries** in a problem, implementation, experiment, or design decision.

1. **Linux and container isolation concepts**
   - kind: `lesson`
2. **Container images and runtime boundaries**
   - kind: `lesson`
3. **Checkpoint: container security**
   - kind: `test`

4. **Micro-lab: Inspect an image and identify unnecessary privileges or components.**
   - kind: `lab`
#### Module 2 — Identity & Least Privilege



### Module outcomes

By the end of this module, the learner can:

- Explain **IAM and service identities** in the context of the course.
- Apply **Least privilege in cloud environments** in a problem, implementation, experiment, or design decision.

1. **IAM and service identities**
   - kind: `lesson`
2. **Least privilege in cloud environments**
   - kind: `lesson`
3. **Checkpoint: identity security**
   - kind: `test`

4. **Micro-lab: Reduce a service identity to the permissions it actually needs.**
   - kind: `lab`
#### Module 3 — Secrets & Supply Chain



### Module outcomes

By the end of this module, the learner can:

- Explain **Secrets management** in the context of the course.
- Apply **Dependency and CI/CD supply-chain risks** in a problem, implementation, experiment, or design decision.

1. **Secrets management**
   - kind: `lesson`
2. **Dependency and CI/CD supply-chain risks**
   - kind: `lesson`
3. **Checkpoint: supply-chain security**
   - kind: `test`

4. **Micro-lab: Identify one credential or dependency risk in a sample pipeline.**
   - kind: `lab`
#### Module 4 — Cloud Attack Surfaces



### Module outcomes

By the end of this module, the learner can:

- Explain **Cloud network and configuration attack surfaces** in the context of the course.
- Apply **Secure deployment verification** in a problem, implementation, experiment, or design decision.

1. **Cloud network and configuration attack surfaces**
   - kind: `lesson`
2. **Secure deployment verification**
   - kind: `lesson`
3. **Checkpoint: cloud security review**
   - kind: `test`

4. **Micro-lab: Review an exposed deployment and verify each remediation.**
   - kind: `lab`
#### Module 5 — Secure Deployment Review



1. **Review identities, secrets, images, network exposure, permissions, and CI/CD security**
   - kind: `lab`

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

---

