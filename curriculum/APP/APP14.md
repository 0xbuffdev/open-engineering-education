# APP14 — API Gateways & Edge Delivery

**Program:** APP — Application Engineering
**Classification:** `elective`
**Type:** `course`
**Prerequisites:** [APP3](APP3.md), [APP7](APP7.md)
**Duration:** 5 weeks
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

## Modules

### Module 1 — Gateway & Routing Boundaries

#### Outcomes

- Explain the gateway's responsibility relative to the backend service.
- Route requests with explicit timeout, header and error policies.

#### Lessons

1. **Course introduction: API Gateways & Edge Delivery** — `lesson`

   Design and operate the boundary between external clients and application services. Study routing, authentication, rate control, caching, TLS, content delivery and edge execution, with special attention to the difference between security at the edge and authority in the origin service.
2. **Reverse proxies and request routing** — `lesson`
3. **Headers, forwarded identity and transport security** — `lesson`
4. **Gateway boundary reasoning** — `test`
5. **Configure an application gateway** — `lab`

### Module 2 — Caching & Content Delivery

#### Outcomes

- Distinguish public assets, private responses and cache keys.
- Choose freshness, validation and invalidation strategies.

#### Lessons

1. **CDN placement and cache keys** — `lesson`
2. **HTTP caching, revalidation and purge** — `lesson`
3. **Evaluating edge cache safety** — `test`
4. **Test an invalidation scenario** — `lab`

### Module 3 — Identity, Rate Limits & Abuse

#### Outcomes

- Preserve origin-side authorization despite edge authentication.
- Explain quota policies, burst behavior and client identification risks.

#### Lessons

1. **Authentication boundaries and token forwarding** — `lesson`
2. **Rate limiting, quotas and failure policies** — `lesson`
3. **Analyzing gateway abuse controls** — `test`
4. **Exercise rate controls** — `lab`

### Module 4 — Edge Compute & Operations

#### Outcomes

- Decide when edge execution is worth operational complexity.
- Investigate origin health, connection pooling and incident recovery.

#### Lessons

1. **Edge functions and execution constraints** — `lesson`
2. **Telemetry, health checks and safe rollback** — `lesson`
3. **Choosing edge versus origin** — `test`
4. **Recover from a bad route** — `lab`

### Module 5 — Measured API Gateway & Edge Deployment

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

**Exit demonstration:**

Demonstrate the resulting implementation, explain its key mechanisms, reproduce at least one failure and recovery and defend the chosen trade-offs with inspectable evidence.
