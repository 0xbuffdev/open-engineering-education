# SEC7 — Detection, Incident Response & Threat Hunting

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** SEC4 and SEC6 *(legacy mapping; reconcile before activation)*
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SEC.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Develop defensive security skills through logging, detection rules, incident triage, evidence handling, host forensics, root-cause analysis, threat hunting, and recovery exercises.

## Learning outcomes

- Design useful security telemetry and detection signals.
- Investigate a controlled security incident from logs and system artifacts.
- Acquire and preserve host evidence in a defensible order, verify its integrity, and examine common host artifacts to reconstruct activity.
- Build and test simple detection rules.
- Construct an incident timeline and identify root cause.
- Recommend and verify remediation following a controlled incident.

## Modules

### Module 1 — Security Telemetry

#### Outcomes

By the end of this module, the learner can:

- Explain **Logs, telemetry, and indicators** in the context of the course.
- Apply **Building useful security evidence** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Logs, telemetry, and indicators** — `lesson`
2. **Building useful security evidence** — `lesson`
3. **Checkpoint: telemetry** — `test`
4. **Micro-lab: Select the telemetry needed to answer a concrete incident question.** — `lab`

### Module 2 — Detection & Triage

#### Outcomes

By the end of this module, the learner can:

- Explain **Detection rules and alert quality** in the context of the course.
- Apply **Incident triage and containment** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Detection rules and alert quality** — `lesson`
2. **Incident triage and containment** — `lesson`
3. **Checkpoint: incident triage** — `test`
4. **Micro-lab: Classify a controlled alert and choose the next evidence to collect.** — `lab`

### Module 3 — Evidence & Root Cause

#### Outcomes

By the end of this module, the learner can:

- Explain **Evidence handling and timelines** in the context of the course.
- Apply **Host acquisition and artifacts** in a problem, implementation, experiment, or design decision.
- Apply **Root-cause analysis** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Evidence handling and timelines** — `lesson`
2. **Host acquisition and artifacts** — order of volatility, integrity hashing, imaging a controlled lab system you own, and examining common host artifacts (authentication and system logs, shell history, process and network state, file timestamps) — `lesson`
3. **Root-cause analysis** — `lesson`
4. **Checkpoint: investigation reasoning** — `test`
5. **Micro-lab: Acquire host evidence from a controlled lab system, verify its integrity, and construct a timeline from the logs and artifacts.** — `lab`

### Module 4 — Threat Hunting & Recovery

#### Outcomes

By the end of this module, the learner can:

- Explain **Threat hunting hypotheses** in the context of the course.
- Apply **Recovery and post-incident review** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Threat hunting hypotheses** — `lesson`
2. **Recovery and post-incident review** — `lesson`
3. **Checkpoint: recovery decisions** — `test`
4. **Micro-lab: Validate a hunting hypothesis and document the remediation follow-up.** — `lab`

### Module 5 — Incident Investigation

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Investigate the controlled incident, produce evidence-backed findings, and verify remediation** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- security logging
- telemetry
- indicators
- detection rules
- incident triage
- containment
- evidence handling
- host forensics: acquisition, order of volatility, integrity verification, host artifacts
- root-cause analysis
- threat hunting
- recovery
- post-incident review

### Labs

- generate known test activity
- detect it from logs
- acquire and examine host evidence from a controlled system
- investigate an incident
- build a simple detection rule
- conduct a tabletop exercise

### Substantial course lab

**Incident Investigation**

Investigate a controlled incident from logs and host artifacts, preserve and document the evidence, produce a timeline, identify the root cause, recommend fixes, and verify the fixes.
