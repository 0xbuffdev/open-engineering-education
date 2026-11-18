# APP14 — API Gateways & Edge Delivery

**Program:** APP — Application Engineering
**Type:** `course`
**Classification:** `elective`
**Prerequisites:** [APP3](APP3.md) — Backend Framework Engineering, [APP7](APP7.md) — Deployment, Cloud & DevOps
**Duration:** 14–18 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–14 focused hours/week (provisional; validate with independent learners)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

**Design, secure, measure and operate the HTTP delivery boundary around an actual application without transferring business authorization from the origin to an untrusted edge.** This optional specialization is not a requirement of APP9 or core graduation. [APP3](APP3.md) already teaches service identity, tenant authorization and database correctness; [APP7](APP7.md) already teaches basic HTTPS/reverse-proxy deployments. APP14 develops advanced intermediary correctness, shared-cache isolation, admission fairness and recovery, not another introductory API or cloud provisioning course.

Start with one APP3/PostgreSQL backend, an authenticated protected write, public mutable response, immutable asset and **a local gateway plus real shared-cache layer**. Nginx OSS with `proxy_cache` is one free route. Caddy/Envoy or another reverse proxy remains valid **when paired with a documented, observed free shared cache**; don't assume it has native caching merely because it sets Cache-Control headers. Use two synthetic tenants, independently controlled origin requests, verified local TLS, disposable processes and bounded workload. Paid CDN/edge workers, global DNS, multiple regions and managed WAF are *comparison topics*, not prerequisites. Local data never prove globally deployed performance.

Trust is hop-specific: do not accept client-supplied `Forwarded`, `X-Forwarded-For`, role or tenant headers as authenticated facts; re-establish TLS peer identity and maintain server-side authorization. Apply RFC 9111 shared-cache rules with extra conservative protection for personalized content, and observe actual origin mutations before claiming cache freshness or failed-write safety. Rate limits cannot replace authorization and may be unfair when client identities are ambiguous. Read-only stale fallbacks do not prove current state, and proxy health checks do not establish database consistency. Operate only owned or disposable local test systems; do not load-test or attack third-party services.

**Instructional sufficiency:** All 17 outcomes use 13 conceptually distinct modules and seven independent summative assessments. Every new edge protocol, trust or cache mechanism needs a worked HTTP/identity model, a running observed example, a falsifying malicious or failed variant, corrective feedback and real system evidence before independent judgment. Require **an actual free shared-cache implementation** such as Nginx OSS `proxy_cache` or another documented component, not a reverse proxy returning cache headers without real storage. RFC 9111 permits certain Authorization-bearing responses in shared caches under special directives; this course deliberately excludes **all personalized tenant responses** regardless of permissive directives and proves the exclusion with a second account. Fewer lessons do not mean fewer competencies, and `draft` source CI cannot establish learner mastery or production readiness.

## Learning outcomes

- **APP14-O1:** Define a defensible public edge boundary, client journeys, threat model and measurable origin/gateway responsibilities without replacing application-side authorization.
- **APP14-O2:** Design and test canonical routing, request normalization, method and body limits, upstream selection and response semantics under malicious and ambiguous requests.
- **APP14-O3:** Establish verifiable TLS termination, upstream identity, trusted forwarded metadata and origin access boundaries against spoofing and bypass.
- **APP14-O4:** Implement controlled gateway authentication and identity propagation while proving independent origin-side action, object, field and tenant authorization.
- **APP14-O5:** Classify representations and design HTTP cache-control, Vary, validators and public/private cache eligibility according to observed RFC 9111 behavior.
- **APP14-O6:** Prove safe cache-key and invalidation policies across personalized, mutable, localized and versioned content without cross-user disclosure.
- **APP14-O7:** Configure rate, concurrency and body-cost admission controls with explicit identity fairness, refusal semantics and bounded resource consumption.
- **APP14-O8:** Evaluate static assets, compression, streaming, range and HTTP/2/3 paths through intermediaries without damaging correctness or accessibility.
- **APP14-O9:** Measure end-to-end client, gateway, upstream and cache latency and resource use with reproducible workloads, trace correlation and attribution limits.
- **APP14-O10:** Apply explicit timeout, retry, circuit and overload budgets while preventing retry amplification, unsafe write replay and misleading health checks.
- **APP14-O11:** Exercise gateway and origin configuration changes with least-privilege policy, independent negative tests, staged rollout and verified rollback.
- **APP14-O12:** Investigate edge/origin failures, cache leak and poisoning risks, protocol desynchronization and incident recovery using sanitized reproducible evidence.
- **APP14-O13:** Compare CDN, multi-region and edge-compute placement against consistency, jurisdiction, operating cost, vendor lock-in and locally measurable constraints.
- **APP14-O14:** Communicate evidence-backed architecture and business trade-offs, documenting limitations of local emulation versus a real global CDN or paid service.
- **APP14-O15:** Design gateway behavior for route and credential revocation, temporary upstream failure and stale-response constraints without promising stronger semantics than tested.
- **APP14-O16:** Reproduce independent attacker and operator scenarios that expose failures across multiple identity, path, cache, rate and origin boundaries.
- **APP14-O17:** Deliver and independently defend an operational gateway/edge slice under an unfamiliar bounded security, performance, outage or configuration change.

