# APP1 — Web & Internet Foundations

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [SEF10](../SEF/SEF10.md) — Software Engineering Foundations
**Duration:** 12–16 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Understand the mechanisms that make a website reachable, trustworthy as
a connection, and visible in a browser. Start with connected devices,
Internet packets, routing, transport, naming, hosting, and HTTP; continue
through TLS, browser processes, resource discovery, HTML/CSS parsing,
layout, paint, and composition. Finish by diagnosing unfamiliar failures
using observable evidence rather than assumptions or memorized labels.

This is **one connected introductory capability**: trace a Web
navigation from a device to visible pixels and identify where it can
fail. The modules divide that journey into coherent learning stages;
they are not separate specialist courses.

APP1 teaches *how* the Internet and Web work, **not** the systematic
authoring of HTML/CSS, JavaScript or TypeScript programming, React,
backend services, authentication implementation, databases, production
network operations, or browser-engine internals. Those belong to
subsequent courses. Learners may inspect or minimally edit static
HTML/CSS fixtures to observe browser behavior, but need not write
a backend HTTP server, dynamic application, or framework code.

All mandatory work can be completed using a standards-capable browser,
developer tools, local static-file serving on loopback, and supplied
synthetic or sanitized reference traces. Concepts that cannot be
honestly observed in a local offline environment, such as public DNS
delegation and TLS certificate validation, must be evaluated using
**explicitly labeled synthetic evidence**. No paid service, public
domain, hosted account, custom trust root, packet interception,
administrator access, or external network is required.

The 12–16-week duration is a revised **draft planning estimate**,
not a rigid learner pace or evidence of course validation. Focused
lessons develop one primary objective; practical investigations and
summative assessments are assigned where they actually measure a
course capability.

## Learning outcomes

- **APP1-O1:** Distinguish Internet infrastructure, the World Wide Web, browsers, resources, clients, servers, and intermediaries, and explain their responsibilities in a complete website visit.
- **APP1-O2:** Trace local connectivity, IPv4/IPv6 addressing, packet forwarding, routing, and observable network failure boundaries using appropriately qualified evidence.
- **APP1-O3:** Explain ports, TCP connection and stream behavior, UDP datagrams, QUIC fundamentals, and the relationship between transport and HTTP versions.
- **APP1-O4:** Trace domain registration, DNS delegation and resolution through resolvers and caches, interpreting record types, TTLs, and common failure responses.
- **APP1-O5:** Distinguish domain names, hosted content, origin servers, reverse proxies, CDNs, load balancers, and distributed content-delivery paths.
- **APP1-O6:** Parse and resolve URLs and explain schemes, authority, ports, paths, queries, fragments, browser origins, and the distinction between origin and site.
- **APP1-O7:** Interpret HTTP messages, request methods, response codes, representation headers, redirects, caching, validators, and the behavior of intermediaries.
- **APP1-O8:** Explain HTTPS and TLS negotiation, certificate-chain and hostname validation, protocol selection, mixed-content behavior, and the limits of connection trust.
- **APP1-O9:** Compare browser, renderer, networking, graphics, and JavaScript-engine responsibilities, including process isolation and implementation differences.
- **APP1-O10:** Trace navigation and incremental document/resource loading, identifying blocking and deferred resources and interpreting browser network waterfalls.
- **APP1-O11:** Explain HTML parsing, DOM creation, CSS parsing, selector matching, the cascade, computed styles, and the distinction between document and accessibility representations.
- **APP1-O12:** Trace the visible rendering pipeline through style resolution, layout, paint, rasterization, and compositing, diagnosing representative delays or visual changes.
- **APP1-O13:** Classify same-origin and CORS boundaries, cookies, browser storage and caching, secure contexts, mixed content, permissions, and relevant privacy risks.
- **APP1-O14:** Investigate an unfamiliar static website's network-to-pixels behavior, reproduce and classify failures, apply safe repairs, and defend observed versus inferred evidence.

