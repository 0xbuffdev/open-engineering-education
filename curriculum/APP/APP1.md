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
8. **Trace name resolution and connection behavior** — `lab`

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

1. **HTTP service contract and framework responsibilities** — `test`
2. **Build the HTTP Service Lab first without a framework, then with a framework** — `lab`

## Completion requirements

- Complete the required practical exercises, knowledge checkpoints, and evaluated labs described in the modules.
- Complete the final integrated `lab` in the last module and satisfy its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, failures investigated, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

**Required practical exercises:**

- inspect a real HTTP exchange
- trace name resolution and distinguish it from an actual DNS packet capture
- compare HTTP methods/status codes
- build a tiny HTTP server
- inspect browser requests with developer tools or explain supplied authentic sanitized browser evidence

**Final integration lab — required work:**

Required artifact: **HTTP Service Lab**.

Build a bounded, loopback-only HTTP service first with standard-library HTTP primitives and then implement the **same published contract** with a freely available learner-selected framework. Both versions must pass one shared acceptance suite covering normal, boundary, invalid and duplicate/retry cases. Record security limits and explain what the framework automates versus what still requires developer reasoning.

**Required module checkpoints and reproducible HTTP labs:**

Each module below has two assessable conceptual questions with expected-answer reasoning and one required practical lab. A reviewer may substitute equivalent unseen situations addressing the same outcomes. Successful completion requires observed request/response or browser/server evidence and a reasoned layer diagnosis; naming the right status or repeating a tutorial is insufficient.

**Shared safe environment and accessibility:**

Use an unprivileged local development environment with Python 3.11+ standard-library socket/http modules, a browser with developer tools (or provided authentic sanitized browser trace when its interface cannot be used), a terminal and synthetic fixtures. Run services on 127.0.0.1 at ephemeral unprivileged ports, document actual OS/interpreter/browser versions and chosen port numbers, and use bounded timeouts and body sizes. A free/open-source framework chosen by the learner is required only for the final framework comparison; document its exact version and repeatable dependency setup. Do not require a paid service, production domain, public network, custom root CA, real user data, privileged port or certificate-validation bypass. No paid service is required for any mandatory exercise or the chosen free/open-source framework. Public-domain DNS/TLS observation may be optional enrichment; mandatory conceptual DNS/TLS evidence can be supplied by sanitized reference traces and must never be presented as locally observed packets.

**Shared assessment and verification rules:**

- Predict the expected request, server effect, response and failure class before each experiment; record what actually happened and compare the two.
- For networking, distinguish a name-resolution result, transport connection, TLS validation, browser policy, HTTP response and business authorization. Do not claim a local plain-HTTP trace proves real TLS identity or wire-level DNS traffic.
- Use isolated local fixture resources. Test normal, empty, boundary, malformed input, duplicate/replay, timeout or refusal cases appropriate to each lab. No credential harvesting, certificate bypass or public server scanning is part of this course.
- Retain local source revisions, exact commands and configurations, raw or sanitized HTTP traces, versions, response/status assertions, one investigated failure and its correction, and a meaningful technical retrospective.
- The final lab compares the same published API implemented both without and with a learner-selected free web framework. A passing green test alone cannot demonstrate independent architectural understanding.

**Module 1 — The Internet & Client/Server Model: checkpoint** — Required assessment details

- **Q1 (free):** A program calls getaddrinfo for localhost and receives 127.0.0.1. Does that prove a DNS query was sent over the network? Why?
  - Expected answer and scoring: No. The host's resolver may use a local hosts file, cache or other configured source before DNS. A name-to-address result is not proof of a network DNS exchange. Capture resolver configuration and distinguish observed packets from inferred resolution.
- **Q2 (free):** A TCP connection to 127.0.0.1 on a closed local port fails, while a hostname lookup succeeds. Which layer failed, and what do the IP address and port designate?
  - Expected answer and scoring: Name resolution succeeded but transport endpoint connection failed. The IP identifies an interface/host and the port identifies a service endpoint in the relevant transport protocol; the client needs both for a TCP connection. No HTTP status is available when no HTTP connection was established.