## Modules

### Module 1 — Edge Product, History and Threat Boundaries

#### Outcomes

- APP14-O1
- APP14-O3
- APP14-O9
- APP14-O13
- APP14-O14
- APP14-O17

#### Lessons

1. **Intermediary history and independent authority** — Compare the evolution of reverse proxies, shared caches/CDNs and programmable edge using one real user task; show why none can substitute for origin-side object/tenant authorization.

2. **One authorized mutable task and public representations** — Select an APP3/PostgreSQL protected read/write, a public versioned asset and a mutable public GET; introduce two synthetic tenants and one committed-but-uncertain mutation.

3. **Actual trust and resource flow at every hop** — Trace TLS peer, gateway, **real cache**, origin, database, authenticated account and untrusted forwarded claims; predict what a cache HIT cannot prove about the server.

4. **Threat model with falsifiable negative cases** — Identify path/authority confusion, cache deception and poisoning, direct-origin bypass, forged proxy metadata, post-commit reply loss and resource exhaustion, assigning independent HTTP/SQL oracles.

5. **Pinned free reference and origin-only baseline** — Run local origin/gateway with inspectable releases and trusted HTTPS, measure authorized/denied traffic and local workload, and explicitly exclude global CDN claims.

*Optional practice — architecture review:* Identify a falsely trusted edge header and correct the origin-owned authority model.

### Module 2 — Canonical Routing and HTTP Message Semantics

#### Outcomes

- APP14-O2
- APP14-O3
- APP14-O12
- APP14-O16

#### Lessons

1. **Request-target forms and authority interpretation** — Trace origin-form, absolute-form, CONNECT authority-form and HTTP/2 :authority translation through actual gateway/origin requests, rejecting a mismatched Host.

2. **Path normalization, suffix confusion and private routes** — Vary percent-encoding, dot segments, slashes and file-like suffixes at the gateway and backend, then prove a private resource is never misclassified or shared-cached.

3. **Host, SNI and authority disagreement** — Challenge Host, :authority, TLS name and forwarded scheme in a controlled client; show explicit rejection rather than a wrong virtual host, and explain 421 as applicable.

4. **Method, 4xx/5xx and protected mutation semantics** — Distinguish GET/HEAD, safe/error methods, 404/405/413/429/502/503 and a committed protected POST, with correct refusals and no unexpected replay.

5. **RFC 9112 framing and hop-by-hop removal** — Remove Connection-nominated headers; test conflicting Content-Length/Transfer-Encoding and gateway/origin interpretation on a disposable lab, rejecting ambiguity to prevent hidden request desynchronization.

6. **Finite request and parser resource budgets** — Enforce size, count, header/body read time and upstream allocation limits, observing oversized and slow request handling without backend resource leak.

7. **Routed API, public assets and safe origins** — Route two API paths and public assets while verifying normalized identity, private/admin route denial and real direct-origin SQL authorization independent of edge path rules.

8. **Differential gateway/origin request interpretation** — For safe and malformed locally owned fixtures, compare method/target/body observed at each hop and prove no unintended second request or unauthorized database side effect.

*Optional practice — hostile request probe:* Produce raw valid and invalid requests and compare observed gateway and origin interpretation.

### Module 3 — TLS, Forwarding Identity and Origin Isolation

#### Outcomes

- APP14-O3
- APP14-O4
- APP14-O11
- APP14-O12
- APP14-O16

#### Lessons

1. **Certificate chain, SAN and individual TLS peer** — Test valid and invalid local certificate/hostname chains, explaining what the browser actually authenticates and what the gateway must authenticate upstream.

2. **Termination, re-encryption and backend identity** — Compare verified HTTPS upstream with protected same-host transport, recording TLS validation and the risk of a publicly reachable cleartext origin.

3. **Trusted proxy allowlist, not client-sent identity** — Use documented proxy trust settings and forged Forwarded/X-Forwarded-* values to show only configured peers can contribute trusted metadata, never object authorization.

4. **Client source IP, NAT and verified principal** — Contrast socket peer, trusted proxy address and authenticated user in a NAT/two-account trace; make clear that IP-based fairness is not an identity proof.

5. **Direct-origin bypass and server-held denial** — Attempt direct-origin forged tenant/role and protected field access on a local disposable network, inspecting independent PostgreSQL rows even if gateway controls are bypassed.

