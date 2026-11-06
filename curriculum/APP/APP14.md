# APP14 — API Gateways & Edge Delivery

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP3](APP3.md), [APP7](APP7.md)
**Duration:** 7 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Design and operate the boundary between external clients and application services. Study routing, authentication, rate control, caching, TLS, content delivery and edge execution, with special attention to the difference between security at the edge and authority in the origin service.

This specialization is optional and not required for APP9 or APP graduation.

## Learning outcomes

By the end of this course, the learner will be able to:

- Explain reverse proxies, gateways, CDNs and edge runtimes and their distinct responsibilities.
- Configure safe request routing, timeout handling, identity propagation and origin protections.
- Apply cache-control policies with correct invalidation and sensitive-data boundaries.
- Design rate limiting and abuse controls and evaluate their fairness and failure modes.
- Measure edge/origin latency, identify failures and document rollback procedures.
- Design correct caching and streaming policies for public, private and mutable HTTP responses.
- Detect gateway identity spoofing and avoid using edge controls as a substitute for backend authorization.
- Rehearse origin outages and controlled failover while bounding retries, cost and service disruption.

## Modules

### Module 1 — Gateway & Routing Boundaries

#### Outcomes

- Explain the gateway's responsibility relative to the backend service.
- Route requests with explicit timeout, header and error policies.

- Configure gateway routing without confusing edge trust with origin authorization.

#### Lessons

1. **Course introduction: API Gateways & Edge Delivery** — `lesson`

   Design and operate the boundary between external clients and application services. Study routing, authentication, rate control, caching, TLS, content delivery and edge execution, with special attention to the difference between security at the edge and authority in the origin service.
2. **Reverse proxies and request routing** — `lesson`
3. **Headers, forwarded identity and transport security** — `lesson`
4. **L4/L7 load balancing and proxy trust** — `lesson`
5. **Request normalization, path routing and upstream health** — `lesson`
6. **TLS termination, certificate lifecycle and upstream TLS** — `lesson`
7. **Gateway boundary reasoning** — `test`
8. **Configure an application gateway** — `lab`

### Module 2 — Caching & Content Delivery

#### Outcomes

- Distinguish public assets, private responses and cache keys.
- Choose freshness, validation and invalidation strategies.

- Apply caching to safe response classes while preserving user-specific confidentiality.

#### Lessons

1. **CDN placement and cache keys** — `lesson`
2. **HTTP caching, revalidation and purge** — `lesson`
3. **Shared versus private cache key design** — `lesson`
4. **Conditional requests, revalidation and TTL policy** — `lesson`
5. **Surrogate keys, purge controls and stale-while-revalidate** — `lesson`
6. **Evaluating edge cache safety** — `test`
7. **Test an invalidation scenario** — `lab`

### Module 3 — Identity, Rate Limits & Abuse

#### Outcomes

- Preserve origin-side authorization despite edge authentication.
- Explain quota policies, burst behavior and client identification risks.

- Enforce admission controls without substituting gateway checks for application permission checks.

#### Lessons

1. **Authentication boundaries and token forwarding** — `lesson`
2. **Rate limiting, quotas and failure policies** — `lesson`
3. **JWT validation boundaries and session revocation** — `lesson`
4. **Adaptive rate limits, quotas and fair identity selection** — `lesson`
5. **WAF trade-offs and application-level authorization** — `lesson`
6. **Analyzing gateway abuse controls** — `test`
7. **Exercise rate controls** — `lab`

### Module 4 — Edge Compute & Operations

#### Outcomes

- Decide when edge execution is worth operational complexity.
- Investigate origin health, connection pooling and incident recovery.

- Diagnose gateway failures across transport, edge logic and origin dependencies.

#### Lessons

1. **Edge functions and execution constraints** — `lesson`
2. **Telemetry, health checks and safe rollback** — `lesson`
3. **Edge compute runtime restrictions** — `lesson`
4. **Observability across edge and origin** — `lesson`
5. **Deployment rollout, configuration drift and rollback** — `lesson`
6. **Choosing edge versus origin** — `test`
7. **Recover from a bad route** — `lab`

### Module 5 — Advanced CDN, Streaming & Delivery

#### Outcomes

- Tune content delivery based on measured application workloads.
- Explain the correctness and latency trade-offs of streaming, compression and edge caching.

#### Lessons

1. **HTTP/2 and HTTP/3 delivery trade-offs** — `lesson`
2. **Compression, range requests and content negotiation** — `lesson`
3. **Streaming responses and edge buffering** — `lesson`
4. **Static asset versioning and cache-bust correctness** — `lesson`
5. **Edge delivery and streaming decisions** — `test`
6. **Benchmark and repair an edge-delivery regression** — `lab`

### Module 6 — Gateway Resilience & Global Operation

#### Outcomes

- Define failure containment and recovery procedures for an application gateway.
- Assess multi-region performance without promising consistency or availability unsupported by the architecture.

#### Lessons

1. **Health checks, circuit breaking and upstream failover** — `lesson`
2. **Timeout budgets and retry amplification** — `lesson`
3. **Geo-routing and multi-region consistency limits** — `lesson`
4. **Cost, egress and blast-radius analysis** — `lesson`
5. **Upstream outages, retries and global trade-offs** — `test`
6. **Recover from an upstream outage** — `lab`