## Modules

### Module 1 — Internet and Web

#### Outcomes

- APP1-O1

#### Lessons

1. **Internet, Web and Historical Context** — Distinguish packet networking from the Web built on top of it; relate open protocol development to their distinct roles.
2. **Resources, Documents and Websites** — Classify a document, its assets, a website and an application from an unfamiliar navigation without conflating their identities.
3. **Clients, Servers and Interoperability** — Identify requester, origin, intermediary and standards responsibilities in an exchange, noting browser differences.
4. **A First Network-to-Pixels Trace** — Sketch the provisional device-to-visible-page journey and mark unobserved steps rather than guessing.

### Module 2 — Connectivity and Routing

#### Outcomes

- APP1-O2
- APP1-O1

#### Lessons

1. **Interfaces, Local Networks and Gateways** — Locate wireless/Ethernet interfaces, switches, local peers and gateways; distinguish link reachability from Internet reachability.
2. **Host Address Configuration** — Interpret DHCP, host addresses, default gateways and possible NAT without assuming all networks use NAT.
3. **Internet Access and Upstream Networks** — Trace access-network and ISP responsibilities, stating what a local observation cannot establish.
4. **Frames and Packets** — Distinguish link-layer framing from IP datagrams and explain what changes across a routed hop.
5. **IPv4 Addressing and Prefix Decisions** — Use a supplied address and route prefix to predict local versus next-hop delivery.
6. **IPv6 Addressing and Prefix Decisions** — Interpret IPv6 addresses/prefixes and compare forwarding without copying IPv4 NAT assumptions.
7. **Routing and Hop Limits** — Trace route selection and next hops; separate forwarding evidence from application success.
8. **Network Measurements and Their Limits** — Distinguish latency, throughput, bandwidth, jitter and loss without making unsupported causal claims.
9. **Connectivity Failure Investigation** — Classify link, gateway, routing, ICMP and upstream symptoms; select a safe next observation when evidence is inconclusive.

### Module 3 — Transport and Connections

#### Outcomes

- APP1-O3
- APP1-O2

#### Lessons

1. **Ports and Sockets** — Relate transport endpoints and listeners to IP addressing.
2. **TCP Handshakes** — Trace a connection attempt at a conceptual level.
3. **TCP Streams** — Explain ordering, retransmission, and why an application must define message boundaries.
4. **Connection Failures** — Distinguish refusal, reset, timeout, and the limitations of each observation.
5. **UDP Datagrams** — Compare datagram delivery with TCP's reliable stream semantics.
6. **QUIC and HTTP/3** — Explain why QUIC uses UDP while providing transport features to HTTP/3.
7. **Connection Reuse** — Relate latency, multiplexing, and protocol choices without treating them as identical.
8. **Loopback and Dual Stack** — Explain local listener tests and IPv4/IPv6 address-family differences.

### Module 4 — Domain Names and DNS

#### Outcomes

- APP1-O4
- APP1-O5

#### Lessons

1. **DNS Names and Hierarchy** — Explain labels, subdomains, the root, TLDs and delegated zones as a namespace rather than a hosting directory.
2. **Registration and Delegated Authority** — Trace registrant, registrar, registry and nameserver responsibilities, including expiry; separate ownership from hosting.
3. **Resource Records and Authorities** — Interpret A, AAAA, CNAME, NS and MX roles, distinguishing authoritative information from cached answers.
4. **From Stub to Recursive Resolution** — Trace stub, recursive and authoritative roles, referrals and answers; identify an already-cached response.
5. **Positive, Negative and Local Caching** — Interpret TTLs, negative caches, stale observations and hosts-file overrides through a supplied timeline.
6. **Failure Evidence and Classification** — Distinguish NXDOMAIN, SERVFAIL and timeouts without inventing hidden resolver behavior.
7. **DNS Observation and Privacy Limits** — Explain what local/browser resolution, encrypted DNS and synthetic traces do and do not establish.

