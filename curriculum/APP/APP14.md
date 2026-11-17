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

Start with one protected local APP3 service backed by PostgreSQL, a public static asset route and a replaceable gateway such as Caddy, Nginx, Envoy or a similarly auditable implementation. Reproduce all mandatory behavior on a free local container/process environment, including two separate synthetic tenants, direct-origin negative requests and one real state-changing operation. CDN providers, DNS global points of presence, edge workers, multiple regions and managed WAFs are *comparison topics*, never required purchases or prerequisites. Distinguish local emulator/simulation evidence from actual global distributed behavior.

Trust is hop-specific: do not accept client-supplied `Forwarded`, `X-Forwarded-For`, role or tenant headers as authenticated facts; re-establish TLS peer identity and maintain server-side authorization. Apply RFC 9111 shared-cache rules with extra conservative protection for personalized content, and observe actual origin mutations before claiming cache freshness or failed-write safety. Rate limits cannot replace authorization and may be unfair when client identities are ambiguous. Read-only stale fallbacks do not prove current state, and proxy health checks do not establish database consistency. Operate only owned or disposable local test systems; do not load-test or attack third-party services.

Seventeen observable outcomes are developed in thirteen deliberately varied modules and evaluated through seven cumulative mandatory summative assessments. The source remains `draft`: machine checks alone do not certify pedagogy or production readiness.

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

1. **Gateway role and evolution** — Contrast reverse proxies, API gateways, CDNs and programmable edge services with application server responsibilities.

2. **One protected user journey** — Select an APP3 service with synthetic tenants, safe public assets and a mutation that must remain authorized.

3. **Flow and trust diagram** — Trace client, DNS, TLS, gateway, cache, upstream and database ownership across hop boundaries.

4. **Threat and failure assumptions** — Enumerate host spoofing, credential replay, cache leaks, origin bypass and request amplification.

5. **Edge placement decisions** — Compare gateway-only, CDN-plus-gateway and optional worker paths without introducing unneeded infrastructure.

6. **Local evidence baseline** — Version an APP7-like container/process deployment and capture origin-only latency and negative authorization.

7. **Developer and operator needs** — State deploy, diagnose and rollback needs with explicit availability and privacy limits.

*Optional practice — architecture review:* Identify a falsely trusted edge header and correct the origin-owned authority model.

### Module 2 — Canonical Routing and HTTP Message Semantics

#### Outcomes

- APP14-O2
- APP14-O3
- APP14-O12
- APP14-O16

#### Lessons

1. **Request-target forms** — Explain absolute, origin and authority request targets and their consequences for route matching.

2. **Path normalization** — Test percent encoding, dot segments, doubled separators and case handling before backend path resolution.

3. **Host and authority enforcement** — Reject conflicting Host, scheme and authority inputs including misdirected virtual hosts.

4. **Method and status correctness** — Preserve safe methods, mutation expectations, 404, 405, 413, 429, 502 and 503 distinctions.

5. **Hop-by-hop metadata** — Remove Connection-nominated and other hop-by-hop headers and avoid trusting client-provided routing fields.

6. **Body and header budgets** — Set explicit size, field count and request duration limits with controlled error behavior.

7. **Upstream selection** — Route two service paths and one public asset class while proving forbidden routes remain inaccessible.

8. **Desynchronization threat** — Explain conflicting message length/framing and why intermediary/backend parsing disagreement is dangerous.

*Optional practice — hostile request probe:* Produce raw valid and invalid requests and compare observed gateway and origin interpretation.

### Module 3 — TLS, Forwarding Identity and Origin Isolation

#### Outcomes

- APP14-O3
- APP14-O4
- APP14-O11
- APP14-O12
- APP14-O16

#### Lessons

1. **Certificate identity** — Trace certificate trust, SAN hostname matching, renewal and the actual peer each hop authenticates.

2. **HTTPS termination modes** — Compare gateway termination with encrypted re-encryption and documented upstream verification.