**Module 1 — Trace name resolution and connection behavior: required lab** — Required assessment details

- **Objective:** Trace client name lookup, addressing and transport behavior using local fixtures and evidence rather than assuming every failure is an HTTP failure.
- **Prerequisites:** Complete this module's lessons and justify the conceptual checkpoint. Reuse earlier module server/client fixtures only after verifying their stated contracts.
- **Environment:** Use an unprivileged local development environment with Python 3.11+ standard-library socket/http modules, a browser with developer tools (or provided authentic sanitized browser trace when its interface cannot be used), a terminal and synthetic fixtures. Run services on 127.0.0.1 at ephemeral unprivileged ports, document actual OS/interpreter/browser versions and chosen port numbers, and use bounded timeouts and body sizes. A free/open-source framework chosen by the learner is required only for the final framework comparison; document its exact version and repeatable dependency setup. Do not require a paid service, production domain, public network, custom root CA, real user data, privileged port or certificate-validation bypass. Public-domain DNS/TLS observation may be optional enrichment; mandatory conceptual DNS/TLS evidence can be supplied by sanitized reference traces and must never be presented as locally observed packets.
- **Procedure:**
  1. Record the OS, Python interpreter and local resolver settings; run a small Python standard-library socket.getaddrinfo inspection for localhost and document that its output is not proof of DNS traffic.
  2. Start a disposable HTTP listener bound to 127.0.0.1 on an ephemeral unprivileged port and record how the selected port is provided to a client.
  3. Connect to the listener through the numeric loopback address and through localhost where supported; compare resolved address families and note that IPv6 localhost may be chosen on some systems.
  4. Stop the listener and retry the same address/port to reproduce a connection-refused or comparable transport error; also inspect an intentionally unresolved test name in a controlled resolver fixture.
  5. Use a provided synthetic DNS answer trace to explain the roles of resolver, recursive query, answer and TTL. An actual public-domain lookup may be optional enrichment but is never mandatory.
  6. Write a fault classification table for resolution failure, refused TCP endpoint, connection timeout (simulated/controlled), and valid HTTP error response.
- **Expected result:** The listener responds only while running, name resolution and TCP failure are separately classified, and the learner explains why localhost resolution does not require a DNS packet.
- **Verification:** Compare the observed address/port and error classes to the recorded socket outputs and fixture data; verify no external host or privileged port was required.
- **Evidence:** Interpreter/OS details, resolver observations, local listener/client command log, mock DNS record, status/error matrix and limitations.
- **Failure analysis:** Explain treating name lookup as a wire-level DNS trace, interpreting connection refusal as HTTP 404 or assuming localhost resolves to only IPv4.
- **Acceptance:** All required observable behaviors, negative cases and layer distinctions match their published contracts under the recorded environment. Inaccurate security claims, missing reproducibility or unexplained unsafe behavior block acceptance.

**Module 2 — HTTP & Web Communication: checkpoint** — Required assessment details

- **Q1 (free):** A GET response has ETag "v1". What should a conforming server do when a later GET sends If-None-Match with the matching validator and the selected representation is unchanged?
  - Expected answer and scoring: For a valid conditional GET with a matching entity tag and no higher-precedence conflicting condition, respond 304 Not Modified with appropriate metadata and no response content; the client can reuse its stored representation. Cache use also depends on Cache-Control and freshness; ETag alone does not make a response cacheable.
- **Q2 (free):** Are POST, PUT and PATCH all automatically safe to retry after a timeout? Distinguish safe and idempotent HTTP method semantics from actual application behavior.
  - Expected answer and scoring: Safe means the requested operation is read-only in its intended semantics (e.g. GET); idempotent means repeated identical requests have the same intended effect (e.g. PUT). POST is not inherently idempotent, and PATCH need not be. Even idempotent operations may emit logs; retries require well-defined failure/duplicate handling and application semantics.

**Module 2 — Inspect methods, caching and redirects: required lab** — Required assessment details

