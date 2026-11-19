# Program 5 — SEC: Security Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · Previous: [AI](../AI/README.md)

## Overview

Security Engineering treats security as an engineering discipline. You begin with threat modeling and secure design, then work through web and application security, native-code and binary security, network and infrastructure security, applied cryptography, cloud and identity security, detection and incident response, and authorized AI security assessment. Offensive work stays inside explicitly authorized or deliberately vulnerable environments.

## Prerequisites

**Assessed completion of Program 1 — SEF — Software Engineering Foundations, including [SEF10](../SEF/SEF10.md).**

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

**SEC integration-branch review only; the current `main` catalog remains authoritative.** SEC1 is staged as a `v0.2.0` `draft` with observable outcomes and summative evidence. SEC2–SEC9 remain legacy course definitions until independently reassessed. The SEC8 legacy AI5 prerequisite is incompatible with the separate AI migration (where AI5 now means Deep Learning); it must be resolved before SEC cutover, not treated as a new mandatory learner requirement. See [SEC M0](https://github.com/0xbuffdev/open-engineering-education/issues/202) and the [derived inventory](../INVENTORY.md).

| Course | Title | Duration | Prerequisites | Type |
| --- | --- | --- | --- | --- |
| [SEC1](SEC1.md) | Security Foundations & Threat Modeling | 7–10 weeks | SEF10 (assessed SEF completion) | `course` |
| [SEC2](SEC2.md) | Web & Application Security | 6 weeks | SEC1, APP1 and APP3 | `course` |
| [SEC3](SEC3.md) | Systems & Binary Security | 6 weeks | SEC1 and SEF6 | `course` |
| [SEC4](SEC4.md) | Network & Infrastructure Security | 5 weeks | SEC2 and SEF7 | `course` |
| [SEC5](SEC5.md) | Applied Cryptography & Secure Protocols | 5 weeks | SEC1 | `course` |
| [SEC6](SEC6.md) | Cloud, Containers & Identity Security | 5 weeks | SEC2, SEC4 and APP7 | `course` |
| [SEC7](SEC7.md) | Detection, Incident Response & Threat Hunting | 5 weeks | SEC4 and SEC6 | `course` |
| [SEC8](SEC8.md) | AI Security & Authorized Red Teaming | 4 weeks | SEC1, SEC2, SEC7, and AI5 | `course` |
| [SEC9](SEC9.md) | Security Engineering Capstone | 8–10 weeks | SEC1–SEC8 | `project` |

Only SEC1 is a proposed v0.2.0 revision on this integration branch; the full prerequisite graph, program completion rules and downstream identity history require later review before publication. The course files remain the authoritative source for their defined work and prerequisites. Use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment for practical work and evidence. The [OEE specification](../../spec/README.md) governs newly authored or explicitly migrated course revisions.