3. **Trusted proxy configuration** — Strip untrusted Forwarded and X-Forwarded-* metadata before constructing an authenticated hop chain.

4. **Client address ambiguity** — Distinguish socket peer, proxy asserted IP and verified principal for abuse and audit decisions.

5. **Origin network restriction** — Demonstrate that an origin cannot rely on a gateway header alone to block bypass traffic.

6. **mTLS use cases** — Evaluate mutually authenticated upstreams while distinguishing machine identity from end-user permissions.

7. **Redirects and HSTS** — Test HTTPS redirect and browser policy only where the local hostname and certificate support claims.

8. **Secrets and certificates in logs** — Redact key material, tokens and sensitive URL components from gateway and upstream diagnostics.

*Optional practice — forged-proxy rehearsal:* Send contradictory address and scheme headers and verify server authority remains unchanged.

### Module 4 — Authentication Propagation and Application Authority

#### Outcomes

- APP14-O1
- APP14-O3
- APP14-O4
- APP14-O15
- APP14-O16

#### Lessons

1. **Gateway credential roles** — Contrast gateway access control, bearer verification, opaque session introspection and backend decisions.

2. **Principal propagation** — Pass minimal authenticated identity through a documented trusted path without accepting arbitrary headers.

3. **Audience and expiry** — Verify token audience, expiry, issuer and key-rotation decisions at the appropriate responsibility boundary.

4. **Dynamic revocation** — Show how cached identity or session state can outlive a revoked account and choose bounded revalidation.

5. **Origin role and tenant rules** — Run two synthetic tenants and reject cross-object and forbidden-field requests directly at origin.

6. **Preflight and CORS** — Test browser-origin policy as a client exposure control rather than a substitute for authentication.

7. **Error shape and privacy** — Keep 401/403 responses distinguishable without returning secrets, internal routes or sensitive policy detail.

*Optional practice — direct-origin attack:* Bypass the configured gateway in an isolated local lab and prove backend permission checks still reject.

### Module 5 — HTTP Cache Semantics and Representation Identity

#### Outcomes

- APP14-O5
- APP14-O6
- APP14-O8
- APP14-O15

#### Lessons

1. **Cache storage versus reuse** — Distinguish private and shared caches, freshness, validation and stored representation eligibility.

2. **RFC 9111 authorization rules** — Verify shared caches cannot reuse authenticated responses absent explicit permitted directives and safe design.

3. **Cache-Control directives** — Exercise private, no-store, max-age, s-maxage and revalidation under precise representative requests.

4. **Validators and 304** — Generate ETag or Last-Modified and prove conditional revalidation against a changed and unchanged representation.

5. **Cache keys and Vary** — Include necessary host, path, query and representation-varying headers while avoiding accidental personalized reuse.

6. **Cookie and session hazards** — Explain why a public directive on a response containing private data can leak across principals.

7. **Partial content boundaries** — Inspect 206, Range and strong validators without incorrectly assembling unrelated byte ranges.

8. **Stale response controls** — Model stale-while-revalidate and stale-if-error only on safely eligible representations with bounded age.

*Optional practice — cache-state trace:* Record MISS, HIT, validation and stale decisions against origin truth and explain mismatches.

### Module 6 — Invalidation, Assets and Content Negotiation

#### Outcomes

- APP14-O5
- APP14-O6
- APP14-O8
- APP14-O15

#### Lessons

1. **Freshness budgets** — Assign public asset and mutable API freshness according to the cost of stale state.

2. **Content-addressed assets** — Use hashed filenames and immutable retention with explicit HTML entrypoint update policy.

3. **Purge ownership** — Constrain purge operations to trusted deployers and scope keys or tags to the intended representation.

4. **Mutation and invalidation race** — Show a committed database mutation and concurrent reader, then bound the permitted stale interval.

5. **Cross-tenant leak scenario** — Swap test principals and vary request headers to prove authorization-dependent responses never share keys.

