# AI12 — Responsible AI, Safety & Governance

**Track:** AI & ML · **Prerequisite:** AI6 · **Core** · **Time:** 4 weeks, 60 hours · **Project:** P9 system card/risk register

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Make explicit the harms, assumptions, and accountability around an AI system. You will build a risk register, map harms to controls, run a benign red-team exercise on your own artifact, and write a system card that a skeptical reviewer can audit.

## Outcomes

You can:

- distinguish capability evaluation from safety evaluation;
- map intended use, non-use, users, and affected parties;
- identify harms across accuracy, safety, privacy, fairness, security, and autonomy;
- assess risk with likelihood, impact, and uncertainty;
- design measurable controls and residual-risk statements;
- apply current governance frameworks without pretending they are law;
- run a bounded, benign red-team exercise;
- define escalation, incident, and rollback paths;
- document model/data provenance and limitations;
- recognize when a system should not be deployed.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework) and Generative AI Profile | Full | Risk framing |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/) | Current edition | AI security risks |
| [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) | Full | Documentation |
| [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | Full | Data documentation |
| [Fairness and Machine Learning](https://fairmlbook.org/) | Ch. **1–3** | Harms and measurement |
| [EU AI Act](https://artificialintelligenceact.eu/) | Overview and high-risk obligations | Regulatory awareness (not legal advice) |
| [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) | Selected risks/controls | Generative-AI risk management |
| [Anthropic/OpenAI system cards](https://www.anthropic.com/) | One example | Reporting practice |

**Currency rule:** record the edition/date of every framework. AI regulation and taxonomies change; do not present this course as legal advice.

## Modules

### 1. Framing and stakeholders

- purpose and intended use;
- affected people and environments;
- beneficiaries and burden bearers;
- non-use cases;
- deployment context and human oversight;
- accountability and ownership;
- legal/regulatory awareness.

### 2. Harms and risk

- accuracy and reliability harms;
- safety and physical harms;
- privacy and surveillance;
- bias, allocative harm, and representation;
- security and misuse;
- autonomy, manipulation, and dependency;
- environmental and labour impacts;
- severity, likelihood, exposure, and uncertainty;
- risk tolerance and residual risk.

### 3. Controls and evaluation

- data controls;
- model controls;
- system controls;
- human controls;
- monitoring and incident response;
- red teaming and adversarial testing;
- benchmark validity and contamination;
- measurement of subgroup performance;
- control effectiveness and defense in depth;
- safety cases (intro).

### 4. Governance and documentation

- model/system cards;
- data cards;
- risk registers;
- impact assessments;
- audit logs and evidence retention;
- change management;
- vendor/model supply chain;
- incident escalation and notification;
- retirement/decommissioning.

### 5. Red teaming within scope

- rules of engagement;
- benign test cases;
- prompt injection and jailbreak tests on your own system;
- tool and data boundary tests;
- measurement and severity;
- avoiding real harm, private data, and weaponization;
- remediation and retest;
- reporting uncertainty.

## Labs

### Lab 1 — System and data cards

Write a system card for P9 covering intended use, non-use, users, affected parties, data provenance, evaluation, limitations, and operational controls. Write or update the data card for the corpus.

### Lab 2 — Risk register

Build a risk register with at least 12 risks across accuracy, privacy, security, fairness, misuse, and operations. For each: cause, impact, affected group, existing control, residual risk, owner, and test/evidence. Rank with a documented method.

### Lab 3 — Benign red-team

Create a scoped test plan for P9. Test the controls for prompt injection, citation mismatch, tool denial, data leakage, and unsafe output. Record only benign evidence. Fix one weakness with two complementary controls and retest.

### Lab 4 — Evaluation audit

Audit P9's evaluation: split validity, contamination, sample size, metric choice, subgroup coverage, and claims. Rewrite one overstated claim into a precise one. Identify what the evaluation cannot prove.

### Lab 5 — Incident and retirement

Write an incident escalation path for a harmful or leaking output. Define who is notified, what is logged, how the service is disabled, and how the model/index is rolled back. Add a retirement plan for data and artifacts.

## Exercises

1. Distinguish capability from safety evaluation.
2. Map three harms to affected stakeholders.
3. Write a non-use statement for a plausible misuse.
4. Assess a risk with likelihood, impact, and uncertainty.
5. Design a measurable control for one risk.
6. Explain why a benchmark score is not a safety case.
7. Identify a privacy risk in prompt logging.
8. Define a human-oversight condition.
9. Explain one limitation of the EU AI Act's high-risk classification.
10. Write residual risk for a control you cannot fully verify.

## Project increment — P9 system card/risk register

Add:

- system card and data card;
- risk register with owners and evidence;
- benign red-team report and retest;
- evaluation-limitations audit;
- incident, rollback, and retirement plan.

**Brief:** [P9 — doc-compass](../projects/project-ladder.md#p9--doc-compass)

## Exit check

- [ ] state intended use, non-use, and affected parties;
- [ ] map at least six harms to controls and residual risk;
- [ ] distinguish measured controls from assumed ones;
- [ ] demonstrate one benign red-team finding, fix, and retest;
- [ ] audit an evaluation claim and correct an overstatement;
- [ ] show an incident/rollback path;
- [ ] recommend deploy, constrain, or do not deploy with reasons.

## Common failure modes

- Treating a policy document as a working control.
- Claiming "safe" after a narrow red-team pass.
- Ignoring affected people who are not users.
- Reporting aggregate metrics without subgroup analysis.
- Copying a framework without mapping it to the system.
- Logging sensitive data "for safety".
- No owner or rollback authority.
- Presenting regulatory analysis as legal advice.

## Evidence to commit

- `labs/ai/AI12/` with system card, risk register, red-team report, evaluation audit, incident plan
- P9 governance documents
- `notes/ai/AI12/summary.md`
- `notes/ai/AI12/resources.md` with framework editions/dates

## Optional depth

- *Weapons of Math Destruction* (O'Neil) or *Atlas of AI* (Crawford).
- *The Alignment Problem* (Christian).
- NIST AI 100-2 (adversarial ML taxonomy).
- ISO/IEC 42001 (AI management systems) overview.
- *Designing for Safety* and safety-case literature.
