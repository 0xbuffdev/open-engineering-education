# Program 5 — SEC: Security Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · [Historical source at 0e14d4ff5808](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SEC.md)

**Migration status:** The course documents below are preserved historical drafts and **not yet conforming to OEE v0.2.0**. Their old curriculum sequence and prerequisites must be reviewed; the source's books, chapters, and other resource assignments stay in the content repository.

## Overview

Security Engineering treats security as an engineering discipline. You begin with threat modeling and secure design, then work through web and application security, native-code and binary security, network and infrastructure security, applied cryptography, cloud and identity security, detection and incident response, and authorized AI security assessment. Offensive work stays inside explicitly authorized or deliberately vulnerable environments.

## Prerequisites

**Program 1 — SEF — Software Engineering Foundations.**

Later courses may require specific Application, Systems, or AI knowledge. These dependencies are stated at the course level so learners can satisfy them through prior study or demonstrated equivalent knowledge.

## Learning outcomes

By the end of this program, you will be able to:

- Model assets, trust boundaries, threats, abuse cases, and security requirements for real software systems.
- Identify, reproduce safely, remediate, and regression-test common web and application security weaknesses.
- Reason about memory-corruption risks, native binaries, operating-system protections, and safer systems designs.
- Assess and harden networked services, hosts, containers, cloud environments, identities, and deployment pipelines.
- Use established cryptographic primitives and protocols correctly and reason about keys, nonces, authentication, and failure behavior.
- Design useful security telemetry, investigate controlled incidents, and perform evidence-based remediation.
- Conduct scoped and authorized security assessments and communicate findings in a developer-actionable form.
- Build and defend a production-grade security assessment and remediation program for a real or controlled system.

## Program completion standard

The learner must demonstrate the knowledge, practical skills, and engineering judgment described by the program outcomes and successfully complete the program capstone.

## Courses

| Code | Course | Type | Duration |
| --- | --- | --- | --- |
| [SEC1](SEC1.md) | Security Foundations & Threat Modeling | `course` | 5 weeks |
| [SEC2](SEC2.md) | Web & Application Security | `course` | 6 weeks |
| [SEC3](SEC3.md) | Systems & Binary Security | `course` | 6 weeks |
| [SEC4](SEC4.md) | Network & Infrastructure Security | `course` | 5 weeks |
| [SEC5](SEC5.md) | Applied Cryptography & Secure Protocols | `course` | 5 weeks |
| [SEC6](SEC6.md) | Cloud, Containers & Identity Security | `course` | 5 weeks |
| [SEC7](SEC7.md) | Detection, Incident Response & Threat Hunting | `course` | 5 weeks |
| [SEC8](SEC8.md) | AI Security & Authorized Red Teaming | `course` | 4 weeks |
| [SEC9](SEC9.md) | Security Engineering Capstone | `project` | 8–10 weeks |

## Required next review

1. Reconcile original prerequisites against today's OEE SEF/APP course codes and the full program dependency graph.
2. Review the learning outcomes and lesson progression under [Course Format](../../spec/course-format.md) and the one-primary-objective-per-lesson guidance in [Curriculum Design Guide](../DESIGN-GUIDE.md).
3. Give the course observable, stable outcome IDs and required summative assessment IDs, with public work, success criteria, and proportionate evidence for **every** required outcome.
4. Treat old module checkpoint and micro-lab placements as **historical proposals**, not mandatory `v0.2.0` completion gates.
5. Specify safe, reproducible experimentation and a reviewable technical defense when substantial project outcomes require it.
6. Preserve book/resource mappings **outside OEE**, keyed by OEE course codes in the content repository.
7. Verify educational coverage manually. A structurally valid file or `draft` status does not constitute course or implementation conformance.