- **Objective:** Predict and verify HTTP request/response semantics, conditional validation, redirection and status interpretation on a controlled local service.
- **Prerequisites:** Complete this module's lessons and justify the conceptual checkpoint. Reuse earlier module server/client fixtures only after verifying their stated contracts.
- **Environment:** Use an unprivileged local development environment with Python 3.11+ standard-library socket/http modules, a browser with developer tools (or provided authentic sanitized browser trace when its interface cannot be used), a terminal and synthetic fixtures. Run services on 127.0.0.1 at ephemeral unprivileged ports, document actual OS/interpreter/browser versions and chosen port numbers, and use bounded timeouts and body sizes. A free/open-source framework chosen by the learner is required only for the final framework comparison; document its exact version and repeatable dependency setup. Do not require a paid service, production domain, public network, custom root CA, real user data, privileged port or certificate-validation bypass. Public-domain DNS/TLS observation may be optional enrichment; mandatory conceptual DNS/TLS evidence can be supplied by sanitized reference traces and must never be presented as locally observed packets.
- **Procedure:**
  1. Implement or reuse a fixture HTTP server supporting GET of a stable JSON resource, a redirect route, a response with a defined ETag and a deliberately invalid route; run it on loopback only.
  2. Capture the method, URL/path, request headers, response status, representation headers and body for ordinary GET, missing resource and a redirect (inspect both the initial and followed request).
  3. Send two GETs: one without conditions, then one with a matching If-None-Match; verify status 200 versus 304 and document any cache metadata separately from the validator.
  4. Test HEAD with the same representation metadata but without response content; compare request/response framing and distinguish a missing body from a failed transport.
  5. Design a tiny in-memory resource fixture for a PUT or POST operation and record what happens on repeated identical requests; distinguish claimed method semantics from proven application idempotence.
  6. Inject an invalid Content-Type or malformed JSON request for a resource-creating route, record an explicit client error and verify no resource was created.
- **Expected result:** Captured HTTP traces match the published routes; matching conditional GET returns 304 without a response body; repeated writes follow the declared endpoint contract and malformed input is rejected.
- **Verification:** Automate status/header/body checks with Python stdlib http.client or urllib and independently inspect one exchange using a browser network panel where available.
- **Evidence:** Local server/client source, request/response transcript, ETag/cache and redirect notes, status assertions and malformed-input tests.
- **Failure analysis:** Explain assuming HTTP status implies network failure, confusing cache validation with freshness, following redirects without observing them, or inferring POST idempotence from one run.
- **Acceptance:** All required observable behaviors, negative cases and layer distinctions match their published contracts under the recorded environment. Inaccurate security claims, missing reproducibility or unexplained unsafe behavior block acceptance.

**Module 3 — Sessions & Secure Transport: checkpoint** — Required assessment details

- **Q1 (free):** A response has Access-Control-Allow-Origin set to an origin not matching the requesting page. Does this prove the API denied access to the endpoint?
  - Expected answer and scoring: No. CORS is primarily a browser-enforced policy controlling whether script can read the response. A request may reach the server and produce an HTTP response even when the browser blocks access to that response; server authorization is a separate check.
- **Q2 (free):** Can a localhost HTTP demo prove that a TLS certificate is trusted, or that Secure cookies would traverse the same insecure connection in production?
  - Expected answer and scoring: No. An HTTP localhost demo can illustrate session/cookie headers and origin rules, but TLS identity and certificate validation require an actual verified TLS connection. Secure and SameSite behavior can be affected by browser restrictions and localhost exceptions; do not use a local HTTP trace to claim verified certificate trust or production cookie protection.

**Module 3 — Inspect TLS, cookies and browser-origin boundaries: required lab** — Required assessment details