6. **Content negotiation** — Exercise language, encoding and media variants without mixing incompatible cached representations.

7. **Error caching policy** — Explain when 404/5xx or maintenance pages may be cached and how to prevent persistent outage masking.

*Optional practice — stale asset recovery:* Deliberately publish a mismatched HTML-to-JavaScript release and repair via versioned asset rollout.

### Module 7 — Admission Control, Identity Fairness and Abuse

#### Outcomes

- APP14-O7
- APP14-O10
- APP14-O12
- APP14-O16

#### Lessons

1. **Resource accounting** — Distinguish request rate, concurrent requests, body bytes and expensive origin operations.

2. **Token and leaky buckets** — Calculate burst allowance and sustained service rate using a reproducible time-controlled workload.

3. **Principal selection** — Compare verified account, API key, route, network and anonymous bucket choices with NAT fairness caveats.

4. **Policy composition** — Apply separate global, per-route and per-tenant budgets to preserve scarce upstream capacity.

5. **429 versus 503** — Distinguish policy refusal from service overload and publish coherent retry guidance where supportable.

6. **Distributed limit coordination** — Explain local counter skew, coordinated stores and degraded availability without claiming global exactness.

7. **Cost-based abuse** — Exercise large payloads, costly queries, open-ended concurrency and replay-safe mutation denial.

8. **Fail-open or fail-closed** — Choose and test limiter-store failure behavior according to feature risk and operability.

*Optional practice — fairness test:* Generate two identities and one noisy client, then inspect false denials and bypass attempts.

### Module 8 — Delivery Protocols, Streaming and Compression

#### Outcomes

- APP14-O2
- APP14-O8
- APP14-O9
- APP14-O15

#### Lessons

1. **HTTP versions and multiplexing** — Distinguish transport semantics of HTTP/1.1, HTTP/2 and HTTP/3 from application authorization.

2. **Head-of-line and queuing** — Compare upstream connection budgets, request scheduling and response latency under contention.

3. **Compression eligibility** — Check content type, secret-adjacent compression risks and actual transfer size before enabling transforms.

4. **Range and resume** — Verify byte-range, content length, validator and unsupported range response behavior for safe files.

5. **Streaming and buffering** — Measure first-byte versus total duration when an intermediary buffers an SSE or chunked response.

6. **Realtime boundary** — Reuse APP12-like streaming semantics only as optional probe; the elective assesses gateway delivery, not APP12 mastery.

7. **Timeouts during streaming** — Separate connect, header, idle and total budgets without prematurely killing valid bounded streams.

*Optional practice — delivery regression:* Compare identical traffic with and without compression/buffering and explain observed correctness trade-offs.

### Module 9 — Measuring Latency, Tracing and Edge Cost

#### Outcomes

- APP14-O9
- APP14-O13
- APP14-O14
- APP14-O16

#### Lessons

1. **Measurement question** — Define client-perceived latency and upstream resource measures before choosing a gateway optimization.

2. **Trace parentage** — Correlate request identifiers and span contexts while treating client-provided traces as untrusted input.

3. **Cache attribution** — Split hit ratio, miss latency, origin compute, response bytes and backend database timings.

4. **Load experiment design** — Pin hardware/processes, warmup, concurrency, payload mix and confidence limits for repeatability.

5. **Tail and uncertainty** — Report p50/p95/p99 only with meaningful sample count and describe sampling or clock uncertainty.

6. **Observer and privacy cost** — Redact identifiers and bounded logs; quantify telemetry volume and performance overhead.

7. **Egress and CDN fees** — Compare measured byte/request counts with hypothetical price tables, clearly labeling assumptions.

*Optional practice — before-and-after:* Reject an apparently faster cache when its results contain a stale or cross-user error.

### Module 10 — Timeouts, Overload and Failure Containment

#### Outcomes

- APP14-O10
- APP14-O11
- APP14-O12
- APP14-O15
- APP14-O16

#### Lessons

