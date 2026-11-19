# SEC13 — Security Architecture & Control Assurance

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC6](SEC6.md), [SEC10](SEC10.md)
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–14 focused hours/week (provisional; 140–252 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**Security architecture is the engineering of defensible system-wide protection, not the act of drawing more trust-boundary boxes or choosing a collection of well-known security controls.** SEC13 prepares an engineer to translate stakeholder protection needs and realistic harms into verifiable system requirements; compare distinct control architectures across multiple cooperating components; allocate enforcement, accountability, monitoring and recovery responsibilities; build and test an integrated design; construct an evidence-limited assurance argument; and defend that argument when a dependency, attacker path, policy or operating assumption changes.

The **central professional competency** is to distinguish a convincing description of a control from evidence that the control works at the right authority boundary. An identity provider may authenticate a principal while an application still accepts an unauthorized object update; a service mesh may encrypt traffic while a backend accepts forged actor headers; a restrictive UI may hide a forbidden action while a running worker performs it; a healthy security dashboard may report a policy that never reached the host. A design can be locally correct but compositionally insecure, fail open when a dependency is unavailable, or become unsafe after apparently harmless operational change. Learners must establish the real system behavior, compare plausible mechanisms, verify the chosen one and state what remains untested.

**Prerequisites and disciplinary ownership.** [SEC1](SEC1.md) already establishes authorized scope, system harms, threat and abuse models, prioritization, individual security requirements and simple independent test oracles. [SEC2](SEC2.md) teaches actual application-side actor/action/resource authorization and regressions; [SEC4](SEC4.md) teaches host/service/network enforcement; [SEC6](SEC6.md) adds container, CI, cloud/workload IAM and supply-chain assurance; [SEC10](SEC10.md) adds workforce identity/federation, lifecycle and privileged authorization. These foundations arrive through direct prerequisites **SEC6 and SEC10**; repeating them as extra direct edges is unnecessary. SEC13 owns a **distinct system-of-systems design and assurance practice**, not an additional generic threat-modeling course, cloud-IAM tutorial, cryptographic primitive class or production deployment program. [SEC5](SEC5.md) supplies independent applied cryptographic mastery later verified at graduation; SEC13 can use vetted authenticated transport/signature fixtures without requiring full SEC5 completion as an entry gate. [SEC7](SEC7.md) owns full detection and incident response, [SEC11](SEC11.md) endpoint defense, [SEC12](SEC12.md) ongoing vulnerability and asset-exposure management. A system architecture must identify the interfaces to those responsibilities, but this course does not duplicate each operational specialist assessment. [SEC9](SEC9.md) remains the cumulative graduation capstone and cannot substitute for independently assessed SEC13 competence.

**Reference architecture and accessible tooling.** Use an owned, free, versioned, runnable **multi-component reference service** with real protected state: for example, a local HTTP frontend or client, a source-inspectable API, an independently configured background worker or secondary service, a persistent local state store and a separate authorizing or identity component. Different processes or trust authorities must exist where a claimed boundary depends on them; one program pretending to be five services is insufficient evidence of isolation. Supply genuine runnable scripts, a supported local loopback networking arrangement, two synthetic user/role or service identities, ordinary and forbidden operations, at least one asynchronous or delegated action, and a deliberate boundary defect or misconfiguration. A second component may use a small Python/SQLite, Node or Rust service or a preconfigured OCI runtime; no single framework, Kubernetes cluster, commercial IdP, cloud subscription, paid threat-modeling product, production-grade service mesh, enterprise SIEM, dedicated hardware or proprietary policy engine is mandatory.

**Actual control proof.** The assessed environment must permit independent inspection and real corrections to source/configuration, a real local authorization or process/resource enforcement decision, and true protected-state observations after normal/denied/failure cases. Network-only diagrams, a simulated provider IAM result, a scanner green badge, a service returning HTTP 403 after already committing a prohibited write, or tests defined solely by the author under review do not prove architecture assurance. Where cloud IAM, hardware trust, external federation, managed network policy or host-level capabilities cannot run in the authorized fixture, use **authentic named-provider, versioned policy/decision traces** to reason about that specific mechanism and mark them as supplied evidence; do not claim local production enforcement. At least one inter-component trust decision and a dependency-failure behavior must be truly executed in the locally owned system.

**Engineering scope and constraints.** The goal is a realistic bounded security architecture, not building a highly available enterprise platform from scratch. The learner should evaluate concerns such as trusted caller identity, authorization delegation, data/control-plane separation, mutually authenticated communication when applicable, limited service authority, failure/retry semantics, log/data exposure, supply-chain provenance, recovery control and continued legitimate service. They must identify any security assumptions of third-party components, cloud services, shared storage and platform operations, but unsupported claims remain explicitly conditional. A formal quantitative assurance case or exhaustive theorem proving is **not** required; a transparent claim → argument → independently observed evidence → unresolved assumption structure is required. Risk acceptance remains a named owner decision, never a self-certified security guarantee.

**Authorization, safety and honest claims.** Use written or otherwise reviewable ownership, permitted source/processes, synthetic data/accounts, safe tests, network/resource ceilings, evidence-handling and reset rules before probing the fixture. Never connect an assessment runner to an unmanaged corporate environment, run unauthorized penetration tests, copy credentials from a real IdP, expose actual customer data, disable live policy enforcement or install a dangerous payload. A small intentionally defective authentication, service-to-service or worker authorization rule with protected synthetic state is sufficient. Use fake secrets and redacted evidence. Learners may explicitly choose a **hold/no-go** when a desired property cannot be credibly verified; a hold does not excuse completing the required, separately testable local architecture work.

**Instruction and readiness.** This draft course builds one coherent multi-component system security argument and its executed tests through competency-derived modules and five distinct summative decisions. It expects learners to defend control selection, real implementation, evidence quality and an unfamiliar architecture change, not to memorize NIST control IDs or produce one document per lesson. The **14–18 weeks at approximately 10–14 focused hours/week** is provisional and must be validated through learner and qualified reviewer evidence. Course status remains `draft`.

## Learning outcomes

- **SEC13-O1:** Elicit and justify stakeholder protection needs, authorized mission/service boundaries, material harms, essential operations, privacy/data consequences, threat starting capabilities, legal/contractual assumptions and owners across a cooperating system, distinguishing declared goals from independently verified state.
- **SEC13-O2:** Reconstruct a versioned, source-attributed multi-component architecture including actor/service/workload identities, data/control flows, process, host, network, tenant, deployment and organizational trust boundaries, permission propagation, shared failure points, dependency assumptions and evidence limitations.
- **SEC13-O3:** Derive architecture-level security invariants, misuse/failure conditions, resilience and recovery objectives and independently decidable requirements from harm and trust paths, with traceable authority, verification conditions and legitimate-function constraints.
- **SEC13-O4:** Compare at least two materially different security architectures for real system goals—central versus distributed enforcement, direct versus delegated authority, split policy-decision/enforcement points, shared versus isolated privilege, synchronous versus asynchronous trust or fail-open versus fail-closed dependency handling—and defend controls using threat, feasibility, operational cost, usability, resilience and residual risk.
- **SEC13-O5:** Allocate and verify control responsibility across components and teams, identifying policy decision, policy enforcement, authenticating issuer, caller identity, resource ownership, log/monitoring source, approval, exception, recovery and change authority without falsely equating configuration, a signed assertion or a monitoring event with actual enforcement.
- **SEC13-O6:** Design and verify cross-boundary authorization and least-authority composition for at least one actual inter-service, background job or delegated operation, including confused-deputy, misbound tenant/resource, stale identity, insecure retry or alternate-path failure with independently observed allowed and forbidden protected state.
- **SEC13-O7:** Evaluate security-relevant dependency and trust failure including unreachable identity/policy service, malformed policy result, message duplication/reordering, stale cache, failed side effect, partial transaction, replay and boundary changes; specify and execute safe fallback/containment and recoverability without substituting blanket outage for a successful control.
- **SEC13-O8:** Design source- and time-qualified assurance evidence for each major system claim, distinguishing reviewed design, effective configuration, genuine executed control, independent state tests, authentic supplied provider evidence, detection-only telemetry and unresolved assumptions; use counterexamples and negative tests to probe assurance strength.
- **SEC13-O9:** Build and maintain a traceable assurance case linking stakeholder harm → security requirement → control and enforcement owner → expected positive/negative/failure behavior → evidence and review outcome → residual risk and decision authority, with no unsupported regulatory or complete-security certification claim.
- **SEC13-O10:** Integrate threat modeling, system requirements, controlled changes and independently executable checks into architecture governance and design review, explaining when changed software supply chain, service ownership, privilege, endpoint posture, data flow or dependency invalidates earlier evidence.
- **SEC13-O11:** Evaluate security-relevant operational assurance: privilege and policy drift, changed deployed source/build or artifact, detection/evidence quality, data handling, restore/failover authority, availability cost, maintenance and independent security regression in a bounded real system rather than claiming a full enterprise rollout.
- **SEC13-O12:** Communicate an accountable architecture decision with rejected alternatives, engineering constraints, effective controls, evidence limits, risk-owner approval, safe release/hold, rollback and future re-verification triggers, separating developer changes from executive/business acceptance.
- **SEC13-O13:** Independently predict, investigate, correct and defend a reviewer-selected unfamiliar system architecture or trust change, using genuine executable local inter-component behavior and appropriately labeled external evidence to revise the security case without concealing uncertainty or losing legitimate operation.

## Modules

### Module 1 — Protection Needs and a Real Multi-Component System

#### Outcomes

- SEC13-O1
- SEC13-O2
- SEC13-O3
- SEC13-O5

#### Lessons

1. **From a feature to a protection need** — Given a runnable synthetic records service, local worker, state store and an identity/permission source, identify users and operators, service purposes, permitted records/actions, dependent business operations and plausible harms. Contrast a user-visible success with the actual state-changing authority and a prohibited alternate path. Obtain explicit local assessment permission, stop/reset conditions and responsible decision owner.
2. **Where authority crosses the real system** — Trace a normal client request through API, identity/resource decision, queue or job, worker and persistent state using current source/configuration and real process identities. Distinguish actor subject, caller/workload identity, delegated end-user authority, local privileged process, tenant and system operators. Reject architecture diagrams contradicted by the code or a runnable trace.
3. **Trust, dependency and failure mapping** — Identify issuer, authorizing resource, external dependency, untrusted message producer, privileged consumer, shared storage, transport, replay/retry boundary, audit source and recovery operator. Draw at least one credible attacker path and one unavailable-provider or stale-cache condition with a concrete unsafe and legitimate consequence.
4. **Architectural invariants and evidence targets** — Derive invariants such as “a worker may mutate only a resource explicitly authorized for the originating actor at execution time,” “a revoked grant cannot become a fresh authority,” or “failure to obtain a trustworthy decision cannot perform a protected mutation.” State exact approved behavior, prohibited effect, adverse-state oracle and control owner; show how a superficially correct component test can miss the composition failure.
5. **Requirement traceability without compliance theater** — Connect stakeholder harm, security objective, real decision owner, enforcement component, testable positive/negative/failure result and evidence state. Separate normative business constraints from an example NIST/OWASP control family; do not infer certification or universal applicability from a numbered requirement.

*Optional formative feedback:* An API correctly denies writes, but a background worker trusts an unverified user ID in a queued message. Locate the still-unprotected authority boundary and write one independent falsifying test.

### Module 2 — Security Architecture Alternatives and Control Allocation

#### Outcomes

- SEC13-O2
- SEC13-O3
- SEC13-O4
- SEC13-O5
- SEC13-O6
- SEC13-O7
- SEC13-O12

#### Lessons

1. **Two credible designs for the same system** — Compare centralized resource authorization at the API against enforcement also performed by the consuming worker, with concrete identity, stale-message, deployment, availability and operating trade-offs. Show how the same actor/resource invariant is supported—or not—by each, using specific source/config and expected state rather than claiming “zero trust” fixes every path.
2. **Policy decision and policy enforcement are separate** — Identify where a policy engine/identity registry forms a decision, how its input subject/action/resource/context reaches the actual mutating process, what proves policy version/current authority and who can modify the rule. Compare a correctly configured but bypassed enforcement point to one with observable denial at the protected store.
3. **Service identity and confused-deputy prevention** — Explore workload identity and delegated end-user authority for a real API-to-worker or service-to-service action. Predict attacks using caller-controlled identity headers, wrong audience, broader worker role, missing tenant context or an alternate route. Specify controls that block untrusted delegation without requiring a paid service mesh or public IdP.
4. **Privilege boundaries and layered controls** — Compare process ownership, service credentials, database/resource policies, network restrictions, tenant isolation and supply-chain provenance. Decide which layer must independently enforce a consequential permission, which control only reduces reachability, and where layered mechanisms share the same failure or administrative authority.
5. **Dependency and availability trade space** — Evaluate deny-on-unknown, cached decision with expiry, offline signed authorization, queue delay, idempotency/retry and time-bound emergency override for an unavailable issuer/policy service. Name possible legitimate disruption, unsafe fail-open, recovery authority and evidence needed under changing conditions.
6. **Select controls with an explicit rejection argument** — Produce an engineering comparison of at least two real feasible architectures: protected property, threat, assumptions, authoritative enforcement, direct/maintenance cost, usability, privacy/data exposure, future testability, failure recovery and residual risks. Select one, name its accountable owner and explain why another plausible design was not chosen.

*Optional investigation:* A shared authorization cache increases availability but preserves access after revocation. Propose a bounded fail-safe or revalidation strategy and an executable stale-identity negative test.

### Module 3 — Integration, Failure Propagation and Actual Enforcement

#### Outcomes

- SEC13-O2
- SEC13-O3
- SEC13-O5
- SEC13-O6
- SEC13-O7
- SEC13-O8
- SEC13-O10
- SEC13-O11

#### Lessons

1. **Reproduce an inter-component control defect** — In the pre-provisioned owned service, execute a permitted resource mutation from a verified actor and a forbidden or misbound action submitted through a distinct source/worker trust path. Observe actual protected data after processing rather than relying on HTTP/queue acknowledgment. Trace the specific code or policy that makes the wrong authority decision.
2. **Implement an enforcing architecture correction** — Repair the API-to-worker authority contract or equivalent inter-service boundary with explicit actor/action/resource, trusted provenance, current permission and minimal worker role. Execute tests against actual processes and state store; verify the allowed operation still succeeds and the forbidden action cannot write through a different route, identity or tenant.
3. **Duplicate, replayed and reordered work** — Apply bounded harmless replay, duplicate delivery, stale context or out-of-order authorization events to the real local workflow. Prove whether the worker maintains idempotent and least-authority behavior, and correct missing freshness/authorization checks without pretending to model an unavailable cloud queue exactly.
4. **Dependency failure without privilege escalation** — Safely make the local permission source unavailable or return malformed/unknown decisions, and independently observe the service's safe fallback and remaining legitimate function. Compare availability and harm for fail-closed, restricted read-only, cached-authority TTL or approval hold under named policy; “all services stopped” is not a complete architectural assurance argument.
5. **Control boundaries across infrastructure and source** — Inspect runtime identity, source/build input, least-privilege storage account and any real available local networking/resource rule. Identify which controls are actually enforced locally versus supplied provider evidence, and verify one changed control configuration cannot silently override the chosen resource invariant.
6. **Effect, detection and recovery are different facts** — Generate a real local allowed/forbidden/failure event, measure actual protected state, trace the decision and audit coverage, then restore a safe versioned fixture after a changed deployment or policy. Preserve evidence and distinguish successful alerting, effective prevention, service restoration and remaining untested paths.

*Optional formative feedback:* Two independent components both log “denied,” but a delegated worker still writes a protected record. Require the actual authoritative state test that exposes the incorrect architectural claim.

### Module 4 — Assurance Cases, Independent Tests and Design Governance

#### Outcomes

- SEC13-O1
- SEC13-O3
- SEC13-O4
- SEC13-O5
- SEC13-O8
- SEC13-O9
- SEC13-O10
- SEC13-O11
- SEC13-O12

#### Lessons

1. **Make the assurance claim falsifiable** — Define a precise system-level guarantee and boundary rather than “secure architecture.” Identify claims about legitimate service, unauthorized mutation, availability under dependency failure, privacy/data handling and evidence quality. For each claim, name the authoritative component and what observation would disprove it.
2. **Evidence provenance and independence** — Connect actual source revision, running process/policy, meaningful data state, test actor, expected/observed action, independent review and timestamp to a claim. Compare an architectural drawing, linted policy file, simulated provider decision, signed artifact, independent local effect test and authentic supplier trace. Label each accurately; do not aggregate weaker evidence into a false certainty.
3. **Negative and fault-injection assurance** — Review independently specified legitimate, prohibited, invalid, replay and dependency-failure oracles; execute at least one counterexample or controlled fault against real local components. Reintroduce a safe previous weakness or use an equivalent changed path to demonstrate that the regression detects a broken control rather than passing even when security fails.
4. **Traceability and real control assessment** — Construct a lightweight claim/argument/evidence record for important protection needs: harm → security requirement → control and owner → authority point → evidence → reviewer decision → residual assumption. Use [NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) examine/interview/test thinking where appropriate, not a demand to complete an entire government audit.
5. **Assurance limitations and shared failure modes** — Examine independent versus correlated verification: tests by the same implementation owner, stale CI artifact, offline authorization fixture, provider IAM trace, shared administrator, clock skew, audit loss, critical dependency and changed system topology. Describe what additional real test or external qualified review is needed before a stronger production deployment claim.
6. **Architecture review and accountable acceptance** — Conduct a review that includes threat/requirements trace, alternate design, demonstrated protection, allowed user experience, adverse-case behavior, residual exposure, accountable risk owner, update/rollback controls and explicit pass/hold/no-go conditions. Communicate both implementer changes and nontechnical decision trade-offs without conflating acceptance with guaranteed safety.

*Optional investigation:* A complete-looking assurance diagram contains only policy configuration screenshots and successful login traces. Identify missing cross-component enforcement evidence and propose a discriminating local negative test.

### Module 5 — Unfamiliar Architecture Change and Individual Defense

#### Outcomes

- SEC13-O1
- SEC13-O2
- SEC13-O3
- SEC13-O4
- SEC13-O5
- SEC13-O6
- SEC13-O7
- SEC13-O8
- SEC13-O9
- SEC13-O10
- SEC13-O11
- SEC13-O12
- SEC13-O13

#### Lessons

1. **Predict a change before inspecting its consequences** — Receive a reviewer-chosen bounded new component, identity issuer, service worker, tenant split, queue retry policy, permission-cache expiry, control ownership, deployment artifact or dependency failure. Write an expected permitted and forbidden result plus a competing explanation before inspecting decisive source/response data. Identify which previous assurance evidence is now stale.
2. **Test and revise the actual assurance argument** — Execute the unfamiliar condition in the owned service or inspect an authentic versioned external trace where a provider-specific mechanism is unavailable. Check real actor/resource state, normal and prohibited operations, altered route and failure handling. Correct the precise enforcing component or justify a bounded safe hold; update requirement-to-evidence and residual-risk links rather than only editing a diagram.
3. **Defend the security decision independently** — Present a reproducible running architecture, two candidate control designs, approved authorization scope, verified current protection, counterexamples, dependency effects, source and test versions, affected stakeholder needs, named release/risk owner and evidence-qualified decision. Independently answer unseen source/policy/trace and cost/security questions, acknowledging claims beyond the observed fixture.

*Optional formative feedback:* The review adds a new background consumer with elevated permissions. Explain why the original API authorization tests no longer establish the overall mutation guarantee and what fresh evidence is required.

## Completion requirements

**Five required summative assessments** establish SEC13's independent system-security design and assurance competency. One owned, functioning multi-component source/state fixture may be reused, but each assessment has distinct evaluation claims; optional lesson investigations are not hidden admission or graduation conditions. Evidence must distinguish **actually executed controls** from reviewed policy/configuration, authored security diagrams, genuine supplied provider decisions, modeled behavior and unresolved assumptions. Each assessment identifies `SEC13-AS#`, mapped `SEC13-O#`, owner permissions, versioned system boundaries, independently predicted normal/denied/adverse behavior, effective evidence sources, decisions and individual contribution.

- **SEC13-AS1** — Stakeholder Protection Needs and Cross-System Requirements
  - **Outcomes:** SEC13-O1, SEC13-O2, SEC13-O3, SEC13-O5, SEC13-O8, SEC13-O9.
  - **Work:** Select an authorized, functioning, source-inspectable multi-component service with two or more genuinely distinct process/trust authorities, synthetic users, protected persistent state and a delegated or asynchronous operation. Independently reconstruct actual actor/workload identity, source/policy/runner versions, data/control flows, service roles, dependency owners and real protected actions. Elicit concrete legitimate service needs, harmful unauthorized states and dependency failure conditions; write a traceable set of system-level protection invariants and oracles for genuine allow, prohibited, invalid and failure-state cases. Identify at least one materially consequential boundary that a single-API test cannot protect, and explicitly qualify unsupported provider/host assumptions.
  - **Criteria:** The assessment can identify the actual data mutation authority and its real path through components, verify at least one legitimate inter-component effect, and distinguish current observed state from an architecture diagram. Each major requirement has named accountable owner, system-level observable result, independent test plan and realistic threat/benefit link. A policy label, framework control number, generic STRIDE enumeration or test without a protected-state oracle cannot establish a system assurance claim. Scope, safety, data handling, uncertainty and implementation feasibility are independently reviewable.
  - **Evidence:** Authorized system/actor/process boundaries, source and environment revisions, verified normal cross-component operation and protected state, stakeholder/harm ledger, current trust/dependency graph, threat and failure hypotheses, enforceable requirements, independent expected behavior, evidence gaps and owner/approval responsibilities.

- **SEC13-AS2** — Comparative Architecture and Control Allocation Decision
  - **Outcomes:** SEC13-O1, SEC13-O2, SEC13-O3, SEC13-O4, SEC13-O5, SEC13-O6, SEC13-O7, SEC13-O12.
  - **Work:** Compare at least two feasible, materially different architectures to secure the same running local resource and delegated operation: for example, API-only authorization against worker revalidation using current resource permission and minimally privileged service identity. For each, reason from real source/constraints about authentic caller and delegated actor, chosen policy decision/enforcement and resource owner, stale/replayed/alternate path, unavailable dependency, available network/runtime restriction, legitimate service costs, privacy/data access, fault tolerance and rollback. Select one architecture under explicit stakeholder priorities and independently testable assumptions, show why the other remains vulnerable or disproportionately harmful, and map all critical control/accountability interfaces.
  - **Criteria:** Alternative architectures differ at an actual security mechanism and cross-boundary effect, not only diagram styling or the vendor name. Control allocation identifies the authoritative enforcement point in the service that actually mutates protected state, actual policy/identity trust, resource and escalation owner, effective failure modes and feasible tests. Legitimate workload and availability are considered along with denied operations. The decision has a reasoned risk/operability argument, real evidence limitations, accountable approval and a testable reason to reconsider if deployment or authority changes. Merely saying "zero trust" or citing NIST 800-53 controls without tests fails.
  - **Evidence:** Versioned competing architecture decision records, actual service traces/role mapping, authority/control comparison, threat/requirement-to-owner allocations, expected normal/denied/dependency-failure state for both, explicit rejected alternative, cost/risk/rollback trade-offs, named accountable reviewer and verification plan.

- **SEC13-AS3** — Executed Cross-Boundary Protection and Failure Assurance
  - **Outcomes:** SEC13-O2, SEC13-O3, SEC13-O5, SEC13-O6, SEC13-O7, SEC13-O8, SEC13-O10, SEC13-O11.
  - **Work:** In the learner-owned system, actually reproduce a cross-component permission, identity/delegation or asynchronous worker defect; independently inspect source/configuration, process identities and protected persistent state. Implement a real minimally scoped application/worker/policy correction at the component exercising the consequential authority, not an interface-only filter. Demonstrate a legitimate operation still commits its intended result, at least one prohibited cross-tenant/actor/stale-message operation cannot commit, and an unknown/unavailable permission decision or replay/failure condition cannot silently escalate authority. Execute a safe changed route, duplicate message or dependency failure; verify rollback or recovery where appropriate. Include a safe reintroduced flaw or equivalent mutation that makes an independent negative oracle fail.
  - **Criteria:** The protected-state and service observation originates from actual local processes with a genuine inter-component trust boundary and current source identity; neither a single mocked function nor an HTTP 403 with a completed forbidden write qualifies. A distinct legitimate and denied operation are independently observed; a changed message, tenant, route, retry or unavailable authority probes the chosen control's real enforcement. An effective correction preserves justified service and fails safely under named adverse conditions; availability costs and ambiguous states are acknowledged. A supplier simulator can inform a particular external mechanism but cannot be passed off as this local execution.
  - **Evidence:** Owner-approved target and source/actor/policy inventory, reproducible local startup and controlled stop/reset, original allowed/unsafe state trace, minimal source/configuration diff, executed cross-component allowed/denied/invalid/failure and replay/mutation cases, protected resource observations, versioned log/telemetry provenance, rollback and residual limits.

- **SEC13-AS4** — Independent Control Assurance Case and Architecture Review
  - **Outcomes:** SEC13-O1, SEC13-O3, SEC13-O4, SEC13-O5, SEC13-O7, SEC13-O8, SEC13-O9, SEC13-O10, SEC13-O11, SEC13-O12.
  - **Work:** Assemble a transparent, concise assurance record for the approved design: stakeholder harm/protection goals, independently decidable system requirements, architecture choice and rejected alternative, authority and maintenance owners, policy decisions versus actual enforcement, actual local positive/negative/fault checks, evidence provenance, external provider assumptions, monitoring/rollback and owner residual-risk decision. Have an assessor independently review the claim-evidence relationships, re-run a critical local test or inspect an equivalent source-backed independent record, challenge a policy-only or detection-only assertion and identify an intentionally stale/unsupported claim. Recompute which claims remain defensible after a controlled component, issuer or owner change and which require new tests.
  - **Criteria:** The assurance case has auditable linkages from protection need to independently verified current control, and the reviewer can falsify a consequential requirement when the relevant enforcement is broken. Tests and claim scope are separable from implementation author optimism, supply-side diagrams and incomplete policy configuration. Evidence of actual denied protected state is not confused with logs of a denied request, and an unavailable platform capability is marked with authentic supplied source and appropriate uncertainty. Residual hazards, accepted exceptions, approval authority, service trade-offs, revalidation and hold conditions are clear. No claim of full system proof, government framework certification or enterprise penetration-test coverage is asserted.
  - **Evidence:** Compact claim/argument/evidence table, source-and-risk traceability graph, executed independent test results and reintroduced-fault observation, verified environment/actor versions, authentic supplier limitations, alternative design and reviewer comments, risk-owner release/hold record and review trigger.

- **SEC13-AS5** — Unfamiliar Security Architecture Change and Individual Defense
  - **Outcomes:** SEC13-O1, SEC13-O2, SEC13-O3, SEC13-O4, SEC13-O5, SEC13-O6, SEC13-O7, SEC13-O8, SEC13-O9, SEC13-O10, SEC13-O11, SEC13-O12, SEC13-O13.
  - **Work:** Receive a reviewer-selected unknown but bounded change in a new trusted component, async consumer, workload identity, tenant/source-of-truth switch, policy decision cache, retry/duplicate order, permission-provider outage or supply-chain source revision. Before inspecting decisive outputs, predict how an allowed and prohibited action should affect real protected state, identify an alternative causal explanation and which prior assurance record would become stale. Execute the change against the approved local system or use authentic named external evidence where a specific provider capability is unavailable. Repair the correct enforcement point or defend an enforceable narrow hold; rerun real local legitimate, forbidden, changed-path and failure/recovery checks; reconstruct updated control ownership, alternatives, assurance claims, evidence and residual risk. Answer independently chosen source/policy/assurance questions in a written, recorded or live technical defense.
  - **Criteria:** The learner demonstrates transfer to a condition not solved by rehearsing the previous model; the updated architecture argument is causally consistent with observed cross-component protected state and source provenance. A safe local control change produces a measurable effect, or a justified hold blocks the relevant harm while required real baseline evidence remains demonstrated. The defense distinguishes actual executable proof, genuine supplied provider/host traces, source review and untested risk, considers legitimate operation and false denial, and makes appropriate owner-facing decisions. Individual mastery cannot be satisfied by a team diagram, certification badge, a generic checklist, or missing predecessor completion.
  - **Evidence:** New reviewer challenge and pre-observation prediction/alternative, actual changed component/source/actor map, real local before/after allowed/denied/invalid/failure state, minimal correction or enforceable hold, updated source-and-risk assurance trace, rejected alternatives, reproducible independent regression and mutation, owner-facing release/rollback plan and individual source-backed defense.

### Evaluation and professional limits

Each assessor must distinguish **written architecture**, **reviewed implementation**, **actually executing security controls**, **authentic external supplier decisions** and **unverified assumptions**. Running source and a real local trust boundary are compulsory; generic control mapping without genuine protected-state behavior cannot pass AS3 or AS5. Negative and adverse-state tests must be independently predicted, including at least one case that exposes a known controlled defect if reintroduced. A library signature or a cloud IAM simulation is not a system-wide authorization proof; a monitored denied request is not automatically a denied resource write. Real fault handling must be safely bounded to learner-owned services and must state legitimate-function effects.

Successful completion does not provide enterprise security architect certification, exhaustive regulatory compliance, high-assurance formally verified system proof, cloud vendor accreditation, a complete system-of-systems rollout or production security approval. The graduate can design and defend a **bounded professional multi-component security architecture** and trace a meaningful protection claim from stakeholder need to real controls and independent evidence. Unsupported platform mechanisms remain qualified; a no-go recommendation is a valid decision only after required engineering and assessment evidence has been produced. Course readiness remains `draft` pending actual learner and independent reviewer assessment under [Status Labels](../../spec/status-labels.md).

### Optional disciplinary references

- [NIST SP 800-160 Volume 1 Revision 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) — stakeholder protection needs, security architecture, engineering trade space, system requirements, verification and assurance.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/final) and [NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) — control objectives and examine/interview/test assessment thinking; no automatic public certification or blanket control import.
- [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) — policy decision, enforcement, identity and resource access, with actual distributed system assumptions.
- [OWASP SAMM Security Requirements](https://owaspsamm.org/model/design/security-requirements/), [Secure Architecture](https://owaspsamm.org/model/design/secure-architecture/) and [Architecture Assessment](https://owaspsamm.org/model/verification/architecture-assessment/) — requirements, feasible protection design and independent verification/architecture review.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — accountable governance, identification, protection, detection, response and recovery for bounded owner decisions, not a curriculum checklist.
- [OWASP ASVS](https://asvs.owasp.org/) — application-side verifiable requirements when genuinely relevant; a passing application checklist does not establish secure system composition.

The required competence is defined by the explicit `SEC13-O#` and `SEC13-AS#` evidence, not a prescribed framework coverage count, equal number of lessons, vendor product choice or paper architecture portfolio.
