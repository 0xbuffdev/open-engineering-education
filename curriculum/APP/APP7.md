# APP7 — Deployment, Cloud & DevOps

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP3](APP3.md), [APP6](APP6.md)
**Duration:** 9 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Learn the operational path from a working application to a service that can be released and recovered reliably. The course covers deployment environments, containers, networking, secrets, CI/CD, health checks, monitoring, rollback, and practical cloud services.

## Learning outcomes

By the end of this course, the learner will be able to:

- Package an application for reproducible deployment.
- Separate development, staging, and production configuration safely.
- Build automated build, test, and deployment pipelines.
- Operate HTTPS, health checks, logs, and basic monitoring in production.
- Perform and verify a rollback after a failed release.
- Reason about infrastructure choices, operational risk, and cost.
- Provision and reconstruct application environments declaratively while detecting drift and protecting infrastructure state.
- Restore stateful application data from a verified backup under stated recovery point and recovery time goals.
- Operate a deployment through monitored failure, incident diagnosis and safe recovery or rollback.
- Compare deployment services with documented capacity, security responsibility and ongoing cost assumptions.

## Modules

### Module 1 — Deployment Foundations

#### Outcomes

- Explain **Linux deployment and application processes** in the context of the course.
- Apply **Containers and container images** in a problem, implementation, experiment, or design decision.

- Package and run applications reproducibly with observable startup and shutdown behavior.

#### Lessons

1. **Course introduction: Deployment, Cloud & DevOps** — `lesson`

   Learn the operational path from a working application to a service that can be released and recovered reliably. The course covers deployment environments, containers, networking, secrets, CI/CD, health checks, monitoring, rollback, and practical cloud services.
2. **Linux deployment and application processes** — `lesson`
3. **Containers and container images** — `lesson`
4. **Container isolation and image layering** — `lesson`
5. **Multi-stage builds and supply-chain hygiene** — `lesson`
6. **Process supervision, signals and graceful shutdown** — `lesson`
7. **deployment basics** — `test`
8. **Containerize the application and inspect its runtime configuration** — `lab`

### Module 2 — Networking for Production

#### Outcomes

- Explain **Reverse proxies, DNS, and TLS operations** in the context of the course.
- Apply **Health checks and service exposure** in a problem, implementation, experiment, or design decision.

- Expose applications through explicit network boundaries and verify the entire client-to-service path.

#### Lessons

1. **Reverse proxies, DNS, and TLS operations** — `lesson`
2. **Health checks and service exposure** — `lesson`
3. **TCP ports, service discovery and load balancers** — `lesson`
4. **TLS certificates, trust, and renewal** — `lesson`
5. **Ingress, firewalls and application proxy headers** — `lesson`
6. **production networking** — `test`
7. **Place the service behind a reverse proxy and verify its health endpoint** — `lab`

### Module 3 — Environments & Secrets

#### Outcomes

- Explain **Development, staging, and production environments** in the context of the course.
- Apply **Secrets management and configuration separation** in a problem, implementation, experiment, or design decision.

- Keep secrets out of build artifacts and separate runtime configuration from code.

#### Lessons

1. **Development, staging, and production environments** — `lesson`
2. **Secrets management and configuration separation** — `lesson`
3. **Configuration lifecycle and environment parity** — `lesson`
4. **Secrets rotation and least privilege** — `lesson`
5. **Persistent state and encryption boundaries** — `lesson`
6. **configuration safety** — `test`
7. **Move sensitive configuration out of source control and rotate it** — `lab`

### Module 4 — CI/CD & Recovery

#### Outcomes

- Explain **Automated build, test, and deployment pipelines** in the context of the course.
- Apply **Deployment strategies, rollback, and cost awareness** in a problem, implementation, experiment, or design decision.

- Plan deployments that are observable and recoverable, including stateful changes.

#### Lessons

1. **Automated build, test, and deployment pipelines** — `lesson`
2. **Deployment strategies, rollback, and cost awareness** — `lesson`
3. **Continuous deployment controls and release approvals** — `lesson`
4. **Blue-green versus rolling releases** — `lesson`
5. **Database migration compatibility and rollback constraints** — `lesson`
6. **release operations** — `test`
7. **Perform a controlled rollback after a deliberately bad release** — `lab`

### Module 5 — Infrastructure as Code & Environment Provisioning

#### Outcomes

- Describe and verify reproducible infrastructure without undocumented manual configuration.
- Detect drift and evaluate infrastructure changes through reviewable plans.

#### Lessons

1. **Declarative infrastructure and desired state** — `lesson`
2. **Provisioning plans, drift and idempotency** — `lesson`
3. **Environment isolation and identity** — `lesson`
4. **Resource ownership, state protection and review** — `lesson`
5. **Infrastructure state and drift reasoning** — `test`
6. **Provision two equivalent deployment environments** — `lab`

### Module 6 — Persistent Data, Backups & Disaster Recovery

#### Outcomes

- Choose persistence and recovery approaches based on stated data loss and outage limits.
- Perform a tested restore with validated data integrity.

#### Lessons