6. **Optional mutual TLS and service versus user** — Explain optional mTLS trust and machine/key rotation from a local fixture without making mTLS mandatory; prove a verified service cannot bypass app user policy.

7. **Redirect and HSTS without host injection** — Test an owned HTTPS hostname, invalid Host redirect and actual HSTS limitations, avoiding claims about public preload/long-term browser policies not tested.

8. **Protect secrets in proxy and origin evidence** — Inspect sanitized errors and traces for Cookie, bearer, full private query and key bytes, verifying diagnostic provenance without leaking protected source.

*Optional practice — forged-proxy rehearsal:* Send contradictory address and scheme headers and verify server authority remains unchanged.

### Module 4 — Authentication Propagation and Application Authority

#### Outcomes

- APP14-O1
- APP14-O3
- APP14-O4
- APP14-O15
- APP14-O16

#### Lessons

1. **Gateway credential check versus origin authority** — Compare accepted edge session/JWT and server-side per-object/action/property/tenant checks, including a forbidden write by a valid user.

2. **Minimal verified principal across a trusted hop** — Strip attacker-supplied X-User/X-Tenant and use a verifiable trusted channel or application-owned session; prove raw client identity headers cannot grant authority.

3. **Issuer, audience, expiry and key/permission freshness** — Exercise an expired or wrong-audience credential and stale credential-cache case; distinguish token verification from current dynamic object rights.

4. **Revocation versus cached authentication response** — Revoke a test account and compare edge/direct-origin paths, including stale cached state, then choose bounded revalidation and privacy-safe denial.

5. **Actual server-side tenant and property decision** — Run two independent synthetic accounts against APP3 APIs, inspecting direct HTTP and PostgreSQL after unauthorized object and write-property attempts.

6. **CORS, preflight and cookie CSRF are separate** — Demonstrate browser preflight and a controlled cross-site credentialed mutation; distinguish CORS exposure from real CSRF/session authorization.

7. **Understandable 401/403 without secret disclosure** — Preserve correct refusal and accessible error behavior without leaking private routes, tokens or caching role-dependent denial across users.

*Optional practice — direct-origin attack:* Bypass the configured gateway in an isolated local lab and prove backend permission checks still reject.

### Module 5 — HTTP Cache Semantics and Representation Identity

#### Outcomes

- APP14-O5
- APP14-O6
- APP14-O8
- APP14-O15

#### Lessons

1. **Real shared cache storage and reuse** — Use Nginx OSS proxy_cache or another **real free shared-cache layer**, observe HIT/MISS/Age and origin SQL/revision; Caddy reverse_proxy alone is not evidence of response caching.

2. **RFC 9111 authenticated-response shared-cache exceptions** — Work through public, s-maxage and must-revalidate directives for responses to Authorization requests, then enforce stricter *no personalized response in shared cache* policy with real two-user evidence.

3. **Freshness arithmetic and private/no-store handling** — Calculate current Age and s-maxage/max-age, test private, no-store and explicit revalidation against actual cache state rather than treating a response header as proof of implementation.

4. **Strong/weak ETag, 304 and correct object** — Test changed/unchanged resource and a wrong validator/variant counterexample, proving the origin-provided current public representation is the one validated.

5. **Vary, canonical key and unkeyed input poisoning** — Compare host/path/query, language/encoding and an unkeyed reflected header, then prevent a shared public response or redirect from being poisoned.

6. **Cookies, private responses and cache deception** — Request a private tenant resource with static-looking suffix under two principals; show the cache cannot store/serve protected body, ETag, redirect or 4xx even with a mistaken public origin directive.

7. **Range 206, If-Range and byte identity** — Test actual static file partial response, strong validator and content range, confirming a revalidated different object cannot be assembled from stale segments.

8. **RFC 5861 bounded public stale and forbidden private stale** — Calculate stale-while-revalidate and stale-if-error bounds on safe public content, reject stale permission/private user data and show an actual controlled origin-outage difference.

*Optional practice — cache-state trace:* Record MISS, HIT, validation and stale decisions against origin truth and explain mismatches.

### Module 6 — Invalidation, Assets and Content Negotiation

#### Outcomes

- APP14-O5
- APP14-O6
- APP14-O8
- APP14-O15

#### Lessons

1. **Public and private content freshness consequences** — Use actual server revision and customer task to choose public asset/mutable content staleness and exclude dynamic tenant/permission state from shared cache.

2. **Hashed assets, retained chunks and new mutable HTML** — Open an old app tab after new deployment; find a missing lazy bundle or stale HTML and verify versioned immutable asset retention and safe entry-page policy.

3. **Privileged purge and precise cache key** — Exercise operator-only purge or version-key invalidation, deny untrusted purge and confirm correct host/variant entry is evicted rather than a different tenant.

