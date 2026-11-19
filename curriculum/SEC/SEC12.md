# SEC12 — Vulnerability & Exposure Management

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC11](SEC11.md)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–14 focused hours/week (provisional; 120–224 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**Vulnerability management is the continuing engineering responsibility to know which owned assets and software are exposed, decide what warrants treatment, implement or coordinate effective changes, and verify that the exposure truly changed.** A scanner report, a critical score, a software bill of materials (SBOM), a vendor advisory or a green patch dashboard is **not independently sufficient** proof that a particular asset is affected, exploitable, remediated or safe. SEC12 prepares a security engineer to own an evidence-backed vulnerability and exposure workflow across a small but realistic heterogeneous collection of synthetic services, hosts, container images and dependencies: discover and reconcile actual assets and owners, interpret advisories and component identities, confirm or qualify affectedness and reachability, use credible exploitation and contextual business-harm signals to prioritize, implement safe patches or effective containment, independently establish closure, maintain justified exceptions, and revise decisions when new information or asset state changes.

**Distinct from finding a single defect.** [SEC2](SEC2.md) and [SEC3](SEC3.md) teach engineering analysis and repair of web, native and binary vulnerabilities. [SEC4](SEC4.md) assesses bounded network/service exposure and local configuration; [SEC6](SEC6.md) covers OCI dependency inventories, CI build provenance and resource-policy controls; [SEC11](SEC11.md) covers endpoint execution policy, update/change baselines and actual Linux/Windows endpoint evidence. [SEC7](SEC7.md) teaches detection and incident response. SEC12 uses those already assessed abilities to establish a different exit competency: **maintaining an accountable, changing exposure state across multiple assets, advisory sources and remediation owners**, with independently verified decisions rather than isolated bug-fix demonstrations. A full SIEM, exploit-development project, professional certification, cloud account, commercial scanner or enterprise ticketing license is not required.

**Prerequisite rationale.** [SEC11](SEC11.md) is the sole direct prerequisite. It supplies device/OS state, patch/configuration and local host control evidence; through [SEC7](SEC7.md) it inherits [SEC6](SEC6.md) source/build/image/component and cloud-policy provenance, along with [SEC10](SEC10.md), [SEC4](SEC4.md), [SEC2](SEC2.md) and [SEC1](SEC1.md) preparation. There is no reason to list SEC6 again as a redundant direct prerequisite. SEC12 does **not** require prior completion of every specialist native-code or cryptography exercise as an entry gate; [SEC9](SEC9.md) separately verifies all required core courses before graduation. SEC12 teaches any necessary inventory/advisory data reconciliation within this course instead of assuming enterprise CMDB, asset-discovery tooling or advanced vulnerability-scanner operation.

**One free, honest reference environment.** A provided or learner-owned versioned local assessment set should include a handful of **different asset and ownership conditions**, not a mandated asset count: a real running local service with protected synthetic state and a known intentionally defective version/configuration; a local OS/package or container/base-image component; a source/dependency inventory with at least one transitive component; and a safely simulated external asset, unsupported supplier component or unreachable management service represented by authentic labeled evidence rather than live scans. Each record includes a stable asset identity and role, owner/contact, inventory source and observation time, installed package/build/commit/digest or other proof of precise version, service reachability and business/safety criticality. At least one asset must be **truly patchable or containable in the owned lab** and have an independent executable allowed/denied or vulnerable/safe oracle. Other supplier/cloud/Windows controls may be assessed from real named-version advisory/policy traces when unavailable. No public IP scan, paid cloud, actual production system, live internet exploit download, proprietary scanner, Windows license or privileged kernel changes are required.

**Non-equivalent facts must remain separate.** A **CVE** identifies an issue but is not an asset inventory. A **CWE** describes a weakness class and does not prove a product release contains the defect. A **CPE** or package name may assist correlation but is not precise affectedness proof across forks, distributions, fix backports or vendor naming. A **CVSS v4.0 Base** score characterizes technical severity under defined assumptions; optional Threat and Environmental modifiers require their own evidence. **CISA KEV** indicates evidence of observed exploitation in the wild, subject to catalog scope and date, but does not prove a particular owned asset was exploited; applicable U.S. federal directives are **not automatically binding on every organization**. **FIRST EPSS** is an estimate of exploitation probability in the next 30 days in its observed population, not impact, proof of an ongoing intrusion or a universally calibrated probability for this specific asset. **SSVC-style decision trees** make stakeholder/mission and exploitation conditions explicit; they are not another hidden numeric risk score. A supplier **VEX** or CSAF status statement is a source-backed claim about a specified product/issue/context, not an exemption from independent asset and configuration review. Preserve status date, producer, provenance, confidence, exclusions and later corrections.

**Safety, responsibility and verifiable treatment.** Assess only owned targets or material explicitly authorized by an owner; state exact host/account, asset, scan and test scope, time, resource ceilings, exclusions, synthetic data, evidence retention, stop/reset and disclosure contacts. Do not probe production, third-party networks or software distribution systems without permission, run unsafe payloads, exploit public targets, brute-force credentials, disrupt services, download real malware or treat a scanner's license as testing authorization. Prefer passive source/version inspection, offline manifests and benign local vulnerability demonstrations. Real remediation must retain legitimate service, preserve required evidence, show a genuine changed running component or enforced boundary and test a meaningful forbidden or unsafe case independently; merely editing a manifest, incrementing a version string or filing a ticket does not qualify. If the original defect cannot be safely patched, a real locally enforced and time-limited containment plus a documented **hold/restriction** can meet the treatment evidence for the bounded fixture, but must not be misrepresented as eradication.

**Program-level professional judgment.** A valuable vulnerability decision has a named accountable asset and remediation owner, defensible affectedness, observed reachability and business consequence, relevant threat evidence with observation date, measured available fix or control, scheduled review and after-change verification. The engineer must choose whether to **fix now, expedite, schedule, temporarily contain, accept a time-bounded exception, defer with evidence, or retire** the asset. Approved exceptions need authority, rationale, residual exposure, compensating-control proof, expiry, monitoring/revisit condition and a plan if the risk increases. Do not silently designate everything "critical," infer closure from no scanner alert, promise zero exposure or pretend all assets were discovered. For a sampled fixed set, calculate honest coverage and exposure-age metrics with clear denominators and unknowns; do not equate closure statistics with the absence of residual security risk.

**Educational readiness.** The same owned evidence set is investigated throughout six competency-derived modules and five summative decisions. Source/version and local verification can be reproduced using free tools, local CSV/JSON files, maintained package managers, container inspection, an optional freely available safe scanner and executable synthetic services. The **12–16-week, 10–14-hour/week** workload is provisional, not learner-calibrated. This draft course establishes public reviewable competencies, not enterprise vulnerability-manager certification or production asset-inventory completeness. Its scope is a **bounded professional vulnerability-management system**, not an obligation to build a production CMDB or remediate every vulnerability.

## Learning outcomes

- **SEC12-O1:** Establish an authorized exposure-management charter, inventory distinct owned assets, software/services, owners, data and critical dependencies, identify missing/unmanaged or duplicated records, and distinguish discovered, inventoried and actually reachable scope with timestamps, authority and stated completeness limits.
- **SEC12-O2:** Reconcile component and platform identities from running binaries, service configuration, package/version/digest, source/build metadata, SBOM and supplier records, tracing direct/transitive, vendored, backported or withdrawn components with reproducible provenance and uncertainty.
- **SEC12-O3:** Interpret authoritative advisory and vulnerability evidence (CVE, CWE, CVSS vector and version, vendor affected-range, fixed-version, product status, VEX/CSAF and scanner findings) and independently adjudicate affected, not affected, under investigation and unsupported claims for named asset/configuration conditions.
- **SEC12-O4:** Safely evaluate actual attack-surface reachability and vulnerability preconditions using independently specified authorized normal/unsafe test oracles; distinguish technical affectedness, runtime exposure, vulnerability presence, successful exploitation and observed attack evidence without claiming unsafe real-world intrusion proof.
- **SEC12-O5:** Correctly interpret and time-bound CVSS v4.0 technical severity (Base, Threat and Environmental where assessed), CISA KEV known-exploitation evidence, FIRST EPSS 30-day probability, supplier urgency and stakeholder-specific SSVC-style decisions without treating any one as organization-specific risk or as proof of local compromise.
- **SEC12-O6:** Prioritize accountable remediation work across unlike assets using asset value and business/safety impact, public versus internal reachability, controls, privilege, attacker prerequisites, known exploitation, uncertainty, time and operational disruption; justify competing rankings, incident escalation thresholds and why some apparent scanner issues should not dominate.
- **SEC12-O7:** Define actionable vulnerability finding and treatment states with asset/issue version, affectedness confidence, triage status, risk owner, responsible remediation owner, target decision date, technical dependency and reviewable communication; distinguish discovery, suppression, exception, containment, fixed, independently verified and reopened.
- **SEC12-O8:** Design proportionate patch, upgrade, configuration, exposure reduction, credential/restriction, isolate or retirement treatments with provider/dependency constraints, sequencing, approval, staged change, rollback and normal-service availability, including cases in which a vendor fix is absent or unsafe.
- **SEC12-O9:** Execute or independently verify at least one genuine locally enforced corrective change in an authorized running asset or protected resource, with exact original and corrected version/policy state, negative/failure regression, user-success checks and evidence of the actual behavior or resource access that changed.
- **SEC12-O10:** Independently validate remediation and residual exposure through post-change asset/component identity, actual effective service or policy state, prior and alternative attack-path oracles, changed/missing inventory observations and justified re-opening when fixes do not address the actual affected instance.
- **SEC12-O11:** Evaluate formal time-limited risk exceptions, compensating controls, accepted/mitigated/retired treatments, accountable approval and escalation, expiry, scheduled reassessment and evidence-handling protections, rejecting unowned, indefinitely deferred or untested exception claims.
- **SEC12-O12:** Maintain and evaluate a repeatable exposure-workflow and honest metrics for asset coverage, verified affected assets, treatment age, exploitation-priority queues, overdue remediation, exception expiry, re-openings and unresolved unknowns, with correct denominators and time/provider limitations.
- **SEC12-O13:** Reconcile evolving advisory, vendor, asset and control evidence across a new discovery or contradicted supplier status; independently revise affectedness, priority, owner, patch/containment and communication decisions without resetting the historical evidence or inventing certainty.
- **SEC12-O14:** Defend a complete, reproducible and privacy-safe bounded exposure-management program through an unfamiliar reviewer-selected asset/version/KEV/EPSS/reachability/remediation condition, executable local tests and clear technical/owner-facing residual-risk recommendations.

## Modules

### Module 1 — Asset Reality, Authorization and Exposure Boundaries

#### Outcomes

- SEC12-O1
- SEC12-O2
- SEC12-O4
- SEC12-O7
- SEC12-O12

#### Lessons

1. **Inventory is a claim about what exists** — From conflicting local service, host/package, container artifact and supplied ownership records, identify actual assets and dependent services; name the asset owner and data/resource consequence. Determine which observations prove a current running endpoint, a dormant image, a configured but absent service or a stale/duplicate record, and state coverage gaps rather than assuming the provided list is complete.
2. **Scope and authorization before discovery** — Write a bounded owner-approved observation and verification charter, including addresses/processes, tools, time/resource budgets, explicit exclusions, synthetic data, safe stop and disclosure. Compare passive component inspection, host inventory and authorized local active probes; show why a visible public service is not automatically a permitted target.
3. **Normalize source, component and instance identity** — Reconcile a package manager record, a service binary/version, image digest, build revision and a direct/transitive SBOM component into stable asset-instance/dependency relationships. Mark disagreement between claimed and actual source, backported distribution packages, namespace reuse, missing PURL/CPE match and vendor naming rather than attributing a CVE from a string match.
4. **Exposure and reachable trust paths** — Reconstruct approved legitimate and unwanted paths into a running owned service including client identity, network exposure, route/auth policy, local process and dependent library. Record whether a flaw's preconditions are reachable from the proposed attacker, and distinguish access controls that merely restrict entry from the underlying vulnerable version.
5. **Operational ownership and continuity** — Establish minimal discover → investigate → assign → treat → verify → watch states with evidence/provenance/time for each. Require a named decision owner and correction owner; record an orphaned/unmanaged asset, asset replacement and service shutdown in a way that cannot falsely close a still-running instance.

*Optional formative feedback:* A vendor report lists two identical package names and one deprecated server, but only one is deployed. Reconcile the three records without discarding the uncertainty or inventing an additional scanning requirement.

### Module 2 — Vulnerability Intelligence, Affectedness and Verified Exposure

#### Outcomes

- SEC12-O2
- SEC12-O3
- SEC12-O4
- SEC12-O5
- SEC12-O13

#### Lessons

1. **Advisory identity is not affectedness** — Read a CVE record, associated CWE, supplier/OS distribution bulletin, precise version/configuration and affected/fixed status. Contrast a generic CPE match with source/build evidence for a backport or fork, and distinguish "no record" from "proven not affected." An issue description without a matching running component is insufficient to assert local exposure.
2. **Trust and reconcile heterogeneous findings** — Inspect available scanner report, dependency alert, SBOM, signed supplier update, CSAF or VEX-style product status and host process evidence. Record source, date, subject, version ranges, parent component and confidence; investigate false positives, false negatives, transitive dependencies and supplier contradictions without treating scanner absence or an unverified `not_affected` status as a closure decision.
3. **Validate the vulnerable precondition safely** — In a deliberately defective owned service or controlled package version, independently define allowed and prohibited behavior and a harmless trigger; observe actual source/configuration, service process and protected state. Label a proven effect, a plausible but unexercised path, a correctly denied attempt and an authentic supplied vendor test separately. Never run destructive exploit samples or probe someone else's host.
4. **CVSS technical severity and the actual environment** — Read the genuine CVSS v4.0 vector and correctly distinguish Base from Threat and Environmental conditions. Compare two assets with the same base score but different reachability, privilege, compensating controls and business harm; explain exactly which environmental assumptions were independently checked.
5. **Known exploitation, probability and confidence** — Interpret date/version-bound CISA KEV evidence and FIRST EPSS probability/percentile without equating them with each other, incident confirmation or impact. Handle absent CVEs, unknown EPSS, stale score dates and competing vendor urgency. Document applicable jurisdictional obligations instead of assuming a U.S. federal remediation directive binds all learners or companies.
6. **When upstream findings change** — Re-evaluate a corrected vendor affected range, newly backported patch, revised CVE, withdrawn advisory or replaced SBOM and determine which assets and treatment decisions must be reopened. Preserve what the earlier analyst reasonably knew and the decision's original observation date.

*Optional investigation:* A high CVSS score refers to an installed component version, but the operating-system distributor backported a fix and the running build confirms it. Design the evidence needed to justify "not affected" rather than suppressing an inconvenient scanner finding.

### Module 3 — Risk-Led Prioritization and Accountable Treatment Decisions

#### Outcomes

- SEC12-O1
- SEC12-O4
- SEC12-O5
- SEC12-O6
- SEC12-O7
- SEC12-O8
- SEC12-O11

#### Lessons

1. **Priorities depend on assets, not just identifiers** — Combine confirmed or qualified affectedness, internet/internal reachability, accessible privileges, protected business value, dependency concentration, patch readiness, known attacks, plausible harmful effect and user/service disruption. Rank unlike cases and explicitly explain why a business-critical externally reachable issue can outrank a larger technical severity score on an unreachable test service.
2. **KEV, EPSS, CVSS and SSVC-style decisions together** — For an independently created synthetic queue, compare verified exploited-in-wild status, probability estimates, technical severity with vector, public-safety/mission effects, automation/attacker conditions and owner-specific tolerances. Choose response urgency with defensible assumptions rather than inventing a universal formula or treating EPSS as a product's individualized compromise probability.
3. **Verify the treatment owner and decision right** — Create specific exposure records with asset/source revision, CVE or non-CVE defect, confidence, proof, urgency, correction owner, business risk owner, decision/verification deadline and approved action. Separate the engineering recommendation from the authority to accept or defer risk; model an absent owner and conflicting deadline without silently closing the item.
4. **Patch, configuration, isolation, emergency restriction or retirement** — Compare operationally realistic treatments for a running local vulnerable instance, upstream component with no vendor fix, unsupported OS and dependent service. Include staged validation, service-level safety, rollback/backup, change window, supplier dependency and whether a compensating control addresses the actual exploit preconditions.
5. **Escalation, emergency response and informed deferral** — Decide when credible observed intrusion evidence belongs to SEC7 incident response rather than a quiet patch queue, and when a named owner can authorize a reversible containment or time-limited exception. Distinguish expired owner approval, compliance obligation, credible uncontained exposure and truly verified low risk.

*Optional formative feedback:* A remote-code-execution advisory becomes KEV-listed overnight but affects an inaccessible test component in one environment and an internet-exposed production replica in another. Defend urgency without claiming either host has already been compromised.

### Module 4 — Safe Remediation, Regression and Verified Closure

#### Outcomes

- SEC12-O4
- SEC12-O7
- SEC12-O8
- SEC12-O9
- SEC12-O10
- SEC12-O11
- SEC12-O13

#### Lessons

1. **Original and corrected state are measurable** — Before touching a bounded running vulnerable fixture, record the actual executable/service package, process, dependency build/digest, exact unsafe precondition and legitimate workflow. Derive independent allowed, unsafe, invalid/alternative and failure-state oracles; document the authority to patch, expected change and restore path.
2. **A real authorized patch or replacement** — Upgrade or repair an actual owned running component from a known defective release to an appropriate fixed build, or correct a real enforcement/configuration defect. Verify the changed binary/process/load path and protected result—not merely a package manifest, build number or success notification—and maintain reproducible source and dependency provenance.
3. **When a patch cannot be deployed** — Demonstrate an independently testable compensating restriction, safe service isolation or temporary disablement in an owned fixture whose unavailable upstream fix is explicitly stated. Measure what it prevents and the legitimate-user cost, set an expiry and replacement plan; do not call containment permanent eradication or silently accept indefinite exposure.
4. **Check alternate paths and regression failure** — Re-run original negative and legitimate tests using an independent oracle, then change identity, route, component version, cache, configuration/rollback or another plausible route capable of bypassing the fix. A safe known-defective control or comparable mutation must make the verification detect the vulnerability again; otherwise the green test proves little.
5. **Evidence of closure and the residual** — Join corrected running state, effective configuration, independent protected-resource behavior, affectedness revision, updated inventory and responsible review decision. Distinguish fixed, mitigated but still affected, accepted exception, false positive/verified not affected, withdrawn, superseded asset and still unknown; reject a "closed" scanner alert when a protected service remains unsafe.
6. **Operational delivery and safe rollback** — Plan patch rollout order and maintenance constraints across differing owned assets, check user impact and availability, demonstrate safe restore of a broken local upgrade and ensure the restored state does not reopen a previously restricted exploit path. Define the event that must halt or reverse rollout and who owns a failed patch.

*Optional investigation:* A package manager reports that an update completed, but an old long-running service process still has the vulnerable library loaded. Show why the asset cannot be called remediated and what evidence is needed after an approved restart.

### Module 5 — Sustainable Exposure Operations, Exceptions and Measurement

#### Outcomes

- SEC12-O1
- SEC12-O3
- SEC12-O6
- SEC12-O7
- SEC12-O10
- SEC12-O11
- SEC12-O12
- SEC12-O13

#### Lessons

1. **Keep ownership, sources and dates alive** — Implement a transparent local CSV/JSON/ticket-like exposure ledger that links approved asset identities, version/provenance, affectedness, source/score observation dates, risk and correction owners, authority, planned action and verification result. Reconcile a discovered new asset, retired/renamed instance and missing scanner entry without treating one inventory stream as omniscient.
2. **Risk exceptions have conditions and expiry** — Review a documented temporary nonfix for a vulnerable package with actual compensating control, named business authority, rationale, exact affected version/asset, expiry, remaining exploit path and next check. Reject a purported "accepted risk" with absent owner, no current control, silently renewed deadline or no policy for newly observed exploitation.
3. **Measure the right denominators** — For a fixed, labeled time window, calculate inventory/assessment coverage, verified affected items, age by disposition, remediated-and-independently-verified fraction, accepted/expired exceptions, reopening frequency and uncertain/unowned records. State which assets are outside observation and how metrics change when a new service appears; a lower unresolved count can arise from false closure or lost inventory rather than better security.
4. **Automated feeds without automatic truth** — Consume a small offline or free public sample of advisories, KEV and EPSS dated snapshots, reconcile IDs, changing scores and source corrections and trigger a targeted reassessment. Identify duplicate vulnerability aliases, product mismatch, rate limits, disappearance of feeds, unknown status and automation-induced unjustified closure. Scanner, SBOM or VEX presence alone is not a safe risk-decision engine.
5. **Communicate urgent and ordinary exposure decisions** — Prepare a defensible technical issue owner packet and short accountable risk-owner summary: actual affected systems, evidence certainty, plausible harm, options, verified control, interruption/rollout cost, deadlines or legal scope, unresolved unknowns and responsible next observation. Distinguish emergency active incident declaration from routine management and never publish keys, internal secrets or restricted asset coordinates.

*Optional formative feedback:* An exposure backlog appears to improve after adding a new scanner, because duplicate alerts were suppressed but owners were lost. Audit the metric and recommend evidence-preserving cleanup rather than celebrating a superficial trend.

### Module 6 — Unfamiliar Exposure Change and Independent Professional Defense

#### Outcomes

- SEC12-O1
- SEC12-O2
- SEC12-O3
- SEC12-O4
- SEC12-O5
- SEC12-O6
- SEC12-O7
- SEC12-O8
- SEC12-O9
- SEC12-O10
- SEC12-O11
- SEC12-O12
- SEC12-O13
- SEC12-O14

#### Lessons

1. **A new source changes the exposure map** — Receive a reviewer-selected bounded asset or issue change such as a previously unknown public listener, package backport, changed SBOM/digest, a newly listed KEV item, altered EPSS observation date, false supplier VEX status or a different business owner. Before checking the decisive data, predict affectedness, urgency and a plausible competing interpretation, and specify an independent observation that could disprove the guess.
2. **Reconcile conflicting source and actual system state** — Verify the relevant asset/commit/digest, affected-range claim, current process/configuration and meaningful safe exploit precondition; inspect authentic supplied vendor/host records for unavailable systems without pretending to have scanned them. Correct a stale record and identify which previous treatment or exception decision must be reopened.
3. **Implement or confirm a relevant treatment** — Change the authorized owned fixture's actual vulnerable runtime or effective resource restriction, or defend a verified temporary containment and hold. Execute new allowed, forbidden, invalid, altered-path and failure/rollback oracles; account for version/instance change, scanner blindness and the cost to legitimate operation. The original fix must not become an automatically accepted result after the unseen change.
4. **Defend the complete accountable exposure cycle** — Present versioned authorized assets and component identities, dated evidence/advisories, affectedness and reachability conclusions, ranked decisions, concrete owners and deadlines, actual local before/after proof, reproducible verification, exceptions, reopening logic, honest coverage measures and audience-appropriate recommendations. Individually answer an unseen causal/prioritization/verification question; correct prior unsupported assertions and name the remaining unverified exposures.

*Optional formative feedback:* A new vendor advisory changes one asset from "not affected" to "affected" while a compensating network restriction remains active. Reassess priority, exception expiry and release decision rather than assuming the earlier closure stands.

## Completion requirements

**Five independently reviewed summative assessments** establish the SEC12 outcomes. The same evolving, reproducible, locally owned exposure register, supplier/advisory snapshot, running fixture and protected-state test harness can support all five, but each must establish its own observable claims. Work is limited to owned or expressly authorized assets, safe offline/synthetic advisory and exploit evidence, and genuine labeled supplier/cloud/Windows traces when relevant. No paid scanner, production CMDB, licensed ticketing system, external host penetration, dangerous exploit sample or privileged third-party access is a condition. Optional formative investigations are not summatives. Every decision identifies `SEC12-AS#` and associated `SEC12-O#`, version and evidence source, original expected/actual status, independent review and residual unknowns.

- **SEC12-AS1** — Authorized Asset Inventory, Source Reconciliation and Exposure Contract
  - **Outcomes:** SEC12-O1, SEC12-O2, SEC12-O4, SEC12-O7, SEC12-O12.
  - **Work:** Establish an explicitly authorized small asset/exposure boundary with at least genuinely different service/host/image/component ownership conditions, a functioning locally observable protected service and at least one stale, orphaned or duplicate record. Reconcile real source/build/package/image identities, a direct/transitive dependency, asset location/reachability and the responsible correction/risk owners. Define approved passive/active observation limits, named adversary starting ability and an independent legitimate/unsafe test oracle for the running service. Create a versioned living exposure ledger and correctly distinguish observed, claimed, unavailable and out-of-scope assets.
  - **Criteria:** Every in-scope asset has a stable identity, time, actual source and responsible owner or is explicitly unresolved; multiple observations cannot be silently mistaken for multiple assets. A discovered component/version is tied to the correct process/image instance and provenance rather than an assumed name. Reachability claims have an identifiable tested path or accurately labeled supplied source. Unauthorized discovery, arbitrary public scanning, fabricated asset inventory coverage and a blanket finding that everything is "affected" do not meet acceptance. The ledger can be reproduced by another learner from synthetic/source-controlled fixtures and does not conceal known unowned or missing instances.
  - **Evidence:** Owner-signed/approved scope and harmless testing limits, actual asset/process/image/source identifiers and timestamped inventory sources, dependency and service relationship map, owner/asset provenance, reachability/authorization matrix, missing/duplicate reconciliation, bounded test fixture and initial independent oracle, reviewable source-controlled exposure ledger.

- **SEC12-AS2** — Advisory, Affectedness and Reachability Adjudication
  - **Outcomes:** SEC12-O2, SEC12-O3, SEC12-O4, SEC12-O5, SEC12-O10, SEC12-O13.
  - **Work:** For the inventory, examine conflicting genuine or carefully labeled synthetic CVE/vendor, package/distro backport, vulnerability scanner, SBOM/VEX/CSAF status and source/build information. Judge the actual or qualified affectedness and reachability of at least one vulnerable installed instance, one clean/backported/not-applicable or unsupported issue, and an unknown or disputed case **as distinct claims, not a numerical item quota**. Parse a genuine CVSS v4.0 vector, dated KEV and EPSS samples and explain their different semantics. Derive a pre-test legitimate/unsafe oracle and execute a harmless local affected-condition observation or authoritative state test where permitted. Update the ledger to distinguish unaffected, affected-but-restricted, confirmed local failure and unknown states, with changing observation dates and credible supplier correction.
  - **Criteria:** The candidate vulnerability actually corresponds to a specific asset and running component or is accurately marked uncertain. Source, package/build context and conflicting supplier status are independently checked; a CVE name/CPE string, severity, scanner alert, purported VEX exemption or absent scan does not establish affectedness. The learner identifies the effective entry/control condition, avoids confusing local test vulnerability behavior with exploitation in the wild or an actual intrusion, and interprets KEV as known exploitation versus EPSS as population-level 30-day probability with explicit dates. Safe genuine local tests, independent state checks or clearly qualified authentic external traces support each claim and cannot exaggerate unavailable provider/OS behavior.
  - **Evidence:** Precise original process/package/image and advisory identifiers, vendor affected/fixed range, genuine vector/source/observation dates, scanner/SBOM/VEX/CSAF comparison, backport/fork rationale, affectedness and reachability oracle, harmless executed local request/resource outcome, conflicting evidence, uncertainty/decision changes and cleaned exposure-ledger references.

- **SEC12-AS3** — Risk-Led Prioritization and Accountable Treatment Portfolio
  - **Outcomes:** SEC12-O1, SEC12-O4, SEC12-O5, SEC12-O6, SEC12-O7, SEC12-O8, SEC12-O11, SEC12-O12.
  - **Work:** Prioritize a bounded mixed exposed/isolated, high/low-value, KEV/non-KEV and unresolved vulnerability portfolio using actual affectedness, reachability, technical impact, privilege, exploitation intelligence, owner-specific service/business costs and credible uncertainty. Contrast at least two materially different rankings under revised threat/owner assumptions. For each item select and justify fix now, expedite, schedule, restrictive containment, time-bound risk exception, verified not-affected, retirement or explicit investigation. Record correction owner and business risk authority separately; set meaningful time and evidence triggers; identify a possible incident escalation and competing available mitigations. Do not use an undocumented single numerical score to replace professional judgment.
  - **Criteria:** High urgency follows independently explained affected asset/control/impact and current exploitation conditions, not solely a vendor severity or raw EPSS percentile. The candidate understands CVSS v4.0 Base versus contextual Threat/Environmental, KEV known exploitation, EPSS forecast uncertainty and SSVC-style stakeholder trade-offs; U.S. federal requirements are only claimed when jurisdiction actually applies. Treatment choices fit patch availability, operational disruption and potential harm; unowned/unknown cases cannot be marked low risk or closed without evidence. Exceptions contain actual approval, scope, compensating control, expiry and reopening conditions. The assessor can change an asset or threat condition and observe a justified reprioritization.
  - **Evidence:** Dated multi-asset evidence register with independently reviewed affectedness, versions and exploitation signals, declared risk and service-harm rationale, ranked action queue, assigned risk/correction owners, patch/containment alternatives, accepted/denied exception, approval and safe communication, revised-ranking challenge and explicit unknown coverage.

- **SEC12-AS4** — Actual Remediation, Verification and Continuous Closure
  - **Outcomes:** SEC12-O2, SEC12-O4, SEC12-O7, SEC12-O8, SEC12-O9, SEC12-O10, SEC12-O11, SEC12-O12, SEC12-O13.
  - **Work:** Select an authorized vulnerable local running asset and independently demonstrate its original susceptible component or incorrect enforced condition and legitimate operation. Implement a genuine safe patch, supported replacement or proportionate locally enforced temporary containment, maintaining a reproducible clean setup and rollback. Verify the **actually loaded/running** fixed component and real protected state through independent before/after allowed, forbidden, alternative-path and adverse/failure oracles. Show a safe known-vulnerable regression, configuration drift or equivalent mutation is detected; validate the effect of a service restart or rollback and demonstrate that closure is not inferred from a scanner badge or manifest change. Propagate status, dates and remaining exposures into the ledger, reject a false closure and document exceptions/monitoring/reassessment.
  - **Criteria:** A real protected-state or legitimate/unauthorized service property improves at the declared effective boundary without deleting all functionality, and the exact running component/configuration is observed. A source edit not loaded in the process, an unavailable service, an app-only denial, an unverified proxy rule or an update notification alone cannot pass. Independent tests fail on a realistic reintroduced defect or alternate path; normal user behavior and recovery are separately verified. If only tested containment is feasible, the ledger and risk decision explicitly remain restricted/mitigated with a real expiry, not falsely marked fully fixed. Every status change has owner, evidence, time, review and the ability to reopen when assets/advisories change.
  - **Evidence:** Authorized original fixture/source/installed and loaded version, source/build/dependency/protected-state baseline, patch or exact policy diff, verified post-change runtime/permission state, reproducible independent positive/negative/invalid/failure oracles and mutation, safe rollback/restoration, reviewer-verified correction or bounded containment, updated dated ledger and residual-risk/exception decision.

- **SEC12-AS5** — Unfamiliar Exposure Change and Independent Professional Defense
  - **Outcomes:** SEC12-O1, SEC12-O2, SEC12-O3, SEC12-O4, SEC12-O5, SEC12-O6, SEC12-O7, SEC12-O8, SEC12-O9, SEC12-O10, SEC12-O11, SEC12-O12, SEC12-O13, SEC12-O14.
  - **Work:** Receive a previously unknown but authorized change in an asset owner, running version/backport, newly exposed path, dependency graph, vendor affectedness, KEV/EPSS observation or expected patch/exception outcome. Before observing decisive results, state the predicted affectedness, priority, patch/containment, owner and permitted/forbidden effect with a competing explanation. Reconcile the changed source/host/vendor evidence; rerun genuinely owned local protected-state checks, modify a real correction or defend a justified restriction, and determine which previously closed/deferred queue items require reopening. Update ranking, documented treatment owner, review deadline, exception policy and honest metrics. Defend all published SEC12 outcomes, assessed evidence, source/provenance, ambiguity and feasible professional next actions under independent code, artifact and risk questioning.
  - **Criteria:** The learner correctly revises a prior claim when new credible evidence contradicts it, separately traces asset/component/affectedness/reachability/impact/owner and re-evaluates threat urgency rather than restating a fixed severity list. Genuine protected-state repair or documented effective containment with independent normal/denied/failure checks is required; unverified system/scan claims remain unresolved. The revised dashboard/metrics cannot hide missing or newly discovered assets, and decisions about remediation, exception and reopening identify a real accountable owner and revisit trigger. The learner makes a personally defensible bounded risk decision without live third-party exploitation, fabricated vendor evidence, guaranteed discovery claims or treating the capstone as a replacement for uncompleted core competence.
  - **Evidence:** Reviewer-selected changed asset/advisory/scope condition and pre-observation prediction, source/score timestamps and challenged assumptions, original and new affectedness/reachability records, actual local before/after security-control tests and safe regression, revised treatment/backlog/exception/reopening state, independently auditable metrics, evidence/data handling and individual recorded/written/live technical defense.

### Graduation evidence and honest professional scope

For every summative, identify the relevant `SEC12-AS#` and `SEC12-O#`, versioned asset and advisory data, exact known affectedness and availability conditions, independent expected and observed behavior, uncertainty, authorized real fix/containment, owner authority, review and residual decision. A learner may use provided synthetic or securely offline historical vulnerability examples; whenever a **live current** threat signal is used, record the access/observation date and avoid silently replacing it with a future scoring interpretation. Logs and asset records must be privacy-safe, with protected secrets and internal identifiers redacted where public. Technical reviewers can inspect the freely accessible fixture, versioned input snapshots and independent assertion/test runner without a paid scanner or production environment.

**A successful course does not certify an organization's entire exposure inventory, guarantee absence of vulnerabilities, confer authority to scan networks, fulfill jurisdiction-specific federal obligations, or replace a security operations center.** The graduate can perform and defend a bounded representative multi-asset vulnerability-management workflow, demonstrate a genuine corrective control, and explain the limits to scaling discovery, ownership, monitoring and compliance across real organizations. A verified "hold" or time-limited containment can be technically sound, but does not excuse absent required local correction/assurance evidence or pretend remediation has been completed. Course status remains `draft` pending independent reviewer and actual learner-performance evidence under [Status Labels](../../spec/status-labels.md).

### Optional disciplinary references

- [NIST SP 800-40 Rev. 4](https://csrc.nist.gov/pubs/sp/800/40/r4/final) — enterprise patch management planning, accountable treatment and operational risk reduction.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) and [CIS Critical Security Controls v8.1](https://www.cisecurity.org/controls/cis-controls-list) — risk ownership, asset/software inventories, continuous vulnerability management, secure configurations and verified actions rather than a control-score checklist.
- [FIRST CVSS v4.0 specification](https://www.first.org/cvss/v4.0/specification-document) and [CVSS Consumer Implementation Guide](https://www.first.org/cvss/v4.0/implementation-guide) — Base, Threat, Environmental and Supplemental semantics, vector/source and context.
- [FIRST EPSS](https://www.first.org/epss/) and [EPSS FAQ](https://www.first.org/epss/faq) — estimated next-30-day exploitation probability, population, percentile and limits; not actual impact or a finding of local exploitation.
- [CISA Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) and [CISA SSVC guidance](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc) — credible exploitation evidence and stakeholder-specific remediation prioritization, with legally applicable directives kept separate from universal educational recommendations.
- [CVE program](https://www.cve.org/About/Overview), [NVD](https://nvd.nist.gov/), [CWE](https://cwe.mitre.org/), [CPE](https://nvd.nist.gov/products/cpe) and [CycloneDX VEX](https://cyclonedx.org/capabilities/vex/) — issue taxonomy, identity and qualified supplier affectedness without replacing actual host/source evidence.
- [CSAF standard / OASIS](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html) and [OpenVEX](https://github.com/openvex/spec) — supplier product status/provenance evidence; claims must match the installed affected configuration and reviewer authority.
- [CISA Secure by Design](https://www.cisa.gov/securebydesign) and [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) — manufacturer/engineering responsibility and verified repair practices, not a universal obligation to build a vendor patch distribution service.

References support a particular vulnerability-management decision or test. The published `SEC12-O#` and `SEC12-AS#` definitions, not the number of CVE identifiers or scanner results, govern mastery.
