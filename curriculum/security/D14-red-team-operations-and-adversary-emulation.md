# D14 — Red Team Operations & Adversary Emulation

**Track:** Security · **Prerequisite:** D4, D7 · **Elective** · **Time:** 5 weeks, 75 hours · **Project:** elective

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Learn how authorized adversary emulation differs from penetration testing: objective-based campaigns, stealth, detection, command-and-control concepts, and reporting that improves defence. All activity is on isolated lab infrastructure under written authorization.

## Outcomes

You can:

- define a threat model and emulation objective with a sponsor;
- select adversary behaviours from MITRE ATT&CK;
- plan infrastructure, OPSEC, and deconfliction;
- design a campaign with stop conditions and safety controls;
- execute non-destructive emulation in an isolated lab;
- coordinate with defenders and measure detection;
- distinguish persistence, lateral movement, and exfiltration concepts without uncontrolled use;
- write an operational report and defender debrief;
- state legal, ethical, and scope limits;
- explain why red-team success is not a complete security measure.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| *Red Team Development and Operations* (Vest & Tubberville) | Ch. **1–10** | Program, planning, execution, reporting |
| [MITRE ATT&CK](https://attack.mitre.org/) | Enterprise tactics and selected techniques | Emulation library |
| [PTES](http://www.pentest-standard.org/) | Full | Engagement method |
| [TIBER-EU Framework](https://www.ecb.europa.eu/pub/pdf/other/ecb.tiber_eu_framework.en.pdf) | Overview | Threat-led assessment |
| [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) | Selected | Technical testing |
| [CISA Red Team Assessments](https://www.cisa.gov/resources-tools/services/red-team-assessments) | Public reports | Realistic objectives and lessons |
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | Local test definitions | Safe emulation building blocks |
| [SigmaHQ](https://github.com/SigmaHQ/sigma) | Detection rules | Defender coordination |

## Modules

### 1. Program and authorization

- red team versus pentest versus adversary emulation;
- sponsor, objectives, and success criteria;
- scope, exclusions, and deconfliction;
- written authorization and legal review;
- emergency stop and rollback;
- safety of people and production;
- data handling and reporting;
- ethics and disclosure.

### 2. Threat-informed planning

- threat intelligence and relevant adversaries;
- ATT&CK mapping;
- attack trees and kill chains;
- assume-breach versus external start;
- critical asset and mission focus;
- detection assumptions;
- campaign narrative;
- resource and time budget.

### 3. Infrastructure and OPSEC

- isolated lab vs authorized environment;
- redirectors and C2 concepts (awareness);
- domain/email infrastructure policy;
- payload handling and non-persistence;
- logging and evidence;
- avoid real third parties;
- no phishing without explicit approval;
- cleanup and decommission.

### 4. Execution in a lab

- initial access via a designated vector;
- discovery and privilege escalation concepts;
- lateral movement concepts with stop conditions;
- collection/exfiltration simulation using synthetic data;
- defender observation;
- deconfliction and timeouts;
- abort criteria.

### 5. Detection and purple teaming

- telemetry coverage;
- detection opportunities;
- purple-team feedback loop;
- measure detect/respond, not just "access achieved";
- false negatives and false positives;
- detection engineering (connect D7);
- reporting to defenders.

### 6. Reporting and improvement

- executive summary and objectives;
- campaign timeline;
- techniques and evidence;
- detection results;
- business impact;
- remediation priorities;
- residual risk;
- debrief and follow-up.

## Labs

### Lab 1 — Campaign plan

Write a red-team plan for an isolated lab with a sponsor, objective, ATT&CK techniques, scope, stop conditions, safety controls, and detection hypotheses. Get explicit authorization before execution.

### Lab 2 — Emulation build

Select three ATT&CK techniques that can be safely emulated with Atomic Red Team or custom local scripts. Document prerequisites and expected telemetry. Do not use live malware or target third parties.

### Lab 3 — Execute and observe

Run the emulation in the isolated lab while a defender monitors. Record what was detected, what was missed, and the time to detect. Stop at the agreed boundary.

### Lab 4 — Purple-team iteration

Share one technique with the defender. Improve a detection rule or telemetry source. Re-run the technique and measure the change. Document false positives.

### Lab 5 — Operational report

Write a report with objectives, scope, timeline, techniques, detection outcomes, impact, and prioritized remediation. Include a defender debrief and one limitation of the exercise.

## Exercises

1. Distinguish red teaming from penetration testing.
2. Write a deconfliction plan.
3. Map an objective to three ATT&CK techniques.
4. Explain a stop condition for production safety.
5. Design a detection hypothesis.
6. Explain C2 infrastructure risk at a high level.
7. Measure time to detect.
8. Write a purple-team feedback item.
9. Explain why "domain admin achieved" is not the only success metric.
10. State what an isolated lab cannot prove.

## Project increment (optional)

Run a purple-team exercise against P4 or P10 in an isolated lab under written authorization. Map one emulated technique to ATT&CK, show whether the detection fired, and improve the detection or control. Keep evidence minimal and non-destructive. This is an elective extension to P11/C4, not a new ladder project.

## Exit check

- [ ] show written authorization, scope, and stop conditions;
- [ ] map an objective to techniques and expected telemetry;
- [ ] execute a non-destructive emulation in an isolated lab;
- [ ] measure detection and response;
- [ ] improve one detection with the defender;
- [ ] write an operational report and debrief;
- [ ] state legal/ethical and lab limits.

## Common failure modes

- Running a campaign without a sponsor or written authorization.
- Targeting real people or third-party infrastructure.
- Using live malware or uncontrolled persistence.
- Optimizing for "access" instead of defender learning.
- No deconfliction or emergency stop.
- Leaking sensitive data in reports.
- Treating a missed detection as a tool failure only.
- Claiming production impact from an isolated lab.

## Evidence to commit

- `labs/security/D14/` with campaign plan, authorization, emulation, detection measurements, report
- `notes/security/D14/summary.md`
- sanitized lab diagram and technique mapping

## Optional depth

- *The Red Team Handbook* (University of Washington, public).
- *Adversary Emulation Plans* from MITRE Center for Threat-Informed Defense.
- *Purple Team Strategies* (Kowalski).
- CISA red-team public reports.
- Detection engineering with Sigma and ATT&CK coverage maps.
