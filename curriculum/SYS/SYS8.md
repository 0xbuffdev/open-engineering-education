## SYS8 — Systems Design & Production Engineering

**Duration:** 5 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SYS6 and SYS7

### Overview

Synthesize the program's systems knowledge into production engineering decisions involving service boundaries, reliability, capacity, operations, and failure handling.

### Prerequisites

**SYS6 — Distributed Systems**
**SYS7 — Performance Engineering & Observability**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Translate system requirements into explicit performance, reliability, and operational targets.
- Choose system boundaries and communication patterns appropriate to those requirements.
- Design failure handling, recovery, and observability into a systems architecture.
- Evaluate resource, complexity, and operational trade-offs with measured evidence.
- Design and defend a production-oriented systems architecture.


### Resource map

**Required**

- **B26** Ch. 3–4, 6, 10–15, 17, 21–22, 27 and 32.
- **B29** Ch. 3–5, 7, 9–10 and 13–14.
- **B43** Ch. 4–9, 14 and 16–18.
- **B25** Ch. 1–2 (reliability, scalability, maintainability).

### Modules

#### Module 1 — Reliability & Failure Design

**Reading:** **B26** Ch. 3 (Embracing Risk), Ch. 4 (Service Level Objectives), Ch. 22 (Addressing Cascading Failures). **B29** Ch. 3–5 (stability: antipatterns and patterns). **B25** Ch. 1–2.


### Module outcomes

By the end of this module, the learner can:

- Explain **Reliability goals and failure modes** in the context of the course.
- Apply **Resource limits and failure handling** in a problem, implementation, experiment, or design decision.

1. **Reliability goals and failure modes**
   - kind: `lesson`
2. **Resource limits and failure handling**
   - kind: `lesson`
3. **Checkpoint: reliability reasoning**
   - kind: `test`

4. **Micro-lab: Define one failure budget and test the system against it.**
   - kind: `lab`
#### Module 2 — Service Boundaries & Configuration

**Reading:** **B29** Ch. 7 (Foundations), Ch. 9 (Interconnect), Ch. 10 (Control Plane). **B43** Ch. 5 (Design for Least Privilege), Ch. 6 (Design for Understandability). **R16** the twelve factors.


### Module outcomes

By the end of this module, the learner can:

- Explain **Service boundaries and dependency contracts** in the context of the course.
- Apply **Configuration and safe operational defaults** in a problem, implementation, experiment, or design decision.

1. **Service boundaries and dependency contracts**
   - kind: `lesson`
2. **Configuration and safe operational defaults**
   - kind: `lesson`
3. **Checkpoint: operational boundaries**
   - kind: `test`

4. **Micro-lab: Introduce configuration validation and failure-safe defaults.**
   - kind: `lab`
#### Module 3 — Observability & Load Testing

**Reading:** **B26** Ch. 6 (Monitoring Distributed Systems), Ch. 10 (Practical Alerting from Time-Series Data), Ch. 17 (Testing for Reliability). **B32** Ch. 12 (Benchmarking). **B27** Ch. 12–13 (SLOs; acting on SLO-based alerts).


### Module outcomes

By the end of this module, the learner can:

- Explain **Operational metrics and logs** in the context of the course.
- Apply **Load testing and capacity signals** in a problem, implementation, experiment, or design decision.

1. **Operational metrics and logs**
   - kind: `lesson`
2. **Load testing and capacity signals**
   - kind: `lesson`
3. **Checkpoint: production evidence**
   - kind: `test`

4. **Micro-lab: Run a controlled load test and identify one resource limit.**
   - kind: `lab`
#### Module 4 — Incidents & Readiness

**Reading:** **B26** Ch. 11 (Being On-Call), Ch. 12 (Effective Troubleshooting), Ch. 13 (Emergency Response), Ch. 14 (Managing Incidents), Ch. 15 (Postmortem Culture). **B43** Ch. 16 (Disaster Planning), Ch. 17 (Crisis Management), Ch. 18 (Recovery and Aftermath).


### Module outcomes

By the end of this module, the learner can:

- Explain **Incident analysis and recovery** in the context of the course.
- Apply **Operational documentation and handoff** in a problem, implementation, experiment, or design decision.

1. **Incident analysis and recovery**
   - kind: `lesson`
2. **Operational documentation and handoff**
   - kind: `lesson`
3. **Checkpoint: readiness review**
   - kind: `test`

4. **Micro-lab: Write a runbook for one failure scenario and test the procedure.**
   - kind: `lab`
#### Module 5 — Production Readiness Review

**Reading:** **B26** Ch. 32 (The Evolving SRE Engagement Model — production readiness reviews), Ch. 27 (Reliable Product Launches at Scale). **B29** Ch. 13 (Design for Deployment), Ch. 14 (Handling Versions). **B43** Ch. 8 (Design for Resilience), Ch. 9 (Design for Recovery), Ch. 14 (Deploying Code).


1. **Harden and review one systems service for another engineering team to operate**
   - kind: `lab`

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

---

