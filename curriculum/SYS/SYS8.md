# SYS8 — Systems Design & Production Engineering

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** [SYS6](SYS6.md), [SYS7](SYS7.md)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional)

> [Systems Engineering](README.md) · [Course format](../../spec/course-format.md) · [Design guide](../DESIGN-GUIDE.md)

## Overview

Use independently verified systems competence to design, harden and hand over an **operable service** under explicit reliability, security, resource and staffing constraints. SYS6 provides distributed-failure reasoning and SYS7 provides measurement discipline. This course does not reproduce APP product UI, web-framework deployment or generic DevOps tutorials; it owns system-level SLO, capacity, failure-domain, packaging, release/rollback and incident readiness judgments. The reference assessment hardens an earlier SYS4/SYS6 service in a free nonprivileged local environment using synthetic incidents. A full cloud deployment or an actual on-call rotation is not a prerequisite. Document what cannot be established without production traffic or an independent failure domain.

## Learning outcomes

- **SYS8-O1:** Translate a systems brief into measurable functional requirements, workload assumptions and reliability/capacity targets.
- **SYS8-O2:** Select component boundaries, communication, persistence and consistency trade-offs from declared failure and resource constraints.
- **SYS8-O3:** Design explicit failure domains, redundancy, retries, circuit breaking and graceful degradation without inventing availability guarantees.
- **SYS8-O4:** Define service-level indicators, objectives and error-budget or risk policies appropriate to a bounded operating context.
- **SYS8-O5:** Estimate CPU, memory, disk, network and queue capacity from measured demand and include justified safety margins.
- **SYS8-O6:** Design secure nonprivileged configuration, secrets handling, limits and change-control policies for a systems component.
- **SYS8-O7:** Specify reproducible packaging, startup, readiness, health, deploy, rollback and version-compatibility behavior.
- **SYS8-O8:** Design actionable monitoring, incident detection, escalation and operator procedures using diagnosable service signals.
- **SYS8-O9:** Conduct risk-driven load, soak, fault and recovery exercises with independent safety and acceptance oracles.
- **SYS8-O10:** Compare architecture alternatives by total operational complexity, cost, performance and failure consequences.
- **SYS8-O11:** Perform an independent production-readiness review, documenting unresolved risks and legitimate release blockers.
- **SYS8-O12:** Defend a revised systems architecture after an unfamiliar failure, capacity or operational constraint.

## Modules

### Module 1 — Requirements, Workloads and Service Contracts

#### Outcomes

- SYS8-O1
- SYS8-O2
- SYS8-O4

#### Lessons

1. **Systems design versus diagrams** — Start from a specific service and user-visible effects, not a template of microservices.
2. **Workload characterization** — Describe requests, concurrency, read/write mix, payloads and meaningful failure demand.
3. **Reliability definitions** — Distinguish availability, correctness, durability, recovery objectives and maintenance windows.
4. **Service-level indicators** — Define a measurement and counting policy for success, errors, latency and freshness.
5. **Error-budget reasoning** — Translate an SLO into a bounded operational decision; avoid universal SLO percentages.
6. **Constraint register** — Identify device, network, deployment, budget, access, privacy and staffing constraints.
7. **Acceptance contract** — Make normal and failure requirements independently testable.

### Module 2 — Architecture Boundaries and Consistency

#### Outcomes

- SYS8-O2
- SYS8-O3
- SYS8-O10

#### Lessons

1. **Monolith versus service split** — Compare isolation, deploy independence, latency and complexity under the stated workload.
2. **Communication patterns** — Select synchronous calls, queues or local IPC with retry and ordering consequences.
3. **State and authority** — Define who owns durable records, protocol versions and request deduplication.
4. **Replication choices** — Reuse SYS6 guarantees without requiring a new consensus implementation.
5. **Failure-domain map** — Identify process, host, disk and network failure assumptions and consequences.
6. **Design alternatives** — Present at least two architectures with falsifiable trade-offs and an accountable selection.

### Module 3 — Reliability, Resources and Capacity

#### Outcomes

- SYS8-O3
- SYS8-O4
- SYS8-O5
- SYS8-O9

#### Lessons

1. **Load and queue model** — Calculate an initial capacity estimate with measured service time and arrival distribution.
2. **Admission and overload** — Prefer bounded queues, rate controls and useful rejection over silent overload collapse.
3. **Backoff and retry budgets** — Avoid synchronized retry storms and double effects after uncertain completion.
4. **Degraded modes** — Define what remains correct when a dependency is unavailable or stale.
5. **Disk/memory risk** — Plan growth, filesystem exhaustion, compaction spikes and safe failure.
6. **Recovery objectives** — Separate RTO, RPO and deterministic local restart from untested disaster recovery claims.
7. **Reliability experiment** — Run a local overload or failure case to compare predictions with observations.

### Module 4 — Deployment and Safe Configuration

#### Outcomes

- SYS8-O6
- SYS8-O7
- SYS8-O10

#### Lessons

1. **Config contracts** — Validate typed operating settings, bounded defaults and safe startup refusal.
2. **Privilege and secrets** — Run as a nonprivileged process, avoid logged secrets and document minimum file/network access.
3. **Build provenance** — Pin toolchains and dependencies and explain binary/OS compatibility limits.
4. **Readiness versus liveness** — Design health checks that do not assert an unhealthy service is ready.
5. **Change and rollback** — Test safe stop/start, version mismatch, schema/storage migration limits and rollback preconditions.
6. **Automation choice** — Use a local script or free reproducible VM/container; no mandatory hosted orchestrator.

