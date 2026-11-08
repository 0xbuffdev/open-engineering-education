## AI7 — Production AI Systems & MLOps

**Duration:** 6 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** AI5 and AI6

**Recommended:** SYS7 and SYS8.

### Overview

Learn the engineering work required after model development: serving, batching, caching, concurrency, versioning, monitoring, rollout, rollback, incident handling, and cost control.

### Prerequisites

**AI5 — Retrieval, Agents & Applied Generative AI**
**AI6 — Training, Fine-Tuning & Evaluation**
**Recommended:** SYS7 and SYS8.

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Package and serve an AI model or AI application behind a reliable interface.
- Measure latency, throughput, resource use, and cost under representative workloads.
- Choose batching, caching, concurrency, and versioning strategies deliberately.
- Implement monitoring, alerts, rollout controls, and rollback procedures.
- Investigate a production regression using traces and measurements.


### Modules

#### Module 1 — Model Serving



### Module outcomes

By the end of this module, the learner can:

- Explain **Model serving architectures** in the context of the course.
- Apply **API boundaries and resource management** in a problem, implementation, experiment, or design decision.

1. **Model serving architectures**
   - kind: `lesson`
2. **API boundaries and resource management**
   - kind: `lesson`
3. **Checkpoint: serving architecture**
   - kind: `test`

4. **Micro-lab: Wrap a model in a small service and measure request behavior.**
   - kind: `lab`
#### Module 2 — Batching & Concurrency



### Module outcomes

By the end of this module, the learner can:

- Explain **Batching and concurrent requests** in the context of the course.
- Apply **Latency and throughput trade-offs** in a problem, implementation, experiment, or design decision.

1. **Batching and concurrent requests**
   - kind: `lesson`
2. **Latency and throughput trade-offs**
   - kind: `lesson`
3. **Checkpoint: serving performance**
   - kind: `test`

4. **Micro-lab: Compare throughput and tail latency across batch settings.**
   - kind: `lab`
#### Module 3 — Model & Runtime Optimization



### Module outcomes

By the end of this module, the learner can:

- Explain **Caching and model/version management** in the context of the course.
- Apply **CPU/GPU trade-offs and cost controls** in a problem, implementation, experiment, or design decision.

1. **Caching and model/version management**
   - kind: `lesson`
2. **CPU/GPU trade-offs and cost controls**
   - kind: `lesson`
3. **Checkpoint: optimization decisions**
   - kind: `test`

4. **Micro-lab: Measure one optimization and state its cost trade-off.**
   - kind: `lab`
#### Module 4 — Deployment & Reliability



### Module outcomes

By the end of this module, the learner can:

- Explain **Deployment, monitoring, and alert conditions** in the context of the course.
- Apply **Rollback and incident handling** in a problem, implementation, experiment, or design decision.

1. **Deployment, monitoring, and alert conditions**
   - kind: `lesson`
2. **Rollback and incident handling**
   - kind: `lesson`
3. **Checkpoint: production AI reliability**
   - kind: `test`

4. **Micro-lab: Simulate a bad model release and recover to a known-good version.**
   - kind: `lab`
#### Module 5 — Production AI Service



1. **Package, deploy, observe, and recover the Production AI Service**
   - kind: `lab`

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

---