1. **End-to-end deadline** — Allocate upstream, gateway and client budgets without multiplying hidden retries.

2. **Safe write retries** — Require stable idempotency or explicit uncertainty handling for state-changing requests.

3. **Circuit and queue policies** — Bound pending work and explain open, half-open, rejected and recovering states.

4. **Health versus readiness** — Separate process liveness, dependency reachability and actual authorized request success.

5. **Origin outage experiment** — Stop the origin during concurrent reads and writes and record what clients can trust.

6. **Failure of limiter or cache** — Analyze degraded dependency policy and ensure it does not silently grant origin permissions.

7. **Multi-origin fallbacks** — Explain why healthy routing targets do not guarantee consistent mutable state or global availability.

8. **Reconnection and retry storms** — Exercise deterministic jitter and admission budgets after a synchronized recovery.

*Optional practice — retry amplification:* Repair a gateway that retries a POST after an unknown committed database outcome.

### Module 11 — Release Control, Incident Response and Rollback

#### Outcomes

- APP14-O9
- APP14-O11
- APP14-O12
- APP14-O15
- APP14-O16

#### Lessons

1. **Configuration as reviewed code** — Version routes, cache policies, limits and certificates with safe defaults and no secret literals.

2. **Local staging promotion** — Recreate isolated configurations and check their provenance before serving synthetic test traffic.

3. **Change diff and dry run** — Compare intended routes, cache keys, identities and limit budgets before enabling a new version.

4. **Canary and kill switch** — Scope a policy rollout to one test path and provide a bounded immediate reversal.

5. **Negative-path acceptance** — Re-run wrong tenant, forged header, private-cache and unauthorized purge tests on every release.

6. **Observable rollback** — Induce a bad route or cache policy, identify the revision and verify restored correct responses.

7. **Incident timeline** — Preserve sanitized correlated gateway and origin records, limitations and observed recovery timing.

8. **Forward repair** — Explain when purged caches, changed keys or client-stored assets prevent rollback alone.

*Optional practice — unfamiliar failure:* Investigate a reviewer-injected route bypass or cache poisoning pattern without relying on the original author.

### Module 12 — Edge Compute, Geographic Policy and Alternatives

#### Outcomes

- APP14-O3
- APP14-O9
- APP14-O13
- APP14-O14
- APP14-O15

#### Lessons

1. **When edge code is justified** — Compare declarative routing and application logic with a small user-facing edge transformation.

2. **Runtime constraints** — Trace isolate, memory, CPU, storage, secrets and network limitations of representative edge workers.

3. **Authorization at execution sites** — Show why a worker cannot safely make final object permission decisions from stale headers.

4. **Geo placement and residency** — Distinguish geolocation hints, data residency requirements and measured endpoint proximity.

5. **Multi-region mutable truth** — Explain invalidation, revision ownership and eventual propagation without promising linearizable reads.

6. **Vendor and outage risk** — Evaluate proprietary APIs, configuration portability, origin fallback and provider incidents.

7. **Local emulation honesty** — Label simulated edge execution and never claim globally distributed timing from one host.

*Optional practice — placement decision:* Reject an edge feature whose measured benefit does not exceed its complexity and security cost.

### Module 13 — Integrated Gateway, Negative Tests and Defense

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

1. **Defensible deployment brief** — State a realistic public asset, private tenant API and replay-sensitive mutation contract.

2. **Reproducible gateway source** — Build a local gateway in front of a real APP3 origin with verified APP7 deployment controls.

3. **Routing and identity proof** — Submit valid/forged requests at both gateway and direct origin to show trust and authorization.

4. **Safe public cache proof** — Trace fresh, stale, conditional and invalidated representations without mixing tenant responses.

5. **Controlled rate fairness** — Exercise limits for multiple identities and inspect failure status, bounds and resource use.

6. **Delivery comparison** — Measure asset and streaming response behavior under fixed compression and buffer settings.

