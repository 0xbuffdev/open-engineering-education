# APP1 — Web & Internet Foundations

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [SEF10](../SEF/SEF10.md) — Software Engineering Foundations
**Duration:** 7 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Understand the network and web foundations that modern application software depends on, then use that knowledge to build and investigate HTTP services.

## Learning outcomes

By the end of this course, the learner will be able to:

- Explain the client/server model and the roles of DNS, IP, ports, HTTP, and TLS in a web request.
- Read and reason about HTTP requests, responses, headers, methods, status codes, cookies, and sessions.
- Inspect browser and network behavior using appropriate development tools.
- Design a simple resource-oriented API and distinguish application concerns from transport concerns.
- Build and test a small HTTP service and explain what a web framework abstracts away.
- Diagnose browser/network failures by distinguishing DNS, transport, TLS, origin policy, HTTP and application-level causes.
- Implement safe HTTP caching, retry and idempotency behavior and explain why those controls affect service correctness.
- Trace browser fetch execution and investigate a web trust-boundary fault using reproducible client/server evidence.

## Modules

### Module 1 — The Internet & Client/Server Model

#### Outcomes

- Explain **Networks, IP addresses, ports, and clients/servers** in the context of the course.
- Apply **DNS and name resolution** in a problem, implementation, experiment, or design decision.

- Trace a client request across addressing, transport, and name resolution, explaining observed latency and failure points.

#### Lessons

1. **Course introduction: Web & Internet Foundations** — `lesson`

   Understand the network and web foundations that modern application software depends on, then use that knowledge to build and investigate HTTP services.
2. **Networks, IP addresses, ports, and clients/servers** — `lesson`
3. **DNS and name resolution** — `lesson`
4. **Packet switching, latency, throughput, and loss** — `lesson`
5. **TCP connections, UDP datagrams, and socket endpoints** — `lesson`
6. **Addressing, routing, and basic network diagnostics** — `lesson`
7. **Internet fundamentals** — `test`
8. **Trace DNS resolution for a real domain and record each step** — `lab`

### Module 2 — HTTP & Web Communication

#### Outcomes

- Explain **HTTP requests, responses, methods, and status codes** in the context of the course.
- Apply **URLs, headers, JSON, and serialization** in a problem, implementation, experiment, or design decision.

- Predict and verify HTTP request behavior under caching, redirection, representation selection, and repeated requests.

#### Lessons

1. **HTTP requests, responses, methods, and status codes** — `lesson`
2. **URLs, headers, JSON, and serialization** — `lesson`
3. **HTTP semantics, safe and idempotent methods** — `lesson`
4. **Representation metadata, content negotiation, and compression** — `lesson`
5. **Conditional requests, ETags, cache-control, and redirects** — `lesson`
6. **HTTP reasoning** — `test`
7. **Inspect a real browser request and reconstruct its request/response pair** — `lab`

### Module 3 — Sessions & Secure Transport

#### Outcomes

- Explain **Cookies, sessions, and state** in the context of the course.
- Apply **TLS and secure transport concepts** in a problem, implementation, experiment, or design decision.

- Demonstrate where confidentiality, identity, and browser-origin restrictions apply and where they do not.

#### Lessons

1. **Cookies, sessions, and state** — `lesson`
2. **TLS and secure transport concepts** — `lesson`
3. **TLS certificate chains, hostname validation, and trust** — `lesson`
4. **Cookie attributes, session expiry, and server-side session state** — `lesson`
5. **Same-origin policy, CORS, CSRF, and browser credential handling** — `lesson`
6. **sessions and transport security** — `test`
7. **Inspect which parts of a browser connection are visible before and after TLS** — `lab`

### Module 4 — APIs & Resource Design

#### Outcomes

- Explain **Resource-oriented API design** in the context of the course.
- Apply **Inspecting application traffic with browser/network tools** in a problem, implementation, experiment, or design decision.

- Design an API that states resource and error semantics and remains predictable under invalid or repeated requests.

#### Lessons

1. **Resource-oriented API design** — `lesson`
2. **Inspecting application traffic with browser/network tools** — `lesson`
3. **API contracts, schemas, and structured error responses** — `lesson`
4. **Pagination, filtering, and resource identity** — `lesson`
5. **Backward compatibility, versioning, and developer documentation** — `lesson`
6. **API design** — `test`
7. **Use developer tools to diagnose a failing API request** — `lab`

### Module 5 — Browser Execution & HTTP APIs

#### Outcomes

- Explain how navigation, fetch requests and browser security policies determine observable network activity.
- Implement and diagnose credentialed and uncredentialed browser requests with explicit error handling.

#### Lessons

1. **Navigation and document loading lifecycle** — `lesson`
2. **Fetch API, promises, and asynchronous failure** — `lesson`
3. **Credentials, preflight requests, and browser-origin boundaries** — `lesson`
4. **Streams and progressive response handling** — `lesson`
5. **Browser request lifecycle and policy reasoning** — `test`
6. **Trace and repair a browser API interaction** — `lab`

