# Security Engineering Practice Guide

Security practice is permitted only on intentionally vulnerable local programs, named training-platform labs, or systems for which you hold explicit written authorization. Do not scan public addresses, use real credentials, publish exploit payloads, or run destructive tests. Keep a scope statement with every activity.

## D1 — Security Foundations and Threat Modeling

### Labs

1. **Rules of engagement.** Write scope, asset list, allowed actions, prohibited actions, data handling, stop conditions, escalation contact, and evidence-retention policy for an F1, S10, or AI10 artifact you control.
2. **Threat model to test.** Create a data-flow diagram, trust boundaries, STRIDE threats, abuse cases, prioritization rationale, and verification tests for the highest risks.

### Exercises

1. label assets, actors, entry points, and trust boundaries in three diagrams;
2. map one scenario to each STRIDE category;
3. turn five threats into security requirements and tests;
4. compare risk severity with likelihood/impact assumptions; and
5. review a threat model for missing authorization or data boundaries.

**Ready when:** scope is legally clear and at least one threat has a verified control.

## D2 — Memory Corruption and Binary Exploitation

### Labs

1. **Sandboxed vulnerability/mitigation pair.** In a private local C program or named training lab, document one memory-safety bug, its observable harmless failure, compiler/runtime mitigations, safe repair, and regression test. Do not retain or publish weaponized payloads.
2. **C-to-Rust safety comparison.** Rebuild the same bounded behavior in safe Rust where appropriate; identify what is prevented, what still needs validation, and what cannot be concluded.

### Exercises

1. explain stack/heap layout and lifetime for supplied code;
2. classify bounds, use-after-free, double-free, and null-pointer cases;
3. map ASLR, NX/DEP, and canaries to the class of protection they provide;
4. write secure input-length/ownership checks; and
5. complete only assigned pwn.college-style sandbox lessons and record mitigation learning, not attack steps.

**Ready when:** every finding is tied to a local/authorized target, root cause, mitigation, and regression test.

## D3 — Network and Web Application Security

### Labs

1. **Local insecure-demo repair.** Build or use a local intentionally insecure demo under your control. Repair at least five representative classes of weaknesses, add regression tests, and write a developer-focused review report.
2. **Authorized academy practice.** Complete representative PortSwigger-style training labs within the platform. Record category, impact, defence, and lesson; do not copy attack payloads into this repository.

### Exercises

1. trace server-side authorization versus client-side display checks;
2. design input validation and output encoding boundaries;
3. define secure session/cookie/logout behaviors;
4. reason about rate limits, audit logs, and error messages; and
5. map each repaired flaw to a test that fails before and passes after the fix.

**Ready when:** vulnerable behaviour and verified fixes are demonstrated only in the controlled environment.

## D4 — Systems and Infrastructure Penetration Testing

### Labs

1. **Authorized assessment.** Assess only your S11 store or a named isolated training network under a D1 rules-of-engagement document. Maintain a timeline, minimal harmless evidence, severity rationale, and stop conditions.
2. **Remediation/retest.** Turn findings into developer tasks, fix the agreed highest-priority items, retest only those paths, and record remaining risk.

### Exercises

1. create an asset and attack-surface inventory from a supplied architecture;
2. write evidence handling and severity rationale for hypothetical findings;
3. distinguish discovery, validation, and exploitation in an authorized workflow;
4. draft a developer-actionable finding without reproduction payloads; and
5. define retest success/failure criteria.

**Ready when:** the report is scoped, reproducible, non-destructive, and useful to the system owner.

## D5 — Applied Cryptography and Secure Systems Design

### Labs

1. **Vetted-library protocol.** Build a small local protocol with an established cryptographic library. Document threat model, key/nonce lifecycle, associated data, errors, test vectors/format compatibility, and no-secret logging policy.
2. **Misuse resistance study.** Use safe test fixtures to demonstrate rejected invalid inputs, nonce/key misuse prevention where the library offers it, authentication failure, and version/format handling. Do not implement primitives.

### Exercises

1. choose primitives/parameters for stated requirements and justify each;
2. distinguish encryption, MAC, hash, signature, KDF, and AEAD;
3. explain why ECB, nonce reuse, unauthenticated encryption, and home-grown crypto fail;
4. model replay/downgrade/key-compromise cases; and
5. review a protocol transcript for missing authentication or context binding.

**Ready when:** implementation uses established APIs only and its security claims are bounded by the threat model.

## D6 — AI Security and Red Teaming

### Labs

1. **Controlled AI red-team suite.** Test only AI9/AI10 or a local demo for retrieval isolation, authority boundaries, rate limits, dangerous-output handling, logging, escalation, and safe denial. Use benign local test prompts/corpora.
2. **Layered remediation/retest.** Correct an identified weakness with at least two complementary controls, add regression tests, and report residual risk rather than claiming complete safety.

### Exercises

1. identify data, tool, model, user, and system trust boundaries;
2. turn prompt-injection, retrieval, and tool-abuse scenarios into harmless test cases;
3. define an agent permission model and human-stop condition;
4. assess logging/privacy trade-offs; and
5. update the AI system card and incident path after a finding.

**Ready when:** a benign in-scope attack path is documented with failed controls, layered fixes, and retest evidence.