7. **Outage and retry experiment** — Interrupt the origin, lose a write response and prove bounded retries and committed effect.

8. **Rollback practice** — Introduce an unsafe route or cache configuration and recover with independent verification.

9. **Local versus global claims** — Defend where CDN, multi-region, worker and paid-cloud behavior remains hypothetical.

10. **Unfamiliar incident defense** — Diagnose a bounded injected cache, trust, rate or retry defect, reproduce and explain its repair.

11. **Technical retrospective** — Present checked-in configuration, threat matrix, raw results, trade-offs and remaining risks.

## Completion requirements

All **APP14-O1–APP14-O17** must be demonstrated across **seven required summative assessments**. One integrated local origin/gateway application may supply evidence throughout. Module practice and formative probes are instructional, not additional unpublished graduation gates.

- **APP14-AS1** — Controlled Routing, Proxy Trust and Origin Authorization
  - **Outcomes:** APP14-O1, APP14-O2, APP14-O3, APP14-O4, APP14-O12, APP14-O16.
  - **Work:** Implement local gateway routes for public assets, two service endpoints and two synthetic tenants; attack ambiguous paths, forwarded metadata, direct-origin access and forbidden objects.
  - **Criteria:** Correct routing and explicit failure statuses; no spoofed principal or proxy address grants authority; direct origin independently rejects unauthorized action, object, property and tenant requests; errors expose no secrets.
  - **Evidence:** Versioned proxy/origin source, route map, test inputs, TLS/forwarding traces, rejected request/SQL results and redacted operator transcript.

- **APP14-AS2** — RFC-Correct Caching, Invalidation and Private Data Defense
  - **Outcomes:** APP14-O5, APP14-O6, APP14-O8, APP14-O12, APP14-O15, APP14-O16.
  - **Work:** Implement one public mutable representation, one versioned asset, one authenticated personalized endpoint and a controlled invalidation/revalidation schedule.
  - **Criteria:** Show correct MISS/HIT, 304 and Vary behavior; stale bounds match published policy; no authenticated representation crosses test identities; unsafe directives and purge permissions are rejected.
  - **Evidence:** Cache configuration and keys, request/response headers, origin revisions, tests for concurrent mutation and user switching, captured state transitions and corrected regression.

- **APP14-AS3** — Fair Admission, Gateway Security and Resource Bounds
  - **Outcomes:** APP14-O3, APP14-O4, APP14-O7, APP14-O10, APP14-O12, APP14-O16.
  - **Work:** Configure per-principal/route rate, concurrency and body budgets; run mixed normal, burst, malicious and uncertain-client traces including limiter failure.
  - **Criteria:** Excessive work is bounded with coherent refusal; two identities remain isolated within declared fairness limitations; bypass and unauthorized origin mutation fail; no unbounded retry amplification.
  - **Evidence:** Traffic generator, timed fixtures, resource and response distribution, policy decisions, unauthorized tests, failure mode traces and explicit fairness limitations.

- **APP14-AS4** — Correct Delivery and Measured Edge/Origin Attribution
  - **Outcomes:** APP14-O5, APP14-O8, APP14-O9, APP14-O13, APP14-O14, APP14-O15.
  - **Work:** Compare public asset, range and streaming API delivery with and without compression, buffering and safe caching; evaluate an edge-worker or CDN alternative without requiring deployment.
  - **Criteria:** Report repeatable client/edge/origin p50/tail timing and byte counts; preserve range and stream semantics; justify optimization only where measured gain coexists with correct caching and identity.
  - **Evidence:** Pinned workload scripts, environment table, network traces, sample sizes, latency/byte measurements, privacy-safe spans and cost/placement decision.

