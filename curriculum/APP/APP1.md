# APP1 — Web & Internet Foundations

**Program:** APP — Application Engineering
**Type:** `course`
**Prerequisites:** [SEF10](../SEF/SEF10.md) — Software Engineering Foundations
**Duration:** 4 weeks
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

## Modules

### Module 1 — The Internet & Client/Server Model

#### Outcomes

- Explain **Networks, IP addresses, ports, and clients/servers** in the context of the course.
- Apply **DNS and name resolution** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Course introduction: Web & Internet Foundations** — `lesson`

   Understand the network and web foundations that modern application software depends on, then use that knowledge to build and investigate HTTP services.
2. **Networks, IP addresses, ports, and clients/servers** — `lesson`
3. **DNS and name resolution** — `lesson`
4. **Internet fundamentals** — `test`
5. **Trace DNS resolution for a real domain and record each step** — `lab`

### Module 2 — HTTP & Web Communication

#### Outcomes

- Explain **HTTP requests, responses, methods, and status codes** in the context of the course.
- Apply **URLs, headers, JSON, and serialization** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **HTTP requests, responses, methods, and status codes** — `lesson`
2. **URLs, headers, JSON, and serialization** — `lesson`
3. **HTTP reasoning** — `test`
4. **Inspect a real browser request and reconstruct its request/response pair** — `lab`

### Module 3 — Sessions & Secure Transport

#### Outcomes

- Explain **Cookies, sessions, and state** in the context of the course.
- Apply **TLS and secure transport concepts** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Cookies, sessions, and state** — `lesson`
2. **TLS and secure transport concepts** — `lesson`
3. **sessions and transport security** — `test`
4. **Inspect which parts of a browser connection are visible before and after TLS** — `lab`

### Module 4 — APIs & Resource Design

#### Outcomes

- Explain **Resource-oriented API design** in the context of the course.
- Apply **Inspecting application traffic with browser/network tools** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Resource-oriented API design** — `lesson`
2. **Inspecting application traffic with browser/network tools** — `lesson`
3. **API design** — `test`
4. **Use developer tools to diagnose a failing API request** — `lab`

### Module 5 — HTTP Service

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

**Exit demonstration:**

The learner can explain what happens from entering a URL to receiving a rendered response and can diagnose common request/response failures.

---
