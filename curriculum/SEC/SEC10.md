# SEC10 — Enterprise Identity & Access Security

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC4](SEC4.md)
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** approximately 10–14 focused hours/week (provisional; 140–252 hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**Enterprise identity security is the engineering of who becomes an identity, how they authenticate, what authority that identity receives, how it changes, and how access is actually withdrawn across cooperating systems.** SEC10 prepares a security engineer to reason independently about and test a bounded workforce identity environment. Learners establish a principal and relying-party trust model; investigate authentication and recovery; verify OAuth and OpenID Connect federation; evaluate provisioning and group/privilege changes; distinguish directory/SAML/Kerberos semantics; enforce constrained privileged access; test session, token and entitlement revocation; and defend an unfamiliar identity trust change with actual allowed/denied evidence.

**A valid login, signed token or successful SSO redirect is not proof that the correct user can access only the intended resource.** Identity proofing, authenticator assurance, federation, delegated authorization, application entitlement, privileged access, device conditions and session state are separate enforcement decisions. Wrong issuer, audience or tenant, code-injection/mix-up conditions, group name collisions, stale entitlements, recovery bypass, orphaned service accounts and cached sessions can preserve unauthorized authority even after an identity provider reports a user disabled. A secure implementation must predict what changes in each enforcement layer and independently observe protected resource state.

**Preparation and ownership.** [SEC2](SEC2.md) provides HTTP/browser/session semantics, source-inspectable services, real server-side actor/action/resource authorization and independent negative tests. [SEC4](SEC4.md) provides POSIX service and host trust, network reachability, authenticated transport and honest enforcement-point evidence. SEC4 already requires SEC2, so SEC10 lists SEC4 as its only direct prerequisite. Their SEF preparation supplies programming, tests, local services and safe file/process inspection. SEC10 adds **enterprise authentication, federation, identity lifecycle and privileged access assurance**, rather than reteaching cookie flags, simple web-app login handlers or generic TLS. [SEC6](SEC6.md) owns provider-specific **cloud/workload and CI federation**, image/runtime/supply-chain trust and its authentic hosted-evidence boundaries; SEC10 owns **human/workforce identity, relying parties, account/group lifecycle and enterprise privilege**. [SEC7](SEC7.md) owns full incident response; this course records and evaluates identity decisions only as bounded control evidence. [SEC11](SEC11.md) owns endpoint and platform defense, including Windows device policy assessment and real Linux host control assurance; reviewing Windows/AD traces in SEC10 does not establish hands-on Windows administration.

**Reference environment and truthful availability.** Use a provided or learner-owned **versioned local identity lab** with a free standards-conformant identity provider or authentic signed test-issuer fixtures, two small source-inspectable relying-party/resource services, two or more synthetic users, a local identity/entitlement registry, administrative and nonadministrative roles, controlled provisioning/deactivation events, a bounded approval authority and protected test records. A pre-provisioned free local OpenID Connect provider with maintained client/token-verification libraries is preferred for the federated-login work. Where provider startup is unavailable, an **authentic, labeled signed-assertion/test-issuer fixture and a locally executed relying-party verifier** may establish signature and claims validation, but cannot establish that a networked login/redirect occurred; do not misrepresent offline token validation as a completed live SSO flow. At least one required assessment must exercise an actual local authorized request and its denied counterpart against a running resource service with independent state checks, and at least one must execute a real user/group change and revocation policy. A typed, bounded identity registry suffices; a commercial identity provider, enterprise directory license, billable tenant, physical authenticator, TPM, domain controller, administrator privilege or public DNS is not required.

**Technical boundaries and limitations.** A simulated SCIM-like lifecycle is a *declared subset*, not proof of conformance with [RFC 7643](https://www.rfc-editor.org/rfc/rfc7643) and [RFC 7644](https://www.rfc-editor.org/rfc/rfc7644). An opaque locally signed claim, self-written JWT parser, unverified signature or fabricated IdP log is not genuine federation evidence. Use maintained cryptographic, OIDC and SAML verification libraries or independently provenance-labeled verifier results. Authentic SAML, LDAP, Kerberos or Active Directory traces may be supplied for protocols and directory controls that cannot be safely deployed, with original target, versions, principal, trust path, expected/observed decisions and collection limits identified. These traces do **not** count as locally configuring, operating or defending a Windows domain. Identity assurance levels are context-dependent; do not equate one factor count, the word "passkey", a JWT or an IdP badge with certified IAL/AAL/FAL conformance.

**Ethics and safety.** All accounts, groups, clients, keys, assertions, recovery material and protected data must be synthetic and owned. Never enumerate organizational directories, test real SSO tenants without permission, capture another person's tokens, disable shared accounts, perform credential stuffing, collect biometric data, access a third-party domain, reuse a production client secret or upload an authentic bearer token in a public submission. Use bounded, non-destructive local negative cases, safe clock fixtures and redacted log evidence. Record exact source revisions, test identities, authorization policy and stop/reset controls. Real administrative actions require controlled synthetic state and explicit scope. Identity material that is valid beyond the lab must be redacted and handled with appropriate access restrictions.

**Learning and evaluation.** One evolving local identity system supports four distinct summative evaluations: federation and authenticator trust; lifecycle and entitlement changes; privileged enterprise identity and directory evidence; and unfamiliar-case security engineering defense. The same user/role fixture may recur, but each assessment tests a different claim with independent oracles. Optional lesson investigations are formative, not a quota of required micro-labs. The provisional **14–18 weeks at 10–14 focused hours/week** accounts for actual identity service observation, protocol and session validation, lifecycle/privilege changes, independent negative tests, authentic protocol-trace analysis and a reviewer challenge. It is not calibrated by learner studies. Status remains `draft`.

## Learning outcomes

- **SEC10-O1:** Define an authorized enterprise identity assessment and reconstruct independently observed subject/identifier, identity-provider, authenticator, relying-party, resource-server, directory, policy and trust boundaries, distinguishing identity proofing, authentication, federation and resource authorization.
- **SEC10-O2:** Evaluate authenticator enrollment, multifactor and phishing-resistant methods, account recovery, authenticator replacement and session establishment against a stated threat and assurance context, detecting weaker recovery and fallback paths without demanding a physical authenticator or claiming certification.
- **SEC10-O3:** Trace and test an OAuth authorization-code exchange with PKCE and applicable browser-client protections, including state, redirect/client binding and mix-up/code-injection conditions, without treating an authorization grant as end-user authentication or granting broad access from a bearer token alone.
- **SEC10-O4:** Validate a genuine OpenID Connect assertion and relying-party session using maintained tooling and issuer, audience/authorized-party, subject, signature/key selection, nonce, time and context requirements; distinguish ID tokens, access tokens, service authorization and incorrect trust in decoded but unverified claims.
- **SEC10-O5:** Explain and evaluate actual SAML assertion/SSO, directory and Kerberos/Active Directory trust decisions from protocol specifications and authentic labeled evidence, identifying replay, audience, subject mapping, delegation, ticket/service-principal or privileged-group risks without falsely claiming live enterprise administration.
- **SEC10-O6:** Reconstruct and test joiner/mover/leaver identity lifecycles, group membership, account linkage and SCIM-style create/update/deactivate behavior with an authoritative source, asynchronous propagation, duplicate identity and changed-ownership cases, distinguishing provisioning from revoking existing resource authority.
- **SEC10-O7:** Derive enforceable least-privilege RBAC/ABAC and delegated-authorization policies for named actor/action/resource/context tuples, inspect group inheritance and separation of duties, and independently test explicit permitted, denied, conflicting and changed-role decisions at a real local resource enforcement point.
- **SEC10-O8:** Evaluate and test session, refresh/access token, cached entitlement and relying-party account revocation boundaries, including expiration, propagation delays, risk-sensitive reauthorization and emergency disablement, distinguishing a provider-side status change from proven resource denial.
- **SEC10-O9:** Design and independently assess scoped privileged access, emergency/break-glass authority, administrator separation, service accounts, temporary elevation, reviewer/approver identity, expiration and revocation, with effective actual local allowed/denied state and truthful platform-specific trace interpretation.
- **SEC10-O10:** Evaluate enterprise identity and device/risk-context trust, policy decision versus enforcement points, conditional access and federation/organization boundaries using a named, limited authorization model, without treating a network location or unverified device claim as a universal security proof.
- **SEC10-O11:** Construct privacy-safe authentication, federation, provisioning and privilege-change evidence with correlation identifiers, original event times and audit coverage, checking unauthorized identity actions and false alarms without falsely claiming comprehensive incident detection.
- **SEC10-O12:** Compare independently evidenced controls and trade-offs for federation, MFA/recovery, provisioning, access recertification, privileged actions and revoke/rollback, and deliver a repeatable identity-security review that distinguishes genuine local observations, authentic supplied enterprise traces and assumptions.
- **SEC10-O13:** Independently predict, investigate, correct and defend an unfamiliar bounded issuer, session, group, privilege, recovery or identity-lifecycle change while preserving justified legitimate access and documenting residual risk, privacy and individual authorship.

## Modules

### Module 1 — Enterprise Identity Trust, Authentication and Assurance

#### Outcomes

- SEC10-O1
- SEC10-O2
- SEC10-O10
- SEC10-O11

#### Lessons

1. **Identity is not an authorization decision** — Inspect a provided two-user, two-relying-party local identity/resource fixture. Identify authoritative identity records, credentials, IdP, relying parties, access tokens and the local resource's own permission check. Map an allowed and forbidden operation with exact actor, tenant, resource and trusted decision. Show how passing a login can coexist with incorrect group/resource access.
2. **Proofing, authentication and federation assurance** — Contrast the purposes and limitations of identity proofing (IAL), authentication (AAL), and federation assertions (FAL) under NIST SP 800-63 Revision 4. Determine the risk being controlled, the verifier/IdP responsibility and the evidence that would justify an assurance claim. Do not assign a universal AAL/FAL merely by counting factors or observing a signed token.
3. **Authenticators and phishing-resistant design** — Compare passwords, one-time codes, push approval and WebAuthn/passkeys with the actual origin/RP binding and possession/user-verification conditions. Inspect genuine supplied ceremony/browser output or an available test authenticator, and reason about phishing, stolen sessions, fallback and device binding. Use source-backed evidence; no physical security key is mandatory.
4. **Recovery can downgrade a strong login** — Model enrollment, authenticator loss, replacement, helpdesk escalation and account recovery using synthetic users and a controlled role. Show a normal recovery, an unauthorized takeover attempt and an administrative override path under a documented independent approval rule. Explain exactly which policy is enforced in local code versus described only in provider guidance.
5. **Identity context and privacy-safe observability** — Define subject identifiers, stable vs mutable email/usernames, issuer namespace, event identifiers, audit actor/target/time and protected recovery data. Inspect two sample sign-in or entitlement decisions, including a missing record or wrong-context input; redact unnecessary personal or token material and qualify claims when logs originate from the same compromised application.

*Optional formative feedback:* Given a phishing-resistant login followed by email-only recovery, explain what protects the original ceremony and what weaker account-takeover path remains.

### Module 2 — OAuth and OpenID Connect Relying-Party Security

#### Outcomes

- SEC10-O1
- SEC10-O3
- SEC10-O4
- SEC10-O7
- SEC10-O8
- SEC10-O11

#### Lessons

1. **Authentication, authorization grant and resource access** — Trace a named local client's request to an authorization server and a protected resource: which component knows the user, which grants a client scope, which authenticates a relying-party session and which evaluates a resource/action. Contrast OAuth access authorization and OIDC identity assertion without treating the presence of an access token as proof of the correct human user.
2. **Code exchange with PKCE and browser defenses** — Inspect a genuine local or supplied authorization-code with PKCE flow, registered redirect URI, client binding, state and exact callback parameters. Where a browser client is used, apply the final [RFC 10017](https://www.rfc-editor.org/rfc/rfc10017.html) assumptions and [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html) current security practice. Test benign callback, wrong state, wrong client/redirect and mismatched verifier; identify any mechanism that the locally accessible IdP, browser or test stub did not actually enforce.
3. **Issuer and discovery are trust decisions** — Inspect trusted configuration, issuer identifier, client registration and JWK discovery/key rotation. Independently set the expected issuer and approved algorithms/key policy. Reject an untrusted issuer, key/substitution, inappropriate algorithm, wrong audience/client or ambiguous authorization-server response without inferring trust from a matching email claim or a convenient unverified `kid`.
4. **ID token and session validation** — Use a maintained verifier to validate authentic signed test identity material for signature, exact issuer/audience, `azp` where applicable, subject, expiration/clock skew and nonce in the applicable flow. Establish a local session only from validated identity context and defend subject-to-account mapping. Compare a rejected signed-but-wrong-audience token to a genuine permitted one; never create a custom JWT signature parser for required security evidence.
5. **Resource server and scopes are separate gates** — Inspect whether the locally running resource verifies the correct access token type/issuer/intended audience/scope and the *current actor/resource entitlement*. Demonstrate a validly issued token with insufficient resource authority, a revoked or moved user's request and a permitted current user; response content and protected state must both be checked.
6. **Callback replays, browser containment and regressions** — Evaluate state/nonce lifetime, authorization code replay, session fixation or mix-up across at least two local relying parties and a changed redirect/client condition. Re-run a real allowed identity and resource flow plus denied injection/replay and failure-path outcomes, and explain which client/IdP behavior was observed versus derived from the standard.

*Optional investigation:* Explain why an ID token valid for one client is not a reusable API access token, and how a resource server should refuse it even if the signature is mathematically valid.

### Module 3 — Identity Lifecycle, Entitlement and Revocation

#### Outcomes

- SEC10-O1
- SEC10-O6
- SEC10-O7
- SEC10-O8
- SEC10-O10
- SEC10-O11

#### Lessons

1. **Authoritative source and joiner identity** — Identify the system of record, unique stable identity, HR-like fictional event, IdP account, two relying-party accounts, role/grant mapping and audit state. Execute one owned local create and provision event, distinguish provisioning an account from granting specific resource authorization and reject unintended duplicate-email/identity-collision linkage.
2. **Mover, group and entitlement propagation** — Execute a synthetic department/group change on a user with initial legitimate access. Compare claims embedded in an existing token, live group state, cached entitlement and local resource authorization. Demonstrate the before/after permitted and prohibited operations independently; show that changing a group at the IdP alone may not invalidate an accepted session.
3. **Deprovisioning is a distributed control** — Perform a real local disable/leaver event and propagate it to two relying parties and a resource rule, with a deliberately delayed or unavailable consumer. Predict whether active sessions, refresh tokens, previously minted access tokens and resource caches remain usable; implement/verify a bounded revocation strategy and document the lag or fail-safe choice. A successful deactivation API response is not automatically proof of immediate cross-service denial.
4. **SCIM semantics and asynchronous reconciliation** — Read the actual provisioning contract, stable resource IDs, group membership and partial update semantics in [RFC 7643](https://www.rfc-editor.org/rfc/rfc7643) and [RFC 7644](https://www.rfc-editor.org/rfc/rfc7644). Exercise a declared local SCIM subset or verified reference fixture with missing, duplicate, reordered and retry events, including an independently observed conflict. Label incomplete standards support rather than claiming formal SCIM interoperability.
5. **RBAC, ABAC and delegated identity** — Derive a principal/action/object/context matrix across a normal user, contractor, reviewer, service account and administrator. Demonstrate a real local resource allow, explicit deny, changed-role denial and conflicting-group resolution using a documented policy semantics; scope delegation to the intended actor and purpose rather than assuming role membership is sufficient.
6. **Session, token and account recovery after change** — Test session/refresh rotation, risk-based step-up or forced reauthentication after a role move or account recovery in an owned fixture. Contrast locally enforced introspection/session lookup with still-valid offline tokens and token-revocation requests; specify actual revocation and cache propagation guarantees under the named implementation.

*Optional formative feedback:* A departing contractor is disabled in the IdP but can still read an object through a long-lived relying-party session. Identify the missing resource enforcement and produce a safe reproducible repair test.

### Module 4 — Enterprise Federation, Directory Trust and Privileged Access

#### Outcomes

- SEC10-O1
- SEC10-O2
- SEC10-O5
- SEC10-O7
- SEC10-O9
- SEC10-O10
- SEC10-O11
- SEC10-O12

#### Lessons

1. **SAML identity federation and signed assertion conditions** — Trace an IdP, service provider, binding, authentication request, signed response/assertion, subject/NameID, audience, destination, `InResponseTo`, validity window and replay conditions from an official OASIS example and genuine labeled verifier evidence. Compare valid, replayed and wrong-audience assertions; distinguish a trusted signed XML subtree from an unsigned substituted field and avoid implementing XML signature processing for production.
2. **Directory, Kerberos and enterprise trust boundaries** — Interpret authentic labeled directory/KDC/Windows-domain traces: account/group and service-principal identity, domain/forest trust, ticket-granting vs service ticket, ticket lifetime, delegation and authentication audit events. Reconstruct the claimed authority path and one mistaken service/SPN/delegation or privileged-group condition. These investigations do **not** count as actually operating Active Directory, administering a domain controller or exploiting Windows credentials.
3. **Administrative separation and delegated privilege** — Model privileged roles, approving authority, privilege escalation through group membership, admin identity used for normal browsing, break-glass access and time-bounded elevation. Execute a safe local privileged-action control with two distinct approvers/actors, exact requested resource/action, expiration, changed membership and explicit denial. Identify and reject a subject who can approve their own otherwise forbidden elevation where the declared policy requires separation of duties.
4. **Service accounts, machine identity and standing privileges** — Inventory local service accounts, owned keys or short-lived credentials, workload operator boundaries, insecure shared admin identities and orphaned accounts. Compare legitimate machine identity rotation and delegated privilege with cloud-specific CI federation owned by SEC6. Verify one bounded local service credential/permission change and its effect on an actual resource operation.
5. **Conditional identity and zero-trust reasoning** — Inspect a named conditional-access rule with principal, action, requested resource, device/risk signal and audit/evaluation point. Predict an authorized and unauthorized request when a device claim is stale/unverified, group changes or network location shifts. A locally modeled device posture is not a verified managed endpoint; do not claim system-wide device trust from an IdP field.

*Optional investigation:* Distinguish a Windows domain administrator added to a privileged group from a normal user with access to a single application resource, and explain which authority and evidence must be revoked independently.

### Module 5 — Integrated Identity Assurance and Independent Defense

#### Outcomes

- SEC10-O1
- SEC10-O3
- SEC10-O4
- SEC10-O5
- SEC10-O6
- SEC10-O7
- SEC10-O8
- SEC10-O9
- SEC10-O10
- SEC10-O11
- SEC10-O12
- SEC10-O13

#### Lessons

1. **Identity assurance from source to protected state** — Consolidate the local provider, two clients, provisioning events, privilege rule and resource records into an actor/issuer/subject/action/revocation map. Define independent expected results for normal sign-in, wrong issuer/client, account move, expired approval, stale session and resource-denied operations. Mark actual local enforcement versus authentic supplied SAML/AD conditions.
2. **Repair the first false authority assumption** — Locate a plausible root cause in verified OIDC identity mapping, session trust, provisioning identity collision, local resource entitlement or privileged role approval. Patch the specific source/configuration/policy that makes the wrong authorization decision. Demonstrate actual protected state and safe rollback, not merely a successful login or an attractive identity architecture diagram.
3. **Unfamiliar identity trust change** — Receive a reviewer-chosen bounded new condition, such as issuer/key rotation, identity rename, client misbinding, unexpected SCIM retry, stale group claim, concurrent deactivation or privileged-approval replay. Before execution, predict allowed and forbidden behavior and a competing explanation. Run a discriminating local negative test and reason precisely from genuine target-labeled external protocol evidence where live infrastructure is unavailable.
4. **Security decision and reproducible technical defense** — Present a concise owner- and implementer-facing access-control/recovery recommendation, identity lifecycle risks, exact source revisions, executed and supplied evidence, false-accept/false-deny trade-offs, unresolved provider limits and an individual live, recorded or written source-backed defense. Explain why a signed token, compliant-looking SAML field or federation configuration alone is not proof of the actual resource decision.

*Optional formative feedback:* A user with a revoked admin role still operates an application through an old refresh token. Require a fix that closes the observed gap without denying another user's legitimate recovery.

## Completion requirements

**Four required summative assessments** establish the SEC10 outcomes. One small, freely accessible identity fixture can support the distinct security properties; instructors must not demand a paid SSO product, live corporate domain, production user data, physical passkey or advanced APP product. Optional investigations and lesson checkpoints are not graduation conditions. Every summative declares the actor, issuer/client/provider, protected resource, authenticator/credential claim, expected permission, actual local action/state, source and clock versions, and whether any protocol evidence was supplied rather than executed.

- **SEC10-AS1** — Authentication and Federated Relying-Party Security
  - **Outcomes:** SEC10-O1, SEC10-O2, SEC10-O3, SEC10-O4, SEC10-O7, SEC10-O8, SEC10-O11.
  - **Work:** Assess a running local relying-party/resource application with a preconfigured free IdP or authentic signed test-provider assertions and maintained verifiers. First trace an authorized user, client, identity assertion, relying-party session and protected resource path. For a locally accessible IdP, execute a genuine authorization-code/PKCE login and a legitimate permitted API operation; test wrong state/nonce, client/redirect/issuer/audience, invalid signature/key or expired token according to the applicable actual flow, plus an insufficient-scope/role protected-resource operation. If only signed authentic fixtures are available, execute local verifier and resource gates but **do not claim to have performed a live OAuth redirect/token exchange**. Compare phishing-resistant authentication versus fallback/recovery from a qualified authentic browser/provider trace or accessible local test method. Patch one real locally tested session/claims/authorization defect and rerun independently specified normal and denied cases.
  - **Criteria:** The assessor can distinguish identity proof, authenticator assurance, OIDC authentication, OAuth delegated authorization and resource authorization. The exact issuer/client/RP and signed assertion provenance are trustworthy and recorded; decoded but unverified claims do not pass. Invalid context and insufficient current resource permission cannot commit protected state even after legitimate authentication. Tests exercise a real locally running resource and a maintained identity verifier, with genuinely executed federation distinguished from supplied token/flow traces. The repaired control maintains normal login and permitted resource behavior while rejecting the relevant changed identity, replay or invalid case. No custom cryptographic JWT algorithm or vendor assertion is substituted for genuine verification evidence.
  - **Evidence:** Authorized local fixture/IdP and client versions, provider/assertion trust configuration, request/redirect or authentic fixed flow records, real verifier outputs, independently expected actor/client/issuer/audience/resource matrix, local permitted and forbidden state, patched code/configuration, redacted recovery/authenticator evidence and residual limitations.

- **SEC10-AS2** — Identity Lifecycle, Provisioning and Revocation Assurance
  - **Outcomes:** SEC10-O1, SEC10-O6, SEC10-O7, SEC10-O8, SEC10-O10, SEC10-O11, SEC10-O12.
  - **Work:** Define a fictional authoritative identity registry and execute real local joiner, mover, leaver and group/role-change operations against two source-inspectable relying parties/resource contexts. Use a documented bounded SCIM-like provider interface or genuine test SCIM implementation, distinguishing its supported subset. Verify a legitimate new user's grant, changed department/role/resource ownership and disabled identity while checking pre-existing session, cached entitlement, refresh/access token and provisioning retry semantics. Deliberately introduce a safe stale-grant, duplicate link or delayed consumer defect, repair the **actual** enforcing service/policy, and compare independent authorized, unauthorized, out-of-order and failure-case state. Produce privacy-safe account/privilege audit evidence without an actual external identity provider or customer record.
  - **Criteria:** The current authoritative principal and resource permission are independently derived, not inferred from a successful provisioning API response. Real local state shows the intended account creation/role change, the forbidden cross-tenant/stale grant denied after the specified policy-effective time, and the legitimate state preserved. The learner explicitly distinguishes locally enforced revocation from tokens that can remain valid until expiry and provider-side claims not polled by a resource. Duplicate identity, asynchronous propagation and meaningful failure paths are evaluated, and any SCIM conformance claim is limited to tested behaviors. Privacy protections exclude real account data or bearer credentials.
  - **Evidence:** Versioned two-client identity/resource and role matrix, actual provisioning event/source records, declared protocol semantics, before/after IdP/resource/cache and protected-state traces, negative stale/duplicate/changed-role tests, minimal code/policy patch, replay/expiry expectations and evaluator-supplied unknown-condition handling.

- **SEC10-AS3** — Privileged Enterprise Identity and Directory Trust Review
  - **Outcomes:** SEC10-O1, SEC10-O2, SEC10-O5, SEC10-O7, SEC10-O9, SEC10-O10, SEC10-O11, SEC10-O12.
  - **Work:** Assess a synthetic workforce identity/control-plane scenario containing normal and privileged users, groups, a delegated service account, time-bounded administrator rights, an approval actor and an emergency account. Inspect genuine target/issuer-labeled SAML assertion results and Kerberos/AD directory, ticket and audit excerpts from a supplied safe enterprise fixture or owned evaluation target; identify subject/group/authority/delegation and relevant audience, replay and time constraints. **Execute a real local privileged-resource policy** with legitimate temporary admin approval, rejected unapproved self-elevation, expired/replayed approval, changed group or orphaned service identity and a safe emergency case. Repair one actually demonstrated local least-authority or approval-binding weakness; compare the limits of local policy tests versus real AD/SAML enforcement and propose scoped monitoring and revocation.
  - **Criteria:** The chosen identity/privilege model correctly separates sign-in, directory group and service-principal identity, real local protected authority and SAML/Kerberos observations. At least one real local high-impact operation is permitted only with authorized, correctly bound, nonexpired approval; changing actor/resource/role invalidates inappropriate grants. The learner can identify the evidence/authority boundaries of a given Windows-domain ticket or directory condition without pretending to have deployed or configured Windows/AD. No live domain controller, real password, LDAP query of third-party users or home-written SAML signature verification is required. Competing explanations, service and break-glass residual risks and false denials are documented.
  - **Evidence:** Privilege and approval matrix, synthetic service/group account inventory, genuine labeled external SAML/Kerberos/AD trace/verifier record with origin and applicability, actual local privileged-resource tests and state, approval/revocation negatives, revised policy or controlled code, redacted audit/rollback and risk-owner review.

- **SEC10-AS4** — Unfamiliar End-to-End Identity Security Assessment and Defense
  - **Outcomes:** SEC10-O1, SEC10-O2, SEC10-O3, SEC10-O4, SEC10-O5, SEC10-O6, SEC10-O7, SEC10-O8, SEC10-O9, SEC10-O10, SEC10-O11, SEC10-O12, SEC10-O13.
  - **Work:** Receive an independent reviewer-selected unknown but bounded condition in the same permitted identity system: an issuer/key rollover, unexpected group-to-tenant mapping, session still accepted after deactivation, new IdP client/redirect, changed recovery fallback, SAML subject collision, approval replay, directory delegation or missing audit event. Before decisive inspection, predict a valid and prohibited resource result and a competing explanation. Use real local relying-party, lifecycle, authorization or privileged-state checks plus genuine supplied platform-specific traces when needed; patch the earliest unsafe trust decision, or justify an enforced hold when a real correction is not permitted. Rerun independent permitted, prohibited, invalid/failure and changed-context regressions, including a check that detects a safely reintroduced weakness. Deliver a prioritized identity security review and an individually defensible source-backed explanation of which controls, authenticating parties and residual tokens remain trusted.
  - **Criteria:** The trainee distinguishes authentic signed/federated identity from a valid **resource permission**, preserves source and user context, and corrects a real local trust boundary with independently observed effects rather than a dashboard, role diagram or blanket denial. The changed condition and alternative hypothesis are evaluated against actual and accurately labeled supplied evidence, including false acceptance and legitimate-user denial. Prior SEC2/SEC4 outcomes are used but not substituted for SEC10 federation/lifecycle/privileged assurance. A safe failure/hold is appropriately scoped, and the owner can reproduce relevant checks without a paid provider or real user credentials. Authorship, uncertainty and non-observed enterprise mechanisms are disclosed under technical questioning.
  - **Evidence:** Reviewer-selected scenario and pre-observation predictions, original/current actor/issuer/client/resource diagram, real executed control and protected-state traces, authenticated labeled enterprise/SSO evidence where relevant, source/policy correction, independent before/after regression and mutation result, redacted incident/rollback notes, owner-facing prioritization and individual written/recorded/live technical defense.

### Evaluation evidence and readiness

Every summative decision identifies `SEC10-AS#`, the applicable `SEC10-O#` outcomes, actual versioned source/IdP/provider/service environment, authorized actor and resource, independently specified allow/deny oracle, observed local enforcement and qualified supplied or modeled evidence. Test fixtures may be pre-provisioned but must permit independent inspection, reset, runnable permission checks and a real code/configuration/control correction. **Local resource authority cannot be proven solely by the identity provider's claim**. A SAML/Windows/Kerberos trace is an evidence source for its declared protocol/host conditions, not a substitute for an actual client, resource or account-state result in the owned test environment.

No paid Microsoft/Google/Okta service, production realm, sensitive identity proofing, administrator-level directory configuration, custom JWT/SAML cryptography, general endpoint hardening or full incident response is required. Successful completion does **not** constitute IAM vendor certification, NIST IAL/AAL/FAL certification, comprehensive enterprise directory administration, Windows security engineer qualification or a guarantee that a deployed organization's identities cannot be compromised. Course status remains `draft` pending [Status Labels](../../spec/status-labels.md) and independent learner-calibrated evaluation.

### Optional disciplinary references

- [NIST SP 800-63-4, final July 2025](https://csrc.nist.gov/pubs/sp/800/63/4/final) — digital identity guidance; [SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) for authentication and [SP 800-63C-4](https://csrc.nist.gov/pubs/sp/800/63/c/4/final) for federation.
- [OAuth 2.0 Security Best Current Practice, RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html) — PKCE, code-injection/mix-up protection, token leakage and sender constraints, applied to a named client type.
- [OAuth 2.0 for Browser-Based Applications, RFC 10017, August 2026](https://www.rfc-editor.org/rfc/rfc10017.html) — current browser-based application security and token-mediation considerations.
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) — authentication flow, issuer, subject and ID-token validation; an ID token is not a generalized API permission.
- [Web Authentication Level 3, W3C Recommendation, August 2026](https://www.w3.org/TR/webauthn-3/) — origin-bound public-key authentication and real relying-party validation expectations.
- [SCIM Core Schema, RFC 7643](https://www.rfc-editor.org/rfc/rfc7643) and [SCIM Protocol, RFC 7644](https://www.rfc-editor.org/rfc/rfc7644) — controlled user/group provisioning, partial updates and identity lifecycle.
- [OAuth 2.0 Token Revocation, RFC 7009](https://www.rfc-editor.org/rfc/rfc7009.html) and [Token Introspection, RFC 7662](https://www.rfc-editor.org/rfc/rfc7662.html) — distinguish revocation at an authorization server from resource-side effective access.
- [OASIS SAML 2.0 Technical Overview](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) — SAML assertions, relying parties, conditions and bindings.
- [Kerberos V5, RFC 4120](https://www.rfc-editor.org/rfc/rfc4120.html) and [Microsoft Active Directory security guidance](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory) — domain service/credential/privilege trust, qualified by actual target.
- [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) — subject/resource conditional authorization, policy decision and enforcement distinction.

Public primary references support the taught mechanisms; the required assessable competencies and evidence are explicitly specified above.
