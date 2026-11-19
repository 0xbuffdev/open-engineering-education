# SEC4 — Network & Infrastructure Security

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC2](SEC2.md)
**Duration:** 10–14 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–13 focused hours/week (provisional; 100–182 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**A secure service environment must admit intended communication while denying unintended reachability, authority and information disclosure—and must preserve those properties when configuration or dependencies change.** SEC4 develops the ability to inspect an actual small networked service environment, reconstruct its exposure and administrative boundaries, derive explicit ingress/egress and host-permission policies, implement proportionate controls, independently verify permitted and forbidden flows, validate authenticated transport, and defend repairs when the topology or configuration changes. A firewall configuration, an encrypted connection or a green service-health check alone is not sufficient evidence.

**Context and applications.** A deployed service has multiple security-relevant surfaces: listening sockets and address families, host and proxy interfaces, administrative channels, inter-service communication, outbound destinations, filesystem and process privileges, identity material, configuration, update paths and observable failures. An exposed debugging port, unexpected IPv6 listener, broad outbound permission, untrusted forwarded header or stale secret can compromise a system even when its application request handlers are correct. Network filtering and service isolation reduce reachable paths but do not replace authentication, object authorization or a trust decision at the resource. Effective infrastructure security requires explicit policies, real enforcement and evidence about where each boundary holds.

**Preparation and ownership.** [SEC2](SEC2.md) supplies adversarial web-service investigation, server-side authority and security-regression methods. [SEF7](../SEF/SEF7.md) teaches POSIX sockets, loopback TCP, descriptors, processes, file identity, signal handling and failure-aware local service interfaces; SEC2 inherits SEF10 through SEC1, and SEF10's verified entry requirements already include SEF7. SEC4 uses these abilities to assess the **operational security posture** of service processes, their exposure, network policy, configuration and transport trust. It does not reteach C socket programming or require [SYS4](../SYS/SYS4.md) event-loop/Rust multi-client implementation. [APP7](../APP/APP7.md) teaches application deployment, local HTTPS, release and recovery; SEC4 instead conducts adversarial assurance of a given environment, so APP7 is not a direct prerequisite. [SEC5](SEC5.md) owns cryptographic primitives, key-exchange details and protocol correctness: SEC4 owns **operational TLS endpoint and client-trust configuration**, not cipher implementation. SEC6 owns cloud IAM, container isolation and CI/supply-chain controls; SEC7 owns detection and incident investigations. Do not quietly introduce an elective or additional program as a graduation condition.

**Reference environment and honest constraints.** A nonprivileged Linux user account, an owned loopback listener and its client, a small reverse proxy or supplied proxy fixture, a local directory with synthetic configuration and credentials, an optional disposable local database/service and free inspection tools suffice. Use a versioned, reproducible topology containing a public-facing *role* represented on loopback, a protected internal service, and an administrative endpoint. A separate local client/process or namespace may emulate external/internal actors, but **loopback addresses by themselves do not create independent network security zones**. Actual L3/L4 packet-filter experiments may use an authorized disposable VM, user-enabled network namespace, or authentic supplied policy/packet traces; no root access, real firewall modification or virtual networking feature is mandatory. An executable unprivileged proxy can demonstrate its **own** allow/deny policy, not prove system-wide firewalling or isolation of a service still directly reachable. State precisely which layer each observation validates. Pre-provisioned free local tools are acceptable. Required work needs no public domain, cloud subscription, commercial scanner, Kubernetes, administrator privileges, production host or account.

**Safe work and evidence.** Restrict all active listening, probes and failed-connection experiments to explicitly authorized learner-owned loopback endpoints or deliberately isolated disposable environments. Never scan external ranges, modify a shared host firewall, collect unrelated packet data or test third-party services. Keep configuration changes inside the owned process/user/VM, record before/after state, and prepare a safe rollback so management access cannot be accidentally lost. Use synthetic identities and test secrets; do not install unreviewed certificate roots into the system trust store. Every security claim identifies an actual enforcement point, its configured decision, a positive and negative test, and any untested route, address family or failure behavior. Redacted traces, text policy matrices and supplied authentic host observations are valid evidence when they support the specific claim; a drawing or simulated result must not be represented as measured network isolation.

**Instruction and workload.** Five coherent stages develop exposure investigation, segmentation policy, host/service privileges, transport and proxy trust, then independent review under drift. Four summative evaluations can reuse one evolving local environment, snapshots, test fixtures and technical report. Supplemental module investigations are optional formative work. The provisional 10–14 weeks at 10–13 focused hours/week covers service inspection, policy design, safe configuration and reset, dual-direction denial tests, client-verified TLS, failure-mode diagnosis and an unfamiliar challenge. Actual completion is determined by demonstrated evidence, not time, number of lessons or scanning-tool output.

## Learning outcomes

- **SEC4-O1:** Define an authorized infrastructure security review, reconstruct an evidence-backed service/host topology and inventory its actors, assets, listeners, trust zones, dependencies, administrator paths and outbound destinations, separating observed exposure from assumptions.
- **SEC4-O2:** Investigate service reachability across bind addresses, ports, IPv4/IPv6, interfaces, proxies and local socket paths; distinguish an advertised service, an actual listener, a permitted connection and authenticated/authorized application access.
- **SEC4-O3:** Derive a justified least-reachability ingress/egress and management-plane policy from legitimate flows and threat boundaries, specifying enforcement points, precedence, defaults, exceptions, state and the conditions under which a path may be opened.
- **SEC4-O4:** Implement or evaluate appropriate network/service-level access restrictions and independently test allowed, denied, cross-zone and failure-path traffic; identify bypasses, direct-backend paths and the limits of proxy-based versus L3/L4 isolation evidence.
- **SEC4-O5:** Inspect and harden service process and host-resource authority through dedicated identities, filesystem and socket permissions, bound interfaces, unnecessary services, executable/writable paths and meaningful privilege reduction without assuming unavailable administrator powers.
- **SEC4-O6:** Establish a reviewable security configuration and update baseline covering daemon options, sensitive local settings, supported version/patch posture, test credentials, administrative access and recovery, with changes prioritized by actual exposure and operational risk.
- **SEC4-O7:** Configure or independently assess authenticated service transport and client trust through local TLS certificate/hostname validation, endpoint identity, supported protocol policy and negative trust cases, distinguishing a deliberately trusted local test CA from a publicly trusted service.
- **SEC4-O8:** Examine termination, upstream trust, redirect and proxy-header boundaries, ensuring client-supplied forwarding metadata cannot grant authority and direct-backend access cannot silently bypass the intended policy; qualify which transport legs are actually protected.
- **SEC4-O9:** Produce privacy-preserving security visibility for exposure, configuration, accepted/rejected traffic and relevant service failures; distinguish logger observations, packet-filter evidence and missing logs without claiming comprehensive detection or incident response.
- **SEC4-O10:** Evaluate configuration drift, rule precedence, dependency failures and changed topologies using independently derived positive/negative checks, safe change ordering and rollback, and distinguish a verified local control from an unsupported production-wide security claim.
- **SEC4-O11:** Deliver a reproducible, prioritized infrastructure security assessment and independently defend or revise its recommendations when an unfamiliar bounded service, policy or trust assumption changes.

## Modules

### Module 1 — Service Exposure and Actual Trust Boundaries

#### Outcomes

- SEC4-O1
- SEC4-O2
- SEC4-O9

#### Lessons

1. **What an infrastructure security review can assert** — Establish a scoped owner, authorized hosts/processes, client identities, test destinations, synthetic credentials and stop rules. Contrast the application-level vulnerability boundary from SEC2 with service exposure and OS/network configuration authority. Identify unobserved assumptions instead of inferring compromise or safety from a port number.
2. **Listeners, address families and interface binding** — Distinguish a process binding to loopback, wildcard, a named interface, a Unix-domain socket and different IPv4/IPv6 addresses. Inspect a real owned listener and reconcile its process, socket state, configured address and actual allowed client connection. Explain why an IPv4-only inspection may miss an IPv6 binding and why loopback testing cannot prove public Internet reachability.
3. **Proxies, service chains and bypass routes** — Trace a client through a fronting proxy to an application, optional data service and administrative endpoint. Identify a direct-to-backend route, unintended management listener or unexpected egress dependency; show why a proxy restriction does not help if the protected process remains independently reachable.
4. **Service and administration inventory** — Reconstruct intended clients, data/management interfaces, ports, file/socket permission paths, principals and outbound dependencies. Separate known connections, expected flows, system-observed listeners and documented but unobserved interfaces. Mark owner and business purpose for each exception, rather than listing all open ports as automatically exploitable.
5. **Active observation versus passive claims** — Use declared, narrowly scoped local connection attempts and service/client logs to compare listener state, connection refusal, application rejection and timeouts. Explain what a successful TCP handshake does **not** say about authority and why no packet log entry does not prove a path was blocked.

*Optional formative feedback:* Critique a supplied inventory that documents only the main HTTP listener and ignores a local administrative socket, an IPv6 entry and a background egress path.

### Module 2 — Segmentation, Policy Enforcement and Reachability

#### Outcomes

- SEC4-O2
- SEC4-O3
- SEC4-O4
- SEC4-O10

#### Lessons

1. **Legitimate traffic and trust-zone matrix** — Build an explicit actor/service/operation/direction policy for frontdoor, internal state, management and outbound dependencies. Distinguish the business need for one connection from a blanket right to any address/port, and explain why network location is not a substitute for authenticated resource authorization.
2. **Ingress, egress and management-plane choices** — Compare a host firewall, network ACL, proxy policy, interface binding, Unix socket permissions and an application route check. Place each actual enforcement point on the topology and distinguish transport reachability from request authorization. Select a deny-by-default, permit-by-exception rule for a named mechanism where appropriate, then account for necessary maintenance and recovery.
3. **Rule order, state and return traffic** — Evaluate a supplied concrete packet/rule trace with direction, family, source/destination, protocol, priority and statefulness. Predict first-match/priority behavior only when the named rule engine defines it; distinguish a stateful established response from a new unauthorized connection and review asymmetric return-path assumptions.
4. **Direct paths and dual-stack gaps** — Reconcile the intended access matrix with controlled attempts to bypass a proxy, contact the backend directly or reach an unexpectedly bound IPv6 listener. A proxy's 403, a local listener's refusal and an actual packet-filter drop are different observations; explain where each was enforced.
5. **An unprivileged policy experiment** — Use a controlled local gateway or connection broker to enforce a route/destination allowlist with real success/failure, and an authentic supplied or authorized VM packet-filter trace for L3/L4 cases. State explicitly that gateway denials cannot certify that its backend is unreachable by another route. Predict and test a deliberately broadened rule or failed gateway case without modifying shared networks.
6. **Policy changes without losing access** — Sequence a safer rule or listener change using a known-good administrative recovery path, independently specified acceptance/denial checks and rollback criteria. Explain how a missing dependency, incorrect default or stale connection can lead to either an unintended exposure or avoidable outage.

*Optional investigation:* Evaluate a six-row network policy matrix and identify one overbroad egress exception, one unprotected management route and one evidence gap without constructing an actual public network.

### Module 3 — Service Hardening, Local Identity and Configuration Integrity

#### Outcomes

- SEC4-O1
- SEC4-O5
- SEC4-O6
- SEC4-O9

#### Lessons

1. **Service identity and least privilege** — Distinguish login users, runtime service identities, effective permissions and the privileges actually needed to read configuration, bind owned ports, write application state and access logs. Inspect a supplied service account policy or a real unprivileged user-level process and justify what can be removed without breaking required work.
2. **Filesystem, socket and process boundaries** — Test permissions on an owned private directory, Unix socket, configuration and log location; trace read/write/execute and path traversal requirements. Identify sensitive writable executables or overly broad access and choose a narrow control. Record where ownership, mount or capability controls require an unavailable privileged host and use credible supplied observations instead of pretending a local chmod test enforces kernel sandboxing.
3. **Security-relevant daemon configuration** — Inspect listener modes, management/debug features, optional endpoints, directory roots, administrative interfaces, unneeded modules and startup defaults. Correct a local configuration defect and verify both permitted function and an unintended access path. Distinguish stopping an unnecessary listener from simply hiding it behind a friendly route.
4. **Secrets and administrative credential handling** — Use synthetic passwords, tokens and a local client-certificate/key fixture to compare environment inheritance, protected files, command-line arguments, repository artifacts and log exposure. Explain how to restrict access and rotate a compromised test secret, including dependent processes; do not treat an environment variable as a universal secret vault.
5. **Supported versions, updates and rollback** — Create a version/configuration inventory, determine whether a relevant component is supported and identify the evidence required before prioritizing an update. Model an unsafe administrative change, test an approved patch/config revision in the disposable system and specify recovery and continuity limits without assuming a version string alone proves vulnerability.

*Optional formative feedback:* Review a service launch manifest for a wildcard management listener, world-readable test key, writable executable, missing owner and unverified patch statement.

### Module 4 — Authenticated Transport and Proxy Trust

#### Outcomes

- SEC4-O2
- SEC4-O7
- SEC4-O8
- SEC4-O10

#### Lessons

1. **TLS identity as a deployment property** — Trace client-to-service/server-certificate verification, intended hostname, chain, configured trust anchors, endpoint address and protocol negotiation. Reuse APP1/SEC2 transport basics; focus on operational validation rather than designing encryption, handshakes or cryptographic primitives taught in SEC5.
2. **A local verified service connection** — Configure or use a provided loopback TLS service with a synthetic local CA and a client whose trust is deliberately restricted to that CA for this test. Demonstrate a successful matching-hostname connection and denied untrusted-root or mismatched-hostname connections *with verification enabled*. Never globally disable certificate checking, install an unreviewed root into the OS trust store, or call a local trust anchor publicly trusted.
3. **Protocol and secret configuration limits** — Inspect an explicit supported TLS version/configuration policy and client/server evidence, including how a removed/expired local certificate or private-key permission affects service behavior. Distinguish a failed handshake caused by hostname/trust from one caused by incompatible versions. Identify where the library and platform determine supported controls, and avoid claiming to prove an absence of cryptographic vulnerabilities from a successful handshake.
4. **Reverse-proxy identity and forwarding claims** — Trace client-to-proxy and proxy-to-service security as *separate legs*. Evaluate Host and forwarded source/scheme/identity headers, trusted proxy addresses, ingress rewriting and direct-backend reachability. Demonstrate with local fixtures that a caller-supplied forwarding header cannot promote a guest into an administrator or trick downstream security decisions; distinguish a proxy-verified identity from an arbitrary header.
5. **Transport failure and fail-closed behavior** — Use controlled expired/untrusted certificate fixtures, unavailable upstream and invalid forwarded metadata to predict permitted recovery and denied actions. Check that service availability fallbacks do not silently switch to unauthenticated transport, ignore certificate errors or expose privileged backend operations.

*Optional investigation:* Given a local proxy terminating HTTPS and forwarding plain HTTP to a loopback upstream, describe precisely which leg is encrypted and which identity assumptions are not independently authenticated.

### Module 5 — Independent Verification, Change and Security Decision

#### Outcomes

- SEC4-O1
- SEC4-O3
- SEC4-O4
- SEC4-O5
- SEC4-O6
- SEC4-O8
- SEC4-O9
- SEC4-O10
- SEC4-O11

#### Lessons

1. **From inventory to independently verified control** — For one important security path, link asset and attacker precondition to policy owner, actual enforcement point and a testable allowed/denied/failure oracle. Reconcile active connections, listener states, logs, packet-filter metadata and configuration source. Explain why a plan-only rule or diagram is not proof of enforcement.
2. **Logging without disclosure or false assurance** — Configure a bounded local stream of redacted service/proxy acceptance, denial and error events with correlation or equivalent timestamp context. Distinguish what an application logger observes from the firewall's packet decisions; a missing log must not be presented as proof of a drop. Avoid publishing test secret material or unrelated traffic.
3. **Detecting drift and safe remediation** — Compare a baseline against an altered listener, firewall/policy rule, key permission or trusted proxy setting. Predict access effects first, rerun positive/negative checks, identify unintended operational harm and apply or justify a safe rollback. Distinguish measured local behavior from a claimed production-wide security posture.
4. **An unfamiliar environment and defender's argument** — Investigate a supplied unseen topology or change, such as a second listener family, direct backend connection, changed management path or newly trusted proxy. Produce an owner-actionable finding with reproducible traces, risk/impact ranking, trade-offs, remaining gaps and a brief defense that corrects a mistaken hypothesis if counterevidence appears.

*Optional formative feedback:* Reject or qualify a report claiming comprehensive network isolation from a single local proxy rejection and one green TLS client test.

## Completion requirements

**Four required summative evaluations** establish the SEC4 outcomes. A single evolving, versioned owned service topology and its safe test harness can support all four; the assessments have distinct substantive criteria. Optional module investigations, tooling demonstrations and informal checkpoints are not completion conditions. Each assessment records the actual enforcement layer and clearly differentiates executed checks, supplied authentic traces, theoretical policy reasoning and unobserved claims.

- **SEC4-AS1** — Exposure, Segmentation and Path Verification
  - **Outcomes:** SEC4-O1, SEC4-O2, SEC4-O3, SEC4-O4, SEC4-O10.
  - **Work:** Declare scope and reconstruct a small service topology including a frontdoor process, directly reachable or deliberately protected backend, management endpoint and one outbound dependency. Inventory active listeners, IPv4/IPv6 assumptions, permitted clients, direct/backend routes and actual enforcement points. Derive a source/destination/direction/operation policy matrix, implement an appropriate owned unprivileged listener/gateway restriction, and test authorized and denied flows against it. For host/network firewall semantics not locally accessible, analyze a named authentic packet-filter configuration/trace and clearly label these as supplied evidence rather than claiming local host enforcement. Include a broadened rule or changed listener and a safe rollback decision.
  - **Criteria:** The inventory distinguishes configuration from observed process/socket facts, origin reachability from authenticated application permission, and the real layer that accepted/rejected each attempted connection. The policy denies concrete unnecessary paths while preserving each justified legitimate flow, with IPv4/IPv6 and management coverage or explicitly bounded gaps. Tests expose a proxy bypass if the backend is independently reachable; a gateway denial is not mislabeled an L3/L4 drop. Rule precedence, statefulness and failure behavior are correct for the specified engine. A controlled change prompts a meaningful negative regression and an access-preserving recovery plan.
  - **Evidence:** Authorized setup and target manifest, topology and actor/path matrix, inventory/observed listener traces, versioned policy/configuration, independent expected allowed/denied outcomes, redacted executed local client results, labeled genuine packet-policy trace where used, change/rollback result and limitations.

- **SEC4-AS2** — Host/Service Privilege and Configuration Hardening
  - **Outcomes:** SEC4-O1, SEC4-O5, SEC4-O6, SEC4-O9, SEC4-O10.
  - **Work:** Audit a disposable local service process and its startup/configuration files, private data, administrative features, file/socket permissions and synthetic credentials. Establish a justified minimal service-privilege and supported-version policy, repair at least two materially distinct issues such as world-readable credentials, unneeded listener, excessive data-write permission or exposed administrative feature, and verify behavior with separate allowed and denied user/process cases. Demonstrate a controlled failure or revoked-access state, capture redacted events, and provide a safe change/rollback plan. If an OS privilege mechanism cannot be exercised without administrator rights, analyze an authentic supplied configuration/trace and identify the untested portion.
  - **Criteria:** Each chosen fix names the authority removed, actual previously reachable operation and the legitimate functions that still work. File permissions and process identities are evaluated at actual access points; merely documenting least privilege or storing synthetic secrets in environment variables is insufficient. Config and version claims are traceable to specified software, and update conclusions state exposure and support uncertainty. Tests reproduce intended denial and safe failure under named permissions; logging preserves useful evidence without publishing secrets. Privileged/unavailable controls are not represented as locally tested.
  - **Evidence:** Scoped environment, process/config/permission inventory, before/after source and settings, independent access matrix, executed allow/deny and failure checks, redacted event excerpts, patch/rollback rationale, source revision and disclosed OS privilege limits.

- **SEC4-AS3** — Authenticated Transport and Proxy-Trust Assurance
  - **Outcomes:** SEC4-O2, SEC4-O7, SEC4-O8, SEC4-O10.
  - **Work:** Use a supplied or built loopback TLS endpoint with a deliberately configured *local test* CA and a validating client, plus a simple fronting proxy/upstream fixture. Predict and check successful verified connection, wrong-hostname or untrusted-CA rejection, invalid/expired identity where supported, and an unavailable upstream. Trace which transport leg has TLS and how a proxy constructs/validates forwarded metadata. Demonstrate a safe negative case proving caller-supplied forwarding data cannot elevate authority, and verify that direct backend access is either appropriately denied or explicitly classified as a remaining gap.
  - **Criteria:** An allowed connection succeeds only with actually enabled chain and hostname verification; invalid trust cases fail without disabling validation or installing a global root. The learner identifies the certificate's intended name, local trust scope, protocol evidence and unprotected/unknown legs. Forwarded identity/scheme/source data are not treated as inherently trusted when supplied by a client. Changes preserve legitimate requests while preventing the demonstrated bypass; server fallback does not silently ignore TLS failures. No claim of public CA trust or cryptographic proof is made from local handshake success.
  - **Evidence:** Local endpoint/client/proxy fixture and named TLS tool versions, controlled test CA and SAN expectations without exposing private key, pretest connection matrix, redacted verified/rejected outcomes, proxy/header trust findings, before/after policy/config diff and bounded transport-assurance statement.

- **SEC4-AS4** — Unfamiliar Configuration Drift and Infrastructure Defense
  - **Outcomes:** SEC4-O1, SEC4-O3, SEC4-O4, SEC4-O5, SEC4-O6, SEC4-O8, SEC4-O9, SEC4-O10, SEC4-O11.
  - **Work:** Receive a previously unseen bounded service-topology or configuration change, such as an IPv6 listener, new direct-backend route, revoked service identity, misordered deny/allow rule, exposed admin path or incorrectly trusted proxy. Before observation, predict affected legitimate and prohibited paths and one competing failure hypothesis. Investigate inside the controlled environment or authentic supplied trace, implement or specify a minimal valid and appropriately tested correction, and rerun independent allow/deny/failure checks with a rollback or continuity plan. Present a concise operator and risk-owner recommendation and individually defend its assumptions.
  - **Criteria:** The learner identifies the actual changed enforcement/privilege point, distinguishes observed reachability, application denial, simulated policy and missing telemetry, and reconciles a contradictory test rather than repeating a static hardening checklist. The correction closes the evidenced unwanted path without unnecessarily disabling legitimate operations, and the independently prepared negative check would detect regression. Ownership, management recovery, redacted evidence, scope limits and risks of untested network layers are explicit. The technical defense demonstrates transfer and an ability to correct an initial wrong diagnosis.
  - **Evidence:** New approved scenario and assumptions, pre-observation predictions, affected asset/flow policy, genuine local/supplied traces with provenance, revised configuration or justified no-change response, independent regression/rollback checks, concise operator/risk-owner finding and reviewable written, recorded or live individual defense.

### Evaluation evidence and readiness

Every evaluation identifies the SEC4 revision, assessment ID, outcome IDs, actual inspected artifact, independent expected behavior, measured or explicitly modeled result and review decision. Where a control operates in the kernel, an isolated network or a separate host that cannot be tested locally, use authentic target-specific fixtures with clear provenance **instead of claiming a software simulation proves packet isolation**. Actual local controls and changed configurations require a clean reproduction path, synthetic accounts, documented tool/runtime versions and deterministic cleanup. Neither scanning a port nor reading a settings file demonstrates that an operational security property holds. No real third-party data, private keys, production traffic or unreviewed certificate roots may be published.

The course remains `draft` pending the educational readiness criteria in [Status Labels](../../spec/status-labels.md). Its completion establishes bounded infrastructure security engineering competence; it does not certify a production deployment, blanket zero-trust compliance, absolute host isolation or universal network protection.

### Optional disciplinary references

- [NIST SP 800-41 Rev. 1](https://csrc.nist.gov/pubs/sp/800/41/r1/final) — firewall policy, placement and testing principles, adapted to current packet-filter implementations.
- [NIST SP 800-123](https://csrc.nist.gov/pubs/sp/800/123/final) — server configuration, administration and maintenance security baseline.
- [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) — network locality is not automatically authority; policy enforcement and resource access remain distinct.
- [CISA Zero Trust Maturity Model v2.0](https://www.cisa.gov/sites/default/files/2023-04/zero_trust_maturity_model_v2_508.pdf) — network segmentation, identity and operational maturity as context, not an accreditation claim.
- [NSA Zero Trust Implementation Guideline, Phase One (January 2026)](https://media.defense.gov/2026/Jan/30/2003868308/-1/-1/0/CTR_ZIG_PHASE_ONE.PDF) — deny-by-default network policy and authenticated management guidance.
- [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446.html) — TLS 1.3 protocol definitions; SEC4 assesses deployed trust and enforcement rather than implementing the protocol.
- [Mozilla TLSRef Server Side TLS](https://mozilla.github.io/server-side-tls/) — tool/version-specific secure TLS configuration recommendations.
- [Linux ip(7)](https://man7.org/linux/man-pages/man7/ip.7.html) — declared address-family and socket-binding semantics for the reference Linux environment.

These freely accessible references support verification and independent study; they do not impose a proprietary tool, paid platform or new course prerequisite.
