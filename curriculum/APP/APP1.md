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

1. **Course Orientation** — Trace what this course explains, why it matters, and where its model ends.
2. **Internet History** — Explain the relationship between packet networking, open protocols, and the Web's development.
3. **Internet and Web** — Distinguish network infrastructure from applications built on it.
4. **Web Resources** — Distinguish pages, websites, applications, documents, and referenced resources.
5. **Client and Server** — Explain request/response responsibility without assuming every server is a web framework.
6. **Standards and Interoperability** — Relate published protocols and browser variation to compatible delivery.
7. **The Web Journey** — Sketch a first device-to-visible-page model with identified unknown steps.

### Module 2 — Connectivity and Routing

#### Outcomes

- APP1-O2
- APP1-O1

#### Lessons

1. **Network Interfaces** — Explain link media and the roles of interfaces on a connected device.
2. **Local Networks** — Distinguish wireless access, Ethernet, switches, and routers.
3. **IP Configuration** — Explain host addresses, DHCP, default gateways, and basic NAT.
4. **Internet Access** — Relate last-mile connections, ISPs, and upstream networks.
5. **Packets and Frames** — Distinguish link-layer delivery from IP datagrams and packet forwarding.
6. **IPv4 Addresses** — Interpret addresses, prefixes, and local versus routed destinations.
7. **IPv6 Addresses** — Interpret basic IPv6 address and prefix structure without assuming IPv4 behavior.
8. **Routing Decisions** — Read a route and next hop; explain forwarding and hop-limit consequences.
9. **Network Measurements** — Distinguish latency, bandwidth, throughput, jitter, loss, and their evidence limits.
10. **Connectivity Failures** — Classify link, gateway, routing, ICMP, and upstream symptoms using safe observations.

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

1. **Domain Names** — Explain human-readable labels, subdomains, and the DNS namespace.
2. **DNS Hierarchy** — Distinguish root, top-level domains, and delegated zones.
3. **Domain Registration** — Trace registrant, registrar, registry, ICANN, renewal, transfer, and expiration roles.
4. **Nameserver Delegation** — Explain how delegated authority differs from owning a website or hosting it.
5. **DNS Resolvers** — Distinguish local stub, recursive, and authoritative resolvers.
6. **Resolution Walkthrough** — Trace referrals, records, caching, and the resulting answer.
7. **DNS Records** — Interpret A, AAAA, CNAME, NS, and the limited role of MX.
8. **DNS Caching** — Explain TTLs, positive/negative caching, stale answers, and hosts-file overrides.
9. **DNS Failures** — Distinguish NXDOMAIN, SERVFAIL, timeout, and local cache effects.
10. **DNS Observation Limits** — Explain why a local or browser lookup does not prove a public-network query and where DoH/privacy affects visibility.

### Module 5 — Hosting and Delivery

#### Outcomes

- APP1-O5
- APP1-O1

#### Lessons

1. **Web Hosting** — Distinguish hosted files/content, servers, and domain-name services.
2. **Static and Dynamic** — Compare static resource delivery with dynamically produced responses conceptually.
3. **Hosting Models** — Compare shared hosting, virtual machines, managed hosting, and serverless at a high level.
4. **Origin Servers** — Relate a listening HTTP process to an origin and its hosted resources.
5. **Reverse Proxies** — Explain intermediated requests and origin visibility.
6. **CDN Edges** — Explain geographically distributed delivery and shared caching boundaries.
7. **Load Balancing** — Trace requests among origin instances and describe availability limitations.
8. **Delivery Paths** — Distinguish DNS answers, origin identity, intermediary responses, and the actual serving location.

### Module 6 — URLs and Origins

#### Outcomes

- APP1-O6
- APP1-O13

#### Lessons

