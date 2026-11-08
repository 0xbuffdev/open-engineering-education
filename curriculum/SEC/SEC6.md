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


### Resource map

**Required**

- **B44** Ch. 1–4, 6–7 and 9–16 (2nd-edition numbering) · **B43** Ch. 5, 6 and 14 · **R72** NIST SP 800-190.
- **R77** SLSA · **R78** OWASP Top 10 CI/CD Security Risks · **R79** AWS IAM documentation (or your cloud's equivalent) · **R14** Secrets Management cheat sheet.
- **B5** Ch. 39 (Capabilities).

### Modules

#### Module 1 — Isolation & Container Security

**Reading:** **B44** Ch. 2 (Linux System Calls, Permissions and Capabilities), Ch. 3 (Control Groups), Ch. 4 (Container Isolation), Ch. 6 (Container Images), Ch. 10 (Strengthening Container Isolation). **R72** NIST SP 800-190 (image, registry, orchestrator, container and host-OS risks). **B5** Ch. 39.


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

**Reading:** **R79** Security best practices in IAM; Policy evaluation logic. **B43** Ch. 5 (Design for Least Privilege). **R31** A01 Broken Access Control.


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

**Reading:** **B44** Ch. 14 (Passing Secrets to Containers), Ch. 7 (Supply Chain Security), Ch. 9 (Infrastructure as Code and GitOps). **R14** Secrets Management cheat sheet. **R77** SLSA requirements and provenance levels. **R78** OWASP Top 10 CI/CD Security Risks. **B43** Ch. 14 (Deploying Code). **R31** A03 Software Supply Chain Failures.


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

**Reading:** **B44** Ch. 11 (Breaking Container Isolation), Ch. 12 (Container Network Security), Ch. 13 (Securely Connecting Components). **R67** CIS Benchmarks (container, Kubernetes and cloud baselines). **R31** A02 Security Misconfiguration.


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

**Reading:** **B44** Ch. 1 (Container Security Threats), Ch. 15 (Container Runtime Protection), Ch. 16 (Containers and the OWASP Top 10). **R72** and **R77** as the review checklists.


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

