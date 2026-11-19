# SEC2 — Web & Application Security

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** [SEC1](SEC1.md), [APP1](../APP/APP1.md)
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; approximately 120–224 focused hours)

> [Security Engineering](README.md) · [Design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**Web and application security is the engineering of enforceable trust boundaries in the presence of adversarial input and changing state.** In SEC2, learners investigate real application mechanisms, formulate falsifiable security hypotheses, reproduce bounded failures in authorized environments, repair their causes, and independently test the resulting behavior. Successful investigation requires more than a scanner finding or a passing happy-path test: it requires a causal account of why the boundary failed, an evidence-backed remediation, negative and failure-path regression, and honest limits on what the tests establish.

**Context and applications.** Browsers, HTTP clients, web services, databases, file stores and third-party integrations cross different authority and interpretation boundaries. An identity assertion becomes dangerous when accepted as authorization; untrusted data becomes dangerous when reinterpreted as code, a query, HTML or a destination; and a server-initiated request can reach resources a client cannot. Session misuse, broken object/field authorization, SQL injection, cross-site scripting, cross-site request forgery, server-side request forgery and API data exposure are concrete failures of those mechanisms, not a checklist that can certify security. The same investigative reasoning transfers to user dashboards, SaaS applications, APIs and multi-tenant systems.

**Prerequisites and course ownership.** [SEC1](SEC1.md) supplies authorized investigation, threat modeling, risk decisions and independently specified security-test oracles. [APP1](../APP/APP1.md) supplies actual HTTP, URL, cookie, origin, browser, CORS and TLS semantics. Their [SEF10](../SEF/SEF10.md) preparation supplies programming, Git, debugging, tests, C/Unix basics and reproducible local tools. SEC2 teaches the **security-specific** backend reading and modification needed for assessment through an inspectable provided running service: trace request routing and decoding, a session principal, the server-side actor/action/resource decision, persistence/transaction or synthetic state, response serialization and relevant browser behavior before attempting a repair. Learners must actually inspect and change the exposed source/configuration, reproduce a material failure and verify authoritative post-request state. [APP3](../APP/APP3.md) develops construction and operation of a complete typed backend with a framework and relational database; SEC2 does **not** require that separate implementation course, a particular language/framework, or [APP2](../APP/APP2.md) UI engineering. Its deeper exit capability remains independent adversarial assurance: reproduce and repair session, access, interpreter, cross-site, outbound/file and API failures; test alternative and changed-state paths; and defend observed security effects. [SEC4](SEC4.md) owns host/network controls, [SEC5](SEC5.md) cryptographic protocols, [SEC6](SEC6.md) cloud/supply-chain controls and [SEC7](SEC7.md) incident evidence.

**Accessible reference environment and preparation.** Start from a **provided or learner-owned working, version-pinned and source-inspectable local HTTP service** with reproducible setup, synthetic accounts, seed/reset state, runnable tests and explicit route/session/data-flow examples. It must expose a real request handler, a server-held session or authenticated principal, an authorization decision, persistently checkable protected state (such as an actual local SQLite database or a transparent deterministic store), response rendering, and separately bounded outbound/file actions. At least two actors with distinct roles or tenants, legitimate mutations and intentionally vulnerable paths must be available. The opening lessons teach how to follow one functional request from browser/client through handler, identity, authorization, storage and response, inspect the code and run an independent expected-state check **before** the adversarial investigation; the learner must be able to make and explain an actual minimal correction. A free Python/SQLite or similarly small service is suitable; an existing Node/TypeScript or APP3 implementation may also be reused but is **not compulsory**. The learner is not required to build a complete backend, relational schema or frontend product before taking this security course. Real browser-only claims require a free real browser or a clearly identified behavior model with stated limitations; an HTTP-only mock cannot establish browser enforcement. No paid portal, proxy license, public domain, cloud subscription, production access, privileged packet capture or proprietary evaluator is necessary.

**Safety and independent study.** All active security tests occur only against owned loopback services or fully specified training fixtures within documented scope, with stop conditions and clean resets. Neither a public hostname nor source-code availability grants authorization for testing. SSRF and file exercises use entirely local allow/deny targets and disposable data, never real cloud-metadata endpoints or private third-party networks. No real credential theft, destructive payloads, external scanning, malicious uploads or sustained denial-of-service traffic is required. Present diagrams with equivalent labeled text/traces and redact sensitive results.

**Workload and completion.** The 12–16-week allocation at 10–14 focused hours/week is provisional; it includes code/trace analysis, environment setup, multiple controlled failures, meaningful patches, browser verification, independent negative tests, review and an unfamiliar case. Five summative assessments cover distinct security mechanisms; they may reuse one evolving versioned application and test harness. Optional lesson investigations are not completion gates. Actual mastery depends on demonstrated outcomes rather than lesson or week counts.

## Learning outcomes

- **SEC2-O1:** Bound and justify an authorized application security assessment, reconstruct concrete actor, route, identity, data, parser, browser and server-initiated trust boundaries, and formulate reproducible, risk-led failure hypotheses.
- **SEC2-O2:** Investigate session and authentication lifecycle failures, including session binding, regeneration, expiration, logout, revocation, identity changes and credential disclosure, distinguishing browser behavior from server enforcement.
- **SEC2-O3:** Discover, explain and remediate authorization flaws at object, action, property and tenant boundaries across alternate routes and role changes, with evidence that rejected operations preserve authoritative state and response confidentiality.
- **SEC2-O4:** Investigate cross-request security invariants under stale permission caches, ownership changes, retries, concurrent operations and asynchronous effects; identify effective enforcement and distinguish demonstrated failures from hypothetical races.
- **SEC2-O5:** Trace untrusted data through decoding, normalization and interpreter boundaries, reproduce bounded query/command/template-style injection behavior in controlled fixtures, and enforce interpreter-appropriate structural separation with independent tests.
- **SEC2-O6:** Analyze untrusted HTML, attributes, URLs, JavaScript and DOM-rendering contexts, distinguish safe encoding, DOM APIs, sanitization and defense in depth, and verify repairs against multiple harmless encoded/input variants.
- **SEC2-O7:** Evaluate browser origin/site, cookie and credential behaviors, CSRF preconditions, CORS policy and response visibility, and demonstrate that server-side cross-site defenses preserve legitimate actions while denying prohibited effects.
- **SEC2-O8:** Investigate SSRF and file/upload/download trust boundaries, including destinations, redirects, canonicalization, traversal, file identity and content handling, and implement verifiable local-only containment controls.
- **SEC2-O9:** Detect and correct API property overexposure, mass assignment, broken object/property authorization and unsafe serialization using actor/field matrices and independently derived response/state expectations.
- **SEC2-O10:** Test bounded application resource controls and failure behavior for body size, pagination, request rates, concurrency and dependency errors, with safe diagnostics and appropriately limited availability claims.
- **SEC2-O11:** Implement proportionate security fixes and reproducible regression suites using independent positive, denied, invalid, altered-state and failure-path oracles, and demonstrate sensitivity to a reintroduced weakness.
- **SEC2-O12:** Explain and prioritize developer-actionable security findings with redacted causal evidence, remediation decisions, residual risk and uncertainty; independently defend or correct a diagnosis for an unfamiliar in-scope variant.

## Modules

### Module 1 — Security Investigation and Evidence

#### Outcomes

- SEC2-O1
- SEC2-O11
- SEC2-O12

#### Lessons

1. **Read a functioning service before attacking it** — Starting from the provided running, source-inspectable HTTP fixture, follow one permitted request through route matching, decoding, session/principal, server authorization, persistent state and response. Verify its expected outcome using a separate client/state observation, then change the actor, input, order or route. Distinguish a successful functional operation from a tested security guarantee and identify which source statement actually enforces it.
2. **Authorized targets and controlled fixtures** — Declare system owner, allowed ports, permitted accounts, methods, synthetic data, reset steps, exclusions and stop conditions. Compare deliberate vulnerable training code with a public website and reject testing for which no permission exists.
3. **Independent security oracles** — Derive expected allowed responses, denied responses, unchanged persistent state and absence of sensitive output *before* testing the application. Contrast an HTTP 403 status with a forbidden write that still commits; an output observed from the implementation cannot be its own specification.
4. **Causal evidence and uncertainty** — Collect redacted request/response, relevant server-side branch and database state, then distinguish missing authentication, inadequate object authorization and unsafe serialization. Explain why one proxy log, 200 response or scanner warning does not establish the root cause.

*Optional formative feedback:* Challenge a report that calls an endpoint secure based solely on two passing unit tests and an unexamined framework middleware rule.

### Module 2 — Sessions and Authorization Under State Changes

#### Outcomes

- SEC2-O2
- SEC2-O3
- SEC2-O4

#### Lessons

1. **Authentication proof and session authority** — Trace genuine credential validation through server-issued session state. Analyze regeneration on authentication or elevation, session binding, expiration and logout, and demonstrate with local disposable identities how a stale session could be misinterpreted as current authority.
2. **Cookie storage and lifecycle boundaries** — Distinguish Secure, HttpOnly, SameSite, Domain and Path, including each attribute's limitations. Compare stored client state with server revocation, and test whether a prior session still authorizes access after a changed identity.
3. **Object, action and tenant checks** — Create an actor-resource-action matrix and test an owned object, another user's object, another tenant and an alternate route. Explain why a hidden UI feature, opaque ID or CORS policy cannot enforce server authorization.
4. **Property mutation and workflow authority** — Challenge role/ownership/status fields, admin-only operations, bulk updates and multi-step approvals. Contrast request-shape validation with the set of properties an actor may change, and inspect persisted state and emitted side effects after denial.
5. **Stale decisions, retries and concurrent writes** — Change ownership or revoke a privilege between two processing steps; inspect stale caches, asynchronous jobs and repeated requests. Use a specified controlled schedule before claiming a race, locate the atomic decision boundary and retest with a separate route or execution order.

*Optional investigation:* Trace a permission revocation across an authenticated browser, a background worker and two simultaneous updates using supplied event timings.

### Module 3 — Interpreter and Rendering Boundaries

#### Outcomes

- SEC2-O5
- SEC2-O6
- SEC2-O11

#### Lessons

1. **Untrusted values and changing grammar** — Track bytes through parsing, decoding, canonicalization, validation and a query/template/command interpreter. Compare values, identifiers and structure; use a harmless local marker to observe a bad boundary without executing external commands.
2. **SQL structure versus parameter values** — Analyze a deliberately flawed local query over synthetic records, independently predict the wrong result, and repair with parameter binding. Where column names or ordering are dynamic, use a constrained identifier mapping. Verify invalid and alternate inputs, not a single memorized string.
3. **HTML, attribute, script and URL contexts** — Trace one user-supplied value into distinct output locations. Explain why HTML text encoding does not automatically secure an event-handler, URL or script context, and choose a suitable safe rendering API or context-specific protection.
4. **DOM sinks and secondary interpretation** — Compare text insertion and HTML-parsing sinks, later re-rendering, dangerous URL schemes and trusted-content assumptions. Evaluate vetted sanitizers, CSP and Trusted Types as distinct defenses with browser and policy limits; do not treat TypeScript as runtime validation.
5. **Alternate encodings and regression sensitivity** — Recheck repaired sinks/queries using harmless Unicode, encoded separators, malformed values and a second render or route. Show how an independently expected result would expose a regressed boundary, while recording interpreter contexts not investigated.

*Optional formative feedback:* Explain why a safely parameterized SQL value and a safely inserted DOM text node require different mechanisms even though both handle untrusted strings.

### Module 4 — Cross-Site Browser and Credential Boundaries

#### Outcomes

- SEC2-O2
- SEC2-O6
- SEC2-O7

#### Lessons

1. **Origins, sites and browser access** — Derive origin from scheme, host and port; distinguish origin from schemeful site and browser response-reading restrictions from request sending. Predict whether CORS allows script access without assuming it prevents a server-side state change.
2. **CSRF conditions and session transport** — Investigate cookie-bearing cross-site requests against a state-changing local endpoint, distinguishing bearer-token use, SameSite behavior, preflight and browser navigation. Identify the trusted server-side property a successful CSRF attempt would violate.
3. **Defending state-changing operations** — Compare synchronizer tokens, Origin/Referer validation, Fetch Metadata, content-type rules and SameSite settings under their real deployment assumptions. Test legitimate state change, missing/invalid token, hostile-origin request and actual protected state after denial.
4. **Credentialed CORS and observable enforcement** — Analyze Access-Control-Allow-Origin/Credentials, wildcard limits, preflight and unsafe origin reflection. Use a real local browser, or a clearly specified modeled browser with limitations, to distinguish request transmitted, credential sent, response readable and action authorized.

*Optional formative feedback:* Diagnose a case where a cross-origin script cannot read the response but a state-changing request has already succeeded.

### Module 5 — Server-Initiated Requests and Files

#### Outcomes

- SEC2-O1
- SEC2-O8
- SEC2-O11

#### Lessons

1. **Outbound requests and server authority** — Follow an untrusted URL through parsing, allowed schemes and destinations, name resolution, request initiation and redirects. Explain why naive string prefixes, a first DNS result or an initial redirect check do not necessarily enforce the final destination boundary.
2. **SSRF verification without third-party targets** — Construct an owned local allowed responder and an owned forbidden fixture. Test invalid schemes, ports and redirects under controlled local semantics, checking that rejected inputs cause no forbidden request. No real metadata, public IP or private network probing is required.
3. **File paths, identities and traversal** — Trace user filenames, normalization, relative path segments and symbolic links into filesystem access. Explain why string-prefix checks can fail and why a check/use race requires care. Compare a legitimate read with a denied traversal against disposable local files.
4. **Uploads, retrieval and safe storage** — Examine claimed MIME type, extension, file signature, size, canonical server-controlled storage identity, access control and response headers. Test unauthorized read/download, oversized or mismatched content and cleanup, without introducing real malware or public file services.

*Optional investigation:* Explain one redirect or symlink counterexample to a weak containment policy using a fully local fixture.

### Module 6 — API Data Boundaries and Resource Abuse

#### Outcomes

- SEC2-O3
- SEC2-O4
- SEC2-O9
- SEC2-O10

#### Lessons

1. **Object- and property-level response exposure** — Derive permitted response fields for actor, role and tenant. Detect a list endpoint or serializer that leaks protected fields despite denying a write, then enforce an explicit public output contract and independent negative tests.
2. **Mass assignment and process transitions** — Investigate untrusted object updates, admin-only flags, approval order and alternate API routes. Compare validation of a payload's *shape* with authorization to mutate each property or perform a function.
3. **Bounded service workloads** — Design safe local tests for body limits, page bounds, request quotas, concurrency, deadlines and dependency timeouts. Distinguish accepted work from safely rejected work and avoid extrapolating a local limit to universal DDoS resistance.
4. **Errors, sensitive logs and recovery** — Detect information disclosure in exceptions, serialized errors, debug output, caches and request logs. Repair to preserve useful correlation while redacting secrets/PII, and verify dependency failure is non-authorizing and accurately observable.

*Optional feedback:* Review a synthetic API where 403 responses are correct but a log or list endpoint still reveals another tenant's data.

### Module 7 — Remediation, Regression and Independent Diagnosis

#### Outcomes

- SEC2-O1
- SEC2-O4
- SEC2-O11
- SEC2-O12

#### Lessons

1. **Fixing the violated invariant** — Identify the earliest failed authority or interpretation boundary, compare the smallest defensible fix with a symptom-level patch, and analyze side effects for legitimate behavior and related routes. Reject unnecessary full rewrites that obscure causal evidence.
2. **Independent negative regression** — Organize allowed, denied, malformed, revoked, changed-state, alternate-path and dependency-failure checks. Prepare expected results independently, reproduce the original fault before patching, and safely weaken a corrected control to demonstrate the suite would detect regression.
3. **Unfamiliar challenge and security report** — Predict the effect of an unseen actor, endpoint, origin, rendering context or service rule before executing a bounded test. Defend a causal finding or justify a no-change result, then document evidence, uncertainty, owner action and a testable remediation without replicating every earlier exercise.

*Optional formative feedback:* Critique a universal "secure" claim based on a single fixed payload and two successful scans, identifying substantive missing assurances.

## Completion requirements

**Five required summative evaluations** establish the SEC2 outcomes. They can reuse a coherent versioned, fully source-inspectable working HTTP training service, real local state and its test harness; constructing a full APP3 backend or frontend product is not a hidden completion requirement. The learner must execute actual controlled requests, inspect the relevant handler, identity and state code, make real security corrections, and reproduce independently expected legitimate, denied and failure-state behavior. Each assessment criterion must nevertheless be independently reviewed. Lesson checks and investigations are optional unless their work is explicitly included below. All active tests must remain inside owned loopback or supplied synthetic environments.

- **SEC2-AS1** — Authentication, Session and Authorization Investigation
  - **Outcomes:** SEC2-O1, SEC2-O2, SEC2-O3, SEC2-O4.
  - **Work:** Assess a disposable, source-inspectable running local service with at least two principals and genuinely checkable protected state. Trace one actual request through its handler, session principal, authorization condition, persistent data operation and output before testing; reproduce one session lifecycle failure and two materially distinct authorization failures involving action, object, field, tenant, role or alternate route. Include a revoked/expired session, a changed-permission or ownership condition and a second route or independently specified request sequence. Establish expected allowed/denied behavior before observation, repair root causes and test protected state before and after.
  - **Criteria:** Permission and target scope are verifiable; actual source and locally executed state checks establish the relevant handler, principal, authorization and persistence decisions, independently of the service's response status. The causal explanations distinguish authentication, session binding, authorization and state transitions. A denied action neither alters protected data nor leaks restricted response fields. The patch enforces the authoritative boundary across tested routes rather than merely hiding UI controls. The tests catch a reintroduced fault, and concurrent claims are limited to the schedule actually controlled. Required positive behavior remains available.
  - **Evidence:** Scope, source revision and environment declaration, executed handler/principal/state trace, actor/object/action matrix, independently expected responses and actual protected state, redacted pre-fix and post-fix observations, code diff, clean reset/run instructions, negative cases and uncertainty notes.

- **SEC2-AS2** — Query and Rendering Security Repair
  - **Outcomes:** SEC2-O5, SEC2-O6, SEC2-O11.
  - **Work:** Investigate a local query-construction weakness and a distinct browser rendering/DOM-context weakness using synthetic data and harmless markers. Identify the exact boundary where untrusted data becomes query or display structure. Correct query parameter handling and restricted dynamic structure, plus safe context-aware rendering. Retest at least two relevant output contexts and an alternate malformed or encoded input using independent expected results.
  - **Criteria:** The original behaviors and their root causes are demonstrated, not inferred from a scanner label. User values cannot alter query structure; unauthorized records stay unchanged. Browser-controlled content remains in intended safe locations under tested contexts; the learner distinguishes encoding, safe DOM APIs, sanitization and CSP and identifies their limits. Tests would detect a meaningful reintroduced weakness, not just the original marker string.
  - **Evidence:** Local source/fixture, pre- and post-fix request/query and browser traces, independently expected results, precise code/config repair, boundary/invalid tests, and remaining interpreter-context limitations.

- **SEC2-AS3** — Browser Credential and Cross-Site Control Verification
  - **Outcomes:** SEC2-O2, SEC2-O6, SEC2-O7, SEC2-O11.
  - **Work:** Evaluate a local cookie-authenticated state-changing workflow from a legitimate and a second origin/site. Predict cookie sending, script response visibility and committed state before testing. Demonstrate a bounded CSRF or credentialed-CORS failure in the controlled environment, implement an appropriate server-side control with complementary browser settings, and rerun legitimate, denied and invalid-token cases.
  - **Criteria:** Expected and actual credential, origin/site, CORS and server authorization behavior are accurately separated. Allowed requests work and disallowed cross-site requests do not mutate protected state. The explanation does not treat HttpOnly, SameSite, CSP or CORS as a universal replacement for server-side checks; real browser observations or explicit model limitations are provided. A proposed regression test exposes the original failed security property.
  - **Evidence:** Explicit synthetic origin/cookie/identity fixtures, expected state matrix, browser or labeled model traces, source changes, allowed/denied state comparisons, and compatibility/coverage limitations.

- **SEC2-AS4** — Server/API Data, File and Resource Boundary Review
  - **Outcomes:** SEC2-O1, SEC2-O8, SEC2-O9, SEC2-O10, SEC2-O11.
  - **Work:** Investigate an outbound URL policy and an unsafe local file or upload path, plus one API data/property exposure or resource limit failure in the same owned system or coherent fixture suite. Exercise controlled redirects, invalid destinations, traversal/symlink or unsafe filename cases, multi-actor field access, oversized input or dependency failure. Remediate controls at actual consumption boundaries and test both legitimate and prohibited behavior. Never contact external metadata services or deploy harmful files.
  - **Criteria:** The before state shows an actual unsafe path within the declared fixture; the after state blocks it at a verifiable boundary, including redirects and file identity where applicable. Protected data is neither disclosed nor mutated across denied API operations, resource limits have safe observable effects, and diagnostics do not reveal sensitive data. Extrapolations about network isolation or DDoS immunity are explicitly excluded. Tests are reproducible and discriminate proper enforcement from cosmetic filtering.
  - **Evidence:** Target/fixture declaration, route/asset map, independent allow/deny results, controlled before/after traces, source/config changes, resettable negative and failure tests, output/permission evidence and residual risk.

- **SEC2-AS5** — Unfamiliar Security Variant and Technical Defense
  - **Outcomes:** SEC2-O1, SEC2-O4, SEC2-O11, SEC2-O12.
  - **Work:** Investigate a previously unseen bounded variation on a studied mechanism, such as a new route, revoked permission during background work, changed browser origin, new render sink or outbound redirect. Predict whether the existing invariant still holds, compare a meaningful counter-hypothesis, test within the approved fixture, and make a minimal justified correction or defend a no-change decision. Produce a developer-actionable security finding, risk disposition and independent defense without duplicating AS1–AS4.
  - **Criteria:** A new causal analysis correctly separates the actor, authority boundary, input interpretation and observed effect. Predictions precede measurements; independently expected allowed and denied outcomes distinguish a repaired control from a weak one. A safe legitimate flow continues to work, the repair addresses the root cause, and the reviewer can challenge the learner's assumptions. The result clearly states scope, impact, uncertainty, residual risk and limitations rather than claiming universal security.
  - **Evidence:** Unseen case and permission, pretest hypothesis and counter-hypothesis, local reproduction/trace, minimal code or decision change, independent regression results, concise technical and owner-facing report, and a reviewable written, recorded or live defense.

### Evidence and course readiness

For each required evaluation, record the course revision, assessment ID, actual outcome IDs, independent expected behavior, executed or explicitly modeled observations, reviewer decision and the material environment assumptions. Code artifacts must rebuild and run from a clean setup with declared free dependencies and synthetic fixtures. A test that passes without a justified oracle, a copied attack transcript and a checklist of OWASP categories cannot establish the required reasoning. Do not expose credentials, private learner records or third-party data.

This course remains `draft` until the relevant educational readiness requirements in [Status Labels](../../spec/status-labels.md) are met. Course completion establishes only the published SEC2 outcomes; it does not certify a product's general safety or authorize security testing elsewhere.

### Optional disciplinary references

- [OWASP Application Security Verification Standard 5.0.0](https://asvs.owasp.org/) — verification criteria for authentication, authorization, data handling and Web security.
- [OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0x00-header/) — object, property, workflow and API resource risk categories.
- [OWASP Web Security Testing Guide](https://wstg.owasp.org/) — structured Web testing methods; use dated/versioned pages when citing a particular requirement.
- [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html) and [Cross Site Scripting Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) — interpreter and rendering defenses.
- [NIST SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/B/4/final) — authentication and session guidance; its assurance-level requirements do not automatically bind every training fixture.

These open resources support research and independent study without paid accounts.
