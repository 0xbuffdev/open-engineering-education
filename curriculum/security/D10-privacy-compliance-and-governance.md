# D10 — Privacy, Compliance & Governance

**Track:** Security · **Prerequisite:** D1, D7, D8 · **Core** · **Time:** 4 weeks, 60 hours · **Project:** P11 risk register
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Treat privacy and compliance as engineering constraints with evidence, not paperwork. You will map personal data, assess privacy risk, design retention and access controls, and produce a governance package. This is not legal advice; escalate legal questions to qualified counsel.

## Outcomes

You can:

- distinguish privacy, confidentiality, security, and compliance;
- map data flows and classify personal/sensitive data;
- apply data minimization, purpose limitation, and retention;
- assess privacy risk with LINDDUN or a comparable method;
- design access, deletion, and subject-request workflows;
- review a vendor/data-processing boundary;
- understand GDPR/CCPA/HIPAA obligations at a working level;
- build a risk register and control evidence;
- explain breach notification and incident escalation;
- state jurisdictional and legal limits.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [NIST Privacy Framework](https://www.nist.gov/privacy-framework) | Core functions, profiles | Privacy risk management |
| [GDPR official text](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Art. **5–6, 12–22, 25, 30–35** | Principles, rights, DPIA, security |
| [CCPA/CPRA](https://oag.ca.gov/privacy/ccpa) | Overview and key rights | California obligations |
| [HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html) | Overview | Health-data safeguards (US) |
| [LINDDUN](https://linddun.org/) | Full | Privacy threat modeling |
| [ISO/IEC 27701](https://www.iso.org/standard/71670.html) | Overview | Privacy information management |
| [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Privacy and access-control families | Control mapping |
| [ICO GDPR guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/) | Selected | Practical interpretation |

## Modules

### 1. Privacy fundamentals

- personal data, sensitive data, pseudonymization, anonymization;
- data subject, controller, processor;
- lawfulness and consent (and its limits);
- purpose limitation and minimization;
- storage limitation and retention;
- accuracy and integrity;
- transparency and rights;
- privacy by design and by default.

### 2. Data mapping and classification

- data inventory and flow maps;
- collection points and third parties;
- cross-border transfers;
- sensitive attributes and children's data;
- logs, backups, analytics, and AI corpora;
- classification and ownership;
- data lifecycle.

### 3. Risk assessment

- LINDDUN threat categories;
- likelihood and impact;
- DPIA triggers and structure;
- risk to individuals versus organizations;
- mitigation and residual risk;
- documentation and review;
- when to escalate to legal/DPO.

### 4. Controls and operations

- access control and least privilege;
- encryption and key management;
- retention/deletion and backups;
- subject access/erasure/portability workflows;
- consent management;
- vendor management and contracts;
- audit logging;
- incident and breach notification.

### 5. Governance

- policies and standards;
- roles and accountability;
- training and awareness;
- metrics and audit;
- exceptions and risk acceptance;
- regulatory change management;
- AI-specific privacy (connect AI12/D6).

## Labs

### Lab 1 — Data map

Map personal data for P1/P9 or a hypothetical service: source, purpose, storage, access, retention, sharing, and deletion. Identify one unnecessary collection and one orphaned copy.

### Lab 2 — Privacy threat model

Apply LINDDUN to the data map. Produce at least eight threats, affected individuals, controls, and residual risk. Distinguish privacy from security threats.

### Lab 3 — DPIA

Write a DPIA for a plausible feature (e.g., analytics or an AI assistant). Include necessity/proportionality, risks, mitigations, consultation, and a decision. State that this is a learning exercise, not legal advice.

### Lab 4 — Rights and deletion

Design and test a subject-access and erasure workflow on synthetic data. Include identity verification, scope, backups, logs, third parties, and evidence. Measure whether deletion actually propagates.

### Lab 5 — Vendor and incident review

Review a hypothetical vendor/data-processing agreement against a checklist. Then write a breach-notification timeline and escalation path, including who decides and what evidence is needed.

## Exercises

1. Classify five data fields by sensitivity.
2. Distinguish pseudonymization from anonymization.
3. Apply data minimization to a feature request.
4. Identify a retention violation.
5. Write a DPIA trigger list.
6. Map a LINDDUN threat to a control.
7. Design an erasure workflow including backups.
8. Explain a cross-border transfer risk.
9. Draft a breach-notification decision tree.
10. State when to escalate to counsel.

## Project increment — P11 risk register

Produce:

- data inventory/flow map;
- privacy threat model;
- DPIA-style assessment;
- retention and access policy;
- subject-request/deletion workflow;
- vendor and incident review;
- risk register with owners and evidence;
- legal-escalation note.

**Brief:** [P11 — authorized-assessment](../projects/project-ladder.md#p11--authorized-assessment)

## Exit check

- [ ] map personal data and identify unnecessary collection;
- [ ] distinguish privacy risk from security risk;
- [ ] produce a DPIA-style assessment with mitigations;
- [ ] test a deletion/access workflow;
- [ ] review a vendor boundary;
- [ ] define breach escalation and notification ownership;
- [ ] state clearly what requires legal advice.

## Common failure modes

- Treating compliance as a checkbox.
- Calling data "anonymous" without evidence.
- Retaining logs/backups indefinitely.
- Ignoring third-party sharing.
- Designing consent as the only lawful basis.
- Writing policy with no control or owner.
- Promising deletion without testing propagation.
- Giving legal advice instead of escalating.

## Evidence to commit

- `labs/security/D10/` with data map, LINDDUN model, DPIA, deletion test, vendor review, incident path
- P11 risk register
- `notes/security/D10/summary.md`
- framework editions and jurisdiction record

## Optional depth

- *Privacy Engineering* (Dennedy et al.) or *Understanding Privacy* (Solove).
- *Data and Goliath* (Schneier) for context.
- IAPP CIPP/E materials (if pursuing certification).
- ISO/IEC 27001/27701 implementation guidance.
- AI privacy and data-protection impact assessment guidance.
