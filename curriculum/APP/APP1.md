# APP1 — Web & Internet Foundations

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [SEF10](../SEF/SEF10.md) — Software Engineering Foundations
**Duration:** 16–18 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Application Engineering](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Start at the absolute foundations of the Internet and World Wide Web, then trace how an address becomes a visible page. Learners examine access networks, packets, routing, transport, domains, DNS, hosting, URLs, HTTP, caching, HTTPS, browser processes and engines, navigation, resource loading, HTML and CSS parsing, layout, painting, compositing, security and evidence-based diagnostics.

This course develops the **mechanisms behind the Web**, not a programming framework. Learners use a browser and supplied or locally served static fixtures to explain and diagnose behavior. They do **not** have to write JavaScript, TypeScript, a frontend framework, a backend HTTP service, production infrastructure or a database. HTML/CSS authoring is only a small observational fixture here; it is taught systematically in a subsequent dedicated course. DNS/TLS and HTTP examples may use sanitized simulated traces when actual networks or tooling are unavailable. An offline local setup is sufficient for mandatory work.

The course is a **draft curriculum contract**, not complete teaching materials and not evidence that learners have completed its labs. The 16–18 week estimate is intentionally provisional: more subjects than the original seven-week course are included, but depth is calibrated by meaningful lessons, practice and demonstrations rather than a fixed module quota.

## Learning outcomes

By the end of this course, the learner will be able to:

- Distinguish Internet connectivity from Web applications and explain the roles of browser, network, client, server and intermediary.
- Trace local connectivity through gateways, IP addressing, routing, ports and TCP/UDP transport and classify link, name, transport and application failures.
- Explain domain registration, delegation and DNS resolution, including caching, record types, response failures and observation limits.
- Distinguish domain names, DNS services, web hosting, origin servers, reverse proxies, CDNs and content delivery paths.
- Parse URLs and explain relative resolution, origins, ports, fragments, resource identity and navigation.
- Interpret HTTP request and response semantics, methods, status codes, headers, representations, redirects, caching and conditional requests.
- Explain why HTTPS uses TLS and how certificate-chain and hostname validation establish connection trust without proving content integrity beyond that boundary.
- Distinguish browser UI, renderer, graphics/compositor and JavaScript engines; compare architecture choices without assuming all browsers behave identically.
- Describe browser navigation, incremental resource discovery and the difference between parser-blocking and render-blocking resources.
- Explain how HTML and CSS are parsed into document/style representations and how semantics, computed style and accessibility relate without claiming prior HTML/CSS mastery.
- Trace style resolution, layout, paint, rasterization and composition, including why incremental rendering and layout shifts may occur.
- Classify origin restrictions, cookies, cache, local storage, mixed content and privacy responsibilities at a conceptual level.
- Use safe, reproducible tools and evidence to diagnose a faulty website end-to-end, explain limits and defend appropriate fixes.

## Modules

### Module 1 — Understanding the Internet and the Web

#### Outcomes

- Distinguish the Internet, the World Wide Web, the browser and an application without collapsing their responsibilities.
- Construct a basic explanation of how a website is reached and represented, with explicit unknowns.

#### Lessons

1. **Course introduction: Web & Internet Foundations** — `lesson`

   Introduce what learners will investigate, why the Web matters to application engineering, its history and limits, where these mechanisms are used, and how evidence-based explanation differs from tool memorization.
2. **A brief history of packet networking and the Web** — `lesson`
3. **What the Internet is, and what the Web is not** — `lesson`
4. **Websites, pages, web applications and resources** — `lesson`
5. **Clients, servers, requests and responses** — `lesson`
6. **Open standards, browsers and interoperability** — `lesson`
7. **A first end-to-end website-loading mental model** — `lesson`
8. **Understanding the Internet and the Web reasoning checkpoint** — `test`
9. **Draw and critique a complete web visit** — `lab`

### Module 2 — Devices, Access Networks and Connectivity

#### Outcomes

- Explain how a device joins a network and reaches a configured gateway.
- Diagnose local link, configuration and upstream connectivity failures without assuming every failure is DNS or HTTP.

#### Lessons

1. **Network interface, link and physical versus wireless media** — `lesson`
2. **Home and campus networks, switches and routers** — `lesson`
3. **Wi-Fi association and Ethernet connectivity** — `lesson`
4. **IP configuration and DHCP as a provisioning mechanism** — `lesson`
5. **Default gateways, local delivery and NAT overview** — `lesson`
6. **Internet service providers, last-mile links and upstream networks** — `lesson`
7. **Local connectivity diagnostics and safe troubleshooting** — `lesson`
8. **Devices, Access Networks and Connectivity reasoning checkpoint** — `test`
9. **Inspect and classify local connectivity states** — `lab`

### Module 3 — Internet Protocol, Packets and Routing

#### Outcomes

- Distinguish link, network and transport responsibilities and explain packet forwarding.
- Read an IPv4/IPv6 address, prefix and route in sufficient detail to predict a packet's next hop.

#### Lessons

1. **Why large messages are divided into packets** — `lesson`
2. **Link-layer frames versus IP datagrams** — `lesson`
3. **IPv4 addressing and prefixes** — `lesson`
4. **IPv6 addressing and basic differences from IPv4** — `lesson`
5. **Routing tables, next hops and default routes** — `lesson`
6. **Hop limits, ICMP, packet loss and path changes** — `lesson`
7. **Latency, bandwidth, throughput and jitter** — `lesson`
8. **Traceroute-style evidence and its limitations** — `lesson`
9. **Internet Protocol, Packets and Routing reasoning checkpoint** — `test`
10. **Explain a packet path using sanitized routes** — `lab`

### Module 4 — Transport Connections and Delivery

#### Outcomes

- Explain the roles of ports, sockets, TCP and UDP and their relationship to IP.
- Compare connection-oriented byte streams and datagrams; explain how QUIC and HTTP versions fit at a high level.

#### Lessons

1. **Ports, endpoint tuples and listening services** — `lesson`
2. **TCP connection establishment and handshake concepts** — `lesson`
3. **Streams, reliability, ordering and retransmission** — `lesson`
4. **Connection refusal, reset and timeouts** — `lesson`
5. **UDP datagrams and delivery trade-offs** — `lesson`
6. **QUIC overview and how HTTP/3 differs from TCP-based HTTP** — `lesson`
7. **Connection reuse, multiplexing and network latency** — `lesson`
8. **Local loopback and dual-stack address behavior** — `lesson`
9. **Transport Connections and Delivery reasoning checkpoint** — `test`
10. **Distinguish listener, refusal and timeout** — `lab`

### Module 5 — Domain Names and Registration

#### Outcomes

- Explain the naming hierarchy and distinguish domain ownership arrangements from hosting and DNS resolution.
- Describe registrants, registrars, registries, delegation and the lifecycle of a registered name.

#### Lessons

1. **Human-readable names and the DNS namespace** — `lesson`
2. **Labels, subdomains and fully qualified names** — `lesson`
3. **Top-level domains and the root zone** — `lesson`
4. **Registrant, registrar, registry and ICANN roles** — `lesson`
5. **Registration, renewal, transfer and expiry** — `lesson`
6. **Nameservers, zone ownership and delegation** — `lesson`
7. **Domain name versus website versus hosting** — `lesson`
8. **Domain-control and ownership misconceptions** — `lesson`
9. **Domain Names and Registration reasoning checkpoint** — `test`
10. **Model a domain's administrative and technical ownership** — `lab`

### Module 6 — DNS Resolution and Caching

#### Outcomes

- Trace recursive resolution through caches, authoritative servers and delegated zones.
- Interpret common DNS records, TTL behavior and DNS failure responses without making claims that a lookup necessarily reached the public network.

#### Lessons

1. **Stub resolvers and recursive resolvers** — `lesson`
2. **Root, TLD and authoritative nameservers** — `lesson`
3. **DNS delegation and iterative resolution concept** — `lesson`
4. **A and AAAA records, CNAME aliases and MX/NS overview** — `lesson`
5. **TTL, positive caching and stale/negative responses** — `lesson`
6. **NXDOMAIN, SERVFAIL and timeout distinctions** — `lesson`
7. **Local hosts files, browser/OS caches and DNS over HTTPS overview** — `lesson`
8. **DNS observation limits and privacy considerations** — `lesson`
9. **DNS Resolution and Caching reasoning checkpoint** — `test`
10. **Trace DNS records and controlled resolution failures** — `lab`

### Module 7 — Web Hosting, Origins and Delivery Infrastructure

#### Outcomes

- Distinguish site content, an HTTP origin server, hosting arrangements and distributed delivery.
- Explain how proxies, CDNs and load balancers influence delivery and trust boundaries without implementing backend infrastructure.

#### Lessons

1. **What it means to host a website** — `lesson`
2. **Static files versus dynamically generated responses** — `lesson`
3. **Shared hosting, managed hosting, virtual machines and serverless overview** — `lesson`
4. **Server processes, listening ports and basic deployment concepts** — `lesson`
5. **Reverse proxies and HTTP gateway responsibilities** — `lesson`
6. **Content delivery networks, edges and cached responses** — `lesson`
7. **Load balancing, availability and geographical placement** — `lesson`
8. **DNS answers, origin identity and hosting misconceptions** — `lesson`
9. **Web Hosting, Origins and Delivery Infrastructure reasoning checkpoint** — `test`
10. **Compare origin, reverse proxy and cache paths** — `lab`

### Module 8 — URLs, Origins and Web Navigation Identities

#### Outcomes

- Decompose URLs into their components and explain the implications of authority, scheme and fragments.
- Distinguish origin, site and resource identity and predict when browser navigation changes network requests.

#### Lessons

1. **URI, URL and resource identifier basics** — `lesson`
2. **Scheme, authority, host and port** — `lesson`
3. **Paths, query parameters and fragments** — `lesson`
4. **Relative URLs and base URL resolution** — `lesson`
5. **Percent encoding, Unicode names and normalization concepts** — `lesson`
6. **Origins: scheme, host and port** — `lesson`
7. **Sites, subdomains, navigation and redirect targets** — `lesson`
8. **When fragments do not cause a new HTTP request** — `lesson`
9. **URLs, Origins and Web Navigation Identities reasoning checkpoint** — `test`
10. **Resolve and classify web addresses** — `lab`

### Module 9 — HTTP Messages and Resource Semantics

#### Outcomes

- Interpret HTTP methods, status codes, headers and representation metadata.
- Reconstruct and classify request/response behavior using reproducible traces rather than framework-specific code.

#### Lessons

1. **HTTP as an application-layer request-response protocol** — `lesson`
2. **Start lines, fields, message bodies and representation metadata** — `lesson`
3. **GET, HEAD, POST, PUT, PATCH, DELETE semantics** — `lesson`
4. **Safe and idempotent method meaning (not retry policy)** — `lesson`
5. **Status codes: success, redirect, client and server errors** — `lesson`
6. **Content-Type, negotiation, compression and content length concepts** — `lesson`
7. **URL requests, headers, Host/authority and origins** — `lesson`
8. **HTTP/1.1, HTTP/2 and HTTP/3: stable semantics versus framing** — `lesson`
9. **HTTP Messages and Resource Semantics reasoning checkpoint** — `test`
10. **Inspect and explain HTTP exchanges** — `lab`

### Module 10 — HTTP Caching, Redirects and Intermediaries

#### Outcomes

- Explain cache freshness, validation, redirects and intermediate response behavior.
- Predict how caches and conditional requests change traffic, including when a `304 Not Modified` can occur.

#### Lessons

1. **Why HTTP caching exists and who may cache** — `lesson`
2. **Cache-Control freshness, no-store and private/shared scope** — `lesson`
3. **ETag and Last-Modified validators** — `lesson`
4. **Conditional requests and HTTP 304 responses** — `lesson`
5. **Redirect codes and browser navigation changes** — `lesson`
6. **Vary, representation selection and cache keys** — `lesson`
7. **Proxies, response transformation and origin visibility** — `lesson`
8. **Caching versus application storage and correctness limits** — `lesson`
9. **HTTP Caching, Redirects and Intermediaries reasoning checkpoint** — `test`
10. **Reason about freshness and validator timelines** — `lab`

### Module 11 — HTTPS, TLS and Web Trust

#### Outcomes

- Explain TLS negotiation and the role of certificate validation in HTTPS security.
- Distinguish transport encryption, domain identity, origin authorization and application trust.

#### Lessons

1. **HTTP versus HTTPS and secure transport goals** — `lesson`
2. **TLS handshake and authenticated key establishment at a conceptual level** — `lesson`
3. **Certificate chains, certificate authorities and hostname validation** — `lesson`
4. **SNI, ALPN and selecting a secure application protocol** — `lesson`
5. **TLS 1.3 and QUIC high-level relationship** — `lesson`
6. **Mixed content, downgrade and certificate-warning behavior** — `lesson`
7. **Security limits: encryption is not proof of honest content** — `lesson`
8. **Safe TLS inspection without bypassing trust verification** — `lesson`
9. **HTTPS, TLS and Web Trust reasoning checkpoint** — `test`
10. **Evaluate synthetic TLS trust outcomes** — `lab`

### Module 12 — Browser Architecture and Engines

#### Outcomes

- Describe browser, renderer and GPU responsibilities as a conceptual architecture while distinguishing implementations.
- Explain how rendering engines and JavaScript engines differ and why process isolation matters.

#### Lessons

1. **What a browser does beyond downloading HTML** — `lesson`
2. **Browser UI, networking, renderer and GPU responsibilities** — `lesson`
3. **Processes, threads and sandboxing concepts** — `lesson`
4. **Rendering engines: Blink, Gecko and WebKit** — `lesson`
5. **JavaScript engines: V8, SpiderMonkey and JavaScriptCore** — `lesson`
6. **HTML/CSS standards versus engine-specific implementations** — `lesson`
7. **Site isolation, origins and failure containment** — `lesson`
8. **Browser task and performance inspection without engine-specific assumptions** — `lesson`
9. **Browser Architecture and Engines reasoning checkpoint** — `test`
10. **Compare two browser architecture implementations** — `lab`

### Module 13 — Navigation, Discovery and Resource Loading

#### Outcomes

- Trace browser navigation, network requests, redirects and resource discovery without requiring learners to program JavaScript.
- Distinguish parser-blocking, render-blocking and deferred resources with reproducible observations.

#### Lessons

1. **Entering a URL, navigation and session history** — `lesson`
2. **Connection reuse, redirects and navigation commit** — `lesson`
3. **Document responses, streams and incremental parsing** — `lesson`
4. **Discovering stylesheets, images, fonts and scripts** — `lesson`
5. **The preload scanner and resource prioritization concepts** — `lesson`
6. **Parser-blocking scripts and deferred or async loading overview** — `lesson`
7. **Stylesheets, render blocking and critical resources** — `lesson`
8. **Load events versus initial paint and interactive readiness** — `lesson`
9. **Network waterfall interpretation and caching effects** — `lesson`
10. **Navigation, Discovery and Resource Loading reasoning checkpoint** — `test`
11. **Investigate a static document's resource waterfall** — `lab`

### Module 14 — HTML and CSS Parsing: Document to Style Data

#### Outcomes

- Explain how browser parsers build the DOM and CSSOM and how styles are matched to elements.
- Relate semantic HTML structure and accessible representations to later specialized HTML/CSS and accessibility coursework.

#### Lessons

1. **HTML bytes, character encodings and tokenization overview** — `lesson`
2. **HTML tree building and error recovery concepts** — `lesson`
3. **The DOM as an internal document representation** — `lesson`
4. **CSS stylesheet parsing, declarations and error handling** — `lesson`
5. **Selectors, matching and the CSS object model** — `lesson`
6. **Cascade, inheritance and computed style overview** — `lesson`
7. **Semantic structure and the accessibility tree overview** — `lesson`
8. **Stylesheet failure and computed-style inspection** — `lesson`
9. **Difference between DOM tree and visual/rendered boxes** — `lesson`
10. **HTML and CSS Parsing: Document to Style Data reasoning checkpoint** — `test`
11. **Reconstruct a document and computed-style change** — `lab`

### Module 15 — Layout, Paint, Rasterization and Compositing

#### Outcomes

- Trace the high-level rendering pipeline from computed styles to visible pixels.
- Explain why layout, paint and compositing work can recur after content changes and why browser-specific performance observations need qualification.

#### Lessons

1. **The render tree and boxes versus DOM nodes** — `lesson`
2. **Style resolution and layout constraints** — `lesson`
3. **Formatting context, flow and geometry overview** — `lesson`
4. **Viewport dimensions, font metrics and reflow** — `lesson`
5. **Paint instructions, stacking and visual order** — `lesson`
6. **Rasterization and pixel generation concepts** — `lesson`
7. **Compositing layers and GPU responsibilities** — `lesson`
8. **Incremental rendering and browser invalidation** — `lesson`
9. **Diagnosing delayed paint and layout shift conceptually** — `lesson`
10. **Layout, Paint, Rasterization and Compositing reasoning checkpoint** — `test`
11. **Explain a measured render and layout change** — `lab`

### Module 16 — Browser Security, State and Privacy Boundaries

#### Outcomes

- Explain the browser origin trust model, basic state storage and privacy risks without implementing authentication or backend services.
- Classify common browser warnings and cross-origin limitations at a conceptual level.

#### Lessons

1. **Same-origin policy and site concepts revisited** — `lesson`
2. **Cross-origin resource sharing (CORS) as a controlled access mechanism** — `lesson`
3. **Cookies, sessions and attributes overview** — `lesson`
4. **Local storage, browser cache and service workers: different purposes** — `lesson`
5. **Secure contexts, mixed content and permission prompts** — `lesson`
6. **Browser isolation, untrusted content and sandbox principles** — `lesson`
7. **CSRF and credential handling as future backend topics** — `lesson`
8. **Data minimization, private browsing and shared-device risk** — `lesson`
9. **Safe browser troubleshooting and responsible evidence collection** — `lesson`
10. **Browser Security, State and Privacy Boundaries reasoning checkpoint** — `test`
11. **Classify browser security and storage scenarios** — `lab`

### Module 17 — End-to-End Website Loading and Diagnostic Defense

#### Outcomes

- Independently explain the full journey from address entry to rendered page, including alternate paths, caching and failures.
- Produce reproducible evidence that isolates DNS, transport, TLS, HTTP, resource-loading, parsing, style and paint faults without writing backend or framework code.

#### Lessons

1. **End-to-end journey review: connectivity to visible page** — `lesson`
2. **A layered diagnostic decision tree** — `lesson`
3. **Evidence quality, uncertainty and negative paths** — `lesson`
4. **Comparing network waterfall, document tree and computed styles** — `lesson`
5. **Communicating a repair recommendation without untested claims** — `lesson`
6. **End-to-End Website Loading and Diagnostic Defense reasoning checkpoint** — `test`
7. **Defend a complete web-page loading investigation** — `lab`

## Completion requirements

- Complete the conceptual checkpoint and required lab for every module, with evidence that matches the published acceptance criteria. The final integration lab is required.
- Retain original or sanitized outputs, tool/version information, assumptions and corrections under the [OEE Evidence Rules](../../spec/evidence-rules.md). Never publish credentials, unredacted browsing histories, real client data or intrusive diagnostics.
- Complete required practical exercises and present a reasoned independent defense of the final investigation, including at least one negative-path scenario, reproduced corrections, and a technical retrospective.
- The mandatory environment requires **no paid service** or deployed domain. Use unprivileged local static serving on 127.0.0.1; local resolver outputs do not prove external DNS traffic and HTTP over localhost does not prove TLS.
- CORS and same-origin restrictions are introduced conceptually. JavaScript/TypeScript coding, backend API/framework implementation, mutating HTTP endpoints, retry and idempotency implementation, and production operations belong to later courses.

**Required practical exercises:**

- Draw layered diagrams for connectivity, DNS and browser navigation and label observed versus inferred steps.
- Reconstruct synthetic packets/routes, DNS records, TLS certificate outcomes and HTTP exchanges without presenting them as live captures.
- Use a local browser and static fixture to observe successful and failing requests, document parsing/style effects and inspect visible layout differences.
- Explain at least four distinct failure classes (for example refused connection, DNS failure, HTTP 404 and missing CSS), with a safe next-step observation for each.

**Final integration lab — required work:**

Required artifact: **End-to-End Web Loading Investigation**. Reproduce the Module 17 lab in a local, unprivileged environment, show how a valid static website loads and renders, introduce and diagnose four controlled failures, repair at least two, defend the full browser loading model and document limits. Supplied DNS/TLS scenarios are explicitly simulated and cannot be represented as captured local network traffic.

**Expanded module assessments and practical work:**

**Module 1 — Understanding the Internet and the Web: checkpoint** — Required assessment details

- **Q1 (free):** Is the Internet the same thing as the World Wide Web? Give two examples of non-web Internet use.
  - Expected answer and scoring: No. The Internet interconnects networks; the Web is an application ecosystem using URLs, HTTP, browsers and documents. Email and DNS are examples of other Internet services.
- **Q2 (free):** Does opening a page necessarily mean one request to one computer? Explain.
  - Expected answer and scoring: No. A page may require multiple resources and intermediaries; name resolution, redirects, caches and distributed delivery can affect its loading. Score for identifying at least two distinct dependencies.

**Module 1 — Draw and critique a complete web visit: required lab** — Required assessment details

- **Objective:** Build an evidence-labelled dependency map from a person entering a URL to the first visible page.
- **Prerequisites:** Complete Module 1's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Draw the user device, access network, resolver, origin or content provider, browser and rendered page; mark each assumed interaction.
  2. Use a browser's Network panel on an offline local static page to find document and supporting resource requests; identify which diagram edges were actually observed.
  3. Annotate at least three plausible failure points and separate directly observed facts from conceptual inferences.
- **Expected result:** A coherent annotated sequence with separate Internet/Web definitions and no claim that local browsing proves public DNS/TLS use.
- **Verification:** Explain each arrow aloud and answer both checkpoint questions without collapsing network transport into HTTP.
- **Evidence:** Labelled diagram, request list, assumption table and corrected version after review.
- **Failure analysis:** Treating HTML as the network, a website as a physical server, or local `localhost` traffic as evidence of Internet routing.
- **Acceptance:** Correct distinctions, at least three failure boundaries, and no unsupported network claims.

**Module 2 — Devices, Access Networks and Connectivity: checkpoint** — Required assessment details

- **Q1 (free):** A laptop is associated with Wi-Fi but cannot reach the default gateway. Does this prove a website is down?
  - Expected answer and scoring: No. Association alone is not IP reachability. Test local address/configuration, gateway connectivity and routing before inferring anything about a remote website.
- **Q2 (free):** Why might two household devices share one public IPv4 address?
  - Expected answer and scoring: A gateway can translate private addresses/ports using NAT. That is not how IPv6 must work, and the shared public address is not the device's private address.

**Module 2 — Inspect and classify local connectivity states: required lab** — Required assessment details

- **Objective:** Separate link, address configuration, gateway and public-reachability concepts.
- **Prerequisites:** Complete Module 2's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Record the active interface and assigned IPv4/IPv6 addresses using non-privileged OS tools; redact personal addresses before sharing.
  2. Identify the current default route or explain what it would be on an offline fixture; draw the route from device to access router.
  3. Use supplied synthetic outputs for link-down, missing address and unreachable gateway scenarios; classify each without contacting unfamiliar hosts.
- **Expected result:** A layer-labelled table showing different diagnostics and realistic uncertainty.
- **Verification:** For each scenario propose one safe next observation and explain why HTTP request inspection would be premature.
- **Evidence:** Redacted configuration excerpt, topology sketch, classification table and limitations.
- **Failure analysis:** Confusing Wi-Fi association with Internet availability or assuming NAT is universally required.
- **Acceptance:** All three failure scenarios correctly classified without unsafe diagnostics.

**Module 3 — Internet Protocol, Packets and Routing: checkpoint** — Required assessment details

- **Q1 (free):** Why might a packet reach a destination through routers without carrying a URL?
  - Expected answer and scoring: Routers forward mainly using network-layer addresses and routing state; the URL belongs to an application-level model, not each forwarded IP packet.
- **Q2 (free):** A traceroute omits a hop. Must packets have failed to pass through that router?
  - Expected answer and scoring: No. Intermediate devices can suppress, deprioritize or not respond to probe packets. Missing probe replies do not prove missing data-plane forwarding.

**Module 3 — Explain a packet path using sanitized routes: required lab** — Required assessment details

- **Objective:** Reconstruct forwarding decisions while distinguishing real observations from illustrative data.
- **Prerequisites:** Complete Module 3's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Given a fictional source address, destination address and three sample routing-table entries, select the longest-prefix matching next hop.
  2. Annotate a provided six-hop trace, explicitly marking unanswered probes as unknown rather than failed hops.
  3. Change the sample destination/prefix and document how the expected forwarding decision changes.
- **Expected result:** A reproducible forwarding table, packet sketch and bounded interpretation of probe evidence.
- **Verification:** Check each longest-prefix choice and distinguish IP routing from DNS and application-layer messages.
- **Evidence:** Route calculations, annotated trace and interpretation notes.
- **Failure analysis:** Assuming a hop response is mandatory, or confusing an HTTP redirect with IP routing.
- **Acceptance:** Correct forwarding decisions and no unsupported interpretation of missing probes.

**Module 4 — Transport Connections and Delivery: checkpoint** — Required assessment details

- **Q1 (free):** A local TCP connection to a closed port is refused. What does it tell you about HTTP?
  - Expected answer and scoring: It demonstrates a transport endpoint failure, not an HTTP status. There may be no HTTP request or response at all.
- **Q2 (free):** Does HTTP/3 run over TCP? What mechanism supplies its secure transport?
  - Expected answer and scoring: HTTP/3 uses QUIC, typically over UDP, with transport security integrated using TLS 1.3; HTTP semantics remain related across versions.

**Module 4 — Distinguish listener, refusal and timeout: required lab** — Required assessment details

- **Objective:** Observe bounded local transport behavior without building a server application.
- **Prerequisites:** Complete Module 4's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Start a preinstalled static HTTP server bound to 127.0.0.1 on an available unprivileged port; record its advertised address and port.
  2. Connect with a browser or `curl`; stop the server and repeat to reproduce refusal or equivalent local error.
  3. Use a supplied sanitized timeout trace to compare timeout with refusal; record that local tests do not prove QUIC support.
- **Expected result:** A successful local request and a later connection failure clearly separated from any HTTP 404.
- **Verification:** Check socket endpoint and failure-layer descriptions against command output; no privileged operations are used.
- **Evidence:** Command log, success/error traces, comparison table and environment versions.
- **Failure analysis:** Interpreting connection refusal as an HTTP response or assuming an unanswered probe proves an HTTP timeout.
- **Acceptance:** Correct distinction between TCP endpoint behavior and application-level responses.

**Module 5 — Domain Names and Registration: checkpoint** — Required assessment details

- **Q1 (free):** If a person registers a domain name, have they automatically purchased a working website?
  - Expected answer and scoring: No. Registration provides contractual control of the name subject to registrar/registry rules; DNS service, hosting, content and TLS arrangements are separate.
- **Q2 (free):** Does a subdomain always require purchasing another domain?
  - Expected answer and scoring: No. A registrant can typically configure labels under a domain they control, within DNS and provider policy; that is different from registering a separate second-level domain.

**Module 5 — Model a domain's administrative and technical ownership: required lab** — Required assessment details

- **Objective:** Explain domain-name roles using a fictional example without buying a domain.
- **Prerequisites:** Complete Module 5's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. For `docs.example.test` in a fictional zone, identify the registrant, registrar, registry, delegated zone operator, host and website operator as distinct roles.
  2. Draw how `docs` is a subdomain label and what delegation would mean; use `.test` only for fictional documentation and not as a public production site.
  3. Walk through a hypothetical renewal failure and explain which operational capabilities may be affected while distinguishing assumptions.
- **Expected result:** An accurate hierarchy and responsibility table for the fictional registration lifecycle.
- **Verification:** Reviewer can independently label the actors and explain why a registered name is not synonymous with a server.
- **Evidence:** Administrative/technical diagram, owner-role table and lifecycle failure note.
- **Failure analysis:** Treating registrar as hosting provider by definition, or claiming fictional DNS data was queried live.
- **Acceptance:** Distinct naming, registration and hosting roles with a defensible failure explanation.

**Module 6 — DNS Resolution and Caching: checkpoint** — Required assessment details

- **Q1 (free):** A system resolves `localhost` to `127.0.0.1`. Does that demonstrate a wire-level DNS exchange?
  - Expected answer and scoring: No. Name resolution may use local hosts data, a resolver cache or other sources. Only an actual trace of network DNS packets proves a wire-level query.
- **Q2 (free):** Why can two clients receive different answers after a DNS record change?
  - Expected answer and scoring: Different recursive caches, TTL expiry, policy, geography or configuration can result in different observed answers; propagation is not a single global switch.

**Module 6 — Trace DNS records and controlled resolution failures: required lab** — Required assessment details

- **Objective:** Reconstruct an observed-versus-simulated DNS resolution with caching and failure classifications.
- **Prerequisites:** Complete Module 6's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Inspect local resolver configuration and resolve `localhost`; record why this does not imply a public DNS query.
  2. Use this **synthetic trace**: resolver cache miss → root delegation → TLD delegation → authoritative A answer `192.0.2.42`, TTL 300 seconds; label each actor and expected cache effect.
  3. Compare three supplied fault cases (NXDOMAIN, SERVFAIL, transport timeout); explain how each differs and what evidence is required before diagnosis.
- **Expected result:** Resolution diagram with no fabricated packet capture and a correct TTL/failure matrix.
- **Verification:** Check the RFC 5737 documentation address is treated as synthetic and local configuration is not mistaken for a network trace.
- **Evidence:** Resolver output, simulated query sequence, cache timeline and failure table.
- **Failure analysis:** Using `localhost` as proof of external DNS, confusing CNAME with IP records, or using private data in public evidence.
- **Acceptance:** All three failure responses explained, caching interpretation correct and observations clearly labelled.

**Module 7 — Web Hosting, Origins and Delivery Infrastructure: checkpoint** — Required assessment details

- **Q1 (free):** Does pointing a domain's DNS record at an address mean the website contents are stored in DNS?
  - Expected answer and scoring: No. DNS supplies naming information such as address records; the web content is retrieved from HTTP-serving systems or intermediaries.
- **Q2 (free):** Why can a CDN return a valid page when the origin is temporarily unreachable?
  - Expected answer and scoring: An eligible cached representation can be served under the cache policy and freshness/staleness constraints; it is not guaranteed for every resource or failure.

**Module 7 — Compare origin, reverse proxy and cache paths: required lab** — Required assessment details

- **Objective:** Use supplied delivery traces to identify where a response may originate.
- **Prerequisites:** Complete Module 7's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Draw direct hosting, reverse-proxy and CDN-cached response paths for the same hypothetical site.
  2. Use two sanitized HTTP exchanges with distinct cache headers to label an origin response versus a cache hit; state any ambiguity.
  3. List what the learner would have to observe to prove the serving layer, and why DNS alone cannot establish it.
- **Expected result:** A defensible traffic flow showing separate origin/edge responsibilities.
- **Verification:** Identify all headers as evidence with limitations, not universal proof of internal topology.
- **Evidence:** Three flow diagrams, trace annotations and claim-versus-evidence table.
- **Failure analysis:** Assuming every `X-Cache` header is trustworthy or treating public IP and physical server as identical.
- **Acceptance:** Correct layer boundaries and no unjustified topology claims.

**Module 8 — URLs, Origins and Web Navigation Identities: checkpoint** — Required assessment details

- **Q1 (free):** What is the difference between `https://site.test/a?q=1#part` and the request target sent over HTTP?
  - Expected answer and scoring: The fragment `#part` is handled client-side and is not sent in an HTTP request target; path and query identify the requested resource representation context.
- **Q2 (free):** Do `https://example.test` and `https://example.test:8443` have the same origin?
  - Expected answer and scoring: No. Origin includes scheme, host and effective port. A different effective port changes origin.

**Module 8 — Resolve and classify web addresses: required lab** — Required assessment details

- **Objective:** Predict URL resolution and origin boundaries before inspecting network behavior.
- **Prerequisites:** Complete Module 8's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Resolve a table of relative URLs against a fictional base including parent paths, queries and fragment-only links.
  2. Group ten supplied URL examples by origin, explaining effective-port normalization and where differences exist.
  3. Use browser inspection on a local static page to compare fragment-only navigation with a resource fetch; record exceptions or browser-specific behavior.
- **Expected result:** Resolved URL table and accurate same-origin groups.
- **Verification:** Check fragment handling and scheme/host/port comparisons; explain why a path alone does not change origin.
- **Evidence:** Resolution table, origin equivalence groups and local navigation observations.
- **Failure analysis:** Treating URL fragments as request headers or equating registrable domain with same origin.
- **Acceptance:** All provided URLs correctly classified and no fragment transmitted in the claimed HTTP request.

**Module 9 — HTTP Messages and Resource Semantics: checkpoint** — Required assessment details

- **Q1 (free):** Does a 404 response mean the network connection failed?
  - Expected answer and scoring: No. It is a valid HTTP response indicating the target resource was not found or not disclosed; the transport and HTTP communication were established sufficiently to receive it.
- **Q2 (free):** Is POST always non-idempotent and PUT always safe?
  - Expected answer and scoring: PUT is defined as idempotent but is not safe, while POST is neither safe nor guaranteed idempotent by method semantics. A server can implement additional application guarantees, which cannot be inferred from a method label alone.

**Module 9 — Inspect and explain HTTP exchanges: required lab** — Required assessment details

- **Objective:** Use browser and command-line network inspection to reason about real and intentionally failing HTTP requests.
- **Prerequisites:** Complete Module 9's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Serve a small local HTML document and a missing path using a preinstalled static server; record request methods, target, status and key headers.
  2. For a supplied sanitized POST/redirect trace, explain its semantics without implementing POST handling.
  3. Reconstruct a request/response timeline that distinguishes protocol version, body content, headers and failure cases.
- **Expected result:** Correctly classified local 200/404 and sanitized redirect cases without writing service code.
- **Verification:** Compare reported status and headers to raw outputs; reject any inference that 404 or 500 is a DNS/transport failure.
- **Evidence:** Redacted HTTP transcript, status classification table, sequence diagram and limitations.
- **Failure analysis:** Treating a URL as an HTTP method or assuming a request body always exists.
- **Acceptance:** Accurate interpretation of methods, status families and transport/application boundaries.

**Module 10 — HTTP Caching, Redirects and Intermediaries: checkpoint** — Required assessment details

- **Q1 (free):** What does `304 Not Modified` mean, and is it a normal replacement for an initial full response?
  - Expected answer and scoring: It answers a conditional request indicating a stored representation remains valid under the supplied validator; clients generally reuse a cached body. It is not a replacement for sending initial content without a cached representation.
- **Q2 (free):** Can a shared cache safely reuse every response carrying user-specific information?
  - Expected answer and scoring: No. Shared caches must obey authorization and cache-control rules; private responses or sensitive data require appropriate restrictions. A header alone does not justify serving private data to another user.

**Module 10 — Reason about freshness and validator timelines: required lab** — Required assessment details

- **Objective:** Reconstruct cache decisions from a synthetic response log and verify browser cache inspection where available.
- **Prerequisites:** Complete Module 10's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Given a synthetic GET → 200 (ETag, max-age=60) → conditional GET → 304 timeline, annotate when a cached representation is reused.
  2. Classify supplied private, no-store and public responses for a private browser cache versus a shared proxy.
  3. Inspect local browser caching behavior with DevTools cache toggles, noting that a simple static server may not demonstrate 304 without additional supplied fixtures.
- **Expected result:** Correct freshness/validation decisions and explicit separation of private and shared cache rules.
- **Verification:** Compare the written decisions against the supplied timestamps and headers; require explanation of 304 preconditions.
- **Evidence:** Annotated cache timeline, privacy decision matrix and observed-versus-simulated flags.
- **Failure analysis:** Inventing a 304 from a server that never emitted it or treating `no-store` as identical to `no-cache`.
- **Acceptance:** Correct cache matrix, 304 reasoning and evidence classification.

**Module 11 — HTTPS, TLS and Web Trust: checkpoint** — Required assessment details

- **Q1 (free):** Does seeing a padlock guarantee the website is legitimate and its content safe?
  - Expected answer and scoring: No. HTTPS protects a connection to a certified endpoint under its trust assumptions; it does not certify that all content or business behavior is benign.
- **Q2 (free):** Why might a valid certificate for one hostname fail for another?
  - Expected answer and scoring: Hostname validation compares the requested identity against the certificate's permitted names. A valid chain alone does not establish identity for a different host.

**Module 11 — Evaluate synthetic TLS trust outcomes: required lab** — Required assessment details

- **Objective:** Classify valid and invalid HTTPS trust outcomes without self-signed CA installation or insecure bypass flags.
- **Prerequisites:** Complete Module 11's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Inspect the connection information of a known local or optional public HTTPS example only if allowed, then explicitly state which values were actually observable.
  2. Use supplied synthetic certificate cases: trusted chain and matching hostname; trusted chain but mismatching name; unknown issuer; expired certificate.
  3. For each case, determine expected browser warning/acceptance and explain what TLS cannot establish about content safety.
- **Expected result:** A clear trust-decision table and accurate HTTPS boundary explanation.
- **Verification:** Reject incorrect advice to click through certificate warnings for mandatory work; no custom CA or paid domain required.
- **Evidence:** Synthetic certificate table, optional sanitized browser observations and limitations.
- **Failure analysis:** Confusing encryption with authentication of a business, treating no warning as blanket safety, or bypassing certificate checks.
- **Acceptance:** All trust cases classified and safe observation practices documented.

**Module 12 — Browser Architecture and Engines: checkpoint** — Required assessment details

- **Q1 (free):** Are the JavaScript engine and CSS rendering engine the same component?
  - Expected answer and scoring: No. JavaScript engines execute ECMAScript, while rendering engines parse and lay out documents and styles; browser architectures integrate but distinguish these roles.
- **Q2 (free):** Does every browser spawn exactly one renderer process for every tab?
  - Expected answer and scoring: No. Process models depend on implementation, site isolation policy and resource constraints. A Chrome-specific diagram cannot be asserted as universal.

**Module 12 — Compare two browser architecture implementations: required lab** — Required assessment details

- **Objective:** Build an annotated model distinguishing standards-defined behavior from browser implementation choices.
- **Prerequisites:** Complete Module 12's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Compare a Chrome/Chromium reference diagram with a Firefox or WebKit architecture summary from a publicly accessible source or a provided schematic.
  2. Label browser, renderer, JavaScript engine and graphics/compositor roles; identify two implementation-specific choices.
  3. Use an available browser's task manager or performance tools if present; otherwise document why such process information is inaccessible in the environment.
- **Expected result:** An architecture map with correctly attributed engine components and clearly bounded claims.
- **Verification:** Reviewer can identify which components are mandatory Web platform concepts versus Chrome/Firefox/WebKit implementation specifics.
- **Evidence:** Comparative table, annotated diagram, optional process observations and caveats.
- **Failure analysis:** Equating Blink with V8 or claiming every renderer pipeline uses the same internal process model.
- **Acceptance:** Engine roles correctly separated, two implementation differences and no unsupported universality claims.

**Module 13 — Navigation, Discovery and Resource Loading: checkpoint** — Required assessment details

- **Q1 (free):** Does a browser normally wait for every image on a page before its first paint?
  - Expected answer and scoring: No. Browsers can render incrementally while images and other noncritical resources arrive; required render-blocking resources and implementation choices influence timing.
- **Q2 (free):** Why might a synchronous script in a document delay parsing?
  - Expected answer and scoring: A classic synchronous script may inspect or alter the document while parsing, so the HTML parser can be blocked until it executes. This concept does not require writing the script in APP1.

**Module 13 — Investigate a static document's resource waterfall: required lab** — Required assessment details

- **Objective:** Trace discovery and load ordering using only supplied static HTML/CSS/image assets.
- **Prerequisites:** Complete Module 13's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Create a local static page with an HTML document, stylesheet and an image (the image may be a tiny local SVG). Serve it with the standard static server.
  2. Use browser Network and Performance tools to record document/style/image loading; repeat once with cache enabled and once disabled and document variance.
  3. Change a stylesheet URL to a nonexistent resource, reload and explain the resulting 404 and visual differences without implementing JavaScript.
- **Expected result:** A labelled resource dependency graph tied to recorded requests and visual behavior.
- **Verification:** Network records include paths, statuses and evidence for the missing stylesheet; distinguish observation from generalized loading rules.
- **Evidence:** HAR or screenshots with redacted data, resource graph, failed-style comparison and environment.
- **Failure analysis:** Assuming requests are strictly sequential or treating DOMContentLoaded as equivalent to all content fully loaded.
- **Acceptance:** Correct dependency graph and repeatable missing-resource diagnosis.

**Module 14 — HTML and CSS Parsing: Document to Style Data: checkpoint** — Required assessment details

- **Q1 (free):** Are DOM nodes identical to the painted pixels shown on screen?
  - Expected answer and scoring: No. DOM nodes represent document structure; style and layout determine displayed boxes and painting. Some DOM elements contribute no painted boxes.
- **Q2 (free):** Why might invalid CSS leave parts of the page still styled?
  - Expected answer and scoring: CSS parsing and error recovery may ignore unsupported or invalid declarations while retaining valid rules; the actual observed result depends on selector/cascade context.

**Module 14 — Reconstruct a document and computed-style change: required lab** — Required assessment details

- **Objective:** Observe DOM structure and CSS effects in a minimal static page.
- **Prerequisites:** Complete Module 14's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Write a small HTML page with nested headings, lists, links and a stylesheet containing two conflicting selector rules.
  2. Draw the expected DOM outline, then compare it with the browser's Elements/Inspector view and computed styles.
  3. Introduce a malformed declaration and explain precisely which style outcome changes; observe accessibility semantics where tools allow and disclose any lack of assistive-technology verification.
- **Expected result:** Document tree sketch, computed-style reasoning and visible difference from an invalid declaration.
- **Verification:** Reviewer checks selectors, computed values and DOM outline; requires no JavaScript authoring.
- **Evidence:** Source fragments, DOM diagram, computed-style screenshots and observation notes.
- **Failure analysis:** Confusing DOM with CSSOM, calling style rules HTML elements or asserting screen-reader behavior without testing.
- **Acceptance:** Correct DOM/CSS boundaries and at least one traceable cascade/error example.

**Module 15 — Layout, Paint, Rasterization and Compositing: checkpoint** — Required assessment details

- **Q1 (free):** Does every DOM element necessarily correspond to a visible box?
  - Expected answer and scoring: No. Some DOM elements have no visible box or are omitted from the render tree; layout and computed style determine painted output.
- **Q2 (free):** If an image loads after initial paint without reserved dimensions, what work might repeat?
  - Expected answer and scoring: The browser may need to recalculate affected layout, repaint and composite. The exact operations depend on the implementation and what changed; not every change forces every stage.

**Module 15 — Explain a measured render and layout change: required lab** — Required assessment details

- **Objective:** Tie an observed visual change to relevant rendering stages without claiming access to internal GPU implementation details.
- **Prerequisites:** Complete Module 15's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Serve an HTML/CSS fixture with a large image whose dimensions are initially not reserved and record its effect on layout in a current browser.
  2. Repeat after adding explicit intrinsic width and height attributes or an aspect-ratio constraint; compare visible movement, avoiding claims about exact metric improvements without measurements.
  3. Use browser Performance/Rendering panels if available to identify paints or layout work; otherwise supply an annotated stage-by-stage explanation based on the observed page.
- **Expected result:** Before/after layout evidence and a bounded explanation of style → layout → paint → composition.
- **Verification:** Check that the learner avoids universal statements about layers or GPU processes and clearly separates observed traces from theory.
- **Evidence:** Before/after screenshots or recordings, source difference, measurements if available and explanation.
- **Failure analysis:** Treating DOM parsing as painting, assuming every frame repaints everything, or claiming improved performance without comparable conditions.
- **Acceptance:** Correct pipeline and defensible observed-versus-inferred report.

**Module 16 — Browser Security, State and Privacy Boundaries: checkpoint** — Required assessment details

- **Q1 (free):** Is receiving an HTTP 200 from a cross-origin server proof that browser JavaScript can read its contents?
  - Expected answer and scoring: No. Cross-origin network delivery and script-readable responses have different policies; CORS can govern read access when browser script is involved. APP1 studies the boundary conceptually.
- **Q2 (free):** Does clearing the HTTP cache necessarily remove every cookie and local-storage record?
  - Expected answer and scoring: No. Cache storage, cookies and web storage have distinct lifecycles; an explicit browser clearing action may target different kinds of site data.

**Module 16 — Classify browser security and storage scenarios: required lab** — Required assessment details

- **Objective:** Use sanitized browser observations to separate secure-transport, origin, cookie and cache rules.
- **Prerequisites:** Complete Module 16's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Group supplied scenarios into origin-policy, credential/session, cache or TLS failures; explain why one failure type does not imply another.
  2. Inspect the site-information or storage overview for a local static page without creating personal data or accepting risky permissions.
  3. Use supplied synthetic CORS/mixed-content errors to propose safe diagnostic observations, explicitly deferring code-level repair to later courses.
- **Expected result:** A threat-boundary matrix with correct browser behaviors and privacy-preserving evidence.
- **Verification:** Check no security bypasses or live credentials are recommended and that network 200 vs script access is distinguished.
- **Evidence:** Sanitized inspector notes, classification table, incident hypotheses and limitations.
- **Failure analysis:** Treating CORS as an authentication system, sharing personal browser data or equating cache with local storage.
- **Acceptance:** All boundary cases classified safely and correctly.

**Module 17 — End-to-End Website Loading and Diagnostic Defense: checkpoint** — Required assessment details

- **Q1 (free):** A page remains unstyled but the document returns 200. Name three different plausible causes and the first observations to distinguish them.
  - Expected answer and scoring: Possible causes include missing stylesheet (404), incorrect stylesheet URL, invalid CSS/selector, wrong MIME or blocked resource; check Network request/status, Console and computed styles before concluding.
- **Q2 (free):** How do you distinguish a DNS failure from TLS, HTTP 404 and CSS rendering failures in an incident report?
  - Expected answer and scoring: DNS occurs before an origin connection; TLS affects authenticated transport; 404 is an HTTP response; CSS rendering occurs after document/resource handling. Include evidence at each boundary and do not infer unobserved packets.

**Module 17 — Defend a complete web-page loading investigation: required lab** — Required assessment details

- **Objective:** Diagnose a supplied, intentionally faulty static website using observable evidence from network access to rendered output.
- **Prerequisites:** Complete Module 17's instructional lessons and checkpoint; use the conceptual and diagnostic skills introduced earlier in APP1. Do not require subsequent APP course capabilities.
- **Environment:** A current standards-capable browser with developer tools (Chromium or Firefox), a terminal, and a local static fixture directory served by a preinstalled unprivileged static-file server such as Python's standard-library `http.server` on 127.0.0.1. Record OS, browser, server-tool versions, chosen port and exact commands. A synthetic, sanitized trace may replace external-network observations; no paid service, account, public domain, administrator privileges, custom trust root, interception of others' traffic or live production system is required.
- **Procedure:**
  1. Create or use a local static website fixture with `index.html`, `styles.css` and a local image; run it with a standard static server, not a learner-written backend.
  2. Prepare at least four reproducible faults: missing stylesheet URL (HTTP 404), stopped listener (connection refusal), a fragment-only navigation that should not fetch a new document, and a CSS rule/layout issue; add DNS/TLS failures from explicitly labelled sanitized traces rather than falsely claiming local reproduction.
  3. For the healthy and faulty cases collect request/response summaries, resource dependencies, DOM/CSS inspection, rendered screenshots, error classification, and a record of every tool/version used.
  4. Produce a narrated start-to-finish web journey: device and route assumptions, name-resolution caveats, connection and HTTP phases, resource discovery, DOM/CSSOM, style, layout, paint and composition; distinguish omitted optional cases (CDN, QUIC, TLS, JavaScript).
  5. Propose and apply safe static-site fixes for at least two issues, repeat observations and write a short engineering retrospective.
- **Expected result:** A functioning static site and a layered incident report with at least four diagnosed failures, independently reproducible changes and no backend implementation requirement.
- **Verification:** A reviewer can reproduce the local faults, distinguish simulated DNS/TLS observations, follow the healthy page request timeline, and verify two repaired cases and one negative path.
- **Evidence:** Fixture source and run instructions, tool/version list, screenshots or sanitized traces, fault matrix, repair diffs, layered journey diagram, unresolved claims and technical retrospective.
- **Failure analysis:** Inventing DNS/TLS packet observations from localhost, bypassing certificate validation, mistaking an HTTP error for failed connection, or treating paint as the same as DOM construction.
- **Acceptance:** All four failures are correctly isolated, two repairs reproduced, required pipeline stages and uncertainty documented, and the learner defends the diagnosis without guessing.

**Exit assessment expectation:**

A reviewer must independently reproduce the mandatory local observations and verify the written explanations. Completion requires accurate distinctions among link, routing, DNS, transport, TLS, HTTP, browser loading, parsing and visual rendering. Positive and negative cases must be supported by actual observations or **explicitly marked synthetic evidence**, never by invented traces. Question scoring must reward mechanisms and uncertainty rather than isolated terminology.

**Exit demonstration:**

Given a previously unseen static website and a reproducible failure report, the learner explains the Internet-to-pixels journey and proposes the smallest safe next observation at each possible failure boundary, repairs applicable static-site faults, and defends the evidence without writing backend services or relying on a proprietary learning platform.

---