### Module 5 — Hosting and Delivery

#### Outcomes

- APP1-O5
- APP1-O1

#### Lessons

1. **Hosting Responsibilities and Content Models** — Compare static/dynamic delivery across shared, VM, managed and serverless hosting; distinguish hosting from naming.
2. **Origin Servers** — Trace a listening HTTP origin to the resource it serves without assuming a web framework.
3. **Reverse Proxies and Visibility** — Locate a proxy on the request path and identify which origin details browser inspection cannot prove.
4. **CDN Edges and Caching** — Explain geographically distributed delivery and when a response may not reach the origin.
5. **Load Balancing** — Trace instance selection and identify what load balancing alone cannot guarantee about correctness or availability.
6. **Delivery Path Comparison** — Compare two supplied paths and distinguish DNS answer, origin identity, intermediary response and actual serving location.

### Module 6 — URLs and Origins

#### Outcomes

- APP1-O6
- APP1-O13

#### Lessons

1. **URL Identity and Components** — Parse scheme, authority, host, port, path, query and fragment and explain why a URL does not guarantee availability.
2. **Relative Reference Resolution** — Resolve references against a declared base; correct a mistaken path-only interpretation.
3. **Encoding and Internationalized Names** — Identify percent-encoding and Unicode-name interpretation hazards.
4. **Tuple Origins** — Compare scheme/host/port origin tuples, changing one component at a time.
5. **Sites versus Origins** — Distinguish registrable-site relationships, subdomains and same-origin comparisons.
6. **Navigation and Fragment Targets** — Predict request consequences of path, query, redirects and fragments; identify fragment-only nonfetches.

### Module 7 — HTTP Semantics, Redirects and Caching

#### Outcomes

- APP1-O7
- APP1-O6

#### Lessons

1. **HTTP Exchanges and Message Anatomy** — Interpret request targets, fields, bodies and representation metadata in a supplied exchange.
2. **Methods, Safety and Idempotence** — Predict GET, HEAD, POST, PUT, PATCH and DELETE intent; distinguish protocol properties from retry guarantees.
3. **Response Status and Redirect Semantics** — Interpret success, errors and Location redirects, including possible method changes.
4. **Representations and Negotiation** — Compare Content-Type, negotiation, compression and body constraints for differing representations.
5. **Target Authority and Intermediary Fields** — Distinguish request authority from untrusted forwarded claims.
6. **HTTP Versions and Transport** — Compare shared semantics with HTTP/1.1, HTTP/2 and HTTP/3 framing and multiplexing.
7. **Caches and Storage Scopes** — Separate browser/private and shared HTTP caches from application storage.
8. **Freshness and Reuse** — Apply Cache-Control, freshness lifetime, no-store and private to a trace.
9. **Validators and Revalidation** — Trace ETag, Last-Modified, conditional requests and 304 without inventing a response body.
10. **Variants and Cache Keys** — Interpret Vary and representation selection for requests to one URL.
11. **What a Waterfall Proves** — Distinguish cache hits, forwarded requests and origin observation; correct an unsupported origin-contact claim.

### Module 8 — HTTPS and TLS

#### Outcomes

- APP1-O8
- APP1-O13

#### Lessons

1. **HTTPS Guarantees** — Explain protected transport and the risks of plaintext HTTP.
2. **TLS Handshake** — Describe negotiated cryptography and authenticated key establishment conceptually.
3. **Certificate Chains and Hostname Identity** — Explain trust anchors, issuers, and certificate validation; relate requested host identity to a certificate without equating it to content honesty.
4. **Protocol Negotiation** — Explain SNI and ALPN at an appropriate introductory level.
5. **TLS and QUIC** — Distinguish TLS use with TCP-based HTTPS and HTTP/3 over QUIC.
6. **Mixed Content** — Explain security warnings, downgrade risks, and secure-context boundaries.
7. **Trust Failures** — Classify supplied certificate/hostname errors without bypassing browser validation.

