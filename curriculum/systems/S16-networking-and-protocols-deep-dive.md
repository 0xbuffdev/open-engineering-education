# S16 — Networking & Protocols Deep Dive

**Track:** Systems · **Prerequisite:** S10 · **Elective** · **Time:** 4 weeks, 60 hours · **Project:** elective

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Go below the socket API to understand how packets move, why latency and throughput behave the way they do, and how protocols fail under loss, reordering, and middleboxes. This course turns `curl` and `tcpdump` from magic into evidence.

## Outcomes

You can:

- explain Ethernet, ARP, IPv4/IPv6, routing, NAT, and the path of a packet;
- explain TCP handshake, flow control, congestion control, retransmission, and TIME_WAIT;
- explain UDP, QUIC, and when each transport is appropriate;
- read a packet capture and correlate it with application behaviour;
- explain DNS resolution, caching, TTLs, and failure modes;
- explain TLS handshakes, certificates, SNI, ALPN, and trust stores;
- explain HTTP/1.1, HTTP/2, HTTP/3, proxies, and load balancers;
- diagnose latency, loss, MTU, and connection-pool problems with measurements;
- design a bounded, observable network client/server protocol.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| *Computer Networking: A Top-Down Approach* (Kurose & Ross) | Ch. **1–4**, selected Ch. 6 | Layering, application, transport, network |
| *TCP/IP Illustrated, Volume 1* (Stevens) | Ch. **1–4, 17–18, 21** | Packet-level TCP behaviour |
| B5 *The Linux Programming Interface* | Ch. **56–61** | Sockets, TCP/IP, DNS, TLS overview |
| [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/) | Ch. 1–9 | Practical socket programming |
| [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) (TCP) | Selected sections | Normative transport behaviour |
| [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) (HTTP semantics) | Selected sections | Methods, status, caching |
| [QUIC RFC 9000](https://www.rfc-editor.org/rfc/rfc9000) | Overview, streams, recovery | Modern transport |
| [Wireshark user guide](https://www.wireshark.org/docs/wsug_html_chunked/) | Capture and display filters | Evidence |

## Modules

### 1. Layers and packet path

- application → transport → network → link;
- encapsulation and headers;
- Ethernet, VLANs, ARP/NDP;
- IPv4/IPv6 addressing, CIDR, routing tables;
- NAT and connection tracking;
- MTU, fragmentation, PMTUD;
- loopback, veth, bridge, overlay networks;
- `ip`, `ss`, `traceroute`, `mtr`.

### 2. TCP and UDP

- three-way handshake and close states;
- sequence/acknowledgement numbers;
- sliding window and flow control;
- retransmission timers and fast retransmit;
- congestion control: Reno, CUBIC, BBR (concepts);
- Nagle, delayed ACK, `TCP_NODELAY`;
- keepalive and idle timeouts;
- TIME_WAIT, port exhaustion, ephemeral ports;
- UDP semantics, MTU, and application-level reliability;
- QUIC streams, 0-RTT, and head-of-line blocking.

### 3. DNS and naming

- recursive vs authoritative resolution;
- records: A, AAAA, CNAME, MX, TXT, NS, SRV;
- TTL, caching, negative caching;
- resolv.conf, `getaddrinfo`, search domains;
- DNSSEC and DoH/DoT (awareness);
- failure modes: NXDOMAIN, SERVFAIL, slow resolver, stale cache.

### 4. TLS and HTTP

- symmetric/asymmetric crypto and key exchange (concepts);
- certificates, chain of trust, hostname validation;
- SNI, ALPN, session resumption;
- TLS 1.3 handshake;
- HTTP request/response, methods, status codes, caching;
- HTTP/1.1 keep-alive and pipelining;
- HTTP/2 multiplexing and flow control;
- HTTP/3 over QUIC;
- proxies, reverse proxies, load balancers, connection pools;
- WebSocket and server-sent events.

### 5. Measurement and troubleshooting

- capture placement and timestamp accuracy;
- display filters and stream following;
- RTT, loss, jitter, goodput;
- `ss -ti`, `netstat`, `tcpdump`, `tshark`;
- `curl -w`, `openssl s_client`, `dig +trace`;
- load-generator pitfalls;
- middleboxes, proxies, and MTU black holes.

## Labs

### Lab 1 — Packet path

Capture a DNS lookup, TCP handshake, HTTP request, and close. Annotate every packet with the layer, purpose, and state transition. Explain one packet that surprised you.

### Lab 2 — TCP behaviour under loss

Use `tc netem` on a private network namespace or VM to add delay, loss, reordering, and duplication. Measure throughput and latency with `iperf3`/`curl`. Compare one congestion-control algorithm if available.

### Lab 3 — DNS and TLS diagnosis

Use `dig +trace`, `getaddrinfo`, `openssl s_client`, and `curl -v` to diagnose a deliberately broken local setup: wrong TTL, missing SAN, expired certificate, or blocked port. Document the evidence chain.

### Lab 4 — Protocol implementation

Build a small length-delimited TCP protocol with heartbeats, timeouts, backpressure, and graceful close. Test partial reads, half-close, reset, and slow consumers. Add a packet-capture-based test.

### Lab 5 — HTTP/2 or HTTP/3 comparison

Serve a small local endpoint over HTTP/1.1 and HTTP/2 (or HTTP/3). Compare connection reuse, multiplexing, and latency under concurrent requests. State what the local test cannot prove about the public Internet.

## Exercises

1. Calculate the sequence-number space and wrap behaviour.
2. Explain why TIME_WAIT exists and one mitigation.
3. Explain the difference between flow control and congestion control.
4. Explain head-of-line blocking at the TCP and HTTP/2 layers.
5. Trace a TLS 1.3 handshake and identify what is encrypted.
6. Explain certificate validation and one common misconfiguration.
7. Explain DNS caching and a stale-record failure.
8. Explain NAT and why inbound connections need port forwarding.
9. Explain an MTU black hole and how to detect it.
10. Design retry/timeout semantics for an HTTP client.

## Project increment (optional)

Apply the course to P4 `workbenchd` or another local service: capture and explain the packet path, compare two protocol or configuration variants, and write a diagnostic report with a reproducible capture and a stated limitation. This is an elective extension, not a new ladder project.

## Exit check

- [ ] read a capture and explain the TCP state machine for a real connection;
- [ ] demonstrate the effect of loss/delay on throughput and latency;
- [ ] diagnose a DNS or TLS failure from command output;
- [ ] explain HTTP/2 multiplexing and its limits;
- [ ] implement a framed protocol with bounded buffers and clean shutdown;
- [ ] distinguish a local measurement from a public-Internet claim.

## Common failure modes

- Assuming TCP preserves message boundaries.
- Blaming "the network" without a capture or measurement.
- Ignoring DNS caching and resolver behaviour.
- Disabling certificate verification to "make it work".
- Measuring throughput on loopback and generalizing to WAN.
- Forgetting connection-pool and ephemeral-port limits.
- Treating HTTP/2 as automatically faster.

## Evidence to commit

- `labs/systems/S16/` with annotated capture, netem results, TLS/DNS diagnosis, protocol implementation, HTTP comparison
- `notes/systems/S16/summary.md`

## Optional depth

- *High Performance Browser Networking* (Grigorik), free online.
- *UNIX Network Programming, Volume 1* (Stevens), selected chapters.
- `man 7 tcp`, `man 7 ip`, `man 7 socket`.
- Cloudflare and APNIC blog posts on BBR, QUIC, and anycast.
- eBPF networking with `tc`/XDP (after S9).
