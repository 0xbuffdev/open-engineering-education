# D4 — Systems & Infrastructure Penetration Testing

**Track:** Security · **Prerequisite:** D2, D3, S11 · **Core** · **Time:** 6 weeks, 90 hours · **Project:** P11 assessment
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Plan and execute a scoped, non-destructive assessment of a system you own or are explicitly authorized to test. You will practice reconnaissance, validation, controlled exploitation, evidence handling, remediation, and retest — with the report as the primary deliverable.

## Outcomes

You can:

- build an asset and attack-surface inventory from an architecture;
- write a test plan with scope, hypotheses, stop conditions, and rollback;
- perform authorized reconnaissance and service validation;
- distinguish discovery, validation, and exploitation;
- choose non-destructive evidence that proves impact;
- assess severity with environmental context;
- write a developer-actionable finding without weaponized payloads;
- map findings to controls and tests;
- retest fixes and record residual risk;
- handle sensitive evidence and disclosure responsibly.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [PTES](http://www.pentest-standard.org/) | Pre-engagement through reporting | Assessment method |
| [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) | Full | Technical security testing |
| [MITRE ATT&CK](https://attack.mitre.org/) | Enterprise tactics and selected techniques | Adversary model |
| *Penetration Testing* (Weidman, 2nd ed.) | Ch. **1–8, 12** | Practical workflow |
| *The Hacker Playbook 3* (Kim) | Selected, authorized lab only | Alternative workflow; verify currency |
| B5 *The Linux Programming Interface* | Ch. **37–39, 56–63** | Credentials, capabilities, sockets, services |
| [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) | Infrastructure-adjacent test cases | Web surface |
| Provider hardening guides | CIS Benchmarks or cloud security docs | Configuration evidence |

## Modules

### 1. Engagement planning

- scope, assets, exclusions, time window;
- authorization and sign-off;
- rules of engagement;
- success criteria;
- communication and escalation;
- stop conditions;
- data handling and retention;
- emergency contacts and rollback.

### 2. Reconnaissance and inventory

- architecture and trust boundaries;
- DNS, certificates, and exposed services;
- version/banner validation;
- authenticated versus unauthenticated surface;
- cloud metadata and storage exposure (authorized only);
- documentation review;
- avoiding noisy or out-of-scope discovery.

### 3. Validation and controlled testing

- service configuration review;
- authentication and authorization testing;
- credential hygiene;
- known-vulnerability validation;
- safe proof of impact;
- privilege escalation concepts in a lab;
- lateral movement concepts without uncontrolled execution;
- logging and detection observation.

### 4. Evidence and severity

- reproducible minimal evidence;
- timestamps and command logs;
- protecting secrets/PII;
- false-positive elimination;
- CVSS environmental score and its limits;
- business impact;
- vulnerability versus misconfiguration versus accepted risk;
- chaining findings without overclaiming.

### 5. Remediation and retest

- developer-actionable language;
- root cause and compensating controls;
- prioritization;
- fix verification;
- regression tests;
- partial fixes and accepted risk;
- closure criteria.

### 6. Reporting

- executive summary;
- methodology and scope;
- findings with evidence, impact, severity, remediation;
- positive controls;
- limitations;
- retest appendix;
- disclosure.

## Labs

### Lab 1 — Scope and plan

Write a rules-of-engagement and test plan for P4 `workbenchd` or an isolated training network. Include assets, hypotheses, allowed tools, prohibited actions, stop conditions, and a snapshot/rollback plan. Have it reviewed before any testing.

### Lab 2 — Inventory and validation

Build an asset/service inventory from the authorized target. Validate versions and configurations without exploitation. Document what you could not determine.

### Lab 3 — Controlled finding

Find one real weakness in the authorized target. Produce harmless evidence of impact, root cause, and a proposed fix. Do not use destructive payloads or persistence.

### Lab 4 — Report and remediation

Write two findings: one technical and one configuration/process. Include severity rationale, remediation, and a retest procedure. Have a developer review for actionability.

### Lab 5 — Retest

Fix the highest-priority finding. Retest only the agreed path, record before/after evidence, and classify the result as fixed, partially fixed, or accepted risk. Update the report.

## Exercises

1. Write a scope statement with three exclusions.
2. Build an asset inventory from a diagram.
3. Distinguish discovery from validation.
4. Write a non-destructive proof of impact.
5. Score a finding with and without environmental context.
6. Explain why scanner output is not a finding.
7. Write a retest criterion.
8. Identify sensitive data in an evidence packet.
9. Explain a stop condition for availability risk.
10. Draft an executive summary without jargon.

## Project increment — P11 assessment

Produce:

- authorization and test plan;
- asset inventory and attack surface;
- at least three validated findings on the private target;
- minimal evidence and severity rationale;
- remediation guidance;
- retest results;
- residual-risk statement.

**Brief:** [P11 — authorized-assessment](../projects/project-ladder.md#p11--authorized-assessment)

## Exit check

- [ ] show written authorization and scope before evidence;
- [ ] validate findings rather than repeating scanner output;
- [ ] keep testing non-destructive and in scope;
- [ ] write findings a developer can act on;
- [ ] justify severity with environmental context;
- [ ] retest and classify outcomes;
- [ ] protect evidence and state limitations.

## Common failure modes

- Testing without explicit authorization.
- Running exploitation before inventory.
- Using destructive or persistence techniques in a routine assessment.
- Reporting unvalidated scanner findings.
- Inflating severity with a generic CVSS score.
- Storing real credentials or personal data in evidence.
- Calling a partial fix "closed".
- Omitting scope limits from the report.

## Evidence to commit

- `labs/security/D4/` with scope, inventory, validated findings, evidence, report, retest
- P11 assessment report
- `notes/security/D4/summary.md`
- authorization record (sanitized; no secrets)

## Optional depth

- *The Web Application Hacker's Handbook* selected chapters.
- *Red Team Development and Operations* (Vest & Tubberville), planning chapters.
- MITRE ATT&CK technique pages relevant to validated findings.
- CIS Benchmarks for the target OS/service.
- NIST SP 800-53 control mapping (awareness).