4. **Mutation, cache refill and purge timing race** — Commit a real SQL update while a public response is filling cache; show the classic purge-before-fill stale race and choose a valid versioned-key/guarded policy.

5. **Two-tenant cache poisoning and private-data isolation** — Vary principal, path aliases, spoofed headers and query, then inspect actual cache/HIT/SQL to prove no other tenant's authorized body or stale permission can appear.

6. **Content encoding/language and ETag variant** — Test gzip/plain and two languages with Vary and actual bytes; detect a mismatched encoding, 304 or locale cache-key regression.

7. **Maintenance, error cache and recovery boundary** — Trigger local 404/503 and restore origin; demonstrate denied/private/error body is not cached into persistent false success or prolonged outage.

*Optional practice — stale asset recovery:* Deliberately publish a mismatched HTML-to-JavaScript release and repair via versioned asset rollout.

### Module 7 — Admission Control, Identity Fairness and Abuse

#### Outcomes

- APP14-O7
- APP14-O10
- APP14-O12
- APP14-O16

#### Lessons

1. **Measure rate, concurrency, body and SQL work** — Compare actual upstream active requests, bytes and completed operations under safe and abusive synthetic traffic instead of using 429 count alone.

2. **Token bucket numerical trace and edge burst** — Calculate concrete refill/burst recurrence, contrast fixed window boundary and test actual enforced rate with the provided time-controlled fixture.

3. **Authenticated principal versus spoofable IP** — Use two users behind one synthetic NAT and a forged X-Forwarded-For, choosing fair identity and independently finite anonymous/in-flight admission.

4. **Per-route, per-tenant and global protection** — Layer resource/CPU/body and request concurrency budgets; prove noisy tenant cannot starve another's legitimate completed work while service capacity remains finite.

5. **429/503 and finite retry guidance** — Differentiate business quota from upstream overload, check Retry-After as appropriate and ensure clients cannot amplify retries of uncertain committed writes.

6. **Independent limiter counters versus global claim** — Run two local gateway processes or a clearly labeled counter simulation, show local limits are not globally exact and defend coordination/failure costs.

7. **Payload-cost abuse and correct POST handling** — Probe locally bounded expensive SQL, oversized bodies and slow tasks; verify permitted SQL effects and origin resource bounds, including replay-safe state-changing requests.

8. **Limiter storage outage, refusal and fairness recovery** — Interrupt a test limiter component and document feature-specific fail-open/closed behavior without accidentally granting tenant rights or unlimited resources.

*Optional practice — fairness test:* Generate two identities and one noisy client, then inspect false denials and bypass attempts.

### Module 8 — Delivery Protocols, Streaming and Compression

#### Outcomes

- APP14-O2
- APP14-O8
- APP14-O9
- APP14-O15

#### Lessons

1. **HTTP/1.1, HTTP/2 and optional HTTP/3 negotiation** — Explain application/proxy/upstream protocol conversions with actual observed HTTP/1.1/2 where supported; HTTP/3/QUIC stays optional and not falsely claimed.

2. **Multiplexing cannot overcome origin pool limits** — Measure upstream concurrency/DB occupancy under identical client request mix, contrasting head-of-line/connections and actual origin capacity.

3. **Public compression, CPU/bytes and secret risk** — Measure gzip/Brotli where available against real static payload, cache encoding variants and private secret-adjacent reflected-content risks.

4. **Range and resumed static bytes** — Test real If-Range/Content-Range and validators before/after asset revision, showing exact bytes and safe unsupported behavior.

5. **Streaming response and buffer-caused delay** — Run actual bounded local event/chunk stream with buffering on/off, measure first-byte versus total completion and show false latency claims when the proxy coalesces output.

6. **Gateway streaming probe versus APP12 specialist skills** — Test stream/upgrade forwarding as an optional local probe without mandating APP12's SSE/WebSocket state synchronization or a paid transport.

7. **Connection, header, idle and total budgets** — Separate timeout phases on a slow but valid finite stream and a stalled upstream, ensuring bounded client resources without premature good-stream rejection.

*Optional practice — delivery regression:* Compare identical traffic with and without compression/buffering and explain observed correctness trade-offs.

### Module 9 — Measuring Latency, Tracing and Edge Cost

#### Outcomes

- APP14-O9
- APP14-O13
- APP14-O14
- APP14-O16

#### Lessons

1. **Eligible user task and end-to-end outcome** — Define successful authorized operation, wrong/private cache, rejected and timed-out populations before measuring gateway speed.

2. **Trace IDs without trusted client baggage** — Correlate controlled client/gateway/origin requests and note wall-clock offsets; a caller's traceparent/tenant string cannot grant authority or create a safe raw label.

3. **Actual HIT/MISS, SQL work and cache efficacy** — Measure public cache reuse, conditional revalidation, origin timing, bytes and a deliberately faster wrong-private response that must fail.

