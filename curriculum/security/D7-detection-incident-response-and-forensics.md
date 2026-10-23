# D7 — Detection, Incident Response & Forensics

**Track:** Security · **Prerequisite:** D1, S10 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P11 detection/IR drill

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Learn to detect, investigate, contain, and learn from security incidents. You will build telemetry and detection rules for a system you own, run a tabletop and a local drill, preserve evidence, and write a timeline and postmortem.

## Outcomes

You can:

- identify useful telemetry sources and their blind spots;
- write and test detection rules with low false positives;
- explain the incident-response lifecycle;
- triage an alert and form an evidence-based hypothesis;
- preserve volatile and persistent evidence;
- build a timeline from logs and artifacts;
- contain and eradicate without destroying evidence;
- write an incident report and blameless postmortem;
- map activity to MITRE ATT&CK;
- state chain-of-custody and privacy constraints.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [NIST SP 800-61](https://csrc.nist.gov/pubs/sp/800/61/r3/final) (current revision) | Full | Incident-response lifecycle |
| [MITRE ATT&CK](https://attack.mitre.org/) | Detection, data sources, selected techniques | Adversary mapping |
| [SigmaHQ](https://github.com/SigmaHQ/sigma) | Rule format and selected rules | Detection engineering |
| [Zeek docs](https://docs.zeek.org/) | Logs, scripts, network evidence | Network telemetry |
| [Suricata docs](https://docs.suricata.io/) | Rules, EVE JSON | IDS telemetry |
| *The Art of Memory Forensics* (Ligh et al.) | Ch. **1–3** selected | Volatile evidence |
| *Practical Malware Analysis* (Sikorski & Honig) | Ch. **1–3** | Safe triage concepts |
| [The DFIR Report](https://thedfirreport.com/) | Two case studies | Realistic timelines |

## Modules

### 1. Telemetry and detection

- host: process creation, file, registry, authentication, kernel audit;
- network: DNS, flow, TLS metadata, proxy, IDS;
- application: auth, authorization, errors, audit;
- cloud: control-plane and data-plane logs;
- identity: sign-in, MFA, token use;
- log quality, time sync, retention, cost;
- detection rule anatomy and testing.

### 2. Detection engineering

- signature vs behavioral detection;
- ATT&CK mapping;
- false positives and tuning;
- baseline and anomaly detection;
- detection-as-code;
- test fixtures and replay;
- coverage gaps;
- alert triage and severity.

### 3. Incident response

- preparation, identification, containment, eradication, recovery, lessons learned;
- roles and incident command;
- severity and escalation;
- evidence preservation;
- communications;
- legal/privacy/notification boundaries;
- containment trade-offs;
- recovery validation.

### 4. Forensics

- order of volatility;
- disk, memory, network, and cloud artifacts;
- hashing and chain of custody;
- timeline analysis;
- artifact interpretation and anti-forensics awareness;
- malware triage in an isolated environment;
- reporting uncertainty;
- privacy and data minimization.

### 5. Drill and postmortem

- tabletop design;
- injects and stop conditions;
- local detection/response lab;
- timeline and decision log;
- blameless postmortem;
- detection/response improvements;
- measuring MTTD/MTTR with caveats.

## Labs

### Lab 1 — Telemetry inventory

For P4 or a local Linux VM, list available logs and what question each can answer. Identify three blind spots. Configure one host audit rule and one network log source.

### Lab 2 — Detection rule

Write a Sigma-style rule for a behavior you can generate locally (e.g., suspicious shell spawn, repeated failed logins, unexpected outbound connection). Test true positive and false positive fixtures. Tune once and document the trade-off.

### Lab 3 — Timeline

Generate a small local incident trace (login failures, process execution, file change, network connection). Build a timeline from at least three sources. Reconcile clock skew and one missing event.

### Lab 4 — Tabletop and drill

Run a tabletop for a ransomware or credential-theft scenario. Then run a safe local drill: detect, triage, contain a test process/account, preserve logs, and recover. Record decisions, timestamps, and evidence.

### Lab 5 — Incident report and postmortem

Write an incident report with executive summary, timeline, scope, evidence, impact, containment, recovery, root/contributing factors, and actions. Separate facts from hypotheses. Add a blameless postmortem.

## Exercises

1. Map three log sources to ATT&CK data sources.
2. Write a detection rule and two test fixtures.
3. Explain a false positive and how to tune it.
4. Order evidence by volatility.
5. Build a timeline with conflicting timestamps.
6. Explain a containment trade-off.
7. Distinguish eradication from recovery.
8. Write a chain-of-custody entry.
9. Explain one anti-forensics technique and a countermeasure.
10. State what a log gap means for conclusions.

## Project increment — P11 detection/IR drill

Produce:

- telemetry inventory and detection rule;
- tested true/false positive fixtures;
- incident timeline from multiple sources;
- containment/recovery evidence;
- incident report and blameless postmortem;
- detection/response improvements with owners.

**Brief:** [P11 — authorized-assessment](../projects/project-ladder.md#p11--authorized-assessment)

## Exit check

- [ ] show a detection rule with tested positives and negatives;
- [ ] build a multi-source timeline and resolve clock issues;
- [ ] preserve evidence in volatility order;
- [ ] contain and recover a local incident;
- [ ] separate fact from hypothesis in the report;
- [ ] identify detection gaps and owned improvements;
- [ ] state privacy/legal boundaries.

## Common failure modes

- Alerting on every event and calling it detection.
- Writing a rule without false-positive testing.
- Reimaging a host before preserving evidence.
- Treating a log timestamp as ground truth.
- Confusing containment with eradication.
- Writing a timeline from memory.
- Publishing real victim data.
- No follow-up owner for postmortem actions.

## Evidence to commit

- `labs/security/D7/` with telemetry inventory, rules/fixtures, timeline, drill log, report, postmortem
- P11 detection/IR report
- `notes/security/D7/summary.md`

## Optional depth

- *Incident Response & Computer Forensics* (Luttgens et al.).
- *The Practice of Network Security Monitoring* (Bejtlich).
- Velociraptor and osquery documentation.
- Atomic Red Team (local, authorized tests).
- NIST SP 800-86 (forensic techniques).
