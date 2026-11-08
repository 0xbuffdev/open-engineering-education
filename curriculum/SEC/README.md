> Part of the [Zero to Software Engineer](../00-overview.md) curriculum · Program 5 of 5 · [Resource library](../resources/README.md) · [Shared standards](../shared/electives-assessment-graduation.md) · Previous: [AI](04-AI-ai-engineering.md)

# PROGRAM 5 — SEC
# Security Engineering

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

---

---

## SEC resource index

*Generated from the master library: 49 resources are used in this program. "Also used in" shows reuse by other programs. Full details: [books](../resources/books.md) · [online](../resources/online.md) · [matrix](../resources/matrix.md) · [glossary](../resources/glossary.md).*

> Access markers: 📚 local library · 🌐 free online/download · 🛒 obtain (borrow or buy) · 🔐 account, isolated lab or GPU needed.

### Books

| Code | Resource | Access | Courses in this program | Also used in |
|---|---|---|---|---|
| B2 | *The C Programming Language*, 2nd ed. — Kernighan & Ritchie | 📚 | SEC3 | SEF, SYS |
| B4 | *Operating Systems: Three Easy Pieces* — Arpaci-Dusseau & Arpaci-Dusseau | 📚 | SEC3 | SEF, SYS |
| B5 | *The Linux Programming Interface* — Michael Kerrisk | 📚 | SEC1, SEC2, SEC3, SEC4, SEC6 | SEF, APP, SYS |
| B14 | *Computer Systems: A Programmer's Perspective*, 3rd ed. (CS:APP) — Bryant & O'Hallaron (Pearson, 2015) | 🛒 | SEC3 | SEF, SYS |
| B15 | *The Rust Programming Language* (2024 edition) — Klabnik, Nichols & Krycho | 🌐 | SEC3 | SEF, SYS |
| B19 | *Computer Networking: A Top-Down Approach*, 8th ed. — Kurose & Ross (Pearson, 2020); the 9th ed. (2026) moves Socket Programming to §2.6 | 🛒 | SEC4 | APP, SYS |
| B20 | *High Performance Browser Networking* — Ilya Grigorik (O'Reilly, 2013) | 🌐 | SEC4 | APP |
| B26 | *Site Reliability Engineering* — Beyer, Jones, Petoff & Murphy (O'Reilly, 2016) | 🌐 | SEC7 | APP, SYS, AI |
| B38 | *AI Engineering* — Chip Huyen (O'Reilly, 2025) | 🛒 | SEC8 | AI |
| B40 | *Threat Modeling: Designing for Security* — Adam Shostack (Wiley, 2014) | 🛒 | SEC1, SEC9 | — |
| B41 | *Security Engineering*, 3rd ed. — Ross Anderson (Wiley, 2020) | 🛒 · 🌐 chapters online | SEC1, SEC4 | — |
| B42 | *Serious Cryptography*, 2nd ed. — Jean-Philippe Aumasson (No Starch, 2024) | 🛒 | SEC5 | — |
| B43 | *Building Secure and Reliable Systems* — Adkins et al. (O'Reilly / Google, 2020) | 🌐 | SEC6, SEC7, SEC9 | SYS |
| B44 | *Container Security*, 2nd ed. — Liz Rice (O'Reilly); the 2020 first edition numbers chapters differently | 🛒 | SEC6 | — |

### Online resources, standards and papers

| Code | Resource | Access | Courses in this program | Also used in |
|---|---|---|---|---|
| R14 | OWASP Cheat Sheet Series (cheatsheetseries.owasp.org) | 🌐 | SEC1, SEC2, SEC4, SEC6, SEC7, SEC9 | APP |
| R22 | Mozilla Server-Side TLS guidelines and Let's Encrypt documentation | 🌐 | SEC4 | APP |
| R28 | OWASP Application Security Verification Standard (ASVS) 5.0 (owasp.org/www-project-application-security-verification-standard) | 🌐 | SEC1, SEC2, SEC9 | APP |
| R29 | OWASP Web Security Testing Guide (WSTG) (owasp.org/www-project-web-security-testing-guide) | 🌐 | SEC2, SEC9 | — |
| R30 | OWASP API Security Top 10 (2023) (owasp.org/API-Security) | 🌐 | SEC2 | APP |
| R31 | OWASP Top 10:2025 (owasp.org/Top10/2025) | 🌐 | SEC1, SEC2, SEC4, SEC6, SEC7 | APP |
| R32 | PortSwigger Web Security Academy (portswigger.net/web-security) | 🌐 · 🔐 account | SEC2 | — |
| R36 | The Rustonomicon (doc.rust-lang.org/nomicon) | 🌐 | SEC3 | SYS |
| R59 | “Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection” — Greshake et al. (2023) (arxiv.org/abs/2302.12173) | 🌐 | SEC8 | AI |
| R60 | OWASP Top 10 for LLM Applications 2025 (genai.owasp.org/llm-top-10) | 🌐 | SEC8 | AI |
| R61 | OWASP Top 10 for Agentic Applications (genai.owasp.org) | 🌐 | SEC8 | — |
| R62 | NIST AI 100-2 E2025 — Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (csrc.nist.gov) | 🌐 | SEC8 | — |
| R63 | MITRE ATLAS (atlas.mitre.org) | 🌐 | SEC8 | — |
| R64 | pwn.college (pwn.college) | 🌐 · 🔐 isolated lab | SEC3 | — |
| R65 | “SoK: Eternal War in Memory” — Szekeres et al. (IEEE S&P 2013) | 🌐 | SEC3 | — |
| R66 | *Nmap Network Scanning* — Gordon “Fyodor” Lyon (nmap.org/book) | 🌐 | SEC4 | — |
| R67 | CIS Benchmarks (cisecurity.org/cis-benchmarks) | 🌐 · 🔐 free account | SEC4, SEC6 | — |
| R68 | NIST SP 800-123 — Guide to General Server Security (csrc.nist.gov) | 🌐 | SEC4 | — |
| R69 | NIST SP 800-92 — Guide to Computer Security Log Management (csrc.nist.gov) | 🌐 | SEC4, SEC7 | — |
| R70 | NIST SP 800-52 Rev. 2 — Guidelines for TLS Implementations (csrc.nist.gov) | 🌐 | SEC4 | — |
| R71 | NIST SP 800-57 Part 1 Rev. 5 — Recommendation for Key Management (csrc.nist.gov) | 🌐 | SEC5 | — |
| R72 | NIST SP 800-190 — Application Container Security Guide (csrc.nist.gov) | 🌐 | SEC6 | — |
| R73 | NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management (csrc.nist.gov) | 🌐 | SEC7 | — |
| R74 | NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response (csrc.nist.gov) | 🌐 | SEC7 | — |
| R75 | NIST SP 800-115 — Technical Guide to Information Security Testing and Assessment (csrc.nist.gov) | 🌐 | SEC8, SEC9 | — |
| R76 | libsodium documentation (doc.libsodium.org) | 🌐 | SEC5 | — |
| R77 | SLSA specification (slsa.dev) | 🌐 | SEC6 | — |
| R78 | OWASP Top 10 CI/CD Security Risks (owasp.org/www-project-top-10-ci-cd-security-risks) | 🌐 | SEC6 | — |
| R79 | AWS IAM documentation — security best practices and policy evaluation logic (docs.aws.amazon.com/IAM) | 🌐 · 🔐 account optional | SEC6 | — |
| R80 | MITRE ATT&CK (attack.mitre.org) | 🌐 | SEC7, SEC9 | — |
| R81 | Sigma detection-rule specification (sigmahq.io) | 🌐 | SEC7 | — |
| R82 | PTES — Penetration Testing Execution Standard (pentest-standard.org) | 🌐 | SEC9 | — |
| R83 | FIRST CVSS v4.0 specification (first.org/cvss) | 🌐 | SEC9 | — |
| R84 | OWASP Juice Shop (owasp.org/www-project-juice-shop) | 🌐 · 🔐 isolated lab | SEC2 | — |
| R85 | TryHackMe / Hack The Box (authorized labs) | 🌐 · 🔐 account | SEC4 | — |

---

