# Program 5 — SEC: Security Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · Previous: [AI](../AI/README.md)

## Overview

Security Engineering treats security as an engineering discipline. You begin with threat modeling and secure design, then work through web and application security, native-code and binary security, network and infrastructure security, applied cryptography, cloud and workload security, detection and incident response, authorized AI security assessment, enterprise identity and privileged access assurance, endpoint and platform defense, continuous vulnerability and exposure management, multi-component security architecture assurance, and data security and privacy across the processing lifecycle. Offensive work stays inside explicitly authorized or deliberately vulnerable environments.

## Prerequisites

[SEF10](../SEF/SEF10.md) is required for SEC1. Additional prerequisites are specified for each course in the catalog.

## Learning outcomes

By the end of this program, you will be able to:

- Model assets, trust boundaries, threats, abuse cases, and security requirements for real software systems.
- Identify, reproduce safely, remediate, and regression-test web and application security weaknesses, including long-lived WebSocket sessions, messages and confidential server-push events.
- Investigate native memory-corruption and binary-security risks through bounded coverage-guided input testing, minimized defect reproduction, verified repairs, operating-system protections and safer systems design.
- Assess and harden networked services, DNS resolution and protective policy, hosts, containers, cloud environments, Kubernetes orchestration RBAC/admission and pod-network policy, workload identities, and deployment pipelines; distinguish source-verified platform policies from actually exercised enforcement.
- Evaluate enterprise authentication and federation, identity lifecycle, privileged access, resource authorization and effective account/session revocation.
- Assess and harden endpoint privilege, executable integrity and host configuration; distinguish actual Linux enforcement from authentic Windows platform policy and event evidence, verify sensor coverage and recover from safe configuration drift.
- Reconcile owned assets and software versions against advisory evidence, distinguish actual affectedness from scanning and severity labels, prioritize active exposure, verify patch or containment effects, and maintain reviewable owner decisions and exceptions.
- Engineer system-level security architectures with independently verifiable protection requirements, accountable control allocation, failure-safe inter-component trust and source-backed assurance evidence.
- Track sensitive and personal data across primary, derived, logged, exported and backed-up copies; enforce purpose and recipient limits, verify logical deletion and restore-safe restrictions, and assess de-identification and residual privacy harms.
- Use established cryptographic primitives and protocols correctly, including executed authenticated record protection and a real two-party vetted-library key agreement, and reason about peer-key trust, nonces, key lifecycle and failure behavior.
- Design useful security telemetry, investigate controlled incidents, and perform evidence-based remediation.
- Conduct scoped and authorized security assessments and communicate findings in a developer-actionable form.
- Build and defend an independently reproducible security assessment and corrective risk decision for a bounded real or controlled system.

## Program completion standard

Graduation requires two separate, independently reviewable decisions: verified assessed completion of every required core course from SEC1 through SEC8, SEC10, SEC11, SEC12, SEC13 and SEC14 before admission to SEC9, and satisfactory evaluation of all published SEC9 outcomes, summative assessments, cumulative project evidence and individual technical defense. A completed capstone does not replace missing prerequisite mastery, and predecessor completion does not replace the capstone.

## Courses

| Course | Title | Duration | Prerequisites | Type |
| --- | --- | --- | --- | --- |
| [SEC1](SEC1.md) | Security Foundations & Threat Modeling | 7–10 weeks | SEF10 | `course` |
| [SEC2](SEC2.md) | Web & Application Security | 12–16 weeks | SEC1, APP1 | `course` |
| [SEC3](SEC3.md) | Systems & Binary Security | 10–14 weeks | SEC1 | `course` |
| [SEC4](SEC4.md) | Network & Infrastructure Security | 12–16 weeks | SEC2 | `course` |
| [SEC5](SEC5.md) | Applied Cryptography & Secure Protocols | 12–16 weeks | SEC1 | `course` |
| [SEC6](SEC6.md) | Cloud, Containers & Identity Security | 16–20 weeks | SEC4 | `course` |
| [SEC7](SEC7.md) | Detection, Incident Response & Threat Hunting | 12–16 weeks | SEC6 | `course` |
| [SEC8](SEC8.md) | AI Security & Authorized Red Teaming | 12–16 weeks | SEC7 | `course` |
| [SEC10](SEC10.md) | Enterprise Identity & Access Security | 14–18 weeks | SEC4 | `course` |
| [SEC11](SEC11.md) | Endpoint & Platform Defense | 14–18 weeks | SEC7, SEC10 | `course` |
| [SEC12](SEC12.md) | Vulnerability & Exposure Management | 12–16 weeks | SEC11 | `course` |
| [SEC13](SEC13.md) | Security Architecture & Control Assurance | 14–18 weeks | SEC6, SEC10 | `course` |
| [SEC14](SEC14.md) | Data Security & Privacy Engineering | 14–18 weeks | SEC5, SEC13 | `course` |
| [SEC9](SEC9.md) | Security Engineering Capstone | 14–18 weeks | SEC1–SEC8, SEC10, SEC11, SEC12, SEC13, SEC14 | `project` |

Catalog prerequisites are **direct** course-entry requirements. Prerequisites already established by an earlier required course still apply through that dependency path; omitting a redundant direct link does not waive its assessed mastery. The SEC9 admission gate separately verifies every required core course.

Course definitions specify the required outcomes, learning sequence and completion evidence. Work can be completed in [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment. The [OEE specification](../../spec/README.md) governs course requirements.
