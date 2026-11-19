# SEC7 — Detection, Incident Response & Threat Hunting

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC4](SEC4.md), [SEC6](SEC6.md)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–14 focused hours/week (provisional; 120–224 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**A defensive security conclusion must be traceable from an observable event through a tested detection, preserved evidence, competing explanations, a proportionate response and verified recovery.** SEC7 teaches learners to design threat-informed telemetry; implement and measure detection logic on real generated and independent benign/malicious training records; triage alerts without conflating suspicion and compromise; acquire and preserve accessible host evidence; reconstruct events from imperfect logs and artifacts; conduct bounded hypothesis-driven hunting; and make containment, eradication and recovery decisions with documented uncertainty. One incident timeline or dashboard screenshot does not by itself establish an intrusion, root cause or security improvement.

**Scope and relevance.** Security investigation often begins with incomplete or contradictory signals: a privileged operation lacking an audit event, a suspicious process that is an approved administrator tool, an identity change seen in one log but not another, a host clock skew, or a sequence whose missing events could reflect collection failure. Analysts must separate attacker behavior from benign overlap, decide what evidence could falsify their hypothesis, preserve fragile state without modifying a system they do not own, and protect business recovery. Automated alerts, threat-hunting hypotheses and incident declarations are related but not interchangeable. Evidence fidelity, detection error rates, timeliness and reversibility are engineering properties, not decorative report sections.

**Prerequisites and disciplinary ownership.** [SEC4](SEC4.md) supplies service/host exposure, network policy, security configuration and the limits of enforcement-point observations. [SEC6](SEC6.md) supplies cloud/container/workload identity, local CI/artifact security evidence, redacted control checks and real/supplied evidence boundaries. Their transitive preparation includes [SEC2](SEC2.md), [SEC1](SEC1.md) and the necessary [SEF7](../SEF/SEF7.md) service/process fundamentals. [APP6](../APP/APP6.md) teaches full-application CI, quality telemetry and operational incidents; [APP7](../APP/APP7.md) teaches full deployment, rollback and database recovery. These provide useful examples but **are not SEC7 prerequisites**. SEC7 owns security-specific detection engineering, falsifiable alert evaluation, real user-owned host evidence acquisition, adversary-behavior investigation, justified containment and independently checked recovery; it does not repeat generic software SLO dashboards, CI construction or a full deployment/restore project. [SEC8](SEC8.md) can apply the same investigative methods to model-powered systems. No mandatory SOC employment, production access, vendor SIEM, extra offensive course or privileged kernel-forensics training is assumed.

**Guidance and correct level of claim.** Follow the final April 2025 [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), which integrates incident response throughout CSF 2.0 cybersecurity-risk functions. Preparation, detection, response, recovery, learning and governance interact; do not represent older phase diagrams as normative sequencing or evidence that all incidents progress identically. The current MITRE ATT&CK detection-strategy, analytic and data-component framework supplies adversary-behavior hypotheses and potential observables, **not** turnkey proof that a matching event is malicious. The current Sigma rule specification can express portable detection intent when source fields, conversion and actual engine semantics are known. Test **the executed rule or query**, not merely whether a Sigma YAML file parses.

**Accessible, reproducible reference environment.** Use one nonprivileged learner-owned Linux user environment with a small controlled service or supplied service fixture, synthetic authentication/administrative events, bounded container/CI-style identity changes, a local collection/normalization script and a reproducible local event-query or rule engine. A compact Python 3 standard-library event evaluator is acceptable if the detection semantics are fully specified, executable and tested against independent expected records. A free Sigma parser or open-source search engine may be added, but no proprietary SIEM, EDR license, internet-facing server, cloud tenant, privileged packet capture, root access, forensic workstation or image of an unrelated person's device is required. Supply genuine, target-identified host/log excerpts for unavailable kernel, cloud or enterprise telemetry, clearly distinguishing supplied observations from local execution. Synthetic attack-like actions must be harmless and authorized; a behavioral trace may be generated without creating malware, stealing data or executing dangerous payloads.

**Host-evidence obligation and safety.** At least one required assessment must **actually acquire** a bounded evidence set from the learner's own disposable host or user-scoped process and preserve a verifiable original working copy and independently recomputed cryptographic hashes. This includes a contemporaneous reachable process/file state where available and selected authentication, process, filesystem or service records. A copied log bundle is not a full-disk forensic image; an accessible process-list snapshot is not a RAM image. Host disk/memory images, low-level kernel artifacts and privileged acquisition tools may be analyzed from properly sourced teaching fixtures instead of requiring a privileged live collection. Acquisition can change timestamps and state; record when/how access may have altered evidence, time source/uncertainty, evidence owner, tool versions, sequence of transfers and limits. A hash proves equality to the hashed bytes, not correct attribution, tamper-free prior history or complete chain of custody. Do not acquire other users' files, secrets, real credentials, production evidence or third-party host data.

**Incident boundaries.** All exercises remain local, fictional or explicitly authorized. Containment may be demonstrated with controlled user-level process stop, local credential revocation fixture, disabled test workflow or bounded network policy without affecting a shared host. Eradication and recovery require independently verified removal of the *specified* cause and restoration of intended function, not an unsupported assertion that an unknown persistent adversary is gone. Preserve evidence before potentially destructive action where safe and feasible; explain exceptions where immediate harm reduction dominates. Threat hunting is a disciplined search over defined telemetry, not permission to scan outside the authorized scope.

**Workload and assessed performance.** Learners can reuse one evolving synthetic incident case, a versioned dataset, locally acquired host artifacts and a single detection/test harness across **four** distinct summative evaluations. Optional lesson investigations are formative and impose no separate submission requirement. The provisional 12–16 weeks at approximately 10–14 focused hours/week covers event collection, normalization, detection rules and false-positive/negative studies, actual scoped evidence preservation, timeline triangulation, hypothesis-driven hunting, response/restore exercises and an unfamiliar technical defense. Calendar hours, an alert count and the number of indicators detected do not establish mastery. Status remains `draft` pending independent expert and learner calibration.

## Learning outcomes

- **SEC7-O1:** Define an authorized defensive investigation and asset/identity/host scope, including protected evidence, stop conditions, privacy, responsible roles and what an observed event can or cannot establish about malicious activity.
- **SEC7-O2:** Derive threat- and behavior-specific telemetry requirements from an explicit detection hypothesis and trust boundaries, mapping necessary event fields, identity/resource coverage, collection positions, missing sources and likely blind spots without treating ATT&CK labels as automatic detections.
- **SEC7-O3:** Collect, normalize, retain and inspect bounded security events with an explicit timestamp/time-zone/clock-skew model, correlation fields, source identity, collection loss, integrity, access restrictions and redaction, distinguishing actual observations from generated or supplied traces.
- **SEC7-O4:** Implement and independently test reproducible detection logic for meaningful security behaviors using labeled positive, ordinary-benign, benign-lookalike, altered and missing-data cases, measuring appropriate coverage, false alarms and trade-offs without claiming a synthetic dataset represents production performance.
- **SEC7-O5:** Triage a credible security signal using severity, asset importance, affected authority, competing hypotheses, supporting/contradictory evidence and a justified next observation, distinguishing an alert, a confirmed event and an incident declaration.
- **SEC7-O6:** Acquire, document and protect a real bounded user-owned host evidence set in a defensible order, using verifiable integrity hashes, provenance, custody/transfer notes, acquisition-impact limits and appropriate handling of volatile and persistent artifacts.
- **SEC7-O7:** Examine authenticated host/service/process/file artifacts and their metadata, identify conflicting or unavailable traces, and reconstruct a bounded host activity claim without equating tool output, file timestamps or a missing record with complete truth.
- **SEC7-O8:** Construct and defend a multi-source incident timeline and causal account with normalized event times, competing explanations, observable action and trust changes, corroboration, uncertainty and defensible distinctions between initial condition, observed impact and possible root cause.
- **SEC7-O9:** Design and conduct a time-bounded threat hunt from a falsifiable behavior hypothesis over stated data components/queries and an independently defined negative condition, document pivot choices and coverage gaps, and conclude with a justified finding or inconclusive result.
- **SEC7-O10:** Choose and justify proportionate containment, preservation and escalation actions based on active risk, scope, authority, service impact, reversibility and evidence loss, then verify the allowed/denied state under controlled conditions.
- **SEC7-O11:** Plan and demonstrate controlled eradication, recovery and follow-up verification for the established cause and affected services, including legitimate-function checks, security regression, scoped watch criteria and accountable communication, without claiming that a local exercise proves total attacker removal.
- **SEC7-O12:** Produce a reviewable incident assessment and individually defend an unfamiliar changed detection, timeline, evidence-integrity or containment scenario through independent prediction, discriminating observation, corrected decision and explicit residual uncertainty.

## Modules

### Module 1 — Security Telemetry as Evidence

#### Outcomes

- SEC7-O1
- SEC7-O2
- SEC7-O3

#### Lessons

1. **Detectable behavior and protected assets** — Begin from a supplied authorized service/identity system and one plausible abuse of privileged access. Identify which actor, operation, resource and state change would matter, which normal authorized behavior resembles it and which observable fields could separate them. Distinguish system activity, recorded event, alert and incident; show why a scanner finding or a login failure alone cannot establish an attack.
2. **ATT&CK strategies and data-component selection** — Use the current ATT&CK detection strategy, associated analytics and data components as *hypothesis sources*. Reconstruct the necessary input events and preconditions for a bounded example such as unexpected role grant or credential use after revocation. Contrast conceptual tactic labels with actual analytic predicates and the specific host/application/cloud event fields needed to run them.
3. **Event identity, context and normalization** — Create a small reproducible schema and conversion contract for source identifier, actor, account, subject, object, operation, result, event time, collection time, correlation and environment. Preserve original event content separately; label synthetic/test provenance. Show how dropped fields, source-specific encodings, implicit time zones or a naïve join between different account IDs invent incorrect correlations.
4. **Clock, completeness and collection failure** — Reconcile log timestamps with known host clock offset, ingestion delay, out-of-order delivery and non-UTC records. Analyze one missing source, filtered failure event or event lost during interruption; record what cannot be concluded from silence. Prioritize fields and log points by an actual detection decision, not by maximum data collection.
5. **Safe and useful retention** — Decide which records must remain protected, for how long under a fictional documented purpose, and who can read, change or export them. Verify a bounded local log collector produces usable records for both permitted and denied actions while excluding synthetic secrets and unnecessary personal attributes. Explain why a log stored next to a compromised service may not be independently reliable.

*Optional formative feedback:* Given an ATT&CK technique name and a ten-field sample log, identify the missing data component and one false interpretation introduced by clock skew.

### Module 2 — Detection Logic, Measurement and Alert Triage

#### Outcomes

- SEC7-O2
- SEC7-O3
- SEC7-O4
- SEC7-O5

#### Lessons

1. **From behavior hypothesis to executable predicate** — Write an explicit rule for a concrete security event such as unexpected privileged role assignment or repeated denied workload credential use followed by a grant. Define actor identity, event types, time window, sequence/order, exclusions and required data; explain why an ordinary login or authorized administrator change must not trigger it. Execute a local query/rule against labeled independent records.
2. **Portable rule descriptions and engine semantics** — If using Sigma, inspect its current schema, logsource/detection syntax, field mapping, and documented false-positive notes. Verify the **converted backend query or local evaluator behavior** on the declared engine; a portable label does not make unsupported correlation/sequence semantics magically correct. A carefully specified non-Sigma query is equally legitimate when it tests the same security claim.
3. **Independent benign and malicious-looking cases** — Construct a held-out test set with known permitted admin operations, accidental user errors, repeated controlled malicious-like fixture events, partial record loss, out-of-order event arrival and a plausible benign lookalike. Define true/false positive/negative labels relative to the *specific declared oracle* and prevent a rule merely memorizing a training fixture's unique ID. Compare a rule's behavior before and after changing one legitimate-use assumption.
4. **Detection performance without false certainty** — Derive confusion counts, precision/recall for the *labeled fixture* and conditional rates when defined. Discuss low-prevalence base rates, alert volume, missed collection and drift, plus sensitivity to window size, missing fields and environment changes. Distinguish a perfect score on ten synthetic records from real-world sensitivity or an exhaustive hunt.
5. **Triage with competing explanations** — Take a triggered local alert, enumerate at least two hypotheses, inspect a corroborating and a contradictory source, assess impact and actor/resource privilege, then choose a safe next collection or escalation decision. Write a disposition as likely benign, suspicious, confirmed in-scope incident or inconclusive, and explain the exact evidence threshold that would change it.
6. **Detection tuning and regressions** — Correct a false-positive-heavy or easily evaded rule using a defensible extra field or temporal condition, then retest the same unchanged holdout set plus new boundary/failure examples. Record what legitimate or hostile action the revised rule still misses and why a broad exception could hide real activity.

*Optional investigation:* Show that filtering all release-worker operations removes several false alerts but also hides an unauthorized protected-environment event; derive a safer rule from actual role/subject semantics.

### Module 3 — Scoped Host Acquisition and Forensic Integrity

#### Outcomes

- SEC7-O1
- SEC7-O3
- SEC7-O6
- SEC7-O7

#### Lessons

1. **Collection authority, volatility and preservation risk** — Plan a host evidence acquisition for one learner-owned disposable Linux process and files. Identify active process/socket/file state that could change, durable service/authentication logs and timeline-bearing filesystem objects; choose an order under declared goals and safety constraints. Explain how reading files can modify metadata and how containment may destroy volatile evidence.
2. **An actual local bounded acquisition** — Independently collect process/command or owned connection state, accessible service event records and relevant file/object metadata from the declared user-owned sandbox. Record tool/version, command, collection-time clock, path/scope, observer privileges and whether collection may have changed live state. Use snapshots and copied files rather than claim a full memory/disk image without actually acquiring one.
3. **Integrity, custody and working-copy discipline** — Acquire an original evidence bundle and a separate analysis copy, record hashes for each object and a manifest, independently recompute hashes after transfer, and demonstrate detection of a controlled changed-byte mismatch. Trace who acquired/transferred/read it and when; distinguish evidence integrity **since the initial hash** from authenticity of the original event or uninterrupted chain of custody.
4. **Host artifacts, timestamps and alternate readings** — Examine approved process, service/authentication log, shell activity, file ownership/permissions and mtime/ctime metadata where available. Use platform-appropriate definitions: Unix ctime is not file creation time; shell history may be incomplete; child or remote activity may not appear in the same host log. Correlate at least two independent artifacts while identifying missing records and changed clocks.
5. **Privileged forensic sources as labeled references** — Review genuine supplied Linux audit, memory/process, filesystem-journal or disk-image excerpts from an explicitly named target when the local sandbox lacks capture permission. Distinguish volatile memory content from a task/process snapshot, a file copy from an image and a synthetic exercise timeline from a documented observation. Do not require physical device acquisition, root privileges or a paid forensic tool.

*Optional formative feedback:* Detect that an investigator's copied evidence no longer matches its original hash and explain the limited claim still supported by the existing notes.

### Module 4 — Timeline Reconstruction and Hypothesis-Driven Hunting

#### Outcomes

- SEC7-O2
- SEC7-O5
- SEC7-O7
- SEC7-O8
- SEC7-O9

#### Lessons

1. **A causal security timeline, not a sorted dashboard** — Combine independently sourced event, identity-policy, process and artifact records around one synthetic privilege change or failed secret boundary. Normalize times while preserving original timestamps and collection skew; separate known event order, plausible ordering, actor inference and unsupported root-cause assertions. Identify the exact earliest observed deviation rather than inventing initial access.
2. **Competing explanations and pivotal observations** — Build two or more plausible causal accounts, such as approved emergency access versus unauthorized role grant, then choose a record or host artifact that could discriminate them. Investigate contradictions and loss; reject a hypothesis when its predicted event is present/absent *under adequate coverage*, not merely because one dashboard has no match.
3. **Hunt scope, query and stopping rules** — Form a falsifiable adversary-behavior hypothesis from an actual validated threat assumption, select the available data components and authorized time/asset scope, and run a reproducible query or series of narrowing pivots. Predict benign lookalikes and a negative condition, explicitly accounting for gaps, before interpreting results.
4. **What a hunt can conclude** — Examine findings from a bounded synthetic dataset plus one altered or unseen context. Distinguish positive corroboration, an inconclusive result due to missing logs and a bounded negative result under adequate coverage. Suggest a proportionate new detection candidate, collection improvement or risk decision without calling a hunt a successful breach simulation.

*Optional investigation:* Compare a hunt of all administrative process names to a hunt of privileged actions involving an unexpected subject and resource; identify where attribution changes and why both may miss unlogged actions.

### Module 5 — Incident Decision, Containment and Verified Recovery

#### Outcomes

- SEC7-O1
- SEC7-O5
- SEC7-O8
- SEC7-O10
- SEC7-O11

#### Lessons

1. **Classification, accountable decisions and escalation** — Define when a controlled suspicious event becomes a declared test incident using scope, consequence, confidence, active harm and owner-defined thresholds. Assign communications and decision authority, confidentiality/notification limits and a preservation owner. Follow the current NIST SP 800-61 Rev. 3 / CSF 2.0 integrated view, not an assumption that preparation or detection ends before response starts.
2. **Containment and evidence trade-offs** — Compare disabling a synthetic account, revoking a local test role, stopping a learner-owned process, isolating a disposable service route and preserving an evidence copy. For the chosen response, predict what malicious and legitimate actions will cease, what telemetry will disappear and which access paths remain. Choose a narrow reversible control and show why a global shutdown or host-wide firewall rule is neither required nor always safer.
3. **Identify and correct the established cause** — Reconstruct the specific misconfiguration or application/control weakness using preceding evidence; distinguish cause, enabling condition and symptom. Correct an owned identity, service/policy or record-processing flaw and verify that alternative access, stale credential and failing dependency paths behave as specified. Do not infer eradication of an imaginary persistent actor from restarting the training service.
4. **Service recovery and security regression** — Restore the fictional approved service function, confirm legitimate requests/identity remain valid and rerun an independent negative security case and targeted detection query. Where data integrity/backup recovery matters, use actual bounded test records or authentic supplied evidence; do not redo APP7's complete deployment, database restore or failover course. Record residual exposure, decision criteria for lifting containment and owner sign-off.
5. **Post-incident learning and sustainable detection** — Produce a concise chronology of decisions, evidence and impact, specific telemetry/detection deficiencies, preventive repair and retest ownership. Distinguish a demonstrated local change from a proposed production control, and set measurable re-evaluation triggers without promising continuous monitoring or asserting that a single training case proves resilience.

*Optional formative feedback:* Explain why removing an account immediately may prevent harm but also invalidate a volatile session artifact, and what minimum evidence can still be preserved safely.

### Module 6 — Unfamiliar Incident and Independent Technical Defense

#### Outcomes

- SEC7-O1
- SEC7-O3
- SEC7-O4
- SEC7-O5
- SEC7-O6
- SEC7-O8
- SEC7-O9
- SEC7-O10
- SEC7-O11
- SEC7-O12

#### Lessons

1. **Build a falsifiable incident evidence case** — Reuse the learner's detection, bounded acquired host evidence and one approved synthetic incident with real local observation or correctly labeled authentic reference traces. Prepare a sequence tying legitimate activity, unexpected action, privileged consequence, visibility gaps and response decisions to independent expected behavior; explicitly preserve unknowns rather than invent compromise.
2. **Changing evidence and rule sensitivity** — Receive an unfamiliar variation such as a missing auth log, a new benign administrative workflow, a clock-shifted host, a revoked role that remains cached, or a changed event field. Before further queries, predict the effect on detection, timeline and containment, identify an alternative explanation and select a discriminating safe check.
3. **Reproducible response and recovery record** — Execute permitted local containment or evaluate a genuine supplied higher-privilege action, then retest protected and legitimate state and compare revised rule output on held-out positive/negative cases. Verify evidence hashes remain interpretable and document what the response changed or destroyed.
4. **Findings, uncertainty and defender review** — Give a reviewer and accountable owner a short, actionable report that links event observations, acquisition provenance, competing diagnoses, detection misses, chosen actions, operational costs, correction and residual risk. Defend or revise the finding under questioning or an independently supplied bounded change; a polished narrative without reproducible evidence fails.

*Optional investigation:* Ask a peer to switch one benign event label and one collection timestamp without changing the incident truth; determine whether the analyst overfits the original dataset.

## Completion requirements

**Four required summative assessments** establish the SEC7 outcomes. Learners may reuse one local training service, an instrumented identity/action event fixture, an executable detection evaluator, a genuinely acquired user-owned host evidence set and authentic supplied privileged trace excerpts. Only evidence specified below is mandatory; module investigations, ungraded readings and self-checks are optional. No evaluation assumes access to a real compromised environment. Assessment decisions must distinguish actual events, authentic reference observations, synthetic modeled behavior, source-derived deductions and missing proof.

- **SEC7-AS1** — Security Telemetry, Executed Detection and Alert Triage
  - **Outcomes:** SEC7-O1, SEC7-O2, SEC7-O3, SEC7-O4, SEC7-O5.
  - **Work:** Define a bounded approved service/identity threat such as an unintended privileged grant, build or adapt a *working* local event collection and query/rule evaluator, document specific source/event/time/actor/resource fields and independently label held-out authorized, suspicious-like, benign-lookalike, malformed, time-shifted and missing-field events. Implement at least one meaningful detection rule against actual generated local traces or genuine labeled training records; test before/after rule adjustment. Quantify confusion counts on the test set, explain false alarms, missed cases, base-rate/coverage limits and safely triage a triggered and a misleading alert. Sigma format is optional; when used, run/test the backend logic, not only YAML.
  - **Criteria:** Collected events have reproducible provenance, bounded redaction, normalized timestamps and documented loss/clock assumptions. The predicate detects a specific unauthorized condition and meaningfully distinguishes a legitimate similar workflow; positive, negative, changed-context and missing-coverage cases show actual evaluator behavior. Expected case labels precede execution; the revised rule does not silently suppress all real positives. Any precision/recall claim is tied to the explicit held-out set, not production detection rates. An alert disposition identifies impact, competing explanation, next observation, and whether the evidence does or does not support declaring an incident.
  - **Evidence:** Authorized test scope and input fixture, versioned schema/event generator or source, executable query/rule plus run instructions, independent labeled expected results, actual alert outcomes and confusion counts, redacted normal/malformed/missing-data records, rule-change comparison and triage note with limitations.

- **SEC7-AS2** — Actual Host Acquisition, Integrity and Correlated Artifact Analysis
  - **Outcomes:** SEC7-O1, SEC7-O3, SEC7-O6, SEC7-O7, SEC7-O8.
  - **Work:** Acquire a **real** bounded evidence set from an owned disposable local host/process: contemporaneous user-visible process/connection or resource state, accessible service/security logs and selected filesystem metadata. State volatile/persistent collection priorities, safe authority, collection impact and what cannot be acquired without privilege. Preserve an original evidence bundle separate from the analysis copy, hash and manifest source objects and copies, independently recompute them after transfer, and show one controlled mismatch is detected. Correlate at least two independent actual artifacts with a genuine or clearly labeled reference host trace to build a small timeline; note shell history, ctime, event-time and attribution limits without fabricating forensic provenance.
  - **Criteria:** Actual acquisition occurred; the learner did not merely receive a ZIP and claim to have acquired a live host. Times, tools, actor, scope, sequence and collection impact are documented sufficiently for independent reproduction. Integrity verification detects changed bytes while its limitations are stated; an original is preserved for review and the examiner works from a copy. A process snapshot, selected file export, disk image and memory image are not misidentified as each other. The timeline reconciles clocks and contradictory events, identifies actual observed host activity, and does not elevate untrusted/missing logs to a proven attack cause.
  - **Evidence:** Owned-sandbox acquisition permissions and tool versions, real collection commands and record timestamps, original/working-copy manifests with verified per-object hashes and a controlled mismatch result, custody/transfer notes, two or more annotated host/service artifacts, reconciled timeline, any authentic labeled supplied trace and material uncertainty.

- **SEC7-AS3** — Hypothesis-Driven Threat Hunt and Causal Investigation
  - **Outcomes:** SEC7-O2, SEC7-O4, SEC7-O5, SEC7-O7, SEC7-O8, SEC7-O9.
  - **Work:** Starting from a behavior-based adversary hypothesis with explicit authorized assets and time range, map relevant ATT&CK detection strategy/analytics/data components to actual available events and missing collection. State an independent normal/abnormal/falsifying criterion; execute one or more reproducible queries/pivots over a new bounded dataset that includes benign lookalikes, a changed actor or privilege, and at least one absent/misleading event. Compare two plausible explanations using a discriminating independent source or host artifact and reconstruct a grounded chronology, then either substantiate a bounded finding or conclude the evidence is insufficient. Offer a traceable detection improvement without creating a new unrelated intrusion simulation.
  - **Criteria:** The hypothesis is testable, scoped and not simply "find hackers"; the event fields/analytic predicates match the named available data. Queries actually execute and preserve original record provenance; positive, benign and insufficient-coverage decisions are supported by checkable results. A seemingly negative hunt does not claim absence of compromise where the required field or source was missing. The learner differentiates event sequence, suspiciousness, cause and proven impact, adjusts the hypothesis for contradictory evidence, and communicates residual risk and next useful data.
  - **Evidence:** Pre-run hunt question and ATT&CK data/analytic mapping, bounded data inventory and coverage exclusions, runnable query/pivot definitions, actual redacted results and contrasting cases, cross-source timeline, competing hypotheses, justified decision and proposed rule/collection correction.

- **SEC7-AS4** — Controlled Incident Response, Recovery and Unfamiliar Defense
  - **Outcomes:** SEC7-O1, SEC7-O3, SEC7-O4, SEC7-O5, SEC7-O6, SEC7-O8, SEC7-O9, SEC7-O10, SEC7-O11, SEC7-O12.
  - **Work:** Use the same approved fictional incident, versioned detection/evidence artifacts and a **previously unseen** bounded change: a missing event source, altered benign action, clock-offset host, stale-role privilege, wrong-actor correlation or changed containment assumption. Before decisive inspection, predict authorized and prohibited outcomes and one alternative cause. Triage and declare or withhold an incident with a reasoned confidence/impact decision; preserve endangered accessible local evidence and choose reversible containment of an owned process, synthetic account, role or route. Demonstrate actual controlled permitted/denied state where available, correct the established root cause, restore ordinary service behavior and rerun independent security/detection regressions; review a supplied authentic privileged response trace only where live enforcement cannot safely be exercised. Present an actionable report and defend the technical decision under independent questioning or variant evidence.
  - **Criteria:** The decision is proportionate to observed harm, authority and uncertainty; containment is proven at the declared layer and documented for legitimate-user effect, preservation trade-offs and safe rollback. Acquired evidence remains independently integrity-checkable after handling, with acknowledged unavoidable state changes. The repair targets an actually justified cause, with legitimate action restored and one prohibited/recurrence path denied. Detection is retested against known benign and hostile-like cases after the change; a green rule or stopped host is not represented as complete attacker eradication. The novel challenge demonstrates independent causal reasoning, correction of an unsupported hypothesis, defined owner/escalation communication and explicitly bounded remaining gaps.
  - **Evidence:** New authorized scenario and prediction, incident declaration/escalation rationale, timeline and preservation/response decision log, before/after actual process/identity/access checks, original evidence hash continuity or documented re-acquisition, versioned controlled fix, independent positive/negative/failure and detection reruns, post-incident action list and individual reviewable written/recorded/live defense.

### Evaluation evidence and readiness

For each required evaluation, record `SEC7-AS#`, supporting `SEC7-O#`, source revision, permitted scope, assessor decision, actual observations, synthetic fixture labels and necessary tool/clock/environment assumptions. Executable code and owned-host acquisition steps must be reproducible from a clean allowed fixture. Privileged images and third-party incidents are neither required nor to be secretly collected. Authentic supplied privileged excerpts must have a named target, tool, collection conditions and source; they cannot be presented as the learner's own acquisition. Independent test labels and artifact hashes establish particular claims, not universal rule accuracy, evidence provenance before acquisition or production response readiness.

The course remains `draft` pending [Status Labels](../../spec/status-labels.md). A learner completing this course does not receive an incident responder certification, forensic examiner credential, permission to conduct live intrusion work or assurance of detection of all unauthorized behavior.

### Optional disciplinary references

- [NIST SP 800-61 Rev. 3, final April 2025](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — current incident response recommendations integrated with NIST CSF 2.0.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — Govern, Identify, Protect, Detect, Respond and Recover as interdependent security-risk functions, not a rigid live-incident phase order.
- [MITRE ATT&CK detection strategies](https://attack.mitre.org/detectionstrategies/), [analytics](https://attack.mitre.org/analytics/) and [data components](https://attack.mitre.org/datacomponents/) — current behavior/detection evidence concepts; the October 2026 release makes strategies, analytics and components the relevant current detection objects.
- [Sigma rule specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html) — portable security-detection intent, source fields and rule semantics subject to real backend execution.
- [NIST SP 800-92, final](https://csrc.nist.gov/pubs/sp/800/92/final) — foundational log management; revised log-management guidance may be available in draft and must not be mislabeled as a new final edition.
- [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) — forensic evidence collection, process and chain-of-custody principles; target-specific host/tool facts must be verified separately.
- [CISA Federal Incident and Vulnerability Response Playbooks](https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks) — concrete decision/communication examples; not automatically mandatory for every learner or fictional organization.

These are freely accessible supporting references. Required learning and assessment criteria are fully specified above, independently of any paid incident platform.
