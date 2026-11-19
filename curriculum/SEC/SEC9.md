# SEC9 — Security Engineering Capstone

**Program:** SEC — Security Engineering
**Type:** `project`
**Prerequisites:** [SEC1](SEC1.md)–[SEC8](SEC8.md)
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–14 focused hours/week (provisional; 140–252 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**Security engineering culminates in a defensible decision about a real system and its observed security behavior—not a collection of vulnerability labels, scanner screenshots or disconnected course exercises.** SEC9 is one substantial, cumulative security assessment and improvement project. The learner selects a meaningful, explicitly authorized software/service environment, establishes a verifiable charter and protection goals, reconstructs its trust and dependency boundaries, derives risk-led hypotheses and independent test oracles, demonstrates a material controlled security failure or attempted bypass, repairs or verifiably contains its cause, validates legitimate and prohibited behavior, exercises security detection and proportionate incident handling, and defends the final risk/release decision when an unfamiliar condition changes. The work must be independently reproducible, technically attributable and honest about gaps.

**A separate predecessor completion decision protects graduation.** Before admission to assessed SEC9 work, there must be independently reviewable satisfactory completion decisions for **every one of SEC1–SEC8** against each course's applicable assessed outcomes and source revision. A record identifies the course code, revision/specification, decision, reviewer and inspectable evidence reference; a governed review can correct an erroneous record but **SEC9 cannot invent credit, substitute project work for an uncompleted predecessor, or silently waive a specialist requirement**. Completing SEC8 alone does not establish independent SEC3 or SEC5 mastery: both and all other required SEC courses must be checked individually. Missing, unverified or inaccessible required completion evidence results in a documented admission hold, not a provisional graduation pass. **Capstone admission and capstone completion are distinct review decisions.**

**One coherent target, not eight replacement projects.** The project must demonstrate substantive cross-boundary security engineering: an actual application, service, native component, identity/resource path or model-assisted tool may be examined in relation to at least one independently controlled permission, runtime, data, delivery or observability boundary. A two-tenant local service with a workload identity, a native-backed authorized processing service, an authenticated local record service or a bounded retrieval/tool application with an independent dispatcher are possible choices. The system must provide actual inspectable functionality, protected state and plausible legitimate users; an architecture diagram alone is insufficient. It is **not** compulsory to implement a native exploit, cryptographic protocol, cloud deployment, incident platform and AI agent together. SEC3, SEC5, SEC8 and other specialist competencies were evaluated in their own required courses; capstone evidence uses them when causally relevant and explains justified non-applicability otherwise. Do not falsely claim that all specialties were assessed again on the chosen target.

**Meaningful newly evaluated integration and authorship.** The learner may reuse a previous owned implementation, approved open-source training code, supplied deliberately vulnerable fixture or freely available security tool. That earlier work must be attributed. SEC9 requires new and personally defensible assessment choices, system-specific security hypotheses, independently prepared expected results, cross-boundary analysis, a material control improvement or tested containment, and a reviewer-supplied unfamiliar variation. Re-running an old SEC2 patch, SEC4 firewall exercise, SEC7 detection worksheet or SEC8 prompt-injection transcript without new project-level causal integration is insufficient. A team may collaborate on a shared target, but each learner's judgments, implementation/review contributions, observations and individual defense must remain separately assessable. Tool-assisted code or generated explanations may be disclosed and reviewed; a learner cannot outsource their assessed reasoning or evidence claims.

**Available target and safe environment.** A freely runnable, user-owned local service and synthetic records are sufficient. An eligible target has protected test resources, distinct legitimate and unauthorized actors, a reproducible state-changing operation or real security control, inspectable application/host/identity events, and a recovery/reset path. A pre-provisioned open-source container may be used where available, but root, privileged packet capture, paid cloud accounts, a public IP, commercial SIEM/EDR, proprietary scanning software, production systems, real customer data, third-party LLM inference or a particular programming language are **not required**. If a selected control requires unavailable kernel or hosted-provider authority, the learner may interpret genuine target-labeled supplied traces for that *specific* control, while a core security boundary, mitigation, test and detection/response effect must be executed in the owned local fixture. Clearly label simulated, executed and supplied results, rather than treating a unit test as proof of global network or cloud isolation.

**Authorization and nonharm are mandatory.** Written or otherwise reviewable owner permission must identify the actual permitted target, actors, synthetic data, tested operations, period, exclusions, network destinations, resource ceilings, observation/collection limits, emergency stop, reporting and evidence-disposal expectations. A public IP address, open-source license or vulnerability disclosure policy is not automatic permission to probe arbitrary assets. Use inert payloads, disposable state, synthetic credentials and local request bounds; no live credential theft, public network scanning, malware, persistence, denial-of-service traffic, real exfiltration or destructive operations are required. Preserve relevant evidence before a potentially destructive local response when safe; revoke or reset only owned test identities and services. A risk finding outside the permitted scope must be documented and escalated, **not tested**.

**What earns a defensible capstone security claim.** At least one priority finding must be grounded in a real controlled behavior or independently reproducible boundary/permission defect. It may arise from an intentionally defective authorized fixture or a new safe reviewer-provided variation: the objective is **causal diagnosis and verifiable correction**, not unsafe discovery on strangers' systems or a quota of vulnerabilities. A finding distinguishes attacker starting ability, conditions, observed effect, protected state, actual enforcement point and a plausible benign alternative; the changed control must be tested through independent legitimate, prohibited, invalid or failure cases and alternative paths relevant to the claim. Demonstrate security visibility with an actual event/detection query and bounded triage/containment/recovery decision connected to the same system. Failure to demonstrate a claimed exploit or security correction is not repaired by a dramatic severity score or polished report. If the responsible decision is to **hold or restrict release**, the learner must still meet the tested evidence and corrective/containment requirements for the owned fixture.

**Project scale, transparency and educational status.** The same versioned target, scope charter, findings, controls, event corpus and operator/runbook evidence progress through five summative decisions; module activities prepare and extend that project rather than create separate labs. The provisional **14–18 weeks at 10–14 focused hours/week** covers target investigation, scoped experiments, evidence and test design, root-cause correction, authentic local security signals and an unfamiliar individual defense. It is a planning estimate rather than empirically established learner workload or a way to waive mastery. Course status remains `draft` until qualified independent educational review and observed learner evidence justify a change.

## Learning outcomes

- **SEC9-O1:** Verify and defend an independently reviewed SEC1–SEC8 predecessor-evidence ledger and explicit capstone admission decision, separating prior specialist mastery from SEC9's new integration requirements and rejecting missing or unverified completion.
- **SEC9-O2:** Select one legitimate, feasible security-assessment target and establish owner authorization, exact scope, protected people/assets, rules of engagement, exclusions, evidence handling, resource limits, stop conditions and reviewable objectives.
- **SEC9-O3:** Reconstruct the target's actors, data and command flows, identity/control planes, trust boundaries, dependencies and operating assumptions using actual source/configuration/state observations, clearly distinguishing verified paths from unobserved claims.
- **SEC9-O4:** Prioritize security risks from plausible attacker starting capabilities, boundary transitions, asset harms, exposure and evidence uncertainty, and justify which integrated paths merit testing versus informed deferral.
- **SEC9-O5:** Derive an independent security verification plan with explicit allowed, prohibited, invalid and adverse-state oracles, test preconditions and alternative routes that would falsify the intended control guarantee.
- **SEC9-O6:** Execute safe, authorized, reproducible tests against a genuinely functioning target or controlled defect, demonstrating a material exposure, unexpected protected-state effect or rejected attack path with accurate observed/supplied/model provenance.
- **SEC9-O7:** Preserve and interpret security-test and incident evidence through source/version, actor, event/time, expected/observed state, integrity and redaction records, explaining what the evidence cannot establish and how collection affects it.
- **SEC9-O8:** Explain and defend the causal root condition of a substantive finding, distinguish vulnerability from symptom, compare proportionate control choices and identify failure paths or assumptions that could defeat a superficial patch.
- **SEC9-O9:** Implement or independently verify a material corrective security control or demonstrably effective containment in the actual owned environment, with real before/after, authorized/denied, changed-path and failure-state regression evidence.
- **SEC9-O10:** Evaluate the selected system's detection and response readiness through an executed behavior-sensitive security signal, independent benign/hostile-like cases, controlled triage, preservation/containment trade-offs, and verified recovery or justified continued hold.
- **SEC9-O11:** Integrate applicable specialist controls and explain non-applicable ones across application, native-code, infrastructure, cryptographic, cloud/identity, detection and AI-assisted trust boundaries, without inventing new feature obligations or substituting a single case for prerequisite mastery.
- **SEC9-O12:** Deliver one reproducible, accessible, source-attributed and privacy-safe security project and evidence collection that an independent reviewer can reproduce, challenge and verify from clean authorized state without paid tools or private secrets.
- **SEC9-O13:** Communicate prioritized, owner-actionable remediation and residual-risk decisions to technical and nontechnical audiences, choosing and defending release, restrict, hold or no-use with explicit acceptance authority, operational costs and review triggers.
- **SEC9-O14:** Independently predict, investigate and resolve or responsibly refuse an unfamiliar bounded security/evidence/authority change, demonstrating genuine authorship, correction of an incorrect hypothesis and a reviewable end-to-end technical defense.

## Modules

### Module 1 — Admission, Authorized Target and Security Charter

#### Outcomes

- SEC9-O1
- SEC9-O2
- SEC9-O3
- SEC9-O13

#### Lessons

1. **An authentic predecessor-evidence gate** — Before assessment work begins, obtain a reviewer decision for each of SEC1–SEC8 with course revision, outcomes, required summative completion and usable evidence. Check SEC3 and SEC5 separately despite the SEC8 prerequisite path. Record admit or hold; a capstone proposal or persuasive interview cannot replace a missing predecessor.
2. **One target with consequential security authority** — Select an owned, real locally functioning application, service or control interface with legitimate users, protected state and interacting trust boundaries. Compare it against a smaller, demonstrably equivalent training fixture, reject needless technology inventory and identify the new technical work not previously assessed.
3. **Owner consent and safe operating rules** — Specify exactly which assets/accounts are covered, permitted test actions, target network/host paths, prohibited attacks, duration/resource limits, evidence privacy, reset/rollback, emergency stop and escalation owner. Walk through a case that is interesting but outside scope and justify refusing it.
4. **User harm, technical boundaries and measurable success** — Establish the actual users, data/resource authorities, essential legitimate flows and plausible attacker capabilities. Declare minimum accepted system behavior, confidentiality/integrity/availability goals, bounded control improvement and security-readiness question before modifying the target.
5. **Authorship, prior assets and feasibility** — Label inherited and supplied source, third-party components, collaborative contributions and generated assistance. Identify the learner's newly owned hypotheses, repairs, tests, evidence decisions and individual defense; match scope to free local tools and an independent reviewer's reproducibility needs.

*Optional formative feedback:* Decline a compelling capstone proposal when its SEC3 record is missing or when the only available "target" is a production system without owner permission.

### Module 2 — Cross-Boundary Risk Model and Independent Security Assessment

#### Outcomes

- SEC9-O3
- SEC9-O4
- SEC9-O5
- SEC9-O6
- SEC9-O7
- SEC9-O8
- SEC9-O11

#### Lessons

1. **Observe the actual trust and state graph** — Inspect the target's real source/configuration, user identity, request or tool pathway, protected backing state and separate enforcement/visibility component. Reconcile architecture drawings and documentation with actual listeners, data access, identity checks or controlled outputs. Label every untested segment.
2. **From asset harm to concrete boundary-crossing hypothesis** — Formulate distinct legitimate and unwanted actor/action/resource sequences where a failure in one control can reach another layer. Prioritize by credible precondition, effect and tractable tests, not a scanner severity label or an arbitrary target count.
3. **An independent oracle before execution** — Specify authorized, denied, malformed and failure-state expected state/response for the selected high-risk path, with an alternative route or stale/retry/role-change condition capable of invalidating an incomplete fix. Identify a meaningful benign lookalike and the exact observation that would disprove the original diagnosis.
4. **Safe execution and source fidelity** — Carry out bounded real local requests, identity/state operations or safe sanitizer-based native checks according to the chosen target. Record test actor, input, environment and actual protected-state effect; distinguish executed behavior, supplied authentic specialized traces and hypothetical policy diagrams. Do not inflate a model-generated claim or proxy denial into a proved downstream state violation.
5. **Causal analysis and finding adjudication** — Correlate actual observable effects with the earliest missing or incorrect authorization, interpretation, privilege or cryptographic-state check. Distinguish confirmed weakness, observed denial, misconfiguration, symptom and unresolved hypothesis; verify an independent alternative case, decide risk and identify the smallest credible repair surface.
6. **Responsibility for specialist applicability** — Evaluate whether native memory/ABI, cryptographic key and nonce handling, cloud/container identity, or model/tool data trust is present in this particular target. Connect applicable evidence and controls to SEC3/SEC5/SEC6/SEC8 competence already assessed, and explain exclusions honestly rather than inserting irrelevant features to demonstrate topic coverage.

*Optional investigation:* Compare a finding supported only by an unauthenticated text response with one supported by independently verified protected-state change; determine which security claim the evidence actually establishes.

### Module 3 — Material Correction, Regression and Reproducibility

#### Outcomes

- SEC9-O5
- SEC9-O7
- SEC9-O8
- SEC9-O9
- SEC9-O11
- SEC9-O12

#### Lessons

1. **Design a control at the real authority boundary** — Compare a local server-side authorization check, narrower runtime identity, trusted source policy, safer crypto-library use or genuine tool-dispatch approval against superficial filtering, masking, documentation or relying only on a scanner. Choose the smallest defensible correction with meaningful remaining attack-path analysis.
2. **New authored change, not a replayed course lab** — Apply a real targeted source/config/permission change or contained repair in the approved owned environment. State inherited code, new control behavior, dependencies and required rollback. If a flaw cannot be safely fixed during the project, demonstrate a verifiable restrictive local containment while clearly choosing hold rather than claiming it is fully repaired.
3. **Positive, negative and changed-assumption regression** — Test legitimate functionality, the original prohibited outcome, alternative routes or principals, invalid requests and one meaningful failure condition. Compare actual authoritative records before/after and include a controlled reintroduction or equivalent mutation where safe to show the negative oracle can detect the defect.
4. **Reproducibility and independent evidence scrutiny** — Pin source and free tool versions, maintain synthetic fixture reset instructions and a bounded verification entry point. Have a reviewer reproduce the key observation/fix from clean state or conduct an equivalently independent review of deterministic evidence, explain differences and correct unsupported assertions.
5. **Control trade-offs and residual exposure** — Evaluate what the patch does not protect, downstream dependencies, operational safety, maintenance and the cost of denial or outage. State who must accept remaining risk and what new evidence or changed conditions would reopen the choice; avoid asserting total system security.

*Optional formative feedback:* Show that a successful unit test is generated using the same permissive authorization predicate as the implementation and derive a genuinely independent negative oracle.

### Module 4 — Security Signals, Controlled Incident and Responsible Release

#### Outcomes

- SEC9-O4
- SEC9-O7
- SEC9-O9
- SEC9-O10
- SEC9-O12
- SEC9-O13

#### Lessons

1. **A detection signal connected to the actual finding** — Produce a real local event for the prioritized unauthorized or suspicious behavior at the declared source; implement/execute a narrowly scoped security query or rule with benign lookalike and missed-data cases. Compare alert result, control decision, actual state and logging gaps without redoing all of SEC7 or claiming production detection coverage.
2. **Preservation, triage and containment decision** — For a bounded injected recurrence or new evidence, decide what is truly known, who must be informed, what local information requires preservation and whether to disable a synthetic identity, stop an owned process or restrict a safe route. Execute an approved reversible action; note evidence lost by acting and false-positive/legitimate-user cost.
3. **Recovery with independent security and user oracles** — Restore intended owned test functionality, verify that the prohibited security path remains denied, rerun the detection/signal check and reconcile unresolved effects or still-valid credentials. An unavailable privileged/cloud response may be discussed from authentic supplied traces, never credited as local execution.
4. **Developer and accountable-owner decision** — Present a prioritized technical finding, reproducible repair/retest references and an accessible risk brief. Choose a meaningful local go, restricted go, hold or no-use decision against predeclared criteria; distinguish capstone evidence from external certification, real production readiness or legal authorization.

*Optional investigation:* A harmless local incident is contained but the privileged role remains valid in a supplied cloud-policy trace. Explain which control was verified, which exposure is untested and why recovery cannot be declared complete.

### Module 5 — Unfamiliar Security Change and Independent Graduation Defense

#### Outcomes

- SEC9-O1
- SEC9-O4
- SEC9-O5
- SEC9-O6
- SEC9-O7
- SEC9-O8
- SEC9-O9
- SEC9-O10
- SEC9-O11
- SEC9-O12
- SEC9-O13
- SEC9-O14

#### Lessons

1. **An unseen reviewer-chosen variable** — Receive a bounded unexpected condition in identity, resource ownership, source data, parser/native input, nonce/key state, runtime policy, approval, logging, event clock or recovery procedure as applicable to the selected target. Before execution, predict a normal and prohibited result and a competing explanation, then choose the smallest discriminating authorized test.
2. **Defend or revise the root cause** — Inspect genuinely new trace or test output, qualify discrepancies, reject a false positive or uncover a new path, and implement a minimal patch or justified restrictive hold. Re-run independent approved, denied and failure cases; avoid a new unrelated feature or an unverifiable retelling of the original fix.
3. **Reviewable project, operator handoff and individual authorship** — Present the cumulative source/fixture, independently checked evidence, dependency attribution, test suite, incident decision, operator reset/rollback, privacy limits and residual risks. Answer concrete code/policy/trace questions that reveal personal understanding rather than relying on a team artifact or generated text.
4. **Separate capstone and graduation decisions** — Verify accepted evidence for **all fourteen SEC9 outcomes and all five summatives**, including unfamiliar-case transfer and defense. Independently reconfirm the eight authentic predecessor decisions and their revision-linked evidence; fail or hold appropriately for missing mastery, even when the project appears technically impressive. A cautious no-go release decision can coexist with satisfactory capstone performance when the validated work still meets its published security engineering outcomes.

*Optional formative feedback:* Present a new owner role and a false alert in an otherwise sound target; require a correction that preserves legitimate use and leads to an honest risk decision instead of a generic critical-severity finding.

## Completion requirements

**Five required summative evaluations and fourteen SEC9 outcomes** are assessed **after the independent pre-entry SEC1–SEC8 verification**. An entry hold prevents beginning qualifying capstone work. This is **one cumulative project**, not five applications or duplicate specialist assessments. The same fixture, source revisions, risk model, genuine controlled observations, incident event and corrective control can support several outcome decisions only where the published success criteria substantively establish each. An impressive final defense cannot substitute for failed or unreviewed summative evidence; an excellent prior-course record cannot substitute for newly demonstrated capstone transfer.

**Required cumulative deliverables:** reviewed admission ledger for SEC1–SEC8; authorized target and safety charter; source-attributed operating target and accurate architecture/trust model; prior-to-test security requirements and independent expected outcomes; evidence-backed prioritized findings and controlled real security checks; a meaningful reviewed source/config/permission correction or demonstrably effective bounded containment; replayable positive, denied, invalid and failure regressions; security telemetry with a controlled incident, preservation/containment and recovery verification; evidence/provenance and clean-state reproduction guide; concise developer and owner communication including release/hold decision; an unforeseen bounded challenge with observed correction or refusal; and a reviewable individual technical defense. Related material may be located within one versioned repository and referenced by compact identifiers rather than duplicated into separate mandatory reports.

- **SEC9-AS1** — Predecessor Verification, Authorized Charter and Project Contract
  - **Outcomes:** SEC9-O1, SEC9-O2, SEC9-O3, SEC9-O4, SEC9-O13.
  - **Work:** **Before assessed capstone construction**, verify all eight predecessor courses SEC1–SEC8 individually, naming each applicable revision, actual completion outcome and reviewer/evidence reference; make an admit/hold decision and separately confirm SEC3 and SEC5. Select a single functioning owned target or small authorized synthetic vulnerable training system; define legitimate users, protected assets and a consequential cross-boundary security question, exact permissions, attack/testing exclusions, synthetic identities, resource limits, data/evidence handling, emergency stop, safe reset, project time/technical feasibility and identifiable new learner work. Compare alternative target/control choices and an explicit no-assessment option if authority or conditions are insufficient. State what success and an unacceptable security effect would mean.
  - **Criteria:** No admission without actual prior reviewed completion for each course; missing or undisclosed decisions cannot be replaced with SEC9 artifacts or a fictional equivalence. The target is genuinely runnable and sufficiently meaningful for at least one security boundary plus a separate relevant enforcement/visibility layer; its users, protected state, legitimate operations, attack starting capability and scope limits are concrete. Rules of engagement avoid any unauthorized production, shared-host or third-party impact. The work introduces substantive new system-specific assessment, control and evidence reasoning, rather than a rebranded prior lab or full-platform feature checklist. A different reviewer can tell what will be demonstrated and refused.
  - **Evidence:** Eight-entry predecessor code/revision/completion/reviewer/evidence ledger and admit/hold decision; project and actor/asset brief; authorization and stop/reset charter; initial source/target inventory, plausible threat and resource constraints, feasibility/alternatives, ownership and assistance disclosures, and first versioned acceptance/rejection criteria.

- **SEC9-AS2** — Executed Cross-Boundary Assessment and Causal Security Findings
  - **Outcomes:** SEC9-O3, SEC9-O4, SEC9-O5, SEC9-O6, SEC9-O7, SEC9-O8, SEC9-O11.
  - **Work:** Inspect real target source/config/state and confirm its main identity/resource/trust route. Choose a risk-led hypothesis whose consequence depends on an application/service/component decision and a meaningful separate resource/authority or visibility layer. Derive independently checkable legitimate, prohibited and failure-state results *before* testing. Execute bounded safe local requests/operations; verify the actual protected response or state, actor and layer, check at least one plausible alternate entry or role/expiry/path condition, and document causal distinctions among real violation, denied attempt, hypothetical exposure and supplied specialized observations. Reproduce one material controlled weakness from an approved deliberately defective fixture or identify a safely demonstrated policy defect/failed control; prioritize it and compare competing repairs. For all other SEC specialist fields, make an explicit applicability decision without inventing tests.
  - **Criteria:** The finding is linked to an authorized, reproducible input and actual observed security-relevant state or truthful denied outcome; an unverified scanner finding, guessed secret, unsupported model narration or paper-only architecture cannot pass as executable assessment. Threat preconditions and harm are bounded, not exaggerated. The earliest incorrect enforcement or interpretation assumption is identified and a competing benign/technical hypothesis has been checked. The independent oracle would reveal at least one safely introduced or already present flaw, and the alternate-path investigation demonstrates why a superficial first repair might fail. The learner accurately classifies real local versus genuine supplied, simulated and unobserved boundaries, with no forced implementation of unrelated specialist subsystems.
  - **Evidence:** Versioned actor/asset/trust map, original target revision and redacted scope, independent before-run outcome matrix, reproducible actual normal/denied/failure and changed-context observations, protected-state proof or bounded denial, source/log/trace provenance, causal finding and impact ranking, alternative hypotheses, control options and unapplied-domain reasoning.

- **SEC9-AS3** — Material Control Repair, Independent Regression and Reproducibility
  - **Outcomes:** SEC9-O5, SEC9-O7, SEC9-O8, SEC9-O9, SEC9-O11, SEC9-O12.
  - **Work:** Implement a material authorized source/configuration/permission fix at the observed unsafe enforcement point, or demonstrate a real effective restrictive containment under a documented local hold when the underlying target cannot safely be corrected. Preserve the original failing or explicitly rejected case and a minimum necessary legitimate workflow. Independently test correct, denied, invalid, alternate-path and one meaningful adverse-state case after the change, with a safe defect reintroduction or comparable negative-control check where feasible. Provide all commands, synthetic fixtures, free version-pinned inputs and permitted environment details to reproduce from clean state. Ask an independent reviewer to challenge at least one causal claim or expected outcome.
  - **Criteria:** A real security property improves in the owned target at the declared layer; a prompt-only message, dashboard change, decorative policy description or deletion of all functionality is not an acceptable repair. Legitimate operation and security invariants both hold under meaningful regression and the selected changed/failure path; tests are independent of the flawed rule and detect a relevant reintroduced defect. An effective containment is evaluated as a restricted/hold outcome, not falsely as permanent eradication. Important trade-offs, access/availability effects, reusable prior source, tool versions and untested paths are disclosed. A reviewer can independently reproduce or rigorously challenge the decisive evidence without paid access or private secrets.
  - **Evidence:** Ownable revision and attributed source/config diff, independently specified expected-oracle fixtures, pre/post actual acceptance and protected-state results, alternate/failure or mutation regression, clean-start/run/reset instructions, resource and privacy limits, corrected scope/risk argument and reviewer challenge record.

- **SEC9-AS4** — Detection, Incident Decision and Verified Recovery
  - **Outcomes:** SEC9-O4, SEC9-O7, SEC9-O9, SEC9-O10, SEC9-O12, SEC9-O13.
  - **Work:** Connect the same system's prioritized security path to a locally generated permitted and suspicious/denied event pair and a working bounded event rule/query. Establish independent expected alert and benign/no-alert results and identify missing source, identity or timing coverage. Exercise one authorized controlled recurrence or changed-context incident scenario, determine what evidence warrants triage/declaration, preserve accessible synthetic evidence, select an appropriate reversible local containment or justified refusal, verify actual permitted/denied state, and restore legitimate behavior without re-opening the demonstrated weakness. Present a truthful risk-owner decision (go, restrict, hold or no-use) and concrete follow-up signals, not a second full SOC/IR platform or a production readiness certificate.
  - **Criteria:** Detection logic executes against actual controlled events, not only a checklist or unattested dashboard. At least one meaningful benign lookalike and one missing-data/changed-state case qualify what the alert can prove. Incident handling identifies owner/authority, likely harm, alternative explanation and preservation-versus-containment cost. Real local containment/recovery observations show legitimate action restored and prohibited effect still denied, or a justified hold when recovery is not safe; telemetry behavior is retested. The decision does not overclaim absence of unknown compromise, complete eradication or enterprise-wide coverage, and the stakeholder brief distinguishes observed and recommended controls.
  - **Evidence:** Generated event and detection schema/version, executable rule plus independent positive/negative cases, controlled triage and evidence notes, redacted response/containment action and before/after state, service restore and regression checks, escalation/owner communication, residual coverage and release/hold decision.

- **SEC9-AS5** — Unfamiliar Integrated Security Challenge and Graduation Defense
  - **Outcomes:** SEC9-O1, SEC9-O4, SEC9-O5, SEC9-O6, SEC9-O7, SEC9-O8, SEC9-O9, SEC9-O10, SEC9-O11, SEC9-O12, SEC9-O13, SEC9-O14.
  - **Work:** Receive an independently chosen, previously unseen **bounded** change appropriate to the actual project—such as revoked identity, changed tenant/resource, fresh service listener, altered key/nonce state, native input bound, poisoned retrieval source, tool approval, CI release identity, missing event or modified incident evidence. **Before observing the decisive result**, specify the anticipated permitted and prohibited state and an alternative causal hypothesis. Execute a safe discriminating local test, inspect any authentic labeled external-control fixture, revise or justify the diagnosis, patch/contain/refuse as warranted, and repeat relevant positive, negative, invalid/failure and detection/recovery checks. Present a complete attribution map, accessible clean-reproduction/evidence collection, prioritization and owner-risk recommendation; individually defend implementation, test provenance, trade-offs, applicable and non-applicable specialist transfer and unresolved gaps. The reviewer makes separate recorded decisions for every SEC9 outcome/evaluation and the eight original predecessor courses.
  - **Criteria:** The learner can reason about a changed condition not rehearsed in the initial run, modify the actual correct boundary without unauthorized behavior, and identify counterevidence that should retract a prior claim. Independently derived test oracles distinguish real effect from model-generated or simulated narrative. Correction preserves declared legitimate service or explicitly requires continued hold, and actual executed response/telemetry and risk analysis remain causally consistent. The learner personally explains and can locate source/policy/evidence rather than recite generated prose. All five SEC9 evaluations and all fourteen outcomes receive inspectable satisfactory decisions; each of SEC1–SEC8 remains individually verified. Missing predecessor, unsupported individual authorship or required evidence results in hold or noncompletion regardless of demo quality.
  - **Evidence:** New challenge brief and pre-observation predictions, real/supplied labeled traces and event timing, changed file/policy/control and expected/actual tests, incident/recovery and risk-decision re-evaluation, versioned source/ownership disclosure, accessible written/recorded/live defense, final outcome/assessment decision matrix, and separately signed or reviewable eight-course admission/graduation ledger.

### Graduation and evidence integrity

**Two distinct decisions are necessary:** (1) authentic, individually verified SEC1–SEC8 completion **before** qualifying capstone entry; (2) successful independent review of SEC9-AS1–AS5, **all fourteen SEC9 outcomes** and a substantive new individual project defense. The reviewer records revision, outcome/assessment, evidence location and disposition for each. A hold, needs-repair or failed requirement may be corrected and reassessed with a new explicit decision; neither attendance, time invested, a CI badge, a scanner score nor accumulated project pages can silently turn a missing decision into completion. No optional course or unrelated AI/APP/SYS specialization is added as a new SEC graduation requirement.

Recorded evidence must support replay from a fresh authorized local fixture, keep expected and actual behavior distinct and label any authentic supplied specialized trace. Publish redacted artifacts or provide appropriately access-controlled review where needed; never post customer records, private keys, credentials or unauthorized host data. An independent reviewer should be able to determine the exact tested control, commit/version, operator actions, known untested paths, legitimate-user effects and accountable owner decision. Visual diagrams require equivalent accessible text or tables. An unfavorable but honest **hold** or **no-use** risk recommendation can be academically defensible; it does not excuse absent implemented/verified learning outcomes.

SEC9 remains `draft` pending [Status Labels](../../spec/status-labels.md). Completion demonstrates bounded, evidenced security engineering integration; it does **not** certify a production system, award legal permission to conduct penetration testing, claim blanket vulnerability absence, guarantee live incident-response readiness, establish vendor accreditation or certify regulatory compliance.

### Optional disciplinary references

- [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) — authorized technical testing, planning, execution and reporting; a foundational guide, not permission to test third-party systems.
- [OWASP Application Security Verification Standard 5.0.0](https://asvs.owasp.org/downloads/) — current stable application-control verification requirements where applicable, not a generic graduation checklist or certification.
- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — current incident-response recommendations aligned with CSF 2.0, relevant to bounded triage, action and recovery.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — risk ownership, protection, detection, response and recovery viewed together; the project is not evidence of organizational framework conformance.
- [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — secure software development and risk-reduction practices across the chosen implementation.
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) — appropriate ethical web assessment techniques if the selected target genuinely involves a web application.

These free resources explain representative professional practices; public acceptance criteria above, not a proprietary assessment service or paywalled framework, govern this course.