### Module 5 — Operational Evidence and Incidents

#### Outcomes

- SYS8-O4
- SYS8-O8
- SYS8-O9
- SYS8-O11

#### Lessons

1. **Operator signals** — Connect SLOs to metrics, logs and trace examples that localize likely failures.
2. **Alert policies** — Distinguish actionable symptom alerts from noisy metric threshold guessing.
3. **Incident command** — Define ownership, mitigation, communication, restart and escalation using a synthetic incident.
4. **Runbook verification** — Execute procedures against controlled fixtures and verify they preserve intended state.
5. **Post-incident analysis** — Construct a timeline that separates observed facts, assumptions and disputed root causes.
6. **Safety and privacy** — Redact sensitive diagnostics and prevent destructive test procedures from targeting shared resources.
7. **Go/no-go review** — Classify critical blockers, mitigated risks and deferred changes with evidence.

### Module 6 — Production Readiness Design Review

#### Outcomes

- SYS8-O1
- SYS8-O2
- SYS8-O5
- SYS8-O6
- SYS8-O7
- SYS8-O8
- SYS8-O9
- SYS8-O10
- SYS8-O11
- SYS8-O12

#### Lessons

1. **Select a known artifact** — Harden a SYS4 or SYS6 service, or use a published synthetic system; do not demand unrelated projects.
2. **Architecture record** — Document constraints, service boundaries, decision matrix and data lifecycle.
3. **Operational package** — Provide reproducible install/config, safe startup, readiness and rollback procedures.
4. **Load/fault exercise** — Test one limit and one failure with independent acceptance criteria.
5. **Independent handoff** — Have another reviewer follow the runbook or use a reproducible scripted equivalent.
6. **Unfamiliar change defense** — Revise architecture under a new bounded incident or traffic constraint without masking defects.

## Completion requirements

These are required summative assessments. Formative runbook trials and design exercises are not additional completion obligations unless cited within the explicit required work.

- **SYS8-AS1** — Requirements and Architecture Decision
  - **Outcomes:** SYS8-O1, SYS8-O2, SYS8-O3, SYS8-O4, SYS8-O10.
  - **Work:** Define an actual workload/contract, evaluate at least two component structures and state consistency/failure guarantees.
  - **Criteria:** A measurable contract, authentic trade-offs, explicit rejected alternatives and testable architecture decisions are present.
  - **Evidence:** Requirements, workload assumptions, diagrams, risk table, decision record and trace to outcomes.

- **SYS8-AS2** — Capacity and Resilience Model
  - **Outcomes:** SYS8-O3, SYS8-O4, SYS8-O5, SYS8-O9.
  - **Work:** Estimate capacity and exercise one overload or failure mode under bounded local conditions.
  - **Criteria:** Arithmetic and queue assumptions defensible; actual limit measured; correct reject/degrade behavior; uncertainty and recovery limits reported.
  - **Evidence:** Calculations, resource budgets, synthetic load trace, observed responses and recovery evidence.

- **SYS8-AS3** — Secure Operations and Lifecycle
  - **Outcomes:** SYS8-O6, SYS8-O7, SYS8-O8.
  - **Work:** Prepare a service's configuration, startup/readiness, deployment/rollback and incident runbook.
  - **Criteria:** Nonprivileged reproducible startup, no secret in logs, invalid config safe refusal, meaningful health signals and workable recovery procedures.
  - **Evidence:** Scripts, manifests/config examples, privacy tests, runbook, clean-state install and rollback scenario.

- **SYS8-AS4** — Independent Readiness Review
  - **Outcomes:** SYS8-O1, SYS8-O7, SYS8-O8, SYS8-O9, SYS8-O10, SYS8-O11.
  - **Work:** Review a prior systems artifact as another engineer's operational responsibility; test prescribed procedures.
  - **Criteria:** Go/no-go criteria applied consistently; blockers and limitations not hidden; reviewer can reproduce core checks and at least one injected incident.
  - **Evidence:** Review checklist mapped to outcomes, reproduced evidence, measured limitations, risk register and reviewer response.

- **SYS8-AS5** — Unfamiliar Production Constraint Defense
  - **Outcomes:** SYS8-O2, SYS8-O3, SYS8-O5, SYS8-O10, SYS8-O11, SYS8-O12.
  - **Work:** Respond to a new failure-domain, demand, secret-leak or operational handoff scenario by revising a documented design.
  - **Criteria:** Changed assumptions named; correction addresses root cause without silently weakening reliability or security; regression verified.
  - **Evidence:** Scenario, updated architecture, counterexample, bounded tests and defense.

### Production-readiness and scope limitations

A synthetic load test and a written SLO are not evidence of production availability; a rollback plan is not a tested rollback until exercised. Disaster recovery, multi-region high availability, compliance certifications and private organizational operations are not silently required or claimed. Safe service shutdown, least privilege, bounded overload and operator reproducibility are required where applicable. Course completion is based on the published decisions and evidence, not choosing one vendor's production stack.

### Independent evidence and revision

Reproduce configuration, startup, failure and recovery from clean checkout or equivalently clean environment with synthetic data and no secrets. Preserve assumptions, expected and observed operation, load settings, compatibility limits and reviewer notes. Each decision records course revision, assessment ID, mapped outcomes, evidence and status. Existing learner completions remain revision-scoped; this course is `draft` until authentic learner/review evidence warrants promotion.