- **Objective:** Reason from TLS and cookie evidence without conflating encryption, origin policy and application authorization.
- **Prerequisites:** Complete this module's lessons and justify the conceptual checkpoint. Reuse earlier module server/client fixtures only after verifying their stated contracts.
- **Environment:** Use an unprivileged local development environment with Python 3.11+ standard-library socket/http modules, a browser with developer tools (or provided authentic sanitized browser trace when its interface cannot be used), a terminal and synthetic fixtures. Run services on 127.0.0.1 at ephemeral unprivileged ports, document actual OS/interpreter/browser versions and chosen port numbers, and use bounded timeouts and body sizes. A free/open-source framework chosen by the learner is required only for the final framework comparison; document its exact version and repeatable dependency setup. Do not require a paid service, production domain, public network, custom root CA, real user data, privileged port or certificate-validation bypass. Public-domain DNS/TLS observation may be optional enrichment; mandatory conceptual DNS/TLS evidence can be supplied by sanitized reference traces and must never be presented as locally observed packets.
- **Procedure:**
  1. Study a supplied, sanitized TLS certificate/handshake trace showing hostname, certificate chain, validation decision and negotiated transport state; optionally inspect a real HTTPS site in a browser, but do not require public network access or bypass certificate warnings.
  2. Run a local HTTP service on 127.0.0.1 that issues a synthetic session token through Set-Cookie with documented HttpOnly/SameSite settings. Never embed real credentials in fixtures.
  3. Trace Set-Cookie and a later Cookie header in browser developer tools or an HTTP client, then verify a session-expiry or invalid-session response from the server.
  4. Run a second local origin on a different port and demonstrate that an allowed CORS response permits the browser to read a fixture, while a disallowed origin prevents script access; compare the actual server log/status with the browser console.
  5. Document separately what an HTTPS packet capture normally reveals (encrypted application content) and what the browser network panel shows after TLS processing. Explain the trust boundaries with a diagram.
  6. Test an unauthenticated API path independently of CORS settings and explain why permitting a CORS origin must not grant server authorization.
- **Expected result:** The evidence differentiates TLS endpoint validation, cookie/session state, browser-origin enforcement and server-side authorization; no unsafe certificate bypass or secret exposure is necessary.
- **Verification:** Check session cookie attributes and expiry behavior, controlled origin responses and the supplied TLS chain interpretation against independent expected outcomes.
- **Evidence:** Sanitized handshake reference, local session traces, origin configuration, browser/server observations, authentication-negative case and model-limit note.
- **Failure analysis:** Explain conflating HTTPS with CORS, assuming HttpOnly eliminates CSRF, interpreting a CORS browser error as an HTTP authorization status, or making an unsupported TLS claim.
- **Acceptance:** All required observable behaviors, negative cases and layer distinctions match their published contracts under the recorded environment. Inaccurate security claims, missing reproducibility or unexplained unsafe behavior block acceptance.

**Module 4 — APIs & Resource Design: checkpoint** — Required assessment details

- **Q1 (free):** Why should API error responses distinguish malformed JSON (400), an unauthenticated request (401 when authentication is required), forbidden access (403) and missing resource (404)?
  - Expected answer and scoring: These cases correspond to different client corrections and server policies. A documented API should use status codes consistently with its authentication and resource model, avoiding leakage of hidden resource existence when necessary. A TCP connection succeeding does not determine API authorization.
- **Q2 (free):** An endpoint lists 1000 resources. How would you specify page size and cursor/offset behavior without promising order implicitly?
  - Expected answer and scoring: Define a stable deterministic order, a bounded page-size parameter, cursor/offset encoding and invalid-cursor behavior; document whether results can shift under concurrent updates. Tests should exercise empty, first, last and invalid pages.

**Module 4 — Specify and diagnose a resource API: required lab** — Required assessment details

- **Objective:** Produce an API contract with deterministic validation, pagination and failure behavior that is independently testable.
- **Prerequisites:** Complete this module's lessons and justify the conceptual checkpoint. Reuse earlier module server/client fixtures only after verifying their stated contracts.
- **Environment:** Use an unprivileged local development environment with Python 3.11+ standard-library socket/http modules, a browser with developer tools (or provided authentic sanitized browser trace when its interface cannot be used), a terminal and synthetic fixtures. Run services on 127.0.0.1 at ephemeral unprivileged ports, document actual OS/interpreter/browser versions and chosen port numbers, and use bounded timeouts and body sizes. A free/open-source framework chosen by the learner is required only for the final framework comparison; document its exact version and repeatable dependency setup. Do not require a paid service, production domain, public network, custom root CA, real user data, privileged port or certificate-validation bypass. Public-domain DNS/TLS observation may be optional enrichment; mandatory conceptual DNS/TLS evidence can be supplied by sanitized reference traces and must never be presented as locally observed packets.
- **Procedure:**
  1. Design a synthetic tasks/items resource with explicit JSON schema, ID rules, GET list/detail and POST create operations, including a stable pagination or bounded-limit policy.
  2. Document method/path, request and response examples, status codes, content type, validation errors and a structured error body, including failure for unsupported method and unknown resource.
  3. Implement a minimal loopback stub or tests against a provided test stub. Use synthetic records to check page boundaries, unknown IDs, invalid JSON and duplicate IDs.
  4. Inspect one intentionally failing request and trace the responsibility for its status among HTTP routing, schema validation and domain logic.
  5. Write a compatibility note about adding an optional response field versus deleting or renaming a required field; create a test against the existing client contract.
  6. Have a reviewer use only the specification to predict responses for three unseen requests, then revise any ambiguous contract.
