# Program 5 — SEC: Security Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · Previous: [AI](../AI/README.md)

## Overview

Security Engineering treats security as an engineering discipline. You begin with threat modeling and secure design, then work through web and application security, native-code and binary security, network and infrastructure security, applied cryptography, cloud and identity security, detection and incident response, and authorized AI security assessment. Offensive work stays inside explicitly authorized or deliberately vulnerable environments.

## Prerequisites

[SEF10](../SEF/SEF10.md) is required for SEC1. Additional prerequisites are specified for each course in the catalog.

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

Graduation requires two separate, independently reviewable decisions: verified assessed completion of every required course from SEC1 through SEC8 before admission to SEC9, and satisfactory evaluation of all published SEC9 outcomes, summative assessments, cumulative project evidence and individual technical defense. A completed capstone does not replace missing prerequisite mastery, and predecessor completion does not replace the capstone.

## Courses

| Course | Title | Duration | Prerequisites | Type |
| --- | --- | --- | --- | --- |
| [SEC1](SEC1.md) | Security Foundations & Threat Modeling | 7–10 weeks | SEF10 | `course` |
| [SEC2](SEC2.md) | Web & Application Security | 12–16 weeks | SEC1, APP1, APP3 | `course` |
| [SEC3](SEC3.md) | Systems & Binary Security | 10–14 weeks | SEC1, SEF6 | `course` |
| [SEC4](SEC4.md) | Network & Infrastructure Security | 10–14 weeks | SEC2, SEF7 | `course` |
| [SEC5](SEC5.md) | Applied Cryptography & Secure Protocols | 12–16 weeks | SEC1 | `course` |
| [SEC6](SEC6.md) | Cloud, Containers & Identity Security | 14–18 weeks | SEC2, SEC4, APP7 | `course` |
| [SEC7](SEC7.md) | Detection, Incident Response & Threat Hunting | 12–16 weeks | SEC4, SEC6 | `course` |
| [SEC8](SEC8.md) | AI Security & Authorized Red Teaming | 12–16 weeks | SEC7 | `course` |
| [SEC9](SEC9.md) | Security Engineering Capstone | 14–18 weeks | SEC1–SEC8 | `project` |

Course definitions specify the required outcomes, learning sequence and completion evidence. Work can be completed in [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment. The [OEE specification](../../spec/README.md) governs course requirements.