### Module 7 — Measured API Gateway & Edge Deployment

#### Outcomes

- Integrate the elective's techniques in a working and verifiable application change or system.
- Evaluate correctness, operational limitations and trade-offs through reproducible evidence.

#### Lessons

1. **Measured API Gateway & Edge Deployment** — `lab`

## Completion requirements

- Complete the required module checkpoints and practical exercises, then complete the final integration lab.
- State tools, versions, system assumptions and test data for reproducibility.
- Retain artifacts, test results, design decisions, an investigated failure and a technical retrospective in accordance with [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required module checkpoints and practical work:**

- **Module 1 — Gateway & Routing Boundaries:** Pass `Gateway boundary reasoning` by explaining and applying the module outcomes; perform the `Configure an application gateway` lab: Place a gateway before two endpoints and verify routing, forwarded headers, TLS settings and upstream errors. Retain Configuration, request traces and negative-path tests.
- **Module 2 — Caching & Content Delivery:** Pass `Evaluating edge cache safety` by explaining and applying the module outcomes; perform the `Test an invalidation scenario` lab: Cache a public response, update the origin and verify freshness; show why an authenticated response cannot leak across users. Retain Cache-control evidence, request headers and purge/revalidation trace.
- **Module 3 — Identity, Rate Limits & Abuse:** Pass `Analyzing gateway abuse controls` by explaining and applying the module outcomes; perform the `Exercise rate controls` lab: Send controlled bursts from multiple identities, verify enforcement and measure false rejection or bypass risk. Retain Traffic generator, response table and access log.
- **Module 4 — Edge Compute & Operations:** Pass `Choosing edge versus origin` by explaining and applying the module outcomes; perform the `Recover from a bad route` lab: Deploy an intentional route/configuration defect in an isolated environment, diagnose it and roll back with verifiable recovery. Retain Deployment revision, incident timeline and rollback test.

**Final integration lab — Measured API Gateway & Edge Deployment:**

Deploy a gateway/CDN in front of an existing application API and static frontend. Configure secure routes, differentiated caching, bounded rate controls and observability, then conduct a controlled failure and recovery. Keep backend authorization enforceable independently of the gateway.

**Success criteria:**

- Prove public content cache behavior and demonstrate that user-specific responses are not shared.
- Demonstrate correct routing, client identity handling, origin authorization and bounded rate controls.
- Compare gateway and origin latency under a documented workload.
- Successfully reproduce and recover from a bad configuration with an auditable rollback.

**Evidence to retain:**

- Version-controlled implementation and configuration, including clean-rebuild instructions.
- Inputs and repeatable tests, output or measurements, and failure/recovery records.
- Trade-off analysis, limitations and technical retrospective.

**Failure analysis:**

Investigate cache poisoning or leakage, forged forwarding headers, incorrect TLS termination, rate-limit unfairness and stale edge configuration.

**Expanded module assessment and lab requirements:**

- **Module 1 checkpoint and micro-lab:** Prove route isolation, correct identity forwarding, TLS certificate behavior and safe upstream failures.
- **Module 2 checkpoint and micro-lab:** Demonstrate correct fresh/stale transitions and tests proving authenticated responses cannot be shared.
- **Module 3 checkpoint and micro-lab:** Show correct rejection of forged forwarded identity and unauthorized object access, including rate-limit behavior.
- **Module 4 checkpoint and micro-lab:** Trace requests across edge and origin and recover from a bad route or deployment using versioned configuration.

- **Module 5 — Advanced CDN, Streaming & Delivery (Benchmark and repair an edge-delivery regression):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Measure a static asset and streaming API endpoint through a gateway with and without caching/compression, then verify cache invalidation.
  - Verification: Match test conditions and prove correct range/stream behavior and authenticated data isolation.
  - Evidence: Request timing traces, cache headers, error responses and client tests.
  - Failure analysis: Explain buffering latency, cache key collisions, unsafe response compression and stale asset deployment.
- **Module 6 — Gateway Resilience & Global Operation (Recover from an upstream outage):**
  - Prerequisites: Explain the module outcomes and complete its teaching lessons.
  - Environment: Document a safe, reproducible local or simulated environment with exact relevant settings.
  - Required work: Simulate an origin timeout and failover target, enforce retry limits and verify that state-changing requests are not duplicated.
  - Verification: Demonstrate controlled error signaling, bounded resource use and a tested rollback or failover procedure.
  - Evidence: Gateway configuration, request traces, failure timeline and cost assumptions.
  - Failure analysis: Identify unbounded retries, forwarding-header spoofing and CDN cost spikes.

**Exit assessment expectation:**

Demonstrate the subject outcomes on an unfamiliar example, show at least one negative path and retain evidence allowing another reviewer to reproduce the result. Checkpoint answers must explain mechanisms, while the final integration lab must integrate and verify the expanded topics.

**Exit demonstration:**

Demonstrate the resulting implementation, explain its key mechanisms, reproduce at least one failure and recovery and defend the chosen trade-offs with inspectable evidence.