1. **Volume/storage lifecycle and database persistence** — `lesson`
2. **Backup consistency and recovery point objectives** — `lesson`
3. **Restore testing and data integrity** — `lesson`
4. **Disaster scenarios and runbooks** — `lesson`
5. **Recovery objectives and failure scenarios** — `test`
6. **Restore a stateful application from backup** — `lab`

### Module 7 — Production Monitoring, SLOs & Incident Response

#### Outcomes

- Detect user-impacting production failures from actionable signals.
- Run a controlled incident response and demonstrate recovery with evidence.

#### Lessons

1. **Logs, metrics, traces and runtime health** — `lesson`
2. **SLOs and error-budget-aware operations** — `lesson`
3. **Alerting and escalation design** — `lesson`
4. **Post-incident repair and rollback drills** — `lesson`
5. **Monitoring signal and alert correctness** — `test`
6. **Run a release incident drill** — `lab`

### Module 8 — Cloud Services, Capacity & Cost

#### Outcomes

- Select deployment services using reliability, portability, security and cost constraints.
- Estimate steady-state and burst costs from explicit workloads.

#### Lessons

1. **Managed compute, data and object storage trade-offs** — `lesson`
2. **Capacity planning and autoscaling basics** — `lesson`
3. **Network egress and usage-based pricing** — `lesson`
4. **Security responsibilities and cost guardrails** — `lesson`
5. **Cloud service choice and cost assumptions** — `test`
6. **Evaluate a deployment cost and scale proposal** — `lab`

### Module 9 — Deployed Product

#### Outcomes

- Complete and explain the Deployed Product lab, demonstrating the applicable course outcomes and retaining required evidence.

#### Lessons

1. **Deploy, observe, and recover the Deployed Product** — `lab`

## Completion requirements

- Complete the required practical exercises, knowledge checkpoints, and evaluated labs described in the modules.
- Complete the final integrated `lab` in the last module and satisfy its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, failures investigated, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required practical exercises:**

- containerize the APP5 service
- configure staging and production
- automate deployment
- perform a rollback
- intentionally break a deployment and recover it
**Final integration lab — required work:**

Required artifact: **Deployed Product**.

Deploy the APP5 system to a real environment with automated build/test/deploy, HTTPS, configuration separation, health checks, logging, monitoring and a tested rollback procedure.

**Expanded module assessments and practical work:**

- **Module 1 checkpoint and micro-lab:** Build from a clean checkout, verify image provenance and show that the process handles termination cleanly.
- **Module 2 checkpoint and micro-lab:** Demonstrate HTTPS, valid health routing and rejection of untrusted forwarded client identity.
- **Module 3 checkpoint and micro-lab:** Show rotating one credential without data loss and verify no secret appears in repository or logs.
- **Module 4 checkpoint and micro-lab:** Prove the automated pipeline rejects a failing release and can restore a known-good application version.

- **Module 5 — Infrastructure as Code & Environment Provisioning (Provision two equivalent deployment environments):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Create a declarative local/cloud-sandbox environment, rebuild it from clean state, and compare expected and observed resources.
  - Verification: Re-running provisioning is idempotent; a deliberate drift produces a clear planned correction.
  - Evidence: Versioned configuration, safe plan, resource inventory and cleanup record.
  - Failure analysis: Explain secrets in state files, accidental deletion and shared environment leakage.
- **Module 6 — Persistent Data, Backups & Disaster Recovery (Restore a stateful application from backup):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Create a backup from a running test application, induce data loss in a disposable environment and restore to a verified state.
  - Verification: Check record counts and integrity, record measured recovery time and state any unavoidable data loss.
  - Evidence: Backup checksum, recovery transcript and RPO/RTO assumptions.
  - Failure analysis: Distinguish copies from usable backups, crash consistency and accidental restoration to the wrong environment.
- **Module 7 — Production Monitoring, SLOs & Incident Response (Run a release incident drill):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Deploy a defective release into a test environment, monitor errors and latency, trigger a diagnostic response and restore the prior version.
  - Verification: Show time to detect, time to recover, clear incident ownership and a regression check.
  - Evidence: Telemetry screenshots/queries, rollback revision and incident review.
  - Failure analysis: Identify false health signals, alert floods and unsafe rollback of incompatible data.
- **Module 8 — Cloud Services, Capacity & Cost (Evaluate a deployment cost and scale proposal):**
  - Prerequisites: Explain the module outcomes and complete the instructional lessons.
  - Environment: A controlled reproducible implementation or simulation with documented configuration and test data.
  - Required work: Compare two plausible deployment architectures for a documented workload, then run a small measured test to check an assumption.
  - Verification: Provide a bill-of-materials, capacity estimate and sensitivity analysis; no paid service is required.
  - Evidence: Service diagram, calculation, workload trace and decision note.
  - Failure analysis: Explain hidden network costs, autoscaling delay and shared-responsibility misunderstandings.

**Exit assessment expectation:**

Demonstrate the relevant course outcomes on an unfamiliar scenario, including failure behavior and independently reproducible evidence. Checkpoint responses must explain mechanisms; every final lab or project must integrate and verify the expanded material.

**Exit demonstration:**

The learner can ship a change through CI/CD, observe the deployment and recover from a failed release.

---
