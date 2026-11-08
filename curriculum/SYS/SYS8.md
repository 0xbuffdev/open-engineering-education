# SYS8 — Systems Design & Production Engineering

**Program:** SYS — Systems Engineering
**Type:** `course`
**Prerequisites:** SYS6 and SYS7 *(legacy mapping; reconcile before activation)*
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SYS.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Synthesize the program's systems knowledge into production engineering decisions involving service boundaries, reliability, capacity, operations, and failure handling.

## Learning outcomes

- Translate system requirements into explicit performance, reliability, and operational targets.
- Choose system boundaries and communication patterns appropriate to those requirements.
- Design failure handling, recovery, and observability into a systems architecture.
- Evaluate resource, complexity, and operational trade-offs with measured evidence.
- Design and defend a production-oriented systems architecture.

## Modules

### Module 1 — Reliability & Failure Design

#### Outcomes

By the end of this module, the learner can:

- Explain **Reliability goals and failure modes** in the context of the course.
- Apply **Resource limits and failure handling** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Reliability goals and failure modes** — `lesson`
2. **Resource limits and failure handling** — `lesson`
3. **Checkpoint: reliability reasoning** — `test`
4. **Micro-lab: Define one failure budget and test the system against it.** — `lab`

### Module 2 — Service Boundaries & Configuration

#### Outcomes

By the end of this module, the learner can:

- Explain **Service boundaries and dependency contracts** in the context of the course.
- Apply **Configuration and safe operational defaults** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Service boundaries and dependency contracts** — `lesson`
2. **Configuration and safe operational defaults** — `lesson`
3. **Checkpoint: operational boundaries** — `test`
4. **Micro-lab: Introduce configuration validation and failure-safe defaults.** — `lab`

### Module 3 — Observability & Load Testing

#### Outcomes

By the end of this module, the learner can:

- Explain **Operational metrics and logs** in the context of the course.
- Apply **Load testing and capacity signals** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Operational metrics and logs** — `lesson`
2. **Load testing and capacity signals** — `lesson`
3. **Checkpoint: production evidence** — `test`
4. **Micro-lab: Run a controlled load test and identify one resource limit.** — `lab`

### Module 4 — Incidents & Readiness

#### Outcomes

By the end of this module, the learner can:

- Explain **Incident analysis and recovery** in the context of the course.
- Apply **Operational documentation and handoff** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Incident analysis and recovery** — `lesson`
2. **Operational documentation and handoff** — `lesson`
3. **Checkpoint: readiness review** — `test`
4. **Micro-lab: Write a runbook for one failure scenario and test the procedure.** — `lab`

### Module 5 — Production Readiness Review

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Harden and review one systems service for another engineering team to operate** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- reliability
- service boundaries
- resource limits
- failure handling
- configuration
- deployment
- observability
- load testing
- incident analysis
- operational documentation

### Substantial course lab

**Production Readiness Review**

Harden one earlier service as if another engineering team were going to operate it.