### Module 9 — Browser Architecture

#### Outcomes

- APP1-O9
- APP1-O13

#### Lessons

1. **Browser Responsibilities** — Identify UI, navigation, networking, rendering, and device interaction roles.
2. **Browser Processes** — Explain conceptual process separation, threads, and sandbox boundaries.
3. **Rendering Engines** — Distinguish Blink, Gecko, and WebKit as engine implementations.
4. **JavaScript Engines** — Distinguish V8, SpiderMonkey, and JavaScriptCore from layout/rendering engines.
5. **Engine Variations** — Explain how shared standards coexist with implementation differences.
6. **Site Isolation** — Explain why browsers isolate potentially untrusted content.
7. **Browser Inspection** — Relate developer-tool observations to engine behavior without unsupported generalization.

### Module 10 — Navigation and Resource Loading

#### Outcomes

- APP1-O10
- APP1-O7
- APP1-O9

#### Lessons

1. **Navigation and Connection Reuse** — Trace history decisions, redirects and reused connections; distinguish navigation commitment from prior network steps.
2. **Incremental Document Streaming** — Explain how arriving bytes can lead to progressive parsing before full response completion.
3. **Resource Discovery** — Trace stylesheet, script, image and font requests through a supplied document.
4. **Preload and Priority** — Contrast speculative discovery and observed resource scheduling without presuming one browser algorithm.
5. **Blocking Behavior** — Distinguish parser-blocking scripts, async/deferred execution and render-blocking styles with a fixture.
6. **Readiness Milestones** — Compare load events, first paint and interactive readiness without equating them.
7. **Waterfall Investigation** — Interpret timing, cache, reuse and failure indicators; identify evidence missing from a delay diagnosis.

### Module 11 — HTML and CSS Parsing

#### Outcomes

- APP1-O11
- APP1-O10

#### Lessons

1. **HTML Decoding and Tree Building** — Trace bytes, tokens and DOM construction, including a recoverable malformed-markup case.
2. **Source, DOM and Accessibility Models** — Compare source bytes, document nodes and accessibility representations without authoring a full interface.
3. **CSS Parsing and Selector Matching** — Trace a rule through parser recovery and element matching.
4. **Cascade and Inheritance** — Resolve competing declarations and inheritance to predict displayed values.
5. **Computed Styles and CSSOM** — Inspect computed values versus authored rules and document nodes.
6. **Parser and Style Failure Investigation** — Contrast an invalid declaration, unmatched selector and HTML recovery; select a discriminating observation.

### Module 12 — Layout to Pixels

#### Outcomes

- APP1-O12
- APP1-O11

#### Lessons

1. **Rendered Boxes** — Distinguish the box/render representation from DOM nodes.
2. **Layout Constraints** — Explain geometry, containing blocks, and basic formatting context.
3. **Text and Viewports** — Relate font metrics and viewport changes to layout results.
4. **Paint Order** — Explain painting instructions, stacking, and visible order.
5. **Rasterization** — Explain conversion of paint operations into pixels.
6. **Compositing** — Explain compositing layers and conceptual GPU responsibilities.
7. **Incremental Rendering** — Describe what changes can require style, layout, paint, or compositing work.
8. **Visual Diagnostics** — Identify layout shifts, missing styles, and delayed paint using controlled comparisons.

### Module 13 — Security, State and Privacy

#### Outcomes

- APP1-O13
- APP1-O6
- APP1-O8

#### Lessons

1. **Same-Origin and CORS Decisions** — Classify browser read boundaries without confusing them with transport delivery or bypasses.
2. **Cookies and Session Identifiers** — Explain cookie scope, transport and conceptual session state without backend implementation.
3. **Storage versus HTTP Caching** — Contrast local storage, HTTP caches and service-worker-controlled resources.
4. **Trustworthy Contexts and Permissions** — Apply earlier TLS and mixed-content understanding to secure-context and permission scenarios without repeating TLS.
5. **Threat and Privacy Boundaries** — Recognize CSRF, untrusted content, credential exposure and sensitive observation data at a foundation level.
6. **Security Symptom Diagnosis** — Distinguish TLS, CORS, HTTP, storage and permission failures using labeled evidence.