- **Expected result:** The contract and local stub agree on statuses, validated bodies and deterministic pagination, and unseen valid/invalid cases can be evaluated without guessing.
- **Verification:** Run documented HTTP client assertions against fixture data and compare method/path/status/JSON bodies to a contract table.
- **Evidence:** API contract, schema and pagination policy, fixture stub, successful/invalid request logs, compatibility test and reviewer correction.
- **Failure analysis:** Explain exposing stack traces as user-facing errors, ambiguous pagination, accepting malformed records or conflating transport with domain failures.
- **Acceptance:** All required observable behaviors, negative cases and layer distinctions match their published contracts under the recorded environment. Inaccurate security claims, missing reproducibility or unexplained unsafe behavior block acceptance.

**Module 5 — Browser Execution & HTTP APIs: checkpoint** — Required assessment details

- **Q1 (free):** A browser fetch across origins uses Content-Type: application/json on POST. Why can a preflight request occur, and what should the server return?
  - Expected answer and scoring: A cross-origin request with a non-CORS-safelisted content type typically requires an OPTIONS preflight to check the intended method/headers. A successful permitted preflight authorizes the browser to send the actual request but is not server-side authentication or business authorization.
- **Q2 (free):** A credentialed cross-origin browser fetch receives Access-Control-Allow-Origin: * and Access-Control-Allow-Credentials: true. Will the browser expose it to the script?
  - Expected answer and scoring: No. Credentialed CORS access requires a specific matching origin rather than the wildcard, along with appropriate credentials policy; the browser refuses script access with that combination. Cookies may also be blocked by SameSite/Secure or browser policies.

**Module 5 — Trace and repair a browser API interaction: required lab** — Required assessment details

- **Objective:** Observe browser navigation, fetch promises, preflight, and credential handling using a small prepared fixture rather than assuming prior JavaScript expertise.
- **Prerequisites:** Complete this module's lessons and justify the conceptual checkpoint. Reuse earlier module server/client fixtures only after verifying their stated contracts.
- **Environment:** Use an unprivileged local development environment with Python 3.11+ standard-library socket/http modules, a browser with developer tools (or provided authentic sanitized browser trace when its interface cannot be used), a terminal and synthetic fixtures. Run services on 127.0.0.1 at ephemeral unprivileged ports, document actual OS/interpreter/browser versions and chosen port numbers, and use bounded timeouts and body sizes. A free/open-source framework chosen by the learner is required only for the final framework comparison; document its exact version and repeatable dependency setup. Do not require a paid service, production domain, public network, custom root CA, real user data, privileged port or certificate-validation bypass. Public-domain DNS/TLS observation may be optional enrichment; mandatory conceptual DNS/TLS evidence can be supplied by sanitized reference traces and must never be presented as locally observed packets.
- **Procedure:**
  1. Use a supplied minimal HTML/JavaScript page served on one loopback port and a separate JSON API server on another loopback port. Record both origins (scheme, host and port).
  2. Trace page navigation and a simple GET fetch, including request start, asynchronous completion and displayed result; note that failed HTTP status and fetch rejection are not identical.
  3. Trigger a controlled preflight using a cross-origin JSON POST or a custom header and capture OPTIONS and the actual request or its absence.
  4. Seed an incorrect CORS origin/credentials response and reproduce the browser's blocked read while recording the server's actual request/response logs.
  5. Repair configuration for an allowed known origin and validate both a permitted browser request and a disallowed origin, preserving independent server authentication checks.
  6. Exercise a network disconnect or controlled server error and display a user-visible failure without silently assuming the request succeeded.