4. **Matched traffic and generator saturation** — Pin process/data/warmup and tenant/payload mix, account for client-generator limits, queue and denied/failed operations rather than success-only p95.

5. **Sample count, per-hop timing and percentile validity** — Compute p50/p95 with explicit sample/error denominator, respecting monotonic per-hop durations instead of subtracting unsynchronized host timestamps.

6. **Trace/log volume, cardinality and privacy** — Limit labels, bytes and CPU costs, scrub secrets/tenant IDs and compare observability overhead under load.

7. **Edge cost model tied to observed data** — Build labeled local byte/request/CPU input and hypothetical CDN/egress/region charges; never call one-host timing a measured global CDN response.

*Optional practice — before-and-after:* Reject an apparently faster cache when its results contain a stale or cross-user error.

### Module 10 — Timeouts, Overload and Failure Containment

#### Outcomes

- APP14-O10
- APP14-O11
- APP14-O12
- APP14-O15
- APP14-O16

#### Lessons

1. **Request deadlines and one end-to-end budget** — Trace client/gateway/origin/DB time and bound total retries, with a failure case where nested retries multiply attempts.

2. **Lost response after true committed mutation** — Commit through actual PostgreSQL then drop HTTP response; use server-recognized idempotency or authoritative reconciliation and never retry an unsafe POST blindly.

3. **Limited queues and optional circuit policy** — Simulate open/half-open/closed when a breaker is justified; compare a simpler finite in-flight/denial policy and check actual protected task outcome.

4. **Healthy gateway does not equal healthy business task** — Show green proxy /health while SQL or session auth fails; verify one legitimate and one denied request before claiming readiness.

5. **Actual stopped origin, public stale and protected refusal** — Stop the origin, compare eligible public stale-if-error with private tenant or uncertain write, inspecting real cache and SQL state.

6. **Failed limiter/cache dependencies without privilege expansion** — Shut down or fault a local component, choose bounded fail policy and independently prove tenant authorization and resource limits remain intact.

7. **Multiple processes, same data authority and inconsistency** — Compare two local upstreams with shared PostgreSQL or intentionally divergent fixture; explain why healthy routing does not establish coherent mutable data.

8. **Restart and coordinated retry-storm containment** — Resume origin with bounded simultaneous clients, measure retries/queue, choose jitter/admission and preserve authorized committed work.

*Optional practice — retry amplification:* Repair a gateway that retries a POST after an unknown committed database outcome.

### Module 11 — Release Control, Incident Response and Rollback

#### Outcomes

- APP14-O9
- APP14-O11
- APP14-O12
- APP14-O15
- APP14-O16

#### Lessons

1. **Versioned gateway policy with secure defaults** — Track route, TLS peers, real cache, limiter and stale config with reproducible source and explicit no-secret deny-by-default controls.

2. **Isolated staging source, digest and endpoint identity** — Start old/new local config and trusted CA with actual source/version provenance and accepted/denied policy checks before traffic change.

3. **Negative review of route, key and trust diffs** — Compare path normalization, auth headers, private cache exclusions and limiter failure behavior, anticipating a seeded leaking configuration.

4. **Scoped canary and tested kill switch** — Deploy one bounded synthetic route/cohort and fail back safely, distinguishing reversible proxy config from existing cached bodies and committed SQL.

5. **Recheck hostile cache, header, route and origin paths** — Use genuine tenant-negative, spoofed forwarded, static-like private suffix, unauthorized purge and real origin SQL cases at every policy change.

6. **Real bad policy, rollback and poisoned cache purge** — Introduce wrong routing or caching, reproduce an observable leak/stale response, revert and independently purge or forward-repair leftover corrupted cache state.

7. **Redacted operator runbook and complete repair oracle** — Document exact config version, disable/cache purge, origin SQL/tenant negative checks and measured recovery/remaining risk without secret-bearing logs.

*Optional practice — unfamiliar failure:* Investigate a reviewer-injected route bypass or cache poisoning pattern without relying on the original author.

### Module 12 — Edge Compute, Geographic Policy and Alternatives

#### Outcomes

- APP14-O3
- APP14-O9
- APP14-O13
- APP14-O14
- APP14-O15

#### Lessons

1. **When worker logic beats declarative config** — Compare routing/cache headers with a bounded transform/use case and document why a no-worker choice may be superior.

2. **Edge runtime CPU, storage and vendor assumptions** — Explain isolated workers, execution limits, secret access and billing from named docs; a local mock cannot prove real provider isolation.

3. **Worker identity cannot confer object permissions** — Challenge a supposed edge-authorized tenant header, requiring current APP3 action/object/property check on every protected origin operation.

4. **Geolocation is not data-residency compliance** — Reason through geography-derived routing with explicit model jurisdiction assumptions rather than equating user IP with lawful storage location.

