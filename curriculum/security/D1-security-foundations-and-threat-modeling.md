# D1 — Security Foundations & Threat Modeling

**Track:** Security · **Prerequisite:** Foundations · **Core** · **Time:** 4 weeks, 60 hours · **Project:** P10 rules of engagement
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Learn to reason about security as a property of a system: assets, actors, trust boundaries, abuse cases, controls, and residual risk. You will produce a threat model and a rules-of-engagement document that govern every later security lab.

## Outcomes

You can:

- define assets, actors, entry points, trust boundaries, and data flows;
- distinguish confidentiality, integrity, availability, authenticity, and privacy;
- apply STRIDE, attack trees, and abuse-case analysis;
- map threats to security requirements, controls, and tests;
- assess likelihood and impact without false precision;
- distinguish a vulnerability, a misconfiguration, and accepted risk;
- write scope, authorization, stop conditions, and evidence rules;
- explain defense in depth and least privilege;
- communicate risk to engineers and decision-makers;
- recognize when an activity requires legal or compliance expertise.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| *Threat Modeling: Designing for Security* (Shostack, 2014) | Ch. **1–11** | STRIDE, diagrams, threat elicitation, management |
| [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) | Full | Practical checklist |
| [OWASP Top 10](https://owasp.org/projects/top-ten/) | Current edition | Web risk baseline |
| [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) | Ch. **1–4** | Risk assessment vocabulary |
| [MITRE ATT&CK](https://attack.mitre.org/) | Enterprise overview, selected techniques | Adversary behaviour model |
| [CVSS v4.0 specification](https://www.first.org/cvss/) | Overview and examples | Severity vocabulary and limits |
| B5 *The Linux Programming Interface* | Ch. **8–9, 15, 17, 38–39** | Users, permissions, process credentials, filesystems, resource limits |

## Modules

### 1. Security fundamentals

- threat, vulnerability, exploit, risk, control;
- confidentiality, integrity, availability;
- authentication, authorization, accounting;
- least privilege, separation of duties, defense in depth;
- fail-safe defaults and complete mediation;
- attack surface and trust boundaries;
- security versus privacy versus safety.

### 2. System modeling

- data-flow diagrams;
- assets and data classification;
- actors and capabilities;
- entry points and privilege levels;
- deployment and supply-chain boundaries;
- human and organizational factors;
- assumptions and unknowns.

### 3. Threat elicitation

- STRIDE per element;
- attack trees;
- abuse cases and misuse cases;
- kill chains and ATT&CK techniques;
- adversary capability and motivation;
- insider and supply-chain threats;
- privacy harms (preview of D10).

### 4. Risk and controls

- likelihood and impact;
- qualitative versus quantitative risk;
- CVSS and its limits;
- control categories: preventive, detective, corrective;
- compensating controls;
- residual risk and risk acceptance;
- prioritization and cost.

### 5. Requirements and verification

- turn a threat into a requirement;
- derive a test or verification method;
- security acceptance criteria;
- regression tests;
- design review versus code review versus testing;
- evidence quality and reproducibility.

### 6. Authorization and professional conduct

- scope, assets, time window, prohibited actions;
- written authorization and sign-off;
- isolation and snapshots;
- data handling and retention;
- stop conditions and escalation;
- disclosure and reporting;
- legal/ethical limits;
- no testing of third-party systems.

## Labs

### Lab 1 — Rules of engagement

Write a complete rules-of-engagement document for a system you own (P1/P4/P9):

- scope and exclusions;
- authorized actions;
- prohibited actions;
- test window and contacts;
- data handling and evidence retention;
- stop conditions and rollback;
- reporting and disclosure.

Have a second person review it for ambiguity.

### Lab 2 — Threat model

Create a data-flow diagram with trust boundaries for a small web or AI service. Apply STRIDE per element, produce an abuse-case list, and prioritize the top five threats. For each, write a requirement and a verification test.

### Lab 3 — Attack tree

Build an attack tree for one high-value asset. Identify the cheapest path and the control that changes the economics. Distinguish prevention, detection, and recovery.

### Lab 4 — Risk register

Create a risk register with ten items. Include cause, impact, affected assets, existing controls, residual risk, owner, and evidence/test. Use a documented ranking method and state its subjectivity.

### Lab 5 — Control verification

Pick one threat from Lab 2 and verify the control empirically in a local environment. Record the command, result, and one bypass/failure case. If the control is organizational, state what evidence would demonstrate it.

## Exercises

1. Classify five assets by sensitivity and criticality.
2. Draw trust boundaries for a three-tier application.
3. Map one scenario to each STRIDE category.
4. Write three abuse cases for an API.
5. Turn a threat into an acceptance test.
6. Compare two controls by cost and residual risk.
7. Explain why CVSS alone cannot prioritize a finding.
8. Explain the difference between authentication and authorization.
9. Write a stop condition for a lab.
10. Review a scope document for ambiguity.

## Project increment — P10 rules of engagement

Produce:

- the P10 scope and authorization document;
- a system/data-flow diagram;
- a threat model with prioritized threats;
- a risk register;
- a verification plan for the top controls;
- a disclosure and evidence-handling policy.

**Brief:** [P10 — secure-review](../projects/project-ladder.md#p10--secure-review)

## Exit check

- [ ] define scope and trust boundaries precisely;
- [ ] produce a threat model another engineer can review;
- [ ] map threats to requirements, controls, and tests;
- [ ] explain residual risk and risk acceptance;
- [ ] distinguish a vulnerability from a misconfiguration;
- [ ] state the authorization and stop conditions for any lab;
- [ ] identify one assumption that needs validation.

## Common failure modes

- Starting with tools instead of assets and boundaries.
- Producing a threat list with no owners or tests.
- Treating CVSS as a complete risk score.
- Testing a system without written authorization.
- Confusing a control's existence with its effectiveness.
- Ignoring supply chain and human factors.
- Calling a risk "accepted" without an accountable owner.

## Evidence to commit

- `labs/security/D1/` with scope, diagrams, threat model, attack tree, risk register, control test
- P10 rules of engagement and threat model
- `notes/security/D1/summary.md`

## Optional depth

- *Security Engineering* (Anderson), selected chapters.
- *The Security Engineer's Interview Guide* or equivalent for breadth.
- NIST Cybersecurity Framework 2.0.
- OWASP ASVS and Testing Guide.
- LINDDUN privacy threat modeling.
