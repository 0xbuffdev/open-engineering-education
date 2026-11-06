# APP7 — Deployment, Cloud & DevOps

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [APP3](APP3.md), [APP6](APP6.md)
**Duration:** 5 weeks
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

## Modules

### Module 1 — Deployment Foundations

#### Outcomes

- Explain **Linux deployment and application processes** in the context of the course.
- Apply **Containers and container images** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Course introduction: Deployment, Cloud & DevOps** — `lesson`

   Learn the operational path from a working application to a service that can be released and recovered reliably. The course covers deployment environments, containers, networking, secrets, CI/CD, health checks, monitoring, rollback, and practical cloud services.
2. **Linux deployment and application processes** — `lesson`
3. **Containers and container images** — `lesson`
4. **deployment basics** — `test`
5. **Containerize the application and inspect its runtime configuration** — `lab`

### Module 2 — Networking for Production

#### Outcomes

- Explain **Reverse proxies, DNS, and TLS operations** in the context of the course.
- Apply **Health checks and service exposure** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Reverse proxies, DNS, and TLS operations** — `lesson`
2. **Health checks and service exposure** — `lesson`
3. **production networking** — `test`
4. **Place the service behind a reverse proxy and verify its health endpoint** — `lab`

### Module 3 — Environments & Secrets

#### Outcomes

- Explain **Development, staging, and production environments** in the context of the course.
- Apply **Secrets management and configuration separation** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Development, staging, and production environments** — `lesson`
2. **Secrets management and configuration separation** — `lesson`
3. **configuration safety** — `test`
4. **Move sensitive configuration out of source control and rotate it** — `lab`

### Module 4 — CI/CD & Recovery

#### Outcomes

- Explain **Automated build, test, and deployment pipelines** in the context of the course.
- Apply **Deployment strategies, rollback, and cost awareness** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Automated build, test, and deployment pipelines** — `lesson`
2. **Deployment strategies, rollback, and cost awareness** — `lesson`
3. **release operations** — `test`
4. **Perform a controlled rollback after a deliberately bad release** — `lab`

### Module 5 — Deployed Product

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

**Exit demonstration:**

The learner can ship a change through CI/CD, observe the deployment and recover from a failed release.

---