5. **Two-region stale public cache and mutable truth** — Trace hypothetical POP invalidation differences against one authoritative revision; do not mislabel eventual propagation as tested globally linearizable data.

6. **Cost, portability and provider-failure comparison** — Estimate CDN/edge versus local proxy on illustrated egress, requests, runbooks, dependencies and outage recovery; keep provider-specific unknowns visible.

7. **Unsupported global claims and revisit trigger** — Distinguish measured one-host latency from modeled POP time, regional compliance, managed WAF and global reliability; define evidence that would justify deployment later.

*Optional practice — placement decision:* Reject an edge feature whose measured benefit does not exceed its complexity and security cost.

### Module 13 — One Tested Gateway and Independent Unfamiliar Incident Defense

#### Outcomes

- APP14-O1
- APP14-O2
- APP14-O3
- APP14-O4
- APP14-O5
- APP14-O6
- APP14-O7
- APP14-O8
- APP14-O9
- APP14-O10
- APP14-O11
- APP14-O12
- APP14-O13
- APP14-O14
- APP14-O15
- APP14-O16
- APP14-O17

#### Lessons

1. **One existing gateway, origin and accepted assessment index** — Reuse one APP3/PostgreSQL service plus real shared cache and **reference separately accepted APP14-AS1–AS6** config, SQL, traffic and security evidence rather than rebuild six projects.

2. **Reproduce protected routes, TLS identity and cache behavior** — Start clean free pinned proxy/cache/backend; observe public HIT/MISS/304/Vary, actual private-user exclusion, forged metadata and independent origin SQL denial.

3. **Recheck fair admission, stream, unknown commit and recovery** — Run representative accepted/denied quota, buffering, post-commit lost response and bad policy recovery from previously evaluated evidence without merely trusting health dashboards.

4. **Unseen bounded gateway/security/performance fault** — Receive an assessor-supplied previously unfamiliar path normalization, private cache, poisoned key, forwarded-trust, limiter, streaming, retry or deployment defect and predict client plus authoritative origin failure.

5. **Independent before/after causal correction** — Prove the new defect from independent real HTTP/cache/SQL outcomes, fix or safely contain it, and rerun only relevant prior authorization, resource and safe rollback regressions.

6. **Personally defended, accessible architecture decision** — Explain source/config and third-party contributions, actual versus modeled global/energy/cost claims, privacy, recovery and why simpler local gateway or CDN placement is justified.

## Completion requirements

All **APP14-O1–APP14-O17** require **seven independently decidable assessments** on one running gateway/cache/APP3 origin. AS1 owns correct routing and trust, AS2 measured RFC 9111 shared-cache behavior plus tenant safety, AS3 fair bounded admission, AS4 HTTP delivery and honest latency, AS5 uncertain commits and policy recovery, AS6 geographic/economic alternatives, and AS7 a fresh assessor-supplied bounded incident. Accepted AS1–AS6 evidence may be referenced, not duplicated as six new projects; AS7 cannot waive prior failed work. This **elective does not affect APP9 graduation**. Other exercises are formative.

- **APP14-AS1** — Controlled Routing, Proxy Trust and Origin Authorization
  - **Outcomes:** APP14-O1, APP14-O2, APP14-O3, APP14-O4, APP14-O12, APP14-O16.
  - **Work:** Implement a genuine local APP3/PostgreSQL backend and gateway with verified local TLS, safe static and two protected API routes. Send both direct-origin and proxied legitimate/forged requests testing path percent/dot/suffix confusion, Host/SNI/:authority, X-Forwarded-* and claimed user/tenant, invalid methods, hop-by-hop fields and controlled ambiguous Content-Length/Transfer-Encoding framing. Check actual backend SQL after unauthorized reads/writes.
  - **Criteria:** A reviewer observes faithful or rejected method/path/authority at both hops with no unintended second request or privileged route, and a valid TLS hostname/upstream trust. Untrusted forwarded/client identity cannot alter application rights or limiter identity, and a direct-origin bypass fails real APP3 object/action/property/tenant authorization. Real independent HTTP/SQL denial and redacted traces—not an edge 2xx or CORS setting—prove safety.
  - **Evidence:** Versioned proxy/origin source, route map, test inputs, TLS/forwarding traces, rejected request/SQL results and redacted operator transcript.

