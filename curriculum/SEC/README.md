# Program 5 — SEC: Security Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · Previous: [AI](../AI/README.md)

## Overview

Security Engineering teaches learners to investigate and improve the security of software and the systems that run it. The sequence begins with threat modeling and application security, then develops native-code investigation, network controls, cryptography, cloud workload security and incident response. Later courses cover enterprise identity, endpoint defense, vulnerability management, security architecture and data privacy.

Work is performed on owned or explicitly authorized systems and controlled training fixtures. Learners execute checks and repairs in free local environments where possible. For controls that require unavailable infrastructure, they analyze identified reference evidence and state what they could not execute. A written policy or a passing scan is never enough to establish that a control worked.

## Prerequisites

[SEF10](../SEF/SEF10.md) is required for SEC1. [SEC2](SEC2.md) also requires [APP1](../APP/APP1.md) for web and Internet fundamentals. The catalog lists each course's direct prerequisites; earlier required preparation is inherited through the course sequence.

## Learning outcomes

Graduates can:

- Identify assets and trust boundaries, develop realistic abuse cases, and turn risk decisions into testable security requirements.
- Reproduce and repair web and API vulnerabilities, including authorization changes during long-lived WebSocket connections and confidential server-push events. Verify permitted and prohibited outcomes after the fix.
- Investigate native memory and binary weaknesses using bounded coverage-guided testing, diagnostic evidence and secure repair. Explain what a crash or runtime mitigation can and cannot prove.
- Assess reachable services, network policies, DNSSEC and DNS protective policy, TLS trust and host permissions. Verify intended access and failures with safe tests.
- Use established cryptographic libraries for authenticated records, signatures, password protection, KDFs and a real two-party vetted-library key agreement. Verify expected peer identity, context binding, key lifecycle and rejection behavior.
- Test container runtime boundaries, cloud workload identity, delivery and artifact provenance, and Kubernetes orchestration RBAC, admission and pod-network policy. Distinguish an executed control from a source-attributed policy or trace.
- Evaluate enterprise authentication, federation, privileged access, account provisioning, permission changes and effective session or entitlement revocation.
- Review Linux endpoint privileges and execution controls and interpret authentic Windows policy and event evidence. Check sensor coverage, configuration changes and recovery without claiming enforcement that was not tested.
- Maintain an accurate asset and software exposure record, resolve advisory affectedness, prioritize vulnerability treatment and verify patch or containment effects. Record owners, exceptions and unresolved risk.
- Design multi-component protection requirements, assign controls to their actual authority points, and support security architecture decisions with independent failure and protected-state evidence.
- Track personal and sensitive data through primary storage, derived copies, logs, exports and backups. Apply purpose and recipient controls, test deletion and restore restrictions, and qualify privacy and reidentification claims.
- Implement and test useful security telemetry, investigate evidence from authorized incidents, and verify proportionate containment and recovery.
- Perform authorized security assessments with clear scope and stop conditions, then provide findings that developers and accountable owners can act on.
- Complete an independently reproducible security assessment of an actual interacting cross-boundary control path, including a material correction or justified restriction, tested detection and recovery, an accountable risk decision and an individual technical defense.

## Program completion standard

Graduation has two independently reviewable decisions. The first requires verified assessed completion of every required core course from SEC1 through SEC8, SEC10, SEC11, SEC12, SEC13 and SEC14 before admission to SEC9. Each course decision must identify its revision and inspectable evidence.

The second decision assesses all SEC9 outcomes and summative requirements through one cumulative project and an individual technical defense. A completed capstone does not replace missing prerequisite mastery. Completing the prerequisite courses does not replace the capstone.

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

The catalog records direct prerequisites. Earlier required courses remain part of the preparation inherited through those links. SEC9 independently checks the completion evidence for every core predecessor.

Each course file publishes its learning outcomes, instructional sequence and required assessment evidence. Learners can organize their work in [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or an environment they control. The [OEE specification](../../spec/README.md) defines the shared completion requirements.