1. **Resource Identifiers** — Explain why addresses identify resources and what a URL does not guarantee.
2. **URL Components** — Parse scheme, authority, hostname, port, path, query, and fragment.
3. **Relative URLs** — Resolve paths against a document or declared base URL.
4. **Encoding and Names** — Explain percent encoding, Unicode domain-name concepts, and ambiguous interpretation.
5. **Browser Origins** — Derive origins from scheme, host, and port.
6. **Sites and Domains** — Distinguish registrable sites, subdomains, and origins.
7. **Navigation Targets** — Predict how redirects, changed paths, and fragment-only navigation affect requests.

### Module 7 — HTTP Requests and Responses

#### Outcomes

- APP1-O7
- APP1-O6

#### Lessons

1. **HTTP Exchange** — Interpret the application-layer request and response model.
2. **Message Structure** — Explain request targets, fields, bodies, and representation metadata.
3. **Request Methods** — Distinguish GET, HEAD, POST, PUT, PATCH, and DELETE semantics.
4. **Safety and Idempotence** — Separate protocol method properties from application retry behavior.
5. **Response Status** — Classify successful, redirected, client-error, and server-error responses.
6. **Representations** — Interpret Content-Type, negotiation, compression, and body-length constraints.
7. **Authority and Headers** — Explain the request's target authority and selected headers.
8. **HTTP Versions** — Distinguish shared HTTP semantics from HTTP/1.1, HTTP/2, and HTTP/3 framing and transport.

### Module 8 — HTTP Caching and Redirects

#### Outcomes

- APP1-O7

#### Lessons

1. **Cache Purposes** — Distinguish browser/private caches, shared caches, and origin responses.
2. **Freshness Controls** — Interpret Cache-Control, freshness lifetime, no-store, and private scope.
3. **Cache Validators** — Explain ETag and Last-Modified as representation validation mechanisms.
4. **Conditional Requests** — Trace If-None-Match, If-Modified-Since, and 304 Not Modified decisions.
5. **Redirect Behavior** — Interpret redirect locations, status codes, and follow-up requests.
6. **Cache Keys** — Explain Vary, representation differences, and why a URL alone may be insufficient.
7. **Intermediary Effects** — Distinguish cache hits, proxy behavior, and origin observability.
8. **Storage Boundaries** — Separate HTTP caching from browser application storage and persistent content.

### Module 9 — HTTPS and TLS

#### Outcomes

- APP1-O8
- APP1-O13

#### Lessons

1. **HTTPS Guarantees** — Explain protected transport and the risks of plaintext HTTP.
2. **TLS Handshake** — Describe negotiated cryptography and authenticated key establishment conceptually.
3. **Certificate Chains** — Explain trust anchors, issuers, and certificate validation.
4. **Hostname Verification** — Relate requested host identity to a certificate without equating it to content honesty.
5. **Protocol Negotiation** — Explain SNI and ALPN at an appropriate introductory level.
6. **TLS and QUIC** — Distinguish TLS use with TCP-based HTTPS and HTTP/3 over QUIC.
7. **Mixed Content** — Explain security warnings, downgrade risks, and secure-context boundaries.
8. **Trust Failures** — Classify supplied certificate/hostname errors without bypassing browser validation.

### Module 10 — Browser Architecture

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

### Module 11 — Navigation and Resource Loading

#### Outcomes

- APP1-O10
- APP1-O7
- APP1-O9

#### Lessons

1. **Navigation Lifecycle** — Trace address entry, history, navigation decisions, and document commitment.
2. **Connections and Redirects** — Relate redirects and existing connections to navigation timing.
3. **Document Streaming** — Explain incremental arrival and discovery of document content.
4. **Resource Discovery** — Explain how stylesheets, images, fonts, and scripts are requested.
5. **Preload and Priority** — Describe speculative discovery and relative resource scheduling at a high level.
6. **Blocking Behavior** — Distinguish parser-blocking scripts, deferred/async loading, and render-blocking stylesheets.
7. **Readiness Milestones** — Distinguish load events, first paint, and interactive readiness conceptually.
8. **Network Waterfalls** — Interpret request ordering, reuse, caching, and failure evidence in browser tools.