- **Expected result:** The learner can explain the browser's request and preflight sequence, repair one origin-policy error without weakening authorization, and distinguish HTTP errors from network failures.
- **Verification:** Compare browser console/network traces with API server log and an independent HTTP client for success, CORS blocked and server-failure fixtures.
- **Evidence:** Minimal HTML/JS fixture, two local origins and versions, before/after browser traces, CORS response policy, errors and fix rationale.
- **Failure analysis:** Explain why curl does not enforce browser CORS, why wildcard credentials fails, why POST may preflight, or why an HTTP 500 does not always reject fetch.
- **Acceptance:** All required observable behaviors, negative cases and layer distinctions match their published contracts under the recorded environment. Inaccurate security claims, missing reproducibility or unexplained unsafe behavior block acceptance.

**Module 6 — HTTP Reliability & Intermediaries: checkpoint** — Required assessment details

- **Q1 (free):** A client sends POST to create an item, times out before receiving the response, then retries. How can the service avoid creating two items?
  - Expected answer and scoring: Use a documented idempotency-key contract: recognize repeat requests with the same key and matching payload, return the original operation result or an explicitly documented duplicate outcome, and reject conflicting payload reuse. The storage and expiry scope must be stated; the HTTP method alone does not make POST idempotent.
- **Q2 (free):** A reverse proxy forwards X-Forwarded-For sent by a client. When may an application trust that field?
  - Expected answer and scoring: Only under a deliberately configured trusted-proxy boundary where the edge/proxy strips or controls untrusted forwarding headers; arbitrary client-supplied values are spoofable. Do not use the header as authentication.

**Module 6 — Diagnose retries, duplicate writes and proxy trust: required lab** — Required assessment details

- **Objective:** Demonstrate bounded retries, idempotent write handling, controlled cache behavior and proxy identity boundaries.
- **Prerequisites:** Complete this module's lessons and justify the conceptual checkpoint. Reuse earlier module server/client fixtures only after verifying their stated contracts.
- **Environment:** Use an unprivileged local development environment with Python 3.11+ standard-library socket/http modules, a browser with developer tools (or provided authentic sanitized browser trace when its interface cannot be used), a terminal and synthetic fixtures. Run services on 127.0.0.1 at ephemeral unprivileged ports, document actual OS/interpreter/browser versions and chosen port numbers, and use bounded timeouts and body sizes. A free/open-source framework chosen by the learner is required only for the final framework comparison; document its exact version and repeatable dependency setup. Do not require a paid service, production domain, public network, custom root CA, real user data, privileged port or certificate-validation bypass. Public-domain DNS/TLS observation may be optional enrichment; mandatory conceptual DNS/TLS evidence can be supplied by sanitized reference traces and must never be presented as locally observed packets.
- **Procedure:**
  1. Run a loopback API fixture and a controlled local forwarding proxy or recorded proxy test harness with clear upstream/edge boundaries; keep all endpoints offline.
  2. Create an in-memory POST endpoint with an idempotency-key store and a deterministic response; simulate response delay or drop after the server commits a request.
  3. Retry the same key and payload, verify only one item exists and compare the repeated result; test the same key with a different payload and document conflict behavior.
  4. Run a client with finite timeout and retry budget, and demonstrate why blindly retrying every status or indefinitely waiting is unsafe. Show an explicit no-retry case.
  5. Test ETag/Cache-Control response validation or a stale cached representation and describe the invalidation policy when a resource changes.
  6. Send a forged forwarding header from the untrusted client side, and verify the application does not treat that value as verified identity without a configured trusted proxy.