### Module 14 — End-to-End Diagnosis

#### Outcomes

- APP1-O14
- APP1-O1
- APP1-O2
- APP1-O4
- APP1-O7
- APP1-O8
- APP1-O10
- APP1-O12
- APP1-O13

#### Lessons

1. **Healthy Navigation and Controls** — Reproduce a static local site and fragment-only navigation; separate loopback evidence from public DNS/TLS claims.
2. **Layered Fault Investigation** — Classify controlled connection, missing-resource, visual and labeled synthetic failures with evidence provenance.
3. **Repair and Re-observation** — Repair bounded local faults and verify changed behavior using the same observation conditions.
4. **Integrated Technical Defense** — Explain the supported network-to-pixels causal chain, uncertainties and safe next inspections.

## Completion requirements

All 14 course outcomes MUST be demonstrated against the public criteria
through **four required summative assessments**. These replace the
17 repeated module checkpoint/lab pairs. Formative sketches, small
practice traces, simulator exercises, and lesson self-checks are not
additional completion requirements.

| Assessment | Outcomes covered | Principal evidence |
| --- | --- | --- |
| `APP1-AS1` — Network and DNS Investigation | APP1-O1, APP1-O2, APP1-O3, APP1-O4 | Qualified packet/route and connection traces, domain/DNS explanation |
| `APP1-AS2` — Web Delivery Investigation | APP1-O5, APP1-O6, APP1-O7, APP1-O8 | Hosting/URL diagrams, HTTP/cache traces, synthetic TLS evaluation |
| `APP1-AS3` — Browser Pipeline Investigation | APP1-O9, APP1-O10, APP1-O11, APP1-O12, APP1-O13 | Browser process model, waterfall, DOM/style/render observations, security classifications |
| `APP1-AS4` — Website Diagnostic Defense | APP1-O14, APP1-O1, APP1-O2, APP1-O4, APP1-O7, APP1-O8, APP1-O10, APP1-O12, APP1-O13 | Reproducible static-site failure matrix, repairs, full browser journey, defense |

One assessment may establish several outcomes, and the final
investigation intentionally integrates outcomes where doing so
is educationally necessary. A completed checklist, guessed
layer diagnosis, copied answer, or invented network capture
does not establish competence.

### Shared environment and observation rules

A current Chromium- or Firefox-family browser with developer
tools, a terminal, and a local static fixture are sufficient.
An example unprivileged fixture command is
`python3 -m http.server 8000 --bind 127.0.0.1` from a
disposable directory. A different installed static file server
is acceptable. Do not ask the learner to implement a backend
server or write JavaScript or TypeScript. Static HTML/CSS edits
for observational purposes are allowed but not assessed as
general frontend authoring capability.

Use sanitized public examples, fictitious domains, supplied
packet/route diagrams and DNS/TLS traces as appropriate.
**Label synthetic evidence as synthetic.** A `127.0.0.1`
request does not demonstrate public Internet routing, public
DNS delegation, a real TLS handshake, or a CDN. A browser's
cached response does not prove that an origin was contacted.
Observation limits and missing evidence must be explicitly
identified.

Do not require paid hosting, domain registration, online
certificate testing, login, custom root certificates, network
interception, scanning unfamiliar hosts, administrator or
privileged access, third-party traffic capture, or changing
operating-system trust settings. Avoid logging secrets,
tokens, cookies, private browsing history, and unrelated
user data. Browser and OS versions and actual commands
should be recorded when materially relevant.

### Required assessments