- **APP14-AS2** — RFC-Correct Caching, Invalidation and Private Data Defense
  - **Outcomes:** APP14-O5, APP14-O6, APP14-O8, APP14-O12, APP14-O15, APP14-O16.
  - **Work:** Configure **actual free shared-cache storage** (for example OSS Nginx proxy_cache) for one mutable public GET and hashed static asset, and explicitly bypass all authenticated/personal responses. Measure MISS/HIT, Age, Vary language/encoding, ETag/Last-Modified and true 304/200 after a real origin revision, invalidation and bounded public stale-if-error. Demonstrate RFC 9111 Authorization-bearing storage exceptions in an isolated explanatory trace while still prohibiting personalized reuse. Inject concurrent purge/fill, unkeyed hostile header, static-looking private suffix and two-account cookie/bearer changes.
  - **Criteria:** The cache actually stores/reuses public responses and independent origin state supports its measured validation/freshness/invalidation, with correct key, representation, partial/range and stale bounds. A header-only proxy or a fabricated HIT fails. No personalized tenant body, private error, redirect, validator or revoked data enters shared reuse even if a dangerous origin directive would permit storage under HTTP caching rules; cache deception/poisoning and unauthorized purge must fail.
  - **Evidence:** Cache configuration and keys, request/response headers, origin revisions, tests for concurrent mutation and user switching, captured state transitions and corrected regression.

- **APP14-AS3** — Fair Admission, Gateway Security and Resource Bounds
  - **Outcomes:** APP14-O3, APP14-O4, APP14-O7, APP14-O10, APP14-O12, APP14-O16.
  - **Work:** Use an actual gateway to enforce finite request/route/tenant/principal rate, body and concurrent expensive-origin limits; drive two legitimate synthetic identities sharing one source IP, anonymous/forged forwarding and a noisy tenant under controlled clock/burst. Calculate and exercise a token-bucket schedule, 429 versus 503 and Retry-After when valid, trigger limiter failure and one uncertain committed POST; count accepted, rejected, completed SQL, queue age, resource and retry attempts.
  - **Criteria:** Actual upstream CPU/queue/SQL and refusal data show finite resource use and fair progress for a second tenant, not merely lower successful-request latency. A spoofed X-Forwarded-For does not grant free budget and per-process limits aren't misrepresented as globally exact. Limiter/cache failure does not grant app permissions or unbounded origin work, and gateway retries do not duplicate committed mutations.
  - **Evidence:** Traffic generator, timed fixtures, resource and response distribution, policy decisions, unauthorized tests, failure mode traces and explicit fairness limitations.

- **APP14-AS4** — Correct Delivery and Measured Edge/Origin Attribution
  - **Outcomes:** APP14-O5, APP14-O8, APP14-O9, APP14-O13, APP14-O14, APP14-O15.
  - **Work:** With pinned local gateway, true public cache and APP3 origin, compare warmed/cold immutable/mutable asset delivery, safe Range/If-Range, compression and Vary variants, streaming with and without proxy buffering, eligible cache HIT/MISS and client/gateway/origin/SQL latency. Record negotiated HTTP version where supported, repeat counts, missing/timeouts and monotonic duration limitations. Evaluate hypothetical CDN/edge placement with separately labeled price/geography assumptions.
  - **Criteria:** Independent byte/Content-Range/validator and first-byte-versus-completion traces preserve actual authorized task and correct cache representation while comparing CPU, bandwidth and supported p50/p95. Compression or caching private/wrong assets cannot qualify as improvement. Do not subtract unsynchronized clocks, omit failed/denied samples or claim a local gateway tests POP, HTTP/3 or global geography it did not.
  - **Evidence:** Pinned workload scripts, environment table, network traces, sample sizes, latency/byte measurements, privacy-safe spans and cost/placement decision.

- **APP14-AS5** — Outage Containment, Change Control and Recoverable Rollback
  - **Outcomes:** APP14-O2, APP14-O3, APP14-O10, APP14-O11, APP14-O12, APP14-O15, APP14-O16.
  - **Work:** Version a real gateway policy, stage a bounded synthetic canary, introduce an actual bad route, proxy trust or private cache configuration and a stopped local APP3 origin. Execute a genuine PostgreSQL write whose committed response is lost before gateway confirmation, a limited public stale GET and a synchronized reconnect/retry wave. Observe actual active config, cache contents, user/denied paths, SQL commits and finite timeouts; repair via rollback, **poisoned cache purge** or safe forward fix.
  - **Criteria:** The reviewer reproduces bad policy and independently observes its correction with real client, cache and PostgreSQL evidence; config rollback by itself is not falsely assumed to remove a previously poisoned shared entry or undo committed effects. Uncertain POSTs are not blindly retried, stale tenant/permission information is not served and origin health alone doesn't declare business success. Redacted operator runbook states meaningful recovery and limitations.
  - **Evidence:** Config revisions, rollout and fault schedule, origin database truth, logs/metrics, rejected negative paths, incident timeline and tested operator runbook.