- **Expected result:** The duplicated POST produces one logical effect, bounded retries stop correctly, cache freshness/validation matches the declared policy, and forwarded identity is not blindly trusted.
- **Verification:** Compare operation count, item IDs, retry timestamps/statuses, cache validators and proxy logs across normal, delayed, duplicate and conflicting fixtures.
- **Evidence:** Service/proxy fixture, retry limits, idempotency test script, cache and header traces, error cases and trust-boundary explanation.
- **Failure analysis:** Explain duplicate side effects, replay of conflicting payloads, infinite retry loops, cache staleness or trusting an attacker-controlled proxy header.
- **Acceptance:** All required observable behaviors, negative cases and layer distinctions match their published contracts under the recorded environment. Inaccurate security claims, missing reproducibility or unexplained unsafe behavior block acceptance.

**Module 7 — Web Threats, Observability & Verification: checkpoint** — Required assessment details

- **Q1 (free):** A browser displays a generic fetch failure but the server logs HTTP 403. Which evidence distinguishes a browser CORS policy block from the server's authorization decision?
  - Expected answer and scoring: Inspect the browser network/console, request origin and CORS response headers alongside server logs and a nonbrowser HTTP client result. The server's 403 records an authorization decision; CORS may separately prevent the browser from reading that response.
- **Q2 (free):** What should a correlation ID help diagnose, and why must a log never include raw session tokens or passwords to make tracing convenient?
  - Expected answer and scoring: A correlation ID links related client/proxy/server events without exposing credentials. Logging secrets increases disclosure risk and is not necessary to connect status, timing and route observations; logs should be appropriately sanitized.

**Module 7 — Investigate a failing web request end to end: required lab** — Required assessment details

- **Objective:** Diagnose request failures across client, origin policy, HTTP, application and transport boundaries using controlled traces and safe logs.
- **Prerequisites:** Complete this module's lessons and justify the conceptual checkpoint. Reuse earlier module server/client fixtures only after verifying their stated contracts.
- **Environment:** Use an unprivileged local development environment with Python 3.11+ standard-library socket/http modules, a browser with developer tools (or provided authentic sanitized browser trace when its interface cannot be used), a terminal and synthetic fixtures. Run services on 127.0.0.1 at ephemeral unprivileged ports, document actual OS/interpreter/browser versions and chosen port numbers, and use bounded timeouts and body sizes. A free/open-source framework chosen by the learner is required only for the final framework comparison; document its exact version and repeatable dependency setup. Do not require a paid service, production domain, public network, custom root CA, real user data, privileged port or certificate-validation bypass. Public-domain DNS/TLS observation may be optional enrichment; mandatory conceptual DNS/TLS evidence can be supplied by sanitized reference traces and must never be presented as locally observed packets.
- **Procedure:**
  1. Use the existing local server and browser/client fixture. Add a request correlation ID to normal logs without recording token values, passwords or private payloads.
  2. Seed one application authorization/session failure and one transport-level failure such as a stopped local listener; reproduce both from clean fixture commands.
  3. Capture browser/client console/status plus server log (or absence of server log), route, timestamp and sanitized correlation ID for each case.
  4. Classify what failed first among name resolution, TCP connection, TLS (from provided evidence only), browser origin policy, HTTP routing and application authorization; avoid inventing observations absent from the trace.
  5. Repair the application authorization regression without changing unrelated CORS settings and add an automated regression test for it.
  6. Write a concise incident report with hypothesis, evidence, confirmed root cause, fix, verification and unresolved limitations.
- **Expected result:** The learner distinguishes a transport failure from a successful HTTP exchange with application rejection, and the accepted fix is verified by a repeatable negative-case test.
- **Verification:** Compare client/server trace IDs and expected error classes, then reproduce the original and repaired fixture outcomes.
- **Evidence:** Fault setup, sanitized client/server logs, layer classification, cause-and-fix report, test run and confidentiality review.
- **Failure analysis:** Explain a misleading generic browser error, diagnosing only from HTTP status, exposing cookies in logs or claiming a root cause unsupported by evidence.
- **Acceptance:** All required observable behaviors, negative cases and layer distinctions match their published contracts under the recorded environment. Inaccurate security claims, missing reproducibility or unexplained unsafe behavior block acceptance.

**Module 8 — HTTP Service: checkpoint** — Required assessment details

