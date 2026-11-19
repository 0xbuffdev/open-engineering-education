# SEC1 — Security Foundations & Threat Modeling

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEF10](../SEF/SEF10.md) — assessed completion of Software Engineering Foundations
**Duration:** 7–10 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–12 focused hours/week (provisional; 70–120 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**Security engineering begins with a defensible claim about what a system must protect, against what, and under which assumptions.** Learners establish authorized review boundaries; reconstruct a software system's actors, assets, state and trust relationships; derive threat and abuse hypotheses; assess consequential risk under uncertainty; and turn chosen controls into testable security requirements. They must communicate an honest, prioritized security decision and defend it when the system changes. A scanner report, generic checklist or colorful diagram cannot substitute for this reasoning.

**Context and scope.** Security practice protects people, systems, operations and information. Confidentiality, integrity and availability are important but incomplete: identity, privacy, authorized use, recoverability and accountable decisions depend on context. Threat modeling brings together architecture, realistic adversary capabilities, security properties, potential harms, control choices and reviewable evidence. STRIDE, abuse cases and attack paths are useful prompts, not proof of exhaustive coverage. The result is a revisable engineering argument, not a certificate of safety.

**Preparation and ownership.** [SEF10](../SEF/SEF10.md) represents assessed foundation-level programming, tests, C memory, Unix interfaces, workflow and professional responsibility. SEC1 uses that preparation rather than reteaching basic code or networks. Brief examples of sessions, roles and access decisions develop a model of authority; [SEC2](SEC2.md) owns actual application vulnerabilities and repairs. SEC3–SEC8 own their distinct specialized risks, and [SEC9](SEC9.md) integrates previously assessed capabilities. No unmerged AI course, paid platform, production security clearance or specialist exploit skill is needed here.

**Access, reproducibility and safety.** A learner-controlled loopback application or a supplied fictional system with explicit semantics is sufficient. The system must contain different actors, a protected resource, a meaningful authority/trust boundary and at least one external dependency or untrusted input. Use labeled data-flow diagrams *or equivalent textual tables*, plus supplied request traces, small programs or paper reasoning. No privileged OS access, commercial scanning tool, live production target or internet exploitation is required. Before examining a real system, record the owner's permission, exact scope, exclusions, data handling, stop rules and escalation channel. Public reachability, a software license or curiosity does not constitute permission.

**Workload and completion.** The proposed 7–10 weeks at about 10–12 hours/week is an unverified allocation for understanding an architecture, formulating falsifiable threats and controls, constructing independent expected results, revision and an unfamiliar defense. One coherent case grows through three distinct summative assessments, without three independent applications or mandatory reports for each lesson. All other investigations are optional formative feedback. Learner-tested duration and course readiness cannot be inferred from the source alone.

## Learning outcomes

- **SEC1-O1:** Define and defend authorized review scope, legitimate purpose, system ownership, exclusions, rules of engagement, sensitive-data limits, stop criteria and escalation, and reject actions not covered by permission.
- **SEC1-O2:** Reconstruct and challenge a software system's protected assets, harms, actors, data/control flows, trust boundaries, privileges, dependencies and assumptions, distinguishing documented facts from unknown behavior.
- **SEC1-O3:** Derive and compare specific threat and abuse hypotheses from plausible attacker goals, starting capability, preconditions, boundary crossings and resulting harm; identify unsupported or overlooked paths instead of naming generic vulnerability categories.
- **SEC1-O4:** Prioritize threats and select proportionate treatments using consequences, likelihood or exposure assumptions, control feasibility, evidence uncertainty and residual risk, assigning accountable decisions without false numerical precision.
- **SEC1-O5:** Derive enforceable security requirements and independently checkable allowed, denied, invalid and failure-path tests for important threats, naming enforcement authority, expected state and verification limits.
- **SEC1-O6:** Re-evaluate a threat model when architecture, attacker capability, dependency behavior or new evidence changes; identify invalid assumptions, missing controls and regression checks without mistaking old passing tests for complete assurance.
- **SEC1-O7:** Produce clear developer-actionable remediation and decision-maker risk communication, explain trade-offs, evidence and remaining uncertainty, and independently defend or correct a decision on an unfamiliar bounded case.

## Modules

### Module 1 — Protection Goals and Authorized Work

#### Outcomes

- SEC1-O1
- SEC1-O2
- SEC1-O4

#### Lessons

1. **Protection properties in context** — Compare confidentiality, integrity, availability, authenticity, privacy and continuity for a note-sharing service. Identify people, operations and data harmed by distinct failures; reject the unsupported inference that encrypted transport alone makes a system secure.
2. **Assets, stakeholders and consequences** — Distinguish people, protected data, service functions, reputation and operational dependencies from the components that store or use them. Formulate concrete harm scenarios and identify why two apparently similar data disclosures may have different consequences.
3. **Scope, consent and responsible testing** — Define owner, allowed targets, accounts, methods, time, private data, stopping and notification conditions. Compare authorized local review with an out-of-scope public endpoint; practice stating a refusal and escalation without conducting the test.
4. **Security claims and epistemic limits** — Separate security objectives, documented constraints, observations, hypotheses and unknowns. Critique a claim based only on an absent incident or a green test. State which safe observation could disprove it.

*Optional feedback:* Critique a fictional review charter for missing permission, an unowned risk and an unsupported guarantee.

### Module 2 — Software Decomposition and Trust Boundaries

#### Outcomes

- SEC1-O2
- SEC1-O3
- SEC1-O5

#### Lessons

1. **Legitimate requests and protected state** — Trace an authorized operation from actor to endpoint, service, storage and dependency, including state changes and data classification. Contrast it with a prohibited action using the same components.
2. **Entry points and trust crossings** — Distinguish an actor, asset, API, untrusted input, access-controlled operation and trust boundary. Mark changes of authority across process, tenant, service or organizational boundaries, not just network arrows.
3. **Identity claims and enforcement** — Trace authentication evidence, subject identity, policy, authoritative authorization decision and denied write. Explain why a disabled UI button or client-side role variable cannot enforce server-side authorization; concrete app repair remains SEC2's responsibility.
4. **Dependencies and failure behavior** — Analyze a failing identity provider, stale permission cache, third-party webhook or shared secret. Predict whether failure preserves or bypasses the protected boundary and identify what the diagram omitted.
5. **Internal model consistency** — Cross-check an asset table, data-flow view, request traces and privileged state against each other. Find a missing background path, overlooked actor or contradictory assumption; revise the model using evidence rather than embellishment.

*Optional investigation:* Model a synthetic shared-note application with an owner, collaborator, anonymous viewer and untrusted webhook. Supply a text table if a diagram is inaccessible.

### Module 3 — Threat Hypotheses and Abuse Reasoning

#### Outcomes

- SEC1-O2
- SEC1-O3
- SEC1-O4

#### Lessons

1. **Adversary objective and initial capability** — Name what an adversary seeks and can actually influence, which protection they must cross and which preconditions matter. Reject a path that silently assumes administrator access.
2. **Structured threat discovery** — Use STRIDE or another declared method to challenge *actual* flows for spoofing, unauthorized state changes, disclosure, denial and accountability failures. Exclude irrelevant prompts with reasons; method completeness is not security completeness.
3. **Abuse cases and causal paths** — Turn a concrete harmful outcome into a sequence of required steps and broken invariants, contrasting one-step authorization failure with a chain involving an untrusted dependency. Identify a boundary that could interrupt the path.
4. **Threat confidence and coverage** — Distinguish proven behavior, plausible but untested conditions, a generic weakness category and irrelevant speculation. Challenge one assumption using a counterexample and describe high-value paths the current model may have missed.

*Optional feedback:* Sort supplied threat statements by evidenced, conditional, unsupported and out-of-scope, with a falsifiable reason for each decision.

### Module 4 — Risk Treatment and Security Verification

#### Outcomes

- SEC1-O3
- SEC1-O4
- SEC1-O5
- SEC1-O6

#### Lessons

1. **Risk, impact and uncertainty** — Compare harms, reachability, attacker constraints, control strength and observation quality for two threats. Explain why multiplying arbitrary severity numbers or copying CVSS cannot establish organization-specific risk.
2. **Treatments, owners and residual exposure** — Compare prevention, detection, containment and recovery, plus avoid/reduce/transfer/accept decisions. Assign responsibility and identify the strongest rejected alternative and what remains uncontrolled.
3. **Enforceable security requirements** — Express an invariant such as “only a current collaborator may alter a note” with the responsible server decision and protected state. Contrast actual enforcement with UI convention, logging alone and an informal policy.
4. **Independent security test oracles** — Derive allowed and denied behavior, revoked permissions, malformed inputs and dependency-failure results *before* implementing a check. Separate an HTTP status from persisted state and an implementation's output from its own truth oracle.
5. **Control validation and change-sensitive retesting** — Map threats to requirements, expected observation, negative and failure cases, reproducible fixture or trace, and the conditions under which old evidence becomes stale. State what a passing case cannot prove.

*Optional feedback:* Fix a proposed authorization test that checks only “403” while a prohibited state change still occurs.

### Module 5 — Assurance Review, Revision and Communication

#### Outcomes

- SEC1-O1
- SEC1-O4
- SEC1-O5
- SEC1-O6
- SEC1-O7

#### Lessons

1. **Architecture changes and new paths** — Revisit the threat model after adding a sharing feature, background worker, webhook or third-party storage. Predict affected trust crossings and required regression changes before inspecting the new trace.
2. **Evidence-limited review** — Contrast a design claim, a code inspection, an executed test and an unresolved unknown. State which security properties are supported and where the argument remains conditional; do not infer safety from non-observation.
3. **Communicating the engineering decision** — Write a precise engineer-facing fix (broken invariant, control and verification) and a risk-owner decision (impact, urgency, responsible action and remaining uncertainty). Avoid generic “harden security” guidance and unjustified catastrophic labels.
4. **Independent defense and safe closure** — Diagnose a new bounded case, distinguish observations from assumptions, propose a discriminating check and make a correction when evidence disagrees. Identify when the test must stop or escalate rather than extending permission on the fly.

*Optional feedback:* Review a synthetic security report for an incomplete boundary, unsupported severity claim, untestable remedy and missing residual-risk owner.

## Completion requirements

**Three required summative decisions** jointly establish all seven outcomes using one evolving local or synthetic case. Earlier artifacts can be referenced in later assessments, but each distinct criterion must be reviewed. Optional lessons and formative checks are not completion conditions; a generic template, scanner report or memorized STRIDE list alone never passes.

- **SEC1-AS1** — Authorized System and Threat Model
  - **Outcomes:** SEC1-O1, SEC1-O2, SEC1-O3.
  - **Work:** Select a fictional or learner-owned software system with at least two different actors, protected state, a nontrivial authorization boundary and an untrusted input or dependency. Publish the explicit allowed scope and stop rules, model assets/harms/legitimate and prohibited flows, and trace at least three *distinct* plausible threats with actor, goal, initial capability, preconditions, boundary crossing and effect. Investigate an unsupported candidate and explain its exclusion without attempting out-of-scope work.
  - **Criteria:** A reviewer can reconstruct positive and denied behavior and consistently match actors, assets, data flows and authoritative checks across the diagram or table and traces. Each threat is an actual causal hypothesis, not only a named vulnerability category; at least one protects integrity/authorization and one involves a dependency or failure condition. Identified permissions are adequate for every proposed observation, with private data excluded. Evidence differentiates facts, assumptions and uncertainty, and one tempting threat is correctly rejected or qualified.
  - **Evidence:** Target authorization/fictional-case declaration, rules of engagement, labeled architecture or equivalent text table, assets/harms and actor inventory, allowed and forbidden request traces, threats with conditions and outcomes, and documented excluded case. No real secrets or third-party private records.

- **SEC1-AS2** — Risk Treatment and Verification Argument
  - **Outcomes:** SEC1-O3, SEC1-O4, SEC1-O5, SEC1-O6.
  - **Work:** Continue the AS1 case. Prioritize consequential threats through explicit system-specific harm, exposure, attacker preconditions, evidence and uncertainty; compare control alternatives and assign ownership for remaining risk. For at least two distinct priority paths, define enforceable requirements, allowed/denied/boundary and dependency-failure expectations, authoritative state invariants, independently established test oracles and retesting conditions. Implement a small local check **or** give a complete independently replayable synthetic trace where system implementation is not part of this foundation course.
  - **Criteria:** Priorities and residual risk follow the declared consequences and assumptions, not an unexplained numeric formula. Chosen measures interrupt the actual path; a plausible rejected alternative is analyzed. Each proposed check would distinguish enforced from broken authority and includes a negative or failed-dependency condition with expected state. The learner distinguishes executed observations from planned verification and identifies an inconclusive or insufficient test. No unvalidated diagram or single green test is claimed to prove comprehensive safety.
  - **Evidence:** Threat/control/requirement/evidence matrix, risk-treatment reasoning with owner, specific positive and negative expected results prepared independently, reproducible local fixture and outputs where executed or a fully specified textual fixture/traces, and residual-uncertainty statement.

- **SEC1-AS3** — Unfamiliar Change and Security Decision Defense
  - **Outcomes:** SEC1-O1, SEC1-O2, SEC1-O4, SEC1-O5, SEC1-O6, SEC1-O7.
  - **Work:** Respond to a reviewer-provided *unseen* small architecture change, altered permission, dependency failure or attacker assumption. Predict which trusted flows and tests change, find the newly credible threat, revise one appropriate control and independent negative test, and produce separate implementer and risk-owner recommendations. Explain the authorization boundary for the new investigation. Do not recreate the AS1/AS2 reports.
  - **Criteria:** The new analysis follows from explicit changed facts and threat preconditions rather than rote repetition; it identifies a relevant violated or newly protected boundary. Predictions precede observation, and a proposed safe check distinguishes a secure from an insecure behavior under the changed case. The proposed fix is actionable and has an observable acceptance criterion. Communication is proportionate, identifies accountable ownership, remaining risk and limitations, and respects permission and stopping rules. The learner can independently correct a wrong initial hypothesis under review.
  - **Evidence:** Unseen scenario and scope, prior-to-check prediction, affected path and revised test oracle, brief engineer-focused fix and owner-facing risk disposition, plus written, recorded or live defense showing rationale, corrections and unresolved uncertainty.

### Assessment evidence and readiness

For each assessment, record the course/source revision, required outcome IDs, expected independent results, observed outcomes if executed, criteria decisions, material assumptions and any restricted evidence references. Executable artifacts need clean reproduction instructions and environment details where relevant; synthetic arguments require specified semantics and independently reviewable reasoning. A technical defense may be written, recorded or live but must reveal individual understanding.

No unauthorized access, live probing, private information disclosure or exploit deployment is required or acceptable. The `draft` status remains until actual learner and expert review supports promotion; structure checks alone do not establish educational readiness, formal security certification or complete threat coverage.

### Optional disciplinary references

- [NIST NICE Framework](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center) — observable work competencies.
- [NIST SP 800-218 SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) — secure software engineering practice.
- [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — decomposition, threats, mitigations and review.
- [OWASP ASVS 5.0.0](https://asvs.owasp.org/) — concrete verifiable software security requirements.
- [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) — organizational risk and resilience context.
- [MITRE ATT&CK](https://attack.mitre.org/) — observed adversary behaviors as non-exhaustive prompts.

These are public reference aids, not new paid prerequisites or certification claims.