### Module 12 — HTML and CSS Parsing

#### Outcomes

- APP1-O11
- APP1-O10

#### Lessons

1. **HTML Decoding** — Explain byte/character decoding and tokenization at a conceptual level.
2. **DOM Construction** — Trace tree building and common parser recovery effects.
3. **DOM Representation** — Distinguish the DOM from source bytes and rendered boxes.
4. **CSS Parsing** — Explain declarations, rule parsing, and error recovery.
5. **Selector Matching** — Trace a simple selector to affected elements.
6. **Cascade and Inheritance** — Explain why competing style declarations produce specific computed values.
7. **Computed Styles** — Inspect an element's computed styling and distinguish it from authored CSS.
8. **Semantics and Accessibility** — Relate meaningful document structure to the accessibility tree without requiring authoring mastery.

### Module 13 — Layout to Pixels

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

### Module 14 — Security, State and Privacy

#### Outcomes

- APP1-O13
- APP1-O6
- APP1-O8

#### Lessons

1. **Same-Origin Policy** — Explain default cross-origin access restrictions.
2. **CORS Boundaries** — Explain controlled permission for cross-origin reads, not a way to bypass transport rules.
3. **Cookies and Sessions** — Distinguish cookie state and conceptual session identifiers.
4. **Browser Storage** — Compare local storage, HTTP caches, and service-worker-controlled resources.
5. **Secure Contexts** — Explain mixed content, permission prompts, and trustworthy-context restrictions.
6. **Web Attack Concepts** — Recognize CSRF, credential handling, and untrusted-content boundaries without implementing backend authentication.
7. **Privacy and Evidence** — Protect browsing histories, credentials, local data, and observation context.
8. **Security Diagnostics** — Distinguish TLS, CORS, HTTP, permission, and storage symptoms using available evidence.

### Module 15 — End-to-End Diagnosis

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

1. **The Complete Journey** — Explain how connection, name resolution, transport, HTTP, parsing, and rendering connect.
2. **Failure Boundaries** — Classify link/routing, DNS, transport, TLS, HTTP, resource, parsing, and visual failures.
3. **Static-Site Fixtures** — Prepare or inspect a controlled HTML/CSS/image site using an unprivileged local server.
4. **Evidence Collection** — Record request traces, document/style observations, tool versions, and uncertainty.
5. **Controlled Failures** — Compare four distinct fault cases and explicit nonfault controls.
6. **Repair Verification** — Apply narrow safe changes and re-run observations to verify at least two repairs.
7. **Diagnostic Defense** — Present a reproducible Internet-to-pixels explanation and justified next observations.

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

### Completion decision and migration

Each assessment is complete only when its
specified Work, Criteria and Evidence are
demonstrated. Together the four required
assessments cover all `APP1-O*` outcomes.
Passing quizzes, inspecting a fixture without
interpreting it, or submitting synthetic
output as live capture is insufficient.

This rewrite replaces the former 17 module
checkpoint/lab pairs and mandatory-by-template
final lab with evidence selected for the
course's actual outcomes. It **retains**
the original technical scope, safe local
inspection, public DNS/TLS examples, and
the full end-to-end diagnostic requirement
(including four fault cases and two repairs).
The course remains focused on foundations;
it does not add frontend/backend programming
as a prerequisite.

The program catalog duration changes from
`16–18 weeks` to `12–16 weeks` as a
**provisional workload revision**, not a
claim of improved efficacy. Learner evidence
should inform a future estimate. Historical
course completion records remain bound to
the requirements in force when they were
assessed; no automatic equivalence or
reclassification is implied.

This course remains `draft`. Structural
validation cannot establish pedagogical
effectiveness, independently reproduced
investigations, learner testing or
`verified` readiness. Consult
[Evidence Rules](../../spec/evidence-rules.md)
and [Status Labels](../../spec/status-labels.md).