- **APP14-AS6** — Global/Edge Economics and Architecture Defense
  - **Outcomes:** APP14-O1, APP14-O9, APP14-O10, APP14-O13, APP14-O14, APP14-O15.
  - **Work:** Model no-CDN local gateway, managed CDN and optional edge worker against **actual** task-complete local gateway/cache/request/byte/resource measurements and stated hypothetical traffic, region, privacy, vendor lock-in, egress cost and incident burden. Compare when a single free local cache wins and when public geographic delivery might justify new complexity.
  - **Criteria:** Pricing/traffic/geography are labeled sourced assumptions or illustrative sensitivity, not fabricated measured POP latency or legal compliance. The decision preserves origin-held object authorization and mutable data consistency, includes failure/privacy/operating costs, gives a concrete revisit threshold and does not require paying for a cloud or worker.
  - **Evidence:** Topology and alternatives matrix, sample input measurements, budget assumptions, threat/security review, constraints and reasoned decision.

- **APP14-AS7** — Integrated Gateway Service and Independent Unfamiliar Defense
  - **Outcomes:** APP14-O1, APP14-O2, APP14-O3, APP14-O4, APP14-O5, APP14-O6, APP14-O7, APP14-O8, APP14-O9, APP14-O10, APP14-O11, APP14-O12, APP14-O13, APP14-O14, APP14-O15, APP14-O16, APP14-O17.
  - **Work:** Provide **one evolving APP3/PostgreSQL gateway with actual free shared-cache layer** and reference individually accepted APP14-AS1–AS6 judgments rather than recreate all their projects. Reproduce a few representative safe origin/tenant HTTP, real HIT/304/Vary, bounded fairness, streaming and unknown-commit/recoverable policy cases. Accept an **unseen bounded** hostile path/Host/forwarded identity, private cache poisoning/deception, unauthorized purge, limiter, buffered stream, stale revocation, unsafe retry or bad deployment case; predict and obtain independent before-fix HTTP/cache/SQL facts, repair and rerun targeted prior regressions.
  - **Criteria:** All APP14-AS1–AS6 remain separately passed; AS7 cannot excuse a missing gate or make this elective compulsory for core graduation. The genuinely unfamiliar failure is reproduced and corrected using actual origin SQL, cache keys/bodies and client observations, preserving trust, privacy, durable business state, bounded work and correct protocol handling. A fresh reviewer can run free local artifacts and the learner personally defends source, trade-offs, accessibility, unsupported global claims and residual risk.
  - **Evidence:** One pinned real proxy/cache and APP3 source, references-first accepted APP14-AS1–AS6 outcomes/evidence index, synthetic tenant/source and SQL fixtures, independent HTTP/cached response/rate/stream/rollback logs, assessor's unfamiliar bounded prompt, observed failing-before/passing-after cache/SQL/client checks and accessible documented/written/live defense.

### Shared academic and operational boundaries

- **Local, free, reproducible:** The assessed gateway, **actual free shared cache**, two tenant identities, controlled traffic, origin/database state, TLS trust configuration and faults run on disposable local infrastructure. A plain reverse proxy without response storage cannot pass HIT/MISS, conditional revalidation or purge evidence; a separate observed compatible cache is valid. Paid CDN/WAF vendors, cloud accounts, public domains, multiple regions and production load tests are optional.
- **Existing competence, deeper application:** Use APP3 server-held role/object/tenant/field checks and APP7 deploy/TLS basics rather than re-teaching them. A gateway may authenticate a session but cannot independently grant a backend operation. A passed edge token check never proves tenant/object authorization.
- **HTTP truth over slogans:** Use RFC 9110/9111/9112 and RFC 5861 where applicable, distinguishing actual cached storage/conditional `304`/`Vary`/`Age`/stale rules from merely configured headers. `public`, `s-maxage` and `must-revalidate` can permit certain shared reuse of Authorization-bearing responses within RFC 9111 constraints, but **deliberately bypass shared caching for all personalized responses** even if an origin sets an unsafe permissive directive. Independently test cache deception/poisoning, canonical path/host identity, wrong tenant and server permission revocation; TTL alone cannot prove safety.
- **Reproducible adversarial evidence:** Include malformed routes, forged trusted metadata, cross-tenant cache/permission attempts, ambiguous client address, burst fairness, lost response after a committed write, origin outage, invalid policy deployment and recovery. Retain independent origin SQL observations; avoid treating proxy `2xx` alone as final business truth.
- **Bounded measurements:** Describe workload, versions, actual system topology, sample counts, CPU and network budgets, warmup, clocks, observed tails and sources of error. Local results do not demonstrate global geographic latency, physical CDN behavior or external SLA.
- **Safe operation and privacy:** Use disposable synthetic identities; avoid attacking unaffiliated infrastructure. Limit resource consumption, redact authentication material, log only necessary identifiers, and document safe rollback and forward-repair paths.
- **Independent defense:** A reviewer may supply an unfamiliar, bounded security, performance, routing or cache failure. Provide reproducible before/after tests, a defensible correction or containment, a short operator runbook, failure analysis and a technical retrospective.