- **APP14-AS5** — Outage Containment, Change Control and Recoverable Rollback
  - **Outcomes:** APP14-O2, APP14-O3, APP14-O10, APP14-O11, APP14-O12, APP14-O15, APP14-O16.
  - **Work:** Introduce bad route/cache policy, stopped origin, unknown-commit mutation response and simulated rollouts on an isolated disposable environment.
  - **Criteria:** Demonstrate bounded deadlines, no unintended duplicate writes, identified bad revision, verified rollback or forward repair and no relaxed authorization during recovery.
  - **Evidence:** Config revisions, rollout and fault schedule, origin database truth, logs/metrics, rejected negative paths, incident timeline and tested operator runbook.

- **APP14-AS6** — Global/Edge Economics and Architecture Defense
  - **Outcomes:** APP14-O1, APP14-O9, APP14-O10, APP14-O13, APP14-O14, APP14-O15.
  - **Work:** Publish an engineering decision comparing local gateway, CDN and edge worker paths and analyze geographic data/routing claims with a realistic resource budget.
  - **Criteria:** Choose based on user task and measured local inputs; distinguish model from observed external behavior; explain consistency, egress, regional regulation and paid/managed operational uncertainty.
  - **Evidence:** Topology and alternatives matrix, sample input measurements, budget assumptions, threat/security review, constraints and reasoned decision.

- **APP14-AS7** — Integrated Gateway Service and Independent Unfamiliar Defense
  - **Outcomes:** APP14-O1, APP14-O2, APP14-O3, APP14-O4, APP14-O5, APP14-O6, APP14-O7, APP14-O8, APP14-O9, APP14-O10, APP14-O11, APP14-O12, APP14-O13, APP14-O14, APP14-O15, APP14-O16, APP14-O17.
  - **Work:** Rebuild, demonstrate and defend one complete gateway-plus-origin slice; accept an unknown bounded route, identity, cache, limit, stream or failure defect, diagnose and correct or safely contain it.
  - **Criteria:** Clean reproduction with no paid provider; all core negative tests pass; observed origin SQL truth, cache/privacy, admission and rollback evidence match stated outcomes; review explains unresolved hazards.
  - **Evidence:** Source and environment lock, runnable test harness, sanitized traces and SQL observations, two-identity fault matrix, before/after change, timing measurements, reviewed runbook and accessible technical defense.

### Shared academic and operational boundaries

- **Local, free, reproducible:** The assessed gateway, two tenant identities, controlled traffic, origin/database state, TLS trust configuration and faults must be observable on disposable local infrastructure. Paid CDN/WAF vendors, cloud accounts, public domains, multi-region deployment and production load tests are optional and never required.
- **Existing competence, deeper application:** Use APP3 server-held role/object/tenant/field checks and APP7 deploy/TLS basics rather than re-teaching them. A gateway may authenticate a session but cannot independently grant a backend operation. A passed edge token check never proves tenant/object authorization.
- **HTTP truth over slogans:** Cite the applicable version of HTTP caching and message standards in project reasoning. Differentiate `private`, `no-store`, conditional `304`, `Vary`, authorized shared reuse and stale extensions. Never intentionally cache personal responses in a shared store for convenience or claim that a TTL alone prevents a privacy leak.
- **Reproducible adversarial evidence:** Include malformed routes, forged trusted metadata, cross-tenant cache/permission attempts, ambiguous client address, burst fairness, lost response after a committed write, origin outage, invalid policy deployment and recovery. Retain independent origin SQL observations; avoid treating proxy `2xx` alone as final business truth.
- **Bounded measurements:** Describe workload, versions, actual system topology, sample counts, CPU and network budgets, warmup, clocks, observed tails and sources of error. Local results do not demonstrate global geographic latency, physical CDN behavior or external SLA.
- **Safe operation and privacy:** Use disposable synthetic identities; avoid attacking unaffiliated infrastructure. Limit resource consumption, redact authentication material, log only necessary identifiers, and document safe rollback and forward-repair paths.
- **Independent defense:** A reviewer may supply an unfamiliar, bounded security, performance, routing or cache failure. Provide reproducible before/after tests, a defensible correction or containment, a short operator runbook, failure analysis and a technical retrospective.