- **Q1 (free):** Why is a framework-free service useful for this course if a framework will later be used for the same API?
  - Expected answer and scoring: The manual implementation exposes request parsing/routing, status and header choices, serialization, validation and resource ownership; the framework automates or organizes these tasks but does not remove responsibility for authorization, input correctness, idempotency, caching or tests.
- **Q2 (free):** The framework implementation passes one GET smoke test but a retrying POST creates duplicates. Has it achieved behavioral parity with the first implementation?
  - Expected answer and scoring: No. Equivalence must cover the published API's normal, boundary, invalid-input and retry/idempotency behavior, including persistent state effects and status/error contracts. One successful GET is inadequate.

**Module 8 — Build and defend an HTTP service without and with a framework: required lab** — Required assessment details

- **Objective:** Deliver the same small, bounded HTTP API first with standard-library primitives and then with a free/open-source framework, with measurable contractual parity.
- **Prerequisites:** Complete this module's lessons and justify the conceptual checkpoint. Reuse earlier module server/client fixtures only after verifying their stated contracts.
- **Environment:** Use an unprivileged local development environment with Python 3.11+ standard-library socket/http modules, a browser with developer tools (or provided authentic sanitized browser trace when its interface cannot be used), a terminal and synthetic fixtures. Run services on 127.0.0.1 at ephemeral unprivileged ports, document actual OS/interpreter/browser versions and chosen port numbers, and use bounded timeouts and body sizes. A free/open-source framework chosen by the learner is required only for the final framework comparison; document its exact version and repeatable dependency setup. Do not require a paid service, production domain, public network, custom root CA, real user data, privileged port or certificate-validation bypass. Public-domain DNS/TLS observation may be optional enrichment; mandatory conceptual DNS/TLS evidence can be supplied by sanitized reference traces and must never be presented as locally observed packets.
- **Procedure:**
  1. Publish one concise HTTP contract for a synthetic items resource: GET /health, GET /items, GET /items/{id} and POST /items with explicit JSON fields, status/error schemas, data limits, and a documented repeat-write rule.
  2. Build a first version using Python 3.11+ standard-library HTTP handling on 127.0.0.1 with an ephemeral port; explicitly bound request-body sizes, parse JSON carefully, and reject unknown paths/methods/invalid input without uncontrolled exceptions.
  3. Write an independent client contract suite using standard-library HTTP tools covering normal creation/list/detail, empty collection, missing ID, malformed JSON, oversized payload, duplicate ID/idempotency behavior, repeated read and an intentional server error.
  4. Reimplement the same routes and behaviors using a chosen free/open-source web framework; record the framework and version, installation source and a reproducible local dependency setup. No paid platform or particular provider is mandatory.
  5. Run the **same** acceptance suite against both implementations and compare status codes, response schemas, state changes and relevant headers. Record and explain differences instead of claiming automatic equivalence.
  6. Demonstrate a controlled browser request and origin-policy failure where supported, plus a conditional read or bounded retry/idempotency scenario, reusing prior module fixtures or clear equivalents.
  7. Document what the framework handles and what application code still must handle, including validation, authorization policy, error mapping, logs, resource limits and trust boundaries.
  8. From a clean checkout, reproduce both servers and tests, include a design review and a technical retrospective identifying a failed assumption and verified correction.
- **Expected result:** The unframed and framed services both satisfy the documented API acceptance suite on loopback; malformed/replayed input yields bounded predictable results, and differences and limitations are disclosed.
- **Verification:** Run the exact contract test suite against both implementations and inspect representative raw HTTP traces and independent reviewer setup.
- **Evidence:** Versioned implementations, framework/dependency setup, shared tests, status/body/header comparison, browser and failure traces, README, review, and retrospective.
- **Failure analysis:** Explain assuming framework routing implies secure validation, hiding exceptions as status 200, uncontrolled request size or state divergence across implementations.
- **Acceptance:** All required observable behaviors, negative cases and layer distinctions match their published contracts under the recorded environment. Inaccurate security claims, missing reproducibility or unexplained unsafe behavior block acceptance.

**Exit demonstration:**

The learner can explain what happens from entering a URL to receiving a rendered response and can diagnose common request/response failures.

---
