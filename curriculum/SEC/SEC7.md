## SEC7 — Detection, Incident Response & Threat Hunting

**Duration:** 5 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** SEC4 and SEC6

### Overview

Develop defensive security skills through logging, detection rules, incident triage, evidence handling, host forensics, root-cause analysis, threat hunting, and recovery exercises.

### Prerequisites

**SEC4 — Network & Infrastructure Security**
**SEC6 — Cloud, Containers & Identity Security**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Design useful security telemetry and detection signals.
- Investigate a controlled security incident from logs and system artifacts.
- Acquire and preserve host evidence in a defensible order, verify its integrity, and examine common host artifacts to reconstruct activity.
- Build and test simple detection rules.
- Construct an incident timeline and identify root cause.
- Recommend and verify remediation following a controlled incident.


### Resource map

**Required**

- **R73** NIST SP 800-61 Rev. 3 · **B43** Ch. 15–18 · **R69** NIST SP 800-92 · **R74** NIST SP 800-86.
- **R80** MITRE ATT&CK · **R81** Sigma · **B26** Ch. 15 (Postmortem Culture).

### Modules

#### Module 1 — Security Telemetry

**Reading:** **R69** NIST SP 800-92 (log management). **B43** Ch. 15 (Investigating Systems). **R14** Logging cheat sheet. **R31** A09 Security Logging and Alerting Failures.


### Module outcomes

By the end of this module, the learner can:

- Explain **Logs, telemetry, and indicators** in the context of the course.
- Apply **Building useful security evidence** in a problem, implementation, experiment, or design decision.

1. **Logs, telemetry, and indicators**
   - kind: `lesson`
2. **Building useful security evidence**
   - kind: `lesson`
3. **Checkpoint: telemetry**
   - kind: `test`

4. **Micro-lab: Select the telemetry needed to answer a concrete incident question.**
   - kind: `lab`
#### Module 2 — Detection & Triage

**Reading:** **R80** ATT&CK tactics and techniques; data sources and detections. **R81** Sigma rule specification. **R73** the Detect and Respond functions.


### Module outcomes

By the end of this module, the learner can:

- Explain **Detection rules and alert quality** in the context of the course.
- Apply **Incident triage and containment** in a problem, implementation, experiment, or design decision.

1. **Detection rules and alert quality**
   - kind: `lesson`
2. **Incident triage and containment**
   - kind: `lesson`
3. **Checkpoint: incident triage**
   - kind: `test`

4. **Micro-lab: Classify a controlled alert and choose the next evidence to collect.**
   - kind: `lab`
#### Module 3 — Evidence & Root Cause

**Reading:** **B43** Ch. 15 (Investigating Systems). **R74** NIST SP 800-86 (the forensic process: collection, examination, analysis, reporting; using data from data files and from operating systems). **B26** Ch. 12 (Effective Troubleshooting), Ch. 15 (Postmortem Culture).


### Module outcomes

By the end of this module, the learner can:

- Explain **Evidence handling and timelines** in the context of the course.
- Apply **Host acquisition and artifacts** in a problem, implementation, experiment, or design decision.
- Apply **Root-cause analysis** in a problem, implementation, experiment, or design decision.

1. **Evidence handling and timelines**
   - kind: `lesson`
2. **Host acquisition and artifacts** — order of volatility, integrity hashing, imaging a controlled lab system you own, and examining common host artifacts (authentication and system logs, shell history, process and network state, file timestamps)
   - kind: `lesson`
3. **Root-cause analysis**
   - kind: `lesson`
4. **Checkpoint: investigation reasoning**
   - kind: `test`

5. **Micro-lab: Acquire host evidence from a controlled lab system, verify its integrity, and construct a timeline from the logs and artifacts.**
   - kind: `lab`
#### Module 4 — Threat Hunting & Recovery

**Reading:** **R80** ATT&CK (hypothesis-driven hunting). **B43** Ch. 17 (Crisis Management), Ch. 18 (Recovery and Aftermath). **R73** the Recover function.


### Module outcomes

By the end of this module, the learner can:

- Explain **Threat hunting hypotheses** in the context of the course.
- Apply **Recovery and post-incident review** in a problem, implementation, experiment, or design decision.

1. **Threat hunting hypotheses**
   - kind: `lesson`
2. **Recovery and post-incident review**
   - kind: `lesson`
3. **Checkpoint: recovery decisions**
   - kind: `test`

4. **Micro-lab: Validate a hunting hypothesis and document the remediation follow-up.**
   - kind: `lab`
#### Module 5 — Incident Investigation

**Reading:** **B43** Ch. 15–18. **B26** Ch. 15. **R73** NIST SP 800-61 Rev. 3.


1. **Investigate the controlled incident, produce evidence-backed findings, and verify remediation**
   - kind: `lab`

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

---