- **APP1-AS1** (required network and naming investigation)
  - Outcomes: APP1-O1, APP1-O2, APP1-O3, APP1-O4
  - Work: reconstruct a complete Web reachability path using
    supplied, labeled local-link, IPv4/IPv6 prefix/route,
    transport, and DNS scenario records. Identify the device,
    interface, gateway, possible NAT, IP next hops, transport
    endpoint and connection stage. Trace a domain from
    registrant/registrar/registry and delegated nameservers
    through stub/recursive/authoritative resolution, common
    records, and positive/negative caching. Compare at least
    four controlled observations representing a link/gateway
    problem, routing failure, connection refusal or timeout,
    and NXDOMAIN/SERVFAIL response. Explain differences
    among TCP, UDP, and QUIC and the limits of traceroute
    and local resolver inspection.
  - Criteria: correct separation of Internet versus Web,
    links versus packet routing, transport versus DNS;
    sensible prefix/next-hop reasoning for IPv4 and IPv6;
    correctly interpreted refused, reset and timeout
    signals; accurate domain roles, record/caching behavior,
    and distinct DNS failures. Every conclusion distinguishes
    observed trace content from hypotheses; no simulated
    scenario is claimed as live capture.
  - Evidence: annotated network-layer diagrams, route and
    endpoint tables, DNS delegation/resolution chain,
    supplied or sanitized failure traces, concise
    failure-classification rationale, and the provenance
    and limitations of each observation.

- **APP1-AS2** (required address, delivery, HTTP and TLS investigation)
  - Outcomes: APP1-O5, APP1-O6, APP1-O7, APP1-O8
  - Work: interpret a supplied multi-stage resource
    delivery scenario involving domain resolution,
    origin/hosting, reverse proxy or CDN, absolute
    and relative URLs, and differing origins/sites.
    Explain the request/response meaning of GET, HEAD,
    POST and other common methods without implementing
    mutating endpoints. Examine ordinary, redirect,
    HTTP error, cache hit and conditional validation
    cases, including ETag or Last-Modified and
    `304 Not Modified`. Interpret an explicitly
    synthetic HTTPS handshake and certificate
    hostname/trust-path outcome; compare successful,
    expired/unknown-issuer, and hostname-mismatch
    cases without disabling validation. Explain
    intermediary visibility, HTTP version framing
    differences, and mixed-content limits.
  - Criteria: correct URL decomposition, reference
    resolution, scheme/host/port origin reasoning,
    distinction between domain and hosting and
    proxy/CDN roles; accurate method/status/header
    and freshness/validation interpretation.
    A 304 is not described as a complete new
    response body, and no cache claim exceeds
    observed evidence. TLS proves appropriate
    connection properties, not that a site's content
    is honest or safe.
  - Evidence: annotated URL/origin table, delivery
    topology and request timeline, HTTP message and
    conditional-cache trace explanations, explicitly
    synthetic TLS/hostname case analysis, and
    short accounts of assumptions and uncertainty.

- **APP1-AS3** (required browser navigation and rendering investigation)
  - Outcomes: APP1-O9, APP1-O10, APP1-O11, APP1-O12, APP1-O13
  - Work: inspect a supplied or locally served static
    site with HTML, CSS, and at least one image.
    Use browser tools to identify navigation and
    resource requests, parser/render blocking,
    resource failure, DOM versus source structure,
    CSS parsing/cascade/computed-style effects,
    layout/paint/composition boundaries, and
    a controlled layout or style change. Distinguish
    the roles of browser processes, rendering
    engines and JavaScript engines (including
    differences among named implementations).
    Classify supplied same-origin/CORS, cookie
    and storage, mixed-content, secure-context
    and privacy scenarios without implementing
    authentication or cross-origin bypasses.
  - Criteria: accurate sequencing from document
    navigation through resource loading and visible
    output; credible browser architecture comparison
    without assuming uniform internal processes;
    correct distinctions among DOM, CSSOM, computed
    style, rendered boxes, layout, paint and
    compositing; justified effects of style/
    viewport changes. Origin/CORS and storage
    classifications must not confuse transport
    failures or cache with application state.
  - Evidence: annotated browser waterfall, resource
    dependency graph, DOM/style inspection and
    screenshots or synthetic equivalents,
    before/after render observations, browser
    architecture sketch, a security/state
    classification matrix, tool versions and
    clear limits on inferred behavior.

