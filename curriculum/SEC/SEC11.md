# SEC11 — Endpoint & Platform Defense

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC7](SEC7.md), [SEC10](SEC10.md)
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–14 focused hours/week (provisional; 140–252 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**Endpoint security is a claim about what an actual device, operating system and its protection agents permit, block and record—not a security-baseline spreadsheet or an agent icon that says protected.** SEC11 prepares a security engineer to assess and strengthen enterprise workstation/server endpoint posture across Linux and Windows, making explicit the boundary between the host operating system, local privilege, executable identity, management policy, device and credential trust, defensive agents, telemetry, recovery and the wider identity and deployment systems. Learners establish a controlled host and threat model; apply real least-privilege and execution/resource security changes in a disposable endpoint; interpret genuine Windows and Linux security-policy/event evidence; test protection and sensor effectiveness on benign and safely suspicious cases; respond to drift and compromised local authority; and defend an unfamiliar endpoint change without assuming that compliance, logging or vendor status equals enforcement.

**Prior competence and distinct ownership.** [SEC4](SEC4.md) has already taught network/service reachability, POSIX permissions and host configuration from a service-exposure viewpoint; [SEC7](SEC7.md) has already taught detection logic, evidence preservation, incident handling and recovery; [SEC10](SEC10.md) has already taught workforce authentication, SSO, entitlement lifecycle, service accounts and constrained privilege. SEC11 uses these foundations to assess **endpoint-specific policy and control mechanisms**: host security baseline construction, user/kernel privilege boundaries, Linux MAC/DAC and process execution, Windows endpoint security configuration, policy source/precedence, local administrator or token boundaries, application control, audit-versus-enforce states, endpoint agent/telemetry trust and device-specific drift/rollback. [SEC6](SEC6.md) owns workload container isolation and CI supply-chain authorization; an endpoint is not simply a container. This is not a duplicate SEC7 incident-handling course or a Windows enterprise directory-administration course, and it does not replace [SEC3](SEC3.md) memory/binary exploitation competency.

**The professional distinction between Linux and Windows.** A working Linux permissions experiment cannot prove that Windows App Control, Microsoft Defender, credential protections, Group Policy or a domain token behaves the same way. Conversely, an authentic Windows Event 4688 or Sysmon process event is a record of observed activity under a named policy and configured sensor; it is **not evidence a given execution was blocked**. Application-control audit mode records what would be disallowed under a specific policy and target, but does not itself enforce denial. A Windows setting visible in Group Policy is not always effective policy: inherited precedence, security filtering, policy refresh and device version/context matter. A local application-allowlist mock is not Windows kernel-enforced application control. Preserve those distinctions in every assessment and review.

**Equitable, real endpoint enforcement.** Each learner needs access to one free, owned or pre-provisioned disposable **Linux endpoint or equivalent isolated full OS environment**, with actual kernel-enforced file/process ownership, a safe dedicated unprivileged identity or two preconfigured distinct principals where required, versioned synthetic files, harmless executables, reversible settings and inspectable event sources. The provided fixture must make allowed and denied behavior observable with **real operating-system enforcement**, not merely a model/policy interpreter; if a restricted host cannot safely provide the necessary test boundary, use a pre-provisioned authorized VM or equivalent isolated host provided by the educator, not a false passing substitute. No learner must change a shared/unmanaged host, install a kernel driver, disable real protection, operate root on their personal machine or run offensive payloads. Optional host-specific hardening (for example, service management, systemd sandboxing, auditd, AppArmor, SELinux, eBPF sensors or endpoint firewall rules) requires a disposable authorized environment; when a platform does not support a property, label the genuine target/version source and do not claim a local enforcement test.

**Windows access and honest achievement.** Provide a *separate*, genuine target/OS-version-labeled Windows endpoint reference corpus with appropriate source provenance: effective or expected security policy, Windows Security 4624/4688 and/or Sysmon process/file/registry events, App Control audit/enforcement policy and event results, credential/device-control state where available, a benign lookalike, missing telemetry and a changed-policy case. Learners must analyze these **as Windows artifacts** with Windows-specific semantics, validate competing hypotheses and produce correct, testable Windows endpoint-control plans. A supplied trace does not establish hands-on Windows administration or live Windows policy enforcement. An approved disposable Windows evaluation VM or otherwise legitimately licensed owned Windows device can be used for **additional genuine Windows practical evidence**; record its edition/build, policy mode, actual managed enforcement, access rights, safety, setup and measured before/after result. This extension is recommended when accessible but is **not a hidden licensing, paid cloud or high-RAM VM prerequisite**. The universal graduation claim is **real Linux endpoint enforcement plus evidence-competent Windows defense assessment**, not independent hands-on deployment of a domain-wide Windows security baseline. Windows administration cannot be certified from trace-only work.

**Endpoint assurance versus separate responsibilities.** SEC11 does not teach all Windows Server administration, SOC alert investigation, domain incident response, malware reverse engineering, hard-drive forensic imaging, exploit development, enterprise MDM/EDR deployment or organization-wide compliance. It does require independent control choices and actual safe effects at the host level; correct Windows/platform-specific analysis; testable policy and agent coverage recommendations; and a bounded owner decision with clear residual risk. [SEC7](SEC7.md) supplies deep incident evidence; this course asks whether the **endpoint defense** produced a trustworthy block, alert, telemetry field and protected-state result. Continuous multi-asset vulnerability prioritization and patch-program management belong to the subsequent independent SEC competency, although this course must understand correct local patch/configuration state, rollback and risk.

**Authorization and safety.** Obtain specific owner permission for the selected endpoint, local user and data fixture, permitted process and service operations, local configuration edits, telemetry collection, scope exclusions, resource ceilings, reset, privacy rules and stop conditions. Only synthetic accounts, inert sample processes, deliberately benign persistence-like markers and disposable local data are acceptable. Do not install real malware or rootkits, attempt credential dumping, circumvent antivirus on a real device, tamper with another person's EDR, use unauthorized domain administrative privileges, perform lateral movement or disrupt a corporate network. A safe test may demonstrate an innocuous user-level auto-start entry on an approved fixture; it must never implant covert persistence in a production host. Redact identifiable users, command-line secrets and recovered credentials from evidence.

**Instruction and evaluation.** One evolving owned Linux endpoint plus genuine bounded Windows reference materials supports five summative decisions: platform baseline and actual permission enforcement; Windows policy and execution assurance; endpoint sensor/behavior evaluation; drift, resilience and safe host restoration; and an unfamiliar individual technical defense. Outcomes and summatives are not sized by a template, and optional investigations are not mandatory micro-labs. The **14–18 weeks at approximately 10–14 focused hours/week** is provisional, not learner-calibrated. Status remains `draft`.

## Learning outcomes

- **SEC11-O1:** Establish an authorized endpoint-defense assessment, inventory actual OS/build, owner, workloads, local and federated identities, administrative channels, agents, protected data, network paths, management authorities, policies, recovery state and enforcement-versus-observation boundaries, with a falsifiable host-security objective.
- **SEC11-O2:** Derive and evaluate an endpoint security baseline from explicit user/workload requirements and threat paths, distinguishing required controls, policy owner, effective source/precedence, supported platform and version, exceptions, actual compliance observation, control enforcement and independent negative-test evidence.
- **SEC11-O3:** Inspect and test actual OS-enforced identity, local administrator, user/group, file/IPC/service and process privileges in an owned Linux host environment; correct an excessive privilege or resource exposure while preserving legitimate tasks and documenting the exact kernel-enforced boundary.
- **SEC11-O4:** Assess trusted execution, software provenance, executable/script policies, local service auto-start and harmless persistence-like paths; test a meaningful actual local execute/permission control and distinguish it from application allowlisting, host integrity checks and unavailable Windows kernel enforcement.
- **SEC11-O5:** Interpret target/version-specific Windows endpoint and domain-management artifacts including token elevation, local admin rights, Group Policy/MDM resultant policy, App Control audit-versus-enforce state, AppLocker/ASR distinctions, registry/service persistence and realistic configuration interactions without substituting Linux analogies for Windows evidence.
- **SEC11-O6:** Explain and evaluate endpoint credential, boot, device and disk protection including available secure startup, disk encryption and recovery keys, phishing-resistant sign-in and credential isolation; assess limits of evidence from stated hardware/TPM, policy and event records and avoid claiming enforcement merely because a setting is configured.
- **SEC11-O7:** Build and evaluate target-specific endpoint process, logon, file, registry, executable-integrity and configuration-change telemetry from real locally collected events and genuine labeled Windows traces, preserving event provenance, clock context, sensor configuration, loss, privacy and alternative explanations.
- **SEC11-O8:** Independently test an endpoint protection/detection decision with permitted and safely suspicious behavior, false-positive lookalikes, missing data and a changed configuration, distinguishing detection, audit-only reporting, actual preventive block, protected-state impact and sensor coverage limitations.
- **SEC11-O9:** Evaluate device and management-plane trust for endpoint enrollment, local/remote policy, administrator rights, managed-vs-unmanaged device claims, policy refresh and unauthorized change, separating IdP assertions from tested device compliance and host enforcement.
- **SEC11-O10:** Implement and verify a bounded host hardening or agent/policy correction, independently detecting configuration drift or reverted permission, assessing user disruption, documenting safe rollback and proving continued legitimate service together with an actual denied unsafe path.
- **SEC11-O11:** Design and exercise a safe endpoint containment, evidence preservation and recovery/change-response scenario in an owned fixture with specific authority, identity/credential exposure, service restoration, persistence check and post-recovery enforcement/telemetry verification, without treating host reset as proof no adversary remains.
- **SEC11-O12:** Produce an independently reproducible cross-platform endpoint security review and owner-actionable exception/repair decision, explicitly separating real local Linux effects, authentic Windows/EDR policy traces, modeled behavior, unverified settings, product limitations and professional qualifications not established.
- **SEC11-O13:** Independently predict and investigate a reviewer-selected unfamiliar Windows/Linux policy, execution, privilege, device, sensor or recovery condition, implement a safe local correction or justified restriction, test expected and unexpected effects and defend causal, platform-specific conclusions.

## Modules

### Module 1 — Endpoint Scope, Ownership and Effective Security Baselines

#### Outcomes

- SEC11-O1
- SEC11-O2
- SEC11-O6
- SEC11-O9
- SEC11-O12

#### Lessons

1. **Endpoint versus service, container and directory control** — Given a pre-provisioned owned endpoint with an ordinary synthetic user, a protected configuration and harmless process, identify OS/build, users, local admin versus domain/group authorities, active services, device-policy origin, software source, security agents, recovery boundary and reachable interfaces. Draw which decision is enforced by an actual host, which by a remote manager or application, and which is only reported by a dashboard.
2. **Baseline as testable security requirements** — Derive an authorized workstation or server security baseline from actual legitimate uses and plausible harms, with effective principal/action/resource controls, permitted local services, automatic updates and rollback ownership. Rank controls by actual exposure, reversibility and user effects. A benchmark score or advertised "compliant" policy alone does not pass.
3. **Observed state versus declared management intent** — Trace versioned local settings, service launch options, owned file permissions, running process identity and agent configuration against baseline expectations. Contrast manager intent, last-known configuration, actual enforcement and state inferred from an event; specify a wrong-policy, revoked device or missing telemetry observation that would falsify compliance.
4. **Device and credential protections by supported platform** — Map disk encryption, recovery key custody, supported measured or secure boot/TPM claims, local secret isolation, firmware update and identity/device claims to available platform-specific evidence. Distinguish supported/unsupported feature, enabled/configured status, attestation, actual blocked access and what cannot be tested in a rootless or virtual fixture.
5. **Policy sources, exceptions and safe administration** — Identify local, directory/MDM and endpoint-protection policy owners, effective precedence or refresh, administrative separation, safe audit-first rollout, authorized exceptions and recovery procedure. Do not apply a test policy outside the designated host. Define how to test a user whose functionality must remain permitted.

*Optional formative feedback:* A dashboard displays "compliant" while a user can still read a protected test file. Identify the enforceable layer and the evidence the dashboard lacked.

### Module 2 — Linux Host Privileges, Resource Access and Execution Integrity

#### Outcomes

- SEC11-O1
- SEC11-O2
- SEC11-O3
- SEC11-O4
- SEC11-O9
- SEC11-O10

#### Lessons

1. **A real permission boundary with two host principals** — Run controlled permitted and prohibited file/service operations using preconfigured distinct Linux users, groups or properly isolated OS user contexts on an owned endpoint. Inspect UID/GID, supplementary groups, process identity, ownership, ACL/mode and effective filesystem decisions. Use the actual OS access result and protected file content/state, not an application "deny" string.
2. **Privilege transition and administrative authority** — Inspect minimal approved service identity, setuid/setgid/capability or service-manager restrictions only where provided and safe; distinguish discretionary permissions, effective credentials and a rootless namespace from real host-root authority. Reproduce a least-privilege violation or correctly blocked path; correct it using the smallest allowed change and verify legitimate users still work.
3. **Owned service start, task and harmless auto-start** — Trace a versioned synthetic service's launch command, environment, working directory, writable executables, trusted configuration, user-level scheduled task/timer or auto-start location and parent/child process evidence. Demonstrate a harmless unexpected autostart or writable-script path **only inside an approved disposable fixture**, then close it and independently check it cannot recur.
4. **Executable origin, integrity and host process restrictions** — Compare package signature/source identity, expected hashes, immutable source/verified installation, user/execute permissions and available mandatory access controls. Apply or observe a real host-enforced file/execute or confined-process boundary and a real denied attempt; clearly distinguish it from a user-space allowlist or static hash check.
5. **Safe permission and control changes** — Stage a real owned permission/service policy correction, predeclare normal/forbidden/invalid oracles, observe changed actor or path, test safe rollback and defend residual access from groups, alternate paths, copies or an unchanged privileged process.
6. **Where local Linux evidence does not transfer** — Compare Linux DAC/MAC, seccomp/namespace confinement and audit mechanisms with Windows access tokens, UAC elevation, App Control, ASR, Credential Guard and policy enforcement using named primary specifications. Record which mechanisms were actually exercised and which must be evaluated later from authentic Windows target records.

*Optional investigation:* A protective permission change blocks the test user but a privileged service still modifies the object through another path. Distinguish enforcement scope, expected policy and actual authority.

### Module 3 — Windows Endpoint Policy, Platform Identity and Execution Control

#### Outcomes

- SEC11-O1
- SEC11-O2
- SEC11-O4
- SEC11-O5
- SEC11-O6
- SEC11-O9
- SEC11-O12

#### Lessons

1. **Read real Windows endpoint state without inventing enforcement** — Inspect a genuine Windows build/edition-labeled security baseline and effective or observed configuration, local/domain group membership, UAC/elevated token and approved directory/MDM policy scope. Resolve at least one competing policy source, filtering or refresh condition; distinguish a configured setting, resultant policy, audit evidence and an actual enforcement result.
2. **Windows application control and audit mode** — Evaluate a real target-labeled App Control for Business or AppLocker policy and corresponding authentic audit/allow/deny events. Compare signing/publisher, path/hash, executable/script and rule precedence assumptions appropriate to policy type/version. Predict which safe executable would be allowed or *logged as would-block* in audit mode versus actually denied in enforcement mode; never award a kernel-block test for audit-only events.
3. **Endpoint antimalware and attack-surface reduction** — Analyze authentic Defender/ASR policy and event output, tamper-protection state, relevant exclusion and engine freshness with a benign/hostile-lookalike case. Explain vendor agent trust, sensor failure modes, local admin interference and why a signature update, running service or green EDR console is insufficient proof of blocking.
4. **Windows identity, credential isolation and policy delegation** — Trace genuine logon/elevation, local administrator, service-account, credential-protection, disk/boot security and device-compliance data against SEC10 workforce privileges. Identify what a domain login or MFA token actually changes on an endpoint and what a compromised local admin may still do. A domain controller policy view or identity claim does not prove device compliance or an active hardware-backed protection.
5. **Authentic Windows endpoint case and optional hands-on extension** — Given genuine paired Windows process/registry/file/logon and application-control records, identify actor, executable, parent process, signing trust, policy mode, device build, timestamps, a plausible false positive and an actual unresolved authorization/execution question. Recommend an actionable policy test and valid rollback. Learners with an **approved disposable, legitimately licensed Windows target** may independently test an actual Windows control; those who cannot must report that their evidence is interpretive, not hands-on Windows administration.

*Optional formative feedback:* App Control records an audit event for a harmless test binary while that binary runs successfully. Explain why the audit result is not a prevention test, and specify the distinct evidence needed before enabling enforcement.

### Module 4 — Endpoint Telemetry and Protection Effectiveness

#### Outcomes

- SEC11-O1
- SEC11-O4
- SEC11-O5
- SEC11-O7
- SEC11-O8
- SEC11-O9
- SEC11-O12

#### Lessons

1. **Actual host events and sensor provenance** — Generate bounded permitted and rejected local operations and collect genuine available host/process/file/permission records, recording source, process/user/path, event time, clock resolution, sensor configuration and missing fields. Compare audit source authority and what a log cannot prove about protected state; avoid logging synthetic credential values.
2. **Interpret Windows Security and Sysmon event semantics** — Independently analyze authentic target-labeled Windows Security 4624 and 4688 plus appropriate Sysmon Event ID 1, 11 and 13 or supported equivalent: correct logon and process relationships, process GUID/PID reuse, file creation, registry-value changes, rule include/exclude filters and collection gaps. Do not assume the presence of Sysmon proves all suspicious behavior was captured or that the same event means identical things across builds and configurations.
3. **Audited versus blocked versus undetected** — Specify separately the predicted security policy decision, endpoint application execution, actual resource action and emitted event. Reconstruct a controlled harmless suspicious behavior, approved admin lookalike and omitted-sensor/changed-policy case from local actions plus authentic Windows traces, labeling which environment truly enforced each decision.
4. **Independent protection and alert checks** — Exercise or reproduce a real locally executed protection or access-restriction test, a separate permitted activity and a missed/altered signal; evaluate a narrow event query/rule and its false-positive and false-negative cases. Where the local host lacks an EDR engine, report **host evidence and local protection outcomes** but do not claim tested commercial antivirus, ransomware interception or vendor EDR prevention.
5. **Telemetry retention, tamper limits and decisions** — Evaluate privileged agent settings, log rotation/retention, disconnected endpoint, local timestamp manipulation, missing event, sensitive command-line data and constrained evidence preservation. Explain practical mitigations such as protected forwarding, central policy and least-admin telemetry management, distinguishing demonstrable owned settings from recommended enterprise controls.

*Optional investigation:* A legitimate software update produces the same process and registry pattern as the suspicious case. Derive additional discriminating evidence before escalating a false positive.

### Module 5 — Drift, Change, Containment and Safe Restoration

#### Outcomes

- SEC11-O1
- SEC11-O2
- SEC11-O3
- SEC11-O7
- SEC11-O8
- SEC11-O9
- SEC11-O10
- SEC11-O11
- SEC11-O12

#### Lessons

1. **A baseline must survive real change** — Apply one approved OS/file/service security correction and test its normal/denied behavior; then introduce a safe policy drift, changed group, service reinstall, removed sensor setting or unauthorized change in the disposable host. Independently determine what changed and whether controls, monitoring and expected user access still hold.
2. **Update and platform trust without a fake exposure program** — Verify the selected local OS/package/agent update source, supported version, rollback opportunity, file identity and restart/availability implications. Explain local patch applicability and effects but leave multi-asset vulnerability inventories, KEV/EPSS prioritization, remediation SLA and exception governance to their dedicated SEC competency.
3. **Host restriction, evidence and recovery trade-off** — Given a bounded harmless local security event and a permitted response owner, preserve necessary logs/configuration and choose a reversible process stop, synthetic account disablement, service restriction or local data isolation as appropriate. Measure whether the requested dangerous access is denied and legitimate service can recover; never assume deleting a suspicious file establishes full compromise eradication.
4. **Recovery and persistent exposure verification** — Roll back from a known clean test snapshot or documented configuration, reapply the corrected security control, verify that an unauthorized auto-start/grant is absent, check credentials/role effects and test actual permitted/denied process and resource behavior. Re-evaluate the sensor and owner exception; leave unresolved identity/domain or hardware compromise honestly held.
5. **Owner-focused change approval and sustainable control assurance** — Present a prioritized endpoint control decision with provenance, supported OS/builds, policy-owner responsibility, rollout/rollback order, legitimate-user false-denial risk, observable verification, residual exceptions and review trigger. The recommendation must work at the declared enforcement point, not merely quote CIS or NIST control numbers.

*Optional formative feedback:* After rollback the service is available and its monitoring agent reports healthy, but the original forbidden file is writable again. Produce a safe hold decision and a regression that detects it.

### Module 6 — Unfamiliar Endpoint Defense and Individual Technical Review

#### Outcomes

- SEC11-O1
- SEC11-O2
- SEC11-O3
- SEC11-O4
- SEC11-O5
- SEC11-O6
- SEC11-O7
- SEC11-O8
- SEC11-O9
- SEC11-O10
- SEC11-O11
- SEC11-O12
- SEC11-O13

#### Lessons

1. **Predict an unseen control or sensor change** — Receive a reviewer-selected new bounded event in local privilege, service ownership, executable path, Windows policy mode/effective rule, device management, agent coverage or recovery rollback. Before inspecting decisive evidence, state valid and forbidden behavior and a credible competing explanation. Identify where a real local test is possible and where genuine labeled platform evidence is the only permitted observation.
2. **Correct the enforcing boundary, not the dashboard** — Reproduce a changed local permission/execution/host state or analyze a genuine new Windows policy/telemetry record. Explain the difference between a false block, missed event and actual unsafe permission. Implement a minimal safe change and rerun real local permitted, denied, invalid/failure and changed-state tests; determine whether an observed Windows audit result could actually justify a prevention claim.
3. **Independent defense and accurate professional claim** — Submit versioned authorized Linux fixture and source/policy, protected-state tests, original and changed Windows evidence provenance, effective baseline and agent/sensor conclusions, rollback/response, explicit non-exercised platform limits, owner risk/release recommendation and independent written, recorded or live code/policy/evidence defense. Explain what further access and supervision would be necessary before claiming to have personally administered Windows domain endpoints or enterprise EDR.

*Optional formative feedback:* A reviewer reverses an expected Windows App Control deny to audit-only without changing the policy expression. Explain the observed result, how actual security assurance changes and which original claim must be withdrawn.

## Completion requirements

**Five required summative evaluations** assess SEC11's distinct endpoint mechanisms. The same authorized disposable Linux OS fixture and authentic versioned Windows endpoint corpus may be reused; the required claims differ by actual control and evidence source. Each evaluation must document the exact permitted target/identity, OS/build, controlled authority, source/configuration revision, independent expected result, **actual executed host access/state** where local enforcement is claimed, any external genuinely supplied Windows policy/events, legitimate service effects, safe reset and known unsupported host/agent capabilities. A policy file, scanner finding, "protected" dashboard, malicious-looking process name or synthetically invented log line does not by itself demonstrate a secure host or a compromise. All protected-state and host-enforcement claims must be falsifiable with real owned observations.

- **SEC11-AS1** — Endpoint Baseline and Enforced Host Authority
  - **Outcomes:** SEC11-O1, SEC11-O2, SEC11-O3, SEC11-O4, SEC11-O9, SEC11-O10.
  - **Work:** Identify and characterize an owned, disposable Linux endpoint with distinguishable user/service roles, permitted workload and protected file or command boundary; trace an actual local process to its UID/GID, file/service and relevant policy. Define a least-privilege and execution integrity baseline with a permitted, forbidden, changed-role/path and operational-failure oracle. Using preconfigured users, a supplied isolated environment or a safe named host interface, **execute a genuine kernel-enforced denial** of resource or execution access and the corresponding real normal operation. Introduce a safe intentionally incorrect permission, user/service launch or executable-writability condition, correct it at the actual host boundary, and independently retest effects, rollback and any bypass via alternative path or inherited group. Distinguish local file/OS access controls from merely application-checked permissions and record source and platform constraints.
  - **Criteria:** Real host kernel control—not only a local policy simulator or HTTP status—prevents the named unauthorized operation and retains justified user behavior. Actor, actual effective privilege, path, test boundary and original/changed configuration are demonstrable from owned commands and protected-state observations. A failed command due to missing executable, an unavailable service or an unrelated error does not prove the expected security control denied it. At least one changed-role, alternate path or rollback negative case would expose a superficial repair. The learner avoids unmanaged host modifications, claims only available OS controls and explains scope of an allowed user or service account.
  - **Evidence:** Owner authorization, OS/runtime/build and principal inventory, baseline/exception and control-owner matrix, actual process/UID/GID and resource/file-state evidence, independent allow/deny/failure oracles, before/after and deliberate drift tests, real protected-resource observation, permission/config diff, versioned safe reset and residual constraints.

- **SEC11-AS2** — Windows Policy, Credential and Execution-Control Evidence Review
  - **Outcomes:** SEC11-O1, SEC11-O2, SEC11-O4, SEC11-O5, SEC11-O6, SEC11-O9, SEC11-O12.
  - **Work:** Assess one genuine, version-labeled Windows reference endpoint containing an attributable policy source/precedence/effective configuration, Windows logon/process data, signed/unsigned safe executable identity, audit-only and enforce-like application-control observations, a harmless file/registry persistence-like marker and named device/credential protections. Independently predict which operation is allowed, blocked, logged as would-block or unobserved under each exact policy/OS condition. Evaluate a policy-filtering/refresh or changed-group/token counterexample, an ASR/AppLocker/App Control distinction and a secure-boot/disk/credential claim whose effective state is not established by its configuration alone. Propose a version-appropriate least-authority change, deployment/rollback and a genuine evidence test that would establish the intended enforcement. Optional authorized Windows hands-on tests can supplement but cannot be fabricated or automatically assumed for completion.
  - **Criteria:** The assessor correctly distinguishes source policy from resulting device policy, Windows local/domain token privileges from IdP grants, audit-mode execution from actual prevention and endpoint agent reporting from a genuine protected-state result. Trace provenance identifies at least one real target, OS/build, policy mode, sensor configuration and event-source condition; the learner challenges a supplied false positive or missing event and explicitly marks what was not executed. The recommended repair is technically feasible for the stated Windows capability and includes a safe validation path. Interpretation-only work is **not credited as Windows configuration execution or administrator proficiency**. Live Windows evidence, if supplied, must show actual approved allowed/denied actions rather than a screenshot of a checked setting.
  - **Evidence:** Genuine labeled policy/effective-state material and Windows Security/Sysmon or comparable source event record, OS/build/device constraints, policy precedence and expected/observed audit/enforce matrix, token/credential and application integrity review, credible alternate explanation, corrective plan and reproducible test/rollback proposal; separately labeled actual Windows execution if legitimately performed.

- **SEC11-AS3** — Endpoint Protection Signal and Control Effectiveness
  - **Outcomes:** SEC11-O1, SEC11-O4, SEC11-O5, SEC11-O7, SEC11-O8, SEC11-O9, SEC11-O12.
  - **Work:** Execute a safe local permitted process/file operation, an approved denied/persistence-like change, a benign lookalike and a changed-source/missing-event case. Collect genuine owned Linux host events, capture event identity and source integrity/clock context, and correlate actual OS permission or execution state with recorded evidence. Evaluate authentic Windows process/logon, Sysmon and App Control/Defender/ASR audit or enforcement cases with labeled source/version, including a true mode distinction and at least one realistic sensor filter or coverage gap. Implement and independently evaluate a bounded local query/detection/check, quantify meaningful positive and false-alarm behavior for the fixed corpus and recommend an endpoint control or telemetry correction without claiming a test of an unavailable enterprise EDR.
  - **Criteria:** A host or agent prevention claim is supported by evidence of actual enforcement in the appropriate exercised environment; a mere emitted event cannot be labeled a block. Distinct normal, denied, benign-lookalike, missing-data and changed-config cases establish what the detection/query catches and what it misses. No fabricated Windows events or inferred Windows policy effectiveness is presented as locally run, and actual owned telemetry has time, source, identity, relevant fields and privacy boundaries. A meaningful local control/detection improvement retains normal operation; derived coverage rates are explicitly limited to the given cases, not generalized to production.
  - **Evidence:** Actual Linux actions, resulting protected state and collected logs; independently established positive/negative/benign/missing case matrix and executable query/host check; authentic Windows record/policy/version provenance and audit-versus-enforce comparison; corrected rule/config and post-change replay; redacted collection/retention/limitation notes and risk decision.

- **SEC11-AS4** — Endpoint Drift, Safe Containment and Verified Recovery
  - **Outcomes:** SEC11-O1, SEC11-O2, SEC11-O3, SEC11-O7, SEC11-O8, SEC11-O9, SEC11-O10, SEC11-O11, SEC11-O12.
  - **Work:** For the same authorized endpoint, introduce a reviewer-approved harmless drift event (changed owned ACL/group, user-level auto-start/launch permission, safe service policy or telemetry configuration) with a plausible normal maintenance explanation. Detect it using independently specified policy/state and event checks; decide whether to contain or hold, identify necessary evidence and owner authority, apply a reversible actual local containment or permission restoration and assess service disruption. Reset from a known-good owned fixture, rerun original and changed benign/prohibited requests, test that unwanted auto-start/resource access is not retained and verify a meaningful signal remains available. Explain which recovery and device/account mechanisms cannot be fully established by a local fixture and what should be escalated.
  - **Criteria:** Changes and restoration are actually demonstrated at an OS-enforced host-resource boundary with separate operational and security oracles. Evidence/agent records before containment are preserved where safe, and event loss or changed source is identified. Legitimate functionality returns and the forbidden path remains denied; a healthy agent status or restored process alone fails. A recovery claim does not overstate device/firmware, domain, kernel compromise eradication or production fleet rollout. Risk owner, rollback trigger, exceptions, privacy and safe operation are documented.
  - **Evidence:** Predeclared host baseline, drift stimulus and owned source/policy revisions, actual local allowed/denied/failure-state evidence, bounded event and containment decision, pre/post process/file/service state, restoration and monitoring regression, Windows/other unavailable protection limits and owner recommendation.

- **SEC11-AS5** — Unfamiliar Cross-Platform Endpoint Defense and Individual Review
  - **Outcomes:** SEC11-O1, SEC11-O2, SEC11-O3, SEC11-O4, SEC11-O5, SEC11-O6, SEC11-O7, SEC11-O8, SEC11-O9, SEC11-O10, SEC11-O11, SEC11-O12, SEC11-O13.
  - **Work:** Receive an independent, previously unseen, safe change appropriate to the defended fixture and target evidence: a newly effective Linux group/ACL or service path, changed executable ownership, a Windows application-control policy now only auditing, unexpected process parent or telemetry exclusion, changed device claim, stale administrator group, revised source priority or safe restore condition. Before decisive inspection, predict the legitimate and prohibited host/resource result and a competing explanation, and state precisely which actual enforcement point should decide it. Execute a bounded real local Linux test and inspect the new authentic Windows evidence where applicable; implement a minimal real local correction or justify restricted/hold status, rerun independently derived permitted, denied, invalid/failure and telemetry/restore checks, and individually defend the chosen Windows-specific interpretation, evidence provenance, limitation, user impact and residual risk.
  - **Criteria:** The learner diagnoses a genuine new control or observation failure instead of restating an earlier lab, distinguishes actual OS enforcement, execution audit, agent reporting and unsupported assertions, and can inspect and explain source/config/events under independent challenge. A genuine local correction changes a relevant host-protected state while preserving justified legitimate use, or a safe enforceable hold is defended with its remaining risks. Windows conclusions are correct under the documented version/policy mode and are **not** falsely described as live Windows hands-on if based only on supplied traces. Reviewer decisions cover every published required outcome and the five SEC11 summatives with personal authorship and independently reproducible evidence.
  - **Evidence:** Unfamiliar reviewer brief, pre-observation predictions and alternative explanation, genuine versioned Windows and locally executed Linux observations with independent protected-state checks, actual corrective change or bounded hold, safe reset/changed-path regression and coverage signal, owner report, source attribution and individual live/recorded/written technical defense.

### Graduation evidence and professional scope

Every evaluation records the applicable `SEC11-O#` and `SEC11-AS#`, owner authorization, executable source/policy revision, actual target OS/edition/build/permissions, independently specified expected outcome, genuine executed or authentic supplied evidence and reviewer decision. Authentic Windows excerpts require named endpoint OS and collection/sensor/policy mode provenance; a generated exercise transcript must not be presented as a captured Windows event, and a Linux simulation is not an execution result from Windows. Missing evidence for actual local OS-enforced permission, genuine endpoint events, corrective control or independent individual defense prevents satisfactory completion, even if the written benchmark coverage looks comprehensive.

The required competency is **practical owned Linux endpoint enforcement and cross-platform security-policy/evidence judgment**. A learner with a genuine authorized Windows endpoint may demonstrate additional Windows-specific implementation; without that work, graduation does not certify hands-on Windows administration, domain controller security, managed endpoint platform deployment, commercial EDR operations, enterprise malware/forensics specialist work or full regulatory conformance. A defensible \`hold\` or safe restriction is acceptable only with the independently demonstrated local security/assurance evidence required above. The course remains `draft` pending qualified reviewer and observed learner outcomes under [Status Labels](../../spec/status-labels.md).

### Optional disciplinary references

- [CIS Critical Security Controls v8.1](https://www.cisecurity.org/controls/cis-controls-list) — particularly enterprise inventory, secure configuration, access, audit-log management, malware defenses, data recovery and control verification. A control label is not proof of compliance or protection.
- [NIST SP 800-123 — Guide to General Server Security](https://csrc.nist.gov/pubs/sp/800/123/final) — foundational server-platform configuration and operations, qualified by current OS-specific vendor guidance.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/final) and [SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) — configuration, access, audit and verification concepts, not a mandatory enterprise compliance checklist.
- [Microsoft — App Control for Business](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol) and [App Control audit-mode validation](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/deployment/audit-appcontrol-policies) — distinguish verified would-block observations from enforced execution denial.
- [Microsoft — Sysmon event reference](https://learn.microsoft.com/en-us/windows/security/operating-system-security/sysmon/sysmon-events), [Windows Security Event 4688](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688) and [4624](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624) — genuine process/logon/event semantics and source limitations; policy and collection controls affect interpretation.
- [Microsoft — Windows credential and device protections](https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/how-it-works) — supported edition/version, virtualization and verified effective status determine assurance.
- [Linux kernel — capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html), [systemd sandboxing and resource execution](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html) — Linux controls require safe, allowed host execution and do not automatically transfer to Windows.
- [NIST SP 800-61 Rev. 3, final April 2025](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — response and recovery decision principles; SEC11 applies them only to endpoint control assurance, not a repeat of SEC7 forensic/SOC specialization.

These are public technical reference paths for validating concrete mechanisms; required exit competencies are the course outcomes and published summative criteria above.