### Module 6 — HTTP Reliability & Intermediaries

#### Outcomes

- Explain how intermediaries and retries affect correctness and identity in an HTTP service.
- Choose timeout, retry, caching, and duplicate-handling policies for a concrete API workflow.

#### Lessons

1. **Timeouts, cancellation, and retries with jitter** — `lesson`
2. **Idempotency keys and duplicate operation protection** — `lesson`
3. **Reverse proxies, forwarded headers, and trust boundaries** — `lesson`
4. **Response caching, expiration, and invalidation** — `lesson`
5. **Retries, caches, and proxy correctness** — `test`
6. **Diagnose repeated requests through a proxy** — `lab`

### Module 7 — Web Threats, Observability & Verification

#### Outcomes

- Create a lightweight threat model and relate its assumptions to tests and operating controls.
- Reproduce a web communication failure from client and server evidence without guessing.

#### Lessons

1. **Browser and API trust boundaries** — `lesson`
2. **Request logging and correlation identifiers** — `lesson`
3. **Web threat modeling and misuse cases** — `lesson`
4. **Network diagnostics and minimal reproducible reports** — `lesson`
5. **Web threat modeling and diagnostic reasoning** — `test`
6. **Investigate a failing web request end to end** — `lab`

### Module 8 — HTTP Service

#### Outcomes

- Complete and explain the HTTP Service lab, demonstrating the applicable course outcomes and retaining required evidence.

#### Lessons

1. **Build the HTTP Service Lab first without a framework, then with a framework** — `lab`

## Completion requirements

- Complete the required practical exercises, knowledge checkpoints, and evaluated labs described in the modules.
- Complete the final integrated `lab` in the last module and satisfy its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, failures investigated, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required practical exercises:**

- inspect a real HTTP exchange
- trace DNS resolution
- compare HTTP methods/status codes
- build a tiny HTTP server
- inspect browser requests with developer tools
**Final integration lab — required work:**

Required artifact: **HTTP Service Lab**.

Build a small HTTP service without a framework first, then implement the same API with the learner's chosen web framework. Document what the framework provides and what remains the developer's responsibility.

**Expanded module assessments and practical work:**

- **Module 1 checkpoint and micro-lab:** Identify the resolved address and port, distinguish name-resolution failures from connection failures, and support a network diagnosis with a recorded trace.
- **Module 2 checkpoint and micro-lab:** Compare GET, POST, PUT and PATCH under replay; demonstrate a conditional 304 response and interpret headers without confusing transport and application errors.
- **Module 3 checkpoint and micro-lab:** Inspect secure cookie attributes and certificate validation, separate CORS from authentication, and explain a safe cross-origin request policy.
- **Module 4 checkpoint and micro-lab:** Produce a minimal HTTP contract with representative success and failure cases, schema checks, and explicit pagination behavior.

- **Module 5 — Browser Execution & HTTP APIs (Trace and repair a browser API interaction):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Instrument a browser-to-service request, reproduce a cross-origin or credential failure, and correct the client/server configuration without weakening authorization.
  - Verification: Show the failing and repaired network traces and explain the relevant response headers and credential flow.
  - Evidence: Browser trace, minimal reproduction, request/response samples, and a security decision note.
  - Failure analysis: Distinguish browser-enforced CORS rejection from server authorization failure, DNS failure, and TLS failure.
- **Module 6 — HTTP Reliability & Intermediaries (Diagnose repeated requests through a proxy):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Place a simple API behind a local proxy, inject latency and repeated requests, and enforce a bounded retry and idempotency policy.
  - Verification: Demonstrate that retries stop at the configured boundary, a repeated write is safe, and proxy-provided identity is not blindly trusted.
  - Evidence: Configuration, traces, repeatability script, and before/after error counts.
  - Failure analysis: Explain duplicate side effects, retry storms, stale cached responses, and spoofed forwarding headers.
- **Module 7 — Web Threats, Observability & Verification (Investigate a failing web request end to end):**
  - Prerequisites: Complete the module lessons and explain its stated outcomes.
  - Environment: A controlled local application or service, with tool versions and test data documented.
  - Required work: Seed one authorization or session failure and one transport-level fault; identify the responsible layer using browser and server evidence.
  - Verification: Provide distinct root-cause explanations and automated checks preventing the application-layer regression.
  - Evidence: Fault injection steps, trace/correlation IDs, negative-path tests, and short report.
  - Failure analysis: Describe why a successful HTTP connection does not imply authorization or reliable application state.

**Exit assessment expectation:**

Demonstrate the course outcomes through a new scenario, including at least one negative path and independently reproducible evidence. Checkpoint answers must explain the mechanism and not merely name a tool. The final integration lab must incorporate and verify the expanded material.

**Exit demonstration:**

The learner can explain what happens from entering a URL to receiving a rendered response and can diagnose common request/response failures.

---