- **APP1-AS4** (required end-to-end diagnostic investigation)
  - Outcomes: APP1-O14, APP1-O1, APP1-O2, APP1-O4, APP1-O7, APP1-O8, APP1-O10, APP1-O12, APP1-O13
  - Work: reproduce the healthy navigation and visible
    rendering of a static site served locally with
    `index.html`, `styles.css`, and a local image.
    Construct **at least four distinct controlled
    failure cases**: a stopped listener causing
    connection refusal; a stylesheet or image URL
    returning HTTP 404; a CSS/layout defect causing
    an incorrect visual result; and a fourth
    distinguishable case chosen from another local
    resource failure or an explicitly synthetic
    DNS/TLS scenario. Include a fragment-only
    navigation as a **nonfailure control** and
    explain why it normally does not initiate a
    new document fetch. Diagnose each from
    available network, DOM, style and rendered
    observations. **Repair at least two local
    faults**, show the changed fixture or command,
    and repeat the observation to verify the
    result. Defend the full path from local link
    assumptions to bytes-on-the-wire, DNS
    caveats, transport/TLS boundaries, HTTP,
    incremental resource loading, HTML/CSS parsing,
    style, layout, paint and compositing.
  - Criteria: correct classification of all four
    faults without treating the fragment control
    as a failure; at least two repairs produce
    demonstrably improved local observations;
    each fault is assigned to the earliest
    supported layer rather than explained by
    guesswork. Local HTTP is not claimed as
    HTTPS and synthetic DNS/TLS examples are
    never presented as live captures. An
    independently following reviewer can reproduce
    the healthy path, local failures, and repairs
    without a paid service or backend framework.
    The defense describes uncertain or unobserved
    steps honestly and proposes the next safe
    observation when evidence is insufficient.
  - Evidence: disposable static-site fixtures,
    exact serve/inspect commands and tool versions,
    healthy and faulty request summaries,
    waterfall/DOM/CSS and visual observations,
    a four-case failure matrix, two repair
    diffs and re-tests, a layered
    Internet-to-pixels diagram, labeled
    synthetic-case sources, and a concise
    technical defense and failure retrospective.

### Optional formative practice

Recommended self-checks and exercises that do
**not** independently gate course completion:

- Predict packet forwarding from unfamiliar
  route tables and compare latency versus loss.
- Distinguish connection refusal from a server
  returning an HTTP error.
- Label registrant, registrar, registry, DNS
  operator and host in a domain scenario.
- Resolve relative URLs and compare two origins.
- Trace a cache timeline involving
  `Cache-Control`, `ETag`, and `304`.
- Inspect a supplied certificate error without
  bypassing TLS validation.
- Compare a browser network waterfall with
  the DOM and computed styles.
- Predict the effect of a CSS rule change
  on layout versus paint.
- Classify whether a blocked cross-origin
  read is a CORS policy issue or a failed
  network connection.
- Explain why fragment navigation typically
  does not fetch a new document.

### Completion decision

Each required assessment is complete only when its published Work, Criteria and Evidence are demonstrated. Together `APP1-AS1`–`APP1-AS4` cover all fourteen outcomes. Independent review distinguishes directly observed network/browser behavior from labeled synthetic public DNS/TLS cases; passing quizzes or copying tool output does not establish diagnosis.

Completion records must identify the course and specification revision actually assessed. Editing the public curriculum does not change those decisions. APP1 remains `draft`; structural validation does not establish learner-tested or verified effectiveness. See [Evidence Rules](../../spec/evidence-rules.md) and [Status Labels](../../spec/status-labels.md).
