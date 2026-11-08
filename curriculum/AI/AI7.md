# AI7 — Production AI Systems & MLOps

**Program:** AI — AI Engineering
**Type:** `course`
**Prerequisites:** AI5 and AI6 *(legacy mapping; reconcile before activation)*
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/AI.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Learn the engineering work required after model development: serving, batching, caching, concurrency, versioning, monitoring, rollout, rollback, incident handling, and cost control.

## Learning outcomes

- Package and serve an AI model or AI application behind a reliable interface.
- Measure latency, throughput, resource use, and cost under representative workloads.
- Choose batching, caching, concurrency, and versioning strategies deliberately.
- Implement monitoring, alerts, rollout controls, and rollback procedures.
- Investigate a production regression using traces and measurements.

## Modules

### Module 1 — Model Serving

#### Outcomes

By the end of this module, the learner can:

- Explain **Model serving architectures** in the context of the course.
- Apply **API boundaries and resource management** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Model serving architectures** — `lesson`
2. **API boundaries and resource management** — `lesson`
3. **Checkpoint: serving architecture** — `test`
4. **Micro-lab: Wrap a model in a small service and measure request behavior.** — `lab`

### Module 2 — Batching & Concurrency

#### Outcomes

By the end of this module, the learner can:

- Explain **Batching and concurrent requests** in the context of the course.
- Apply **Latency and throughput trade-offs** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Batching and concurrent requests** — `lesson`
2. **Latency and throughput trade-offs** — `lesson`
3. **Checkpoint: serving performance** — `test`
4. **Micro-lab: Compare throughput and tail latency across batch settings.** — `lab`

### Module 3 — Model & Runtime Optimization

#### Outcomes

By the end of this module, the learner can:

- Explain **Caching and model/version management** in the context of the course.
- Apply **CPU/GPU trade-offs and cost controls** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Caching and model/version management** — `lesson`
2. **CPU/GPU trade-offs and cost controls** — `lesson`
3. **Checkpoint: optimization decisions** — `test`
4. **Micro-lab: Measure one optimization and state its cost trade-off.** — `lab`

### Module 4 — Deployment & Reliability

#### Outcomes

By the end of this module, the learner can:

- Explain **Deployment, monitoring, and alert conditions** in the context of the course.
- Apply **Rollback and incident handling** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Deployment, monitoring, and alert conditions** — `lesson`
2. **Rollback and incident handling** — `lesson`
3. **Checkpoint: production AI reliability** — `test`
4. **Micro-lab: Simulate a bad model release and recover to a known-good version.** — `lab`

### Module 5 — Production AI Service

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Package, deploy, observe, and recover the Production AI Service** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- model serving
- batching
- caching
- concurrency
- latency
- p50/p95/p99
- GPU/CPU trade-offs
- model/version management
- deployment
- monitoring
- rollback
- cost controls
- incident handling

### Labs

- serving benchmark
- batching comparison
- cache experiment
- latency regression
- rollback drill

### Substantial course lab

**Production AI Service**

Package an earlier model or AI system with:

- API/service layer
- tests
- containerization
- deployment configuration
- metrics
- dashboards
- alert conditions
- versioning
- rollback procedure
