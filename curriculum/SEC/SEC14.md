# SEC14 — Data Security & Privacy Engineering

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC5](SEC5.md), [SEC13](SEC13.md)
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–14 focused hours/week (provisional; 140–252 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**Data security is a property of the complete data lifecycle, not simply the presence of encryption, a correctly authorized API or a database column labeled sensitive.** SEC14 prepares an engineer to establish which information is collected, generated, transformed, joined, retained, transmitted, logged, exported, backed up and disposed of; identify who has authority and a legitimate purpose for each action; reduce unintended disclosure and unnecessary processing; implement and verify meaningful lifecycle controls in an owned data-processing system; and defend a qualified risk decision when downstream copies, identities, processing purposes or retention conditions change.

**The independent graduate competency.** A person can have correct [SEC5](SEC5.md) authenticated encryption and secure keys while raw personal data continues to escape through logs or an overbroad export. An application may enforce [SEC2](SEC2.md) resource authorization while a background worker retains disallowed data after a deletion request. [SEC10](SEC10.md) may revoke an account while separately replicated records remain accessible to an unchanged service account. [SEC13](SEC13.md) assesses systems-wide enforcement and assurance, but does not require implementation of **data-specific minimization, purpose restrictions, copy/lineage governance, retention, subject-request workflows, de-identification, backup restoration and erasure verification** as independently reviewable exit skills. SEC14 owns these data-processing and lifecycle decisions. It **does not** reteach password storage, AEAD design, OAuth token verification, general application SQL authorization, architecture decision records or cloud platform compliance configuration. [SEC7](SEC7.md) retains detection and incident response specialization; SEC14 only evaluates data-specific evidence, notification/escalation boundaries and disposition.

**Preparation.** Direct prerequisites are [SEC5](SEC5.md) for correct cryptographic guarantees and key limitations, and [SEC13](SEC13.md) for source-attributed multi-component authority, trust, control/evidence and protected-state verification. SEC13 inherits application security, cloud/workload and enterprise identity foundations. Neither a specific APP elective nor specialist AI course, commercial database/cloud/data-loss-prevention subscription, formal privacy law qualification, physical laboratory or hardware encryption module is required. [SEC9](SEC9.md) separately verifies all SEC core predecessor outcomes before capstone admission.

**A real accessible data lifecycle.** Use one free, versioned learner-controlled reference application: a local source-inspectable HTTP or command-line service with a persisted primary dataset, a derived/reporting or cache view, an export receiver or file artifact, an inspectable application/event log, a genuine backup/snapshot file and a restore runner. A SQLite database, small Python/TypeScript/Rust services, local files and tests are sufficient; distinct processing authorities are required only where a claim depends on such separation. Create multiple **synthetic identities/subjects** and unrelated synthetic records. Include a stable internal subject reference, a benign identifiable field, one optional or sensitive-by-policy field, a purpose designation, a retention state, a correct legitimate workflow and a deliberately faulty path. The data owner, processor, processor-like external recipient, auditor and requester roles may be represented by distinct safe local actors; a mock/simulated third-party sink must be labeled as such, not described as a real cloud processor.

**Mandatory observable behavior.** An assessed learner must actually run the local service, collect a synthetic datum and follow it into at least two **materially different persistence or disclosure boundaries** beyond the primary record—for example a derived cache, an export file and a log—with independent source/state inspection. They must implement or correct a **real enforceable purpose/access or minimization rule** with permitted and denied/omitted-field tests, and a real lifecycle transition such as deletion/expiry or restricted processing with independently checked consequences in the primary state and tracked downstream copies. At least one assessed scenario must deliberately **restore a stale backup or replay an old export/worker event** and demonstrate that removed data or revoked processing authority does not silently become live again. A JSON report saying `deleted=true`, an HTTP 200 response to a request, a hash of a deleted database row, a token revocation in an identity provider or a CSS-hidden field is **not** independent data lifecycle proof.

**Distinct assurance layers and limits.** Ordinary SQL deletion, cache invalidation and application-level file removal can prove bounded **logical data-state effects** on the running test fixture; they do **not** establish SSD block erasure, overwritten snapshots, cloud object replication deletion, enterprise-wide disclosure recall or provider-managed media sanitization. Protected backups may retain data for a justified defined period and require controlled restoration with reapplication of current deletion/restriction instructions. The assessor must separately record which archived copies were actually destroyed, cryptographically rendered unrecoverable under stated verified key custody, scheduled for expiry, technically inaccessible, outside authority or **unknown**. NIST SP 800-88 Rev. 2 concerns media sanitization and sanitization program decisions; it must not be cited as proof that calling `DELETE` on SQLite has sanitized physical media. Similarly, simply deleting a wrapped key without testing surviving keys, replicas or recovery paths is not blanket crypto-erasure proof.

**Security versus privacy are related, not interchangeable.** The reference system should distinguish unauthorized access and tampering from **problematic authorized processing**, such as collecting more data than a legitimate task needs, using records for an incompatible purpose, retaining them too long, exposing them in debug logs or combining ostensibly anonymous fields in a way that reidentifies a subject. The NIST Privacy Framework describes predictability, manageability and disassociability as privacy engineering objectives. De-identification, pseudonymization, aggregation and true irreversibly anonymized outputs are not synonyms; replacement of names with an ID can remain linkable personal data, and re-identification risk depends on auxiliary information, dataset size and processing context. Do not certify "anonymous" because an obvious identifier has been removed.

**Rights, legal rules and accountable decisions.** Choose a **declared synthetic policy/processing context** with collection purpose, notice/consent where relevant, allowed legal/contractual processing basis as determined by an accountable organization, permitted uses, sharing recipients, user controls, retention/hold exceptions and review owners. Study access, correction, export, restriction, objection or deletion workflows as technical mechanisms; *actual* individual rights, exemptions, reporting deadlines and legal bases differ by jurisdiction, controller/processor responsibility and governing law. A synthetic deletion exercise is not a GDPR, NDPA, UK GDPR or another law's compliance certification, nor is a security engineer unilaterally authorized to override litigation holds or retention laws. A truthful response can be "restricted/held and still retained" when a valid governed exception applies, with verification and an accountable decision, rather than falsely reporting irreversible erasure.

**Authorization and ethics.** All records must be invented and safe. No actual customer, patient, employee or student data; no collection of third-party browsing histories, hidden camera recordings, biometric templates, credentials or identifying analytics; no re-identification of real released datasets. Do not use public data dumps to attempt to identify people. Synthetic linkage attacks and controlled data joins are sufficient for privacy-risk evaluation. Secure logs, access to evidence and exports; redact secret tokens and keep a separate synthetic subject-ID mapping. Do not imply authorization to access a vendor-controlled replica, endpoint device or unmanaged backup.

**Draft workload and result.** Provisional 14–18 weeks at 10–14 focused hours per week supports source-linked data mapping, actual lifecycle changes, privacy-by-design controls, tested deletion/recovery, bounded de-identification evidence, independent review and unfamiliar cases. The work is arranged by **mechanism and independently assessed competency**, not a fixed quota of modules/lessons. One evolving local fixture supports five substantial summatives with explicit positive, negative, invalid, failure and changed-condition evidence. Status remains `draft` until qualified reviewer and actual learner testing justify readiness.

## Learning outcomes

- **SEC14-O1:** Define an authorized data-processing and privacy-security charter identifying actual data subjects, stakeholders, data controllers/decision owners and bounded processors or recipients, purposes, risks and harms, data categories, security objectives, applicable policy and jurisdictional assumptions, testing permissions and qualified unknowns.
- **SEC14-O2:** Reconstruct and substantiate end-to-end provenance and data lineage through actual collection, primary records, transformations, joins, derived material, cache, service-to-service flow, logs, exports, recipient copies, backups and disposal, preserving source/time and distinguishing discovered copies from assumed or unreachable ones.
- **SEC14-O3:** Derive testable data classification, collection/minimization, purpose limitation, field/row/subject-level handling and retention requirements; show that a data element is necessary for an explicit authorized operation rather than equating a privacy notice or encryption flag with permission to process it.
- **SEC14-O4:** Implement and verify real at-source and downstream enforcement of permitted/denied collection, use, access, export or disclosure, including role, subject, purpose, data category, service identity and changed consent or processing authority, using independent protected-state/response and alternate-route observations.
- **SEC14-O5:** Evaluate suitable confidentiality, integrity, authenticity and availability protections for stored, transferred and backed-up records, applying reviewed cryptographic and access technologies where required, while independently checking plaintext exposures, logging, derived copies, key custody/recovery and failure limits beyond a successful cipher operation.
- **SEC14-O6:** Discover and correct data leakage through event/diagnostic logs, metrics/tracing, error pages, debug data, analytics, cached responses, exports or worker messages, retaining necessary bounded security/audit observability and validating reduced exposure under normal, invalid and failure conditions.
- **SEC14-O7:** Design and execute an accountable data subject or owner lifecycle operation—inspect/access, correction, restriction, portability or deletion as applicable—verifying requester authority, exact matching subject and record scope, propagation to genuine local copies, status and honest disclosure of unsatisfied or exempted requests.
- **SEC14-O8:** Define and implement evidence-backed retention, expiry, archival, approved hold and disposal decisions over active, cached, derived, exported and backup data; distinguish effective logical deletion and restricted restore from physical sanitization and unsupported provider-mediated erasure claims.
- **SEC14-O9:** Independently verify data removal or processing restriction through a real local primary-store and copy/lineage oracle, and prove that controlled stale backup restoration, replay, worker retry or recreated derived output does not silently resurrect forbidden current data; document unverified historical replicas and actual remaining availability.
- **SEC14-O10:** Assess data sharing, recipient and processor trust and cross-boundary transfers, maintaining accountable purpose, fields, approval, retention instruction, recipient acknowledgment and effective permitted/denied conditions, without treating a locally generated acknowledgment as evidence of deletion on a real third-party provider.
- **SEC14-O11:** Compare pseudonymization, masking, suppression, aggregation, de-identification and anonymization goals under credible auxiliary-data, linkage, sparse-group and inference conditions, test a bounded synthetic reidentification or disclosure counterexample, and qualify residual privacy risk rather than claiming an anonymization guarantee.
- **SEC14-O12:** Evaluate privacy-sensitive processing changes using risk and individual-harm analysis, purpose compatibility, legitimate service usability, user/manageability and disassociability objectives, conflicting security logging or legal retention conditions, and named technical versus legal/risk decision authority without asserting universal regulatory conformance.
- **SEC14-O13:** Maintain a reproducible data protection assurance and governance record linking source and copy inventory, purpose/policy, data authority, real positive/negative/failure tests, changes, effective retention/deletion, recipient/backup exceptions, privacy risk, evidence limitations and owner acceptance or escalation.
- **SEC14-O14:** Independently predict, investigate, correct and defend an unfamiliar bounded data-flow, recipient, consent, export, derived-output, logging, backup/restore or retention change with actual local data-state tests and candid limits on external/physical erasure and legal claims.

## Modules

### Module 1 — Data Lifecycle Ownership, Purpose and Actual Lineage

#### Outcomes

- SEC14-O1
- SEC14-O2
- SEC14-O3
- SEC14-O12
- SEC14-O13

#### Lessons

1. **The data lifecycle and people affected** — Identify what a locally owned record service collects and why, whom it affects, the responsible data owner, processor-like services, operators and recipients. Distinguish confidentiality and integrity harms from surprising but correctly authorized processing, unnecessary accumulation and loss of user control. Record actual permitted assessment scope, safety, privacy and evidence retention rules.
2. **Discover true source and copy boundaries** — Execute a legitimate synthetic record creation; trace the subject and field through primary SQL/file state, a local derived cache/report, a background job, a separate export artifact and a log, with source/commit revision and observation times. Do not infer copies from architecture diagrams alone. Mark unknown external or expired material separately.
3. **Data subject, purpose and lineage identity** — Differentiate internal subject ID, external identifier, event correlation key, pseudonym, derived category and record owner. Reconcile async transformations and shared rows, multiple subjects in one export, versioned schema and two copies of the same field. Establish which processor can modify or release each copy, which controls are genuinely enforced and what evidence is missing.
4. **Classification and collection necessity** — Classify a benign optional field as sensitive under a declared synthetic policy and compare the minimum necessary fields for an allowed task with those the current program collects or retains. Design at-source validation, purpose and retention defaults; reject "collect everything and encrypt it" as an adequate data minimization plan.
5. **Traceable protection and privacy requirements** — Define normal/denied/invalid, changed-purpose and missing-processor outcomes for collection, use, derived reports, logs, exports and deletion. Bind each to harm, authorization/processing authority, source and independent observable data state, with accountable legal/policy review where needed.

*Optional formative feedback:* A profile form no longer displays a telephone number, but the API still persists and exports it. Explain which real data-action boundary remains unprotected.

### Module 2 — Purpose-Bound Access, Transformation and Data Disclosure

#### Outcomes

- SEC14-O2
- SEC14-O3
- SEC14-O4
- SEC14-O5
- SEC14-O6
- SEC14-O10
- SEC14-O12

#### Lessons

1. **At-source processing rules have executable effects** — For two synthetic subjects and distinct authorized/requesting roles, independently demonstrate which fields and actions are necessary for a declared task. Implement a real field/purpose/subject processing decision at a data-writing or releasing component and prove correct allowed/denied stored state and returned fields, including alternate API/worker access.
2. **Data copy and export controls** — Trace a real local report/extraction endpoint or export worker and actual generated file. Restrict recipient identity, selected fields, purpose and transformed data, then test an authorized export, disallowed field/recipient and changed role or purpose. A 403 or successful approval message is insufficient when forbidden plaintext was already placed into an artifact.
3. **Cryptography, data access and recovery are different layers** — Analyze real stored field/backup at-rest protection with vetted libraries or safe pre-provisioned encrypted fixtures, trusted keys, key access and retention assumptions. Contrast data encrypt/decrypt success with authorized purpose, whether plaintext remains in logs and exports, and whether protected records are recoverable after an authorized key or availability change. Do not rebuild SEC5's cipher/nonce syllabus.
4. **Logging and diagnostics without new disclosure** — Trigger success and safe failure/invalid cases that emit real local events and error output. Audit for optional fields, record bodies, secret tokens, hidden identifiers, command-line args and correlation keys. Change logging to bounded pseudonymous/counted evidence preserving genuine troubleshooting/security audit utility, then verify both missing private content and useful event source/actor/action context.
5. **Cache, worker and replayed authorization** — Compare direct requests with delayed worker consumption, materialized views and cached output. Show why an original permitted collection or successful login does not automatically authorize a later unrelated use, export or publication. Execute changed data-purpose or subject-status tests against a real downstream copy, not only a mock policy interpreter.
6. **Recipient and processor control limits** — Build a clearly labeled local stand-in recipient with permitted/denied acceptance and independently inspectable stored artifacts. Establish what transfer acknowledgment, contractual instruction, versioned schema, data-protection obligation or later delete request proves and what it does not prove about an external processor. State escalation/assurance evidence required before a production vendor deletion claim.

*Optional investigation:* An export endpoint denies a request but a job has already written a CSV file. Diagnose the order of actual data disclosure, not the nominal HTTP response.

### Module 3 — Retention, Subject Requests, Deletion and Restore Safety

#### Outcomes

- SEC14-O2
- SEC14-O3
- SEC14-O4
- SEC14-O6
- SEC14-O7
- SEC14-O8
- SEC14-O9
- SEC14-O10
- SEC14-O12
- SEC14-O13

#### Lessons

1. **Request authority and exact scope** — Exercise an authorized synthetic subject's access, correction, restriction or deletion request. Identify requester authentication, subject matching, shared/third-party data, current processing purpose, accountable approval and relevant hold. A response cannot delete another person's data or silently erase records required by an authorized retention decision.
2. **Retention rules and lifecycle states** — Implement an explicit local policy distinguishing active retention, purpose expiry, archival/hold, restriction, pending downstream action, completed logical deletion and unverified external copies. Include source of rule, owner, deadline, permissible exceptions and genuine evidence for transitions; explain why a button click or an expired timer alone cannot prove disposal.
3. **Actual local deletion and propagation** — Starting from real observed record, cache, derived report, log and export state, apply an authorized deletion/restriction transition with a durable current-deletion instruction or comparable source-of-truth mechanism. Prove effective primary-store deletion/restriction, invalidation or rebuilding of derived outputs, and recorded state for files/recipients that require removal or safe quarantine. Independently verify permitted unaffected subjects and remaining legitimate operations.
4. **Copies, backup and stale restore** — Create a genuine snapshot or export **before** deletion, complete the authorized current-state transition and then deliberately restore/replay the old bytes in an isolated test. Reapply or enforce current deletion/restriction decisions and regenerate derived outputs such that removed subject data does not become live/available in the restored authorized service. Prove both an original failing or unsafe restore path and the corrected path with actual record/state oracles; preserve recovery of permitted records. A tombstone is insufficient when ignored by a restored worker.
5. **Media sanitization and unavoidable limits** — Distinguish logical SQL row deletion, cache invalidation, secure erase assumptions, media-specific sanitization of allocated/unallocated areas, discarded virtual volume, encrypted backup/key custody and provider-replicated storage. NIST SP 800-88 Rev. 2 does not establish physical sanitization by running `DELETE`; document exact data/media authority, unknown storage internals and what genuine sanitization/retention evidence an operator must obtain.
6. **Rights and exceptions without legal overclaim** — Work through an access/export or correction request with a conflicting retention/hold condition. Give a truthful user- and owner-facing disposition specifying what was processed, which copies are restricted or scheduled, which require legal/policy interpretation and what remains unknown; no invented law-wide deadline or universal right to erase all historical evidence.

*Optional formative feedback:* A user sees “Your data was deleted,” but yesterday's backup restores their record and the export receiver still exposes an old file. Define the changed source-of-truth and independent check needed to retract the inaccurate claim.

### Module 4 — De-Identification, Sharing and Privacy Risk in Derived Data

#### Outcomes

- SEC14-O1
- SEC14-O2
- SEC14-O3
- SEC14-O4
- SEC14-O5
- SEC14-O10
- SEC14-O11
- SEC14-O12
- SEC14-O13

#### Lessons

1. **Pseudonyms, masking and identity linkage** — Produce an approved synthetic report with removed obvious names but persistent subject keys, joinable timestamps or rare attribute combinations. Demonstrate with a separate synthetic auxiliary dataset that one subject could still be linked. Differentiate pseudonymization, redaction, tokenization and untested anonymization assertions, and record each technique's true assumptions.
2. **Aggregation and suppression with useful output** — Design a genuinely usable local aggregate/report for a stated purpose. Compare exact row release, counts, generalized time or location bins, suppressed sparse groups and the loss of legitimate utility; independently test at least one small-group or differencing privacy leak on synthetic data.
3. **De-identification governance is continuing** — Evaluate intended audience, auxiliary-data availability, source/recipient copies, future joins, updates and disclosure pathways. Use [NIST SP 800-188](https://csrc.nist.gov/pubs/sp/800/188/final) to frame a bounded de-identification technique and governance review; do not certify anonymity from a library call, a static hash or a single chosen threshold.
4. **Export, shared processor and downstream promises** — Inspect a real local export and recipient-like store under changed purpose, fields and authorization. Exercise restricted and permitted data sharing with an auditable instruction/acknowledgment; distinguish locally observed processor behavior from contracts, supplied vendor attestations and unverified external deletion.
5. **Security logging versus individual privacy** — Compare forensic usefulness with field minimization, retention and visibility of logs, correlation identifiers and access records. Test a synthetic incident investigation query that still works after sensitive payload removal, and identify when an organizational or jurisdiction-specific legal hold could reasonably retain bounded information.
6. **Risk and proportionality under uncertain harm** — Produce an accountable decision over source data, pseudonymization/aggregation, export restrictions and user manageability, distinguishing security breach from problematic authorized data use. Examine user surprise, re-identification, error/inference harms, impaired audit, legal uncertainty and owner/processor responsibilities without claiming global compliance or that all useful analytics require raw data.

*Optional investigation:* A system replaces email addresses with SHA-256 values but publishes small-group demographics and event timestamps. Explain why reidentification risk remains and compare feasible release alternatives.

### Module 5 — Integrated Data Assurance, Exception and Independent Review

#### Outcomes

- SEC14-O1
- SEC14-O2
- SEC14-O3
- SEC14-O4
- SEC14-O5
- SEC14-O6
- SEC14-O7
- SEC14-O8
- SEC14-O9
- SEC14-O10
- SEC14-O11
- SEC14-O12
- SEC14-O13

#### Lessons

1. **Claims, observed state and outstanding copies** — Build a concise source-to-sink data/copy ledger of actual source and transformed records, primary/derived/cache/log/export/backup states, data and decision owners, purpose, allowed recipients, retention and exception conditions. For each protection claim, cite real independently tested current state, source/policy revision or clearly labeled authentic external evidence, not only a compliance checklist.
2. **Regression for a data-purpose or lifecycle change** — Introduce a safe wrong-purpose export, unnecessary field, old backup replay, stale logging rule or delayed worker event. Execute independent normal, denied, invalid and adverse-state oracles, with a known-bad mutation that must fail the verification. Verify real existing legitimate service while the unauthorized path remains blocked.
3. **Exception, hold, confidentiality and recovery trade-off** — Review a bounded legal/policy retention exception or operational restore constraint under named accountability. Demonstrate actual restricted processing and log/backup access limitations where locally possible, record when deletion is delayed, and choose credible release/hold and escalation with explicit user-facing wording rather than falsely reporting disposal.
4. **Actual evidence provenance and qualified assurance** — Explain which files/rows/snapshots were executed and inspected, which external processors/hardware/media were not, why only bounded logical deletion/restriction is established, and what independent source, version, restore or vendor assurance could justify a stronger claim. Review with an assessor who challenges at least one misleading “encrypted, deleted or anonymous” conclusion.
5. **Security-and-privacy owner communication** — Provide a reproducible data-lifecycle change packet: affected subjects, purposes, protected data, implemented controls, source and copy evidence, backup/restore result, user/operational impacts, ongoing exception, residual privacy harms, accountable owner and re-verification trigger. Avoid promising complete protection or a legal determination outside an engineer's role.

*Optional formative feedback:* A dashboard reports “All data encrypted” while a failed export task writes a plaintext diagnostic archive. Identify the actual exposed copy, required owner and falsifying test.

### Module 6 — Unfamiliar Data Lifecycle and Individual Technical Defense

#### Outcomes

- SEC14-O1
- SEC14-O2
- SEC14-O3
- SEC14-O4
- SEC14-O5
- SEC14-O6
- SEC14-O7
- SEC14-O8
- SEC14-O9
- SEC14-O10
- SEC14-O11
- SEC14-O12
- SEC14-O13
- SEC14-O14

#### Lessons

1. **Predict an unseen changed data boundary** — Receive a reviewer-selected new data attribute, changed purpose, export recipient, cache/worker replay, log collector, backup retention, shared-subject row, pseudonymous join or deletion exception. Before inspecting decisive results, state what should remain in each actual store, which action ought to be permitted/denied and a competing explanation for any leaked or resurrected copy.
2. **Locate the real data action and correct it** — Inspect current source/schema, identity and purpose rules and actual primary/derived/export/log/backup bytes. Execute a safe changed case; correct the actual enforcing collection/export/retention/deletion or restore mechanism or justify a narrowly verified restriction/hold. Rerun genuine local allowed, forbidden, invalid, stale/replay and relevant backup-restoration oracles; assess utility, lawful-policy uncertainty and whether earlier evidence has become stale.
3. **Defend qualified lifecycle assurance** — Show the versioned running data system, purpose/lineage ledger, effective minimization and access, executed deletion/restore invariants, realistic de-identification challenge, source and source-of-truth evidence, named residual externally held copies, owner decision and privacy-safe technical handoff. Individually explain the source/policy/test and rebut an unfamiliar auditor's overclaim that a deleted row proves physical sanitization or a pseudonymized report is automatically anonymous.
4. **Revise the decision after contradictory evidence** — A reviewer changes a retention exception, auxiliary join, recipient acknowledgment or restore age and challenges the original assurance statement. Specify which subject/processor copy and claim must be reopened, perform a new discriminating bounded test where permitted, document impossible external proof honestly and defend a revised release, restrict, notify or hold recommendation with user and operator effects.

*Optional formative feedback:* A backup restore remains safe for a deleted user but a derived analytics table now contains a joinable identifier previously outside the lineage map. Update both the test and the data-sharing decision; do not merely rerun the old primary-key deletion check.

## Completion requirements

**Five required summative evaluations** assess the distinct data-lifecycle mechanisms. Use one evolving free, owned and source-controlled synthetic service and data fixture, with a genuinely persistent primary database, at least two downstream disclosure or persistence boundaries, an inspectable log and a real backup/restore event. They may share the same test source, but each summative must supply its own independently reviewable Outcomes, Work, Criteria and Evidence. There is no mandatory project count, legal certification, commercial DLP/scanner/cloud service, real personal data or specialist storage hardware. A protected-state conclusion must follow actual bounded execution with independently predicted normal, denied, invalid and failure conditions, source/subject/provenance and residual unknowns. A published policy, deletion-request receipt or simulated provider callback cannot replace the real local data-state checks.

- **SEC14-AS1** — Authorized Data Inventory, Purpose and Lineage Assurance
  - **Outcomes:** SEC14-O1, SEC14-O2, SEC14-O3, SEC14-O4, SEC14-O6, SEC14-O10, SEC14-O12, SEC14-O13.
  - **Work:** In an authorized locally runnable service with invented data and real persisted state, collect a synthetic datum through an actual supported legitimate operation and trace it through primary storage and at least two materially different downstream boundaries, one of which must expose a real cached, derived, logged or exported copy; preserve observation times, source versions, subject and recipient links, accountable decisions and unknown destinations. Identify purpose, field necessity and a problematic currently collected/propagated item. Implement a real in-service at-source or downstream field/purpose restriction, independently run allowed, denied/omitted-field, altered recipient and failure-path cases, and inspect returned and stored bytes to prove the prohibited data did not remain accessible or generate a new unintended copy.
  - **Criteria:** The lineage reflects actual executed source/storage and at least two genuinely distinct data actions, not the same table viewed through two API endpoints or a speculative system diagram. Provenance and data/decision owners are identifiable, and a corrected field/purpose rule produces a real protected-state result while the valid task remains functional. The learner distinguishes a blocked response from a prior unauthorized write/export, detects at least one missing/duplicate or unobserved sink, and does not equate current observed coverage with all possible external processor copies. A notice, encrypted field or log statement cannot substitute for a denied data action.
  - **Evidence:** Owner-approved scope, synthetic data dictionary/purpose and retention policy, actual running source and DB/cache/export/log observations, per-copy subject/field and timestamp inventory, caller/recipient and decision map, original and corrected field-level source/policy diff, independent legitimate/denied/invalid/failure oracles and byte-level effect checks, missing-sink/evidence limitations and a reviewed data-lineage ledger.

- **SEC14-AS2** — Data Disclosure Controls, Logging and Processing-Authority Repair
  - **Outcomes:** SEC14-O2, SEC14-O3, SEC14-O4, SEC14-O5, SEC14-O6, SEC14-O10, SEC14-O12, SEC14-O13.
  - **Work:** Starting from the same real local data service, investigate and correct one actual privacy/security defect in export, derived output, logging/debug records or worker processing: an unnecessary field, wrong recipient/purpose, stale identity or plaintext payload leakage. Compare current at-rest/in-transit confidentiality and key/access control *claims* to actual plaintext/copy locations and enforce one justified processing decision at the source of consequential release or storage. Execute independently designed permitted, disallowed recipient, altered purpose, invalid input and safe failure cases, confirming both true returned/file/state effects and usable bounded audit events. Analyze a clearly labeled external processor/host record where unavailable but never replace the required executed local result with a vendor assurance.
  - **Criteria:** A real sensitive-by-policy field or copied record is no longer released/stored by the prohibited path; the implementation prevents alternate route, delayed worker, incorrect-purpose or failure logging exposure to the scope actually claimed. Legitimate workflows, data integrity and necessary security diagnosis remain verifiably functional. Encryption-only and authentication-only arguments are rejected when data remains readable at an unintended sink. Supplied vendor trace or simulated receiver acknowledgment is not described as proof that a real outside processor enforced the same control.
  - **Evidence:** Versioned local source/config and genuine before/after response/DB/export/log content, policy purpose/recipient and permissions, actual affected copy and caller, independent allowed/denied/invalid/failure and secondary-route oracles, minimally changed enforcing control, bounded audit event with redacted content and residual external/cryptographic assurance limits.

- **SEC14-AS3** — Retention, Authorized Deletion and Backup-Restore Non-Resurrection
  - **Outcomes:** SEC14-O1, SEC14-O2, SEC14-O3, SEC14-O4, SEC14-O6, SEC14-O7, SEC14-O8, SEC14-O9, SEC14-O10, SEC14-O12, SEC14-O13.
  - **Work:** Choose an authorized synthetic subject, distinguish legitimate preservation/hold conditions, execute an actual access, correction, processing restriction or deletion decision and update a durable current policy/source of truth. Capture a **genuine prior backup/snapshot** and an existing derived or exported copy, then delete/restrict or retain according to the declared approved rule. Independently verify primary, cache/derived, export and retained log state, and demonstrate at least one actual local deletion/restriction plus consequential downstream update. **Deliberately restore or replay a pre-deletion snapshot in a controlled test**, demonstrate the unsafe old behavior or another meaningful known-bad mutation, then enforce current tombstone/restriction or trusted post-restore reconciliation such that prohibited current data is not reactivated or exposed; verify a different permitted subject remains available.
  - **Criteria:** The original record and a different descendant copy are independently observed before change, and the effective current data-state/processing prohibition is demonstrably enforced, not merely acknowledged. The stale restore/replay exercises **real saved bytes** and would have exposed the old data without the corrected control or reconciliation; current-state verification detects the unsafe mutation. Denied and legitimate cases hold across primary and a relevant derived/export sink with correct subject matching and failure behavior. A retained backup under an accountable exception remains labeled retained/restricted, not sanitized; the graduate does **not** claim SSD/media destruction, third-party erasure, historical untrusted exports recalled, or legal compliance from an application DELETE, tombstone or deleted encryption-key ID.
  - **Evidence:** Approved synthetic subject/request and purpose/retention/hold matrix, real before/after primary and downstream copy bytes, actual versioned snapshot and controlled old-state restoration, executable tombstone/reconciliation or equivalent stale-replay suppression, independent removed-versus-permitted subject oracles and negative mutation, copy-state ledger with exact residual backup/export/recipient claims, accountable approval, expiry and honest user-facing disposition.

- **SEC14-AS4** — De-Identification, Recipient Trust and Privacy Risk Decision
  - **Outcomes:** SEC14-O1, SEC14-O2, SEC14-O3, SEC14-O4, SEC14-O5, SEC14-O10, SEC14-O11, SEC14-O12, SEC14-O13.
  - **Work:** Create a real local derived or export dataset of synthetic subjects with an explicit permitted statistical or operational purpose. Compare a raw/linked output with a candidate pseudonymized, suppressed or aggregated design. Demonstrate a bounded **synthetic auxiliary-data join or small-group inference** that defeats an overconfident "anonymous" claim, then implement and independently test a lower-disclosure version while preserving an agreed useful outcome. Assess source/recipient authority, actual exported fields, de-identified copies, reidentification uncertainty, log retention and a conflicting preservation/processing requirement. Review a labeled simulated external receiver versus a genuinely independently observed local one, choose a defensible disclosure/hold decision and list what additional external or legal authority would be required before releasing real data.
  - **Criteria:** The original linkage/inference risk and corrected report are reproducible with genuine local data/exports and an explicit utility requirement; a replaced name/hash is not automatically asserted to be anonymization. The learner identifies auxiliary information and sparse-output limits, actual purpose/recipient controls, realistic additional disclosure routes and remaining privacy harm. A correct privacy assessment does not purport to prove mathematical impossibility of linkage, a universal anonymity guarantee, a full DPIA, compliance with all data-protection laws or actual third-party deletion. Normal and prohibited disclosure are separately checked without exposing any actual individual's information.
  - **Evidence:** Synthetic original and auxiliary data fixtures, actual original and safer transformed/aggregated output files, testable linkage or small-group counterexample, minimized purpose/recipient policy, independent allowed/restricted artifact oracles, impact and residual reidentification analysis, source/recipient provenance and owner-reviewed disclosure/hold recommendation.

- **SEC14-AS5** — Unfamiliar Data Lifecycle Change and Independent Technical Defense
  - **Outcomes:** SEC14-O1, SEC14-O2, SEC14-O3, SEC14-O4, SEC14-O5, SEC14-O6, SEC14-O7, SEC14-O8, SEC14-O9, SEC14-O10, SEC14-O11, SEC14-O12, SEC14-O13, SEC14-O14.
  - **Work:** Receive a reviewer-selected unfamiliar but safe data-flow change: new field, mismatched subject, altered processing purpose/recipient, stale export or worker retry, secret in error log, extended backup policy, restored snapshot, supposedly anonymous join, delayed deletion instruction or conflicting retention hold. **Before observing decisive results**, predict which subjects/copies should remain, which action must be denied and a credible alternative explanation. Execute the changed case on the owned versioned system, inspect real primary and downstream data-state bytes, repair the correct data-processing or lifecycle control or defend an actually enforced bounded restriction/hold, and re-run legitimate, denied, invalid, stale restore/replay and meaningful failure tests. Update provenance, purpose, exceptions, residual externally unverified copies and de-identification/privacy risk, then individually defend the source/code/policy/test and honest owner decision.
  - **Criteria:** The learner correctly identifies a new data-processing or lifecycle risk rather than repeating a memorized exercise and demonstrates a real protected data-state change or appropriately enforced restriction with an independently reviewable negative/fault test. Prior evidence is explicitly withdrawn if a changed recipient, retention, derived copy or restoration path makes it invalid. Normal authorized use and relevant data integrity remain verified; backup/recipient limitations and purpose/legal determination boundaries are named. The defense distinguishes logical removal from media sanitization, local synthetic processor evidence from real external deletion and pseudonymization from verified anonymity; it makes no blanket compliance or guaranteed absence-of-copies claim.
  - **Evidence:** Reviewer challenge and pre-observation prediction/alternative, source/data/provenance and policy revisions, actual local primary/derived/export/log and relevant snapshot observations, independently reproducible allowed/denied/invalid/failure and stale-state tests, meaningful correction/hold and negative mutation, updated full data/exception ledger, privacy-safe risk-owner recommendation, and individual written/recorded/live technical defense.

### Graduation evidence and honest professional scope

Each assessor records the appropriate `SEC14-O#` and `SEC14-AS#` decision against the **actual locally observed source, data and policy**. A claimed deletion must say **what was deleted, when, from which observed current copy, how independently verified, and which retained, unavailable or external copies remain**. Successful restore suppression of an old synthetic record is not a claim that the original physical storage blocks were sanitized, that an uncontrolled vendor destroyed its replica, or that all archive and disaster-recovery systems are already clean. Conversely, an approved retained backup or legal hold must not be mislabeled completed erasure. Reject blanket claims that pseudonymization equals anonymous data, that a secure cipher grants permission to process, that a scan establishes all data locations or that an emailed rights request alone proves a correct result.

This course establishes **bounded professional data-security and privacy engineering competence**, not privacy officer/legal counsel accreditation, international regulatory certification, processor auditing authority, physical storage sanitization expertise or production compliance. Independent tests establish meaningful local data processing and lifecycle effects, with explicit remaining uncertainty. A safe “restrict/hold pending owner review” can be an appropriate disposition when evidence or valid legal/policy authority is missing, but cannot replace the course's required executed local protections, data-copy lineage, backup/restore test or independent technical defense. The course remains `draft` pending observed learner and qualified reviewer evidence under [Status Labels](../../spec/status-labels.md).

### Optional disciplinary references

- [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — privacy risk management, authorized processing and predictability, manageability and disassociability; be precise about published versus draft versions of framework updates.
- [NIST SP 800-188 — De-Identifying Government Datasets: Techniques and Governance](https://csrc.nist.gov/pubs/sp/800/188/final) — de-identification and realistic reidentification/linkability governance, not automatic anonymity guarantees.
- [NIST SP 800-88 Rev. 2 — Guidelines for Media Sanitization](https://csrc.nist.gov/pubs/sp/800/88/r2/final) — September 2025 final for storage/media sanitization policies and evidentiary limits; application-level logical deletion is not physical sanitization.
- [OWASP ASVS 5.0, V14 Data Protection](https://github.com/OWASP/ASVS/blob/master/5.0/en/0x23-V14-Data-Protection.md) — requirements for data handling, sensitive logs, exposure, retention and protection appropriate to each data class.
- [OWASP SAMM, Data Protection](https://owaspsamm.org/model/operations/operational-management/stream-a/) — data categories, handling, protection and operational governance by actual risk.
- [NISTIR 8062 — An Introduction to Privacy Engineering and Risk Management](https://www.nist.gov/publications/introduction-privacy-engineering-and-risk-management-federal-information-systems) — problematic data actions and privacy engineering objectives, beyond network confidentiality.
- [EDPB Guidelines on Data Protection by Design and by Default](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-42019-article-25-data-protection-design-and_en) and [2026 coordinated enforcement review on erasure](https://www.edpb.europa.eu/news/edpb-identifies-challenges-hindering-full-implementation-right-erasure_en) — genuine deletion, retention and backup-restoration problems in applicable GDPR contexts; not a universal legal mandate.
- [GDPR Article 17, official EU text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) — right to erasure and qualified exceptions under applicable legal scope; engineers must refer jurisdictional and legal decisions to accountable experts.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/final) — representative access, privacy, media and retention control objectives; course requirements are evidence-driven, not a claim of framework-wide certification.

These references ground technical and privacy-risk decisions. Published `SEC14-O#` and `SEC14-AS#` evidence—not an imposed count of courses, compliance badges, individual regulation, vendor product or diagram—is the educational contract.
